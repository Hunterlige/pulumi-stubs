import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionInstanceGroupResult",
    "AwaitableGetRegionInstanceGroupResult",
    "get_region_instance_group",
    "get_region_instance_group_output",
]

@pulumi.output_type
class GetRegionInstanceGroupResult:
    def __init__(
        __self__,
        id=...,
        instances=...,
        name=...,
        project=...,
        region=...,
        self_link=...,
        size=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def instances(self) -> Sequence[outputs.GetRegionInstanceGroupInstanceResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...

class AwaitableGetRegionInstanceGroupResult(GetRegionInstanceGroupResult):
    def __await__(self): ...

def get_region_instance_group(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    self_link: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionInstanceGroupResult: ...
def get_region_instance_group_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    self_link: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionInstanceGroupResult]: ...
