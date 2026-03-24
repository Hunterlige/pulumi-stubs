

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCustomerSubscriptionResult', 'AwaitableGetCustomerSubscriptionResult', 'get_customer_subscription', 'get_customer_subscription_output']
@pulumi.output_type
class GetCustomerSubscriptionResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., name=..., tenant_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCustomerSubscriptionResult(GetCustomerSubscriptionResult):
    def __await__(self): # -> Generator[Never, Any, GetCustomerSubscriptionResult]:
        ...
    


def get_customer_subscription(customer_subscription_name: Optional[_builtins.str] = ..., registration_name: Optional[_builtins.str] = ..., resource_group: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCustomerSubscriptionResult:
    
    ...

def get_customer_subscription_output(customer_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., registration_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCustomerSubscriptionResult]:
    
    ...

