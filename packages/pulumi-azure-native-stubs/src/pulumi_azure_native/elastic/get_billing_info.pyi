

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetBillingInfoResult', 'AwaitableGetBillingInfoResult', 'get_billing_info', 'get_billing_info_output']
@pulumi.output_type
class GetBillingInfoResult:
    
    def __init__(__self__, marketplace_saas_info=..., partner_billing_entity=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="marketplaceSaasInfo")
    def marketplace_saas_info(self) -> Optional[outputs.MarketplaceSaaSInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerBillingEntity")
    def partner_billing_entity(self) -> Optional[outputs.PartnerBillingEntityResponse]:
        
        ...
    


class AwaitableGetBillingInfoResult(GetBillingInfoResult):
    def __await__(self): # -> Generator[Never, Any, GetBillingInfoResult]:
        ...
    


def get_billing_info(monitor_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetBillingInfoResult:
    
    ...

def get_billing_info_output(monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetBillingInfoResult]:
    
    ...

