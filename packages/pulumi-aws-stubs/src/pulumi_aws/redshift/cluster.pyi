import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
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
        cluster_identifier: pulumi.Input[_builtins.str],
        node_type: pulumi.Input[_builtins.str],
        allow_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        aqua_configuration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        automated_snapshot_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone_relocation_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_version: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        default_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        elastic_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_vpc_routing: Optional[pulumi.Input[_builtins.bool]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_track_name: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        manual_snapshot_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        owner_account: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Input[_builtins.str]: ...
    @node_type.setter
    def node_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowVersionUpgrade")
    def allow_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_version_upgrade.setter
    def allow_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="aquaConfigurationStatus")
    @_utilities.deprecated(...)
    def aqua_configuration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aqua_configuration_status.setter
    def aqua_configuration_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="automatedSnapshotRetentionPeriod")
    def automated_snapshot_retention_period(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @automated_snapshot_retention_period.setter
    def automated_snapshot_retention_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRelocationEnabled")
    def availability_zone_relocation_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @availability_zone_relocation_enabled.setter
    def availability_zone_relocation_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_parameter_group_name.setter
    def cluster_parameter_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterSubnetGroupName")
    def cluster_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_subnet_group_name.setter
    def cluster_subnet_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_type.setter
    def cluster_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_version.setter
    def cluster_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="elasticIp")
    def elastic_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elastic_ip.setter
    def elastic_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @final_snapshot_identifier.setter
    def final_snapshot_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @iam_roles.setter
    def iam_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceTrackName")
    def maintenance_track_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_track_name.setter
    def maintenance_track_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manageMasterPassword")
    def manage_master_password(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manage_master_password.setter
    def manage_master_password(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @manual_snapshot_retention_period.setter
    def manual_snapshot_retention_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password.setter
    def master_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordSecretKmsKeyId")
    def master_password_secret_kms_key_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password_secret_kms_key_id.setter
    def master_password_secret_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWo")
    def master_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password_wo.setter
    def master_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWoVersion")
    def master_password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @master_password_wo_version.setter
    def master_password_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_username.setter
    def master_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_nodes.setter
    def number_of_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_account.setter
    def owner_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_snapshot.setter
    def skip_final_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotArn")
    def snapshot_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_arn.setter
    def snapshot_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotClusterIdentifier")
    def snapshot_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_cluster_identifier.setter
    def snapshot_cluster_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_identifier.setter
    def snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ClusterState:
    def __init__(
        __self__,
        *,
        allow_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        aqua_configuration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        automated_snapshot_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone_relocation_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_namespace_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_nodes: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterClusterNodeArgs]]]
        ] = ...,
        cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_revision_number: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_version: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        default_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elastic_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_vpc_routing: Optional[pulumi.Input[_builtins.bool]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_track_name: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        manual_snapshot_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        owner_account: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowVersionUpgrade")
    def allow_version_upgrade(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_version_upgrade.setter
    def allow_version_upgrade(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_immediately.setter
    def apply_immediately(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="aquaConfigurationStatus")
    @_utilities.deprecated(...)
    def aqua_configuration_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @aqua_configuration_status.setter
    def aqua_configuration_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="automatedSnapshotRetentionPeriod")
    def automated_snapshot_retention_period(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @automated_snapshot_retention_period.setter
    def automated_snapshot_retention_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRelocationEnabled")
    def availability_zone_relocation_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @availability_zone_relocation_enabled.setter
    def availability_zone_relocation_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterNamespaceArn")
    def cluster_namespace_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_namespace_arn.setter
    def cluster_namespace_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterNodes")
    def cluster_nodes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterClusterNodeArgs]]]]: ...
    @cluster_nodes.setter
    def cluster_nodes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterClusterNodeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_parameter_group_name.setter
    def cluster_parameter_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterPublicKey")
    def cluster_public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_public_key.setter
    def cluster_public_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterRevisionNumber")
    def cluster_revision_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_revision_number.setter
    def cluster_revision_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterSubnetGroupName")
    def cluster_subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_subnet_group_name.setter
    def cluster_subnet_group_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_type.setter
    def cluster_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_version.setter
    def cluster_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_iam_role_arn.setter
    def default_iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name.setter
    def dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="elasticIp")
    def elastic_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @elastic_ip.setter
    def elastic_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @final_snapshot_identifier.setter
    def final_snapshot_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @iam_roles.setter
    def iam_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceTrackName")
    def maintenance_track_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maintenance_track_name.setter
    def maintenance_track_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manageMasterPassword")
    def manage_master_password(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @manage_master_password.setter
    def manage_master_password(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @manual_snapshot_retention_period.setter
    def manual_snapshot_retention_period(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password.setter
    def master_password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordSecretArn")
    def master_password_secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password_secret_arn.setter
    def master_password_secret_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordSecretKmsKeyId")
    def master_password_secret_kms_key_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password_secret_kms_key_id.setter
    def master_password_secret_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWo")
    def master_password_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_password_wo.setter
    def master_password_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWoVersion")
    def master_password_wo_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @master_password_wo_version.setter
    def master_password_wo_version(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_username.setter
    def master_username(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @multi_az.setter
    def multi_az(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_of_nodes.setter
    def number_of_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner_account.setter
    def owner_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_final_snapshot.setter
    def skip_final_snapshot(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotArn")
    def snapshot_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_arn.setter
    def snapshot_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotClusterIdentifier")
    def snapshot_cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_cluster_identifier.setter
    def snapshot_cluster_identifier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_identifier.setter
    def snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:redshift/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        aqua_configuration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        automated_snapshot_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone_relocation_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_version: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        default_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        elastic_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_vpc_routing: Optional[pulumi.Input[_builtins.bool]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_track_name: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        manual_snapshot_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        owner_account: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allow_version_upgrade: Optional[pulumi.Input[_builtins.bool]] = ...,
        apply_immediately: Optional[pulumi.Input[_builtins.bool]] = ...,
        aqua_configuration_status: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        automated_snapshot_retention_period: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone_relocation_enabled: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_namespace_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_nodes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ClusterClusterNodeArgs, ClusterClusterNodeArgsDict]
                    ]
                ]
            ]
        ] = ...,
        cluster_parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_revision_number: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_type: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_version: Optional[pulumi.Input[_builtins.str]] = ...,
        database_name: Optional[pulumi.Input[_builtins.str]] = ...,
        default_iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
        elastic_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        enhanced_vpc_routing: Optional[pulumi.Input[_builtins.bool]] = ...,
        final_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        iam_roles: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        maintenance_track_name: Optional[pulumi.Input[_builtins.str]] = ...,
        manage_master_password: Optional[pulumi.Input[_builtins.bool]] = ...,
        manual_snapshot_retention_period: Optional[pulumi.Input[_builtins.int]] = ...,
        master_password: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_secret_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        master_password_wo_version: Optional[pulumi.Input[_builtins.int]] = ...,
        master_username: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_az: Optional[pulumi.Input[_builtins.bool]] = ...,
        node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ...,
        owner_account: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        preferred_maintenance_window: Optional[pulumi.Input[_builtins.str]] = ...,
        publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        skip_final_snapshot: Optional[pulumi.Input[_builtins.bool]] = ...,
        snapshot_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Cluster: ...
    @_builtins.property
    @pulumi.getter(name="allowVersionUpgrade")
    def allow_version_upgrade(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="applyImmediately")
    def apply_immediately(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="aquaConfigurationStatus")
    @_utilities.deprecated(...)
    def aqua_configuration_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="automatedSnapshotRetentionPeriod")
    def automated_snapshot_retention_period(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRelocationEnabled")
    def availability_zone_relocation_enabled(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterNamespaceArn")
    def cluster_namespace_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterNodes")
    def cluster_nodes(self) -> pulumi.Output[Sequence[outputs.ClusterClusterNode]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterPublicKey")
    def cluster_public_key(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterRevisionNumber")
    def cluster_revision_number(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterSubnetGroupName")
    def cluster_subnet_group_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="elasticIp")
    def elastic_ip(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceTrackName")
    def maintenance_track_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="manageMasterPassword")
    def manage_master_password(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="masterPassword")
    def master_password(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordSecretArn")
    def master_password_secret_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordSecretKmsKeyId")
    def master_password_secret_kms_key_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWo")
    def master_password_wo(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="masterPasswordWoVersion")
    def master_password_wo_version(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipFinalSnapshot")
    def skip_final_snapshot(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotArn")
    def snapshot_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotClusterIdentifier")
    def snapshot_cluster_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotIdentifier")
    def snapshot_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
