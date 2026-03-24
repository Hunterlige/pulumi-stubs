import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNpmPackageResult",
    "AwaitableGetNpmPackageResult",
    "get_npm_package",
    "get_npm_package_output",
]

@pulumi.output_type
class GetNpmPackageResult:
    def __init__(
        __self__,
        create_time=...,
        id=...,
        location=...,
        name=...,
        package_name=...,
        project=...,
        repository_id=...,
        tags=...,
        update_time=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetNpmPackageResult(GetNpmPackageResult):
    def __await__(self): ...

def get_npm_package(
    location: Optional[_builtins.str] = ...,
    package_name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    repository_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNpmPackageResult: ...
def get_npm_package_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    package_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNpmPackageResult]: ...
