

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBillingAccountResult', 'AwaitableGetBillingAccountResult', 'get_billing_account', 'get_billing_account_output']
@pulumi.output_type
class GetBillingAccountResult:
    
    def __init__(__self__, billing_account=..., currency_code=..., display_name=..., id=..., lookup_projects=..., name=..., open=..., project_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookupProjects")
    def lookup_projects(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def open(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectIds")
    def project_ids(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetBillingAccountResult(GetBillingAccountResult):
    def __await__(self): # -> Generator[Never, Any, GetBillingAccountResult]:
        ...
    


def get_billing_account(billing_account: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., lookup_projects: Optional[_builtins.bool] = ..., open: Optional[_builtins.bool] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBillingAccountResult:
    
    ...

def get_billing_account_output(billing_account: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., display_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., lookup_projects: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., open: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBillingAccountResult]:
    
    ...

