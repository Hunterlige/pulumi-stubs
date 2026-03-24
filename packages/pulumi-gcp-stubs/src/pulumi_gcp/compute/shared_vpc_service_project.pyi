

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SharedVPCServiceProjectArgs', 'SharedVPCServiceProject']
@pulumi.input_type
class SharedVPCServiceProjectArgs:
    def __init__(__self__, *, host_project: pulumi.Input[_builtins.str], service_project: pulumi.Input[_builtins.str], deletion_policy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostProject")
    def host_project(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host_project.setter
    def host_project(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProject")
    def service_project(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_project.setter
    def service_project(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _SharedVPCServiceProjectState:
    def __init__(__self__, *, deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., host_project: Optional[pulumi.Input[_builtins.str]] = ..., service_project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deletion_policy.setter
    def deletion_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostProject")
    def host_project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_project.setter
    def host_project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProject")
    def service_project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_project.setter
    def service_project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class SharedVPCServiceProject(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., host_project: Optional[pulumi.Input[_builtins.str]] = ..., service_project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SharedVPCServiceProjectArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., deletion_policy: Optional[pulumi.Input[_builtins.str]] = ..., host_project: Optional[pulumi.Input[_builtins.str]] = ..., service_project: Optional[pulumi.Input[_builtins.str]] = ...) -> SharedVPCServiceProject:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionPolicy")
    def deletion_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostProject")
    def host_project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceProject")
    def service_project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


