import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetOutboundRuleResult",
    "AwaitableGetOutboundRuleResult",
    "get_outbound_rule",
    "get_outbound_rule_output",
]

@pulumi.output_type
class GetOutboundRuleResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        name=...,
        properties=...,
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
    @pulumi.getter
    def properties(self) -> outputs.FqdnOutboundRuleResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetOutboundRuleResult(GetOutboundRuleResult):
    def __await__(self): ...

def get_outbound_rule(
    account_name: Optional[_builtins.str] = ...,
    managed_network_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    rule_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetOutboundRuleResult: ...
def get_outbound_rule_output(
    account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    managed_network_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetOutboundRuleResult]: ...
