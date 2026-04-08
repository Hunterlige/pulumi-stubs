import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccessPolicyArgs", "AccessPolicy"]

@pulumi.input_type
class AccessPolicyArgs:
    def __init__(
        __self__,
        *,
        policy: pulumi.Input[AccessPolicyEntryArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        vault_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Input[AccessPolicyEntryArgs]: ...
    @policy.setter
    def policy(self, value: pulumi.Input[AccessPolicyEntryArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Input[_builtins.str]: ...
    @vault_name.setter
    def vault_name(self, value: pulumi.Input[_builtins.str]): ...

@pulumi.type_token("azure-native:keyvault:AccessPolicy")
class AccessPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        policy: Optional[
            pulumi.Input[Union[AccessPolicyEntryArgs, AccessPolicyEntryArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        vault_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccessPolicyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AccessPolicy: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[outputs.AccessPolicyEntry]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
