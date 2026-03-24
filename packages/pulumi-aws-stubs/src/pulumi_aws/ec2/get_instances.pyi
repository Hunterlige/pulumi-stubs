import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInstancesResult",
    "AwaitableGetInstancesResult",
    "get_instances",
    "get_instances_output",
]

@pulumi.output_type
class GetInstancesResult:
    def __init__(
        __self__,
        filters=...,
        id=...,
        ids=...,
        instance_state_names=...,
        instance_tags=...,
        ipv6_addresses=...,
        private_ips=...,
        public_ips=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetInstancesFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceStateNames")
    def instance_state_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceTags")
    def instance_tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipv6Addresses")
    def ipv6_addresses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateIps")
    def private_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicIps")
    def public_ips(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetInstancesResult(GetInstancesResult):
    def __await__(self): ...

def get_instances(
    filters: Optional[
        Sequence[Union[GetInstancesFilterArgs, GetInstancesFilterArgsDict]]
    ] = ...,
    instance_state_names: Optional[Sequence[_builtins.str]] = ...,
    instance_tags: Optional[Mapping[str, _builtins.str]] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInstancesResult: ...
def get_instances_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[Union[GetInstancesFilterArgs, GetInstancesFilterArgsDict]]
            ]
        ]
    ] = ...,
    instance_state_names: Optional[
        pulumi.Input[Optional[Sequence[_builtins.str]]]
    ] = ...,
    instance_tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInstancesResult]: ...
