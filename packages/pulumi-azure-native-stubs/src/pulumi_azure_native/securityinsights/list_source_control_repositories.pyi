

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListSourceControlRepositoriesResult', 'AwaitableListSourceControlRepositoriesResult', 'list_source_control_repositories', 'list_source_control_repositories_output']
@pulumi.output_type
class ListSourceControlRepositoriesResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.RepoResponse]:
        
        ...
    


class AwaitableListSourceControlRepositoriesResult(ListSourceControlRepositoriesResult):
    def __await__(self): # -> Generator[Never, Any, ListSourceControlRepositoriesResult]:
        ...
    


def list_source_control_repositories(client_id: Optional[_builtins.str] = ..., code: Optional[_builtins.str] = ..., installation_id: Optional[_builtins.str] = ..., kind: Optional[Union[_builtins.str, RepositoryAccessKind]] = ..., resource_group_name: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ..., token: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListSourceControlRepositoriesResult:
    
    ...

def list_source_control_repositories_output(client_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., code: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., installation_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, RepositoryAccessKind]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., token: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListSourceControlRepositoriesResult]:
    
    ...

