

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AwsCloudProfileArgs', 'AwsCloudProfileArgsDict']
class AwsCloudProfileArgsDict(TypedDict):
    
    account_id: pulumi.Input[_builtins.str]
    excluded_accounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    is_organizational_account: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class AwsCloudProfileArgs:
    def __init__(__self__, *, account_id: pulumi.Input[_builtins.str], excluded_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., is_organizational_account: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_id.setter
    def account_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedAccounts")
    def excluded_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @excluded_accounts.setter
    def excluded_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isOrganizationalAccount")
    def is_organizational_account(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_organizational_account.setter
    def is_organizational_account(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


