

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FunctionEventInvokeConfigArgs', 'FunctionEventInvokeConfig']
@pulumi.input_type
class FunctionEventInvokeConfigArgs:
    def __init__(__self__, *, function_name: pulumi.Input[_builtins.str], destination_config: Optional[pulumi.Input[FunctionEventInvokeConfigDestinationConfigArgs]] = ..., maximum_event_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> Optional[pulumi.Input[FunctionEventInvokeConfigDestinationConfigArgs]]:
        
        ...
    
    @destination_config.setter
    def destination_config(self, value: Optional[pulumi.Input[FunctionEventInvokeConfigDestinationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    


@pulumi.input_type
class _FunctionEventInvokeConfigState:
    def __init__(__self__, *, destination_config: Optional[pulumi.Input[FunctionEventInvokeConfigDestinationConfigArgs]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., maximum_event_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> Optional[pulumi.Input[FunctionEventInvokeConfigDestinationConfigArgs]]:
        
        ...
    
    @destination_config.setter
    def destination_config(self, value: Optional[pulumi.Input[FunctionEventInvokeConfigDestinationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_name.setter
    def function_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    


@pulumi.type_token(...)
class FunctionEventInvokeConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., destination_config: Optional[pulumi.Input[Union[FunctionEventInvokeConfigDestinationConfigArgs, FunctionEventInvokeConfigDestinationConfigArgsDict]]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., maximum_event_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FunctionEventInvokeConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., destination_config: Optional[pulumi.Input[Union[FunctionEventInvokeConfigDestinationConfigArgs, FunctionEventInvokeConfigDestinationConfigArgsDict]]] = ..., function_name: Optional[pulumi.Input[_builtins.str]] = ..., maximum_event_age_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., maximum_retry_attempts: Optional[pulumi.Input[_builtins.int]] = ..., qualifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> FunctionEventInvokeConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationConfig")
    def destination_config(self) -> pulumi.Output[Optional[outputs.FunctionEventInvokeConfigDestinationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionName")
    def function_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


