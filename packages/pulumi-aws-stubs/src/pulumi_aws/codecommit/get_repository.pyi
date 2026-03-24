import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRepositoryResult",
    "AwaitableGetRepositoryResult",
    "get_repository",
    "get_repository_output",
]

@pulumi.output_type
class GetRepositoryResult:
    def __init__(
        __self__,
        arn=...,
        clone_url_http=...,
        clone_url_ssh=...,
        id=...,
        kms_key_id=...,
        region=...,
        repository_id=...,
        repository_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloneUrlHttp")
    def clone_url_http(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="cloneUrlSsh")
    def clone_url_ssh(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryId")
    def repository_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> _builtins.str: ...

class AwaitableGetRepositoryResult(GetRepositoryResult):
    def __await__(self): ...

def get_repository(
    region: Optional[_builtins.str] = ...,
    repository_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRepositoryResult: ...
def get_repository_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    repository_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRepositoryResult]: ...
