import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLocalRulestackChangeLogResult",
    "AwaitableGetLocalRulestackChangeLogResult",
    "get_local_rulestack_change_log",
    "get_local_rulestack_change_log_output",
]

@pulumi.output_type
class GetLocalRulestackChangeLogResult:
    def __init__(
        __self__, changes=..., last_committed=..., last_modified=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def changes(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastCommitted")
    def last_committed(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[_builtins.str]: ...

class AwaitableGetLocalRulestackChangeLogResult(GetLocalRulestackChangeLogResult):
    def __await__(self): ...

def get_local_rulestack_change_log(
    local_rulestack_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetLocalRulestackChangeLogResult: ...
def get_local_rulestack_change_log_output(
    local_rulestack_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLocalRulestackChangeLogResult]: ...
