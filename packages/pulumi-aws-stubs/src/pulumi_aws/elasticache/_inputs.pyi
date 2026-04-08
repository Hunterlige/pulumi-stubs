import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterCacheNodeArgs",
    "ClusterCacheNodeArgsDict",
    "ClusterLogDeliveryConfigurationArgs",
    "ClusterLogDeliveryConfigurationArgsDict",
    "GlobalReplicationGroupGlobalNodeGroupArgs",
    "GlobalReplicationGroupGlobalNodeGroupArgsDict",
    "ParameterGroupParameterArgs",
    "ParameterGroupParameterArgsDict",
    "ReplicationGroupLogDeliveryConfigurationArgs",
    "ReplicationGroupLogDeliveryConfigurationArgsDict",
    "ReplicationGroupNodeGroupConfigurationArgs",
    "ReplicationGroupNodeGroupConfigurationArgsDict",
    "ReservedCacheNodeRecurringChargeArgs",
    "ReservedCacheNodeRecurringChargeArgsDict",
    "ReservedCacheNodeTimeoutsArgs",
    "ReservedCacheNodeTimeoutsArgsDict",
    "ServerlessCacheCacheUsageLimitsArgs",
    "ServerlessCacheCacheUsageLimitsArgsDict",
    "ServerlessCacheCacheUsageLimitsDataStorageArgs",
    "ServerlessCacheCacheUsageLimitsDataStorageArgsDict",
    "ServerlessCacheCacheUsageLimitsEcpuPerSecondArgs",
    ...,
    "ServerlessCacheEndpointArgs",
    "ServerlessCacheEndpointArgsDict",
    "ServerlessCacheReaderEndpointArgs",
    "ServerlessCacheReaderEndpointArgsDict",
    "ServerlessCacheTimeoutsArgs",
    "ServerlessCacheTimeoutsArgsDict",
    "UserAuthenticationModeArgs",
    "UserAuthenticationModeArgsDict",
    "GetUserAuthenticationModeArgs",
    "GetUserAuthenticationModeArgsDict",
]

class ClusterCacheNodeArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    outpost_arn: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ClusterCacheNodeArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        outpost_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ClusterLogDeliveryConfigurationArgsDict(TypedDict):
    destination: pulumi.Input[_builtins.str]
    destination_type: pulumi.Input[_builtins.str]
    log_format: pulumi.Input[_builtins.str]
    log_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterLogDeliveryConfigurationArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[_builtins.str],
        destination_type: pulumi.Input[_builtins.str],
        log_format: pulumi.Input[_builtins.str],
        log_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> pulumi.Input[_builtins.str]: ...
    @destination_type.setter
    def destination_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> pulumi.Input[_builtins.str]: ...
    @log_format.setter
    def log_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> pulumi.Input[_builtins.str]: ...
    @log_type.setter
    def log_type(self, value: pulumi.Input[_builtins.str]): ...

class GlobalReplicationGroupGlobalNodeGroupArgsDict(TypedDict):
    global_node_group_id: NotRequired[pulumi.Input[_builtins.str]]
    slots: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GlobalReplicationGroupGlobalNodeGroupArgs:
    def __init__(
        __self__,
        *,
        global_node_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        slots: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="globalNodeGroupId")
    def global_node_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_node_group_id.setter
    def global_node_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @slots.setter
    def slots(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ParameterGroupParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

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

class ReplicationGroupLogDeliveryConfigurationArgsDict(TypedDict):
    destination: pulumi.Input[_builtins.str]
    destination_type: pulumi.Input[_builtins.str]
    log_format: pulumi.Input[_builtins.str]
    log_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ReplicationGroupLogDeliveryConfigurationArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[_builtins.str],
        destination_type: pulumi.Input[_builtins.str],
        log_format: pulumi.Input[_builtins.str],
        log_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> pulumi.Input[_builtins.str]: ...
    @destination_type.setter
    def destination_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> pulumi.Input[_builtins.str]: ...
    @log_format.setter
    def log_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> pulumi.Input[_builtins.str]: ...
    @log_type.setter
    def log_type(self, value: pulumi.Input[_builtins.str]): ...

class ReplicationGroupNodeGroupConfigurationArgsDict(TypedDict):
    node_group_id: NotRequired[pulumi.Input[_builtins.str]]
    primary_availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    primary_outpost_arn: NotRequired[pulumi.Input[_builtins.str]]
    replica_availability_zones: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    replica_count: NotRequired[pulumi.Input[_builtins.int]]
    replica_outpost_arns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    slots: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReplicationGroupNodeGroupConfigurationArgs:
    def __init__(
        __self__,
        *,
        node_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_outpost_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        replica_outpost_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        slots: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupId")
    def node_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_group_id.setter
    def node_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryAvailabilityZone")
    def primary_availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_availability_zone.setter
    def primary_availability_zone(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryOutpostArn")
    def primary_outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_outpost_arn.setter
    def primary_outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaAvailabilityZones")
    def replica_availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @replica_availability_zones.setter
    def replica_availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaOutpostArns")
    def replica_outpost_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @replica_outpost_arns.setter
    def replica_outpost_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @slots.setter
    def slots(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReservedCacheNodeRecurringChargeArgsDict(TypedDict):
    recurring_charge_amount: pulumi.Input[_builtins.float]
    recurring_charge_frequency: pulumi.Input[_builtins.str]

@pulumi.input_type
class ReservedCacheNodeRecurringChargeArgs:
    def __init__(
        __self__,
        *,
        recurring_charge_amount: pulumi.Input[_builtins.float],
        recurring_charge_frequency: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recurringChargeAmount")
    def recurring_charge_amount(self) -> pulumi.Input[_builtins.float]: ...
    @recurring_charge_amount.setter
    def recurring_charge_amount(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="recurringChargeFrequency")
    def recurring_charge_frequency(self) -> pulumi.Input[_builtins.str]: ...
    @recurring_charge_frequency.setter
    def recurring_charge_frequency(self, value: pulumi.Input[_builtins.str]): ...

class ReservedCacheNodeTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReservedCacheNodeTimeoutsArgs:
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

class ServerlessCacheCacheUsageLimitsArgsDict(TypedDict):
    data_storage: NotRequired[
        pulumi.Input[ServerlessCacheCacheUsageLimitsDataStorageArgsDict]
    ]
    ecpu_per_seconds: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServerlessCacheCacheUsageLimitsEcpuPerSecondArgsDict]]
        ]
    ]

@pulumi.input_type
class ServerlessCacheCacheUsageLimitsArgs:
    def __init__(
        __self__,
        *,
        data_storage: Optional[
            pulumi.Input[ServerlessCacheCacheUsageLimitsDataStorageArgs]
        ] = ...,
        ecpu_per_seconds: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServerlessCacheCacheUsageLimitsEcpuPerSecondArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStorage")
    def data_storage(
        self,
    ) -> Optional[pulumi.Input[ServerlessCacheCacheUsageLimitsDataStorageArgs]]: ...
    @data_storage.setter
    def data_storage(
        self,
        value: Optional[pulumi.Input[ServerlessCacheCacheUsageLimitsDataStorageArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecpuPerSeconds")
    def ecpu_per_seconds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServerlessCacheCacheUsageLimitsEcpuPerSecondArgs]]
        ]
    ]: ...
    @ecpu_per_seconds.setter
    def ecpu_per_seconds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServerlessCacheCacheUsageLimitsEcpuPerSecondArgs]]
            ]
        ],
    ): ...

class ServerlessCacheCacheUsageLimitsDataStorageArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    maximum: NotRequired[pulumi.Input[_builtins.int]]
    minimum: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServerlessCacheCacheUsageLimitsDataStorageArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        maximum: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum.setter
    def maximum(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum.setter
    def minimum(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServerlessCacheCacheUsageLimitsEcpuPerSecondArgsDict(TypedDict):
    maximum: NotRequired[pulumi.Input[_builtins.int]]
    minimum: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServerlessCacheCacheUsageLimitsEcpuPerSecondArgs:
    def __init__(
        __self__,
        *,
        maximum: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum.setter
    def maximum(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minimum.setter
    def minimum(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServerlessCacheEndpointArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]

@pulumi.input_type
class ServerlessCacheEndpointArgs:
    def __init__(
        __self__,
        *,
        address: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]: ...
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class ServerlessCacheReaderEndpointArgsDict(TypedDict):
    address: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]

@pulumi.input_type
class ServerlessCacheReaderEndpointArgs:
    def __init__(
        __self__,
        *,
        address: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> pulumi.Input[_builtins.str]: ...
    @address.setter
    def address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class ServerlessCacheTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServerlessCacheTimeoutsArgs:
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

class UserAuthenticationModeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    password_count: NotRequired[pulumi.Input[_builtins.int]]
    passwords: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

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

class GetUserAuthenticationModeArgsDict(TypedDict):
    password_count: NotRequired[_builtins.int]
    type: NotRequired[_builtins.str]

@pulumi.input_type
class GetUserAuthenticationModeArgs:
    def __init__(
        __self__,
        *,
        password_count: Optional[_builtins.int] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordCount")
    def password_count(self) -> Optional[_builtins.int]: ...
    @password_count.setter
    def password_count(self, value: Optional[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @type.setter
    def type(self, value: Optional[_builtins.str]): ...
