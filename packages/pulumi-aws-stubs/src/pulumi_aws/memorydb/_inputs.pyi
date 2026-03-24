import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterClusterEndpointArgs",
    "ClusterClusterEndpointArgsDict",
    "ClusterShardArgs",
    "ClusterShardArgsDict",
    "ClusterShardNodeArgs",
    "ClusterShardNodeArgsDict",
    "ClusterShardNodeEndpointArgs",
    "ClusterShardNodeEndpointArgsDict",
    "MultiRegionClusterTimeoutsArgs",
    "MultiRegionClusterTimeoutsArgsDict",
    "ParameterGroupParameterArgs",
    "ParameterGroupParameterArgsDict",
    "SnapshotClusterConfigurationArgs",
    "SnapshotClusterConfigurationArgsDict",
    "UserAuthenticationModeArgs",
    "UserAuthenticationModeArgsDict",
]

class ClusterClusterEndpointArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterClusterEndpointArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterShardArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    nodes: NotRequired[pulumi.Input[Sequence[pulumi.Input[ClusterShardNodeArgsDict]]]]
    num_nodes: NotRequired[pulumi.Input[_builtins.int]]
    slots: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterShardArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        nodes: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterShardNodeArgs]]]
        ] = ...,
        num_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        slots: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nodes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterShardNodeArgs]]]]: ...
    @nodes.setter
    def nodes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterShardNodeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_nodes.setter
    def num_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @slots.setter
    def slots(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterShardNodeArgsDict(TypedDict):
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterShardNodeEndpointArgsDict]]]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterShardNodeArgs:
    def __init__(
        __self__,
        *,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterShardNodeEndpointArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterShardNodeEndpointArgs]]]
    ]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterShardNodeEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterShardNodeEndpointArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class ClusterShardNodeEndpointArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class MultiRegionClusterTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class MultiRegionClusterTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ParameterGroupParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ParameterGroupParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class SnapshotClusterConfigurationArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    engine: NotRequired[pulumi.Input[_builtins.str]]
    engine_version: NotRequired[pulumi.Input[_builtins.str]]
    maintenance_window: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    node_type: NotRequired[pulumi.Input[_builtins.str]]
    num_shards: NotRequired[pulumi.Input[_builtins.int]]
    parameter_group_name: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    snapshot_retention_limit: NotRequired[pulumi.Input[_builtins.int]]
    snapshot_window: NotRequired[pulumi.Input[_builtins.str]]
    subnet_group_name: NotRequired[pulumi.Input[_builtins.str]]
    topic_arn: NotRequired[pulumi.Input[_builtins.str]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SnapshotClusterConfigurationArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        num_shards: Optional[pulumi.Input[_builtins.int]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_window: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numShards")
    def num_shards(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_shards.setter
    def num_shards(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameter_group_name.setter
    def parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @snapshot_retention_limit.setter
    def snapshot_retention_limit(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_window.setter
    def snapshot_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_group_name.setter
    def subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserAuthenticationModeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    password_count: NotRequired[pulumi.Input[_builtins.int]]
    passwords: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class UserAuthenticationModeArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        password_count: Optional[pulumi.Input[_builtins.int]] = ...,
        passwords: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="passwordCount")
    def password_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @password_count.setter
    def password_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def passwords(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @passwords.setter
    def passwords(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
