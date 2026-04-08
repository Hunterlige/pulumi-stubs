import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBillingHubServiceFreeHourBalanceResult",
    "AwaitableGetBillingHubServiceFreeHourBalanceResult",
    "get_billing_hub_service_free_hour_balance",
    "get_billing_hub_service_free_hour_balance_output",
]

@pulumi.output_type
class GetBillingHubServiceFreeHourBalanceResult:
    def __init__(
        __self__, increment_entries=..., total_remaining_free_hours=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="incrementEntries")
    def increment_entries(
        self,
    ) -> Optional[Sequence[outputs.BillingHubFreeHourIncrementEntryResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="totalRemainingFreeHours")
    def total_remaining_free_hours(self) -> Optional[_builtins.float]: ...

class AwaitableGetBillingHubServiceFreeHourBalanceResult(
    GetBillingHubServiceFreeHourBalanceResult
):
    def __await__(self): ...

def get_billing_hub_service_free_hour_balance(
    resource_group_name: Optional[_builtins.str] = ...,
    test_base_account_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBillingHubServiceFreeHourBalanceResult: ...
def get_billing_hub_service_free_hour_balance_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    test_base_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBillingHubServiceFreeHourBalanceResult]: ...
