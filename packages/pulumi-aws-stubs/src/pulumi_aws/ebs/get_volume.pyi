import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVolumeResult",
    "AwaitableGetVolumeResult",
    "get_volume",
    "get_volume_output",
]

@pulumi.output_type
class GetVolumeResult:
    def __init__(
        __self__,
        arn=...,
        availability_zone=...,
        create_time=...,
        encrypted=...,
        filters=...,
        id=...,
        iops=...,
        kms_key_id=...,
        most_recent=...,
        multi_attach_enabled=...,
        outpost_arn=...,
        region=...,
        size=...,
        snapshot_id=...,
        tags=...,
        throughput=...,
        volume_id=...,
        volume_initialization_rate=...,
        volume_type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetVolumeFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iops(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="multiAttachEnabled")
    def multi_attach_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def throughput(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="volumeInitializationRate")
    def volume_initialization_rate(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> _builtins.str: ...

class AwaitableGetVolumeResult(GetVolumeResult):
    def __await__(self): ...

def get_volume(
    filters: Optional[
        Sequence[Union[GetVolumeFilterArgs, GetVolumeFilterArgsDict]]
    ] = ...,
    most_recent: Optional[_builtins.bool] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVolumeResult: ...
def get_volume_output(
    filters: Optional[
        pulumi.Input[
            Optional[Sequence[Union[GetVolumeFilterArgs, GetVolumeFilterArgsDict]]]
        ]
    ] = ...,
    most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVolumeResult]: ...
