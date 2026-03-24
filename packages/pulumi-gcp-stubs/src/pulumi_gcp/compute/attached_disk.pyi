

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AttachedDiskArgs', 'AttachedDisk']
@pulumi.input_type
class AttachedDiskArgs:
    def __init__(__self__, *, disk: pulumi.Input[_builtins.str], instance: pulumi.Input[_builtins.str], device_name: Optional[pulumi.Input[_builtins.str]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disk(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @disk.setter
    def disk(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interface(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface.setter
    def interface(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AttachedDiskState:
    def __init__(__self__, *, device_name: Optional[pulumi.Input[_builtins.str]] = ..., disk: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk.setter
    def disk(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interface(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface.setter
    def interface(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/attachedDisk:AttachedDisk")
class AttachedDisk(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., disk: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AttachedDiskArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., device_name: Optional[pulumi.Input[_builtins.str]] = ..., disk: Optional[pulumi.Input[_builtins.str]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., mode: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> AttachedDisk:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disk(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interface(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


