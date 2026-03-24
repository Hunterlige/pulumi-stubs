

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['StaticIpAttachmentArgs', 'StaticIpAttachment']
@pulumi.input_type
class StaticIpAttachmentArgs:
    def __init__(__self__, *, instance_name: pulumi.Input[_builtins.str], static_ip_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_name.setter
    def instance_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpName")
    def static_ip_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @static_ip_name.setter
    def static_ip_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _StaticIpAttachmentState:
    def __init__(__self__, *, instance_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpName")
    def static_ip_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @static_ip_name.setter
    def static_ip_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class StaticIpAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., instance_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StaticIpAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., instance_name: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., static_ip_name: Optional[pulumi.Input[_builtins.str]] = ...) -> StaticIpAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="staticIpName")
    def static_ip_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


