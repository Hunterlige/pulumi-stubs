import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InstanceArgs", "Instance"]

@pulumi.input_type
class InstanceArgs:
    def __init__(
        __self__,
        *,
        memory_size_gb: pulumi.Input[_builtins.int],
        alternative_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        authorized_network: Optional[pulumi.Input[_builtins.str]] = ...,
        connect_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]] = ...,
        maintenance_version: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        persistence_config: Optional[pulumi.Input[InstancePersistenceConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        read_replicas_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        redis_configs: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        redis_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        reserved_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> pulumi.Input[_builtins.int]: ...
    @memory_size_gb.setter
    def memory_size_gb(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="alternativeLocationId")
    def alternative_location_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alternative_location_id.setter
    def alternative_location_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authEnabled")
    def auth_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auth_enabled.setter
    def auth_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorized_network.setter
    def authorized_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectMode")
    def connect_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connect_mode.setter
    def connect_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_managed_key.setter
    def customer_managed_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_id.setter
    def location_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(
        self,
    ) -> Optional[pulumi.Input[InstanceMaintenancePolicyArgs]]: ...
    @maintenance_policy.setter
    def maintenance_policy(
        self, value: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_version.setter
    def maintenance_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="persistenceConfig")
    def persistence_config(
        self,
    ) -> Optional[pulumi.Input[InstancePersistenceConfigArgs]]: ...
    @persistence_config.setter
    def persistence_config(
        self, value: Optional[pulumi.Input[InstancePersistenceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="readReplicasMode")
    def read_replicas_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @read_replicas_mode.setter
    def read_replicas_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redisConfigs")
    def redis_configs(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @redis_configs.setter
    def redis_configs(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redis_version.setter
    def redis_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reserved_ip_range.setter
    def reserved_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryIpRange")
    def secondary_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_ip_range.setter
    def secondary_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _InstanceState:
    def __init__(
        __self__,
        *,
        alternative_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auth_string: Optional[pulumi.Input[_builtins.str]] = ...,
        authorized_network: Optional[pulumi.Input[_builtins.str]] = ...,
        connect_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        current_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_reserved_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]] = ...,
        maintenance_schedules: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceMaintenanceScheduleArgs]]]
        ] = ...,
        maintenance_version: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        nodes: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNodeArgs]]]] = ...,
        persistence_config: Optional[pulumi.Input[InstancePersistenceConfigArgs]] = ...,
        persistence_iam_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        read_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        read_endpoint_port: Optional[pulumi.Input[_builtins.int]] = ...,
        read_replicas_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        redis_configs: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        redis_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        reserved_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        server_ca_certs: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceServerCaCertArgs]]]
        ] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alternativeLocationId")
    def alternative_location_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alternative_location_id.setter
    def alternative_location_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authEnabled")
    def auth_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auth_enabled.setter
    def auth_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="authString")
    def auth_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_string.setter
    def auth_string(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorized_network.setter
    def authorized_network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectMode")
    def connect_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connect_mode.setter
    def connect_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="currentLocationId")
    def current_location_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @current_location_id.setter
    def current_location_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @customer_managed_key.setter
    def customer_managed_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveReservedIpRange")
    def effective_reserved_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effective_reserved_ip_range.setter
    def effective_reserved_ip_range(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location_id.setter
    def location_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(
        self,
    ) -> Optional[pulumi.Input[InstanceMaintenancePolicyArgs]]: ...
    @maintenance_policy.setter
    def maintenance_policy(
        self, value: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceMaintenanceScheduleArgs]]]
    ]: ...
    @maintenance_schedules.setter
    def maintenance_schedules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceMaintenanceScheduleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_version.setter
    def maintenance_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory_size_gb.setter
    def memory_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nodes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNodeArgs]]]]: ...
    @nodes.setter
    def nodes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNodeArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="persistenceConfig")
    def persistence_config(
        self,
    ) -> Optional[pulumi.Input[InstancePersistenceConfigArgs]]: ...
    @persistence_config.setter
    def persistence_config(
        self, value: Optional[pulumi.Input[InstancePersistenceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="persistenceIamIdentity")
    def persistence_iam_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @persistence_iam_identity.setter
    def persistence_iam_identity(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readEndpoint")
    def read_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @read_endpoint.setter
    def read_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="readEndpointPort")
    def read_endpoint_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @read_endpoint_port.setter
    def read_endpoint_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="readReplicasMode")
    def read_replicas_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @read_replicas_mode.setter
    def read_replicas_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redisConfigs")
    def redis_configs(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @redis_configs.setter
    def redis_configs(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redis_version.setter
    def redis_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reserved_ip_range.setter
    def reserved_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryIpRange")
    def secondary_ip_range(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_ip_range.setter
    def secondary_ip_range(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverCaCerts")
    def server_ca_certs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceServerCaCertArgs]]]]: ...
    @server_ca_certs.setter
    def server_ca_certs(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceServerCaCertArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:redis/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alternative_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        authorized_network: Optional[pulumi.Input[_builtins.str]] = ...,
        connect_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[
            pulumi.Input[
                Union[InstanceMaintenancePolicyArgs, InstanceMaintenancePolicyArgsDict]
            ]
        ] = ...,
        maintenance_version: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        persistence_config: Optional[
            pulumi.Input[
                Union[InstancePersistenceConfigArgs, InstancePersistenceConfigArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        read_replicas_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        redis_configs: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        redis_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        reserved_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InstanceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        alternative_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auth_string: Optional[pulumi.Input[_builtins.str]] = ...,
        authorized_network: Optional[pulumi.Input[_builtins.str]] = ...,
        connect_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        current_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_reserved_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[
            pulumi.Input[
                Union[InstanceMaintenancePolicyArgs, InstanceMaintenancePolicyArgsDict]
            ]
        ] = ...,
        maintenance_schedules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceMaintenanceScheduleArgs,
                            InstanceMaintenanceScheduleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        maintenance_version: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        nodes: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[InstanceNodeArgs, InstanceNodeArgsDict]]]
            ]
        ] = ...,
        persistence_config: Optional[
            pulumi.Input[
                Union[InstancePersistenceConfigArgs, InstancePersistenceConfigArgsDict]
            ]
        ] = ...,
        persistence_iam_identity: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        read_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        read_endpoint_port: Optional[pulumi.Input[_builtins.int]] = ...,
        read_replicas_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        redis_configs: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        redis_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        reserved_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_ip_range: Optional[pulumi.Input[_builtins.str]] = ...,
        server_ca_certs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[InstanceServerCaCertArgs, InstanceServerCaCertArgsDict]
                    ]
                ]
            ]
        ] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Instance: ...
    @_builtins.property
    @pulumi.getter(name="alternativeLocationId")
    def alternative_location_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authEnabled")
    def auth_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="authString")
    def auth_string(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizedNetwork")
    def authorized_network(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectMode")
    def connect_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currentLocationId")
    def current_location_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveReservedIpRange")
    def effective_reserved_ip_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="locationId")
    def location_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenancePolicy")
    def maintenance_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceMaintenancePolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceSchedules")
    def maintenance_schedules(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceMaintenanceSchedule]]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceVersion")
    def maintenance_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memorySizeGb")
    def memory_size_gb(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> pulumi.Output[Sequence[outputs.InstanceNode]]: ...
    @_builtins.property
    @pulumi.getter(name="persistenceConfig")
    def persistence_config(
        self,
    ) -> pulumi.Output[outputs.InstancePersistenceConfig]: ...
    @_builtins.property
    @pulumi.getter(name="persistenceIamIdentity")
    def persistence_iam_identity(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="readEndpoint")
    def read_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readEndpointPort")
    def read_endpoint_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="readReplicasMode")
    def read_replicas_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redisConfigs")
    def redis_configs(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryIpRange")
    def secondary_ip_range(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverCaCerts")
    def server_ca_certs(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceServerCaCert]]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
