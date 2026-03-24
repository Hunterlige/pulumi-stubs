import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPolicyResult",
    "AwaitableGetPolicyResult",
    "get_policy",
    "get_policy_output",
]

@pulumi.output_type
class GetPolicyResult:
    def __init__(
        __self__,
        customer=...,
        id=...,
        name=...,
        policy_queries=...,
        setting=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def customer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyQueries")
    def policy_queries(self) -> Sequence[outputs.GetPolicyPolicyQueryResult]: ...
    @_builtins.property
    @pulumi.getter
    def setting(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPolicyResult(GetPolicyResult):
    def __await__(self): ...

def get_policy(
    name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetPolicyResult: ...
def get_policy_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPolicyResult]: ...
