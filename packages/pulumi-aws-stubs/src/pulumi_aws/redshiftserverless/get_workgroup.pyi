import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkgroupResult",
    "AwaitableGetWorkgroupResult",
    "get_workgroup",
    "get_workgroup_output",
]

@pulumi.output_type
class GetWorkgroupResult:
    def __init__(
        __self__,
        arn=...,
        endpoints=...,
        enhanced_vpc_routing=...,
        id=...,
        namespace_name=...,
        publicly_accessible=...,
        region=...,
        security_group_ids=...,
        subnet_ids=...,
        track_name=...,
        workgroup_id=...,
        workgroup_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Sequence[outputs.GetWorkgroupEndpointResult]: ...
    @_builtins.property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackName")
    def track_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workgroupId")
    def workgroup_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> _builtins.str: ...

class AwaitableGetWorkgroupResult(GetWorkgroupResult):
    def __await__(self): ...

def get_workgroup(
    region: Optional[_builtins.str] = ...,
    workgroup_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkgroupResult: ...
def get_workgroup_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkgroupResult]: ...
