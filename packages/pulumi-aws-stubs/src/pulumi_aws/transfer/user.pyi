

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['UserArgs', 'User']
@pulumi.input_type
class UserArgs:
    def __init__(__self__, *, role: pulumi.Input[_builtins.str], server_id: pulumi.Input[_builtins.str], user_name: pulumi.Input[_builtins.str], home_directory: Optional[pulumi.Input[_builtins.str]] = ..., home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[UserHomeDirectoryMappingArgs]]]] = ..., home_directory_type: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., posix_profile: Optional[pulumi.Input[UserPosixProfileArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_id.setter
    def server_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def home_directory_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserHomeDirectoryMappingArgs]]]]:
        
        ...
    
    @home_directory_mappings.setter
    def home_directory_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserHomeDirectoryMappingArgs]]]]): # -> None:
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
    def posix_profile(self) -> Optional[pulumi.Input[UserPosixProfileArgs]]:
        
        ...
    
    @posix_profile.setter
    def posix_profile(self, value: Optional[pulumi.Input[UserPosixProfileArgs]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _UserState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., home_directory: Optional[pulumi.Input[_builtins.str]] = ..., home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[UserHomeDirectoryMappingArgs]]]] = ..., home_directory_type: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., posix_profile: Optional[pulumi.Input[UserPosixProfileArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., server_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def home_directory_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserHomeDirectoryMappingArgs]]]]:
        
        ...
    
    @home_directory_mappings.setter
    def home_directory_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserHomeDirectoryMappingArgs]]]]): # -> None:
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
    def posix_profile(self) -> Optional[pulumi.Input[UserPosixProfileArgs]]:
        
        ...
    
    @posix_profile.setter
    def posix_profile(self, value: Optional[pulumi.Input[UserPosixProfileArgs]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:transfer/user:User")
class User(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., home_directory: Optional[pulumi.Input[_builtins.str]] = ..., home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UserHomeDirectoryMappingArgs, UserHomeDirectoryMappingArgsDict]]]]] = ..., home_directory_type: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., posix_profile: Optional[pulumi.Input[Union[UserPosixProfileArgs, UserPosixProfileArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., server_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: UserArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., home_directory: Optional[pulumi.Input[_builtins.str]] = ..., home_directory_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[UserHomeDirectoryMappingArgs, UserHomeDirectoryMappingArgsDict]]]]] = ..., home_directory_type: Optional[pulumi.Input[_builtins.str]] = ..., policy: Optional[pulumi.Input[_builtins.str]] = ..., posix_profile: Optional[pulumi.Input[Union[UserPosixProfileArgs, UserPosixProfileArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., server_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> User:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="homeDirectoryMappings")
    def home_directory_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.UserHomeDirectoryMapping]]]:
        
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
    def posix_profile(self) -> pulumi.Output[Optional[outputs.UserPosixProfile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


