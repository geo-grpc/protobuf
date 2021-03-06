# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from epl.protobuf.v1 import geometry_pb2 as epl_dot_protobuf_dot_v1_dot_geometry__pb2


class GeometryServiceStub(object):
    """
    gRPC Interfaces for working with geometry operators
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Operate = channel.unary_unary(
                '/epl.protobuf.v1.GeometryService/Operate',
                request_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
                response_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
                )
        self.OperateBiStream = channel.stream_stream(
                '/epl.protobuf.v1.GeometryService/OperateBiStream',
                request_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
                response_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
                )
        self.OperateBiStreamFlow = channel.stream_stream(
                '/epl.protobuf.v1.GeometryService/OperateBiStreamFlow',
                request_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
                response_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
                )
        self.OperateServerStream = channel.unary_stream(
                '/epl.protobuf.v1.GeometryService/OperateServerStream',
                request_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
                response_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
                )
        self.OperateClientStream = channel.stream_unary(
                '/epl.protobuf.v1.GeometryService/OperateClientStream',
                request_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
                response_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
                )
        self.FileOperateBiStreamFlow = channel.stream_stream(
                '/epl.protobuf.v1.GeometryService/FileOperateBiStreamFlow',
                request_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.FileRequestChunk.SerializeToString,
                response_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
                )


class GeometryServiceServicer(object):
    """
    gRPC Interfaces for working with geometry operators
    """

    def Operate(self, request, context):
        """Execute a single blocking geometry operation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OperateBiStream(self, request_iterator, context):
        """stream in operator requests and get back a stream of results
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OperateBiStreamFlow(self, request_iterator, context):
        """manual flow control bi-directional stream. example
        go shouldn't use this because of https://groups.google.com/forum/#!topic/grpc-io/6_B46Oszb4k ?
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OperateServerStream(self, request, context):
        """Maybe a cut operation that returns a lot of different geometries? for now, this is not implemented.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OperateClientStream(self, request_iterator, context):
        """Maybe something like a union operation. for now, this is not implemented.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FileOperateBiStreamFlow(self, request_iterator, context):
        """stream in file chunks for a geometry file type and stream back results for each geometry encountered
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GeometryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Operate': grpc.unary_unary_rpc_method_handler(
                    servicer.Operate,
                    request_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.FromString,
                    response_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.SerializeToString,
            ),
            'OperateBiStream': grpc.stream_stream_rpc_method_handler(
                    servicer.OperateBiStream,
                    request_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.FromString,
                    response_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.SerializeToString,
            ),
            'OperateBiStreamFlow': grpc.stream_stream_rpc_method_handler(
                    servicer.OperateBiStreamFlow,
                    request_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.FromString,
                    response_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.SerializeToString,
            ),
            'OperateServerStream': grpc.unary_stream_rpc_method_handler(
                    servicer.OperateServerStream,
                    request_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.FromString,
                    response_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.SerializeToString,
            ),
            'OperateClientStream': grpc.stream_unary_rpc_method_handler(
                    servicer.OperateClientStream,
                    request_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.FromString,
                    response_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.SerializeToString,
            ),
            'FileOperateBiStreamFlow': grpc.stream_stream_rpc_method_handler(
                    servicer.FileOperateBiStreamFlow,
                    request_deserializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.FileRequestChunk.FromString,
                    response_serializer=epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'epl.protobuf.v1.GeometryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GeometryService(object):
    """
    gRPC Interfaces for working with geometry operators
    """

    @staticmethod
    def Operate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/epl.protobuf.v1.GeometryService/Operate',
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OperateBiStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/epl.protobuf.v1.GeometryService/OperateBiStream',
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OperateBiStreamFlow(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/epl.protobuf.v1.GeometryService/OperateBiStreamFlow',
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OperateServerStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/epl.protobuf.v1.GeometryService/OperateServerStream',
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OperateClientStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/epl.protobuf.v1.GeometryService/OperateClientStream',
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryRequest.SerializeToString,
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FileOperateBiStreamFlow(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/epl.protobuf.v1.GeometryService/FileOperateBiStreamFlow',
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.FileRequestChunk.SerializeToString,
            epl_dot_protobuf_dot_v1_dot_geometry__pb2.GeometryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
