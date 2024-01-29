# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app.protos.generate_image_pb2 as generate__image__pb2


class ImageGenerationStub(object):
    """Image Generation Service Definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateImage = channel.unary_unary(
                '/ImageGeneration/GenerateImage',
                request_serializer=generate__image__pb2.GenerateImageRequest.SerializeToString,
                response_deserializer=generate__image__pb2.GenerateImageResponse.FromString,
                )


class ImageGenerationServicer(object):
    """Image Generation Service Definition
    """

    def GenerateImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImageGenerationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateImage': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateImage,
                    request_deserializer=generate__image__pb2.GenerateImageRequest.FromString,
                    response_serializer=generate__image__pb2.GenerateImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ImageGeneration', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ImageGeneration(object):
    """Image Generation Service Definition
    """

    @staticmethod
    def GenerateImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ImageGeneration/GenerateImage',
            generate__image__pb2.GenerateImageRequest.SerializeToString,
            generate__image__pb2.GenerateImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
