import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFileShareLimitsResult",
    "AwaitableGetFileShareLimitsResult",
    "get_file_share_limits",
    "get_file_share_limits_output",
]

@pulumi.output_type
class GetFileShareLimitsResult:
    def __init__(__self__, properties=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.FileShareLimitsOutputResponse: ...

class AwaitableGetFileShareLimitsResult(GetFileShareLimitsResult):
    def __await__(self): ...

def get_file_share_limits(
    location: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetFileShareLimitsResult: ...
def get_file_share_limits_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFileShareLimitsResult]: ...
