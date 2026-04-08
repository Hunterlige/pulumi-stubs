import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualHubIpConfigurationArgs", "VirtualHubIpConfiguration"]

@pulumi.input_type
class VirtualHubIpConfigurationArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        virtual_hub_name: pulumi.Input[_builtins.str],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_allocation_method: Optional[
            pulumi.Input[Union[_builtins.str, IPAllocationMethod]]
        ] = ...,
        public_ip_address: Optional[pulumi.Input[PublicIPAddressArgs]] = ...,
        subnet: Optional[pulumi.Input[SubnetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_hub_name.setter
    def virtual_hub_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipConfigName")
    def ip_config_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_config_name.setter
    def ip_config_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateIPAllocationMethod")
    def private_ip_allocation_method(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IPAllocationMethod]]]: ...
    @private_ip_allocation_method.setter
    def private_ip_allocation_method(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IPAllocationMethod]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddress")
    def public_ip_address(self) -> Optional[pulumi.Input[PublicIPAddressArgs]]: ...
    @public_ip_address.setter
    def public_ip_address(self, value: Optional[pulumi.Input[PublicIPAddressArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[SubnetArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[SubnetArgs]]): ...

@pulumi.type_token("azure-native:network:VirtualHubIpConfiguration")
class VirtualHubIpConfiguration(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_config_name: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        private_ip_allocation_method: Optional[
            pulumi.Input[Union[_builtins.str, IPAllocationMethod]]
        ] = ...,
        public_ip_address: Optional[
            pulumi.Input[Union[PublicIPAddressArgs, PublicIPAddressArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet: Optional[pulumi.Input[Union[SubnetArgs, SubnetArgsDict]]] = ...,
        virtual_hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualHubIpConfigurationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualHubIpConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateIPAllocationMethod")
    def private_ip_allocation_method(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIPAddress")
    def public_ip_address(
        self,
    ) -> pulumi.Output[Optional[outputs.PublicIPAddressResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional[outputs.SubnetResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
