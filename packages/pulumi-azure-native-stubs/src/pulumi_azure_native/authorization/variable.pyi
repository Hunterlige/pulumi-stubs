

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
__all__ = ['VariableArgs', 'Variable']
@pulumi.input_type
class VariableArgs:
    def __init__(__self__, *, columns: pulumi.Input[Sequence[pulumi.Input[PolicyVariableColumnArgs]]], variable_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> pulumi.Input[Sequence[pulumi.Input[PolicyVariableColumnArgs]]]:
        
        ...
    
    @columns.setter
    def columns(self, value: pulumi.Input[Sequence[pulumi.Input[PolicyVariableColumnArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="variableName")
    def variable_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @variable_name.setter
    def variable_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:authorization:Variable")
class Variable(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., columns: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PolicyVariableColumnArgs, PolicyVariableColumnArgsDict]]]]] = ..., variable_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VariableArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Variable:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def columns(self) -> pulumi.Output[Sequence[outputs.PolicyVariableColumnResponse]]:
        
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
    


