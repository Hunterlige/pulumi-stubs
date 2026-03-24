

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagedNotificationAccountContactAssociationArgs', 'ManagedNotificationAccountContactAssociation']
@pulumi.input_type
class ManagedNotificationAccountContactAssociationArgs:
    def __init__(__self__, *, contact_identifier: pulumi.Input[_builtins.str], managed_notification_configuration_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactIdentifier")
    def contact_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @contact_identifier.setter
    def contact_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedNotificationConfigurationArn")
    def managed_notification_configuration_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @managed_notification_configuration_arn.setter
    def managed_notification_configuration_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


@pulumi.input_type
class _ManagedNotificationAccountContactAssociationState:
    def __init__(__self__, *, contact_identifier: Optional[pulumi.Input[_builtins.str]] = ..., managed_notification_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactIdentifier")
    def contact_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_identifier.setter
    def contact_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedNotificationConfigurationArn")
    def managed_notification_configuration_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @managed_notification_configuration_arn.setter
    def managed_notification_configuration_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ManagedNotificationAccountContactAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., contact_identifier: Optional[pulumi.Input[_builtins.str]] = ..., managed_notification_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagedNotificationAccountContactAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., contact_identifier: Optional[pulumi.Input[_builtins.str]] = ..., managed_notification_configuration_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> ManagedNotificationAccountContactAssociation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactIdentifier")
    def contact_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedNotificationConfigurationArn")
    def managed_notification_configuration_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


