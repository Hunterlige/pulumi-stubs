

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListIssueResourcesResult', 'AwaitableListIssueResourcesResult', 'list_issue_resources', 'list_issue_resources_output']
@pulumi.output_type
class ListIssueResourcesResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.RelatedResourceResponse]:
        
        ...
    


class AwaitableListIssueResourcesResult(ListIssueResourcesResult):
    def __await__(self): # -> Generator[Never, Any, ListIssueResourcesResult]:
        ...
    


def list_issue_resources(filter: Optional[_builtins.str] = ..., issue_name: Optional[_builtins.str] = ..., resource_uri: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListIssueResourcesResult:
    
    ...

def list_issue_resources_output(filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., issue_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_uri: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListIssueResourcesResult]:
    
    ...

