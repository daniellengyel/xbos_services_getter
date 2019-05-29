# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: occupancy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='occupancy.proto',
  package='occupancy_historical',
  syntax='proto3',
  serialized_options=_b('P\001'),
  serialized_pb=_b('\n\x0foccupancy.proto\x12\x14occupancy_historical\"U\n\x07Request\x12\x10\n\x08\x62uilding\x18\x01 \x01(\t\x12\x0c\n\x04zone\x18\x02 \x01(\t\x12\r\n\x05start\x18\x03 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x04 \x01(\x03\x12\x0e\n\x06window\x18\x05 \x01(\t\"1\n\x0eOccupancyPoint\x12\x0c\n\x04time\x18\x01 \x01(\x03\x12\x11\n\toccupancy\x18\x02 \x01(\x01\x32\x64\n\tOccupancy\x12W\n\x0cGetOccupancy\x12\x1d.occupancy_historical.Request\x1a$.occupancy_historical.OccupancyPoint\"\x00\x30\x01\x42\x02P\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='occupancy_historical.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building', full_name='occupancy_historical.Request.building', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone', full_name='occupancy_historical.Request.zone', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='occupancy_historical.Request.start', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='occupancy_historical.Request.end', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window', full_name='occupancy_historical.Request.window', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=41,
  serialized_end=126,
)


_OCCUPANCYPOINT = _descriptor.Descriptor(
  name='OccupancyPoint',
  full_name='occupancy_historical.OccupancyPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='occupancy_historical.OccupancyPoint.time', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occupancy', full_name='occupancy_historical.OccupancyPoint.occupancy', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=128,
  serialized_end=177,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['OccupancyPoint'] = _OCCUPANCYPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'occupancy_pb2'
  # @@protoc_insertion_point(class_scope:occupancy_historical.Request)
  ))
_sym_db.RegisterMessage(Request)

OccupancyPoint = _reflection.GeneratedProtocolMessageType('OccupancyPoint', (_message.Message,), dict(
  DESCRIPTOR = _OCCUPANCYPOINT,
  __module__ = 'occupancy_pb2'
  # @@protoc_insertion_point(class_scope:occupancy_historical.OccupancyPoint)
  ))
_sym_db.RegisterMessage(OccupancyPoint)


DESCRIPTOR._options = None

_OCCUPANCY = _descriptor.ServiceDescriptor(
  name='Occupancy',
  full_name='occupancy_historical.Occupancy',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=179,
  serialized_end=279,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOccupancy',
    full_name='occupancy_historical.Occupancy.GetOccupancy',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_OCCUPANCYPOINT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_OCCUPANCY)

DESCRIPTOR.services_by_name['Occupancy'] = _OCCUPANCY

# @@protoc_insertion_point(module_scope)
