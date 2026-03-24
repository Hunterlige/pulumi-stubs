import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RolePoliciesExclusiveArgs", "RolePoliciesExclusive"]

@pulumi.input_type
class RolePoliciesExclusiveArgs:
    def __init__(
        __self__,
        *,
        policy_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        role_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @policy_names.setter
    def policy_names(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Input[_builtins.str]: ...
    @role_name.setter
    def role_name(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.input_type
class _RolePoliciesExclusiveState:
    def __init__(
        __self__,
        *,
        policy_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        role_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyNames")
    def policy_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @policy_names.setter
    def policy_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class RolePoliciesExclusive(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        policy_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        role_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RolePoliciesExclusiveArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        policy_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        role_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RolePoliciesExclusive: ...
    @_builtins.property
    @pulumi.getter(name="policyNames")
    def policy_names(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[_builtins.str]: ...
