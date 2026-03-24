import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRepositoriesResult",
    "AwaitableGetRepositoriesResult",
    "get_repositories",
    "get_repositories_output",
]

@pulumi.output_type
class GetRepositoriesResult:
    def __init__(
        __self__, id=..., location=..., name_filter=..., project=..., repositories=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nameFilter")
    def name_filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repositories(self) -> Sequence[outputs.GetRepositoriesRepositoryResult]: ...

class AwaitableGetRepositoriesResult(GetRepositoriesResult):
    def __await__(self): ...

def get_repositories(
    location: Optional[_builtins.str] = ...,
    name_filter: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRepositoriesResult: ...
def get_repositories_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    name_filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRepositoriesResult]: ...
