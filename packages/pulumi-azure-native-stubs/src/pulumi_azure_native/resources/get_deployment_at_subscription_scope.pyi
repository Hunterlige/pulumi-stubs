import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDeploymentAtSubscriptionScopeResult",
    "AwaitableGetDeploymentAtSubscriptionScopeResult",
    "get_deployment_at_subscription_scope",
    "get_deployment_at_subscription_scope_output",
]

@pulumi.output_type
class GetDeploymentAtSubscriptionScopeResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        properties=...,
        tags=...,
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
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.DeploymentPropertiesExtendedResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDeploymentAtSubscriptionScopeResult(
    GetDeploymentAtSubscriptionScopeResult
):
    def __await__(self): ...

def get_deployment_at_subscription_scope(
    deployment_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDeploymentAtSubscriptionScopeResult: ...
def get_deployment_at_subscription_scope_output(
    deployment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDeploymentAtSubscriptionScopeResult]: ...
