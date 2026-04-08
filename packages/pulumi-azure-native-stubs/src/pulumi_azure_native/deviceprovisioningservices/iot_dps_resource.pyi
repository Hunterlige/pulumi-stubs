import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IotDpsResourceArgs", "IotDpsResource"]

@pulumi.input_type
class IotDpsResourceArgs:
    def __init__(
        __self__,
        *,
        properties: pulumi.Input[IotDpsPropertiesDescriptionArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[IotDpsSkuInfoArgs],
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioning_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resourcegroup: Optional[pulumi.Input[_builtins.str]] = ...,
        subscriptionid: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[IotDpsPropertiesDescriptionArgs]: ...
    @properties.setter
    def properties(self, value: pulumi.Input[IotDpsPropertiesDescriptionArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[IotDpsSkuInfoArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[IotDpsSkuInfoArgs]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="provisioningServiceName")
    def provisioning_service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_service_name.setter
    def provisioning_service_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def resourcegroup(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resourcegroup.setter
    def resourcegroup(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subscriptionid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscriptionid.setter
    def subscriptionid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class IotDpsResource(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[
                Union[
                    IotDpsPropertiesDescriptionArgs, IotDpsPropertiesDescriptionArgsDict
                ]
            ]
        ] = ...,
        provisioning_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resourcegroup: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[
            pulumi.Input[Union[IotDpsSkuInfoArgs, IotDpsSkuInfoArgsDict]]
        ] = ...,
        subscriptionid: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IotDpsResourceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> IotDpsResource: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> pulumi.Output[outputs.IotDpsPropertiesDescriptionResponse]: ...
    @_builtins.property
    @pulumi.getter
    def resourcegroup(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.IotDpsSkuInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def subscriptionid(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
