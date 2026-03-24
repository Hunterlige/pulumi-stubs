

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
__all__ = ['ConnectorArgs', 'Connector']
@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *, connect_cluster: pulumi.Input[_builtins.str], connector_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., task_restart_policy: Optional[pulumi.Input[ConnectorTaskRestartPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectCluster")
    def connect_cluster(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connect_cluster.setter
    def connect_cluster(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connector_id.setter
    def connector_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def configs(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @configs.setter
    def configs(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskRestartPolicy")
    def task_restart_policy(self) -> Optional[pulumi.Input[ConnectorTaskRestartPolicyArgs]]:
        
        ...
    
    @task_restart_policy.setter
    def task_restart_policy(self, value: Optional[pulumi.Input[ConnectorTaskRestartPolicyArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectorState:
    def __init__(__self__, *, configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., connect_cluster: Optional[pulumi.Input[_builtins.str]] = ..., connector_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., task_restart_policy: Optional[pulumi.Input[ConnectorTaskRestartPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configs(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @configs.setter
    def configs(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectCluster")
    def connect_cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connect_cluster.setter
    def connect_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_id.setter
    def connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskRestartPolicy")
    def task_restart_policy(self) -> Optional[pulumi.Input[ConnectorTaskRestartPolicyArgs]]:
        
        ...
    
    @task_restart_policy.setter
    def task_restart_policy(self, value: Optional[pulumi.Input[ConnectorTaskRestartPolicyArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:managedkafka/connector:Connector")
class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., connect_cluster: Optional[pulumi.Input[_builtins.str]] = ..., connector_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., task_restart_policy: Optional[pulumi.Input[Union[ConnectorTaskRestartPolicyArgs, ConnectorTaskRestartPolicyArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., configs: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., connect_cluster: Optional[pulumi.Input[_builtins.str]] = ..., connector_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., task_restart_policy: Optional[pulumi.Input[Union[ConnectorTaskRestartPolicyArgs, ConnectorTaskRestartPolicyArgsDict]]] = ...) -> Connector:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def configs(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectCluster")
    def connect_cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskRestartPolicy")
    def task_restart_policy(self) -> pulumi.Output[Optional[outputs.ConnectorTaskRestartPolicy]]:
        
        ...
    


