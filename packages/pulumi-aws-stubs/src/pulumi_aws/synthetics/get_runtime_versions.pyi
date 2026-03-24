import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRuntimeVersionsResult",
    "AwaitableGetRuntimeVersionsResult",
    "get_runtime_versions",
    "get_runtime_versions_output",
]

@pulumi.output_type
class GetRuntimeVersionsResult:
    def __init__(__self__, id=..., region=..., runtime_versions=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersions")
    def runtime_versions(
        self,
    ) -> Sequence[outputs.GetRuntimeVersionsRuntimeVersionResult]: ...

class AwaitableGetRuntimeVersionsResult(GetRuntimeVersionsResult):
    def __await__(self): ...

def get_runtime_versions(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetRuntimeVersionsResult: ...
def get_runtime_versions_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRuntimeVersionsResult]: ...
