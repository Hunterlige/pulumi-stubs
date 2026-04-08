import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCostAllocationRuleResult",
    "AwaitableGetCostAllocationRuleResult",
    "get_cost_allocation_rule",
    "get_cost_allocation_rule_output",
]

@pulumi.output_type
class GetCostAllocationRuleResult:
    def __init__(
        __self__, azure_api_version=..., id=..., name=..., properties=..., type=...
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
    def properties(self) -> outputs.CostAllocationRulePropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetCostAllocationRuleResult(GetCostAllocationRuleResult):
    def __await__(self): ...

def get_cost_allocation_rule(
    billing_account_id: Optional[_builtins.str] = ...,
    rule_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetCostAllocationRuleResult: ...
def get_cost_allocation_rule_output(
    billing_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
    rule_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCostAllocationRuleResult]: ...
