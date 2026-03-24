

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
__all__ = ['InstanceArgs', 'Instance']
@pulumi.input_type
class InstanceArgs:
    def __init__(__self__, *, config: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], autoscaling_config: Optional[pulumi.Input[InstanceAutoscalingConfigArgs]] = ..., default_backup_schedule_type: Optional[pulumi.Input[_builtins.str]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., num_nodes: Optional[pulumi.Input[_builtins.int]] = ..., processing_units: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @config.setter
    def config(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(self) -> Optional[pulumi.Input[InstanceAutoscalingConfigArgs]]:
        
        ...
    
    @autoscaling_config.setter
    def autoscaling_config(self, value: Optional[pulumi.Input[InstanceAutoscalingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBackupScheduleType")
    def default_backup_schedule_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_backup_schedule_type.setter
    def default_backup_schedule_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_nodes.setter
    def num_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingUnits")
    def processing_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @processing_units.setter
    def processing_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceState:
    def __init__(__self__, *, autoscaling_config: Optional[pulumi.Input[InstanceAutoscalingConfigArgs]] = ..., config: Optional[pulumi.Input[_builtins.str]] = ..., default_backup_schedule_type: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., num_nodes: Optional[pulumi.Input[_builtins.int]] = ..., processing_units: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(self) -> Optional[pulumi.Input[InstanceAutoscalingConfigArgs]]:
        
        ...
    
    @autoscaling_config.setter
    def autoscaling_config(self, value: Optional[pulumi.Input[InstanceAutoscalingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @config.setter
    def config(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBackupScheduleType")
    def default_backup_schedule_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_backup_schedule_type.setter
    def default_backup_schedule_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @num_nodes.setter
    def num_nodes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingUnits")
    def processing_units(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @processing_units.setter
    def processing_units(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    


@pulumi.type_token("gcp:spanner/instance:Instance")
class Instance(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_config: Optional[pulumi.Input[Union[InstanceAutoscalingConfigArgs, InstanceAutoscalingConfigArgsDict]]] = ..., config: Optional[pulumi.Input[_builtins.str]] = ..., default_backup_schedule_type: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., num_nodes: Optional[pulumi.Input[_builtins.int]] = ..., processing_units: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., autoscaling_config: Optional[pulumi.Input[Union[InstanceAutoscalingConfigArgs, InstanceAutoscalingConfigArgsDict]]] = ..., config: Optional[pulumi.Input[_builtins.str]] = ..., default_backup_schedule_type: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., force_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., num_nodes: Optional[pulumi.Input[_builtins.int]] = ..., processing_units: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> Instance:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoscalingConfig")
    def autoscaling_config(self) -> pulumi.Output[Optional[outputs.InstanceAutoscalingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBackupScheduleType")
    def default_backup_schedule_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingUnits")
    def processing_units(self) -> pulumi.Output[_builtins.int]:
        
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
    


