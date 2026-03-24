

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
__all__ = ['MetricDescriptorArgs', 'MetricDescriptor']
@pulumi.input_type
class MetricDescriptorArgs:
    def __init__(__self__, *, metric_kind: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], value_type: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[MetricDescriptorLabelArgs]]]] = ..., launch_stage: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[MetricDescriptorMetadataArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., unit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricKind")
    def metric_kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @metric_kind.setter
    def metric_kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value_type.setter
    def value_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricDescriptorLabelArgs]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricDescriptorLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_stage.setter
    def launch_stage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[MetricDescriptorMetadataArgs]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[MetricDescriptorMetadataArgs]]): # -> None:
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
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _MetricDescriptorState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[MetricDescriptorLabelArgs]]]] = ..., launch_stage: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[MetricDescriptorMetadataArgs]] = ..., metric_kind: Optional[pulumi.Input[_builtins.str]] = ..., monitored_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., unit: Optional[pulumi.Input[_builtins.str]] = ..., value_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetricDescriptorLabelArgs]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetricDescriptorLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_stage.setter
    def launch_stage(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[MetricDescriptorMetadataArgs]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[MetricDescriptorMetadataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricKind")
    def metric_kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metric_kind.setter
    def metric_kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoredResourceTypes")
    def monitored_resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @monitored_resource_types.setter
    def monitored_resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit.setter
    def unit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value_type.setter
    def value_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:monitoring/metricDescriptor:MetricDescriptor")
class MetricDescriptor(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MetricDescriptorLabelArgs, MetricDescriptorLabelArgsDict]]]]] = ..., launch_stage: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Union[MetricDescriptorMetadataArgs, MetricDescriptorMetadataArgsDict]]] = ..., metric_kind: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., unit: Optional[pulumi.Input[_builtins.str]] = ..., value_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MetricDescriptorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MetricDescriptorLabelArgs, MetricDescriptorLabelArgsDict]]]]] = ..., launch_stage: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[pulumi.Input[Union[MetricDescriptorMetadataArgs, MetricDescriptorMetadataArgsDict]]] = ..., metric_kind: Optional[pulumi.Input[_builtins.str]] = ..., monitored_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., unit: Optional[pulumi.Input[_builtins.str]] = ..., value_type: Optional[pulumi.Input[_builtins.str]] = ...) -> MetricDescriptor:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[outputs.MetricDescriptorLabel]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[outputs.MetricDescriptorMetadata]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricKind")
    def metric_kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoredResourceTypes")
    def monitored_resource_types(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


