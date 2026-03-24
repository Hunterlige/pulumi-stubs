

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['Disk_attachmentArgs', 'Disk_attachment']
@pulumi.input_type
class Disk_attachmentArgs:
    def __init__(__self__, *, disk_name: pulumi.Input[_builtins.str], disk_path: pulumi.Input[_builtins.str], instance_name: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @disk_name.setter
    def disk_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @disk_path.setter
    def disk_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_name.setter
    def instance_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _Disk_attachmentState:
    def __init__(__self__, *, disk_name: Optional[pulumi.Input[_builtins.str]] = ..., disk_path: Optional[pulumi.Input[_builtins.str]] = ..., instance_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_name.setter
    def disk_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_path.setter
    def disk_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:lightsail/disk_attachment:Disk_attachment")
class Disk_attachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., disk_name: Optional[pulumi.Input[_builtins.str]] = ..., disk_path: Optional[pulumi.Input[_builtins.str]] = ..., instance_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Disk_attachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., disk_name: Optional[pulumi.Input[_builtins.str]] = ..., disk_path: Optional[pulumi.Input[_builtins.str]] = ..., instance_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> Disk_attachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskName")
    def disk_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskPath")
    def disk_path(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


