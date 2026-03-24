

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessPointArgs', 'AccessPoint']
@pulumi.input_type
class AccessPointArgs:
    def __init__(__self__, *, file_system_id: pulumi.Input[_builtins.str], posix_user: Optional[pulumi.Input[AccessPointPosixUserArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_directory: Optional[pulumi.Input[AccessPointRootDirectoryArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixUser")
    def posix_user(self) -> Optional[pulumi.Input[AccessPointPosixUserArgs]]:
        
        ...
    
    @posix_user.setter
    def posix_user(self, value: Optional[pulumi.Input[AccessPointPosixUserArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> Optional[pulumi.Input[AccessPointRootDirectoryArgs]]:
        
        ...
    
    @root_directory.setter
    def root_directory(self, value: Optional[pulumi.Input[AccessPointRootDirectoryArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _AccessPointState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., posix_user: Optional[pulumi.Input[AccessPointPosixUserArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_directory: Optional[pulumi.Input[AccessPointRootDirectoryArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemArn")
    def file_system_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_arn.setter
    def file_system_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixUser")
    def posix_user(self) -> Optional[pulumi.Input[AccessPointPosixUserArgs]]:
        
        ...
    
    @posix_user.setter
    def posix_user(self, value: Optional[pulumi.Input[AccessPointPosixUserArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> Optional[pulumi.Input[AccessPointRootDirectoryArgs]]:
        
        ...
    
    @root_directory.setter
    def root_directory(self, value: Optional[pulumi.Input[AccessPointRootDirectoryArgs]]): # -> None:
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
    


@pulumi.type_token("aws:efs/accessPoint:AccessPoint")
class AccessPoint(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., posix_user: Optional[pulumi.Input[Union[AccessPointPosixUserArgs, AccessPointPosixUserArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_directory: Optional[pulumi.Input[Union[AccessPointRootDirectoryArgs, AccessPointRootDirectoryArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccessPointArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_id: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., posix_user: Optional[pulumi.Input[Union[AccessPointPosixUserArgs, AccessPointPosixUserArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., root_directory: Optional[pulumi.Input[Union[AccessPointRootDirectoryArgs, AccessPointRootDirectoryArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> AccessPoint:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemArn")
    def file_system_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixUser")
    def posix_user(self) -> pulumi.Output[Optional[outputs.AccessPointPosixUser]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> pulumi.Output[outputs.AccessPointRootDirectory]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


