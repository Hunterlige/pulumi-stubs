import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRateBasedRuleResult",
    "AwaitableGetRateBasedRuleResult",
    "get_rate_based_rule",
    "get_rate_based_rule_output",
]

@pulumi.output_type
class GetRateBasedRuleResult:
    def __init__(__self__, id=..., name=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

class AwaitableGetRateBasedRuleResult(GetRateBasedRuleResult):
    def __await__(self): ...

def get_rate_based_rule(
    name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetRateBasedRuleResult: ...
def get_rate_based_rule_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRateBasedRuleResult]: ...
