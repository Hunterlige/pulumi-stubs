

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
__all__ = ['VariableValueAtManagementGroupArgs', 'VariableValueAtManagementGroup']
@pulumi.input_type
class VariableValueAtManagementGroupArgs:
    def __init__(__self__, *, management_group_id: pulumi.Input[_builtins.str], values: pulumi.Input[Sequence[pulumi.Input[PolicyVariableValueColumnValueArgs]]], variable_name: pulumi.Input[_builtins.str], variable_value_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[PolicyVariableValueColumnValueArgs]]]:
        
        ...
    
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[PolicyVariableValueColumnValueArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="variableName")
    def variable_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @variable_name.setter
    def variable_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="variableValueName")
    def variable_value_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @variable_value_name.setter
    def variable_value_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class VariableValueAtManagementGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., management_group_id: Optional[pulumi.Input[_builtins.str]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyVariableValueColumnValueArgs, PolicyVariableValueColumnValueArgsDict]]]]] = ..., variable_name: Optional[pulumi.Input[_builtins.str]] = ..., variable_value_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VariableValueAtManagementGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VariableValueAtManagementGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Output[Sequence[outputs.PolicyVariableValueColumnValueResponse]]:
        
        ...
    


