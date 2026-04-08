import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListKeyByAutomationAccountResult",
    "AwaitableListKeyByAutomationAccountResult",
    "list_key_by_automation_account",
    "list_key_by_automation_account_output",
]

@pulumi.output_type
class ListKeyByAutomationAccountResult:
    def __init__(__self__, keys=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[outputs.KeyResponse]]: ...

class AwaitableListKeyByAutomationAccountResult(ListKeyByAutomationAccountResult):
    def __await__(self): ...

def list_key_by_automation_account(
    automation_account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListKeyByAutomationAccountResult: ...
def list_key_by_automation_account_output(
    automation_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListKeyByAutomationAccountResult]: ...
