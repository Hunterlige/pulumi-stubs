import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

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
        arn=...,
        aws_managed=...,
        content=...,
        description=...,
        id=...,
        name=...,
        policy_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="awsManaged")
    def aws_managed(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str: ...
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
    @pulumi.getter(name="policyId")
    def policy_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetPolicyResult(GetPolicyResult):
    def __await__(self): ...

def get_policy(
    policy_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetPolicyResult: ...
def get_policy_output(
    policy_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPolicyResult]: ...
