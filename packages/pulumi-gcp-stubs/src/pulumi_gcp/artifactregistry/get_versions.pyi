import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetVersionsResult",
    "AwaitableGetVersionsResult",
    "get_versions",
    "get_versions_output",
]

@pulumi.output_type
class GetVersionsResult:
    def __init__(
        __self__,
        filter=...,
        id=...,
        location=...,
        package_name=...,
        project=...,
        repository_id=...,
        versions=...,
        view=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
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
    def versions(self) -> Sequence[outputs.GetVersionsVersionResult]: ...
    @_builtins.property
    @pulumi.getter
    def view(self) -> Optional[_builtins.str]: ...

class AwaitableGetVersionsResult(GetVersionsResult):
    def __await__(self): ...

def get_versions(
    filter: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    package_name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    repository_id: Optional[_builtins.str] = ...,
    view: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetVersionsResult: ...
def get_versions_output(
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    package_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repository_id: Optional[pulumi.Input[_builtins.str]] = ...,
    view: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetVersionsResult]: ...
