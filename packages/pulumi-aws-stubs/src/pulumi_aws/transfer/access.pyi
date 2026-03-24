

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
__all__ = ['AccessArgs', 'Access']
@pulumi.input_type
class AccessArgs:
    def __init__(__self__, *, external_id: pulumi.Input[_builtins.str], server_id: pulumi.Input[_builtins.str], home_directory: Optional[pulumi.Input[_builtins.str]] = ..., home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[AccessHomeDirectoryMappingArgs]]]] = ..., home_directory_type: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., posix_profile: Optional[pulumi.Input[AccessPosixProfileArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @external_id.setter
    def external_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_id.setter
    def server_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @home_directory.setter
    def home_directory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectoryMappings")
    def home_directory_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessHomeDirectoryMappingArgs]]]]:
        
        ...
    
    @home_directory_mappings.setter
    def home_directory_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessHomeDirectoryMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectoryType")
    def home_directory_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @home_directory_type.setter
    def home_directory_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixProfile")
    def posix_profile(self) -> Optional[pulumi.Input[AccessPosixProfileArgs]]:
        
        ...
    
    @posix_profile.setter
    def posix_profile(self, value: Optional[pulumi.Input[AccessPosixProfileArgs]]): # -> None:
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
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AccessState:
    def __init__(__self__, *, external_id: Optional[pulumi.Input[_builtins.str]] = ..., home_directory: Optional[pulumi.Input[_builtins.str]] = ..., home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[AccessHomeDirectoryMappingArgs]]]] = ..., home_directory_type: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., posix_profile: Optional[pulumi.Input[AccessPosixProfileArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., server_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @home_directory.setter
    def home_directory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectoryMappings")
    def home_directory_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessHomeDirectoryMappingArgs]]]]:
        
        ...
    
    @home_directory_mappings.setter
    def home_directory_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessHomeDirectoryMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectoryType")
    def home_directory_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @home_directory_type.setter
    def home_directory_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixProfile")
    def posix_profile(self) -> Optional[pulumi.Input[AccessPosixProfileArgs]]:
        
        ...
    
    @posix_profile.setter
    def posix_profile(self, value: Optional[pulumi.Input[AccessPosixProfileArgs]]): # -> None:
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
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:transfer/access:Access")
class Access(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., external_id: Optional[pulumi.Input[_builtins.str]] = ..., home_directory: Optional[pulumi.Input[_builtins.str]] = ..., home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AccessHomeDirectoryMappingArgs, AccessHomeDirectoryMappingArgsDict]]]]] = ..., home_directory_type: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., posix_profile: Optional[pulumi.Input[Union[AccessPosixProfileArgs, AccessPosixProfileArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., server_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccessArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., external_id: Optional[pulumi.Input[_builtins.str]] = ..., home_directory: Optional[pulumi.Input[_builtins.str]] = ..., home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AccessHomeDirectoryMappingArgs, AccessHomeDirectoryMappingArgsDict]]]]] = ..., home_directory_type: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., posix_profile: Optional[pulumi.Input[Union[AccessPosixProfileArgs, AccessPosixProfileArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., server_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Access:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectoryMappings")
    def home_directory_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.AccessHomeDirectoryMapping]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectoryType")
    def home_directory_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixProfile")
    def posix_profile(self) -> pulumi.Output[Optional[outputs.AccessPosixProfile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


