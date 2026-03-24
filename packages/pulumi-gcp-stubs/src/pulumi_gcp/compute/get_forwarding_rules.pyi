import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetForwardingRulesResult",
    "AwaitableGetForwardingRulesResult",
    "get_forwarding_rules",
    "get_forwarding_rules_output",
]

@pulumi.output_type
class GetForwardingRulesResult:
    def __init__(__self__, id=..., project=..., region=..., rules=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetForwardingRulesRuleResult]: ...

class AwaitableGetForwardingRulesResult(GetForwardingRulesResult):
    def __await__(self): ...

def get_forwarding_rules(
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetForwardingRulesResult: ...
def get_forwarding_rules_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetForwardingRulesResult]: ...
