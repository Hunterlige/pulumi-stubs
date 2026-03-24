

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
class ListBillingAccountInvoiceSectionsByCreateSubscriptionPermissionResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.InvoiceSectionWithCreateSubPermissionResponse]:
        
        ...
    


class AwaitableListBillingAccountInvoiceSectionsByCreateSubscriptionPermissionResult(ListBillingAccountInvoiceSectionsByCreateSubscriptionPermissionResult):
    def __await__(self): # -> Generator[Never, Any, ListBillingAccountInvoiceSectionsByCreateSubscriptionPermissionResult]:
        ...
    


def list_billing_account_invoice_sections_by_create_subscription_permission(billing_account_name: Optional[_builtins.str] = ..., filter: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListBillingAccountInvoiceSectionsByCreateSubscriptionPermissionResult:
    
    ...

def list_billing_account_invoice_sections_by_create_subscription_permission_output(billing_account_name: Optional[pulumi.Input[_builtins.str]] = ..., filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListBillingAccountInvoiceSectionsByCreateSubscriptionPermissionResult]:
    
    ...

