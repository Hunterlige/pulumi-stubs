

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
__all__ = ['EipDomainNameArgs', 'EipDomainName']
@pulumi.input_type
class EipDomainNameArgs:
    def __init__(__self__, *, allocation_id: pulumi.Input[_builtins.str], domain_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[EipDomainNameTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @allocation_id.setter
    def allocation_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[EipDomainNameTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[EipDomainNameTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _EipDomainNameState:
    def __init__(__self__, *, allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., ptr_record: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[EipDomainNameTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_id.setter
    def allocation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ptrRecord")
    def ptr_record(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ptr_record.setter
    def ptr_record(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[EipDomainNameTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[EipDomainNameTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/eipDomainName:EipDomainName")
class EipDomainName(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[EipDomainNameTimeoutsArgs, EipDomainNameTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EipDomainNameArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allocation_id: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., ptr_record: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[EipDomainNameTimeoutsArgs, EipDomainNameTimeoutsArgsDict]]] = ...) -> EipDomainName:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationId")
    def allocation_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ptrRecord")
    def ptr_record(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.EipDomainNameTimeouts]]:
        ...
    


