

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
__all__ = ['UnitKindArgs', 'UnitKind']
@pulumi.input_type
class UnitKindArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], saas: pulumi.Input[_builtins.str], unit_kind_id: pulumi.Input[_builtins.str], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., default_release: Optional[pulumi.Input[_builtins.str]] = ..., dependencies: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindDependencyArgs]]]] = ..., input_variable_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindInputVariableMappingArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., output_variable_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindOutputVariableMappingArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def saas(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @saas.setter
    def saas(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitKindId")
    def unit_kind_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @unit_kind_id.setter
    def unit_kind_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRelease")
    def default_release(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_release.setter
    def default_release(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindDependencyArgs]]]]:
        
        ...
    
    @dependencies.setter
    def dependencies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindDependencyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariableMappings")
    def input_variable_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindInputVariableMappingArgs]]]]:
        
        ...
    
    @input_variable_mappings.setter
    def input_variable_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindInputVariableMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputVariableMappings")
    def output_variable_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindOutputVariableMappingArgs]]]]:
        
        ...
    
    @output_variable_mappings.setter
    def output_variable_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindOutputVariableMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _UnitKindState:
    def __init__(__self__, *, annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., default_release: Optional[pulumi.Input[_builtins.str]] = ..., dependencies: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindDependencyArgs]]]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., input_variable_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindInputVariableMappingArgs]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., output_variable_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindOutputVariableMappingArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., saas: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., unit_kind_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRelease")
    def default_release(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_release.setter
    def default_release(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindDependencyArgs]]]]:
        
        ...
    
    @dependencies.setter
    def dependencies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindDependencyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_annotations.setter
    def effective_annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariableMappings")
    def input_variable_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindInputVariableMappingArgs]]]]:
        
        ...
    
    @input_variable_mappings.setter
    def input_variable_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindInputVariableMappingArgs]]]]): # -> None:
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
    @pulumi.getter(name="outputVariableMappings")
    def output_variable_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindOutputVariableMappingArgs]]]]:
        
        ...
    
    @output_variable_mappings.setter
    def output_variable_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UnitKindOutputVariableMappingArgs]]]]): # -> None:
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
    def saas(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @saas.setter
    def saas(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitKindId")
    def unit_kind_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unit_kind_id.setter
    def unit_kind_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:saasruntime/unitKind:UnitKind")
class UnitKind(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., default_release: Optional[pulumi.Input[_builtins.str]] = ..., dependencies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitKindDependencyArgs, UnitKindDependencyArgsDict]]]]] = ..., input_variable_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitKindInputVariableMappingArgs, UnitKindInputVariableMappingArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., output_variable_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitKindOutputVariableMappingArgs, UnitKindOutputVariableMappingArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., saas: Optional[pulumi.Input[_builtins.str]] = ..., unit_kind_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UnitKindArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., default_release: Optional[pulumi.Input[_builtins.str]] = ..., dependencies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitKindDependencyArgs, UnitKindDependencyArgsDict]]]]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., input_variable_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitKindInputVariableMappingArgs, UnitKindInputVariableMappingArgsDict]]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., output_variable_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UnitKindOutputVariableMappingArgs, UnitKindOutputVariableMappingArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., saas: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., unit_kind_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> UnitKind:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultRelease")
    def default_release(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dependencies(self) -> pulumi.Output[Optional[Sequence[outputs.UnitKindDependency]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariableMappings")
    def input_variable_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.UnitKindInputVariableMapping]]]:
        
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
    @pulumi.getter(name="outputVariableMappings")
    def output_variable_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.UnitKindOutputVariableMapping]]]:
        
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
    def saas(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unitKindId")
    def unit_kind_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


