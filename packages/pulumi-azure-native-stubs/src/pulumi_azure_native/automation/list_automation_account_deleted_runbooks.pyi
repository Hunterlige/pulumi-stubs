

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListAutomationAccountDeletedRunbooksResult', ..., 'list_automation_account_deleted_runbooks', 'list_automation_account_deleted_runbooks_output']
@pulumi.output_type
class ListAutomationAccountDeletedRunbooksResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.DeletedRunbookResponse]]:
        
        ...
    


class AwaitableListAutomationAccountDeletedRunbooksResult(ListAutomationAccountDeletedRunbooksResult):
    def __await__(self): # -> Generator[Never, Any, ListAutomationAccountDeletedRunbooksResult]:
        ...
    


def list_automation_account_deleted_runbooks(automation_account_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListAutomationAccountDeletedRunbooksResult:
    
    ...

def list_automation_account_deleted_runbooks_output(automation_account_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListAutomationAccountDeletedRunbooksResult]:
    
    ...

