import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ClusterArgs", "Cluster"]

@pulumi.input_type
class ClusterArgs:
    def __init__(
        __self__,
        *,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        az_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_discovery: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterLogDeliveryConfigurationArgs]]]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        num_cache_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        outpost_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        preferred_outpost_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_arns: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_window: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="azMode")
    def az_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @az_mode.setter
    def az_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @final_snapshot_identifier.setter
    def final_snapshot_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_discovery.setter
    def ip_discovery(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterLogDeliveryConfigurationArgs]]]
    ]: ...
    @log_delivery_configurations.setter
    def log_delivery_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterLogDeliveryConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_topic_arn.setter
    def notification_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numCacheNodes")
    def num_cache_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_cache_nodes.setter
    def num_cache_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="outpostMode")
    def outpost_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @outpost_mode.setter
    def outpost_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="preferredAvailabilityZones")
    def preferred_availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @preferred_availability_zones.setter
    def preferred_availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preferredOutpostArn")
    def preferred_outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_outpost_arn.setter
    def preferred_outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_group_id.setter
    def replication_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_arns.setter
    def snapshot_arns(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.input_type
class _ClusterState:
    def __init__(
        __self__,
        *,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        az_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_nodes: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterCacheNodeArgs]]]
        ] = ...,
        cluster_address: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_discovery: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterLogDeliveryConfigurationArgs]]]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        num_cache_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        outpost_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        preferred_outpost_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_arns: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_window: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="azMode")
    def az_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @az_mode.setter
    def az_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cacheNodes")
    def cache_nodes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCacheNodeArgs]]]]: ...
    @cache_nodes.setter
    def cache_nodes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCacheNodeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterAddress")
    def cluster_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_address.setter
    def cluster_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationEndpoint")
    def configuration_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_endpoint.setter
    def configuration_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="engineVersionActual")
    def engine_version_actual(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version_actual.setter
    def engine_version_actual(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @final_snapshot_identifier.setter
    def final_snapshot_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_discovery.setter
    def ip_discovery(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterLogDeliveryConfigurationArgs]]]
    ]: ...
    @log_delivery_configurations.setter
    def log_delivery_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterLogDeliveryConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_topic_arn.setter
    def notification_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numCacheNodes")
    def num_cache_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_cache_nodes.setter
    def num_cache_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="outpostMode")
    def outpost_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @outpost_mode.setter
    def outpost_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="preferredAvailabilityZones")
    def preferred_availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @preferred_availability_zones.setter
    def preferred_availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preferredOutpostArn")
    def preferred_outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_outpost_arn.setter
    def preferred_outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_group_id.setter
    def replication_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_arns.setter
    def snapshot_arns(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @transit_encryption_enabled.setter
    def transit_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

@pulumi.type_token("aws:elasticache/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        az_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_discovery: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterLogDeliveryConfigurationArgs,
                            ClusterLogDeliveryConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        num_cache_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        outpost_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        preferred_outpost_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_arns: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_window: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ClusterArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        az_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        cache_nodes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ClusterCacheNodeArgs, ClusterCacheNodeArgsDict]]
                ]
            ]
        ] = ...,
        cluster_address: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_discovery: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterLogDeliveryConfigurationArgs,
                            ClusterLogDeliveryConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        num_cache_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        outpost_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        preferred_outpost_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_arns: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_window: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> Cluster: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azMode")
    def az_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cacheNodes")
    def cache_nodes(self) -> pulumi.Output[Sequence[outputs.ClusterCacheNode]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterAddress")
    def cluster_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationEndpoint")
    def configuration_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersionActual")
    def engine_version_actual(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ClusterLogDeliveryConfiguration]]]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="numCacheNodes")
    def num_cache_nodes(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="outpostMode")
    def outpost_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="preferredAvailabilityZones")
    def preferred_availability_zones(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="preferredOutpostArn")
    def preferred_outpost_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionEnabled")
    def transit_encryption_enabled(self) -> pulumi.Output[_builtins.bool]: ...
