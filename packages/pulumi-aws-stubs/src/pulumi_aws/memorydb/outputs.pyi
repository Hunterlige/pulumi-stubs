import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterClusterEndpoint",
    "ClusterShard",
    "ClusterShardNode",
    "ClusterShardNodeEndpoint",
    "MultiRegionClusterTimeouts",
    "ParameterGroupParameter",
    "SnapshotClusterConfiguration",
    "UserAuthenticationMode",
    "GetClusterClusterEndpointResult",
    "GetClusterShardResult",
    "GetClusterShardNodeResult",
    "GetClusterShardNodeEndpointResult",
    "GetParameterGroupParameterResult",
    "GetSnapshotClusterConfigurationResult",
    "GetUserAuthenticationModeResult",
]

@pulumi.output_type
class ClusterClusterEndpoint(dict):
    def __init__(
        __self__,
        *,
        address: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterShard(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        nodes: Optional[Sequence[outputs.ClusterShardNode]] = ...,
        num_nodes: Optional[_builtins.int] = ...,
        slots: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Optional[Sequence[outputs.ClusterShardNode]]: ...
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterShardNode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zone: Optional[_builtins.str] = ...,
        create_time: Optional[_builtins.str] = ...,
        endpoints: Optional[Sequence[outputs.ClusterShardNodeEndpoint]] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[outputs.ClusterShardNodeEndpoint]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterShardNodeEndpoint(dict):
    def __init__(
        __self__,
        *,
        address: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class MultiRegionClusterTimeouts(dict):
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
class ParameterGroupParameter(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class SnapshotClusterConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        engine: Optional[_builtins.str] = ...,
        engine_version: Optional[_builtins.str] = ...,
        maintenance_window: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        node_type: Optional[_builtins.str] = ...,
        num_shards: Optional[_builtins.int] = ...,
        parameter_group_name: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        snapshot_retention_limit: Optional[_builtins.int] = ...,
        snapshot_window: Optional[_builtins.str] = ...,
        subnet_group_name: Optional[_builtins.str] = ...,
        topic_arn: Optional[_builtins.str] = ...,
        vpc_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserAuthenticationMode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        password_count: Optional[_builtins.int] = ...,
        passwords: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordCount")
    def password_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def passwords(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetClusterClusterEndpointResult(dict):
    def __init__(__self__, *, address: _builtins.str, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterShardResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        nodes: Sequence[outputs.GetClusterShardNodeResult],
        num_nodes: _builtins.int,
        slots: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Sequence[outputs.GetClusterShardNodeResult]: ...
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def slots(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterShardNodeResult(dict):
    def __init__(
        __self__,
        *,
        availability_zone: _builtins.str,
        create_time: _builtins.str,
        endpoints: Sequence[outputs.GetClusterShardNodeEndpointResult],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Sequence[outputs.GetClusterShardNodeEndpointResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetClusterShardNodeEndpointResult(dict):
    def __init__(__self__, *, address: _builtins.str, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetParameterGroupParameterResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetSnapshotClusterConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        engine: _builtins.str,
        engine_version: _builtins.str,
        maintenance_window: _builtins.str,
        name: _builtins.str,
        node_type: _builtins.str,
        num_shards: _builtins.int,
        parameter_group_name: _builtins.str,
        port: _builtins.int,
        snapshot_retention_limit: _builtins.int,
        snapshot_window: _builtins.str,
        subnet_group_name: _builtins.str,
        topic_arn: _builtins.str,
        vpc_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetUserAuthenticationModeResult(dict):
    def __init__(
        __self__, *, password_count: _builtins.int, type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordCount")
    def password_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
