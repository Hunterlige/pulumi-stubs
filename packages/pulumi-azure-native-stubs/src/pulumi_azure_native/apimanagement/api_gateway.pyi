import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ApiGatewayArgs", "ApiGateway"]

@pulumi.input_type
class ApiGatewayArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[ApiManagementGatewaySkuPropertiesArgs],
        backend: Optional[pulumi.Input[BackendConfigurationArgs]] = ...,
        gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_network_type: Optional[
            pulumi.Input[Union[_builtins.str, VirtualNetworkType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[ApiManagementGatewaySkuPropertiesArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[ApiManagementGatewaySkuPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter
    def backend(self) -> Optional[pulumi.Input[BackendConfigurationArgs]]: ...
    @backend.setter
    def backend(self, value: Optional[pulumi.Input[BackendConfigurationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_name.setter
    def gateway_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkType]]]: ...
    @virtual_network_type.setter
    def virtual_network_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VirtualNetworkType]]]
    ): ...

@pulumi.type_token("azure-native:apimanagement:ApiGateway")
class ApiGateway(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        backend: Optional[
            pulumi.Input[Union[BackendConfigurationArgs, BackendConfigurationArgsDict]]
        ] = ...,
        gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[
            pulumi.Input[
                Union[
                    ApiManagementGatewaySkuPropertiesArgs,
                    ApiManagementGatewaySkuPropertiesArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_network_type: Optional[
            pulumi.Input[Union[_builtins.str, VirtualNetworkType]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ApiGatewayArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ApiGateway: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def backend(
        self,
    ) -> pulumi.Output[Optional[outputs.BackendConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="configurationApi")
    def configuration_api(
        self,
    ) -> pulumi.Output[Optional[outputs.GatewayConfigurationApiResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="createdAtUtc")
    def created_at_utc(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def frontend(
        self,
    ) -> pulumi.Output[Optional[outputs.FrontendConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(
        self,
    ) -> pulumi.Output[outputs.ApiManagementGatewaySkuPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="targetProvisioningState")
    def target_provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkType")
    def virtual_network_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
