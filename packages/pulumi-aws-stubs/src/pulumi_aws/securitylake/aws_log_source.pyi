

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
__all__ = ['AwsLogSourceArgs', 'AwsLogSource']
@pulumi.input_type
class AwsLogSourceArgs:
    def __init__(__self__, *, source: pulumi.Input[AwsLogSourceSourceArgs], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[AwsLogSourceSourceArgs]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[AwsLogSourceSourceArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AwsLogSourceState:
    def __init__(__self__, *, region: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[AwsLogSourceSourceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[AwsLogSourceSourceArgs]]:
        
        ...
    
    @source.setter
    def source(self, value: Optional[pulumi.Input[AwsLogSourceSourceArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:securitylake/awsLogSource:AwsLogSource")
class AwsLogSource(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[AwsLogSourceSourceArgs, AwsLogSourceSourceArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AwsLogSourceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source: Optional[pulumi.Input[Union[AwsLogSourceSourceArgs, AwsLogSourceSourceArgsDict]]] = ...) -> AwsLogSource:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[outputs.AwsLogSourceSource]:
        
        ...
    


