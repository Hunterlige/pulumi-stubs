

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SecurityContactArgs', 'SecurityContact']
@pulumi.input_type
class SecurityContactArgs:
    def __init__(__self__, *, emails: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., notifications_by_role: Optional[pulumi.Input[SecurityContactPropertiesNotificationsByRoleArgs]] = ..., notifications_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NotificationsSourceAlertArgs, NotificationsSourceAttackPathArgs]]]]] = ..., phone: Optional[pulumi.Input[_builtins.str]] = ..., security_contact_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def emails(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @emails.setter
    def emails(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationsByRole")
    def notifications_by_role(self) -> Optional[pulumi.Input[SecurityContactPropertiesNotificationsByRoleArgs]]:
        
        ...
    
    @notifications_by_role.setter
    def notifications_by_role(self, value: Optional[pulumi.Input[SecurityContactPropertiesNotificationsByRoleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationsSources")
    def notifications_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[NotificationsSourceAlertArgs, NotificationsSourceAttackPathArgs]]]]]:
        
        ...
    
    @notifications_sources.setter
    def notifications_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NotificationsSourceAlertArgs, NotificationsSourceAttackPathArgs]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @phone.setter
    def phone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityContactName")
    def security_contact_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_contact_name.setter
    def security_contact_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:security:SecurityContact")
class SecurityContact(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., emails: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., notifications_by_role: Optional[pulumi.Input[Union[SecurityContactPropertiesNotificationsByRoleArgs, SecurityContactPropertiesNotificationsByRoleArgsDict]]] = ..., notifications_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Union[NotificationsSourceAlertArgs, NotificationsSourceAlertArgsDict], Union[NotificationsSourceAttackPathArgs, NotificationsSourceAttackPathArgsDict]]]]]] = ..., phone: Optional[pulumi.Input[_builtins.str]] = ..., security_contact_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[SecurityContactArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SecurityContact:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def emails(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationsByRole")
    def notifications_by_role(self) -> pulumi.Output[Optional[outputs.SecurityContactPropertiesResponseNotificationsByRole]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationsSources")
    def notifications_sources(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def phone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


