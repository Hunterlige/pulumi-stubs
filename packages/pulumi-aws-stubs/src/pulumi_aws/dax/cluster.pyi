

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, cluster_name: pulumi.Input[_builtins.str], iam_role_arn: pulumi.Input[_builtins.str], node_type: pulumi.Input[_builtins.str], replication_factor: pulumi.Input[_builtins.int], availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_endpoint_encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., server_side_encryption: Optional[pulumi.Input[ClusterServerSideEncryptionArgs]] = ..., subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @replication_factor.setter
    def replication_factor(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpointEncryptionType")
    def cluster_endpoint_encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_endpoint_encryption_type.setter
    def cluster_endpoint_encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_topic_arn.setter
    def notification_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter_group_name.setter
    def parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> Optional[pulumi.Input[ClusterServerSideEncryptionArgs]]:
        
        ...
    
    @server_side_encryption.setter
    def server_side_encryption(self, value: Optional[pulumi.Input[ClusterServerSideEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_group_name.setter
    def subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_address: Optional[pulumi.Input[_builtins.str]] = ..., cluster_endpoint_encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., configuration_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., nodes: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeArgs]]]] = ..., notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_factor: Optional[pulumi.Input[_builtins.int]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., server_side_encryption: Optional[pulumi.Input[ClusterServerSideEncryptionArgs]] = ..., subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @availability_zones.setter
    def availability_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterAddress")
    def cluster_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_address.setter
    def cluster_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpointEncryptionType")
    def cluster_endpoint_encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_endpoint_encryption_type.setter
    def cluster_endpoint_encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationEndpoint")
    def configuration_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_endpoint.setter
    def configuration_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeArgs]]]]:
        
        ...
    
    @nodes.setter
    def nodes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_topic_arn.setter
    def notification_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter_group_name.setter
    def parameter_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replication_factor.setter
    def replication_factor(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> Optional[pulumi.Input[ClusterServerSideEncryptionArgs]]:
        
        ...
    
    @server_side_encryption.setter
    def server_side_encryption(self, value: Optional[pulumi.Input[ClusterServerSideEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnet_group_name.setter
    def subnet_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:dax/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_endpoint_encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_factor: Optional[pulumi.Input[_builtins.int]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., server_side_encryption: Optional[pulumi.Input[Union[ClusterServerSideEncryptionArgs, ClusterServerSideEncryptionArgsDict]]] = ..., subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_address: Optional[pulumi.Input[_builtins.str]] = ..., cluster_endpoint_encryption_type: Optional[pulumi.Input[_builtins.str]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., configuration_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[_builtins.str]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., nodes: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterNodeArgs, ClusterNodeArgsDict]]]]] = ..., notification_topic_arn: Optional[pulumi.Input[_builtins.str]] = ..., parameter_group_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replication_factor: Optional[pulumi.Input[_builtins.int]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., server_side_encryption: Optional[pulumi.Input[Union[ClusterServerSideEncryptionArgs, ClusterServerSideEncryptionArgsDict]]] = ..., subnet_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterAddress")
    def cluster_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpointEncryptionType")
    def cluster_endpoint_encryption_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationEndpoint")
    def configuration_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nodes(self) -> pulumi.Output[Sequence[outputs.ClusterNode]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationTopicArn")
    def notification_topic_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterGroupName")
    def parameter_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverSideEncryption")
    def server_side_encryption(self) -> pulumi.Output[Optional[outputs.ClusterServerSideEncryption]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetGroupName")
    def subnet_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


