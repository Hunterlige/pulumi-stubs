

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSlackWorkspaceResult', 'AwaitableGetSlackWorkspaceResult', 'get_slack_workspace', 'get_slack_workspace_output']
@pulumi.output_type
class GetSlackWorkspaceResult:
    
    def __init__(__self__, id=..., region=..., slack_team_id=..., slack_team_name=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="slackTeamId")
    def slack_team_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slackTeamName")
    def slack_team_name(self) -> _builtins.str:
        ...
    


class AwaitableGetSlackWorkspaceResult(GetSlackWorkspaceResult):
    def __await__(self): # -> Generator[Never, Any, GetSlackWorkspaceResult]:
        ...
    


def get_slack_workspace(region: Optional[_builtins.str] = ..., slack_team_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSlackWorkspaceResult:
    
    ...

def get_slack_workspace_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., slack_team_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSlackWorkspaceResult]:
    
    ...

