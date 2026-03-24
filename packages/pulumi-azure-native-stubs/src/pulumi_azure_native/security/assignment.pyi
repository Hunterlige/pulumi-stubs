

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AssignmentArgs', 'Assignment']
@pulumi.input_type
class AssignmentArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], additional_data: Optional[pulumi.Input[AssignmentPropertiesAdditionalDataArgs]] = ..., assigned_component: Optional[pulumi.Input[AssignedComponentItemArgs]] = ..., assigned_standard: Optional[pulumi.Input[AssignedStandardItemArgs]] = ..., assignment_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effect: Optional[pulumi.Input[_builtins.str]] = ..., expires_on: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[Any] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> Optional[pulumi.Input[AssignmentPropertiesAdditionalDataArgs]]:
        
        ...
    
    @additional_data.setter
    def additional_data(self, value: Optional[pulumi.Input[AssignmentPropertiesAdditionalDataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedComponent")
    def assigned_component(self) -> Optional[pulumi.Input[AssignedComponentItemArgs]]:
        
        ...
    
    @assigned_component.setter
    def assigned_component(self, value: Optional[pulumi.Input[AssignedComponentItemArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedStandard")
    def assigned_standard(self) -> Optional[pulumi.Input[AssignedStandardItemArgs]]:
        
        ...
    
    @assigned_standard.setter
    def assigned_standard(self, value: Optional[pulumi.Input[AssignedStandardItemArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentId")
    def assignment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assignment_id.setter
    def assignment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def effect(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @effect.setter
    def effect(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expires_on.setter
    def expires_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:security:Assignment")
class Assignment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_data: Optional[pulumi.Input[Union[AssignmentPropertiesAdditionalDataArgs, AssignmentPropertiesAdditionalDataArgsDict]]] = ..., assigned_component: Optional[pulumi.Input[Union[AssignedComponentItemArgs, AssignedComponentItemArgsDict]]] = ..., assigned_standard: Optional[pulumi.Input[Union[AssignedStandardItemArgs, AssignedStandardItemArgsDict]]] = ..., assignment_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effect: Optional[pulumi.Input[_builtins.str]] = ..., expires_on: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[Any] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AssignmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Assignment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> pulumi.Output[Optional[outputs.AssignmentPropertiesResponseAdditionalData]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedComponent")
    def assigned_component(self) -> pulumi.Output[Optional[outputs.AssignedComponentItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignedStandard")
    def assigned_standard(self) -> pulumi.Output[Optional[outputs.AssignedStandardItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
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
    def effect(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


