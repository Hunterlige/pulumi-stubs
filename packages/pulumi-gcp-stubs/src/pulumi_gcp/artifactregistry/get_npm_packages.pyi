import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNpmPackagesResult",
    "AwaitableGetNpmPackagesResult",
    "get_npm_packages",
    "get_npm_packages_output",
]

@pulumi.output_type
class GetNpmPackagesResult:
    def __init__(
        __self__, id=..., location=..., npm_packages=..., project=..., repository_id=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="npmPackages")
    def npm_packages(self) -> Sequence[outputs.GetNpmPackagesNpmPackageResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str: ...

class AwaitableGetNpmPackagesResult(GetNpmPackagesResult):
    def __await__(self): ...

def get_npm_packages(
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    repository_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNpmPackagesResult: ...
def get_npm_packages_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNpmPackagesResult]: ...
