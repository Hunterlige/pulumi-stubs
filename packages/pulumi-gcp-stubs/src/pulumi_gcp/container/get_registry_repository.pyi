import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegistryRepositoryResult",
    "AwaitableGetRegistryRepositoryResult",
    "get_registry_repository",
    "get_registry_repository_output",
]

@pulumi.output_type
class GetRegistryRepositoryResult:
    def __init__(
        __self__, id=..., project=..., region=..., repository_url=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> _builtins.str: ...

class AwaitableGetRegistryRepositoryResult(GetRegistryRepositoryResult):
    def __await__(self): ...

def get_registry_repository(
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegistryRepositoryResult: ...
def get_registry_repository_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegistryRepositoryResult]: ...
