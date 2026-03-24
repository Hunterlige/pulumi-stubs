import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetImageVersionsResult",
    "AwaitableGetImageVersionsResult",
    "get_image_versions",
    "get_image_versions_output",
]

@pulumi.output_type
class GetImageVersionsResult:
    def __init__(
        __self__, id=..., image_versions=..., project=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageVersions")
    def image_versions(
        self,
    ) -> Sequence[outputs.GetImageVersionsImageVersionResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetImageVersionsResult(GetImageVersionsResult):
    def __await__(self): ...

def get_image_versions(
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetImageVersionsResult: ...
def get_image_versions_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetImageVersionsResult]: ...
