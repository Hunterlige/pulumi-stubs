import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCostCategoryResult",
    "AwaitableGetCostCategoryResult",
    "get_cost_category",
    "get_cost_category_output",
]

@pulumi.output_type
class GetCostCategoryResult:
    def __init__(
        __self__,
        cost_category_arn=...,
        default_value=...,
        effective_end=...,
        effective_start=...,
        id=...,
        name=...,
        rule_version=...,
        rules=...,
        split_charge_rules=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="costCategoryArn")
    def cost_category_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveEnd")
    def effective_end(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveStart")
    def effective_start(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ruleVersion")
    def rule_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetCostCategoryRuleResult]: ...
    @_builtins.property
    @pulumi.getter(name="splitChargeRules")
    def split_charge_rules(
        self,
    ) -> Sequence[outputs.GetCostCategorySplitChargeRuleResult]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetCostCategoryResult(GetCostCategoryResult):
    def __await__(self): ...

def get_cost_category(
    cost_category_arn: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCostCategoryResult: ...
def get_cost_category_output(
    cost_category_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCostCategoryResult]: ...
