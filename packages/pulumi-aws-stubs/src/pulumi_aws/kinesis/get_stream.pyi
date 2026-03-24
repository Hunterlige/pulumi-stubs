import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetStreamResult",
    "AwaitableGetStreamResult",
    "get_stream",
    "get_stream_output",
]

@pulumi.output_type
class GetStreamResult:
    def __init__(
        __self__,
        arn=...,
        closed_shards=...,
        creation_timestamp=...,
        encryption_type=...,
        id=...,
        kms_key_id=...,
        max_record_size_in_kib=...,
        name=...,
        open_shards=...,
        region=...,
        retention_period=...,
        shard_level_metrics=...,
        status=...,
        stream_mode_details=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="closedShards")
    def closed_shards(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxRecordSizeInKib")
    def max_record_size_in_kib(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="openShards")
    def open_shards(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="shardLevelMetrics")
    def shard_level_metrics(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="streamModeDetails")
    def stream_mode_details(
        self,
    ) -> Sequence[outputs.GetStreamStreamModeDetailResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetStreamResult(GetStreamResult):
    def __await__(self): ...

def get_stream(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetStreamResult: ...
def get_stream_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetStreamResult]: ...
