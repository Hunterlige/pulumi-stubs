import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSchedulingPolicyResult",
    "AwaitableGetSchedulingPolicyResult",
    "get_scheduling_policy",
    "get_scheduling_policy_output",
]

@pulumi.output_type
class GetSchedulingPolicyResult:
    def __init__(
        __self__,
        arn=...,
        fair_share_policies=...,
        id=...,
        name=...,
        region=...,
        tags=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fairSharePolicies")
    def fair_share_policies(
        self,
    ) -> Sequence[outputs.GetSchedulingPolicyFairSharePolicyResult]: ...
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
    def tags(self) -> Mapping[str, _builtins.str]: ...

class AwaitableGetSchedulingPolicyResult(GetSchedulingPolicyResult):
    def __await__(self): ...

def get_scheduling_policy(
    arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSchedulingPolicyResult: ...
def get_scheduling_policy_output(
    arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSchedulingPolicyResult]: ...
