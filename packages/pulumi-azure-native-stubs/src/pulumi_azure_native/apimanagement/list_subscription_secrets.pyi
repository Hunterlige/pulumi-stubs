

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListSubscriptionSecretsResult', 'AwaitableListSubscriptionSecretsResult', 'list_subscription_secrets', 'list_subscription_secrets_output']
@pulumi.output_type
class ListSubscriptionSecretsResult:
    
    def __init__(__self__, primary_key=..., secondary_key=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListSubscriptionSecretsResult(ListSubscriptionSecretsResult):
    def __await__(self): # -> Generator[Never, Any, ListSubscriptionSecretsResult]:
        ...
    


def list_subscription_secrets(resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., sid: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListSubscriptionSecretsResult:
    
    ...

def list_subscription_secrets_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., sid: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListSubscriptionSecretsResult]:
    
    ...

