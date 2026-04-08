import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccountCapabilityHostArgs", "AccountCapabilityHost"]

@pulumi.input_type
class AccountCapabilityHostArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        capability_host_properties: pulumi.Input[CapabilityHostArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        capability_host_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="capabilityHostProperties")
    def capability_host_properties(self) -> pulumi.Input[CapabilityHostArgs]: ...
    @capability_host_properties.setter
    def capability_host_properties(self, value: pulumi.Input[CapabilityHostArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="capabilityHostName")
    def capability_host_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @capability_host_name.setter
    def capability_host_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class AccountCapabilityHost(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        capability_host_name: Optional[pulumi.Input[_builtins.str]] = ...,
        capability_host_properties: Optional[
            pulumi.Input[Union[CapabilityHostArgs, CapabilityHostArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccountCapabilityHostArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AccountCapabilityHost: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="capabilityHostProperties")
    def capability_host_properties(
        self,
    ) -> pulumi.Output[outputs.CapabilityHostResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
