

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
__all__ = ['SessionLoggerArgs', 'SessionLogger']
@pulumi.input_type
class SessionLoggerArgs:
    def __init__(__self__, *, event_filter: pulumi.Input[SessionLoggerEventFilterArgs], log_configuration: pulumi.Input[SessionLoggerLogConfigurationArgs], additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventFilter")
    def event_filter(self) -> pulumi.Input[SessionLoggerEventFilterArgs]:
        
        ...
    
    @event_filter.setter
    def event_filter(self, value: pulumi.Input[SessionLoggerEventFilterArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> pulumi.Input[SessionLoggerLogConfigurationArgs]:
        
        ...
    
    @log_configuration.setter
    def log_configuration(self, value: pulumi.Input[SessionLoggerLogConfigurationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_encryption_context.setter
    def additional_encryption_context(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
class _SessionLoggerState:
    def __init__(__self__, *, additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., associated_portal_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., event_filter: Optional[pulumi.Input[SessionLoggerEventFilterArgs]] = ..., log_configuration: Optional[pulumi.Input[SessionLoggerLogConfigurationArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., session_logger_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @additional_encryption_context.setter
    def additional_encryption_context(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedPortalArns")
    def associated_portal_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @associated_portal_arns.setter
    def associated_portal_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="eventFilter")
    def event_filter(self) -> Optional[pulumi.Input[SessionLoggerEventFilterArgs]]:
        
        ...
    
    @event_filter.setter
    def event_filter(self, value: Optional[pulumi.Input[SessionLoggerEventFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> Optional[pulumi.Input[SessionLoggerLogConfigurationArgs]]:
        
        ...
    
    @log_configuration.setter
    def log_configuration(self, value: Optional[pulumi.Input[SessionLoggerLogConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionLoggerArn")
    def session_logger_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_logger_arn.setter
    def session_logger_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.type_token("aws:workspacesweb/sessionLogger:SessionLogger")
class SessionLogger(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., event_filter: Optional[pulumi.Input[Union[SessionLoggerEventFilterArgs, SessionLoggerEventFilterArgsDict]]] = ..., log_configuration: Optional[pulumi.Input[Union[SessionLoggerLogConfigurationArgs, SessionLoggerLogConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SessionLoggerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., associated_portal_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., customer_managed_key: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., event_filter: Optional[pulumi.Input[Union[SessionLoggerEventFilterArgs, SessionLoggerEventFilterArgsDict]]] = ..., log_configuration: Optional[pulumi.Input[Union[SessionLoggerLogConfigurationArgs, SessionLoggerLogConfigurationArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., session_logger_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> SessionLogger:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associatedPortalArns")
    def associated_portal_arns(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventFilter")
    def event_filter(self) -> pulumi.Output[outputs.SessionLoggerEventFilter]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> pulumi.Output[outputs.SessionLoggerLogConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionLoggerArn")
    def session_logger_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


