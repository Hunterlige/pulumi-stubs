import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterCredentialsResult",
    "AwaitableGetClusterCredentialsResult",
    "get_cluster_credentials",
    "get_cluster_credentials_output",
]

@pulumi.output_type
class GetClusterCredentialsResult:
    def __init__(
        __self__,
        auto_create=...,
        cluster_identifier=...,
        db_groups=...,
        db_name=...,
        db_password=...,
        db_user=...,
        duration_seconds=...,
        expiration=...,
        id=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoCreate")
    def auto_create(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbGroups")
    def db_groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dbName")
    def db_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbPassword")
    def db_password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="durationSeconds")
    def duration_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def expiration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetClusterCredentialsResult(GetClusterCredentialsResult):
    def __await__(self): ...

def get_cluster_credentials(
    auto_create: Optional[_builtins.bool] = ...,
    cluster_identifier: Optional[_builtins.str] = ...,
    db_groups: Optional[Sequence[_builtins.str]] = ...,
    db_name: Optional[_builtins.str] = ...,
    db_user: Optional[_builtins.str] = ...,
    duration_seconds: Optional[_builtins.int] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterCredentialsResult: ...
def get_cluster_credentials_output(
    auto_create: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    db_groups: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    db_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    db_user: Optional[pulumi.Input[_builtins.str]] = ...,
    duration_seconds: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterCredentialsResult]: ...
