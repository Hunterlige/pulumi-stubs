

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ChannelAssociationArgs', 'ChannelAssociation']
@pulumi.input_type
class ChannelAssociationArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str], notification_configuration_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfigurationArn")
    def notification_configuration_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @notification_configuration_arn.setter
    def notification_configuration_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _ChannelAssociationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., notification_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfigurationArn")
    def notification_configuration_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_configuration_arn.setter
    def notification_configuration_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ChannelAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., notification_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ChannelAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., notification_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> ChannelAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfigurationArn")
    def notification_configuration_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


