import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFirewallSupportInfoResult",
    "AwaitableGetFirewallSupportInfoResult",
    "get_firewall_support_info",
    "get_firewall_support_info_output",
]

@pulumi.output_type
class GetFirewallSupportInfoResult:
    def __init__(
        __self__,
        account_id=...,
        account_registered=...,
        free_trial=...,
        free_trial_credit_left=...,
        free_trial_days_left=...,
        help_url=...,
        product_serial=...,
        product_sku=...,
        register_url=...,
        support_url=...,
        user_domain_supported=...,
        user_registered=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accountRegistered")
    def account_registered(self) -> Optional[_builtins.str]: ...
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
    @pulumi.getter(name="productSerial")
    def product_serial(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productSku")
    def product_sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registerURL")
    def register_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="supportURL")
    def support_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userDomainSupported")
    def user_domain_supported(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userRegistered")
    def user_registered(self) -> Optional[_builtins.str]: ...

class AwaitableGetFirewallSupportInfoResult(GetFirewallSupportInfoResult):
    def __await__(self): ...

def get_firewall_support_info(
    email: Optional[_builtins.str] = ...,
    firewall_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFirewallSupportInfoResult: ...
def get_firewall_support_info_output(
    email: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    firewall_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFirewallSupportInfoResult]: ...
