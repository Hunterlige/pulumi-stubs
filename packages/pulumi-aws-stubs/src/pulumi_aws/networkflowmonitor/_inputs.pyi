import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "MonitorLocalResourceArgs",
    "MonitorLocalResourceArgsDict",
    "MonitorRemoteResourceArgs",
    "MonitorRemoteResourceArgsDict",
    "MonitorTimeoutsArgs",
    "MonitorTimeoutsArgsDict",
    "ScopeTargetArgs",
    "ScopeTargetArgsDict",
    "ScopeTargetTargetIdentifierArgs",
    "ScopeTargetTargetIdentifierArgsDict",
    "ScopeTargetTargetIdentifierTargetIdArgs",
    "ScopeTargetTargetIdentifierTargetIdArgsDict",
    "ScopeTimeoutsArgs",
    "ScopeTimeoutsArgsDict",
]

class MonitorLocalResourceArgsDict(TypedDict):
    identifier: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class MonitorLocalResourceArgs:
    def __init__(
        __self__,
        *,
        identifier: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[_builtins.str]: ...
    @identifier.setter
    def identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class MonitorRemoteResourceArgsDict(TypedDict):
    identifier: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class MonitorRemoteResourceArgs:
    def __init__(
        __self__,
        *,
        identifier: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> pulumi.Input[_builtins.str]: ...
    @identifier.setter
    def identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class MonitorTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MonitorTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ScopeTargetArgsDict(TypedDict):
    region: pulumi.Input[_builtins.str]
    target_identifier: pulumi.Input[ScopeTargetTargetIdentifierArgsDict]
    ...

@pulumi.input_type
class ScopeTargetArgs:
    def __init__(
        __self__,
        *,
        region: pulumi.Input[_builtins.str],
        target_identifier: pulumi.Input[ScopeTargetTargetIdentifierArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetIdentifier")
    def target_identifier(self) -> pulumi.Input[ScopeTargetTargetIdentifierArgs]: ...
    @target_identifier.setter
    def target_identifier(
        self, value: pulumi.Input[ScopeTargetTargetIdentifierArgs]
    ): ...

class ScopeTargetTargetIdentifierArgsDict(TypedDict):
    target_id: pulumi.Input[ScopeTargetTargetIdentifierTargetIdArgsDict]
    target_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ScopeTargetTargetIdentifierArgs:
    def __init__(
        __self__,
        *,
        target_id: pulumi.Input[ScopeTargetTargetIdentifierTargetIdArgs],
        target_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Input[ScopeTargetTargetIdentifierTargetIdArgs]: ...
    @target_id.setter
    def target_id(
        self, value: pulumi.Input[ScopeTargetTargetIdentifierTargetIdArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Input[_builtins.str]: ...
    @target_type.setter
    def target_type(self, value: pulumi.Input[_builtins.str]): ...

class ScopeTargetTargetIdentifierTargetIdArgsDict(TypedDict):
    account_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ScopeTargetTargetIdentifierTargetIdArgs:
    def __init__(__self__, *, account_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[_builtins.str]: ...
    @account_id.setter
    def account_id(self, value: pulumi.Input[_builtins.str]): ...

class ScopeTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ScopeTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...
