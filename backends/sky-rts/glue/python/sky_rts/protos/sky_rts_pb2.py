# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sky-rts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sky-rts.proto',
  package='scaii.rts',
  syntax='proto2',
  serialized_pb=_b('\n\rsky-rts.proto\x12\tscaii.rts\"T\n\nActionList\x12&\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\x15.scaii.rts.UnitAction\x12\x0c\n\x04skip\x18\x02 \x01(\x08\x12\x10\n\x08skip_lua\x18\x03 \x01(\t\"{\n\nUnitAction\x12\x0f\n\x07unit_id\x18\x01 \x02(\x04\x12$\n\x07move_to\x18\x02 \x01(\x0b\x32\x11.scaii.rts.MoveToH\x00\x12,\n\x0b\x61ttack_unit\x18\x03 \x01(\x0b\x32\x15.scaii.rts.AttackUnitH\x00\x42\x08\n\x06\x61\x63tion\"\x1b\n\x03Pos\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\"%\n\x06MoveTo\x12\x1b\n\x03pos\x18\x01 \x02(\x0b\x32\x0e.scaii.rts.Pos\"\x1f\n\nAttackUnit\x12\x11\n\ttarget_id\x18\x01 \x02(\r\"V\n\x0bStateUpdate\x12\x1e\n\x05units\x18\x01 \x03(\x0b\x32\x0f.scaii.rts.Unit\x12\'\n\nunit_types\x18\x02 \x03(\x0b\x32\x13.scaii.rts.UnitType\"P\n\x08UnitType\x12\x14\n\x0cunit_type_id\x18\x01 \x02(\x04\x12\x0e\n\x06max_hp\x18\x02 \x01(\x01\x12\x0f\n\x07movable\x18\x03 \x01(\x01\x12\r\n\x03tag\x18\x04 \x01(\t:\x00\"x\n\x04Unit\x12\n\n\x02id\x18\x01 \x02(\r\x12\x10\n\x08owner_id\x18\x02 \x01(\x04\x12\x14\n\x0cunit_type_id\x18\x03 \x01(\x04\x12 \n\x03pos\x18\x04 \x01(\x0b\x32\x13.scaii.rts.DeltaPos\x12\n\n\x02hp\x18\x05 \x01(\x01\x12\x0e\n\x06\x64\x65lete\x18\n \x02(\x08\" \n\x08\x44\x65ltaPos\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\"/\n\x06\x43onfig\x12%\n\x08scenario\x18\x01 \x01(\x0b\x32\x13.scaii.rts.Scenario\"\x14\n\x04Seed\x12\x0c\n\x04seed\x18\x01 \x03(\x04\"\x18\n\x08Scenario\x12\x0c\n\x04path\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ACTIONLIST = _descriptor.Descriptor(
  name='ActionList',
  full_name='scaii.rts.ActionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actions', full_name='scaii.rts.ActionList.actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skip', full_name='scaii.rts.ActionList.skip', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='skip_lua', full_name='scaii.rts.ActionList.skip_lua', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=112,
)


_UNITACTION = _descriptor.Descriptor(
  name='UnitAction',
  full_name='scaii.rts.UnitAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='scaii.rts.UnitAction.unit_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_to', full_name='scaii.rts.UnitAction.move_to', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attack_unit', full_name='scaii.rts.UnitAction.attack_unit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='action', full_name='scaii.rts.UnitAction.action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=114,
  serialized_end=237,
)


_POS = _descriptor.Descriptor(
  name='Pos',
  full_name='scaii.rts.Pos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='scaii.rts.Pos.x', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='scaii.rts.Pos.y', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=266,
)


_MOVETO = _descriptor.Descriptor(
  name='MoveTo',
  full_name='scaii.rts.MoveTo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='scaii.rts.MoveTo.pos', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=305,
)


_ATTACKUNIT = _descriptor.Descriptor(
  name='AttackUnit',
  full_name='scaii.rts.AttackUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_id', full_name='scaii.rts.AttackUnit.target_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=338,
)


_STATEUPDATE = _descriptor.Descriptor(
  name='StateUpdate',
  full_name='scaii.rts.StateUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='units', full_name='scaii.rts.StateUpdate.units', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_types', full_name='scaii.rts.StateUpdate.unit_types', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=426,
)


_UNITTYPE = _descriptor.Descriptor(
  name='UnitType',
  full_name='scaii.rts.UnitType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit_type_id', full_name='scaii.rts.UnitType.unit_type_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_hp', full_name='scaii.rts.UnitType.max_hp', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='movable', full_name='scaii.rts.UnitType.movable', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tag', full_name='scaii.rts.UnitType.tag', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=508,
)


_UNIT = _descriptor.Descriptor(
  name='Unit',
  full_name='scaii.rts.Unit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='scaii.rts.Unit.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner_id', full_name='scaii.rts.Unit.owner_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_type_id', full_name='scaii.rts.Unit.unit_type_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos', full_name='scaii.rts.Unit.pos', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp', full_name='scaii.rts.Unit.hp', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete', full_name='scaii.rts.Unit.delete', index=5,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=510,
  serialized_end=630,
)


_DELTAPOS = _descriptor.Descriptor(
  name='DeltaPos',
  full_name='scaii.rts.DeltaPos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='scaii.rts.DeltaPos.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='scaii.rts.DeltaPos.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=632,
  serialized_end=664,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='scaii.rts.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scenario', full_name='scaii.rts.Config.scenario', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=666,
  serialized_end=713,
)


_SEED = _descriptor.Descriptor(
  name='Seed',
  full_name='scaii.rts.Seed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seed', full_name='scaii.rts.Seed.seed', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=715,
  serialized_end=735,
)


_SCENARIO = _descriptor.Descriptor(
  name='Scenario',
  full_name='scaii.rts.Scenario',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='scaii.rts.Scenario.path', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=737,
  serialized_end=761,
)

_ACTIONLIST.fields_by_name['actions'].message_type = _UNITACTION
_UNITACTION.fields_by_name['move_to'].message_type = _MOVETO
_UNITACTION.fields_by_name['attack_unit'].message_type = _ATTACKUNIT
_UNITACTION.oneofs_by_name['action'].fields.append(
  _UNITACTION.fields_by_name['move_to'])
_UNITACTION.fields_by_name['move_to'].containing_oneof = _UNITACTION.oneofs_by_name['action']
_UNITACTION.oneofs_by_name['action'].fields.append(
  _UNITACTION.fields_by_name['attack_unit'])
_UNITACTION.fields_by_name['attack_unit'].containing_oneof = _UNITACTION.oneofs_by_name['action']
_MOVETO.fields_by_name['pos'].message_type = _POS
_STATEUPDATE.fields_by_name['units'].message_type = _UNIT
_STATEUPDATE.fields_by_name['unit_types'].message_type = _UNITTYPE
_UNIT.fields_by_name['pos'].message_type = _DELTAPOS
_CONFIG.fields_by_name['scenario'].message_type = _SCENARIO
DESCRIPTOR.message_types_by_name['ActionList'] = _ACTIONLIST
DESCRIPTOR.message_types_by_name['UnitAction'] = _UNITACTION
DESCRIPTOR.message_types_by_name['Pos'] = _POS
DESCRIPTOR.message_types_by_name['MoveTo'] = _MOVETO
DESCRIPTOR.message_types_by_name['AttackUnit'] = _ATTACKUNIT
DESCRIPTOR.message_types_by_name['StateUpdate'] = _STATEUPDATE
DESCRIPTOR.message_types_by_name['UnitType'] = _UNITTYPE
DESCRIPTOR.message_types_by_name['Unit'] = _UNIT
DESCRIPTOR.message_types_by_name['DeltaPos'] = _DELTAPOS
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['Seed'] = _SEED
DESCRIPTOR.message_types_by_name['Scenario'] = _SCENARIO

ActionList = _reflection.GeneratedProtocolMessageType('ActionList', (_message.Message,), dict(
  DESCRIPTOR = _ACTIONLIST,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.ActionList)
  ))
_sym_db.RegisterMessage(ActionList)

UnitAction = _reflection.GeneratedProtocolMessageType('UnitAction', (_message.Message,), dict(
  DESCRIPTOR = _UNITACTION,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.UnitAction)
  ))
_sym_db.RegisterMessage(UnitAction)

Pos = _reflection.GeneratedProtocolMessageType('Pos', (_message.Message,), dict(
  DESCRIPTOR = _POS,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.Pos)
  ))
_sym_db.RegisterMessage(Pos)

MoveTo = _reflection.GeneratedProtocolMessageType('MoveTo', (_message.Message,), dict(
  DESCRIPTOR = _MOVETO,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.MoveTo)
  ))
_sym_db.RegisterMessage(MoveTo)

AttackUnit = _reflection.GeneratedProtocolMessageType('AttackUnit', (_message.Message,), dict(
  DESCRIPTOR = _ATTACKUNIT,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.AttackUnit)
  ))
_sym_db.RegisterMessage(AttackUnit)

StateUpdate = _reflection.GeneratedProtocolMessageType('StateUpdate', (_message.Message,), dict(
  DESCRIPTOR = _STATEUPDATE,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.StateUpdate)
  ))
_sym_db.RegisterMessage(StateUpdate)

UnitType = _reflection.GeneratedProtocolMessageType('UnitType', (_message.Message,), dict(
  DESCRIPTOR = _UNITTYPE,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.UnitType)
  ))
_sym_db.RegisterMessage(UnitType)

Unit = _reflection.GeneratedProtocolMessageType('Unit', (_message.Message,), dict(
  DESCRIPTOR = _UNIT,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.Unit)
  ))
_sym_db.RegisterMessage(Unit)

DeltaPos = _reflection.GeneratedProtocolMessageType('DeltaPos', (_message.Message,), dict(
  DESCRIPTOR = _DELTAPOS,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.DeltaPos)
  ))
_sym_db.RegisterMessage(DeltaPos)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.Config)
  ))
_sym_db.RegisterMessage(Config)

Seed = _reflection.GeneratedProtocolMessageType('Seed', (_message.Message,), dict(
  DESCRIPTOR = _SEED,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.Seed)
  ))
_sym_db.RegisterMessage(Seed)

Scenario = _reflection.GeneratedProtocolMessageType('Scenario', (_message.Message,), dict(
  DESCRIPTOR = _SCENARIO,
  __module__ = 'sky_rts_pb2'
  # @@protoc_insertion_point(class_scope:scaii.rts.Scenario)
  ))
_sym_db.RegisterMessage(Scenario)


# @@protoc_insertion_point(module_scope)
