import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GroupPoliciesExclusiveArgs", "GroupPoliciesExclusive"]

@pulumi.input_type
class GroupPoliciesExclusiveArgs:
    def __init__(
        __self__,
        *,
        group_name: pulumi.Input[_builtins.str],
        policy_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[_builtins.str]: ...
    @group_name.setter
    def group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @policy_names.setter
    def policy_names(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

@pulumi.input_type
class _GroupPoliciesExclusiveState:
    def __init__(
        __self__,
        *,
        group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyNames")
    def policy_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @policy_names.setter
    def policy_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class GroupPoliciesExclusive(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GroupPoliciesExclusiveArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> GroupPoliciesExclusive: ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
