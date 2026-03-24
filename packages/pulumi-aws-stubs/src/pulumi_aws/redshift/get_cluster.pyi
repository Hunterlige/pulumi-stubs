

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
    
    def __init__(__self__, allow_version_upgrade=..., aqua_configuration_status=..., arn=..., automated_snapshot_retention_period=..., availability_zone=..., availability_zone_relocation_enabled=..., bucket_name=..., cluster_identifier=..., cluster_namespace_arn=..., cluster_nodes=..., cluster_parameter_group_name=..., cluster_public_key=..., cluster_revision_number=..., cluster_subnet_group_name=..., cluster_type=..., cluster_version=..., database_name=..., default_iam_role_arn=..., elastic_ip=..., enable_logging=..., encrypted=..., endpoint=..., enhanced_vpc_routing=..., iam_roles=..., id=..., kms_key_id=..., log_destination_type=..., log_exports=..., maintenance_track_name=..., manual_snapshot_retention_period=..., master_username=..., multi_az=..., node_type=..., number_of_nodes=..., port=..., preferred_maintenance_window=..., publicly_accessible=..., region=..., s3_key_prefix=..., tags=..., vpc_id=..., vpc_security_group_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowVersionUpgrade")
    def allow_version_upgrade(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aquaConfigurationStatus")
    def aqua_configuration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedSnapshotRetentionPeriod")
    def automated_snapshot_retention_period(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRelocationEnabled")
    def availability_zone_relocation_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterNamespaceArn")
    def cluster_namespace_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterNodes")
    def cluster_nodes(self) -> Sequence[outputs.GetClusterClusterNodeResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterPublicKey")
    def cluster_public_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterRevisionNumber")
    def cluster_revision_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterSubnetGroupName")
    def cluster_subnet_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterVersion")
    def cluster_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultIamRoleArn")
    def default_iam_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elasticIp")
    def elastic_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> _builtins.bool:
        
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
    @pulumi.getter(name="logDestinationType")
    def log_destination_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logExports")
    def log_exports(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceTrackName")
    def maintenance_track_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manualSnapshotRetentionPeriod")
    def manual_snapshot_retention_period(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="masterUsername")
    def master_username(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3KeyPrefix")
    def s3_key_prefix(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
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

