# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strat_manager_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


import flux_options_pb2 as flux__options__pb2
import strat_core_pb2 as strat__core__pb2
import ui_core_pb2 as ui__core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bstrat_manager_service.proto\x12\x0b\x61\x64\x64ressbook\x1a\x12\x66lux_options.proto\x1a\x10strat_core.proto\x1a\rui_core.proto\"\xd1\x04\n\x0fPairStratParams\x12\x15\n\x07\x65xch_id\x18\x01 \x01(\tB\x04\xb8\xfd\x1a\x01\x12O\n\x08leg1_sec\x18\x02 \x02(\x0b\x32\x15.addressbook.SecurityB&\xf8\xf6\x1a\x01\xb2\xfd\x1a\x1esec_id:CB_List, sec_type=SEDOL\x12\x37\n\x15leg1_sec_reference_px\x18\x03 \x01(\x0b\x32\x18.addressbook.ReferencePx\x12N\n\x08leg2_sec\x18\x04 \x02(\x0b\x32\x15.addressbook.SecurityB%\xf8\xf6\x1a\x01\xb2\xfd\x1a\x1dsec_id:EQT_List, sec_type=RIC\x12\x37\n\x15leg2_sec_reference_px\x18\x05 \x01(\x0b\x32\x18.addressbook.ReferencePx\x12*\n\tleg1_side\x18\x06 \x02(\x0e\x32\x11.addressbook.SideB\x04\xf8\xf6\x1a\x01\x12-\n\x10\x65ligible_brokers\x18\x07 \x03(\x0b\x32\x13.addressbook.Broker\x12>\n\x14residual_restriction\x18\x08 \x01(\x0b\x32 .addressbook.ResidualRestriction\x12\x33\n\x19\x65xch_response_max_seconds\x18\t \x01(\x05:\x02\x33\x30\x42\x0c\x82\xfd\x18\x04True\xb8\xfd\x1a\x01\x12\"\n\x1atrigger_premium_percentage\x18\n \x02(\x02\x12\x16\n\x0bhedge_ratio\x18\x0b \x01(\x02:\x01\x31:\x08\xaa\xfd\x1a\x04Tree\"\xe7\x02\n\x0bStratStatus\x12(\n\x0cstrat_alerts\x18\x01 \x03(\x0b\x32\x12.addressbook.Alert\x12\x39\n\x0bstrat_state\x18\x02 \x02(\x0e\x32\x17.addressbook.StratState:\x0bUNSPECIFIED\x12\x17\n\x0f\x61verage_premium\x18\x03 \x01(\x02\x12@\n\x0b\x66ills_brief\x18\x04 \x03(\x0b\x32!.addressbook.CumulativeOrderBriefB\x08\x9a\xfd\x1a\x04JSON\x12\x46\n\x11open_orders_brief\x18\x05 \x03(\x0b\x32!.addressbook.CumulativeOrderBriefB\x08\x9a\xfd\x1a\x04JSON\x12\x18\n\x10\x62\x61lance_notional\x18\x06 \x01(\x02\x12\'\n\x08residual\x18\x07 \x01(\x0b\x32\x15.addressbook.Residual:\r\xaa\xfd\x1a\x05Table\xb0\xfd\x1a\x01\"\xd5\x03\n\x0bStratLimits\x12\x66\n\x0fmax_cb_notional\x18\x01 \x02(\x02\x42M\x8a\xfd\x18Iconsumption: open+executed, max eqt notional derived applying hedge ratio\x12V\n\x14max_open_cb_notional\x18\x02 \x02(\x02\x42\x38\x8a\xfd\x18\x34max open eqt notional derived applying hedge ratio ]\x12V\n\x10max_open_baskets\x18\x03 \x02(\x05\x42<\x8a\xfd\x18\x38max simultaneous open order pairs allowed for this strat\x12\x63\n\x14market_participation\x18\x04 \x01(\x0b\x32 .addressbook.MarketParticipationB#\x8a\xfd\x18\x1fserver provided, UI overridable\x12>\n\x11max_concentration\x18\x05 \x01(\x02\x42#\x8a\xfd\x18\x1fserver provided, UI overridable:\t\xaa\xfd\x1a\x05Table\"\x8d\x03\n\x0bOrderLimits\x12\x1c\n\x02id\x18\x01 \x02(\x05\x42\x10\xf8\xf6\x1a\x01\xb8\xfd\x1a\x01\x82\xfd\x18\x04True\x12\x1e\n\x10max_price_levels\x18\x02 \x02(\x05\x42\x04\xc8\xfd\x1a\x01\x12$\n\x10max_basis_points\x18\x03 \x02(\x05\x42\n\x82\xf1\x1c\x02\x31\x35\xc8\xfd\x1a\x02\x12`\n\x15max_cb_order_notional\x18\x04 \x02(\x05\x42\x41\xc8\xfd\x1a\x03\x8a\xfd\x18\x39open+executed; max ord eqt notional derived (hedge ratio)\x12;\n\x10max_px_deviation\x18\x05 \x02(\x02:\x01\x32\x42\x1e\xc8\xfd\x1a\x04\x8a\xfd\x18\x16% of Last Traded Price:{\x9a\xfd\x1an\n\x1a\x43reate Doc for OrderLimits\x12\x18Read Doc for OrderLimits\x1a\x1aUpdate Doc for OrderLimits\"\x1a\x44\x65lete Doc for OrderLimits\xaa\xfd\x1a\x05Table\"\x92\x03\n\x0fPortfolioLimits\x12\x1c\n\x02id\x18\x01 \x02(\x05\x42\x10\xf8\xf6\x1a\x01\xb8\xfd\x1a\x01\x82\xfd\x18\x04True\x12\x33\n\x10\x65ligible_brokers\x18\x02 \x03(\x0b\x32\x13.addressbook.BrokerB\x04\xc8\xfd\x1a\x03\x12j\n\x0fmax_cb_notional\x18\x03 \x02(\x02\x42Q\xc8\xfd\x1a\x01\x8a\xfd\x18Iconsumption: open+executed, max eqt notional derived applying hedge ratio\x12\x32\n\x0b\x63\x61ncel_rate\x18\x04 \x02(\x0b\x32\x17.addressbook.CancelRateB\x04\xc8\xfd\x1a\x02:\x8b\x01\x9a\xfd\x1a~\n\x1e\x43reate Doc for PortfolioLimits\x12\x1cRead Doc for PortfolioLimits\x1a\x1eUpdate Doc for PortfolioLimits\"\x1e\x44\x65lete Doc for PortfolioLimits\xaa\xfd\x1a\x05Table\"\xea\x02\n\x0fPortfolioStatus\x12\x1c\n\x02id\x18\x01 \x02(\x05\x42\x10\xf8\xf6\x1a\x01\xb8\xfd\x1a\x01\x82\xfd\x18\x04True\x12@\n\x0bkill_switch\x18\x02 \x02(\x08:\x05\x66\x61lseB$\xa8\xfd\x1a\x01\xc2\xfd\x1a\x1ctrue=ERROR,false=UNSPECIFIED\x12,\n\x10portfolio_alerts\x18\x03 \x03(\x0b\x32\x12.addressbook.Alert\x12\x1c\n\x14overall_buy_notional\x18\x04 \x01(\x02\x12\x1d\n\x15overall_sell_notional\x18\x05 \x01(\x02:\x8b\x01\x9a\xfd\x1a~\n\x1e\x43reate Doc for PortfolioStatus\x12\x1cRead Doc for PortfolioStatus\x1a\x1eUpdate Doc for PortfolioStatus\"\x1e\x44\x65lete Doc for PortfolioStatus\xaa\xfd\x1a\x05Table\"\x88\x03\n\tPairStrat\x12\x1c\n\x02id\x18\x01 \x02(\x05\x42\x10\xf8\xf6\x1a\x01\xb8\xfd\x1a\x01\x82\xfd\x18\x04True\x12\x33\n\x15last_active_date_time\x18\x02 \x01(\x03\x42\x14\x82\xfd\x18\x04True\xa0\xf1\x1c\x02\xb8\xfd\x1a\x01\xb0\xf1\x1c\x01\x12#\n\tfrequency\x18\x03 \x01(\x05\x42\x10\x82\xfd\x18\x04True\xa0\xf1\x1c\x01\xb8\xfd\x1a\x01\x12\x37\n\x11pair_strat_params\x18\x04 \x02(\x0b\x32\x1c.addressbook.PairStratParams\x12.\n\x0cstrat_status\x18\x05 \x01(\x0b\x32\x18.addressbook.StratStatus\x12.\n\x0cstrat_limits\x18\x06 \x02(\x0b\x32\x18.addressbook.StratLimits:j\x9a\xfd\x1a\x66\n\x18\x43reate Doc for PairStrat\x12\x16Read Doc for PairStrat\x1a\x18Update Doc for PairStrat\"\x18\x44\x65lete Doc for PairStrat\"\xeb\x03\n\x0fStratCollection\x12\x1c\n\x02id\x18\x01 \x02(\x05\x42\x10\xf8\xf6\x1a\x01\xb8\xfd\x1a\x01\x82\xfd\x18\x04True\x12\x82\x02\n\x11loaded_strat_keys\x18\x02 \x03(\tB\xe6\x01\x9a\xfd\x1a\x8a\x01PairStrat.pair_strat_params.leg2_sec.sec_id-PairStrat.pair_strat_params.leg1_sec.sec_id-PairStrat.pair_strat_params.leg1_side-PairStrat.id\xd2\xfd\x1a#PairStrat.strat_status.strat_alerts\xda\xfd\x1a,PairStrat.strat_status.strat_alerts.severity\x12\x1b\n\x13\x62uffered_strat_keys\x18\x03 \x03(\t:\x97\x01\x9a\xfd\x1a~\n\x1e\x43reate Doc for StratCollection\x12\x1cRead Doc for StratCollection\x1a\x1eUpdate Doc for StratCollection\"\x1e\x44\x65lete Doc for StratCollection\xaa\xfd\x1a\x11\x41\x62\x62reviatedFilter\"\xe8\x01\n\x08UILayout\x12\x1c\n\x02id\x18\x01 \x02(\x05\x42\x10\xf8\xf6\x1a\x01\xb8\xfd\x1a\x01\x82\xfd\x18\x04True\x12\x18\n\nprofile_id\x18\x02 \x02(\tB\x04\xe8\xbb\x19\x01\x12%\n\x0ewidget_ui_data\x18\x03 \x03(\x0b\x32\r.WidgetUIData\x12\x15\n\x05theme\x18\x04 \x01(\x0e\x32\x06.Theme:f\x9a\xfd\x1a\x62\n\x17\x43reate Doc for UILayout\x12\x15Read Doc for UILayout\x1a\x17Update Doc for UILayout\"\x17\x44\x65lete Doc for UILayout')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'strat_manager_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PAIRSTRATPARAMS.fields_by_name['exch_id']._options = None
  _PAIRSTRATPARAMS.fields_by_name['exch_id']._serialized_options = b'\270\375\032\001'
  _PAIRSTRATPARAMS.fields_by_name['leg1_sec']._options = None
  _PAIRSTRATPARAMS.fields_by_name['leg1_sec']._serialized_options = b'\370\366\032\001\262\375\032\036sec_id:CB_List, sec_type=SEDOL'
  _PAIRSTRATPARAMS.fields_by_name['leg2_sec']._options = None
  _PAIRSTRATPARAMS.fields_by_name['leg2_sec']._serialized_options = b'\370\366\032\001\262\375\032\035sec_id:EQT_List, sec_type=RIC'
  _PAIRSTRATPARAMS.fields_by_name['leg1_side']._options = None
  _PAIRSTRATPARAMS.fields_by_name['leg1_side']._serialized_options = b'\370\366\032\001'
  _PAIRSTRATPARAMS.fields_by_name['exch_response_max_seconds']._options = None
  _PAIRSTRATPARAMS.fields_by_name['exch_response_max_seconds']._serialized_options = b'\202\375\030\004True\270\375\032\001'
  _PAIRSTRATPARAMS._options = None
  _PAIRSTRATPARAMS._serialized_options = b'\252\375\032\004Tree'
  _STRATSTATUS.fields_by_name['fills_brief']._options = None
  _STRATSTATUS.fields_by_name['fills_brief']._serialized_options = b'\232\375\032\004JSON'
  _STRATSTATUS.fields_by_name['open_orders_brief']._options = None
  _STRATSTATUS.fields_by_name['open_orders_brief']._serialized_options = b'\232\375\032\004JSON'
  _STRATSTATUS._options = None
  _STRATSTATUS._serialized_options = b'\252\375\032\005Table\260\375\032\001'
  _STRATLIMITS.fields_by_name['max_cb_notional']._options = None
  _STRATLIMITS.fields_by_name['max_cb_notional']._serialized_options = b'\212\375\030Iconsumption: open+executed, max eqt notional derived applying hedge ratio'
  _STRATLIMITS.fields_by_name['max_open_cb_notional']._options = None
  _STRATLIMITS.fields_by_name['max_open_cb_notional']._serialized_options = b'\212\375\0304max open eqt notional derived applying hedge ratio ]'
  _STRATLIMITS.fields_by_name['max_open_baskets']._options = None
  _STRATLIMITS.fields_by_name['max_open_baskets']._serialized_options = b'\212\375\0308max simultaneous open order pairs allowed for this strat'
  _STRATLIMITS.fields_by_name['market_participation']._options = None
  _STRATLIMITS.fields_by_name['market_participation']._serialized_options = b'\212\375\030\037server provided, UI overridable'
  _STRATLIMITS.fields_by_name['max_concentration']._options = None
  _STRATLIMITS.fields_by_name['max_concentration']._serialized_options = b'\212\375\030\037server provided, UI overridable'
  _STRATLIMITS._options = None
  _STRATLIMITS._serialized_options = b'\252\375\032\005Table'
  _ORDERLIMITS.fields_by_name['id']._options = None
  _ORDERLIMITS.fields_by_name['id']._serialized_options = b'\370\366\032\001\270\375\032\001\202\375\030\004True'
  _ORDERLIMITS.fields_by_name['max_price_levels']._options = None
  _ORDERLIMITS.fields_by_name['max_price_levels']._serialized_options = b'\310\375\032\001'
  _ORDERLIMITS.fields_by_name['max_basis_points']._options = None
  _ORDERLIMITS.fields_by_name['max_basis_points']._serialized_options = b'\202\361\034\00215\310\375\032\002'
  _ORDERLIMITS.fields_by_name['max_cb_order_notional']._options = None
  _ORDERLIMITS.fields_by_name['max_cb_order_notional']._serialized_options = b'\310\375\032\003\212\375\0309open+executed; max ord eqt notional derived (hedge ratio)'
  _ORDERLIMITS.fields_by_name['max_px_deviation']._options = None
  _ORDERLIMITS.fields_by_name['max_px_deviation']._serialized_options = b'\310\375\032\004\212\375\030\026% of Last Traded Price'
  _ORDERLIMITS._options = None
  _ORDERLIMITS._serialized_options = b'\232\375\032n\n\032Create Doc for OrderLimits\022\030Read Doc for OrderLimits\032\032Update Doc for OrderLimits\"\032Delete Doc for OrderLimits\252\375\032\005Table'
  _PORTFOLIOLIMITS.fields_by_name['id']._options = None
  _PORTFOLIOLIMITS.fields_by_name['id']._serialized_options = b'\370\366\032\001\270\375\032\001\202\375\030\004True'
  _PORTFOLIOLIMITS.fields_by_name['eligible_brokers']._options = None
  _PORTFOLIOLIMITS.fields_by_name['eligible_brokers']._serialized_options = b'\310\375\032\003'
  _PORTFOLIOLIMITS.fields_by_name['max_cb_notional']._options = None
  _PORTFOLIOLIMITS.fields_by_name['max_cb_notional']._serialized_options = b'\310\375\032\001\212\375\030Iconsumption: open+executed, max eqt notional derived applying hedge ratio'
  _PORTFOLIOLIMITS.fields_by_name['cancel_rate']._options = None
  _PORTFOLIOLIMITS.fields_by_name['cancel_rate']._serialized_options = b'\310\375\032\002'
  _PORTFOLIOLIMITS._options = None
  _PORTFOLIOLIMITS._serialized_options = b'\232\375\032~\n\036Create Doc for PortfolioLimits\022\034Read Doc for PortfolioLimits\032\036Update Doc for PortfolioLimits\"\036Delete Doc for PortfolioLimits\252\375\032\005Table'
  _PORTFOLIOSTATUS.fields_by_name['id']._options = None
  _PORTFOLIOSTATUS.fields_by_name['id']._serialized_options = b'\370\366\032\001\270\375\032\001\202\375\030\004True'
  _PORTFOLIOSTATUS.fields_by_name['kill_switch']._options = None
  _PORTFOLIOSTATUS.fields_by_name['kill_switch']._serialized_options = b'\250\375\032\001\302\375\032\034true=ERROR,false=UNSPECIFIED'
  _PORTFOLIOSTATUS._options = None
  _PORTFOLIOSTATUS._serialized_options = b'\232\375\032~\n\036Create Doc for PortfolioStatus\022\034Read Doc for PortfolioStatus\032\036Update Doc for PortfolioStatus\"\036Delete Doc for PortfolioStatus\252\375\032\005Table'
  _PAIRSTRAT.fields_by_name['id']._options = None
  _PAIRSTRAT.fields_by_name['id']._serialized_options = b'\370\366\032\001\270\375\032\001\202\375\030\004True'
  _PAIRSTRAT.fields_by_name['last_active_date_time']._options = None
  _PAIRSTRAT.fields_by_name['last_active_date_time']._serialized_options = b'\202\375\030\004True\240\361\034\002\270\375\032\001\260\361\034\001'
  _PAIRSTRAT.fields_by_name['frequency']._options = None
  _PAIRSTRAT.fields_by_name['frequency']._serialized_options = b'\202\375\030\004True\240\361\034\001\270\375\032\001'
  _PAIRSTRAT._options = None
  _PAIRSTRAT._serialized_options = b'\232\375\032f\n\030Create Doc for PairStrat\022\026Read Doc for PairStrat\032\030Update Doc for PairStrat\"\030Delete Doc for PairStrat'
  _STRATCOLLECTION.fields_by_name['id']._options = None
  _STRATCOLLECTION.fields_by_name['id']._serialized_options = b'\370\366\032\001\270\375\032\001\202\375\030\004True'
  _STRATCOLLECTION.fields_by_name['loaded_strat_keys']._options = None
  _STRATCOLLECTION.fields_by_name['loaded_strat_keys']._serialized_options = b'\232\375\032\212\001PairStrat.pair_strat_params.leg2_sec.sec_id-PairStrat.pair_strat_params.leg1_sec.sec_id-PairStrat.pair_strat_params.leg1_side-PairStrat.id\322\375\032#PairStrat.strat_status.strat_alerts\332\375\032,PairStrat.strat_status.strat_alerts.severity'
  _STRATCOLLECTION._options = None
  _STRATCOLLECTION._serialized_options = b'\232\375\032~\n\036Create Doc for StratCollection\022\034Read Doc for StratCollection\032\036Update Doc for StratCollection\"\036Delete Doc for StratCollection\252\375\032\021AbbreviatedFilter'
  _UILAYOUT.fields_by_name['id']._options = None
  _UILAYOUT.fields_by_name['id']._serialized_options = b'\370\366\032\001\270\375\032\001\202\375\030\004True'
  _UILAYOUT.fields_by_name['profile_id']._options = None
  _UILAYOUT.fields_by_name['profile_id']._serialized_options = b'\350\273\031\001'
  _UILAYOUT._options = None
  _UILAYOUT._serialized_options = b'\232\375\032b\n\027Create Doc for UILayout\022\025Read Doc for UILayout\032\027Update Doc for UILayout\"\027Delete Doc for UILayout'
  _PAIRSTRATPARAMS._serialized_start=98
  _PAIRSTRATPARAMS._serialized_end=691
  _STRATSTATUS._serialized_start=694
  _STRATSTATUS._serialized_end=1053
  _STRATLIMITS._serialized_start=1056
  _STRATLIMITS._serialized_end=1525
  _ORDERLIMITS._serialized_start=1528
  _ORDERLIMITS._serialized_end=1925
  _PORTFOLIOLIMITS._serialized_start=1928
  _PORTFOLIOLIMITS._serialized_end=2330
  _PORTFOLIOSTATUS._serialized_start=2333
  _PORTFOLIOSTATUS._serialized_end=2695
  _PAIRSTRAT._serialized_start=2698
  _PAIRSTRAT._serialized_end=3090
  _STRATCOLLECTION._serialized_start=3093
  _STRATCOLLECTION._serialized_end=3584
  _UILAYOUT._serialized_start=3587
  _UILAYOUT._serialized_end=3819
