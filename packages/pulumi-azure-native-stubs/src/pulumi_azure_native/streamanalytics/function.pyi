

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FunctionInitArgs', 'Function']
@pulumi.input_type
class FunctionInitArgs:
    def __init__(__self__, *, job_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], function_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[AggregateFunctionPropertiesArgs, ScalarFunctionPropertiesArgs]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @job_name.setter
    def job_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def properties(self) -> Optional[pulumi.Input[Union[AggregateFunctionPropertiesArgs, ScalarFunctionPropertiesArgs]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Union[AggregateFunctionPropertiesArgs, ScalarFunctionPropertiesArgs]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:streamanalytics:Function")
class Function(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., job_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[Union[AggregateFunctionPropertiesArgs, AggregateFunctionPropertiesArgsDict], Union[ScalarFunctionPropertiesArgs, ScalarFunctionPropertiesArgsDict]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FunctionInitArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Function:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


