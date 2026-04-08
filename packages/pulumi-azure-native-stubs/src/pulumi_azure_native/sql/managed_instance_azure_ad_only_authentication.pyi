import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ManagedInstanceAzureADOnlyAuthenticationArgs",
    "ManagedInstanceAzureADOnlyAuthentication",
]

@pulumi.input_type
class ManagedInstanceAzureADOnlyAuthenticationArgs:
    def __init__(
        __self__,
        *,
        azure_ad_only_authentication: pulumi.Input[_builtins.bool],
        managed_instance_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        authentication_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> pulumi.Input[_builtins.bool]: ...
    @azure_ad_only_authentication.setter
    def azure_ad_only_authentication(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authenticationName")
    def authentication_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authentication_name.setter
    def authentication_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ManagedInstanceAzureADOnlyAuthentication(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authentication_name: Optional[pulumi.Input[_builtins.str]] = ...,
        azure_ad_only_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
        managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedInstanceAzureADOnlyAuthenticationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ManagedInstanceAzureADOnlyAuthentication: ...
    @_builtins.property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
