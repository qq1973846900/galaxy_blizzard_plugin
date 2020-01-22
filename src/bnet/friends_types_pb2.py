# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/friends_types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bnet.attribute_pb2
import bnet.entity_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/friends_types.proto',
  package='bnet.protocol.friends',
  serialized_pb=_b('\n\x18\x62net/friends_types.proto\x12\x15\x62net.protocol.friends\x1a\x14\x62net/attribute.proto\x1a\x11\x62net/entity.proto\"\xfe\x01\n\x12ReceivedInvitation\x12\n\n\x02id\x18\x01 \x02(\x06\x12\x31\n\x10inviter_identity\x18\x02 \x02(\x0b\x32\x17.bnet.protocol.Identity\x12\x31\n\x10invitee_identity\x18\x03 \x02(\x0b\x32\x17.bnet.protocol.Identity\x12\x14\n\x0cinviter_name\x18\x04 \x01(\t\x12\x14\n\x0cinvitee_name\x18\x05 \x01(\t\x12\x1a\n\x12invitation_message\x18\x06 \x01(\t\x12\x15\n\rcreation_time\x18\x07 \x01(\x04\x12\x17\n\x0f\x65xpiration_time\x18\x08 \x01(\x04\"\xbb\x01\n\x06\x46riend\x12#\n\x02id\x18\x01 \x02(\x0b\x32\x17.bnet.protocol.EntityId\x12\x35\n\tattribute\x18\x02 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x10\n\x04role\x18\x03 \x03(\rB\x02\x10\x01\x12\x15\n\nprivileges\x18\x04 \x01(\x04:\x01\x30\x12\x18\n\x10\x61ttributes_epoch\x18\x05 \x01(\x04\x12\x12\n\nbattle_tag\x18\x07 \x01(\t\"C\n\x10\x46riendInvitation\x12\x1d\n\x0e\x66irst_received\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x04role\x18\x02 \x03(\rB\x02\x10\x01\"\xb0\x01\n\x16\x46riendInvitationParams\x12\x14\n\x0ctarget_email\x18\x01 \x01(\t\x12\x19\n\x11target_battle_tag\x18\x02 \x01(\t\x12\x1a\n\x12inviter_battle_tag\x18\x03 \x01(\t\x12\x19\n\x11inviter_full_name\x18\x04 \x01(\t\x12\x1c\n\x14invitee_display_name\x18\x05 \x01(\t\x12\x10\n\x04role\x18\x06 \x03(\rB\x02\x10\x01')
  ,
  dependencies=[bnet.attribute_pb2.DESCRIPTOR,bnet.entity_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RECEIVEDINVITATION = _descriptor.Descriptor(
  name='ReceivedInvitation',
  full_name='bnet.protocol.friends.ReceivedInvitation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.friends.ReceivedInvitation.id', index=0,
      number=1, type=6, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inviter_identity', full_name='bnet.protocol.friends.ReceivedInvitation.inviter_identity', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invitee_identity', full_name='bnet.protocol.friends.ReceivedInvitation.invitee_identity', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inviter_name', full_name='bnet.protocol.friends.ReceivedInvitation.inviter_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invitee_name', full_name='bnet.protocol.friends.ReceivedInvitation.invitee_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invitation_message', full_name='bnet.protocol.friends.ReceivedInvitation.invitation_message', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='bnet.protocol.friends.ReceivedInvitation.creation_time', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration_time', full_name='bnet.protocol.friends.ReceivedInvitation.expiration_time', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=347,
)


_FRIEND = _descriptor.Descriptor(
  name='Friend',
  full_name='bnet.protocol.friends.Friend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.friends.Friend.id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.friends.Friend.attribute', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.Friend.role', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='privileges', full_name='bnet.protocol.friends.Friend.privileges', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes_epoch', full_name='bnet.protocol.friends.Friend.attributes_epoch', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_tag', full_name='bnet.protocol.friends.Friend.battle_tag', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=537,
)


_FRIENDINVITATION = _descriptor.Descriptor(
  name='FriendInvitation',
  full_name='bnet.protocol.friends.FriendInvitation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_received', full_name='bnet.protocol.friends.FriendInvitation.first_received', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.FriendInvitation.role', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=606,
)


_FRIENDINVITATIONPARAMS = _descriptor.Descriptor(
  name='FriendInvitationParams',
  full_name='bnet.protocol.friends.FriendInvitationParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_email', full_name='bnet.protocol.friends.FriendInvitationParams.target_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_battle_tag', full_name='bnet.protocol.friends.FriendInvitationParams.target_battle_tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inviter_battle_tag', full_name='bnet.protocol.friends.FriendInvitationParams.inviter_battle_tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inviter_full_name', full_name='bnet.protocol.friends.FriendInvitationParams.inviter_full_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invitee_display_name', full_name='bnet.protocol.friends.FriendInvitationParams.invitee_display_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role', full_name='bnet.protocol.friends.FriendInvitationParams.role', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=785,
)

_RECEIVEDINVITATION.fields_by_name['inviter_identity'].message_type = bnet.entity_pb2._IDENTITY
_RECEIVEDINVITATION.fields_by_name['invitee_identity'].message_type = bnet.entity_pb2._IDENTITY
_FRIEND.fields_by_name['id'].message_type = bnet.entity_pb2._ENTITYID
_FRIEND.fields_by_name['attribute'].message_type = bnet.attribute_pb2._ATTRIBUTE
DESCRIPTOR.message_types_by_name['ReceivedInvitation'] = _RECEIVEDINVITATION
DESCRIPTOR.message_types_by_name['Friend'] = _FRIEND
DESCRIPTOR.message_types_by_name['FriendInvitation'] = _FRIENDINVITATION
DESCRIPTOR.message_types_by_name['FriendInvitationParams'] = _FRIENDINVITATIONPARAMS

ReceivedInvitation = _reflection.GeneratedProtocolMessageType('ReceivedInvitation', (_message.Message,), dict(
  DESCRIPTOR = _RECEIVEDINVITATION,
  __module__ = 'bnet.friends_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.ReceivedInvitation)
  ))
_sym_db.RegisterMessage(ReceivedInvitation)

Friend = _reflection.GeneratedProtocolMessageType('Friend', (_message.Message,), dict(
  DESCRIPTOR = _FRIEND,
  __module__ = 'bnet.friends_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.Friend)
  ))
_sym_db.RegisterMessage(Friend)

FriendInvitation = _reflection.GeneratedProtocolMessageType('FriendInvitation', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDINVITATION,
  __module__ = 'bnet.friends_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.FriendInvitation)
  ))
_sym_db.RegisterMessage(FriendInvitation)

FriendInvitationParams = _reflection.GeneratedProtocolMessageType('FriendInvitationParams', (_message.Message,), dict(
  DESCRIPTOR = _FRIENDINVITATIONPARAMS,
  __module__ = 'bnet.friends_types_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.friends.FriendInvitationParams)
  ))
_sym_db.RegisterMessage(FriendInvitationParams)


_FRIEND.fields_by_name['role'].has_options = True
_FRIEND.fields_by_name['role']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_FRIENDINVITATION.fields_by_name['role'].has_options = True
_FRIENDINVITATION.fields_by_name['role']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_FRIENDINVITATIONPARAMS.fields_by_name['role'].has_options = True
_FRIENDINVITATIONPARAMS.fields_by_name['role']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)