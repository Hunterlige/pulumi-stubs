

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetApiIssueCommentResult', 'AwaitableGetApiIssueCommentResult', 'get_api_issue_comment', 'get_api_issue_comment_output']
@pulumi.output_type
class GetApiIssueCommentResult:
    
    def __init__(__self__, azure_api_version=..., created_date=..., id=..., name=..., text=..., type=..., user_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userId")
    def user_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetApiIssueCommentResult(GetApiIssueCommentResult):
    def __await__(self): # -> Generator[Never, Any, GetApiIssueCommentResult]:
        ...
    


def get_api_issue_comment(api_id: Optional[_builtins.str] = ..., comment_id: Optional[_builtins.str] = ..., issue_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., service_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetApiIssueCommentResult:
    
    ...

def get_api_issue_comment_output(api_id: Optional[pulumi.Input[_builtins.str]] = ..., comment_id: Optional[pulumi.Input[_builtins.str]] = ..., issue_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetApiIssueCommentResult]:
    
    ...

