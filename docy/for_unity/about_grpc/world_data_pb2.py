# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: world_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='world_data.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10world_data.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x14\n\x04Time\x12\x0c\n\x04step\x18\x01 \x01(\x05\"\xbf\x01\n\x07MapData\x12\x19\n\nagent_locs\x18\x01 \x03(\x0b\x32\x05.Pair\x12\x19\n\nworld_size\x18\x02 \x01(\x0b\x32\x05.Pair\x12\x1e\n\tstone_map\x18\x03 \x01(\x0b\x32\x0b.Map1DArray\x12\x1d\n\x08wood_map\x18\x04 \x01(\x0b\x32\x0b.Map1DArray\x12\x1e\n\twater_map\x18\x05 \x01(\x0b\x32\x0b.Map1DArray\x12\x1f\n\nhouse_maps\x18\x06 \x03(\x0b\x32\x0b.Map1DArray\" \n\x04Pair\x12\x0b\n\x03row\x18\x01 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x02 \x01(\x05\"\x17\n\nMap1DArray\x12\t\n\x01\x66\x18\x01 \x03(\x01\x32\x63\n\x0b\x41IEconomist\x12 \n\x0bGetWorldMap\x12\x05.Time\x1a\x08.MapData\"\x00\x12\x32\n\x0cSendWorldMap\x12\x08.MapData\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='Time.step', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=69,
)


_MAPDATA = _descriptor.Descriptor(
  name='MapData',
  full_name='MapData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_locs', full_name='MapData.agent_locs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='world_size', full_name='MapData.world_size', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stone_map', full_name='MapData.stone_map', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wood_map', full_name='MapData.wood_map', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='water_map', full_name='MapData.water_map', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='house_maps', full_name='MapData.house_maps', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=263,
)


_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='Pair.row', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='col', full_name='Pair.col', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=297,
)


_MAP1DARRAY = _descriptor.Descriptor(
  name='Map1DArray',
  full_name='Map1DArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='f', full_name='Map1DArray.f', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=322,
)

_MAPDATA.fields_by_name['agent_locs'].message_type = _PAIR
_MAPDATA.fields_by_name['world_size'].message_type = _PAIR
_MAPDATA.fields_by_name['stone_map'].message_type = _MAP1DARRAY
_MAPDATA.fields_by_name['wood_map'].message_type = _MAP1DARRAY
_MAPDATA.fields_by_name['water_map'].message_type = _MAP1DARRAY
_MAPDATA.fields_by_name['house_maps'].message_type = _MAP1DARRAY
DESCRIPTOR.message_types_by_name['Time'] = _TIME
DESCRIPTOR.message_types_by_name['MapData'] = _MAPDATA
DESCRIPTOR.message_types_by_name['Pair'] = _PAIR
DESCRIPTOR.message_types_by_name['Map1DArray'] = _MAP1DARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), {
  'DESCRIPTOR' : _TIME,
  '__module__' : 'world_data_pb2'
  # @@protoc_insertion_point(class_scope:Time)
  })
_sym_db.RegisterMessage(Time)

MapData = _reflection.GeneratedProtocolMessageType('MapData', (_message.Message,), {
  'DESCRIPTOR' : _MAPDATA,
  '__module__' : 'world_data_pb2'
  # @@protoc_insertion_point(class_scope:MapData)
  })
_sym_db.RegisterMessage(MapData)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
  'DESCRIPTOR' : _PAIR,
  '__module__' : 'world_data_pb2'
  # @@protoc_insertion_point(class_scope:Pair)
  })
_sym_db.RegisterMessage(Pair)

Map1DArray = _reflection.GeneratedProtocolMessageType('Map1DArray', (_message.Message,), {
  'DESCRIPTOR' : _MAP1DARRAY,
  '__module__' : 'world_data_pb2'
  # @@protoc_insertion_point(class_scope:Map1DArray)
  })
_sym_db.RegisterMessage(Map1DArray)



_AIECONOMIST = _descriptor.ServiceDescriptor(
  name='AIEconomist',
  full_name='AIEconomist',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=324,
  serialized_end=423,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetWorldMap',
    full_name='AIEconomist.GetWorldMap',
    index=0,
    containing_service=None,
    input_type=_TIME,
    output_type=_MAPDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendWorldMap',
    full_name='AIEconomist.SendWorldMap',
    index=1,
    containing_service=None,
    input_type=_MAPDATA,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AIECONOMIST)

DESCRIPTOR.services_by_name['AIEconomist'] = _AIECONOMIST

# @@protoc_insertion_point(module_scope)