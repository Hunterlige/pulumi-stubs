import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAccessEntryResult",
    "AwaitableGetAccessEntryResult",
    "get_access_entry",
    "get_access_entry_output",
]

@pulumi.output_type
class GetAccessEntryResult:
    def __init__(
        __self__,
        access_entry_arn=...,
        cluster_name=...,
        created_at=...,
        id=...,
        kubernetes_groups=...,
        modified_at=...,
        principal_arn=...,
        region=...,
        tags=...,
        tags_all=...,
        type=...,
        user_name=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessEntryArn")
    def access_entry_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesGroups")
    def kubernetes_groups(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str: ...

class AwaitableGetAccessEntryResult(GetAccessEntryResult):
    def __await__(self): ...

def get_access_entry(
    cluster_name: Optional[_builtins.str] = ...,
    principal_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    tags_all: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAccessEntryResult: ...
def get_access_entry_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    principal_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    tags_all: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAccessEntryResult]: ...
