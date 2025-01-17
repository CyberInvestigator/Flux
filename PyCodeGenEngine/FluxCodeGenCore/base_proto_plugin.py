#!/usr/bin/env python
import os
import re
import protogen
from Flux.PyCodeGenEngine.FluxCodeGenCore.extended_protogen_plugin import ExtendedProtogenPlugin
from Flux.PyCodeGenEngine.FluxCodeGenCore.extended_protogen_options import ExtendedProtogenOptions
from FluxPythonUtils.scripts.utility_functions import file_exist, load_yaml_configurations
from typing import List, Callable, Dict
import logging
from abc import ABC


class BaseProtoPlugin(ABC):
    """
    Plugin base script to be inherited from plugin scripts (for example: db binding plugin)
    Uses template file to add content and insertion points in output and adds content provided
    by derived class at insertion points. Derived implementation needs to set data member lists
    `insertion_point_key_list` and `insertion_point_key_to_callable_list` which are used in
    method `__process` to set `insertion_points_to_content_dict` which is assigned to
    `insertion_points_to_content_dict` data member of ``ExtendedProtogenPlugin``.

    Attributes:
    -----------
    base_dir_path: str
        path of directory containing derived plugin implementation
    config_file_path: str
        path of yaml config file
    config_yaml:
        Dictionary converted from content inside yaml config file
    template_file_path: str
        path of template file to be used to generate output file
    output_file_name: str
        name of output file to be generated
    main_proto_msg_class_name: str
        name of proto main message class from proto schema, gets assigned at run-time
    insertion_point_key_to_callable_list: List[Callable]
        List of respective insertion point's handler methods to be assigned by derived class
    insertion_points_to_content_dict: Dict[str, str]
        Dictionary containing insertion point keys with respective contents as value. Gets
        assigned by `__process` method at run-time
    """
    flux_msg_cmnt_option_key = "FluxMsgCmnt"
    flux_fld_cmnt_option_key = "FluxFldCmnt"
    flux_file_cmnt_option_key = "FluxFileCmnt"

    # This class member is used to add content in output file if no template file is provided for output
    # This insertion point is added in output file while creating output file and this insertion point
    # is used to add whole generated content in output file
    default_output_insertion_key = "create_output"

    def __init__(self, base_dir_path: str, config_path: str | None = None):
        self.base_dir_path: str = base_dir_path
        if config_path is None:
            # Setting default config path
            self.config_path: str = os.path.join(base_dir_path, "misc", "configurations.yaml")
        else:
            self.config_path: str = config_path
        self.config_yaml = load_yaml_configurations(self.config_path)

        # self.insertion_point_key_list needs to be overriden if any template file is provided in
        # derived class. It must then contain insertion points according to that template file
        self.insertion_point_key_list: List[str] = [BaseProtoPlugin.default_output_insertion_key]
        self.template_file_path: str | None = None

        # Out of Below 2 data members one needs to be overridden by derived class else exception will be risen
        self.output_file_name_suffix: str | None = None
        self.output_file_name: str | None = None

        # self.insertion_point_key_to_callable_list needs to be overriden to handle both cases:
        # 1. When self.insertion_point_key_list and self.template_file_path are not overriden (which signifies
        #    no template file is required for derived plugin) then derived class must have caller of single method
        #    that returns whole plugin generated content that could be added in generated output file
        # 2. When template file is required to generate output then self.insertion_point_key_list needs to be
        #    overridden in derived plugin to hold insertion point of template file and template_file_path
        #    should be provided. In this case self.insertion_point_key_to_callable_list needs to hold callers
        #    of handler methods of respective insertion point in self.insertion_point_key_list
        self.insertion_point_key_to_callable_list: List[Callable] = []

        # Below data member will override on the run time
        self.insertion_points_to_content_dict: Dict[str, str] | Dict[str, Dict[str, str]] = {}

    @staticmethod
    def find_acronyms_in_string(data: str) -> List[str]:
        return re.findall(r"[A-Z]{2,}", data)

    @staticmethod
    def convert_camel_case_to_specific_case(data: str, char_to_be_added: str = '_', lower_case: bool = True):
        """
        Converts Camel cased vale to specific case. For Example snake case
        Parameters:
        -----------
            data: [str] Camel cased value to be converted
            char_to_be_added: [str]: Default: '_'
                character to be added between words to replace camel
                case to specific case like snake_case using '_' between words
            lower_case: [bool] make return as lower_value if True else ignore
        """

        if acronyms_list:=BaseProtoPlugin.find_acronyms_in_string(data):
            for acronym in acronyms_list:
                if data.startswith(acronym):
                    data = data.replace(acronym, acronym[:-1].lower()+acronym[-1])
                elif data.endswith(acronym):
                    data = data.replace(acronym, "_"+acronym.lower())
                else:
                    data = data.replace(acronym, "_"+acronym[:-1].lower()+acronym[-1])
        # else not required: If data doesn't contain acronym then ignore

        if lower_case:
            return re.sub(r'(?<!^)(?=[A-Z])', char_to_be_added, data).lower()
        else:
            return re.sub(r'(?<!^)(?=[A-Z])', char_to_be_added, data)

    def convert_to_camel_case(self, value: str) -> str:
        if value != value.lower() and value != value.upper() and "_" not in value:
            if value[0].isupper():
                return BaseProtoPlugin.capitalized_to_camel_case(value)
            else:
                return value
        else:
            return BaseProtoPlugin.non_capitalized_to_camel_case(value)

    @staticmethod
    def capitalized_to_camel_case(value: str) -> str:
        if acronyms_list := BaseProtoPlugin.find_acronyms_in_string(value):
            for acronym in acronyms_list:
                if value.startswith(acronym):
                    return value.replace(acronym, acronym[:-1].lower()+acronym[-1])
        # else not required: If data doesn't contain acronym then ignore

        return "".join([value[0].lower(), value[1:]])

    @staticmethod
    def non_capitalized_to_camel_case(value: str) -> str:
        value = re.sub(r"(_|-)+", " ", value).title().replace(" ", "")
        return "".join([value[0].lower(), value[1:]])

    def insertion_points_and_resp_methods_checker(self):
        """
        Checks if number of insertion points in insertion_point_key_list is equal to number of handler
        methods in insertion_point_key_to_callable_list
        """
        if len(self.insertion_point_key_list) != len(self.insertion_point_key_to_callable_list):
            err_str = f"Mismatch found in Length of insertion points and respective implemented methods " \
                      f"Length of insertion keys: {len(self.insertion_point_key_list)} vs " \
                      f"Length of respective callables {len(self.insertion_point_key_to_callable_list)}"
            logging.exception(err_str)
            raise Exception(err_str)
        # else not required: if mismatch not found then ignore

    def required_overrides_checker(self):
        """
        Checks if required data members got overriden by derived class or not
        """
        if self.output_file_name_suffix is None and self.output_file_name is None:
            err_str = "At-least one of output_file_name_suffix and output_file_name data members needs to " \
                      "overriden by derived class"
            logging.exception(err_str)
            raise Exception(err_str)
        # else not required: if condition fails then no need to raise exception

        if not self.insertion_point_key_to_callable_list:
            err_str = "At-least one caller needs to be inside self.insertion_point_key_to_callable_list to handle " \
                      "default insertion point"
            logging.exception(err_str)
            raise Exception(err_str)
        # else not required: if condition fails then no need to raise exception

    @staticmethod
    def get_non_repeated_valued_custom_option_value(option_obj, option_name: str):
        options_list = [option for option in str(option_obj).split("\n") if ":" in option]
        for option in options_list:
            if option_name in option:
                option_content = ":".join(str(option).split(":")[1:])
                return option_content.strip()
            # else not required: Avoiding if option_name not in option_obj

    @staticmethod
    def __get_complex_option_value_as_list_of_tuple(option_string: str, option_name: str):
        option_value_list_of_tuples = []
        for option_str_line in str(option_string).split("\n"):
            temp_list = []
            if option_name in str(option_str_line):
                option_str_line_index = option_string.index(option_str_line)
                sliced_message_option_str = option_string[option_str_line_index:]
                option_string = option_string[option_str_line_index + 1:]
                for sliced_option_str_line in sliced_message_option_str.split("\n"):
                    if ":" in sliced_option_str_line:
                        if '"' in sliced_option_str_line.split(":")[1]:
                            # For string value: removing extra quotation marks
                            temp_list.append(str(sliced_option_str_line.split(":")[1][2:-1]))
                        else:
                            if ' true' == sliced_option_str_line.split(":")[1] or ' false' == \
                                    sliced_option_str_line.split(":")[1]:
                                temp_list.append(True if sliced_option_str_line.split(":")[1] == ' true' else False)
                            else:
                                # For int value
                                temp_list.append(int(sliced_option_str_line.split(":")[1]))
                    elif "}" in sliced_option_str_line:
                        option_value_list_of_tuples.append(tuple(temp_list))
                        break
            # else not required: option_name not in option_string line, then ignore
        return option_value_list_of_tuples

    @staticmethod
    def get_complex_msg_option_values_as_list_of_tuple(message: protogen.Message, option_name: str) -> List[Dict]:
        message_options_temp_str = str(message.proto.options)
        option_value_list_of_tuples = \
            BaseProtoPlugin.__get_complex_option_value_as_list_of_dict(message_options_temp_str, option_name)
        return option_value_list_of_tuples

    @staticmethod
    def get_complex_fld_option_values_as_list_of_tuple(field: protogen.Field, option_name: str) -> List[Dict]:
        fld_options_temp_str = str(field.proto.options)
        option_value_list_of_tuples = \
            BaseProtoPlugin.__get_complex_option_value_as_list_of_dict(fld_options_temp_str, option_name)
        return option_value_list_of_tuples

    # Todo: Change use of above tuple based methods by below dict based methods
    @staticmethod
    def __get_complex_option_value_as_list_of_dict(option_string: str, option_name: str) -> List[Dict]:
        option_value_list_of_dict: List[Dict] = []
        for option_str_line in str(option_string).split("\n"):
            temp_dict = {}
            if option_name in str(option_str_line):
                option_str_line_index = option_string.index(option_str_line)
                sliced_message_option_str = option_string[option_str_line_index:]
                option_string = option_string[option_str_line_index + 1:]
                for sliced_option_str_line in sliced_message_option_str.split("\n"):
                    if ":" in sliced_option_str_line:
                        if '"' in sliced_option_str_line.split(":")[1]:
                            # For string value: removing extra quotation marks
                            temp_dict[sliced_option_str_line.split(":")[0][2:]] = str(sliced_option_str_line.split(":")[1][2:-1])
                        else:
                            if ' true' == sliced_option_str_line.split(":")[1] or ' false' == \
                                    sliced_option_str_line.split(":")[1]:
                                temp_dict[sliced_option_str_line.split(":")[0][2:]] = True if sliced_option_str_line.split(":")[1] == ' true' else False
                            else:
                                # For int value
                                temp_dict[sliced_option_str_line.split(":")[0][2:]] = int(sliced_option_str_line.split(":")[1])
                    elif "}" in sliced_option_str_line:
                        option_value_list_of_dict.append(temp_dict)
                        break
            # else not required: option_name not in option_string line, then ignore
        return option_value_list_of_dict

    @staticmethod
    def get_complex_msg_option_values_as_list_of_dict(message: protogen.Message, option_name: str) -> List[Dict]:
        message_options_temp_str = str(message.proto.options)
        option_value_list_of_dict = \
            BaseProtoPlugin.__get_complex_option_value_as_list_of_dict(message_options_temp_str, option_name)
        return option_value_list_of_dict

    @staticmethod
    def get_complex_fld_option_values_as_list_of_dict(field: protogen.Field, option_name: str) -> List[Dict]:
        fld_options_temp_str = str(field.proto.options)
        option_value_list_of_dict = \
            BaseProtoPlugin.__get_complex_option_value_as_list_of_dict(fld_options_temp_str, option_name)
        return option_value_list_of_dict

    def get_flux_msg_cmt_option_value(self, message: protogen.Message) -> str:
        flux_msg_cmt_option_value = \
            BaseProtoPlugin.get_non_repeated_valued_custom_option_value(str(message.proto.options),
                                                                        BaseProtoPlugin.flux_msg_cmnt_option_key)
        return flux_msg_cmt_option_value[2:-1] \
            if flux_msg_cmt_option_value is not None else ""

    def get_flux_fld_cmt_option_value(self, field: protogen.Field) -> str:
        flux_fld_cmt_option_value = \
            BaseProtoPlugin.get_non_repeated_valued_custom_option_value(field.proto.options,
                                                                        BaseProtoPlugin.flux_fld_cmnt_option_key)
        return flux_fld_cmt_option_value[2:-1] \
            if flux_fld_cmt_option_value is not None else ""

    def get_flux_file_cmt_option_value(self, file: protogen.File) -> str:
        flux_file_cmt_option_value = \
            BaseProtoPlugin.get_non_repeated_valued_custom_option_value(file.proto.options,
                                                                        BaseProtoPlugin.flux_file_cmnt_option_key)
        return flux_file_cmt_option_value[2:-1] \
            if flux_file_cmt_option_value is not None else ""

    @staticmethod
    def import_path_from_os_path(os_path_env_var_name: str, import_file_name: str):
        project_root_dir = os.getenv("PROJECT_ROOT")  # remove projects home prefix from all import paths
        pydantic_path = os.getenv(os_path_env_var_name)
        if pydantic_path is not None and pydantic_path.startswith("/"):
            pydantic_path = pydantic_path.lstrip(project_root_dir)
        else:
            raise Exception(f"invalid absolute path: {pydantic_path}")
        return f'{".".join(pydantic_path.split(os.sep))}.{import_file_name}'

    def __handle_single_file_generation(self, plugin: ExtendedProtogenPlugin, file: protogen.File) -> None:
        # If template file is provided then using the content of it to add in generated file
        if self.template_file_path is not None:
            if file_exist(self.template_file_path):
                with open(self.template_file_path, "r") as fl:
                    file_content = fl.read()
            else:
                err_str = f"file: {self.template_file_path} does not exist"
                logging.exception(err_str)
                raise Exception(err_str)
        # else adding only one insertion point in generated file to add whole content in
        # generated file using this insertion point
        else:
            file_content = f"# @@protoc_insertion_point({BaseProtoPlugin.default_output_insertion_key})"

        if self.output_file_name:
            plugin.output_file_name = self.output_file_name
        else:
            proto_file_name = str(file.proto.name).split(os.sep)[-1]
            if self.output_file_name_suffix:
                plugin.output_file_name = f"{str(proto_file_name).split('.')[0]}_{self.output_file_name_suffix}"
            else:
                plugin.output_file_name = f"{str(proto_file_name).split('.')[0]}.py"

        generator = plugin.new_generated_file(plugin.output_file_name, file.py_import_path)

        generator.P(file_content)

    def __handle_multi_file_generation(self, plugin: ExtendedProtogenPlugin, file: protogen.File,
                                       file_name_to_content_dict: Dict[str, str]):

        for file_name, _ in file_name_to_content_dict.items():
            if self.output_file_name_suffix is None:
                err_str = "output_file_name_suffix can't be None when handling multi file generation"
                logging.exception(err_str)
                raise Exception(err_str)
            # else not required: Avoiding if output_file_name_suffix is not None

            generator = plugin.new_generated_file(file_name, file.py_import_path)
            file_content = f"# @@protoc_insertion_point({file_name})"
            generator.P(file_content)
        return file_name_to_content_dict

    def __process(self, plugin: ExtendedProtogenPlugin) -> None:
        """
        Underlying method, handles the task of creating dictionary of insertion point keys and there
        insertion content as value. This Dictionary is then assigned to `insertion_points_to_content_dict`
        data member of ``ExtendedProtogenPlugin``
        """

        # Handling mismatch in insertion points and respective implemented methods
        self.insertion_points_and_resp_methods_checker()

        # Handling any missed override in derived class
        self.required_overrides_checker()

        # @@@ May contain bug for explicit multi input files, so protoc command should
        # be used for single input file explicitly
        for file in plugin.files_to_generate:

            # Getting content to be injected in insertion points in generated file
            # 1. If template is provided then dict assigned to plugin.insertion_points_to_content_dict
            # will contain insertion points and contents to be injected to respective point as key-value pair
            # 2. If template is not provided then below 2 cases could occur:
            #    2.1 If string return type is received from insertion_point_handler_method: In this case,
            #    single file generation handling needs to be done. In this case, received dict will contain
            #    default insertion point used for output file as key and respective content as value. Generated
            #    file name will be dependent on either provided output file or provided output suffix string
            #    2.2 If Dictionary return type is received from insertion_point_handler_method: In this case,
            #    multi file generation handling needs to be done. In this case, received dict's keys will
            #    have file names to be generated that will be concatenated with suffix string provided
            #    from config (suffix must be provided from config or exception will occur).
            for insert_point, insertion_point_handler_method in zip(self.insertion_point_key_list,
                                                                    self.insertion_point_key_to_callable_list):
                self.insertion_points_to_content_dict[insert_point] = insertion_point_handler_method(file)
            plugin.insertion_points_to_content_dict = self.insertion_points_to_content_dict

            # @@@ Case - 2 from above - Now identifying between 2.1 and 2.2
            if self.template_file_path is None:

                insertion_points_to_content_dict_values: List[str | Dict[str, str]] = \
                    list(self.insertion_points_to_content_dict.values())

                # First checking if when template_file_path is not provided then length of
                # insertion_points_to_content_dict_values should not be more than 1
                # (For Reason refer to above comment paragraph)
                if len(insertion_points_to_content_dict_values) != 1:
                    err_str = f"Length of insertion point - injection content dict should be only 1 when " \
                              f"template file is not provided"
                    logging.exception(err_str)
                    raise Exception(err_str)
                # else not required: If length is 1 then ignoring

                # @@@ Case - 2.1
                if isinstance(insertion_points_to_content_dict_values[0], str):
                    self.__handle_single_file_generation(plugin, file)
                # @@@ Case - 2.2
                elif isinstance(insertion_points_to_content_dict_values[0], dict):
                    plugin.do_generate_multi_files = True
                    self.__handle_multi_file_generation(plugin, file, insertion_points_to_content_dict_values[0])

                else:
                    err_str = f"Invalid data type returned from insertion_point_handler_method: " \
                              f"{insertion_points_to_content_dict_values[0]}"
                    logging.exception(err_str)
                    raise Exception(err_str)
            # @@@ Case - 1
            else:
                self.__handle_single_file_generation(plugin, file)

    def process(self):
        extended_protogen_options = ExtendedProtogenOptions()
        extended_protogen_options.run(self.__process)
