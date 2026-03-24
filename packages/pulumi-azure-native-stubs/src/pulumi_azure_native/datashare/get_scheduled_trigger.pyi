

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetScheduledTriggerResult', 'AwaitableGetScheduledTriggerResult', 'get_scheduled_trigger', 'get_scheduled_trigger_output']
@pulumi.output_type
class GetScheduledTriggerResult:
    
    def __init__(__self__, azure_api_version=..., created_at=..., id=..., kind=..., name=..., provisioning_state=..., recurrence_interval=..., synchronization_mode=..., synchronization_time=..., system_data=..., trigger_status=..., type=..., user_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurrenceInterval")
    def recurrence_interval(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationMode")
    def synchronization_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synchronizationTime")
    def synchronization_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerStatus")
    def trigger_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> _builtins.str:
        
        ...
    


class AwaitableGetScheduledTriggerResult(GetScheduledTriggerResult):
    def __await__(self): # -> Generator[Never, Any, GetScheduledTriggerResult]:
        ...
    


def get_scheduled_trigger(account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., share_subscription_name: Optional[_builtins.str] = ..., trigger_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetScheduledTriggerResult:
    
    ...

def get_scheduled_trigger_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., share_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., trigger_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetScheduledTriggerResult]:
    
    ...

