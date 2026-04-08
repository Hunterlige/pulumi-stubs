import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagedPrivateEndpointInitArgs", "ManagedPrivateEndpoint"]

@pulumi.input_type
class ManagedPrivateEndpointInitArgs:
    def __init__(
        __self__,
        *,
        factory_name: pulumi.Input[_builtins.str],
        managed_virtual_network_name: pulumi.Input[_builtins.str],
        properties: pulumi.Input[ManagedPrivateEndpointArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        managed_private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[_builtins.str]: ...
    @factory_name.setter
    def factory_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedVirtualNetworkName")
    def managed_virtual_network_name(self) -> pulumi.Input[_builtins.str]: ...
    @managed_virtual_network_name.setter
    def managed_virtual_network_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[ManagedPrivateEndpointArgs]: ...
    @properties.setter
    def properties(self, value: pulumi.Input[ManagedPrivateEndpointArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="managedPrivateEndpointName")
    def managed_private_endpoint_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_private_endpoint_name.setter
    def managed_private_endpoint_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token("azure-native:datafactory:ManagedPrivateEndpoint")
class ManagedPrivateEndpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_private_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_virtual_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[ManagedPrivateEndpointArgs, ManagedPrivateEndpointArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedPrivateEndpointInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ManagedPrivateEndpoint: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.ManagedPrivateEndpointResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
