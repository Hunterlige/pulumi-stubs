import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGiVersionsResult",
    "AwaitableGetGiVersionsResult",
    "get_gi_versions",
    "get_gi_versions_output",
]

@pulumi.output_type
class GetGiVersionsResult:
    def __init__(__self__, gi_versions=..., id=..., region=..., shape=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="giVersions")
    def gi_versions(self) -> Sequence[outputs.GetGiVersionsGiVersionResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]: ...

class AwaitableGetGiVersionsResult(GetGiVersionsResult):
    def __await__(self): ...

def get_gi_versions(
    region: Optional[_builtins.str] = ...,
    shape: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGiVersionsResult: ...
def get_gi_versions_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    shape: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGiVersionsResult]: ...
