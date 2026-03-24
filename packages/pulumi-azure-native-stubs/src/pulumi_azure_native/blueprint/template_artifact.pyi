

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['TemplateArtifactArgs', 'TemplateArtifact']
@pulumi.input_type
class TemplateArtifactArgs:
    def __init__(__self__, *, blueprint_name: pulumi.Input[_builtins.str], kind: pulumi.Input[_builtins.str], parameters: pulumi.Input[Mapping[str, pulumi.Input[ParameterValueArgs]]], resource_scope: pulumi.Input[_builtins.str], template: Any, artifact_name: Optional[pulumi.Input[_builtins.str]] = ..., depends_on: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blueprintName")
    def blueprint_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @blueprint_name.setter
    def blueprint_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Mapping[str, pulumi.Input[ParameterValueArgs]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[Mapping[str, pulumi.Input[ParameterValueArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceScope")
    def resource_scope(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_scope.setter
    def resource_scope(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> Any:
        
        ...
    
    @template.setter
    def template(self, value: Any): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactName")
    def artifact_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @artifact_name.setter
    def artifact_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @depends_on.setter
    def depends_on(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:blueprint:TemplateArtifact")
class TemplateArtifact(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., artifact_name: Optional[pulumi.Input[_builtins.str]] = ..., blueprint_name: Optional[pulumi.Input[_builtins.str]] = ..., depends_on: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union[ParameterValueArgs, ParameterValueArgsDict]]]]] = ..., resource_group: Optional[pulumi.Input[_builtins.str]] = ..., resource_scope: Optional[pulumi.Input[_builtins.str]] = ..., template: Optional[Any] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TemplateArtifactArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> TemplateArtifact:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
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
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Mapping[str, outputs.ParameterValueResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Output[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


