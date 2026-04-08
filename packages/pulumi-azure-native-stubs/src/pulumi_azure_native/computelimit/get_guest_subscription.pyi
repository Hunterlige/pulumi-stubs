import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetGuestSubscriptionResult",
    "AwaitableGetGuestSubscriptionResult",
    "get_guest_subscription",
    "get_guest_subscription_output",
]

@pulumi.output_type
class GetGuestSubscriptionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetGuestSubscriptionResult(GetGuestSubscriptionResult):
    def __await__(self): ...

def get_guest_subscription(
    guest_subscription_id: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetGuestSubscriptionResult: ...
def get_guest_subscription_output(
    guest_subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetGuestSubscriptionResult]: ...
