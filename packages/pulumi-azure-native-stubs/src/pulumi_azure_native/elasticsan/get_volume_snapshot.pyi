import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVolumeSnapshotResult",
    "AwaitableGetVolumeSnapshotResult",
    "get_volume_snapshot",
    "get_volume_snapshot_output",
]

@pulumi.output_type
class GetVolumeSnapshotResult:
    def __init__(
        __self__,
        azure_api_version=...,
        creation_data=...,
        id=...,
        name=...,
        provisioning_state=...,
        source_volume_size_gi_b=...,
        system_data=...,
        type=...,
        volume_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> outputs.SnapshotCreationDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceVolumeSizeGiB")
    def source_volume_size_gi_b(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> _builtins.str: ...

class AwaitableGetVolumeSnapshotResult(GetVolumeSnapshotResult):
    def __await__(self): ...

def get_volume_snapshot(
    elastic_san_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    snapshot_name: Optional[_builtins.str] = ...,
    volume_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVolumeSnapshotResult: ...
def get_volume_snapshot_output(
    elastic_san_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
    volume_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVolumeSnapshotResult]: ...
