import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClusterSnapshotResult",
    "AwaitableGetClusterSnapshotResult",
    "get_cluster_snapshot",
    "get_cluster_snapshot_output",
]

@pulumi.output_type
class GetClusterSnapshotResult:
    def __init__(
        __self__,
        allocated_storage=...,
        availability_zones=...,
        db_cluster_identifier=...,
        db_cluster_snapshot_arn=...,
        db_cluster_snapshot_identifier=...,
        engine=...,
        engine_version=...,
        id=...,
        include_public=...,
        include_shared=...,
        kms_key_id=...,
        license_model=...,
        most_recent=...,
        port=...,
        region=...,
        snapshot_create_time=...,
        snapshot_type=...,
        source_db_cluster_snapshot_arn=...,
        status=...,
        storage_encrypted=...,
        tags=...,
        vpc_id=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterIdentifier")
    def db_cluster_identifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterSnapshotArn")
    def db_cluster_snapshot_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterSnapshotIdentifier")
    def db_cluster_snapshot_identifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includePublic")
    def include_public(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="includeShared")
    def include_shared(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="snapshotCreateTime")
    def snapshot_create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDbClusterSnapshotArn")
    def source_db_cluster_snapshot_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

class AwaitableGetClusterSnapshotResult(GetClusterSnapshotResult):
    def __await__(self): ...

def get_cluster_snapshot(
    db_cluster_identifier: Optional[_builtins.str] = ...,
    db_cluster_snapshot_identifier: Optional[_builtins.str] = ...,
    include_public: Optional[_builtins.bool] = ...,
    include_shared: Optional[_builtins.bool] = ...,
    most_recent: Optional[_builtins.bool] = ...,
    region: Optional[_builtins.str] = ...,
    snapshot_type: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClusterSnapshotResult: ...
def get_cluster_snapshot_output(
    db_cluster_identifier: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    db_cluster_snapshot_identifier: Optional[
        pulumi.Input[Optional[_builtins.str]]
    ] = ...,
    include_public: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    include_shared: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    snapshot_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClusterSnapshotResult]: ...
