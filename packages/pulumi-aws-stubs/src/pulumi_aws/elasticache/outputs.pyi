import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterCacheNode",
    "ClusterLogDeliveryConfiguration",
    "GlobalReplicationGroupGlobalNodeGroup",
    "ParameterGroupParameter",
    "ReplicationGroupLogDeliveryConfiguration",
    "ReplicationGroupNodeGroupConfiguration",
    "ReservedCacheNodeRecurringCharge",
    "ReservedCacheNodeTimeouts",
    "ServerlessCacheCacheUsageLimits",
    "ServerlessCacheCacheUsageLimitsDataStorage",
    "ServerlessCacheCacheUsageLimitsEcpuPerSecond",
    "ServerlessCacheEndpoint",
    "ServerlessCacheReaderEndpoint",
    "ServerlessCacheTimeouts",
    "UserAuthenticationMode",
    "GetClusterCacheNodeResult",
    "GetClusterLogDeliveryConfigurationResult",
    "GetReplicationGroupLogDeliveryConfigurationResult",
    "GetReplicationGroupNodeGroupConfigurationResult",
    "GetServerlessCacheCacheUsageLimitsResult",
    ...,
    ...,
    "GetServerlessCacheEndpointResult",
    "GetServerlessCacheReaderEndpointResult",
    "GetUserAuthenticationModeResult",
]

@pulumi.output_type
class ClusterCacheNode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address: Optional[_builtins.str] = ...,
        availability_zone: Optional[_builtins.str] = ...,
        id: Optional[_builtins.str] = ...,
        outpost_arn: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ClusterLogDeliveryConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: _builtins.str,
        destination_type: _builtins.str,
        log_format: _builtins.str,
        log_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str: ...

@pulumi.output_type
class GlobalReplicationGroupGlobalNodeGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        global_node_group_id: Optional[_builtins.str] = ...,
        slots: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="globalNodeGroupId")
    def global_node_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[_builtins.str]: ...

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
class ReplicationGroupLogDeliveryConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination: _builtins.str,
        destination_type: _builtins.str,
        log_format: _builtins.str,
        log_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str: ...

@pulumi.output_type
class ReplicationGroupNodeGroupConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        node_group_id: Optional[_builtins.str] = ...,
        primary_availability_zone: Optional[_builtins.str] = ...,
        primary_outpost_arn: Optional[_builtins.str] = ...,
        replica_availability_zones: Optional[Sequence[_builtins.str]] = ...,
        replica_count: Optional[_builtins.int] = ...,
        replica_outpost_arns: Optional[Sequence[_builtins.str]] = ...,
        slots: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupId")
    def node_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryAvailabilityZone")
    def primary_availability_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryOutpostArn")
    def primary_outpost_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaAvailabilityZones")
    def replica_availability_zones(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="replicaOutpostArns")
    def replica_outpost_arns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ReservedCacheNodeRecurringCharge(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        recurring_charge_amount: _builtins.float,
        recurring_charge_frequency: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recurringChargeAmount")
    def recurring_charge_amount(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="recurringChargeFrequency")
    def recurring_charge_frequency(self) -> _builtins.str: ...

@pulumi.output_type
class ReservedCacheNodeTimeouts(dict):
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
class ServerlessCacheCacheUsageLimits(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_storage: Optional[
            outputs.ServerlessCacheCacheUsageLimitsDataStorage
        ] = ...,
        ecpu_per_seconds: Optional[
            Sequence[outputs.ServerlessCacheCacheUsageLimitsEcpuPerSecond]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStorage")
    def data_storage(
        self,
    ) -> Optional[outputs.ServerlessCacheCacheUsageLimitsDataStorage]: ...
    @_builtins.property
    @pulumi.getter(name="ecpuPerSeconds")
    def ecpu_per_seconds(
        self,
    ) -> Optional[Sequence[outputs.ServerlessCacheCacheUsageLimitsEcpuPerSecond]]: ...

@pulumi.output_type
class ServerlessCacheCacheUsageLimitsDataStorage(dict):
    def __init__(
        __self__,
        *,
        unit: _builtins.str,
        maximum: Optional[_builtins.int] = ...,
        minimum: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServerlessCacheCacheUsageLimitsEcpuPerSecond(dict):
    def __init__(
        __self__,
        *,
        maximum: Optional[_builtins.int] = ...,
        minimum: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServerlessCacheEndpoint(dict):
    def __init__(__self__, *, address: _builtins.str, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class ServerlessCacheReaderEndpoint(dict):
    def __init__(__self__, *, address: _builtins.str, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class ServerlessCacheTimeouts(dict):
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
class GetClusterCacheNodeResult(dict):
    def __init__(
        __self__,
        *,
        address: _builtins.str,
        availability_zone: _builtins.str,
        id: _builtins.str,
        outpost_arn: _builtins.str,
        port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetClusterLogDeliveryConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        destination: _builtins.str,
        destination_type: _builtins.str,
        log_format: _builtins.str,
        log_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetReplicationGroupLogDeliveryConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        destination: _builtins.str,
        destination_type: _builtins.str,
        log_format: _builtins.str,
        log_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logFormat")
    def log_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetReplicationGroupNodeGroupConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        node_group_id: _builtins.str,
        primary_availability_zone: _builtins.str,
        primary_outpost_arn: _builtins.str,
        replica_availability_zones: Sequence[_builtins.str],
        replica_count: _builtins.int,
        replica_outpost_arns: Sequence[_builtins.str],
        slots: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupId")
    def node_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryAvailabilityZone")
    def primary_availability_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryOutpostArn")
    def primary_outpost_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicaAvailabilityZones")
    def replica_availability_zones(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="replicaOutpostArns")
    def replica_outpost_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def slots(self) -> _builtins.str: ...

@pulumi.output_type
class GetServerlessCacheCacheUsageLimitsResult(dict):
    def __init__(
        __self__,
        *,
        data_storage: outputs.GetServerlessCacheCacheUsageLimitsDataStorageResult,
        ecpu_per_second: outputs.GetServerlessCacheCacheUsageLimitsEcpuPerSecondResult,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStorage")
    def data_storage(
        self,
    ) -> outputs.GetServerlessCacheCacheUsageLimitsDataStorageResult: ...
    @_builtins.property
    @pulumi.getter(name="ecpuPerSecond")
    def ecpu_per_second(
        self,
    ) -> outputs.GetServerlessCacheCacheUsageLimitsEcpuPerSecondResult: ...

@pulumi.output_type
class GetServerlessCacheCacheUsageLimitsDataStorageResult(dict):
    def __init__(
        __self__, *, maximum: _builtins.int, minimum: _builtins.int, unit: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str: ...

@pulumi.output_type
class GetServerlessCacheCacheUsageLimitsEcpuPerSecondResult(dict):
    def __init__(
        __self__, *, maximum: _builtins.int, minimum: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> _builtins.int: ...

@pulumi.output_type
class GetServerlessCacheEndpointResult(dict):
    def __init__(__self__, *, address: _builtins.str, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetServerlessCacheReaderEndpointResult(dict):
    def __init__(__self__, *, address: _builtins.str, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetUserAuthenticationModeResult(dict):
    def __init__(
        __self__,
        *,
        password_count: Optional[_builtins.int] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="passwordCount")
    def password_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
