# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SysMsg.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='SysMsg.proto',
  package='',
  serialized_pb='\n\x0cSysMsg.proto\"\x8f\x01\n\rReqSubmitInfo\x12\x0f\n\x04pbid\x18\x01 \x01(\x05:\x01\x32\x12\'\n\x04type\x18\x02 \x02(\x0e\x32\x19.ReqSubmitInfo.SubmitType\x12\x13\n\x0b\x65rr_content\x18\x03 \x02(\t\"/\n\nSubmitType\x12\x08\n\x04INFO\x10\x00\x12\x07\n\x03\x45RR\x10\x01\x12\x0e\n\nSTATISTICS\x10\x02\"\x1d\n\x08ReqHeart\x12\x11\n\theart_num\x18\x01 \x02(\x05*\x1f\n\x08SysMsgID\x12\x13\n\x0fREQ_SUBMIT_INFO\x10\n')

_SYSMSGID = _descriptor.EnumDescriptor(
  name='SysMsgID',
  full_name='SysMsgID',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQ_SUBMIT_INFO', index=0, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=193,
  serialized_end=224,
)

SysMsgID = enum_type_wrapper.EnumTypeWrapper(_SYSMSGID)
REQ_SUBMIT_INFO = 10


_REQSUBMITINFO_SUBMITTYPE = _descriptor.EnumDescriptor(
  name='SubmitType',
  full_name='ReqSubmitInfo.SubmitType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INFO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATISTICS', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=113,
  serialized_end=160,
)


_REQSUBMITINFO = _descriptor.Descriptor(
  name='ReqSubmitInfo',
  full_name='ReqSubmitInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pbid', full_name='ReqSubmitInfo.pbid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='ReqSubmitInfo.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='err_content', full_name='ReqSubmitInfo.err_content', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQSUBMITINFO_SUBMITTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=17,
  serialized_end=160,
)


_REQHEART = _descriptor.Descriptor(
  name='ReqHeart',
  full_name='ReqHeart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heart_num', full_name='ReqHeart.heart_num', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  serialized_start=162,
  serialized_end=191,
)

_REQSUBMITINFO.fields_by_name['type'].enum_type = _REQSUBMITINFO_SUBMITTYPE
_REQSUBMITINFO_SUBMITTYPE.containing_type = _REQSUBMITINFO;
DESCRIPTOR.message_types_by_name['ReqSubmitInfo'] = _REQSUBMITINFO
DESCRIPTOR.message_types_by_name['ReqHeart'] = _REQHEART

class ReqSubmitInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQSUBMITINFO

  # @@protoc_insertion_point(class_scope:ReqSubmitInfo)

class ReqHeart(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQHEART

  # @@protoc_insertion_point(class_scope:ReqHeart)


# @@protoc_insertion_point(module_scope)
