

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, parent: pulumi.Input[_builtins.str], autoscaling_settings: Optional[pulumi.Input[ClusterAutoscalingSettingsArgs]] = ..., datastore_mount_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterDatastoreMountConfigArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeTypeConfigArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingSettings")
    def autoscaling_settings(self) -> Optional[pulumi.Input[ClusterAutoscalingSettingsArgs]]:
        
        ...
    
    @autoscaling_settings.setter
    def autoscaling_settings(self, value: Optional[pulumi.Input[ClusterAutoscalingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastoreMountConfigs")
    def datastore_mount_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterDatastoreMountConfigArgs]]]]:
        
        ...
    
    @datastore_mount_configs.setter
    def datastore_mount_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterDatastoreMountConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeTypeConfigArgs]]]]:
        
        ...
    
    @node_type_configs.setter
    def node_type_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeTypeConfigArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, autoscaling_settings: Optional[pulumi.Input[ClusterAutoscalingSettingsArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., datastore_mount_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterDatastoreMountConfigArgs]]]] = ..., management: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeTypeConfigArgs]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingSettings")
    def autoscaling_settings(self) -> Optional[pulumi.Input[ClusterAutoscalingSettingsArgs]]:
        
        ...
    
    @autoscaling_settings.setter
    def autoscaling_settings(self, value: Optional[pulumi.Input[ClusterAutoscalingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastoreMountConfigs")
    def datastore_mount_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterDatastoreMountConfigArgs]]]]:
        
        ...
    
    @datastore_mount_configs.setter
    def datastore_mount_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterDatastoreMountConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def management(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @management.setter
    def management(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeTypeConfigArgs]]]]:
        
        ...
    
    @node_type_configs.setter
    def node_type_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNodeTypeConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:vmwareengine/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_settings: Optional[pulumi.Input[Union[ClusterAutoscalingSettingsArgs, ClusterAutoscalingSettingsArgsDict]]] = ..., datastore_mount_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterDatastoreMountConfigArgs, ClusterDatastoreMountConfigArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterNodeTypeConfigArgs, ClusterNodeTypeConfigArgsDict]]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_settings: Optional[pulumi.Input[Union[ClusterAutoscalingSettingsArgs, ClusterAutoscalingSettingsArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., datastore_mount_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterDatastoreMountConfigArgs, ClusterDatastoreMountConfigArgsDict]]]]] = ..., management: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_type_configs: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterNodeTypeConfigArgs, ClusterNodeTypeConfigArgsDict]]]]] = ..., parent: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingSettings")
    def autoscaling_settings(self) -> pulumi.Output[Optional[outputs.ClusterAutoscalingSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastoreMountConfigs")
    def datastore_mount_configs(self) -> pulumi.Output[Optional[Sequence[outputs.ClusterDatastoreMountConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def management(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeConfigs")
    def node_type_configs(self) -> pulumi.Output[Optional[Sequence[outputs.ClusterNodeTypeConfig]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


