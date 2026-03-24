

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNotebookWorkspaceResult', 'AwaitableGetNotebookWorkspaceResult', 'get_notebook_workspace', 'get_notebook_workspace_output']
@pulumi.output_type
class GetNotebookWorkspaceResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., notebook_server_endpoint=..., status=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
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
    @pulumi.getter(name="notebookServerEndpoint")
    def notebook_server_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNotebookWorkspaceResult(GetNotebookWorkspaceResult):
    def __await__(self): # -> Generator[Never, Any, GetNotebookWorkspaceResult]:
        ...
    


def get_notebook_workspace(account_name: Optional[_builtins.str] = ..., notebook_workspace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNotebookWorkspaceResult:
    
    ...

def get_notebook_workspace_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., notebook_workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNotebookWorkspaceResult]:
    
    ...

