# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generate_image.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14generate_image.proto\"4\n\x05Image\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"&\n\x14GenerateImageRequest\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"?\n\x15GenerateImageResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\x05image\x18\x02 \x01(\x0b\x32\x06.Image2Q\n\x0fImageGeneration\x12>\n\rGenerateImage\x12\x15.GenerateImageRequest\x1a\x16.GenerateImageResponseB\x02P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generate_image_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'P\001'
  _globals['_IMAGE']._serialized_start=24
  _globals['_IMAGE']._serialized_end=76
  _globals['_GENERATEIMAGEREQUEST']._serialized_start=78
  _globals['_GENERATEIMAGEREQUEST']._serialized_end=116
  _globals['_GENERATEIMAGERESPONSE']._serialized_start=118
  _globals['_GENERATEIMAGERESPONSE']._serialized_end=181
  _globals['_IMAGEGENERATION']._serialized_start=183
  _globals['_IMAGEGENERATION']._serialized_end=264
# @@protoc_insertion_point(module_scope)