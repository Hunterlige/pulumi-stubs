import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VirtualHardDiskArgs", "VirtualHardDisk"]

@pulumi.input_type
class VirtualHardDiskArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        block_size_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        container_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_from_local: Optional[pulumi.Input[_builtins.bool]] = ...,
        disk_file_format: Optional[
            pulumi.Input[Union[_builtins.str, DiskFileFormat]]
        ] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.float]] = ...,
        download_url: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic: Optional[pulumi.Input[_builtins.bool]] = ...,
        extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ...,
        hyper_v_generation: Optional[
            pulumi.Input[Union[_builtins.str, HyperVGeneration]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logical_sector_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        physical_sector_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_hard_disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @block_size_bytes.setter
    def block_size_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="containerId")
    def container_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_id.setter
    def container_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createFromLocal")
    def create_from_local(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_from_local.setter
    def create_from_local(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="diskFileFormat")
    def disk_file_format(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DiskFileFormat]]]: ...
    @disk_file_format.setter
    def disk_file_format(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DiskFileFormat]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="downloadUrl")
    def download_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @download_url.setter
    def download_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dynamic(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dynamic.setter
    def dynamic(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]: ...
    @extended_location.setter
    def extended_location(
        self, value: Optional[pulumi.Input[ExtendedLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HyperVGeneration]]]: ...
    @hyper_v_generation.setter
    def hyper_v_generation(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HyperVGeneration]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logicalSectorBytes")
    def logical_sector_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @logical_sector_bytes.setter
    def logical_sector_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="physicalSectorBytes")
    def physical_sector_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @physical_sector_bytes.setter
    def physical_sector_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="virtualHardDiskName")
    def virtual_hard_disk_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @virtual_hard_disk_name.setter
    def virtual_hard_disk_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:azurestackhci:VirtualHardDisk")
class VirtualHardDisk(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        block_size_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        container_id: Optional[pulumi.Input[_builtins.str]] = ...,
        create_from_local: Optional[pulumi.Input[_builtins.bool]] = ...,
        disk_file_format: Optional[
            pulumi.Input[Union[_builtins.str, DiskFileFormat]]
        ] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.float]] = ...,
        download_url: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic: Optional[pulumi.Input[_builtins.bool]] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        hyper_v_generation: Optional[
            pulumi.Input[Union[_builtins.str, HyperVGeneration]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logical_sector_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        physical_sector_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        virtual_hard_disk_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VirtualHardDiskArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VirtualHardDisk: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blockSizeBytes")
    def block_size_bytes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="containerId")
    def container_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createFromLocal")
    def create_from_local(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="diskFileFormat")
    def disk_file_format(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter(name="downloadUrl")
    def download_url(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def dynamic(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(
        self,
    ) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logicalSectorBytes")
    def logical_sector_bytes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="physicalSectorBytes")
    def physical_sector_bytes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.VirtualHardDiskStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
