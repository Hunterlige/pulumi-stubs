import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDedicatedHostResult",
    "AwaitableGetDedicatedHostResult",
    "get_dedicated_host",
    "get_dedicated_host_output",
]

@pulumi.output_type
class GetDedicatedHostResult:
    def __init__(
        __self__,
        arn=...,
        asset_id=...,
        auto_placement=...,
        availability_zone=...,
        cores=...,
        filters=...,
        host_id=...,
        host_recovery=...,
        id=...,
        instance_family=...,
        instance_type=...,
        outpost_arn=...,
        owner_id=...,
        region=...,
        sockets=...,
        tags=...,
        total_vcpus=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="assetId")
    def asset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="autoPlacement")
    def auto_placement(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cores(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetDedicatedHostFilterResult]]: ...
    @_builtins.property
    @pulumi.getter(name="hostId")
    def host_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostRecovery")
    def host_recovery(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceFamily")
    def instance_family(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sockets(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="totalVcpus")
    def total_vcpus(self) -> _builtins.int: ...

class AwaitableGetDedicatedHostResult(GetDedicatedHostResult):
    def __await__(self): ...

def get_dedicated_host(
    filters: Optional[
        Sequence[Union[GetDedicatedHostFilterArgs, GetDedicatedHostFilterArgsDict]]
    ] = ...,
    host_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDedicatedHostResult: ...
def get_dedicated_host_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[GetDedicatedHostFilterArgs, GetDedicatedHostFilterArgsDict]
                ]
            ]
        ]
    ] = ...,
    host_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDedicatedHostResult]: ...
