

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListNotificationHubKeysResult', 'AwaitableListNotificationHubKeysResult', 'list_notification_hub_keys', 'list_notification_hub_keys_output']
@pulumi.output_type
class ListNotificationHubKeysResult:
    
    def __init__(__self__, key_name=..., primary_connection_string=..., primary_key=..., secondary_connection_string=..., secondary_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> _builtins.str:
        
        ...
    


class AwaitableListNotificationHubKeysResult(ListNotificationHubKeysResult):
    def __await__(self): # -> Generator[Never, Any, ListNotificationHubKeysResult]:
        ...
    


def list_notification_hub_keys(authorization_rule_name: Optional[_builtins.str] = ..., namespace_name: Optional[_builtins.str] = ..., notification_hub_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListNotificationHubKeysResult:
    
    ...

def list_notification_hub_keys_output(authorization_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., notification_hub_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListNotificationHubKeysResult]:
    
    ...

