

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
__all__ = ['PortalArgs', 'Portal']
@pulumi.input_type
class PortalArgs:
    def __init__(__self__, *, additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., browser_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., max_concurrent_sessions: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[PortalTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_encryption_context.setter
    def additional_encryption_context(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="browserSettingsArn")
    def browser_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @browser_settings_arn.setter
    def browser_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_managed_key.setter
    def customer_managed_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentSessions")
    def max_concurrent_sessions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_sessions.setter
    def max_concurrent_sessions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[PortalTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[PortalTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _PortalState:
    def __init__(__self__, *, additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., browser_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., browser_type: Optional[pulumi.Input[_builtins.str]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ..., data_protection_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., ip_access_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., max_concurrent_sessions: Optional[pulumi.Input[_builtins.int]] = ..., network_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., portal_status: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., renderer_type: Optional[pulumi.Input[_builtins.str]] = ..., session_logger_arn: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[PortalTimeoutsArgs]] = ..., trust_store_arn: Optional[pulumi.Input[_builtins.str]] = ..., user_access_logging_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., user_settings_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_encryption_context.setter
    def additional_encryption_context(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="browserSettingsArn")
    def browser_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @browser_settings_arn.setter
    def browser_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="browserType")
    def browser_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @browser_type.setter
    def browser_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_managed_key.setter
    def customer_managed_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProtectionSettingsArn")
    def data_protection_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_protection_settings_arn.setter
    def data_protection_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAccessSettingsArn")
    def ip_access_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_access_settings_arn.setter
    def ip_access_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentSessions")
    def max_concurrent_sessions(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_concurrent_sessions.setter
    def max_concurrent_sessions(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSettingsArn")
    def network_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_settings_arn.setter
    def network_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @portal_arn.setter
    def portal_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalEndpoint")
    def portal_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @portal_endpoint.setter
    def portal_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalStatus")
    def portal_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @portal_status.setter
    def portal_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rendererType")
    def renderer_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @renderer_type.setter
    def renderer_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionLoggerArn")
    def session_logger_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_logger_arn.setter
    def session_logger_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_reason.setter
    def status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[PortalTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[PortalTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @trust_store_arn.setter
    def trust_store_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAccessLoggingSettingsArn")
    def user_access_logging_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_access_logging_settings_arn.setter
    def user_access_logging_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSettingsArn")
    def user_settings_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_settings_arn.setter
    def user_settings_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:workspacesweb/portal:Portal")
class Portal(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., browser_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., max_concurrent_sessions: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[PortalTimeoutsArgs, PortalTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[PortalArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., authentication_type: Optional[pulumi.Input[_builtins.str]] = ..., browser_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., browser_type: Optional[pulumi.Input[_builtins.str]] = ..., creation_date: Optional[pulumi.Input[_builtins.str]] = ..., customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ..., data_protection_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., ip_access_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., max_concurrent_sessions: Optional[pulumi.Input[_builtins.int]] = ..., network_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_arn: Optional[pulumi.Input[_builtins.str]] = ..., portal_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., portal_status: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., renderer_type: Optional[pulumi.Input[_builtins.str]] = ..., session_logger_arn: Optional[pulumi.Input[_builtins.str]] = ..., status_reason: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[PortalTimeoutsArgs, PortalTimeoutsArgsDict]]] = ..., trust_store_arn: Optional[pulumi.Input[_builtins.str]] = ..., user_access_logging_settings_arn: Optional[pulumi.Input[_builtins.str]] = ..., user_settings_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> Portal:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="browserSettingsArn")
    def browser_settings_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="browserType")
    def browser_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProtectionSettingsArn")
    def data_protection_settings_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAccessSettingsArn")
    def ip_access_settings_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConcurrentSessions")
    def max_concurrent_sessions(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSettingsArn")
    def network_settings_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalArn")
    def portal_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalEndpoint")
    def portal_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portalStatus")
    def portal_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rendererType")
    def renderer_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionLoggerArn")
    def session_logger_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> pulumi.Output[_builtins.str]:
        
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
    def timeouts(self) -> pulumi.Output[Optional[outputs.PortalTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustStoreArn")
    def trust_store_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAccessLoggingSettingsArn")
    def user_access_logging_settings_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSettingsArn")
    def user_settings_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


