

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListIntegrationAccountCallbackUrlResult', 'AwaitableListIntegrationAccountCallbackUrlResult', 'list_integration_account_callback_url', 'list_integration_account_callback_url_output']
@pulumi.output_type
class ListIntegrationAccountCallbackUrlResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListIntegrationAccountCallbackUrlResult(ListIntegrationAccountCallbackUrlResult):
    def __await__(self): # -> Generator[Never, Any, ListIntegrationAccountCallbackUrlResult]:
        ...
    


def list_integration_account_callback_url(integration_account_name: Optional[_builtins.str] = ..., key_type: Optional[Union[_builtins.str, KeyType]] = ..., not_after: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListIntegrationAccountCallbackUrlResult:
    
    ...

def list_integration_account_callback_url_output(integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., key_type: Optional[pulumi.Input[Optional[Union[_builtins.str, KeyType]]]] = ..., not_after: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListIntegrationAccountCallbackUrlResult]:
    
    ...

