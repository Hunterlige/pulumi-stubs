

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
__all__ = ['NodeTemplateArgs', 'NodeTemplate']
@pulumi.input_type
class NodeTemplateArgs:
    def __init__(__self__, *, accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateAcceleratorArgs]]]] = ..., cpu_overcommit_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disks: Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateDiskArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., node_type_flexibility: Optional[pulumi.Input[NodeTemplateNodeTypeFlexibilityArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_binding: Optional[pulumi.Input[NodeTemplateServerBindingArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateAcceleratorArgs]]]]:
        
        ...
    
    @accelerators.setter
    def accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateAcceleratorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOvercommitType")
    def cpu_overcommit_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu_overcommit_type.setter
    def cpu_overcommit_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateDiskArgs]]]]:
        
        ...
    
    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAffinityLabels")
    def node_affinity_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @node_affinity_labels.setter
    def node_affinity_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeFlexibility")
    def node_type_flexibility(self) -> Optional[pulumi.Input[NodeTemplateNodeTypeFlexibilityArgs]]:
        
        ...
    
    @node_type_flexibility.setter
    def node_type_flexibility(self, value: Optional[pulumi.Input[NodeTemplateNodeTypeFlexibilityArgs]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverBinding")
    def server_binding(self) -> Optional[pulumi.Input[NodeTemplateServerBindingArgs]]:
        
        ...
    
    @server_binding.setter
    def server_binding(self, value: Optional[pulumi.Input[NodeTemplateServerBindingArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _NodeTemplateState:
    def __init__(__self__, *, accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateAcceleratorArgs]]]] = ..., cpu_overcommit_type: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disks: Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateDiskArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., node_type_flexibility: Optional[pulumi.Input[NodeTemplateNodeTypeFlexibilityArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., server_binding: Optional[pulumi.Input[NodeTemplateServerBindingArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateAcceleratorArgs]]]]:
        
        ...
    
    @accelerators.setter
    def accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateAcceleratorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOvercommitType")
    def cpu_overcommit_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu_overcommit_type.setter
    def cpu_overcommit_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateDiskArgs]]]]:
        
        ...
    
    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NodeTemplateDiskArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAffinityLabels")
    def node_affinity_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @node_affinity_labels.setter
    def node_affinity_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_type.setter
    def node_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeFlexibility")
    def node_type_flexibility(self) -> Optional[pulumi.Input[NodeTemplateNodeTypeFlexibilityArgs]]:
        
        ...
    
    @node_type_flexibility.setter
    def node_type_flexibility(self, value: Optional[pulumi.Input[NodeTemplateNodeTypeFlexibilityArgs]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverBinding")
    def server_binding(self) -> Optional[pulumi.Input[NodeTemplateServerBindingArgs]]:
        
        ...
    
    @server_binding.setter
    def server_binding(self, value: Optional[pulumi.Input[NodeTemplateServerBindingArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/nodeTemplate:NodeTemplate")
class NodeTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NodeTemplateAcceleratorArgs, NodeTemplateAcceleratorArgsDict]]]]] = ..., cpu_overcommit_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NodeTemplateDiskArgs, NodeTemplateDiskArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., node_type_flexibility: Optional[pulumi.Input[Union[NodeTemplateNodeTypeFlexibilityArgs, NodeTemplateNodeTypeFlexibilityArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., server_binding: Optional[pulumi.Input[Union[NodeTemplateServerBindingArgs, NodeTemplateServerBindingArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[NodeTemplateArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NodeTemplateAcceleratorArgs, NodeTemplateAcceleratorArgsDict]]]]] = ..., cpu_overcommit_type: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NodeTemplateDiskArgs, NodeTemplateDiskArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_affinity_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., node_type: Optional[pulumi.Input[_builtins.str]] = ..., node_type_flexibility: Optional[pulumi.Input[Union[NodeTemplateNodeTypeFlexibilityArgs, NodeTemplateNodeTypeFlexibilityArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., server_binding: Optional[pulumi.Input[Union[NodeTemplateServerBindingArgs, NodeTemplateServerBindingArgsDict]]] = ...) -> NodeTemplate:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> pulumi.Output[Optional[Sequence[outputs.NodeTemplateAccelerator]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuOvercommitType")
    def cpu_overcommit_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disks(self) -> pulumi.Output[Optional[Sequence[outputs.NodeTemplateDisk]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeAffinityLabels")
    def node_affinity_labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeTypeFlexibility")
    def node_type_flexibility(self) -> pulumi.Output[Optional[outputs.NodeTemplateNodeTypeFlexibility]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverBinding")
    def server_binding(self) -> pulumi.Output[outputs.NodeTemplateServerBinding]:
        
        ...
    


