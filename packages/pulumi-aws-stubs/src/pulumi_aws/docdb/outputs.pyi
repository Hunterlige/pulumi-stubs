import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterMasterUserSecret",
    "ClusterParameterGroupParameter",
    "ClusterRestoreToPointInTime",
    "ClusterServerlessV2ScalingConfiguration",
    "ElasticClusterTimeouts",
    "GlobalClusterGlobalClusterMember",
]

@pulumi.output_type
class ClusterMasterUserSecret(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kms_key_id: Optional[_builtins.str] = ...,
        secret_arn: Optional[_builtins.str] = ...,
        secret_status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretStatus")
    def secret_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterParameterGroupParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        value: _builtins.str,
        apply_method: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="applyMethod")
    def apply_method(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterRestoreToPointInTime(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_cluster_identifier: _builtins.str,
        restore_to_time: Optional[_builtins.str] = ...,
        restore_type: Optional[_builtins.str] = ...,
        use_latest_restorable_time: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceClusterIdentifier")
    def source_cluster_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="restoreToTime")
    def restore_to_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="restoreType")
    def restore_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useLatestRestorableTime")
    def use_latest_restorable_time(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterServerlessV2ScalingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_capacity: _builtins.float, min_capacity: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="minCapacity")
    def min_capacity(self) -> _builtins.float: ...

@pulumi.output_type
class ElasticClusterTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GlobalClusterGlobalClusterMember(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        db_cluster_arn: Optional[_builtins.str] = ...,
        is_writer: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dbClusterArn")
    def db_cluster_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isWriter")
    def is_writer(self) -> Optional[_builtins.bool]: ...
