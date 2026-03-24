import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLocalDiskResult",
    "AwaitableGetLocalDiskResult",
    "get_local_disk",
    "get_local_disk_output",
]

@pulumi.output_type
class GetLocalDiskResult:
    def __init__(
        __self__,
        disk_id=...,
        disk_node=...,
        disk_path=...,
        gateway_arn=...,
        id=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskNode")
    def disk_node(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetLocalDiskResult(GetLocalDiskResult):
    def __await__(self): ...

def get_local_disk(
    disk_node: Optional[_builtins.str] = ...,
    disk_path: Optional[_builtins.str] = ...,
    gateway_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLocalDiskResult: ...
def get_local_disk_output(
    disk_node: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    disk_path: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    gateway_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLocalDiskResult]: ...
