import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetComputeAllowedResizeSizesResult",
    "AwaitableGetComputeAllowedResizeSizesResult",
    "get_compute_allowed_resize_sizes",
    "get_compute_allowed_resize_sizes_output",
]

@pulumi.output_type
class GetComputeAllowedResizeSizesResult:
    def __init__(__self__, value=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.VirtualMachineSizeResponse]]: ...

class AwaitableGetComputeAllowedResizeSizesResult(GetComputeAllowedResizeSizesResult):
    def __await__(self): ...

def get_compute_allowed_resize_sizes(
    compute_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetComputeAllowedResizeSizesResult: ...
def get_compute_allowed_resize_sizes_output(
    compute_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetComputeAllowedResizeSizesResult]: ...
