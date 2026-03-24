

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['S3AccessPointAttachmentArgs', 'S3AccessPointAttachment']
@pulumi.input_type
class S3AccessPointAttachmentArgs:
    def __init__(__self__, *, openzfs_configuration: pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationArgs], type: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_access_point: Optional[pulumi.Input[S3AccessPointAttachmentS3AccessPointArgs]] = ..., timeouts: Optional[pulumi.Input[S3AccessPointAttachmentTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openzfsConfiguration")
    def openzfs_configuration(self) -> pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationArgs]:
        
        ...
    
    @openzfs_configuration.setter
    def openzfs_configuration(self, value: pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3AccessPoint")
    def s3_access_point(self) -> Optional[pulumi.Input[S3AccessPointAttachmentS3AccessPointArgs]]:
        
        ...
    
    @s3_access_point.setter
    def s3_access_point(self, value: Optional[pulumi.Input[S3AccessPointAttachmentS3AccessPointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[S3AccessPointAttachmentTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[S3AccessPointAttachmentTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _S3AccessPointAttachmentState:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., openzfs_configuration: Optional[pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_access_point: Optional[pulumi.Input[S3AccessPointAttachmentS3AccessPointArgs]] = ..., s3_access_point_alias: Optional[pulumi.Input[_builtins.str]] = ..., s3_access_point_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[S3AccessPointAttachmentTimeoutsArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openzfsConfiguration")
    def openzfs_configuration(self) -> Optional[pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationArgs]]:
        
        ...
    
    @openzfs_configuration.setter
    def openzfs_configuration(self, value: Optional[pulumi.Input[S3AccessPointAttachmentOpenzfsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3AccessPoint")
    def s3_access_point(self) -> Optional[pulumi.Input[S3AccessPointAttachmentS3AccessPointArgs]]:
        
        ...
    
    @s3_access_point.setter
    def s3_access_point(self, value: Optional[pulumi.Input[S3AccessPointAttachmentS3AccessPointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3AccessPointAlias")
    def s3_access_point_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_access_point_alias.setter
    def s3_access_point_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3AccessPointArn")
    def s3_access_point_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_access_point_arn.setter
    def s3_access_point_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[S3AccessPointAttachmentTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[S3AccessPointAttachmentTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class S3AccessPointAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., openzfs_configuration: Optional[pulumi.Input[Union[S3AccessPointAttachmentOpenzfsConfigurationArgs, S3AccessPointAttachmentOpenzfsConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_access_point: Optional[pulumi.Input[Union[S3AccessPointAttachmentS3AccessPointArgs, S3AccessPointAttachmentS3AccessPointArgsDict]]] = ..., timeouts: Optional[pulumi.Input[Union[S3AccessPointAttachmentTimeoutsArgs, S3AccessPointAttachmentTimeoutsArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: S3AccessPointAttachmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., openzfs_configuration: Optional[pulumi.Input[Union[S3AccessPointAttachmentOpenzfsConfigurationArgs, S3AccessPointAttachmentOpenzfsConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., s3_access_point: Optional[pulumi.Input[Union[S3AccessPointAttachmentS3AccessPointArgs, S3AccessPointAttachmentS3AccessPointArgsDict]]] = ..., s3_access_point_alias: Optional[pulumi.Input[_builtins.str]] = ..., s3_access_point_arn: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[S3AccessPointAttachmentTimeoutsArgs, S3AccessPointAttachmentTimeoutsArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> S3AccessPointAttachment:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openzfsConfiguration")
    def openzfs_configuration(self) -> pulumi.Output[outputs.S3AccessPointAttachmentOpenzfsConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3AccessPoint")
    def s3_access_point(self) -> pulumi.Output[Optional[outputs.S3AccessPointAttachmentS3AccessPoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3AccessPointAlias")
    def s3_access_point_alias(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3AccessPointArn")
    def s3_access_point_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.S3AccessPointAttachmentTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


