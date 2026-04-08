import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkspaceProductResult",
    "AwaitableGetWorkspaceProductResult",
    "get_workspace_product",
    "get_workspace_product_output",
]

@pulumi.output_type
class GetWorkspaceProductResult:
    def __init__(
        __self__,
        approval_required=...,
        azure_api_version=...,
        description=...,
        display_name=...,
        id=...,
        name=...,
        state=...,
        subscription_required=...,
        subscriptions_limit=...,
        terms=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionsLimit")
    def subscriptions_limit(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def terms(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWorkspaceProductResult(GetWorkspaceProductResult):
    def __await__(self): ...

def get_workspace_product(
    product_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    workspace_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkspaceProductResult: ...
def get_workspace_product_output(
    product_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkspaceProductResult]: ...
