import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
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
        instance_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        shard_count: pulumi.Input[_builtins.int],
        authorization_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        automated_backup_config: Optional[
            pulumi.Input[InstanceAutomatedBackupConfigArgs]
        ] = ...,
        cross_instance_replication_config: Optional[
            pulumi.Input[InstanceCrossInstanceReplicationConfigArgs]
        ] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        desired_auto_created_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDesiredAutoCreatedEndpointArgs]]]
        ] = ...,
        desired_psc_auto_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDesiredPscAutoConnectionArgs]]]
        ] = ...,
        engine_configs: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_source: Optional[pulumi.Input[InstanceGcsSourceArgs]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        maintenance_policy: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]] = ...,
        maintenance_version: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_backup_source: Optional[
            pulumi.Input[InstanceManagedBackupSourceArgs]
        ] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        persistence_config: Optional[pulumi.Input[InstancePersistenceConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        server_ca_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        server_ca_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_distribution_config: Optional[
            pulumi.Input[InstanceZoneDistributionConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Input[_builtins.int]: ...
    @shard_count.setter
    def shard_count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorization_mode.setter
    def authorization_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="automatedBackupConfig")
    def automated_backup_config(
        self,
    ) -> Optional[pulumi.Input[InstanceAutomatedBackupConfigArgs]]: ...
    @automated_backup_config.setter
    def automated_backup_config(
        self, value: Optional[pulumi.Input[InstanceAutomatedBackupConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crossInstanceReplicationConfig")
    def cross_instance_replication_config(
        self,
    ) -> Optional[pulumi.Input[InstanceCrossInstanceReplicationConfigArgs]]: ...
    @cross_instance_replication_config.setter
    def cross_instance_replication_config(
        self, value: Optional[pulumi.Input[InstanceCrossInstanceReplicationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="desiredAutoCreatedEndpoints")
    def desired_auto_created_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceDesiredAutoCreatedEndpointArgs]]]
    ]: ...
    @desired_auto_created_endpoints.setter
    def desired_auto_created_endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDesiredAutoCreatedEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="desiredPscAutoConnections")
    @_utilities.deprecated(...)
    def desired_psc_auto_connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceDesiredPscAutoConnectionArgs]]]
    ]: ...
    @desired_psc_auto_connections.setter
    def desired_psc_auto_connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDesiredPscAutoConnectionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineConfigs")
    def engine_configs(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @engine_configs.setter
    def engine_configs(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcsSource")
    def gcs_source(self) -> Optional[pulumi.Input[InstanceGcsSourceArgs]]: ...
    @gcs_source.setter
    def gcs_source(self, value: Optional[pulumi.Input[InstanceGcsSourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="managedBackupSource")
    def managed_backup_source(
        self,
    ) -> Optional[pulumi.Input[InstanceManagedBackupSourceArgs]]: ...
    @managed_backup_source.setter
    def managed_backup_source(
        self, value: Optional[pulumi.Input[InstanceManagedBackupSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serverCaMode")
    def server_ca_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_ca_mode.setter
    def server_ca_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverCaPool")
    def server_ca_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_ca_pool.setter
    def server_ca_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="zoneDistributionConfig")
    def zone_distribution_config(
        self,
    ) -> Optional[pulumi.Input[InstanceZoneDistributionConfigArgs]]: ...
    @zone_distribution_config.setter
    def zone_distribution_config(
        self, value: Optional[pulumi.Input[InstanceZoneDistributionConfigArgs]]
    ): ...

@pulumi.input_type
class _InstanceState:
    def __init__(
        __self__,
        *,
        authorization_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        automated_backup_config: Optional[
            pulumi.Input[InstanceAutomatedBackupConfigArgs]
        ] = ...,
        available_maintenance_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        backup_collection: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_instance_replication_config: Optional[
            pulumi.Input[InstanceCrossInstanceReplicationConfigArgs]
        ] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        desired_auto_created_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDesiredAutoCreatedEndpointArgs]]]
        ] = ...,
        desired_psc_auto_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDesiredPscAutoConnectionArgs]]]
        ] = ...,
        discovery_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDiscoveryEndpointArgs]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_maintenance_version: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceEndpointArgs]]]
        ] = ...,
        engine_configs: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_source: Optional[pulumi.Input[InstanceGcsSourceArgs]] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[pulumi.Input[InstanceMaintenancePolicyArgs]] = ...,
        maintenance_schedules: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceMaintenanceScheduleArgs]]]
        ] = ...,
        maintenance_version: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_backup_source: Optional[
            pulumi.Input[InstanceManagedBackupSourceArgs]
        ] = ...,
        managed_server_cas: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceManagedServerCaArgs]]]
        ] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceNodeConfigArgs]]]
        ] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        persistence_config: Optional[pulumi.Input[InstancePersistenceConfigArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_attachment_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstancePscAttachmentDetailArgs]]]
        ] = ...,
        psc_auto_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstancePscAutoConnectionArgs]]]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        server_ca_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        server_ca_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        shard_count: Optional[pulumi.Input[_builtins.int]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceStateInfoArgs]]]
        ] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_distribution_config: Optional[
            pulumi.Input[InstanceZoneDistributionConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @authorization_mode.setter
    def authorization_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="automatedBackupConfig")
    def automated_backup_config(
        self,
    ) -> Optional[pulumi.Input[InstanceAutomatedBackupConfigArgs]]: ...
    @automated_backup_config.setter
    def automated_backup_config(
        self, value: Optional[pulumi.Input[InstanceAutomatedBackupConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availableMaintenanceVersions")
    def available_maintenance_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @available_maintenance_versions.setter
    def available_maintenance_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="backupCollection")
    def backup_collection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @backup_collection.setter
    def backup_collection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="crossInstanceReplicationConfig")
    def cross_instance_replication_config(
        self,
    ) -> Optional[pulumi.Input[InstanceCrossInstanceReplicationConfigArgs]]: ...
    @cross_instance_replication_config.setter
    def cross_instance_replication_config(
        self, value: Optional[pulumi.Input[InstanceCrossInstanceReplicationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="desiredAutoCreatedEndpoints")
    def desired_auto_created_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceDesiredAutoCreatedEndpointArgs]]]
    ]: ...
    @desired_auto_created_endpoints.setter
    def desired_auto_created_endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDesiredAutoCreatedEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="desiredPscAutoConnections")
    @_utilities.deprecated(...)
    def desired_psc_auto_connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceDesiredPscAutoConnectionArgs]]]
    ]: ...
    @desired_psc_auto_connections.setter
    def desired_psc_auto_connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDesiredPscAutoConnectionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="discoveryEndpoints")
    @_utilities.deprecated(...)
    def discovery_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceDiscoveryEndpointArgs]]]
    ]: ...
    @discovery_endpoints.setter
    def discovery_endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceDiscoveryEndpointArgs]]]
        ],
    ): ...
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
    @pulumi.getter(name="effectiveMaintenanceVersion")
    def effective_maintenance_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @effective_maintenance_version.setter
    def effective_maintenance_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEndpointArgs]]]]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceEndpointArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineConfigs")
    def engine_configs(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @engine_configs.setter
    def engine_configs(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcsSource")
    def gcs_source(self) -> Optional[pulumi.Input[InstanceGcsSourceArgs]]: ...
    @gcs_source.setter
    def gcs_source(self, value: Optional[pulumi.Input[InstanceGcsSourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="managedBackupSource")
    def managed_backup_source(
        self,
    ) -> Optional[pulumi.Input[InstanceManagedBackupSourceArgs]]: ...
    @managed_backup_source.setter
    def managed_backup_source(
        self, value: Optional[pulumi.Input[InstanceManagedBackupSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedServerCas")
    def managed_server_cas(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceManagedServerCaArgs]]]
    ]: ...
    @managed_server_cas.setter
    def managed_server_cas(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceManagedServerCaArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNodeConfigArgs]]]]: ...
    @node_configs.setter
    def node_configs(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceNodeConfigArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="pscAttachmentDetails")
    def psc_attachment_details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstancePscAttachmentDetailArgs]]]
    ]: ...
    @psc_attachment_details.setter
    def psc_attachment_details(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstancePscAttachmentDetailArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    @_utilities.deprecated(...)
    def psc_auto_connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstancePscAutoConnectionArgs]]]
    ]: ...
    @psc_auto_connections.setter
    def psc_auto_connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstancePscAutoConnectionArgs]]]
        ],
    ): ...
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
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="serverCaMode")
    def server_ca_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_ca_mode.setter
    def server_ca_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serverCaPool")
    def server_ca_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @server_ca_pool.setter
    def server_ca_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shard_count.setter
    def shard_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateInfos")
    def state_infos(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InstanceStateInfoArgs]]]]: ...
    @state_infos.setter
    def state_infos(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InstanceStateInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transit_encryption_mode.setter
    def transit_encryption_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="zoneDistributionConfig")
    def zone_distribution_config(
        self,
    ) -> Optional[pulumi.Input[InstanceZoneDistributionConfigArgs]]: ...
    @zone_distribution_config.setter
    def zone_distribution_config(
        self, value: Optional[pulumi.Input[InstanceZoneDistributionConfigArgs]]
    ): ...

@pulumi.type_token("gcp:memorystore/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        authorization_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        automated_backup_config: Optional[
            pulumi.Input[
                Union[
                    InstanceAutomatedBackupConfigArgs,
                    InstanceAutomatedBackupConfigArgsDict,
                ]
            ]
        ] = ...,
        cross_instance_replication_config: Optional[
            pulumi.Input[
                Union[
                    InstanceCrossInstanceReplicationConfigArgs,
                    InstanceCrossInstanceReplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        desired_auto_created_endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceDesiredAutoCreatedEndpointArgs,
                            InstanceDesiredAutoCreatedEndpointArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        desired_psc_auto_connections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceDesiredPscAutoConnectionArgs,
                            InstanceDesiredPscAutoConnectionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        engine_configs: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_source: Optional[
            pulumi.Input[Union[InstanceGcsSourceArgs, InstanceGcsSourceArgsDict]]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_policy: Optional[
            pulumi.Input[
                Union[InstanceMaintenancePolicyArgs, InstanceMaintenancePolicyArgsDict]
            ]
        ] = ...,
        maintenance_version: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_backup_source: Optional[
            pulumi.Input[
                Union[
                    InstanceManagedBackupSourceArgs, InstanceManagedBackupSourceArgsDict
                ]
            ]
        ] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        persistence_config: Optional[
            pulumi.Input[
                Union[InstancePersistenceConfigArgs, InstancePersistenceConfigArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        server_ca_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        server_ca_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        shard_count: Optional[pulumi.Input[_builtins.int]] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_distribution_config: Optional[
            pulumi.Input[
                Union[
                    InstanceZoneDistributionConfigArgs,
                    InstanceZoneDistributionConfigArgsDict,
                ]
            ]
        ] = ...,
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
        authorization_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        automated_backup_config: Optional[
            pulumi.Input[
                Union[
                    InstanceAutomatedBackupConfigArgs,
                    InstanceAutomatedBackupConfigArgsDict,
                ]
            ]
        ] = ...,
        available_maintenance_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        backup_collection: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_instance_replication_config: Optional[
            pulumi.Input[
                Union[
                    InstanceCrossInstanceReplicationConfigArgs,
                    InstanceCrossInstanceReplicationConfigArgsDict,
                ]
            ]
        ] = ...,
        deletion_protection_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        desired_auto_created_endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceDesiredAutoCreatedEndpointArgs,
                            InstanceDesiredAutoCreatedEndpointArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        desired_psc_auto_connections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceDesiredPscAutoConnectionArgs,
                            InstanceDesiredPscAutoConnectionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        discovery_endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceDiscoveryEndpointArgs,
                            InstanceDiscoveryEndpointArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_maintenance_version: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[InstanceEndpointArgs, InstanceEndpointArgsDict]]
                ]
            ]
        ] = ...,
        engine_configs: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_source: Optional[
            pulumi.Input[Union[InstanceGcsSourceArgs, InstanceGcsSourceArgsDict]]
        ] = ...,
        instance_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
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
        managed_backup_source: Optional[
            pulumi.Input[
                Union[
                    InstanceManagedBackupSourceArgs, InstanceManagedBackupSourceArgsDict
                ]
            ]
        ] = ...,
        managed_server_cas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceManagedServerCaArgs, InstanceManagedServerCaArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        node_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[InstanceNodeConfigArgs, InstanceNodeConfigArgsDict]
                    ]
                ]
            ]
        ] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        persistence_config: Optional[
            pulumi.Input[
                Union[InstancePersistenceConfigArgs, InstancePersistenceConfigArgsDict]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_attachment_details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstancePscAttachmentDetailArgs,
                            InstancePscAttachmentDetailArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        psc_auto_connections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstancePscAutoConnectionArgs,
                            InstancePscAutoConnectionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        server_ca_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        server_ca_pool: Optional[pulumi.Input[_builtins.str]] = ...,
        shard_count: Optional[pulumi.Input[_builtins.int]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[InstanceStateInfoArgs, InstanceStateInfoArgsDict]
                    ]
                ]
            ]
        ] = ...,
        transit_encryption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        zone_distribution_config: Optional[
            pulumi.Input[
                Union[
                    InstanceZoneDistributionConfigArgs,
                    InstanceZoneDistributionConfigArgsDict,
                ]
            ]
        ] = ...,
    ) -> Instance: ...
    @_builtins.property
    @pulumi.getter(name="authorizationMode")
    def authorization_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="automatedBackupConfig")
    def automated_backup_config(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceAutomatedBackupConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="availableMaintenanceVersions")
    def available_maintenance_versions(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="backupCollection")
    def backup_collection(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="crossInstanceReplicationConfig")
    def cross_instance_replication_config(
        self,
    ) -> pulumi.Output[outputs.InstanceCrossInstanceReplicationConfig]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtectionEnabled")
    def deletion_protection_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="desiredAutoCreatedEndpoints")
    def desired_auto_created_endpoints(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.InstanceDesiredAutoCreatedEndpoint]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="desiredPscAutoConnections")
    @_utilities.deprecated(...)
    def desired_psc_auto_connections(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.InstanceDesiredPscAutoConnection]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryEndpoints")
    @_utilities.deprecated(...)
    def discovery_endpoints(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceDiscoveryEndpoint]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveMaintenanceVersion")
    def effective_maintenance_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Sequence[outputs.InstanceEndpoint]]: ...
    @_builtins.property
    @pulumi.getter(name="engineConfigs")
    def engine_configs(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gcsSource")
    def gcs_source(self) -> pulumi.Output[Optional[outputs.InstanceGcsSource]]: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
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
    def maintenance_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="managedBackupSource")
    def managed_backup_source(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceManagedBackupSource]]: ...
    @_builtins.property
    @pulumi.getter(name="managedServerCas")
    def managed_server_cas(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceManagedServerCa]]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeConfigs")
    def node_configs(self) -> pulumi.Output[Sequence[outputs.InstanceNodeConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="persistenceConfig")
    def persistence_config(
        self,
    ) -> pulumi.Output[outputs.InstancePersistenceConfig]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pscAttachmentDetails")
    def psc_attachment_details(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstancePscAttachmentDetail]]: ...
    @_builtins.property
    @pulumi.getter(name="pscAutoConnections")
    @_utilities.deprecated(...)
    def psc_auto_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstancePscAutoConnection]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="serverCaMode")
    def server_ca_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serverCaPool")
    def server_ca_pool(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateInfos")
    def state_infos(self) -> pulumi.Output[Sequence[outputs.InstanceStateInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionMode")
    def transit_encryption_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneDistributionConfig")
    def zone_distribution_config(
        self,
    ) -> pulumi.Output[outputs.InstanceZoneDistributionConfig]: ...
