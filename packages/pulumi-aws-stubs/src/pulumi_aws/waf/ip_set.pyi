

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
__all__ = ['IpSetArgs', 'IpSet']
@pulumi.input_type
class IpSetArgs:
    def __init__(__self__, *, ip_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input[IpSetIpSetDescriptorArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetDescriptors")
    def ip_set_descriptors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpSetIpSetDescriptorArgs]]]]:
        
        ...
    
    @ip_set_descriptors.setter
    def ip_set_descriptors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpSetIpSetDescriptorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _IpSetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., ip_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input[IpSetIpSetDescriptorArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetDescriptors")
    def ip_set_descriptors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpSetIpSetDescriptorArgs]]]]:
        
        ...
    
    @ip_set_descriptors.setter
    def ip_set_descriptors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpSetIpSetDescriptorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:waf/ipSet:IpSet")
class IpSet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., ip_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IpSetIpSetDescriptorArgs, IpSetIpSetDescriptorArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[IpSetArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., ip_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IpSetIpSetDescriptorArgs, IpSetIpSetDescriptorArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> IpSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetDescriptors")
    def ip_set_descriptors(self) -> pulumi.Output[Optional[Sequence[outputs.IpSetIpSetDescriptor]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


