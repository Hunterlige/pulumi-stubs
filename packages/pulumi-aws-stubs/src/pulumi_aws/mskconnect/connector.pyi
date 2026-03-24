

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
__all__ = ['ConnectorArgs', 'Connector']
@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *, capacity: pulumi.Input[ConnectorCapacityArgs], connector_configuration: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]], kafka_cluster: pulumi.Input[ConnectorKafkaClusterArgs], kafka_cluster_client_authentication: pulumi.Input[ConnectorKafkaClusterClientAuthenticationArgs], kafka_cluster_encryption_in_transit: pulumi.Input[ConnectorKafkaClusterEncryptionInTransitArgs], kafkaconnect_version: pulumi.Input[_builtins.str], plugins: pulumi.Input[Sequence[pulumi.Input[ConnectorPluginArgs]]], service_execution_role_arn: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., log_delivery: Optional[pulumi.Input[ConnectorLogDeliveryArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., worker_configuration: Optional[pulumi.Input[ConnectorWorkerConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[ConnectorCapacityArgs]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: pulumi.Input[ConnectorCapacityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorConfiguration")
    def connector_configuration(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]:
        
        ...
    
    @connector_configuration.setter
    def connector_configuration(self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaCluster")
    def kafka_cluster(self) -> pulumi.Input[ConnectorKafkaClusterArgs]:
        
        ...
    
    @kafka_cluster.setter
    def kafka_cluster(self, value: pulumi.Input[ConnectorKafkaClusterArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaClusterClientAuthentication")
    def kafka_cluster_client_authentication(self) -> pulumi.Input[ConnectorKafkaClusterClientAuthenticationArgs]:
        
        ...
    
    @kafka_cluster_client_authentication.setter
    def kafka_cluster_client_authentication(self, value: pulumi.Input[ConnectorKafkaClusterClientAuthenticationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaClusterEncryptionInTransit")
    def kafka_cluster_encryption_in_transit(self) -> pulumi.Input[ConnectorKafkaClusterEncryptionInTransitArgs]:
        
        ...
    
    @kafka_cluster_encryption_in_transit.setter
    def kafka_cluster_encryption_in_transit(self, value: pulumi.Input[ConnectorKafkaClusterEncryptionInTransitArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaconnectVersion")
    def kafkaconnect_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kafkaconnect_version.setter
    def kafkaconnect_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def plugins(self) -> pulumi.Input[Sequence[pulumi.Input[ConnectorPluginArgs]]]:
        
        ...
    
    @plugins.setter
    def plugins(self, value: pulumi.Input[Sequence[pulumi.Input[ConnectorPluginArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_execution_role_arn.setter
    def service_execution_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDelivery")
    def log_delivery(self) -> Optional[pulumi.Input[ConnectorLogDeliveryArgs]]:
        
        ...
    
    @log_delivery.setter
    def log_delivery(self, value: Optional[pulumi.Input[ConnectorLogDeliveryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfiguration")
    def worker_configuration(self) -> Optional[pulumi.Input[ConnectorWorkerConfigurationArgs]]:
        
        ...
    
    @worker_configuration.setter
    def worker_configuration(self, value: Optional[pulumi.Input[ConnectorWorkerConfigurationArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectorState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity: Optional[pulumi.Input[ConnectorCapacityArgs]] = ..., connector_configuration: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., kafka_cluster: Optional[pulumi.Input[ConnectorKafkaClusterArgs]] = ..., kafka_cluster_client_authentication: Optional[pulumi.Input[ConnectorKafkaClusterClientAuthenticationArgs]] = ..., kafka_cluster_encryption_in_transit: Optional[pulumi.Input[ConnectorKafkaClusterEncryptionInTransitArgs]] = ..., kafkaconnect_version: Optional[pulumi.Input[_builtins.str]] = ..., log_delivery: Optional[pulumi.Input[ConnectorLogDeliveryArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., plugins: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectorPluginArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., worker_configuration: Optional[pulumi.Input[ConnectorWorkerConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[ConnectorCapacityArgs]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[ConnectorCapacityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorConfiguration")
    def connector_configuration(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @connector_configuration.setter
    def connector_configuration(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaCluster")
    def kafka_cluster(self) -> Optional[pulumi.Input[ConnectorKafkaClusterArgs]]:
        
        ...
    
    @kafka_cluster.setter
    def kafka_cluster(self, value: Optional[pulumi.Input[ConnectorKafkaClusterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaClusterClientAuthentication")
    def kafka_cluster_client_authentication(self) -> Optional[pulumi.Input[ConnectorKafkaClusterClientAuthenticationArgs]]:
        
        ...
    
    @kafka_cluster_client_authentication.setter
    def kafka_cluster_client_authentication(self, value: Optional[pulumi.Input[ConnectorKafkaClusterClientAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaClusterEncryptionInTransit")
    def kafka_cluster_encryption_in_transit(self) -> Optional[pulumi.Input[ConnectorKafkaClusterEncryptionInTransitArgs]]:
        
        ...
    
    @kafka_cluster_encryption_in_transit.setter
    def kafka_cluster_encryption_in_transit(self, value: Optional[pulumi.Input[ConnectorKafkaClusterEncryptionInTransitArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaconnectVersion")
    def kafkaconnect_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kafkaconnect_version.setter
    def kafkaconnect_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDelivery")
    def log_delivery(self) -> Optional[pulumi.Input[ConnectorLogDeliveryArgs]]:
        
        ...
    
    @log_delivery.setter
    def log_delivery(self, value: Optional[pulumi.Input[ConnectorLogDeliveryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def plugins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConnectorPluginArgs]]]]:
        
        ...
    
    @plugins.setter
    def plugins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConnectorPluginArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_execution_role_arn.setter
    def service_execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfiguration")
    def worker_configuration(self) -> Optional[pulumi.Input[ConnectorWorkerConfigurationArgs]]:
        
        ...
    
    @worker_configuration.setter
    def worker_configuration(self, value: Optional[pulumi.Input[ConnectorWorkerConfigurationArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:mskconnect/connector:Connector")
class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., capacity: Optional[pulumi.Input[Union[ConnectorCapacityArgs, ConnectorCapacityArgsDict]]] = ..., connector_configuration: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., kafka_cluster: Optional[pulumi.Input[Union[ConnectorKafkaClusterArgs, ConnectorKafkaClusterArgsDict]]] = ..., kafka_cluster_client_authentication: Optional[pulumi.Input[Union[ConnectorKafkaClusterClientAuthenticationArgs, ConnectorKafkaClusterClientAuthenticationArgsDict]]] = ..., kafka_cluster_encryption_in_transit: Optional[pulumi.Input[Union[ConnectorKafkaClusterEncryptionInTransitArgs, ConnectorKafkaClusterEncryptionInTransitArgsDict]]] = ..., kafkaconnect_version: Optional[pulumi.Input[_builtins.str]] = ..., log_delivery: Optional[pulumi.Input[Union[ConnectorLogDeliveryArgs, ConnectorLogDeliveryArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., plugins: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ConnectorPluginArgs, ConnectorPluginArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., worker_configuration: Optional[pulumi.Input[Union[ConnectorWorkerConfigurationArgs, ConnectorWorkerConfigurationArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., capacity: Optional[pulumi.Input[Union[ConnectorCapacityArgs, ConnectorCapacityArgsDict]]] = ..., connector_configuration: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., kafka_cluster: Optional[pulumi.Input[Union[ConnectorKafkaClusterArgs, ConnectorKafkaClusterArgsDict]]] = ..., kafka_cluster_client_authentication: Optional[pulumi.Input[Union[ConnectorKafkaClusterClientAuthenticationArgs, ConnectorKafkaClusterClientAuthenticationArgsDict]]] = ..., kafka_cluster_encryption_in_transit: Optional[pulumi.Input[Union[ConnectorKafkaClusterEncryptionInTransitArgs, ConnectorKafkaClusterEncryptionInTransitArgsDict]]] = ..., kafkaconnect_version: Optional[pulumi.Input[_builtins.str]] = ..., log_delivery: Optional[pulumi.Input[Union[ConnectorLogDeliveryArgs, ConnectorLogDeliveryArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., plugins: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ConnectorPluginArgs, ConnectorPluginArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., worker_configuration: Optional[pulumi.Input[Union[ConnectorWorkerConfigurationArgs, ConnectorWorkerConfigurationArgsDict]]] = ...) -> Connector:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Output[outputs.ConnectorCapacity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorConfiguration")
    def connector_configuration(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaCluster")
    def kafka_cluster(self) -> pulumi.Output[outputs.ConnectorKafkaCluster]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaClusterClientAuthentication")
    def kafka_cluster_client_authentication(self) -> pulumi.Output[outputs.ConnectorKafkaClusterClientAuthentication]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaClusterEncryptionInTransit")
    def kafka_cluster_encryption_in_transit(self) -> pulumi.Output[outputs.ConnectorKafkaClusterEncryptionInTransit]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaconnectVersion")
    def kafkaconnect_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logDelivery")
    def log_delivery(self) -> pulumi.Output[Optional[outputs.ConnectorLogDelivery]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plugins(self) -> pulumi.Output[Sequence[outputs.ConnectorPlugin]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceExecutionRoleArn")
    def service_execution_role_arn(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfiguration")
    def worker_configuration(self) -> pulumi.Output[Optional[outputs.ConnectorWorkerConfiguration]]:
        
        ...
    


