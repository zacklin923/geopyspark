# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: keyMessages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='keyMessages.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x11keyMessages.proto\x12\x06protos\"+\n\x0fProtoSpatialKey\x12\x0b\n\x03\x63ol\x18\x01 \x01(\x05\x12\x0b\n\x03row\x18\x02 \x01(\x05\">\n\x11ProtoSpaceTimeKey\x12\x0b\n\x03\x63ol\x18\x01 \x01(\x05\x12\x0b\n\x03row\x18\x02 \x01(\x05\x12\x0f\n\x07instant\x18\x03 \x01(\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROTOSPATIALKEY = _descriptor.Descriptor(
  name='ProtoSpatialKey',
  full_name='protos.ProtoSpatialKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='col', full_name='protos.ProtoSpatialKey.col', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='protos.ProtoSpatialKey.row', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=72,
)


_PROTOSPACETIMEKEY = _descriptor.Descriptor(
  name='ProtoSpaceTimeKey',
  full_name='protos.ProtoSpaceTimeKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='col', full_name='protos.ProtoSpaceTimeKey.col', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='protos.ProtoSpaceTimeKey.row', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instant', full_name='protos.ProtoSpaceTimeKey.instant', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['ProtoSpatialKey'] = _PROTOSPATIALKEY
DESCRIPTOR.message_types_by_name['ProtoSpaceTimeKey'] = _PROTOSPACETIMEKEY

ProtoSpatialKey = _reflection.GeneratedProtocolMessageType('ProtoSpatialKey', (_message.Message,), dict(
  DESCRIPTOR = _PROTOSPATIALKEY,
  __module__ = 'keyMessages_pb2'
  # @@protoc_insertion_point(class_scope:protos.ProtoSpatialKey)
  ))
_sym_db.RegisterMessage(ProtoSpatialKey)

ProtoSpaceTimeKey = _reflection.GeneratedProtocolMessageType('ProtoSpaceTimeKey', (_message.Message,), dict(
  DESCRIPTOR = _PROTOSPACETIMEKEY,
  __module__ = 'keyMessages_pb2'
  # @@protoc_insertion_point(class_scope:protos.ProtoSpaceTimeKey)
  ))
_sym_db.RegisterMessage(ProtoSpaceTimeKey)


# @@protoc_insertion_point(module_scope)
