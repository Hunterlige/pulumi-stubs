import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PolicyArgs", "Policy"]

@pulumi.input_type
class PolicyArgs:
    def __init__(
        __self__,
        *,
        customer: pulumi.Input[_builtins.str],
        policy_query: pulumi.Input[PolicyPolicyQueryArgs],
        setting: pulumi.Input[PolicySettingArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def customer(self) -> pulumi.Input[_builtins.str]: ...
    @customer.setter
    def customer(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="policyQuery")
    def policy_query(self) -> pulumi.Input[PolicyPolicyQueryArgs]: ...
    @policy_query.setter
    def policy_query(self, value: pulumi.Input[PolicyPolicyQueryArgs]): ...
    @_builtins.property
    @pulumi.getter
    def setting(self) -> pulumi.Input[PolicySettingArgs]: ...
    @setting.setter
    def setting(self, value: pulumi.Input[PolicySettingArgs]): ...

@pulumi.input_type
class _PolicyState:
    def __init__(
        __self__,
        *,
        customer: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_query: Optional[pulumi.Input[PolicyPolicyQueryArgs]] = ...,
        setting: Optional[pulumi.Input[PolicySettingArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def customer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer.setter
    def customer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="policyQuery")
    def policy_query(self) -> Optional[pulumi.Input[PolicyPolicyQueryArgs]]: ...
    @policy_query.setter
    def policy_query(self, value: Optional[pulumi.Input[PolicyPolicyQueryArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def setting(self) -> Optional[pulumi.Input[PolicySettingArgs]]: ...
    @setting.setter
    def setting(self, value: Optional[pulumi.Input[PolicySettingArgs]]): ...

@pulumi.type_token("gcp:cloudidentity/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        customer: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_query: Optional[
            pulumi.Input[Union[PolicyPolicyQueryArgs, PolicyPolicyQueryArgsDict]]
        ] = ...,
        setting: Optional[
            pulumi.Input[Union[PolicySettingArgs, PolicySettingArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        customer: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy_query: Optional[
            pulumi.Input[Union[PolicyPolicyQueryArgs, PolicyPolicyQueryArgsDict]]
        ] = ...,
        setting: Optional[
            pulumi.Input[Union[PolicySettingArgs, PolicySettingArgsDict]]
        ] = ...,
    ) -> Policy: ...
    @_builtins.property
    @pulumi.getter
    def customer(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyQuery")
    def policy_query(self) -> pulumi.Output[outputs.PolicyPolicyQuery]: ...
    @_builtins.property
    @pulumi.getter
    def setting(self) -> pulumi.Output[outputs.PolicySetting]: ...
