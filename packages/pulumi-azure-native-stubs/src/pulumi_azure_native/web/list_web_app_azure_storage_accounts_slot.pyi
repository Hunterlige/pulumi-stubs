

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWebAppAzureStorageAccountsSlotResult', 'AwaitableListWebAppAzureStorageAccountsSlotResult', 'list_web_app_azure_storage_accounts_slot', 'list_web_app_azure_storage_accounts_slot_output']
@pulumi.output_type
class ListWebAppAzureStorageAccountsSlotResult:
    
    def __init__(__self__, id=..., kind=..., name=..., properties=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Mapping[str, outputs.AzureStorageInfoValueResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableListWebAppAzureStorageAccountsSlotResult(ListWebAppAzureStorageAccountsSlotResult):
    def __await__(self): # -> Generator[Never, Any, ListWebAppAzureStorageAccountsSlotResult]:
        ...
    


def list_web_app_azure_storage_accounts_slot(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., slot: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWebAppAzureStorageAccountsSlotResult:
    
    ...

def list_web_app_azure_storage_accounts_slot_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., slot: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWebAppAzureStorageAccountsSlotResult]:
    
    ...

