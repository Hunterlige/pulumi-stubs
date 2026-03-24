

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListWorkspaceConnectionSecretsResult', 'AwaitableListWorkspaceConnectionSecretsResult', 'list_workspace_connection_secrets', 'list_workspace_connection_secrets_output']
@pulumi.output_type
class ListWorkspaceConnectionSecretsResult:
    
    def __init__(__self__, id=..., name=..., properties=..., system_data=..., type=...) -> None:
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
    def properties(self) -> Any:
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableListWorkspaceConnectionSecretsResult(ListWorkspaceConnectionSecretsResult):
    def __await__(self): # -> Generator[Never, Any, ListWorkspaceConnectionSecretsResult]:
        ...
    


def list_workspace_connection_secrets(connection_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListWorkspaceConnectionSecretsResult:
    
    ...

def list_workspace_connection_secrets_output(connection_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListWorkspaceConnectionSecretsResult]:
    
    ...

