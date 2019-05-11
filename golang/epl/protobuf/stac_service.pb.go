// Code generated by protoc-gen-go. DO NOT EDIT.
// source: epl/protobuf/stac_service.proto

package protobuf // import "github.com/geo-grpc/api/golang/epl/protobuf"

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

import (
	context "golang.org/x/net/context"
	grpc "google.golang.org/grpc"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// StacServiceClient is the client API for StacService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type StacServiceClient interface {
	Search(ctx context.Context, in *StacRequest, opts ...grpc.CallOption) (StacService_SearchClient, error)
	Insert(ctx context.Context, in *StacItem, opts ...grpc.CallOption) (*StacUpsertResponse, error)
	Update(ctx context.Context, in *StacItem, opts ...grpc.CallOption) (*StacUpsertResponse, error)
}

type stacServiceClient struct {
	cc *grpc.ClientConn
}

func NewStacServiceClient(cc *grpc.ClientConn) StacServiceClient {
	return &stacServiceClient{cc}
}

func (c *stacServiceClient) Search(ctx context.Context, in *StacRequest, opts ...grpc.CallOption) (StacService_SearchClient, error) {
	stream, err := c.cc.NewStream(ctx, &_StacService_serviceDesc.Streams[0], "/epl.protobuf.StacService/Search", opts...)
	if err != nil {
		return nil, err
	}
	x := &stacServiceSearchClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type StacService_SearchClient interface {
	Recv() (*StacItem, error)
	grpc.ClientStream
}

type stacServiceSearchClient struct {
	grpc.ClientStream
}

func (x *stacServiceSearchClient) Recv() (*StacItem, error) {
	m := new(StacItem)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *stacServiceClient) Insert(ctx context.Context, in *StacItem, opts ...grpc.CallOption) (*StacUpsertResponse, error) {
	out := new(StacUpsertResponse)
	err := c.cc.Invoke(ctx, "/epl.protobuf.StacService/Insert", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *stacServiceClient) Update(ctx context.Context, in *StacItem, opts ...grpc.CallOption) (*StacUpsertResponse, error) {
	out := new(StacUpsertResponse)
	err := c.cc.Invoke(ctx, "/epl.protobuf.StacService/Update", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// StacServiceServer is the server API for StacService service.
type StacServiceServer interface {
	Search(*StacRequest, StacService_SearchServer) error
	Insert(context.Context, *StacItem) (*StacUpsertResponse, error)
	Update(context.Context, *StacItem) (*StacUpsertResponse, error)
}

func RegisterStacServiceServer(s *grpc.Server, srv StacServiceServer) {
	s.RegisterService(&_StacService_serviceDesc, srv)
}

func _StacService_Search_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(StacRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(StacServiceServer).Search(m, &stacServiceSearchServer{stream})
}

type StacService_SearchServer interface {
	Send(*StacItem) error
	grpc.ServerStream
}

type stacServiceSearchServer struct {
	grpc.ServerStream
}

func (x *stacServiceSearchServer) Send(m *StacItem) error {
	return x.ServerStream.SendMsg(m)
}

func _StacService_Insert_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(StacItem)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(StacServiceServer).Insert(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/epl.protobuf.StacService/Insert",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(StacServiceServer).Insert(ctx, req.(*StacItem))
	}
	return interceptor(ctx, in, info, handler)
}

func _StacService_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(StacItem)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(StacServiceServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/epl.protobuf.StacService/Update",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(StacServiceServer).Update(ctx, req.(*StacItem))
	}
	return interceptor(ctx, in, info, handler)
}

var _StacService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "epl.protobuf.StacService",
	HandlerType: (*StacServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Insert",
			Handler:    _StacService_Insert_Handler,
		},
		{
			MethodName: "Update",
			Handler:    _StacService_Update_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "Search",
			Handler:       _StacService_Search_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "epl/protobuf/stac_service.proto",
}

func init() {
	proto.RegisterFile("epl/protobuf/stac_service.proto", fileDescriptor_stac_service_41e5cc1076fef446)
}

var fileDescriptor_stac_service_41e5cc1076fef446 = []byte{
	// 224 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0x92, 0x4f, 0x2d, 0xc8, 0xd1,
	0x2f, 0x28, 0xca, 0x2f, 0xc9, 0x4f, 0x2a, 0x4d, 0xd3, 0x2f, 0x2e, 0x49, 0x4c, 0x8e, 0x2f, 0x4e,
	0x2d, 0x2a, 0xcb, 0x4c, 0x4e, 0xd5, 0x03, 0x8b, 0x0a, 0xf1, 0xa4, 0x16, 0xe4, 0xe8, 0xc1, 0x14,
	0x48, 0x89, 0x63, 0x28, 0x87, 0xc8, 0x19, 0xdd, 0x62, 0xe4, 0xe2, 0x0e, 0x2e, 0x49, 0x4c, 0x0e,
	0x86, 0x68, 0x16, 0xb2, 0xe7, 0x62, 0x0b, 0x4e, 0x4d, 0x2c, 0x4a, 0xce, 0x10, 0x92, 0xd4, 0x43,
	0x36, 0x41, 0x0f, 0xa4, 0x28, 0x28, 0xb5, 0xb0, 0x34, 0xb5, 0xb8, 0x44, 0x4a, 0x0c, 0x53, 0xca,
	0xb3, 0x24, 0x35, 0x57, 0x89, 0xc1, 0x80, 0x51, 0xc8, 0x85, 0x8b, 0xcd, 0x33, 0xaf, 0x38, 0xb5,
	0xa8, 0x44, 0x08, 0x87, 0x2a, 0x29, 0x05, 0x4c, 0xf1, 0xd0, 0x02, 0x90, 0x8e, 0xa0, 0xd4, 0xe2,
	0x82, 0xfc, 0xbc, 0xe2, 0x54, 0x25, 0x06, 0x90, 0x29, 0xa1, 0x05, 0x29, 0x89, 0x25, 0xa9, 0x94,
	0x98, 0xe2, 0x14, 0xc9, 0x25, 0x90, 0x9c, 0x9f, 0x8b, 0xa2, 0xd0, 0x49, 0x00, 0xc9, 0xb7, 0x01,
	0x20, 0xc1, 0x00, 0xc6, 0x28, 0xed, 0xf4, 0xcc, 0x92, 0x8c, 0xd2, 0x24, 0xbd, 0xe4, 0xfc, 0x5c,
	0xfd, 0xf4, 0xd4, 0x7c, 0xdd, 0xf4, 0xa2, 0x82, 0x64, 0xfd, 0xc4, 0x82, 0x4c, 0xfd, 0xf4, 0xfc,
	0x9c, 0xc4, 0xbc, 0x74, 0x7d, 0xe4, 0xc0, 0x5b, 0xc4, 0xc4, 0x1c, 0x1c, 0x12, 0x9c, 0xc4, 0x06,
	0xe6, 0x1b, 0x03, 0x02, 0x00, 0x00, 0xff, 0xff, 0x09, 0x68, 0xac, 0x52, 0x88, 0x01, 0x00, 0x00,
}
