

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterClusterNodeArgs', 'ClusterClusterNodeArgsDict', 'EndpointAccessVpcEndpointArgs', 'EndpointAccessVpcEndpointArgsDict', 'EndpointAccessVpcEndpointNetworkInterfaceArgs', 'EndpointAccessVpcEndpointNetworkInterfaceArgsDict', 'IdcApplicationAuthorizedTokenIssuerArgs', 'IdcApplicationAuthorizedTokenIssuerArgsDict', 'IdcApplicationServiceIntegrationArgs', 'IdcApplicationServiceIntegrationArgsDict', 'IdcApplicationServiceIntegrationLakeFormationArgs', ..., ..., ..., 'IdcApplicationServiceIntegrationRedshiftArgs', 'IdcApplicationServiceIntegrationRedshiftArgsDict', ..., ..., 'IdcApplicationServiceIntegrationS3AccessGrantsArgs', ..., ..., ..., 'IntegrationTimeoutsArgs', 'IntegrationTimeoutsArgsDict', 'ParameterGroupParameterArgs', 'ParameterGroupParameterArgsDict', 'ScheduledActionTargetActionArgs', 'ScheduledActionTargetActionArgsDict', 'ScheduledActionTargetActionPauseClusterArgs', 'ScheduledActionTargetActionPauseClusterArgsDict', 'ScheduledActionTargetActionResizeClusterArgs', 'ScheduledActionTargetActionResizeClusterArgsDict', 'ScheduledActionTargetActionResumeClusterArgs', 'ScheduledActionTargetActionResumeClusterArgsDict']
class ClusterClusterNodeArgsDict(TypedDict):
    node_role: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    public_ip_address: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ClusterClusterNodeArgs:
    def __init__(__self__, *, node_role: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., public_ip_address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeRole")
    def node_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_role.setter
    def node_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpAddress")
    def public_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_ip_address.setter
    def public_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointAccessVpcEndpointArgsDict(TypedDict):
    network_interfaces: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointNetworkInterfaceArgsDict]]]]
    vpc_endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointAccessVpcEndpointArgs:
    def __init__(__self__, *, network_interfaces: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointNetworkInterfaceArgs]]]] = ..., vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointNetworkInterfaceArgs]]]]:
        
        ...
    
    @network_interfaces.setter
    def network_interfaces(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointAccessVpcEndpointNetworkInterfaceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EndpointAccessVpcEndpointNetworkInterfaceArgsDict(TypedDict):
    availability_zone: NotRequired[pulumi.Input[_builtins.str]]
    network_interface_id: NotRequired[pulumi.Input[_builtins.str]]
    private_ip_address: NotRequired[pulumi.Input[_builtins.str]]
    subnet_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointAccessVpcEndpointNetworkInterfaceArgs:
    def __init__(__self__, *, availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_id: Optional[pulumi.Input[_builtins.str]] = ..., private_ip_address: Optional[pulumi.Input[_builtins.str]] = ..., subnet_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceId")
    def network_interface_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_id.setter
    def network_interface_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IdcApplicationAuthorizedTokenIssuerArgsDict(TypedDict):
    authorized_audiences_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    trusted_token_issuer_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IdcApplicationAuthorizedTokenIssuerArgs:
    def __init__(__self__, *, authorized_audiences_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., trusted_token_issuer_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizedAudiencesLists")
    def authorized_audiences_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @authorized_audiences_lists.setter
    def authorized_audiences_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedTokenIssuerArn")
    def trusted_token_issuer_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trusted_token_issuer_arn.setter
    def trusted_token_issuer_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IdcApplicationServiceIntegrationArgsDict(TypedDict):
    lake_formation: NotRequired[pulumi.Input[IdcApplicationServiceIntegrationLakeFormationArgsDict]]
    redshift: NotRequired[pulumi.Input[IdcApplicationServiceIntegrationRedshiftArgsDict]]
    s3_access_grants: NotRequired[pulumi.Input[IdcApplicationServiceIntegrationS3AccessGrantsArgsDict]]


@pulumi.input_type
class IdcApplicationServiceIntegrationArgs:
    def __init__(__self__, *, lake_formation: Optional[pulumi.Input[IdcApplicationServiceIntegrationLakeFormationArgs]] = ..., redshift: Optional[pulumi.Input[IdcApplicationServiceIntegrationRedshiftArgs]] = ..., s3_access_grants: Optional[pulumi.Input[IdcApplicationServiceIntegrationS3AccessGrantsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lakeFormation")
    def lake_formation(self) -> Optional[pulumi.Input[IdcApplicationServiceIntegrationLakeFormationArgs]]:
        
        ...
    
    @lake_formation.setter
    def lake_formation(self, value: Optional[pulumi.Input[IdcApplicationServiceIntegrationLakeFormationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redshift(self) -> Optional[pulumi.Input[IdcApplicationServiceIntegrationRedshiftArgs]]:
        
        ...
    
    @redshift.setter
    def redshift(self, value: Optional[pulumi.Input[IdcApplicationServiceIntegrationRedshiftArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3AccessGrants")
    def s3_access_grants(self) -> Optional[pulumi.Input[IdcApplicationServiceIntegrationS3AccessGrantsArgs]]:
        
        ...
    
    @s3_access_grants.setter
    def s3_access_grants(self, value: Optional[pulumi.Input[IdcApplicationServiceIntegrationS3AccessGrantsArgs]]): # -> None:
        ...
    


class IdcApplicationServiceIntegrationLakeFormationArgsDict(TypedDict):
    lake_formation_query: NotRequired[pulumi.Input[IdcApplicationServiceIntegrationLakeFormationLakeFormationQueryArgsDict]]


@pulumi.input_type
class IdcApplicationServiceIntegrationLakeFormationArgs:
    def __init__(__self__, *, lake_formation_query: Optional[pulumi.Input[IdcApplicationServiceIntegrationLakeFormationLakeFormationQueryArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lakeFormationQuery")
    def lake_formation_query(self) -> Optional[pulumi.Input[IdcApplicationServiceIntegrationLakeFormationLakeFormationQueryArgs]]:
        
        ...
    
    @lake_formation_query.setter
    def lake_formation_query(self, value: Optional[pulumi.Input[IdcApplicationServiceIntegrationLakeFormationLakeFormationQueryArgs]]): # -> None:
        ...
    


class IdcApplicationServiceIntegrationLakeFormationLakeFormationQueryArgsDict(TypedDict):
    authorization: pulumi.Input[_builtins.str]


@pulumi.input_type
class IdcApplicationServiceIntegrationLakeFormationLakeFormationQueryArgs:
    def __init__(__self__, *, authorization: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class IdcApplicationServiceIntegrationRedshiftArgsDict(TypedDict):
    connect: NotRequired[pulumi.Input[IdcApplicationServiceIntegrationRedshiftConnectArgsDict]]


@pulumi.input_type
class IdcApplicationServiceIntegrationRedshiftArgs:
    def __init__(__self__, *, connect: Optional[pulumi.Input[IdcApplicationServiceIntegrationRedshiftConnectArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connect(self) -> Optional[pulumi.Input[IdcApplicationServiceIntegrationRedshiftConnectArgs]]:
        
        ...
    
    @connect.setter
    def connect(self, value: Optional[pulumi.Input[IdcApplicationServiceIntegrationRedshiftConnectArgs]]): # -> None:
        ...
    


class IdcApplicationServiceIntegrationRedshiftConnectArgsDict(TypedDict):
    authorization: pulumi.Input[_builtins.str]


@pulumi.input_type
class IdcApplicationServiceIntegrationRedshiftConnectArgs:
    def __init__(__self__, *, authorization: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class IdcApplicationServiceIntegrationS3AccessGrantsArgsDict(TypedDict):
    read_write_access: NotRequired[pulumi.Input[IdcApplicationServiceIntegrationS3AccessGrantsReadWriteAccessArgsDict]]


@pulumi.input_type
class IdcApplicationServiceIntegrationS3AccessGrantsArgs:
    def __init__(__self__, *, read_write_access: Optional[pulumi.Input[IdcApplicationServiceIntegrationS3AccessGrantsReadWriteAccessArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readWriteAccess")
    def read_write_access(self) -> Optional[pulumi.Input[IdcApplicationServiceIntegrationS3AccessGrantsReadWriteAccessArgs]]:
        
        ...
    
    @read_write_access.setter
    def read_write_access(self, value: Optional[pulumi.Input[IdcApplicationServiceIntegrationS3AccessGrantsReadWriteAccessArgs]]): # -> None:
        ...
    


class IdcApplicationServiceIntegrationS3AccessGrantsReadWriteAccessArgsDict(TypedDict):
    authorization: pulumi.Input[_builtins.str]


@pulumi.input_type
class IdcApplicationServiceIntegrationS3AccessGrantsReadWriteAccessArgs:
    def __init__(__self__, *, authorization: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorization(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization.setter
    def authorization(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class IntegrationTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IntegrationTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ParameterGroupParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class ParameterGroupParameterArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ScheduledActionTargetActionArgsDict(TypedDict):
    pause_cluster: NotRequired[pulumi.Input[ScheduledActionTargetActionPauseClusterArgsDict]]
    resize_cluster: NotRequired[pulumi.Input[ScheduledActionTargetActionResizeClusterArgsDict]]
    resume_cluster: NotRequired[pulumi.Input[ScheduledActionTargetActionResumeClusterArgsDict]]


@pulumi.input_type
class ScheduledActionTargetActionArgs:
    def __init__(__self__, *, pause_cluster: Optional[pulumi.Input[ScheduledActionTargetActionPauseClusterArgs]] = ..., resize_cluster: Optional[pulumi.Input[ScheduledActionTargetActionResizeClusterArgs]] = ..., resume_cluster: Optional[pulumi.Input[ScheduledActionTargetActionResumeClusterArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pauseCluster")
    def pause_cluster(self) -> Optional[pulumi.Input[ScheduledActionTargetActionPauseClusterArgs]]:
        
        ...
    
    @pause_cluster.setter
    def pause_cluster(self, value: Optional[pulumi.Input[ScheduledActionTargetActionPauseClusterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resizeCluster")
    def resize_cluster(self) -> Optional[pulumi.Input[ScheduledActionTargetActionResizeClusterArgs]]:
        
        ...
    
    @resize_cluster.setter
    def resize_cluster(self, value: Optional[pulumi.Input[ScheduledActionTargetActionResizeClusterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resumeCluster")
    def resume_cluster(self) -> Optional[pulumi.Input[ScheduledActionTargetActionResumeClusterArgs]]:
        
        ...
    
    @resume_cluster.setter
    def resume_cluster(self, value: Optional[pulumi.Input[ScheduledActionTargetActionResumeClusterArgs]]): # -> None:
        ...
    


class ScheduledActionTargetActionPauseClusterArgsDict(TypedDict):
    cluster_identifier: pulumi.Input[_builtins.str]


@pulumi.input_type
class ScheduledActionTargetActionPauseClusterArgs:
    def __init__(__self__, *, cluster_identifier: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ScheduledActionTargetActionResizeClusterArgsDict(TypedDict):
    cluster_identifier: pulumi.Input[_builtins.str]
    classic: NotRequired[pulumi.Input[_builtins.bool]]
    cluster_type: NotRequired[pulumi.Input[_builtins.str]]
    node_type: NotRequired[pulumi.Input[_builtins.str]]
    number_of_nodes: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ScheduledActionTargetActionResizeClusterArgs:
    def __init__(__self__, *, cluster_identifier: pulumi.Input[_builtins.str], classic: Optional[pulumi.Input[_builtins.bool]] = ..., cluster_type: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., number_of_nodes: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def classic(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @classic.setter
    def classic(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_type.setter
    def cluster_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_nodes.setter
    def number_of_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ScheduledActionTargetActionResumeClusterArgsDict(TypedDict):
    cluster_identifier: pulumi.Input[_builtins.str]


@pulumi.input_type
class ScheduledActionTargetActionResumeClusterArgs:
    def __init__(__self__, *, cluster_identifier: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


