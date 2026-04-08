import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GatewayArgs", "Gateway"]

@pulumi.input_type
class GatewayArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        service_name: pulumi.Input[_builtins.str],
        gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[GatewayPropertiesArgs]] = ...,
        sku: Optional[pulumi.Input[SkuArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway_name.setter
    def gateway_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[GatewayPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[GatewayPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SkuArgs]]): ...

@pulumi.type_token("azure-native:appplatform:Gateway")
class Gateway(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        gateway_name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Union[GatewayPropertiesArgs, GatewayPropertiesArgsDict]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GatewayArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Gateway: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.GatewayPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SkuResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
