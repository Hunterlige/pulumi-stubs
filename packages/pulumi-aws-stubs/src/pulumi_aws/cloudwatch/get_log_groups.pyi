import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLogGroupsResult",
    "AwaitableGetLogGroupsResult",
    "get_log_groups",
    "get_log_groups_output",
]

@pulumi.output_type
class GetLogGroupsResult:
    def __init__(
        __self__,
        arns=...,
        id=...,
        log_group_name_prefix=...,
        log_group_names=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logGroupNamePrefix")
    def log_group_name_prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logGroupNames")
    def log_group_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetLogGroupsResult(GetLogGroupsResult):
    def __await__(self): ...

def get_log_groups(
    log_group_name_prefix: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLogGroupsResult: ...
def get_log_groups_output(
    log_group_name_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLogGroupsResult]: ...
