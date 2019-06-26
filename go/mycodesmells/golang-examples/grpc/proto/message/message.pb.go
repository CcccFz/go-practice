// Code generated by protoc-gen-go. DO NOT EDIT.
// source: proto/message/message.proto

package message

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Person struct {
	FirstName            string   `protobuf:"bytes,1,opt,name=first_name,json=firstName,proto3" json:"first_name,omitempty"`
	LastName             string   `protobuf:"bytes,2,opt,name=last_name,json=lastName,proto3" json:"last_name,omitempty"`
	DateOfBirth          string   `protobuf:"bytes,3,opt,name=date_of_birth,json=dateOfBirth,proto3" json:"date_of_birth,omitempty"`
	Cool                 bool     `protobuf:"varint,4,opt,name=cool,proto3" json:"cool,omitempty"`
	ArgumentsWon         int32    `protobuf:"varint,5,opt,name=arguments_won,json=argumentsWon,proto3" json:"arguments_won,omitempty"`
	Hobbies              []*Hobby `protobuf:"bytes,6,rep,name=hobbies,proto3" json:"hobbies,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Person) Reset()         { *m = Person{} }
func (m *Person) String() string { return proto.CompactTextString(m) }
func (*Person) ProtoMessage()    {}
func (*Person) Descriptor() ([]byte, []int) {
	return fileDescriptor_f274517418484e40, []int{0}
}

func (m *Person) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Person.Unmarshal(m, b)
}
func (m *Person) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Person.Marshal(b, m, deterministic)
}
func (m *Person) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Person.Merge(m, src)
}
func (m *Person) XXX_Size() int {
	return xxx_messageInfo_Person.Size(m)
}
func (m *Person) XXX_DiscardUnknown() {
	xxx_messageInfo_Person.DiscardUnknown(m)
}

var xxx_messageInfo_Person proto.InternalMessageInfo

func (m *Person) GetFirstName() string {
	if m != nil {
		return m.FirstName
	}
	return ""
}

func (m *Person) GetLastName() string {
	if m != nil {
		return m.LastName
	}
	return ""
}

func (m *Person) GetDateOfBirth() string {
	if m != nil {
		return m.DateOfBirth
	}
	return ""
}

func (m *Person) GetCool() bool {
	if m != nil {
		return m.Cool
	}
	return false
}

func (m *Person) GetArgumentsWon() int32 {
	if m != nil {
		return m.ArgumentsWon
	}
	return 0
}

func (m *Person) GetHobbies() []*Hobby {
	if m != nil {
		return m.Hobbies
	}
	return nil
}

type Hobby struct {
	Name                 string   `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Description          string   `protobuf:"bytes,2,opt,name=description,proto3" json:"description,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *Hobby) Reset()         { *m = Hobby{} }
func (m *Hobby) String() string { return proto.CompactTextString(m) }
func (*Hobby) ProtoMessage()    {}
func (*Hobby) Descriptor() ([]byte, []int) {
	return fileDescriptor_f274517418484e40, []int{1}
}

func (m *Hobby) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Hobby.Unmarshal(m, b)
}
func (m *Hobby) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Hobby.Marshal(b, m, deterministic)
}
func (m *Hobby) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Hobby.Merge(m, src)
}
func (m *Hobby) XXX_Size() int {
	return xxx_messageInfo_Hobby.Size(m)
}
func (m *Hobby) XXX_DiscardUnknown() {
	xxx_messageInfo_Hobby.DiscardUnknown(m)
}

var xxx_messageInfo_Hobby proto.InternalMessageInfo

func (m *Hobby) GetName() string {
	if m != nil {
		return m.Name
	}
	return ""
}

func (m *Hobby) GetDescription() string {
	if m != nil {
		return m.Description
	}
	return ""
}

func init() {
	proto.RegisterType((*Person)(nil), "mycodesmells.golangexamples.grpc.message.Person")
	proto.RegisterType((*Hobby)(nil), "mycodesmells.golangexamples.grpc.message.Hobby")
}

func init() { proto.RegisterFile("proto/message/message.proto", fileDescriptor_f274517418484e40) }

var fileDescriptor_f274517418484e40 = []byte{
	// 289 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x8c, 0x91, 0xbf, 0x4b, 0x03, 0x31,
	0x14, 0xc7, 0x39, 0xfb, 0xc3, 0x36, 0xb5, 0x4b, 0xa6, 0x83, 0x22, 0x1c, 0x75, 0xb9, 0xc5, 0x04,
	0x74, 0x13, 0x5d, 0x3a, 0xe9, 0xa2, 0x72, 0x8b, 0xe0, 0x72, 0x24, 0xd7, 0xd7, 0x34, 0x90, 0xe4,
	0x1d, 0x49, 0x8a, 0xf6, 0x7f, 0xf6, 0x8f, 0x90, 0x8b, 0x3d, 0x39, 0x37, 0xa7, 0xbc, 0x7c, 0xbe,
	0x2f, 0xf0, 0xf9, 0x12, 0xb2, 0x6a, 0x3d, 0x46, 0xe4, 0x16, 0x42, 0x10, 0x0a, 0xfa, 0x93, 0x25,
	0x4a, 0x4b, 0x7b, 0x6c, 0x70, 0x0b, 0xc1, 0x82, 0x31, 0x81, 0x29, 0x34, 0xc2, 0x29, 0xf8, 0x14,
	0xb6, 0x35, 0x10, 0x98, 0xf2, 0x6d, 0xc3, 0x4e, 0xfb, 0xeb, 0xaf, 0x8c, 0x4c, 0x5f, 0xc1, 0x07,
	0x74, 0xf4, 0x92, 0x90, 0x9d, 0xf6, 0x21, 0xd6, 0x4e, 0x58, 0xc8, 0xb3, 0x22, 0x2b, 0xe7, 0xd5,
	0x3c, 0x91, 0x67, 0x61, 0x81, 0xae, 0xc8, 0xdc, 0x88, 0x3e, 0x3d, 0x4b, 0xe9, 0xac, 0x03, 0x29,
	0x5c, 0x93, 0xe5, 0x56, 0x44, 0xa8, 0x71, 0x57, 0x4b, 0xed, 0xe3, 0x3e, 0x1f, 0xa5, 0x85, 0x45,
	0x07, 0x5f, 0x76, 0x9b, 0x0e, 0x51, 0x4a, 0xc6, 0x0d, 0xa2, 0xc9, 0xc7, 0x45, 0x56, 0xce, 0xaa,
	0x34, 0xd3, 0x2b, 0xb2, 0x14, 0x5e, 0x1d, 0x2c, 0xb8, 0x18, 0xea, 0x0f, 0x74, 0xf9, 0xa4, 0xc8,
	0xca, 0x49, 0x75, 0xf1, 0x0b, 0xdf, 0xd0, 0xd1, 0x27, 0x72, 0xbe, 0x47, 0x29, 0x35, 0x84, 0x7c,
	0x5a, 0x8c, 0xca, 0xc5, 0x0d, 0x67, 0xff, 0xed, 0xc7, 0x1e, 0x51, 0xca, 0x63, 0xd5, 0xbf, 0x5f,
	0x3f, 0x90, 0x49, 0x22, 0x9d, 0xcc, 0xa0, 0x66, 0x9a, 0x69, 0x41, 0x16, 0x5b, 0x08, 0x8d, 0xd7,
	0x6d, 0xd4, 0xe8, 0x4e, 0x1d, 0x87, 0x68, 0x73, 0xff, 0x7e, 0xa7, 0x74, 0xdc, 0x1f, 0x24, 0x6b,
	0xd0, 0xf2, 0xa1, 0x04, 0xff, 0x91, 0xb8, 0xee, 0x2d, 0x78, 0x67, 0xc1, 0xff, 0xfc, 0x91, 0x9c,
	0xa6, 0xeb, 0xed, 0x77, 0x00, 0x00, 0x00, 0xff, 0xff, 0x84, 0xbb, 0x89, 0x1a, 0xbb, 0x01, 0x00,
	0x00,
}
