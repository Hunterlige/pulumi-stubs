import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPoliciesForTargetResult",
    "AwaitableGetPoliciesForTargetResult",
    "get_policies_for_target",
    "get_policies_for_target_output",
]

@pulumi.output_type
class GetPoliciesForTargetResult:
    def __init__(__self__, filter=..., id=..., ids=..., target_id=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> _builtins.str: ...

class AwaitableGetPoliciesForTargetResult(GetPoliciesForTargetResult):
    def __await__(self): ...

def get_policies_for_target(
    filter: Optional[_builtins.str] = ...,
    target_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPoliciesForTargetResult: ...
def get_policies_for_target_output(
    filter: Optional[pulumi.Input[_builtins.str]] = ...,
    target_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPoliciesForTargetResult]: ...
