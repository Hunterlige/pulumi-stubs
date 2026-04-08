import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListIssueAlertsResult",
    "AwaitableListIssueAlertsResult",
    "list_issue_alerts",
    "list_issue_alerts_output",
]

@pulumi.output_type
class ListIssueAlertsResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.RelatedAlertResponse]: ...

class AwaitableListIssueAlertsResult(ListIssueAlertsResult):
    def __await__(self): ...

def list_issue_alerts(
    azure_monitor_workspace_name: Optional[_builtins.str] = ...,
    filter: Optional[_builtins.str] = ...,
    issue_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListIssueAlertsResult: ...
def list_issue_alerts_output(
    azure_monitor_workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    issue_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListIssueAlertsResult]: ...
