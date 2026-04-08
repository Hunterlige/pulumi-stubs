import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DependencyOfRelationshipPropertiesArgs",
    "DependencyOfRelationshipPropertiesArgsDict",
    "ServiceGroupMemberRelationshipPropertiesArgs",
    "ServiceGroupMemberRelationshipPropertiesArgsDict",
]

class DependencyOfRelationshipPropertiesArgsDict(TypedDict):
    target_id: pulumi.Input[_builtins.str]
    target_tenant: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DependencyOfRelationshipPropertiesArgs:
    def __init__(
        __self__,
        *,
        target_id: pulumi.Input[_builtins.str],
        target_tenant: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_id.setter
    def target_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetTenant")
    def target_tenant(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_tenant.setter
    def target_tenant(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceGroupMemberRelationshipPropertiesArgsDict(TypedDict):
    target_id: pulumi.Input[_builtins.str]
    target_tenant: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceGroupMemberRelationshipPropertiesArgs:
    def __init__(
        __self__,
        *,
        target_id: pulumi.Input[_builtins.str],
        target_tenant: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Input[_builtins.str]: ...
    @target_id.setter
    def target_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="targetTenant")
    def target_tenant(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_tenant.setter
    def target_tenant(self, value: Optional[pulumi.Input[_builtins.str]]): ...
