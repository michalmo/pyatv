# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/ModifyOutputContextRequestMessage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDpyatv/protocols/mrp/protobuf/ModifyOutputContextRequestMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"E\n\x1eModifyOutputContextRequestType\"#\n\x04\x45num\x12\x1b\n\x17SharedAudioPresentation\x10\x01\"\x8b\x02\n!ModifyOutputContextRequestMessage\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32$.ModifyOutputContextRequestType.Enum\x12\x15\n\raddingDevices\x18\x02 \x03(\t\x12\x17\n\x0fremovingDevices\x18\x03 \x03(\t\x12\x16\n\x0esettingDevices\x18\x04 \x03(\t\x12!\n\x19\x63lusterAwareAddingDevices\x18\x05 \x03(\t\x12#\n\x1b\x63lusterAwareRemovingDevices\x18\x06 \x03(\t\x12\"\n\x1a\x63lusterAwareSettingDevices\x18\x07 \x03(\t:_\n!modifyOutputContextRequestMessage\x12\x10.ProtocolMessage\x18\x34 \x01(\x0b\x32\".ModifyOutputContextRequestMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.ModifyOutputContextRequestMessage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(modifyOutputContextRequestMessage)

  DESCRIPTOR._options = None
  _globals['_MODIFYOUTPUTCONTEXTREQUESTTYPE']._serialized_start=124
  _globals['_MODIFYOUTPUTCONTEXTREQUESTTYPE']._serialized_end=193
  _globals['_MODIFYOUTPUTCONTEXTREQUESTTYPE_ENUM']._serialized_start=158
  _globals['_MODIFYOUTPUTCONTEXTREQUESTTYPE_ENUM']._serialized_end=193
  _globals['_MODIFYOUTPUTCONTEXTREQUESTMESSAGE']._serialized_start=196
  _globals['_MODIFYOUTPUTCONTEXTREQUESTMESSAGE']._serialized_end=463
# @@protoc_insertion_point(module_scope)
