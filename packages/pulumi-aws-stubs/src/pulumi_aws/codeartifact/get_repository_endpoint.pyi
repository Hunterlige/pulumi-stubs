import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRepositoryEndpointResult",
    "AwaitableGetRepositoryEndpointResult",
    "get_repository_endpoint",
    "get_repository_endpoint_output",
]

@pulumi.output_type
class GetRepositoryEndpointResult:
    def __init__(
        __self__,
        domain=...,
        domain_owner=...,
        format=...,
        id=...,
        region=...,
        repository=...,
        repository_endpoint=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainOwner")
    def domain_owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryEndpoint")
    def repository_endpoint(self) -> _builtins.str: ...

class AwaitableGetRepositoryEndpointResult(GetRepositoryEndpointResult):
    def __await__(self): ...

def get_repository_endpoint(
    domain: Optional[_builtins.str] = ...,
    domain_owner: Optional[_builtins.str] = ...,
    format: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    repository: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRepositoryEndpointResult: ...
def get_repository_endpoint_output(
    domain: Optional[pulumi.Input[_builtins.str]] = ...,
    domain_owner: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    format: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repository: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRepositoryEndpointResult]: ...
