import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagementGroupSubscriptionResult",
    "AwaitableGetManagementGroupSubscriptionResult",
    "get_management_group_subscription",
    "get_management_group_subscription_output",
]

@pulumi.output_type
class GetManagementGroupSubscriptionResult:
    def __init__(
        __self__,
        azure_api_version=...,
        display_name=...,
        id=...,
        name=...,
        parent=...,
        state=...,
        system_data=...,
        tenant=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[outputs.DescendantParentGroupInfoResponse]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tenant(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetManagementGroupSubscriptionResult(
    GetManagementGroupSubscriptionResult
):
    def __await__(self): ...

def get_management_group_subscription(
    group_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetManagementGroupSubscriptionResult: ...
def get_management_group_subscription_output(
    group_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagementGroupSubscriptionResult]: ...
