

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
__all__ = ['DefaultCreditSpecificationArgs', 'DefaultCreditSpecification']
@pulumi.input_type
class DefaultCreditSpecificationArgs:
    def __init__(__self__, *, cpu_credits: pulumi.Input[_builtins.str], instance_family: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[DefaultCreditSpecificationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cpu_credits.setter
    def cpu_credits(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceFamily")
    def instance_family(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_family.setter
    def instance_family(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[DefaultCreditSpecificationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DefaultCreditSpecificationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _DefaultCreditSpecificationState:
    def __init__(__self__, *, cpu_credits: Optional[pulumi.Input[_builtins.str]] = ..., instance_family: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[DefaultCreditSpecificationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cpu_credits.setter
    def cpu_credits(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceFamily")
    def instance_family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_family.setter
    def instance_family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[DefaultCreditSpecificationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[DefaultCreditSpecificationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DefaultCreditSpecification(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cpu_credits: Optional[pulumi.Input[_builtins.str]] = ..., instance_family: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[DefaultCreditSpecificationTimeoutsArgs, DefaultCreditSpecificationTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DefaultCreditSpecificationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cpu_credits: Optional[pulumi.Input[_builtins.str]] = ..., instance_family: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[DefaultCreditSpecificationTimeoutsArgs, DefaultCreditSpecificationTimeoutsArgsDict]]] = ...) -> DefaultCreditSpecification:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cpuCredits")
    def cpu_credits(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceFamily")
    def instance_family(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.DefaultCreditSpecificationTimeouts]]:
        ...
    


