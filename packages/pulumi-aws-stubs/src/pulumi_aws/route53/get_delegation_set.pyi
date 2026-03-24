import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDelegationSetResult",
    "AwaitableGetDelegationSetResult",
    "get_delegation_set",
    "get_delegation_set_output",
]

@pulumi.output_type
class GetDelegationSetResult:
    def __init__(
        __self__, arn=..., caller_reference=..., id=..., name_servers=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="callerReference")
    def caller_reference(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Sequence[_builtins.str]: ...

class AwaitableGetDelegationSetResult(GetDelegationSetResult):
    def __await__(self): ...

def get_delegation_set(
    id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetDelegationSetResult: ...
def get_delegation_set_output(
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDelegationSetResult]: ...
