

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
__all__ = ['EfsLocationArgs', 'EfsLocation']
@pulumi.input_type
class EfsLocationArgs:
    def __init__(__self__, *, ec2_config: pulumi.Input[EfsLocationEc2ConfigArgs], efs_file_system_arn: pulumi.Input[_builtins.str], access_point_arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., in_transit_encryption: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2Config")
    def ec2_config(self) -> pulumi.Input[EfsLocationEc2ConfigArgs]:
        
        ...
    
    @ec2_config.setter
    def ec2_config(self, value: pulumi.Input[EfsLocationEc2ConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileSystemArn")
    def efs_file_system_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @efs_file_system_arn.setter
    def efs_file_system_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPointArn")
    def access_point_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_point_arn.setter
    def access_point_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemAccessRoleArn")
    def file_system_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_access_role_arn.setter
    def file_system_access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inTransitEncryption")
    def in_transit_encryption(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @in_transit_encryption.setter
    def in_transit_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
class _EfsLocationState:
    def __init__(__self__, *, access_point_arn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., ec2_config: Optional[pulumi.Input[EfsLocationEc2ConfigArgs]] = ..., efs_file_system_arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., in_transit_encryption: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPointArn")
    def access_point_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_point_arn.setter
    def access_point_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2Config")
    def ec2_config(self) -> Optional[pulumi.Input[EfsLocationEc2ConfigArgs]]:
        
        ...
    
    @ec2_config.setter
    def ec2_config(self, value: Optional[pulumi.Input[EfsLocationEc2ConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileSystemArn")
    def efs_file_system_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @efs_file_system_arn.setter
    def efs_file_system_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemAccessRoleArn")
    def file_system_access_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @file_system_access_role_arn.setter
    def file_system_access_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inTransitEncryption")
    def in_transit_encryption(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @in_transit_encryption.setter
    def in_transit_encryption(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:datasync/efsLocation:EfsLocation")
class EfsLocation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_point_arn: Optional[pulumi.Input[_builtins.str]] = ..., ec2_config: Optional[pulumi.Input[Union[EfsLocationEc2ConfigArgs, EfsLocationEc2ConfigArgsDict]]] = ..., efs_file_system_arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., in_transit_encryption: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EfsLocationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_point_arn: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., ec2_config: Optional[pulumi.Input[Union[EfsLocationEc2ConfigArgs, EfsLocationEc2ConfigArgsDict]]] = ..., efs_file_system_arn: Optional[pulumi.Input[_builtins.str]] = ..., file_system_access_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., in_transit_encryption: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., subdirectory: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> EfsLocation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPointArn")
    def access_point_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2Config")
    def ec2_config(self) -> pulumi.Output[outputs.EfsLocationEc2Config]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileSystemArn")
    def efs_file_system_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemAccessRoleArn")
    def file_system_access_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inTransitEncryption")
    def in_transit_encryption(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    


