# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/GetVolumeMessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3pyatv/protocols/mrp/protobuf/GetVolumeMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"+\n\x10GetVolumeMessage\x12\x17\n\x0foutputDeviceUID\x18\x01 \x01(\t:=\n\x10getVolumeMessage\x12\x10.ProtocolMessage\x18\x35 \x01(\x0b\x32\x11.GetVolumeMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.GetVolumeMessage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(getVolumeMessage)

  DESCRIPTOR._options = None
  _globals['_GETVOLUMEMESSAGE']._serialized_start=107
  _globals['_GETVOLUMEMESSAGE']._serialized_end=150
# @@protoc_insertion_point(module_scope)
