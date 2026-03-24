

import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ArmTemplateParameterArgs', 'ArmTemplateParameterArgsDict', 'ManagementAssociationPropertiesArgs', 'ManagementAssociationPropertiesArgsDict', 'ManagementConfigurationPropertiesArgs', 'ManagementConfigurationPropertiesArgsDict', 'SolutionPlanArgs', 'SolutionPlanArgsDict', 'SolutionPropertiesArgs', 'SolutionPropertiesArgsDict']
class ArmTemplateParameterArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ArmTemplateParameterArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagementAssociationPropertiesArgsDict(TypedDict):
    
    application_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class ManagementAssociationPropertiesArgs:
    def __init__(__self__, *, application_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ManagementConfigurationPropertiesArgsDict(TypedDict):
    
    parameters: pulumi.Input[Sequence[pulumi.Input[ArmTemplateParameterArgsDict]]]
    parent_resource_type: pulumi.Input[_builtins.str]
    template: Any
    application_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ManagementConfigurationPropertiesArgs:
    def __init__(__self__, *, parameters: pulumi.Input[Sequence[pulumi.Input[ArmTemplateParameterArgs]]], parent_resource_type: pulumi.Input[_builtins.str], template: Any, application_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Sequence[pulumi.Input[ArmTemplateParameterArgs]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: pulumi.Input[Sequence[pulumi.Input[ArmTemplateParameterArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentResourceType")
    def parent_resource_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent_resource_type.setter
    def parent_resource_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def template(self) -> Any:
        
        ...
    
    @template.setter
    def template(self, value: Any): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SolutionPlanArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    product: NotRequired[pulumi.Input[_builtins.str]]
    promotion_code: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SolutionPlanArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., product: Optional[pulumi.Input[_builtins.str]] = ..., promotion_code: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def product(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @product.setter
    def product(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SolutionPropertiesArgsDict(TypedDict):
    
    workspace_resource_id: pulumi.Input[_builtins.str]
    contained_resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    referenced_resources: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class SolutionPropertiesArgs:
    def __init__(__self__, *, workspace_resource_id: pulumi.Input[_builtins.str], contained_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., referenced_resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_resource_id.setter
    def workspace_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containedResources")
    def contained_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @contained_resources.setter
    def contained_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="referencedResources")
    def referenced_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @referenced_resources.setter
    def referenced_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


