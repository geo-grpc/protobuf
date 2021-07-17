# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: epl/protobuf/v1/geometry_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from epl.protobuf.v1 import geometry_pb2 as epl_dot_protobuf_dot_v1_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='epl/protobuf/v1/geometry_service.proto',
  package='epl.protobuf.v1',
  syntax='proto3',
  serialized_options=b'\n\023com.epl.protobuf.v1B\024GeometryServiceProtoP\001Z.github.com/geo-grpc/api/golang/epl/protobuf/v1\242\002\003GMS\252\002\023com.epl.protobuf.v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&epl/protobuf/v1/geometry_service.proto\x12\x0f\x65pl.protobuf.v1\x1a\x1e\x65pl/protobuf/v1/geometry.proto2\xca\x04\n\x0fGeometryService\x12P\n\x07Operate\x12 .epl.protobuf.v1.GeometryRequest\x1a!.epl.protobuf.v1.GeometryResponse\"\x00\x12\\\n\x0fOperateBiStream\x12 .epl.protobuf.v1.GeometryRequest\x1a!.epl.protobuf.v1.GeometryResponse\"\x00(\x01\x30\x01\x12`\n\x13OperateBiStreamFlow\x12 .epl.protobuf.v1.GeometryRequest\x1a!.epl.protobuf.v1.GeometryResponse\"\x00(\x01\x30\x01\x12^\n\x13OperateServerStream\x12 .epl.protobuf.v1.GeometryRequest\x1a!.epl.protobuf.v1.GeometryResponse\"\x00\x30\x01\x12^\n\x13OperateClientStream\x12 .epl.protobuf.v1.GeometryRequest\x1a!.epl.protobuf.v1.GeometryResponse\"\x00(\x01\x12\x65\n\x17\x46ileOperateBiStreamFlow\x12!.epl.protobuf.v1.FileRequestChunk\x1a!.epl.protobuf.v1.GeometryResponse\"\x00(\x01\x30\x01\x42y\n\x13\x63om.epl.protobuf.v1B\x14GeometryServiceProtoP\x01Z.github.com/geo-grpc/api/golang/epl/protobuf/v1\xa2\x02\x03GMS\xaa\x02\x13\x63om.epl.protobuf.v1b\x06proto3'
  ,
  dependencies=[epl_dot_protobuf_dot_v1_dot_geometry__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_GEOMETRYSERVICE = _descriptor.ServiceDescriptor(
  name='GeometryService',
  full_name='epl.protobuf.v1.GeometryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=92,
  serialized_end=678,
  methods=[
  _descriptor.MethodDescriptor(
    name='Operate',
    full_name='epl.protobuf.v1.GeometryService.Operate',
    index=0,
    containing_service=None,
    input_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYREQUEST,
    output_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OperateBiStream',
    full_name='epl.protobuf.v1.GeometryService.OperateBiStream',
    index=1,
    containing_service=None,
    input_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYREQUEST,
    output_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OperateBiStreamFlow',
    full_name='epl.protobuf.v1.GeometryService.OperateBiStreamFlow',
    index=2,
    containing_service=None,
    input_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYREQUEST,
    output_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OperateServerStream',
    full_name='epl.protobuf.v1.GeometryService.OperateServerStream',
    index=3,
    containing_service=None,
    input_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYREQUEST,
    output_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OperateClientStream',
    full_name='epl.protobuf.v1.GeometryService.OperateClientStream',
    index=4,
    containing_service=None,
    input_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYREQUEST,
    output_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FileOperateBiStreamFlow',
    full_name='epl.protobuf.v1.GeometryService.FileOperateBiStreamFlow',
    index=5,
    containing_service=None,
    input_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._FILEREQUESTCHUNK,
    output_type=epl_dot_protobuf_dot_v1_dot_geometry__pb2._GEOMETRYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GEOMETRYSERVICE)

DESCRIPTOR.services_by_name['GeometryService'] = _GEOMETRYSERVICE

# @@protoc_insertion_point(module_scope)