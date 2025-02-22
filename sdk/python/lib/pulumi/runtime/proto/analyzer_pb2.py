# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analyzer.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import plugin_pb2 as plugin__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analyzer.proto',
  package='pulumirpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0e\x61nalyzer.proto\x12\tpulumirpc\x1a\x0cplugin.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xd2\x01\n\x0e\x41nalyzeRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03urn\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x33\n\x07options\x18\x05 \x01(\x0b\x32\".pulumirpc.AnalyzerResourceOptions\x12\x35\n\x08provider\x18\x06 \x01(\x0b\x32#.pulumirpc.AnalyzerProviderResource\"\xb5\x03\n\x10\x41nalyzerResource\x12\x0c\n\x04type\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03urn\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x33\n\x07options\x18\x05 \x01(\x0b\x32\".pulumirpc.AnalyzerResourceOptions\x12\x35\n\x08provider\x18\x06 \x01(\x0b\x32#.pulumirpc.AnalyzerProviderResource\x12\x0e\n\x06parent\x18\x07 \x01(\t\x12\x14\n\x0c\x64\x65pendencies\x18\x08 \x03(\t\x12S\n\x14propertyDependencies\x18\t \x03(\x0b\x32\x35.pulumirpc.AnalyzerResource.PropertyDependenciesEntry\x1a\x64\n\x19PropertyDependenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.pulumirpc.AnalyzerPropertyDependencies:\x02\x38\x01\"\xc1\x02\n\x17\x41nalyzerResourceOptions\x12\x0f\n\x07protect\x18\x01 \x01(\x08\x12\x15\n\rignoreChanges\x18\x02 \x03(\t\x12\x1b\n\x13\x64\x65leteBeforeReplace\x18\x03 \x01(\x08\x12\"\n\x1a\x64\x65leteBeforeReplaceDefined\x18\x04 \x01(\x08\x12\x1f\n\x17\x61\x64\x64itionalSecretOutputs\x18\x05 \x03(\t\x12\x0f\n\x07\x61liases\x18\x06 \x03(\t\x12I\n\x0e\x63ustomTimeouts\x18\x07 \x01(\x0b\x32\x31.pulumirpc.AnalyzerResourceOptions.CustomTimeouts\x1a@\n\x0e\x43ustomTimeouts\x12\x0e\n\x06\x63reate\x18\x01 \x01(\x01\x12\x0e\n\x06update\x18\x02 \x01(\x01\x12\x0e\n\x06\x64\x65lete\x18\x03 \x01(\x01\"p\n\x18\x41nalyzerProviderResource\x12\x0c\n\x04type\x18\x01 \x01(\t\x12+\n\nproperties\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03urn\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\",\n\x1c\x41nalyzerPropertyDependencies\x12\x0c\n\x04urns\x18\x01 \x03(\t\"E\n\x13\x41nalyzeStackRequest\x12.\n\tresources\x18\x01 \x03(\x0b\x32\x1b.pulumirpc.AnalyzerResource\"D\n\x0f\x41nalyzeResponse\x12\x31\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x1c.pulumirpc.AnalyzeDiagnostic\"\xd2\x01\n\x11\x41nalyzeDiagnostic\x12\x12\n\npolicyName\x18\x01 \x01(\t\x12\x16\n\x0epolicyPackName\x18\x02 \x01(\t\x12\x19\n\x11policyPackVersion\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x0c\n\x04tags\x18\x06 \x03(\t\x12\x35\n\x10\x65nforcementLevel\x18\x07 \x01(\x0e\x32\x1b.pulumirpc.EnforcementLevel\x12\x0b\n\x03urn\x18\x08 \x01(\t\"k\n\x0c\x41nalyzerInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x02 \x01(\t\x12\'\n\x08policies\x18\x03 \x03(\x0b\x32\x15.pulumirpc.PolicyInfo\x12\x0f\n\x07version\x18\x04 \x01(\t\"\x8c\x01\n\nPolicyInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64isplayName\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x35\n\x10\x65nforcementLevel\x18\x05 \x01(\x0e\x32\x1b.pulumirpc.EnforcementLevel*/\n\x10\x45nforcementLevel\x12\x0c\n\x08\x41\x44VISORY\x10\x00\x12\r\n\tMANDATORY\x10\x01\x32\xa4\x02\n\x08\x41nalyzer\x12\x42\n\x07\x41nalyze\x12\x19.pulumirpc.AnalyzeRequest\x1a\x1a.pulumirpc.AnalyzeResponse\"\x00\x12L\n\x0c\x41nalyzeStack\x12\x1e.pulumirpc.AnalyzeStackRequest\x1a\x1a.pulumirpc.AnalyzeResponse\"\x00\x12\x44\n\x0fGetAnalyzerInfo\x12\x16.google.protobuf.Empty\x1a\x17.pulumirpc.AnalyzerInfo\"\x00\x12@\n\rGetPluginInfo\x12\x16.google.protobuf.Empty\x1a\x15.pulumirpc.PluginInfo\"\x00\x62\x06proto3'
  ,
  dependencies=[plugin__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])

_ENFORCEMENTLEVEL = _descriptor.EnumDescriptor(
  name='EnforcementLevel',
  full_name='pulumirpc.EnforcementLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADVISORY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MANDATORY', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1845,
  serialized_end=1892,
)
_sym_db.RegisterEnumDescriptor(_ENFORCEMENTLEVEL)

EnforcementLevel = enum_type_wrapper.EnumTypeWrapper(_ENFORCEMENTLEVEL)
ADVISORY = 0
MANDATORY = 1



_ANALYZEREQUEST = _descriptor.Descriptor(
  name='AnalyzeRequest',
  full_name='pulumirpc.AnalyzeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pulumirpc.AnalyzeRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.AnalyzeRequest.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.AnalyzeRequest.urn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.AnalyzeRequest.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='pulumirpc.AnalyzeRequest.options', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='pulumirpc.AnalyzeRequest.provider', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=103,
  serialized_end=313,
)


_ANALYZERRESOURCE_PROPERTYDEPENDENCIESENTRY = _descriptor.Descriptor(
  name='PropertyDependenciesEntry',
  full_name='pulumirpc.AnalyzerResource.PropertyDependenciesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pulumirpc.AnalyzerResource.PropertyDependenciesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pulumirpc.AnalyzerResource.PropertyDependenciesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=653,
  serialized_end=753,
)

_ANALYZERRESOURCE = _descriptor.Descriptor(
  name='AnalyzerResource',
  full_name='pulumirpc.AnalyzerResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pulumirpc.AnalyzerResource.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.AnalyzerResource.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.AnalyzerResource.urn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.AnalyzerResource.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='pulumirpc.AnalyzerResource.options', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='pulumirpc.AnalyzerResource.provider', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='pulumirpc.AnalyzerResource.parent', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='pulumirpc.AnalyzerResource.dependencies', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='propertyDependencies', full_name='pulumirpc.AnalyzerResource.propertyDependencies', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ANALYZERRESOURCE_PROPERTYDEPENDENCIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=753,
)


_ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS = _descriptor.Descriptor(
  name='CustomTimeouts',
  full_name='pulumirpc.AnalyzerResourceOptions.CustomTimeouts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='pulumirpc.AnalyzerResourceOptions.CustomTimeouts.create', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='pulumirpc.AnalyzerResourceOptions.CustomTimeouts.update', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete', full_name='pulumirpc.AnalyzerResourceOptions.CustomTimeouts.delete', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1013,
  serialized_end=1077,
)

_ANALYZERRESOURCEOPTIONS = _descriptor.Descriptor(
  name='AnalyzerResourceOptions',
  full_name='pulumirpc.AnalyzerResourceOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protect', full_name='pulumirpc.AnalyzerResourceOptions.protect', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignoreChanges', full_name='pulumirpc.AnalyzerResourceOptions.ignoreChanges', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteBeforeReplace', full_name='pulumirpc.AnalyzerResourceOptions.deleteBeforeReplace', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteBeforeReplaceDefined', full_name='pulumirpc.AnalyzerResourceOptions.deleteBeforeReplaceDefined', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='additionalSecretOutputs', full_name='pulumirpc.AnalyzerResourceOptions.additionalSecretOutputs', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aliases', full_name='pulumirpc.AnalyzerResourceOptions.aliases', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customTimeouts', full_name='pulumirpc.AnalyzerResourceOptions.customTimeouts', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=756,
  serialized_end=1077,
)


_ANALYZERPROVIDERRESOURCE = _descriptor.Descriptor(
  name='AnalyzerProviderResource',
  full_name='pulumirpc.AnalyzerProviderResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pulumirpc.AnalyzerProviderResource.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='pulumirpc.AnalyzerProviderResource.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.AnalyzerProviderResource.urn', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.AnalyzerProviderResource.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1079,
  serialized_end=1191,
)


_ANALYZERPROPERTYDEPENDENCIES = _descriptor.Descriptor(
  name='AnalyzerPropertyDependencies',
  full_name='pulumirpc.AnalyzerPropertyDependencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='urns', full_name='pulumirpc.AnalyzerPropertyDependencies.urns', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1193,
  serialized_end=1237,
)


_ANALYZESTACKREQUEST = _descriptor.Descriptor(
  name='AnalyzeStackRequest',
  full_name='pulumirpc.AnalyzeStackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='pulumirpc.AnalyzeStackRequest.resources', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1239,
  serialized_end=1308,
)


_ANALYZERESPONSE = _descriptor.Descriptor(
  name='AnalyzeResponse',
  full_name='pulumirpc.AnalyzeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diagnostics', full_name='pulumirpc.AnalyzeResponse.diagnostics', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1310,
  serialized_end=1378,
)


_ANALYZEDIAGNOSTIC = _descriptor.Descriptor(
  name='AnalyzeDiagnostic',
  full_name='pulumirpc.AnalyzeDiagnostic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policyName', full_name='pulumirpc.AnalyzeDiagnostic.policyName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policyPackName', full_name='pulumirpc.AnalyzeDiagnostic.policyPackName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policyPackVersion', full_name='pulumirpc.AnalyzeDiagnostic.policyPackVersion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pulumirpc.AnalyzeDiagnostic.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pulumirpc.AnalyzeDiagnostic.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='pulumirpc.AnalyzeDiagnostic.tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enforcementLevel', full_name='pulumirpc.AnalyzeDiagnostic.enforcementLevel', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='urn', full_name='pulumirpc.AnalyzeDiagnostic.urn', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1381,
  serialized_end=1591,
)


_ANALYZERINFO = _descriptor.Descriptor(
  name='AnalyzerInfo',
  full_name='pulumirpc.AnalyzerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.AnalyzerInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='pulumirpc.AnalyzerInfo.displayName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policies', full_name='pulumirpc.AnalyzerInfo.policies', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='pulumirpc.AnalyzerInfo.version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1593,
  serialized_end=1700,
)


_POLICYINFO = _descriptor.Descriptor(
  name='PolicyInfo',
  full_name='pulumirpc.PolicyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pulumirpc.PolicyInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='pulumirpc.PolicyInfo.displayName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='pulumirpc.PolicyInfo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pulumirpc.PolicyInfo.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enforcementLevel', full_name='pulumirpc.PolicyInfo.enforcementLevel', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1703,
  serialized_end=1843,
)

_ANALYZEREQUEST.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ANALYZEREQUEST.fields_by_name['options'].message_type = _ANALYZERRESOURCEOPTIONS
_ANALYZEREQUEST.fields_by_name['provider'].message_type = _ANALYZERPROVIDERRESOURCE
_ANALYZERRESOURCE_PROPERTYDEPENDENCIESENTRY.fields_by_name['value'].message_type = _ANALYZERPROPERTYDEPENDENCIES
_ANALYZERRESOURCE_PROPERTYDEPENDENCIESENTRY.containing_type = _ANALYZERRESOURCE
_ANALYZERRESOURCE.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ANALYZERRESOURCE.fields_by_name['options'].message_type = _ANALYZERRESOURCEOPTIONS
_ANALYZERRESOURCE.fields_by_name['provider'].message_type = _ANALYZERPROVIDERRESOURCE
_ANALYZERRESOURCE.fields_by_name['propertyDependencies'].message_type = _ANALYZERRESOURCE_PROPERTYDEPENDENCIESENTRY
_ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS.containing_type = _ANALYZERRESOURCEOPTIONS
_ANALYZERRESOURCEOPTIONS.fields_by_name['customTimeouts'].message_type = _ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS
_ANALYZERPROVIDERRESOURCE.fields_by_name['properties'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ANALYZESTACKREQUEST.fields_by_name['resources'].message_type = _ANALYZERRESOURCE
_ANALYZERESPONSE.fields_by_name['diagnostics'].message_type = _ANALYZEDIAGNOSTIC
_ANALYZEDIAGNOSTIC.fields_by_name['enforcementLevel'].enum_type = _ENFORCEMENTLEVEL
_ANALYZERINFO.fields_by_name['policies'].message_type = _POLICYINFO
_POLICYINFO.fields_by_name['enforcementLevel'].enum_type = _ENFORCEMENTLEVEL
DESCRIPTOR.message_types_by_name['AnalyzeRequest'] = _ANALYZEREQUEST
DESCRIPTOR.message_types_by_name['AnalyzerResource'] = _ANALYZERRESOURCE
DESCRIPTOR.message_types_by_name['AnalyzerResourceOptions'] = _ANALYZERRESOURCEOPTIONS
DESCRIPTOR.message_types_by_name['AnalyzerProviderResource'] = _ANALYZERPROVIDERRESOURCE
DESCRIPTOR.message_types_by_name['AnalyzerPropertyDependencies'] = _ANALYZERPROPERTYDEPENDENCIES
DESCRIPTOR.message_types_by_name['AnalyzeStackRequest'] = _ANALYZESTACKREQUEST
DESCRIPTOR.message_types_by_name['AnalyzeResponse'] = _ANALYZERESPONSE
DESCRIPTOR.message_types_by_name['AnalyzeDiagnostic'] = _ANALYZEDIAGNOSTIC
DESCRIPTOR.message_types_by_name['AnalyzerInfo'] = _ANALYZERINFO
DESCRIPTOR.message_types_by_name['PolicyInfo'] = _POLICYINFO
DESCRIPTOR.enum_types_by_name['EnforcementLevel'] = _ENFORCEMENTLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnalyzeRequest = _reflection.GeneratedProtocolMessageType('AnalyzeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEREQUEST,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzeRequest)
  })
_sym_db.RegisterMessage(AnalyzeRequest)

AnalyzerResource = _reflection.GeneratedProtocolMessageType('AnalyzerResource', (_message.Message,), {

  'PropertyDependenciesEntry' : _reflection.GeneratedProtocolMessageType('PropertyDependenciesEntry', (_message.Message,), {
    'DESCRIPTOR' : _ANALYZERRESOURCE_PROPERTYDEPENDENCIESENTRY,
    '__module__' : 'analyzer_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerResource.PropertyDependenciesEntry)
    })
  ,
  'DESCRIPTOR' : _ANALYZERRESOURCE,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerResource)
  })
_sym_db.RegisterMessage(AnalyzerResource)
_sym_db.RegisterMessage(AnalyzerResource.PropertyDependenciesEntry)

AnalyzerResourceOptions = _reflection.GeneratedProtocolMessageType('AnalyzerResourceOptions', (_message.Message,), {

  'CustomTimeouts' : _reflection.GeneratedProtocolMessageType('CustomTimeouts', (_message.Message,), {
    'DESCRIPTOR' : _ANALYZERRESOURCEOPTIONS_CUSTOMTIMEOUTS,
    '__module__' : 'analyzer_pb2'
    # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerResourceOptions.CustomTimeouts)
    })
  ,
  'DESCRIPTOR' : _ANALYZERRESOURCEOPTIONS,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerResourceOptions)
  })
_sym_db.RegisterMessage(AnalyzerResourceOptions)
_sym_db.RegisterMessage(AnalyzerResourceOptions.CustomTimeouts)

AnalyzerProviderResource = _reflection.GeneratedProtocolMessageType('AnalyzerProviderResource', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZERPROVIDERRESOURCE,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerProviderResource)
  })
_sym_db.RegisterMessage(AnalyzerProviderResource)

AnalyzerPropertyDependencies = _reflection.GeneratedProtocolMessageType('AnalyzerPropertyDependencies', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZERPROPERTYDEPENDENCIES,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerPropertyDependencies)
  })
_sym_db.RegisterMessage(AnalyzerPropertyDependencies)

AnalyzeStackRequest = _reflection.GeneratedProtocolMessageType('AnalyzeStackRequest', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZESTACKREQUEST,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzeStackRequest)
  })
_sym_db.RegisterMessage(AnalyzeStackRequest)

AnalyzeResponse = _reflection.GeneratedProtocolMessageType('AnalyzeResponse', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZERESPONSE,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzeResponse)
  })
_sym_db.RegisterMessage(AnalyzeResponse)

AnalyzeDiagnostic = _reflection.GeneratedProtocolMessageType('AnalyzeDiagnostic', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZEDIAGNOSTIC,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzeDiagnostic)
  })
_sym_db.RegisterMessage(AnalyzeDiagnostic)

AnalyzerInfo = _reflection.GeneratedProtocolMessageType('AnalyzerInfo', (_message.Message,), {
  'DESCRIPTOR' : _ANALYZERINFO,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.AnalyzerInfo)
  })
_sym_db.RegisterMessage(AnalyzerInfo)

PolicyInfo = _reflection.GeneratedProtocolMessageType('PolicyInfo', (_message.Message,), {
  'DESCRIPTOR' : _POLICYINFO,
  '__module__' : 'analyzer_pb2'
  # @@protoc_insertion_point(class_scope:pulumirpc.PolicyInfo)
  })
_sym_db.RegisterMessage(PolicyInfo)


_ANALYZERRESOURCE_PROPERTYDEPENDENCIESENTRY._options = None

_ANALYZER = _descriptor.ServiceDescriptor(
  name='Analyzer',
  full_name='pulumirpc.Analyzer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1895,
  serialized_end=2187,
  methods=[
  _descriptor.MethodDescriptor(
    name='Analyze',
    full_name='pulumirpc.Analyzer.Analyze',
    index=0,
    containing_service=None,
    input_type=_ANALYZEREQUEST,
    output_type=_ANALYZERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AnalyzeStack',
    full_name='pulumirpc.Analyzer.AnalyzeStack',
    index=1,
    containing_service=None,
    input_type=_ANALYZESTACKREQUEST,
    output_type=_ANALYZERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAnalyzerInfo',
    full_name='pulumirpc.Analyzer.GetAnalyzerInfo',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_ANALYZERINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPluginInfo',
    full_name='pulumirpc.Analyzer.GetPluginInfo',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=plugin__pb2._PLUGININFO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYZER)

DESCRIPTOR.services_by_name['Analyzer'] = _ANALYZER

# @@protoc_insertion_point(module_scope)
