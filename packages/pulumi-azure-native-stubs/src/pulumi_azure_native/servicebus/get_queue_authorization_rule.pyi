import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetQueueAuthorizationRuleResult",
    "AwaitableGetQueueAuthorizationRuleResult",
    "get_queue_authorization_rule",
    "get_queue_authorization_rule_output",
]

@pulumi.output_type
class GetQueueAuthorizationRuleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        location=...,
        name=...,
        rights=...,
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
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rights(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetQueueAuthorizationRuleResult(GetQueueAuthorizationRuleResult):
    def __await__(self): ...

def get_queue_authorization_rule(
    authorization_rule_name: Optional[_builtins.str] = ...,
    namespace_name: Optional[_builtins.str] = ...,
    queue_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetQueueAuthorizationRuleResult: ...
def get_queue_authorization_rule_output(
    authorization_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    queue_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetQueueAuthorizationRuleResult]: ...
