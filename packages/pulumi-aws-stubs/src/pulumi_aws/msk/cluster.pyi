

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, broker_node_group_info: pulumi.Input[ClusterBrokerNodeGroupInfoArgs], kafka_version: pulumi.Input[_builtins.str], number_of_broker_nodes: pulumi.Input[_builtins.int], client_authentication: Optional[pulumi.Input[ClusterClientAuthenticationArgs]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., configuration_info: Optional[pulumi.Input[ClusterConfigurationInfoArgs]] = ..., encryption_info: Optional[pulumi.Input[ClusterEncryptionInfoArgs]] = ..., enhanced_monitoring: Optional[pulumi.Input[_builtins.str]] = ..., logging_info: Optional[pulumi.Input[ClusterLoggingInfoArgs]] = ..., open_monitoring: Optional[pulumi.Input[ClusterOpenMonitoringArgs]] = ..., rebalancing: Optional[pulumi.Input[ClusterRebalancingArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_mode: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerNodeGroupInfo")
    def broker_node_group_info(self) -> pulumi.Input[ClusterBrokerNodeGroupInfoArgs]:
        
        ...
    
    @broker_node_group_info.setter
    def broker_node_group_info(self, value: pulumi.Input[ClusterBrokerNodeGroupInfoArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaVersion")
    def kafka_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kafka_version.setter
    def kafka_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @number_of_broker_nodes.setter
    def number_of_broker_nodes(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> Optional[pulumi.Input[ClusterClientAuthenticationArgs]]:
        
        ...
    
    @client_authentication.setter
    def client_authentication(self, value: Optional[pulumi.Input[ClusterClientAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> Optional[pulumi.Input[ClusterConfigurationInfoArgs]]:
        
        ...
    
    @configuration_info.setter
    def configuration_info(self, value: Optional[pulumi.Input[ClusterConfigurationInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionInfo")
    def encryption_info(self) -> Optional[pulumi.Input[ClusterEncryptionInfoArgs]]:
        
        ...
    
    @encryption_info.setter
    def encryption_info(self, value: Optional[pulumi.Input[ClusterEncryptionInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedMonitoring")
    def enhanced_monitoring(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @enhanced_monitoring.setter
    def enhanced_monitoring(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingInfo")
    def logging_info(self) -> Optional[pulumi.Input[ClusterLoggingInfoArgs]]:
        
        ...
    
    @logging_info.setter
    def logging_info(self, value: Optional[pulumi.Input[ClusterLoggingInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openMonitoring")
    def open_monitoring(self) -> Optional[pulumi.Input[ClusterOpenMonitoringArgs]]:
        
        ...
    
    @open_monitoring.setter
    def open_monitoring(self, value: Optional[pulumi.Input[ClusterOpenMonitoringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rebalancing(self) -> Optional[pulumi.Input[ClusterRebalancingArgs]]:
        
        ...
    
    @rebalancing.setter
    def rebalancing(self, value: Optional[pulumi.Input[ClusterRebalancingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageMode")
    def storage_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_mode.setter
    def storage_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_public_sasl_iam: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_public_sasl_scram: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_public_tls: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_sasl_iam: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_sasl_scram: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_tls: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_vpc_connectivity_sasl_iam: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_vpc_connectivity_sasl_scram: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_vpc_connectivity_tls: Optional[pulumi.Input[_builtins.str]] = ..., broker_node_group_info: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoArgs]] = ..., client_authentication: Optional[pulumi.Input[ClusterClientAuthenticationArgs]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_uuid: Optional[pulumi.Input[_builtins.str]] = ..., configuration_info: Optional[pulumi.Input[ClusterConfigurationInfoArgs]] = ..., current_version: Optional[pulumi.Input[_builtins.str]] = ..., encryption_info: Optional[pulumi.Input[ClusterEncryptionInfoArgs]] = ..., enhanced_monitoring: Optional[pulumi.Input[_builtins.str]] = ..., kafka_version: Optional[pulumi.Input[_builtins.str]] = ..., logging_info: Optional[pulumi.Input[ClusterLoggingInfoArgs]] = ..., number_of_broker_nodes: Optional[pulumi.Input[_builtins.int]] = ..., open_monitoring: Optional[pulumi.Input[ClusterOpenMonitoringArgs]] = ..., rebalancing: Optional[pulumi.Input[ClusterRebalancingArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_mode: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zookeeper_connect_string: Optional[pulumi.Input[_builtins.str]] = ..., zookeeper_connect_string_tls: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokers")
    def bootstrap_brokers(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers.setter
    def bootstrap_brokers(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicSaslIam")
    def bootstrap_brokers_public_sasl_iam(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_public_sasl_iam.setter
    def bootstrap_brokers_public_sasl_iam(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicSaslScram")
    def bootstrap_brokers_public_sasl_scram(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_public_sasl_scram.setter
    def bootstrap_brokers_public_sasl_scram(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicTls")
    def bootstrap_brokers_public_tls(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_public_tls.setter
    def bootstrap_brokers_public_tls(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslIam")
    def bootstrap_brokers_sasl_iam(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_sasl_iam.setter
    def bootstrap_brokers_sasl_iam(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslScram")
    def bootstrap_brokers_sasl_scram(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_sasl_scram.setter
    def bootstrap_brokers_sasl_scram(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersTls")
    def bootstrap_brokers_tls(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_tls.setter
    def bootstrap_brokers_tls(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersVpcConnectivitySaslIam")
    def bootstrap_brokers_vpc_connectivity_sasl_iam(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_vpc_connectivity_sasl_iam.setter
    def bootstrap_brokers_vpc_connectivity_sasl_iam(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersVpcConnectivitySaslScram")
    def bootstrap_brokers_vpc_connectivity_sasl_scram(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_vpc_connectivity_sasl_scram.setter
    def bootstrap_brokers_vpc_connectivity_sasl_scram(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersVpcConnectivityTls")
    def bootstrap_brokers_vpc_connectivity_tls(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bootstrap_brokers_vpc_connectivity_tls.setter
    def bootstrap_brokers_vpc_connectivity_tls(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerNodeGroupInfo")
    def broker_node_group_info(self) -> Optional[pulumi.Input[ClusterBrokerNodeGroupInfoArgs]]:
        
        ...
    
    @broker_node_group_info.setter
    def broker_node_group_info(self, value: Optional[pulumi.Input[ClusterBrokerNodeGroupInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> Optional[pulumi.Input[ClusterClientAuthenticationArgs]]:
        
        ...
    
    @client_authentication.setter
    def client_authentication(self, value: Optional[pulumi.Input[ClusterClientAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_uuid.setter
    def cluster_uuid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> Optional[pulumi.Input[ClusterConfigurationInfoArgs]]:
        
        ...
    
    @configuration_info.setter
    def configuration_info(self, value: Optional[pulumi.Input[ClusterConfigurationInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @current_version.setter
    def current_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionInfo")
    def encryption_info(self) -> Optional[pulumi.Input[ClusterEncryptionInfoArgs]]:
        
        ...
    
    @encryption_info.setter
    def encryption_info(self, value: Optional[pulumi.Input[ClusterEncryptionInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedMonitoring")
    def enhanced_monitoring(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @enhanced_monitoring.setter
    def enhanced_monitoring(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaVersion")
    def kafka_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kafka_version.setter
    def kafka_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingInfo")
    def logging_info(self) -> Optional[pulumi.Input[ClusterLoggingInfoArgs]]:
        
        ...
    
    @logging_info.setter
    def logging_info(self, value: Optional[pulumi.Input[ClusterLoggingInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @number_of_broker_nodes.setter
    def number_of_broker_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openMonitoring")
    def open_monitoring(self) -> Optional[pulumi.Input[ClusterOpenMonitoringArgs]]:
        
        ...
    
    @open_monitoring.setter
    def open_monitoring(self, value: Optional[pulumi.Input[ClusterOpenMonitoringArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rebalancing(self) -> Optional[pulumi.Input[ClusterRebalancingArgs]]:
        
        ...
    
    @rebalancing.setter
    def rebalancing(self, value: Optional[pulumi.Input[ClusterRebalancingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageMode")
    def storage_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_mode.setter
    def storage_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter(name="zookeeperConnectString")
    def zookeeper_connect_string(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zookeeper_connect_string.setter
    def zookeeper_connect_string(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="zookeeperConnectStringTls")
    def zookeeper_connect_string_tls(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zookeeper_connect_string_tls.setter
    def zookeeper_connect_string_tls(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:msk/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., broker_node_group_info: Optional[pulumi.Input[Union[ClusterBrokerNodeGroupInfoArgs, ClusterBrokerNodeGroupInfoArgsDict]]] = ..., client_authentication: Optional[pulumi.Input[Union[ClusterClientAuthenticationArgs, ClusterClientAuthenticationArgsDict]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., configuration_info: Optional[pulumi.Input[Union[ClusterConfigurationInfoArgs, ClusterConfigurationInfoArgsDict]]] = ..., encryption_info: Optional[pulumi.Input[Union[ClusterEncryptionInfoArgs, ClusterEncryptionInfoArgsDict]]] = ..., enhanced_monitoring: Optional[pulumi.Input[_builtins.str]] = ..., kafka_version: Optional[pulumi.Input[_builtins.str]] = ..., logging_info: Optional[pulumi.Input[Union[ClusterLoggingInfoArgs, ClusterLoggingInfoArgsDict]]] = ..., number_of_broker_nodes: Optional[pulumi.Input[_builtins.int]] = ..., open_monitoring: Optional[pulumi.Input[Union[ClusterOpenMonitoringArgs, ClusterOpenMonitoringArgsDict]]] = ..., rebalancing: Optional[pulumi.Input[Union[ClusterRebalancingArgs, ClusterRebalancingArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_mode: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_public_sasl_iam: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_public_sasl_scram: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_public_tls: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_sasl_iam: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_sasl_scram: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_tls: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_vpc_connectivity_sasl_iam: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_vpc_connectivity_sasl_scram: Optional[pulumi.Input[_builtins.str]] = ..., bootstrap_brokers_vpc_connectivity_tls: Optional[pulumi.Input[_builtins.str]] = ..., broker_node_group_info: Optional[pulumi.Input[Union[ClusterBrokerNodeGroupInfoArgs, ClusterBrokerNodeGroupInfoArgsDict]]] = ..., client_authentication: Optional[pulumi.Input[Union[ClusterClientAuthenticationArgs, ClusterClientAuthenticationArgsDict]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., cluster_uuid: Optional[pulumi.Input[_builtins.str]] = ..., configuration_info: Optional[pulumi.Input[Union[ClusterConfigurationInfoArgs, ClusterConfigurationInfoArgsDict]]] = ..., current_version: Optional[pulumi.Input[_builtins.str]] = ..., encryption_info: Optional[pulumi.Input[Union[ClusterEncryptionInfoArgs, ClusterEncryptionInfoArgsDict]]] = ..., enhanced_monitoring: Optional[pulumi.Input[_builtins.str]] = ..., kafka_version: Optional[pulumi.Input[_builtins.str]] = ..., logging_info: Optional[pulumi.Input[Union[ClusterLoggingInfoArgs, ClusterLoggingInfoArgsDict]]] = ..., number_of_broker_nodes: Optional[pulumi.Input[_builtins.int]] = ..., open_monitoring: Optional[pulumi.Input[Union[ClusterOpenMonitoringArgs, ClusterOpenMonitoringArgsDict]]] = ..., rebalancing: Optional[pulumi.Input[Union[ClusterRebalancingArgs, ClusterRebalancingArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_mode: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zookeeper_connect_string: Optional[pulumi.Input[_builtins.str]] = ..., zookeeper_connect_string_tls: Optional[pulumi.Input[_builtins.str]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokers")
    def bootstrap_brokers(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicSaslIam")
    def bootstrap_brokers_public_sasl_iam(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicSaslScram")
    def bootstrap_brokers_public_sasl_scram(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersPublicTls")
    def bootstrap_brokers_public_tls(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslIam")
    def bootstrap_brokers_sasl_iam(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersSaslScram")
    def bootstrap_brokers_sasl_scram(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersTls")
    def bootstrap_brokers_tls(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersVpcConnectivitySaslIam")
    def bootstrap_brokers_vpc_connectivity_sasl_iam(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersVpcConnectivitySaslScram")
    def bootstrap_brokers_vpc_connectivity_sasl_scram(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootstrapBrokersVpcConnectivityTls")
    def bootstrap_brokers_vpc_connectivity_tls(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="brokerNodeGroupInfo")
    def broker_node_group_info(self) -> pulumi.Output[outputs.ClusterBrokerNodeGroupInfo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientAuthentication")
    def client_authentication(self) -> pulumi.Output[Optional[outputs.ClusterClientAuthentication]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterUuid")
    def cluster_uuid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> pulumi.Output[Optional[outputs.ClusterConfigurationInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionInfo")
    def encryption_info(self) -> pulumi.Output[Optional[outputs.ClusterEncryptionInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedMonitoring")
    def enhanced_monitoring(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaVersion")
    def kafka_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingInfo")
    def logging_info(self) -> pulumi.Output[Optional[outputs.ClusterLoggingInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openMonitoring")
    def open_monitoring(self) -> pulumi.Output[Optional[outputs.ClusterOpenMonitoring]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rebalancing(self) -> pulumi.Output[outputs.ClusterRebalancing]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageMode")
    def storage_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zookeeperConnectString")
    def zookeeper_connect_string(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="zookeeperConnectStringTls")
    def zookeeper_connect_string_tls(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


