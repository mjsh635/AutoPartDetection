# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AutoPartDetect.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AutoPartDetect.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x41utoPartDetect.proto\"\'\n\x18Get_List_of_Tags_Request\x12\x0b\n\x03\x61ge\x18\x01 \x01(\x03\"\x82\x01\n\x19Get_List_of_Tags_Response\x12\x36\n\x06person\x18\x01 \x03(\x0b\x32&.Get_List_of_Tags_Response.PersonEntry\x1a-\n\x0bPersonEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"$\n\x14Get_Tag_Data_Request\x12\x0c\n\x04name\x18\x01 \x01(\t\"(\n\x15Get_Tag_Data_Response\x12\x0f\n\x07message\x18\x01 \x01(\t\"0\n\x1dGet_Specific_Tag_Data_Request\x12\x0f\n\x07message\x18\x01 \x01(\t\".\n\x1eGet_Specific_Tag_Data_Response\x12\x0c\n\x04name\x18\x01 \x01(\t\"I\n\x06\x44\x65vice\x12\x12\n\ndeviceName\x18\x01 \x01(\t\x12\x10\n\x08\x64\x65viceId\x18\x02 \x01(\x03\x12\x19\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x0b.DeviceData\"4\n\nDeviceData\x12\x11\n\ttimesUsed\x18\x01 \x01(\x03\x12\x13\n\x0bqualityData\x18\x02 \x01(\t2\xf7\x01\n\x11\x41utoPartDetection\x12I\n\x10Get_List_of_Tags\x12\x19.Get_List_of_Tags_Request\x1a\x1a.Get_List_of_Tags_Response\x12=\n\x0cGet_Tag_Data\x12\x15.Get_Tag_Data_Request\x1a\x16.Get_Tag_Data_Response\x12X\n\x15Get_Specific_Tag_Data\x12\x1e.Get_Specific_Tag_Data_Request\x1a\x1f.Get_Specific_Tag_Data_Responseb\x06proto3'
)




_GET_LIST_OF_TAGS_REQUEST = _descriptor.Descriptor(
  name='Get_List_of_Tags_Request',
  full_name='Get_List_of_Tags_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='age', full_name='Get_List_of_Tags_Request.age', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=63,
)


_GET_LIST_OF_TAGS_RESPONSE_PERSONENTRY = _descriptor.Descriptor(
  name='PersonEntry',
  full_name='Get_List_of_Tags_Response.PersonEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Get_List_of_Tags_Response.PersonEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Get_List_of_Tags_Response.PersonEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=196,
)

_GET_LIST_OF_TAGS_RESPONSE = _descriptor.Descriptor(
  name='Get_List_of_Tags_Response',
  full_name='Get_List_of_Tags_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='Get_List_of_Tags_Response.person', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GET_LIST_OF_TAGS_RESPONSE_PERSONENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=196,
)


_GET_TAG_DATA_REQUEST = _descriptor.Descriptor(
  name='Get_Tag_Data_Request',
  full_name='Get_Tag_Data_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Get_Tag_Data_Request.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=234,
)


_GET_TAG_DATA_RESPONSE = _descriptor.Descriptor(
  name='Get_Tag_Data_Response',
  full_name='Get_Tag_Data_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Get_Tag_Data_Response.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=276,
)


_GET_SPECIFIC_TAG_DATA_REQUEST = _descriptor.Descriptor(
  name='Get_Specific_Tag_Data_Request',
  full_name='Get_Specific_Tag_Data_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='Get_Specific_Tag_Data_Request.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=326,
)


_GET_SPECIFIC_TAG_DATA_RESPONSE = _descriptor.Descriptor(
  name='Get_Specific_Tag_Data_Response',
  full_name='Get_Specific_Tag_Data_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Get_Specific_Tag_Data_Response.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=374,
)


_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceName', full_name='Device.deviceName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='Device.deviceId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Device.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=376,
  serialized_end=449,
)


_DEVICEDATA = _descriptor.Descriptor(
  name='DeviceData',
  full_name='DeviceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timesUsed', full_name='DeviceData.timesUsed', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qualityData', full_name='DeviceData.qualityData', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=503,
)

_GET_LIST_OF_TAGS_RESPONSE_PERSONENTRY.containing_type = _GET_LIST_OF_TAGS_RESPONSE
_GET_LIST_OF_TAGS_RESPONSE.fields_by_name['person'].message_type = _GET_LIST_OF_TAGS_RESPONSE_PERSONENTRY
_DEVICE.fields_by_name['data'].message_type = _DEVICEDATA
DESCRIPTOR.message_types_by_name['Get_List_of_Tags_Request'] = _GET_LIST_OF_TAGS_REQUEST
DESCRIPTOR.message_types_by_name['Get_List_of_Tags_Response'] = _GET_LIST_OF_TAGS_RESPONSE
DESCRIPTOR.message_types_by_name['Get_Tag_Data_Request'] = _GET_TAG_DATA_REQUEST
DESCRIPTOR.message_types_by_name['Get_Tag_Data_Response'] = _GET_TAG_DATA_RESPONSE
DESCRIPTOR.message_types_by_name['Get_Specific_Tag_Data_Request'] = _GET_SPECIFIC_TAG_DATA_REQUEST
DESCRIPTOR.message_types_by_name['Get_Specific_Tag_Data_Response'] = _GET_SPECIFIC_TAG_DATA_RESPONSE
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['DeviceData'] = _DEVICEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Get_List_of_Tags_Request = _reflection.GeneratedProtocolMessageType('Get_List_of_Tags_Request', (_message.Message,), {
  'DESCRIPTOR' : _GET_LIST_OF_TAGS_REQUEST,
  '__module__' : 'AutoPartDetect_pb2'
  # @@protoc_insertion_point(class_scope:Get_List_of_Tags_Request)
  })
_sym_db.RegisterMessage(Get_List_of_Tags_Request)

Get_List_of_Tags_Response = _reflection.GeneratedProtocolMessageType('Get_List_of_Tags_Response', (_message.Message,), {

  'PersonEntry' : _reflection.GeneratedProtocolMessageType('PersonEntry', (_message.Message,), {
    'DESCRIPTOR' : _GET_LIST_OF_TAGS_RESPONSE_PERSONENTRY,
    '__module__' : 'AutoPartDetect_pb2'
    # @@protoc_insertion_point(class_scope:Get_List_of_Tags_Response.PersonEntry)
    })
  ,
  'DESCRIPTOR' : _GET_LIST_OF_TAGS_RESPONSE,
  '__module__' : 'AutoPartDetect_pb2'
  # @@protoc_insertion_point(class_scope:Get_List_of_Tags_Response)
  })
_sym_db.RegisterMessage(Get_List_of_Tags_Response)
_sym_db.RegisterMessage(Get_List_of_Tags_Response.PersonEntry)

Get_Tag_Data_Request = _reflection.GeneratedProtocolMessageType('Get_Tag_Data_Request', (_message.Message,), {
  'DESCRIPTOR' : _GET_TAG_DATA_REQUEST,
  '__module__' : 'AutoPartDetect_pb2'
  # @@protoc_insertion_point(class_scope:Get_Tag_Data_Request)
  })
_sym_db.RegisterMessage(Get_Tag_Data_Request)

Get_Tag_Data_Response = _reflection.GeneratedProtocolMessageType('Get_Tag_Data_Response', (_message.Message,), {
  'DESCRIPTOR' : _GET_TAG_DATA_RESPONSE,
  '__module__' : 'AutoPartDetect_pb2'
  # @@protoc_insertion_point(class_scope:Get_Tag_Data_Response)
  })
_sym_db.RegisterMessage(Get_Tag_Data_Response)

Get_Specific_Tag_Data_Request = _reflection.GeneratedProtocolMessageType('Get_Specific_Tag_Data_Request', (_message.Message,), {
  'DESCRIPTOR' : _GET_SPECIFIC_TAG_DATA_REQUEST,
  '__module__' : 'AutoPartDetect_pb2'
  # @@protoc_insertion_point(class_scope:Get_Specific_Tag_Data_Request)
  })
_sym_db.RegisterMessage(Get_Specific_Tag_Data_Request)

Get_Specific_Tag_Data_Response = _reflection.GeneratedProtocolMessageType('Get_Specific_Tag_Data_Response', (_message.Message,), {
  'DESCRIPTOR' : _GET_SPECIFIC_TAG_DATA_RESPONSE,
  '__module__' : 'AutoPartDetect_pb2'
  # @@protoc_insertion_point(class_scope:Get_Specific_Tag_Data_Response)
  })
_sym_db.RegisterMessage(Get_Specific_Tag_Data_Response)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'AutoPartDetect_pb2'
  # @@protoc_insertion_point(class_scope:Device)
  })
_sym_db.RegisterMessage(Device)

DeviceData = _reflection.GeneratedProtocolMessageType('DeviceData', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEDATA,
  '__module__' : 'AutoPartDetect_pb2'
  # @@protoc_insertion_point(class_scope:DeviceData)
  })
_sym_db.RegisterMessage(DeviceData)


_GET_LIST_OF_TAGS_RESPONSE_PERSONENTRY._options = None

_AUTOPARTDETECTION = _descriptor.ServiceDescriptor(
  name='AutoPartDetection',
  full_name='AutoPartDetection',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=506,
  serialized_end=753,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get_List_of_Tags',
    full_name='AutoPartDetection.Get_List_of_Tags',
    index=0,
    containing_service=None,
    input_type=_GET_LIST_OF_TAGS_REQUEST,
    output_type=_GET_LIST_OF_TAGS_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get_Tag_Data',
    full_name='AutoPartDetection.Get_Tag_Data',
    index=1,
    containing_service=None,
    input_type=_GET_TAG_DATA_REQUEST,
    output_type=_GET_TAG_DATA_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get_Specific_Tag_Data',
    full_name='AutoPartDetection.Get_Specific_Tag_Data',
    index=2,
    containing_service=None,
    input_type=_GET_SPECIFIC_TAG_DATA_REQUEST,
    output_type=_GET_SPECIFIC_TAG_DATA_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTOPARTDETECTION)

DESCRIPTOR.services_by_name['AutoPartDetection'] = _AUTOPARTDETECTION

# @@protoc_insertion_point(module_scope)
