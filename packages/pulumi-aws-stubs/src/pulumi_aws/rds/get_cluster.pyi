

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetClusterResult', 'AwaitableGetClusterResult', 'get_cluster', 'get_cluster_output']
@pulumi.output_type
class GetClusterResult:
    
    def __init__(__self__, arn=..., availability_zones=..., backtrack_window=..., backup_retention_period=..., cluster_identifier=..., cluster_members=..., cluster_resource_id=..., cluster_scalability_type=..., database_insights_mode=..., database_name=..., db_cluster_parameter_group_name=..., db_subnet_group_name=..., db_system_id=..., enabled_cloudwatch_logs_exports=..., endpoint=..., engine=..., engine_mode=..., engine_version=..., final_snapshot_identifier=..., hosted_zone_id=..., iam_database_authentication_enabled=..., iam_roles=..., id=..., kms_key_id=..., master_user_secrets=..., master_username=..., monitoring_interval=..., monitoring_role_arn=..., network_type=..., port=..., preferred_backup_window=..., preferred_maintenance_window=..., reader_endpoint=..., region=..., replication_source_identifier=..., storage_encrypted=..., tags=..., upgrade_rollout_order=..., vpc_security_group_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backtrackWindow")
    def backtrack_window(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterMembers")
    def cluster_members(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterScalabilityType")
    def cluster_scalability_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseInsightsMode")
    def database_insights_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterParameterGroupName")
    def db_cluster_parameter_group_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSubnetGroupName")
    def db_subnet_group_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledCloudwatchLogsExports")
    def enabled_cloudwatch_logs_exports(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineMode")
    def engine_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finalSnapshotIdentifier")
    def final_snapshot_identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamDatabaseAuthenticationEnabled")
    def iam_database_authentication_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoles")
    def iam_roles(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUserSecrets")
    def master_user_secrets(self) -> Sequence[outputs.GetClusterMasterUserSecretResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringInterval")
    def monitoring_interval(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringRoleArn")
    def monitoring_role_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerEndpoint")
    def reader_endpoint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationSourceIdentifier")
    def replication_source_identifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upgradeRolloutOrder")
    def upgrade_rollout_order(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> Sequence[_builtins.str]:
        ...
    


class AwaitableGetClusterResult(GetClusterResult):
    def __await__(self): # -> Generator[Never, Any, GetClusterResult]:
        ...
    


def get_cluster(cluster_identifier: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetClusterResult:
    
    ...

def get_cluster_output(cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetClusterResult]:
    
    ...

