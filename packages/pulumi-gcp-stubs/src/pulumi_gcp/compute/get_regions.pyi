import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionsResult",
    "AwaitableGetRegionsResult",
    "get_regions",
    "get_regions_output",
]

@pulumi.output_type
class GetRegionsResult:
    def __init__(__self__, id=..., names=..., project=..., status=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

class AwaitableGetRegionsResult(GetRegionsResult):
    def __await__(self): ...

def get_regions(
    project: Optional[_builtins.str] = ...,
    status: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionsResult: ...
def get_regions_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    status: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionsResult]: ...
