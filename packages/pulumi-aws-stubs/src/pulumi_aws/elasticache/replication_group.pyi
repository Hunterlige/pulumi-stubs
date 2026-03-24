import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReplicationGroupArgs", "ReplicationGroup"]

@pulumi.input_type
class ReplicationGroupArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auth_token: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_token_update_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        automatic_failover_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cluster_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        data_tiering_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_discovery: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationGroupLogDeliveryConfigurationArgs]]
            ]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationGroupNodeGroupConfigurationArgs]]
            ]
        ] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        num_cache_clusters: Optional[pulumi.Input[_builtins.int]] = ...,
        num_node_groups: Optional[pulumi.Input[_builtins.int]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_cache_cluster_azs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas_per_node_group: Optional[pulumi.Input[_builtins.int]] = ...,
        replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_window: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        user_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_token.setter
    def auth_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authTokenUpdateStrategy")
    def auth_token_update_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_token_update_strategy.setter
    def auth_token_update_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @automatic_failover_enabled.setter
    def automatic_failover_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterMode")
    def cluster_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_mode.setter
    def cluster_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataTieringEnabled")
    def data_tiering_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @data_tiering_enabled.setter
    def data_tiering_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="globalReplicationGroupId")
    def global_replication_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_replication_group_id.setter
    def global_replication_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_discovery.setter
    def ip_discovery(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ReplicationGroupLogDeliveryConfigurationArgs]]
        ]
    ]: ...
    @log_delivery_configurations.setter
    def log_delivery_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationGroupLogDeliveryConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiAzEnabled")
    def multi_az_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_az_enabled.setter
    def multi_az_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupConfigurations")
    def node_group_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReplicationGroupNodeGroupConfigurationArgs]]]
    ]: ...
    @node_group_configurations.setter
    def node_group_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationGroupNodeGroupConfigurationArgs]]
            ]
        ],
    ): ...
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
    @pulumi.getter(name="numCacheClusters")
    def num_cache_clusters(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_cache_clusters.setter
    def num_cache_clusters(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="numNodeGroups")
    def num_node_groups(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_node_groups.setter
    def num_node_groups(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="preferredCacheClusterAzs")
    def preferred_cache_cluster_azs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @preferred_cache_cluster_azs.setter
    def preferred_cache_cluster_azs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replicas_per_node_group.setter
    def replicas_per_node_group(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="securityGroupNames")
    def security_group_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_names.setter
    def security_group_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @snapshot_arns.setter
    def snapshot_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userGroupIds")
    def user_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_group_ids.setter
    def user_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ReplicationGroupState:
    def __init__(
        __self__,
        *,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auth_token: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_token_update_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        automatic_failover_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cluster_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ...,
        data_tiering_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_discovery: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationGroupLogDeliveryConfigurationArgs]]
            ]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        member_clusters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        multi_az_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationGroupNodeGroupConfigurationArgs]]
            ]
        ] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        num_cache_clusters: Optional[pulumi.Input[_builtins.int]] = ...,
        num_node_groups: Optional[pulumi.Input[_builtins.int]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_cache_cluster_azs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        primary_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ...,
        reader_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas_per_node_group: Optional[pulumi.Input[_builtins.int]] = ...,
        replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_window: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        user_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
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
    @pulumi.getter(name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @at_rest_encryption_enabled.setter
    def at_rest_encryption_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_token.setter
    def auth_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="authTokenUpdateStrategy")
    def auth_token_update_strategy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_token_update_strategy.setter
    def auth_token_update_strategy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @automatic_failover_enabled.setter
    def automatic_failover_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterEnabled")
    def cluster_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cluster_enabled.setter
    def cluster_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterMode")
    def cluster_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_mode.setter
    def cluster_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationEndpointAddress")
    def configuration_endpoint_address(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_endpoint_address.setter
    def configuration_endpoint_address(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataTieringEnabled")
    def data_tiering_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @data_tiering_enabled.setter
    def data_tiering_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="globalReplicationGroupId")
    def global_replication_group_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_replication_group_id.setter
    def global_replication_group_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_discovery.setter
    def ip_discovery(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ReplicationGroupLogDeliveryConfigurationArgs]]
        ]
    ]: ...
    @log_delivery_configurations.setter
    def log_delivery_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationGroupLogDeliveryConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memberClusters")
    def member_clusters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @member_clusters.setter
    def member_clusters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="multiAzEnabled")
    def multi_az_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_az_enabled.setter
    def multi_az_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupConfigurations")
    def node_group_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReplicationGroupNodeGroupConfigurationArgs]]]
    ]: ...
    @node_group_configurations.setter
    def node_group_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ReplicationGroupNodeGroupConfigurationArgs]]
            ]
        ],
    ): ...
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
    @pulumi.getter(name="numCacheClusters")
    def num_cache_clusters(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_cache_clusters.setter
    def num_cache_clusters(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="numNodeGroups")
    def num_node_groups(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @num_node_groups.setter
    def num_node_groups(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="preferredCacheClusterAzs")
    def preferred_cache_cluster_azs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @preferred_cache_cluster_azs.setter
    def preferred_cache_cluster_azs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryEndpointAddress")
    def primary_endpoint_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_endpoint_address.setter
    def primary_endpoint_address(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readerEndpointAddress")
    def reader_endpoint_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reader_endpoint_address.setter
    def reader_endpoint_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replicas_per_node_group.setter
    def replicas_per_node_group(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="securityGroupNames")
    def security_group_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_names.setter
    def security_group_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @snapshot_arns.setter
    def snapshot_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
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
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userGroupIds")
    def user_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_group_ids.setter
    def user_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:elasticache/replicationGroup:ReplicationGroup")
class ReplicationGroup(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auth_token: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_token_update_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        automatic_failover_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cluster_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        data_tiering_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_discovery: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReplicationGroupLogDeliveryConfigurationArgs,
                            ReplicationGroupLogDeliveryConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReplicationGroupNodeGroupConfigurationArgs,
                            ReplicationGroupNodeGroupConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        num_cache_clusters: Optional[pulumi.Input[_builtins.int]] = ...,
        num_node_groups: Optional[pulumi.Input[_builtins.int]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_cache_cluster_azs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas_per_node_group: Optional[pulumi.Input[_builtins.int]] = ...,
        replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_window: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        user_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReplicationGroupArgs,
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
        at_rest_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        auth_token: Optional[pulumi.Input[_builtins.str]] = ...,
        auth_token_update_strategy: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_minor_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        automatic_failover_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cluster_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cluster_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ...,
        data_tiering_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_version_actual: Optional[pulumi.Input[_builtins.str]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        global_replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_discovery: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_delivery_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReplicationGroupLogDeliveryConfigurationArgs,
                            ReplicationGroupLogDeliveryConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        member_clusters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        multi_az_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        node_group_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReplicationGroupNodeGroupConfigurationArgs,
                            ReplicationGroupNodeGroupConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        num_cache_clusters: Optional[pulumi.Input[_builtins.int]] = ...,
        num_node_groups: Optional[pulumi.Input[_builtins.int]] = ...,
        parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_cache_cluster_azs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        primary_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ...,
        reader_endpoint_address: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas_per_node_group: Optional[pulumi.Input[_builtins.int]] = ...,
        replication_group_id: Optional[pulumi.Input[_builtins.str]] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        snapshot_name: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_retention_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_window: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        transit_encryption_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        user_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> ReplicationGroup: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="atRestEncryptionEnabled")
    def at_rest_encryption_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="authTokenUpdateStrategy")
    def auth_token_update_strategy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterEnabled")
    def cluster_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="clusterMode")
    def cluster_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationEndpointAddress")
    def configuration_endpoint_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataTieringEnabled")
    def data_tiering_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter(name="globalReplicationGroupId")
    def global_replication_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipDiscovery")
    def ip_discovery(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logDeliveryConfigurations")
    def log_delivery_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ReplicationGroupLogDeliveryConfiguration]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memberClusters")
    def member_clusters(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="multiAzEnabled")
    def multi_az_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeGroupConfigurations")
    def node_group_configurations(
        self,
    ) -> pulumi.Output[Sequence[outputs.ReplicationGroupNodeGroupConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="numCacheClusters")
    def num_cache_clusters(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="numNodeGroups")
    def num_node_groups(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="preferredCacheClusterAzs")
    def preferred_cache_cluster_azs(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="primaryEndpointAddress")
    def primary_endpoint_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="readerEndpointAddress")
    def reader_endpoint_address(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicasPerNodeGroup")
    def replicas_per_node_group(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupNames")
    def security_group_names(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotArns")
    def snapshot_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
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
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userGroupIds")
    def user_group_ids(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
