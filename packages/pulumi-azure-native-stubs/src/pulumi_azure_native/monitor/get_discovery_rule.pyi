import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDiscoveryRuleResult",
    "AwaitableGetDiscoveryRuleResult",
    "get_discovery_rule",
    "get_discovery_rule_output",
]

@pulumi.output_type
class GetDiscoveryRuleResult:
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
    def properties(self) -> Any: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetDiscoveryRuleResult(GetDiscoveryRuleResult):
    def __await__(self): ...

def get_discovery_rule(
    azure_monitor_workspace_name: Optional[_builtins.str] = ...,
    discovery_rule_name: Optional[_builtins.str] = ...,
    health_model_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDiscoveryRuleResult: ...
def get_discovery_rule_output(
    azure_monitor_workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    discovery_rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    health_model_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDiscoveryRuleResult]: ...
