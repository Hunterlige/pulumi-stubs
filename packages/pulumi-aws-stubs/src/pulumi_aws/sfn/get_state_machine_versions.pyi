

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStateMachineVersionsResult', 'AwaitableGetStateMachineVersionsResult', 'get_state_machine_versions', 'get_state_machine_versions_output']
@pulumi.output_type
class GetStateMachineVersionsResult:
    
    def __init__(__self__, id=..., region=..., statemachine_arn=..., statemachine_versions=...) -> None:
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
    @pulumi.getter(name="statemachineArn")
    def statemachine_arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statemachineVersions")
    def statemachine_versions(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetStateMachineVersionsResult(GetStateMachineVersionsResult):
    def __await__(self): # -> Generator[Never, Any, GetStateMachineVersionsResult]:
        ...
    


def get_state_machine_versions(region: Optional[_builtins.str] = ..., statemachine_arn: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStateMachineVersionsResult:
    
    ...

def get_state_machine_versions_output(region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., statemachine_arn: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStateMachineVersionsResult]:
    
    ...

