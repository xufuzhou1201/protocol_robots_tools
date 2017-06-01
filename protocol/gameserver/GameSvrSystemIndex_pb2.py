# Generated by the pb_protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='gameserver.pb_protocol/GameSvrSystemIndex.proto',
  package='protocal.game',
  serialized_pb='\n,gameserver.pb_protocol/GameSvrSystemIndex.proto\x12\rprotocal.game*J\n\nSystemType\x12\x10\n\x0cSERVER_ERROR\x10\x01\x12\x15\n\x11GAMESVR_HEARTBEAT\x10\x02\x12\x08\n\x04ROLE\x10\x03\x12\t\n\x05STAGE\x10\x04')

_SYSTEMTYPE = descriptor.EnumDescriptor(
  name='SystemType',
  full_name='protocal.game.SystemType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='SERVER_ERROR', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GAMESVR_HEARTBEAT', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROLE', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STAGE', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=63,
  serialized_end=137,
)


SERVER_ERROR = 1
GAMESVR_HEARTBEAT = 2
ROLE = 3
STAGE = 4



# @@protoc_insertion_point(module_scope)