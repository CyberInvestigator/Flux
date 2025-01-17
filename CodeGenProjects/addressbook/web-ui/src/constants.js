export const API_ROOT_URL = 'http://127.0.0.1:8000/addressbook';
export const API_PUBLIC_URL = 'http://127.0.0.1:3000';
export const DB_ID = '_id';
export const SCHEMA_DEFINITIONS_XPATH = 'definitions';
export const NEW_ITEM_ID = 999999;
export const COOKIE_NAME = 'addressbook';

export const Modes = {
    EDIT_MODE: 'edit',
    READ_MODE: 'read'
}

export const Layouts = {
    TREE_LAYOUT: 'Tree',
    TABLE_LAYOUT: 'Table',
    ABBREVIATED_FILTER_LAYOUT: 'AbbreviatedFilter',
    UNSPECIFIED: 'UNSPECIFIED'
}

export const ColorTypes = {
    CRITICAL: 'error',
    ERROR: 'error',
    WARNING: 'warning',
    INFO: 'info',
    DEBUG: 'info',
    UNSPECIFIED: 'default'
}

export const Messages = {
    ERROR_GET: 'Error while fetching data',
    CREATE_SUCCESS: 'Created',
    UPDATE_SUCCESS: 'Updated'
}

export const DataTypes = {
    STRING: 'string',
    NUMBER: 'number',
    BOOLEAN: 'boolean',
    ENUM: 'enum',
    OBJECT: 'object',
    ARRAY: 'array'
}
