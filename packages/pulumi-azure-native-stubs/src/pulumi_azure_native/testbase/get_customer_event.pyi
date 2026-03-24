

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCustomerEventResult', 'AwaitableGetCustomerEventResult', 'get_customer_event', 'get_customer_event_output']
@pulumi.output_type
class GetCustomerEventResult:
    
    def __init__(__self__, azure_api_version=..., event_name=..., id=..., name=..., receivers=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventName")
    def event_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def receivers(self) -> Sequence[outputs.NotificationEventReceiverResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCustomerEventResult(GetCustomerEventResult):
    def __await__(self): # -> Generator[Never, Any, GetCustomerEventResult]:
        ...
    


def get_customer_event(customer_event_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., test_base_account_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCustomerEventResult:
    
    ...

def get_customer_event_output(customer_event_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCustomerEventResult]:
    
    ...

