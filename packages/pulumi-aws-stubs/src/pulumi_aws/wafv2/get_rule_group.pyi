import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRuleGroupResult",
    "AwaitableGetRuleGroupResult",
    "get_rule_group",
    "get_rule_group_output",
]

@pulumi.output_type
class GetRuleGroupResult:
    def __init__(
        __self__, arn=..., description=..., id=..., name=..., region=..., scope=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...

class AwaitableGetRuleGroupResult(GetRuleGroupResult):
    def __await__(self): ...

def get_rule_group(
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    scope: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRuleGroupResult: ...
def get_rule_group_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    scope: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRuleGroupResult]: ...
