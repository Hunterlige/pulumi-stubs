

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RuntimeManagementConfigArgs', 'RuntimeManagementConfig']
@pulumi.input_type
class RuntimeManagementConfigArgs:
    def __init__(__self__, *, function_name: pulumi.Input[_builtins.str], qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., update_runtime_on: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qualifier.setter
    def qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersionArn")
    def runtime_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_version_arn.setter
    def runtime_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateRuntimeOn")
    def update_runtime_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_runtime_on.setter
    def update_runtime_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RuntimeManagementConfigState:
    def __init__(__self__, *, function_arn: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., update_runtime_on: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_arn.setter
    def function_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @qualifier.setter
    def qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersionArn")
    def runtime_version_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @runtime_version_arn.setter
    def runtime_version_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateRuntimeOn")
    def update_runtime_on(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_runtime_on.setter
    def update_runtime_on(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class RuntimeManagementConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., update_runtime_on: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RuntimeManagementConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., function_arn: Optional[pulumi.Input[_builtins.str]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., runtime_version_arn: Optional[pulumi.Input[_builtins.str]] = ..., update_runtime_on: Optional[pulumi.Input[_builtins.str]] = ...) -> RuntimeManagementConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersionArn")
    def runtime_version_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateRuntimeOn")
    def update_runtime_on(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


