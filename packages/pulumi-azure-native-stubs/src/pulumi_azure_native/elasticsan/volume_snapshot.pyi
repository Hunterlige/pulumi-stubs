import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["VolumeSnapshotArgs", "VolumeSnapshot"]

@pulumi.input_type
class VolumeSnapshotArgs:
    def __init__(
        __self__,
        *,
        creation_data: pulumi.Input[SnapshotCreationDataArgs],
        elastic_san_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        volume_group_name: pulumi.Input[_builtins.str],
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Input[SnapshotCreationDataArgs]: ...
    @creation_data.setter
    def creation_data(self, value: pulumi.Input[SnapshotCreationDataArgs]): ...
    @_builtins.property
    @pulumi.getter(name="elasticSanName")
    def elastic_san_name(self) -> pulumi.Input[_builtins.str]: ...
    @elastic_san_name.setter
    def elastic_san_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="volumeGroupName")
    def volume_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @volume_group_name.setter
    def volume_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:elasticsan:VolumeSnapshot")
class VolumeSnapshot(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        creation_data: Optional[
            pulumi.Input[Union[SnapshotCreationDataArgs, SnapshotCreationDataArgsDict]]
        ] = ...,
        elastic_san_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: VolumeSnapshotArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> VolumeSnapshot: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> pulumi.Output[outputs.SnapshotCreationDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceVolumeSizeGiB")
    def source_volume_size_gi_b(self) -> pulumi.Output[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Output[_builtins.str]: ...
