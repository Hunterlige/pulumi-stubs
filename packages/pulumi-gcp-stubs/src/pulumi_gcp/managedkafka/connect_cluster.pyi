

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
__all__ = ['ConnectClusterArgs', 'ConnectCluster']
@pulumi.input_type
class ConnectClusterArgs:
    def __init__(__self__, *, capacity_config: pulumi.Input[ConnectClusterCapacityConfigArgs], connect_cluster_id: pulumi.Input[_builtins.str], gcp_config: pulumi.Input[ConnectClusterGcpConfigArgs], kafka_cluster: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityConfig")
    def capacity_config(self) -> pulumi.Input[ConnectClusterCapacityConfigArgs]:
        
        ...
    
    @capacity_config.setter
    def capacity_config(self, value: pulumi.Input[ConnectClusterCapacityConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectClusterId")
    def connect_cluster_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connect_cluster_id.setter
    def connect_cluster_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpConfig")
    def gcp_config(self) -> pulumi.Input[ConnectClusterGcpConfigArgs]:
        
        ...
    
    @gcp_config.setter
    def gcp_config(self, value: pulumi.Input[ConnectClusterGcpConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaCluster")
    def kafka_cluster(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kafka_cluster.setter
    def kafka_cluster(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectClusterState:
    def __init__(__self__, *, capacity_config: Optional[pulumi.Input[ConnectClusterCapacityConfigArgs]] = ..., connect_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gcp_config: Optional[pulumi.Input[ConnectClusterGcpConfigArgs]] = ..., kafka_cluster: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityConfig")
    def capacity_config(self) -> Optional[pulumi.Input[ConnectClusterCapacityConfigArgs]]:
        
        ...
    
    @capacity_config.setter
    def capacity_config(self, value: Optional[pulumi.Input[ConnectClusterCapacityConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectClusterId")
    def connect_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connect_cluster_id.setter
    def connect_cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpConfig")
    def gcp_config(self) -> Optional[pulumi.Input[ConnectClusterGcpConfigArgs]]:
        
        ...
    
    @gcp_config.setter
    def gcp_config(self, value: Optional[pulumi.Input[ConnectClusterGcpConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaCluster")
    def kafka_cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kafka_cluster.setter
    def kafka_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:managedkafka/connectCluster:ConnectCluster")
class ConnectCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., capacity_config: Optional[pulumi.Input[Union[ConnectClusterCapacityConfigArgs, ConnectClusterCapacityConfigArgsDict]]] = ..., connect_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., gcp_config: Optional[pulumi.Input[Union[ConnectClusterGcpConfigArgs, ConnectClusterGcpConfigArgsDict]]] = ..., kafka_cluster: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., capacity_config: Optional[pulumi.Input[Union[ConnectClusterCapacityConfigArgs, ConnectClusterCapacityConfigArgsDict]]] = ..., connect_cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., gcp_config: Optional[pulumi.Input[Union[ConnectClusterGcpConfigArgs, ConnectClusterGcpConfigArgsDict]]] = ..., kafka_cluster: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> ConnectCluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityConfig")
    def capacity_config(self) -> pulumi.Output[outputs.ConnectClusterCapacityConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectClusterId")
    def connect_cluster_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpConfig")
    def gcp_config(self) -> pulumi.Output[outputs.ConnectClusterGcpConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kafkaCluster")
    def kafka_cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


