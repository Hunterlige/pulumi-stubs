

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LocationFsxWindowsArgs', 'LocationFsxWindows']
@pulumi.input_type
class LocationFsxWindowsArgs:
    def __init__(__self__, *, fsx_filesystem_arn: pulumi.Input[_builtins.str], password: pulumi.Input[_builtins.str], security_group_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], user: pulumi.Input[_builtins.str], domain: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @fsx_filesystem_arn.setter
    def fsx_filesystem_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_arns.setter
    def security_group_arns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user.setter
    def user(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _LocationFsxWindowsState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., fsx_filesystem_arn: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fsx_filesystem_arn.setter
    def fsx_filesystem_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_arns.setter
    def security_group_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user.setter
    def user(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:datasync/locationFsxWindows:LocationFsxWindows")
class LocationFsxWindows(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., fsx_filesystem_arn: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LocationFsxWindowsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., creation_time: Optional[pulumi.Input[_builtins.str]] = ..., domain: Optional[pulumi.Input[_builtins.str]] = ..., fsx_filesystem_arn: Optional[pulumi.Input[_builtins.str]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ..., user: Optional[pulumi.Input[_builtins.str]] = ...) -> LocationFsxWindows:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fsxFilesystemArn")
    def fsx_filesystem_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def uri(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


