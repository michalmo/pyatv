# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/protocols/mrp/protobuf/CommandOptions.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import Common_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_Common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1pyatv/protocols/mrp/protobuf/CommandOptions.proto\x1a)pyatv/protocols/mrp/protobuf/Common.proto\"\xe1\x06\n\x0e\x43ommandOptions\x12\x10\n\x08sourceId\x18\x02 \x01(\t\x12\x11\n\tmediaType\x18\x03 \x01(\t\x12\x1d\n\x15\x65xternalPlayerCommand\x18\x04 \x01(\x08\x12\x14\n\x0cskipInterval\x18\x05 \x01(\x02\x12\x14\n\x0cplaybackRate\x18\x06 \x01(\x02\x12\x0e\n\x06rating\x18\x07 \x01(\x02\x12\x10\n\x08negative\x18\x08 \x01(\x08\x12\x18\n\x10playbackPosition\x18\t \x01(\x01\x12$\n\nrepeatMode\x18\n \x01(\x0e\x32\x10.RepeatMode.Enum\x12&\n\x0bshuffleMode\x18\x0b \x01(\x0e\x32\x11.ShuffleMode.Enum\x12\x0f\n\x07trackID\x18\x0c \x01(\x04\x12\x16\n\x0eradioStationID\x18\r \x01(\x03\x12\x18\n\x10radioStationHash\x18\x0e \x01(\t\x12\"\n\x1asystemAppPlaybackQueueData\x18\x0f \x01(\x0c\x12\x1f\n\x17\x64\x65stinationAppDisplayID\x18\x10 \x01(\t\x12\x13\n\x0bsendOptions\x18\x11 \x01(\r\x12/\n\'requestDefermentToPlaybackQueuePosition\x18\x12 \x01(\x08\x12\x11\n\tcontextID\x18\x13 \x01(\t\x12*\n\"shouldOverrideManuallyCuratedQueue\x18\x14 \x01(\x08\x12\x12\n\nstationURL\x18\x15 \x01(\t\x12 \n\x18shouldBeginRadioPlayback\x18\x16 \x01(\x08\x12&\n\x1eplaybackQueueInsertionPosition\x18\x17 \x01(\x05\x12\x15\n\rcontentItemID\x18\x18 \x01(\t\x12\x1b\n\x13playbackQueueOffset\x18\x19 \x01(\x05\x12&\n\x1eplaybackQueueDestinationOffset\x18\x1a \x01(\x05\x12\x16\n\x0elanguageOption\x18\x1b \x01(\x0c\x12\x1c\n\x14playbackQueueContext\x18\x1c \x01(\x0c\x12 \n\x18insertAfterContentItemID\x18\x1d \x01(\t\x12\x1f\n\x17nowPlayingContentItemID\x18\x1e \x01(\t\x12\x15\n\rreplaceIntent\x18\x1f \x01(\x05')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.CommandOptions_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_COMMANDOPTIONS']._serialized_start=97
  _globals['_COMMANDOPTIONS']._serialized_end=962
# @@protoc_insertion_point(module_scope)
