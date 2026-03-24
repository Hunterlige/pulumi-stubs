

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class ListShareSubscriptionSourceShareSynchronizationSettingsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.ScheduledSourceSynchronizationSettingResponse]:
        
        ...
    


class AwaitableListShareSubscriptionSourceShareSynchronizationSettingsResult(ListShareSubscriptionSourceShareSynchronizationSettingsResult):
    def __await__(self): # -> Generator[Never, Any, ListShareSubscriptionSourceShareSynchronizationSettingsResult]:
        ...
    


def list_share_subscription_source_share_synchronization_settings(account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., share_subscription_name: Optional[_builtins.str] = ..., skip_token: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListShareSubscriptionSourceShareSynchronizationSettingsResult:
    
    ...

def list_share_subscription_source_share_synchronization_settings_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., share_subscription_name: Optional[pulumi.Input[_builtins.str]] = ..., skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListShareSubscriptionSourceShareSynchronizationSettingsResult]:
    
    ...

