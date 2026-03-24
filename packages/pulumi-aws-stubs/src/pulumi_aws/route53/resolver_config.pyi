

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ResolverConfigArgs', 'ResolverConfig']
@pulumi.input_type
class ResolverConfigArgs:
    def __init__(__self__, *, autodefined_reverse_flag: pulumi.Input[_builtins.str], resource_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autodefinedReverseFlag")
    def autodefined_reverse_flag(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @autodefined_reverse_flag.setter
    def autodefined_reverse_flag(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ResolverConfigState:
    def __init__(__self__, *, autodefined_reverse_flag: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autodefinedReverseFlag")
    def autodefined_reverse_flag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @autodefined_reverse_flag.setter
    def autodefined_reverse_flag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:route53/resolverConfig:ResolverConfig")
class ResolverConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., autodefined_reverse_flag: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResolverConfigArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., autodefined_reverse_flag: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ...) -> ResolverConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autodefinedReverseFlag")
    def autodefined_reverse_flag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


