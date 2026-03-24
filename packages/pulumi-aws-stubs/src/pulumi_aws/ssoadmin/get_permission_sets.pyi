import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPermissionSetsResult",
    "AwaitableGetPermissionSetsResult",
    "get_permission_sets",
    "get_permission_sets_output",
]

@pulumi.output_type
class GetPermissionSetsResult:
    def __init__(__self__, arns=..., id=..., instance_arn=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetPermissionSetsResult(GetPermissionSetsResult):
    def __await__(self): ...

def get_permission_sets(
    instance_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPermissionSetsResult: ...
def get_permission_sets_output(
    instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPermissionSetsResult]: ...
