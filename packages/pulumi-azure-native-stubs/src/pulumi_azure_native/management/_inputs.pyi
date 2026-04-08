import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CreateManagementGroupDetailsArgs",
    "CreateManagementGroupDetailsArgsDict",
    "CreateParentGroupInfoArgs",
    "CreateParentGroupInfoArgsDict",
    "ParentServiceGroupPropertiesArgs",
    "ParentServiceGroupPropertiesArgsDict",
    "ServiceGroupPropertiesArgs",
    "ServiceGroupPropertiesArgsDict",
]

class CreateManagementGroupDetailsArgsDict(TypedDict):
    parent: NotRequired[pulumi.Input[CreateParentGroupInfoArgsDict]]

@pulumi.input_type
class CreateManagementGroupDetailsArgs:
    def __init__(
        __self__, *, parent: Optional[pulumi.Input[CreateParentGroupInfoArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[CreateParentGroupInfoArgs]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[CreateParentGroupInfoArgs]]): ...

class CreateParentGroupInfoArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CreateParentGroupInfoArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ParentServiceGroupPropertiesArgsDict(TypedDict):
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ParentServiceGroupPropertiesArgs:
    def __init__(
        __self__, *, resource_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceGroupPropertiesArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    parent: NotRequired[pulumi.Input[ParentServiceGroupPropertiesArgsDict]]

@pulumi.input_type
class ServiceGroupPropertiesArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[ParentServiceGroupPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[ParentServiceGroupPropertiesArgs]]: ...
    @parent.setter
    def parent(
        self, value: Optional[pulumi.Input[ParentServiceGroupPropertiesArgs]]
    ): ...
