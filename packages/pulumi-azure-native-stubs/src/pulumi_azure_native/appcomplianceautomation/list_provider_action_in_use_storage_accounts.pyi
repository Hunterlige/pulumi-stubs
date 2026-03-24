

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListProviderActionInUseStorageAccountsResult', ..., 'list_provider_action_in_use_storage_accounts', ...]
@pulumi.output_type
class ListProviderActionInUseStorageAccountsResult:
    
    def __init__(__self__, storage_account_list=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountList")
    def storage_account_list(self) -> Optional[Sequence[outputs.StorageInfoResponse]]:
        
        ...
    


class AwaitableListProviderActionInUseStorageAccountsResult(ListProviderActionInUseStorageAccountsResult):
    def __await__(self): # -> Generator[Never, Any, ListProviderActionInUseStorageAccountsResult]:
        ...
    


def list_provider_action_in_use_storage_accounts(subscription_ids: Optional[Sequence[_builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListProviderActionInUseStorageAccountsResult:
    
    ...

def list_provider_action_in_use_storage_accounts_output(subscription_ids: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListProviderActionInUseStorageAccountsResult]:
    
    ...

