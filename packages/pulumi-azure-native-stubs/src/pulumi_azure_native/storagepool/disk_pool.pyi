import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DiskPoolArgs", "DiskPool"]

@pulumi.input_type
class DiskPoolArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[SkuArgs],
        subnet_id: pulumi.Input[_builtins.str],
        additional_capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        disk_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disks: Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by_extended: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[SkuArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_capabilities.setter
    def additional_capabilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskPoolName")
    def disk_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_pool_name.setter
    def disk_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]]: ...
    @disks.setter
    def disks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DiskArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by.setter
    def managed_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @managed_by_extended.setter
    def managed_by_extended(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:storagepool:DiskPool")
class DiskPool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        disk_pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[DiskArgs, DiskArgsDict]]]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by_extended: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DiskPoolArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DiskPool: ...
    @_builtins.property
    @pulumi.getter(name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def disks(self) -> pulumi.Output[Optional[Sequence[outputs.DiskResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemMetadataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
