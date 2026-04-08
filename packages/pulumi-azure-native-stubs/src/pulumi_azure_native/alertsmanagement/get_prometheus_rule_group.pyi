import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPrometheusRuleGroupResult",
    "AwaitableGetPrometheusRuleGroupResult",
    "get_prometheus_rule_group",
    "get_prometheus_rule_group_output",
]

@pulumi.output_type
class GetPrometheusRuleGroupResult:
    def __init__(
        __self__,
        azure_api_version=...,
        cluster_name=...,
        description=...,
        enabled=...,
        id=...,
        interval=...,
        location=...,
        name=...,
        rules=...,
        scopes=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.PrometheusRuleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPrometheusRuleGroupResult(GetPrometheusRuleGroupResult):
    def __await__(self): ...

def get_prometheus_rule_group(
    resource_group_name: Optional[_builtins.str] = ...,
    rule_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPrometheusRuleGroupResult: ...
def get_prometheus_rule_group_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPrometheusRuleGroupResult]: ...
