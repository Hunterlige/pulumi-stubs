import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class ListPaloAltoNetworksCloudngfwOperationSupportInfoResult:
    def __init__(
        __self__,
        account_id=...,
        account_registration_status=...,
        credits=...,
        end_date_for_credits=...,
        free_trial=...,
        free_trial_credit_left=...,
        free_trial_days_left=...,
        help_url=...,
        hub_url=...,
        monthly_credit_left=...,
        product_serial=...,
        product_sku=...,
        register_url=...,
        start_date_for_credits=...,
        support_url=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accountRegistrationStatus")
    def account_registration_status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def credits(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="endDateForCredits")
    def end_date_for_credits(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="freeTrial")
    def free_trial(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="freeTrialCreditLeft")
    def free_trial_credit_left(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="freeTrialDaysLeft")
    def free_trial_days_left(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="helpURL")
    def help_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hubUrl")
    def hub_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="monthlyCreditLeft")
    def monthly_credit_left(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="productSerial")
    def product_serial(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productSku")
    def product_sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registerURL")
    def register_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startDateForCredits")
    def start_date_for_credits(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportURL")
    def support_url(self) -> Optional[_builtins.str]: ...

class AwaitableListPaloAltoNetworksCloudngfwOperationSupportInfoResult(
    ListPaloAltoNetworksCloudngfwOperationSupportInfoResult
):
    def __await__(self): ...

def list_palo_alto_networks_cloudngfw_operation_support_info(
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListPaloAltoNetworksCloudngfwOperationSupportInfoResult: ...
def list_palo_alto_networks_cloudngfw_operation_support_info_output(
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListPaloAltoNetworksCloudngfwOperationSupportInfoResult]: ...
