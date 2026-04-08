import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTagRuleResult",
    "AwaitableGetTagRuleResult",
    "get_tag_rule",
    "get_tag_rule_output",
]

@pulumi.output_type
class GetTagRuleResult:
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
    def properties(self) -> outputs.MonitoringTagRulesPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetTagRuleResult(GetTagRuleResult):
    def __await__(self): ...

def get_tag_rule(
    monitor_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    rule_set_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTagRuleResult: ...
def get_tag_rule_output(
    monitor_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_set_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTagRuleResult]: ...
