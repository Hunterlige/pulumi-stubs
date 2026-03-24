

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetScriptExecutionLogsResult', 'AwaitableGetScriptExecutionLogsResult', 'get_script_execution_logs', 'get_script_execution_logs_output']
@pulumi.output_type
class GetScriptExecutionLogsResult:
    
    def __init__(__self__, errors=..., failure_reason=..., finished_at=..., hidden_parameters=..., id=..., information=..., name=..., named_outputs=..., output=..., parameters=..., provisioning_state=..., retention=..., script_cmdlet_id=..., started_at=..., submitted_at=..., system_data=..., timeout=..., type=..., warnings=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def errors(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="finishedAt")
    def finished_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hiddenParameters")
    def hidden_parameters(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def information(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namedOutputs")
    def named_outputs(self) -> Optional[Mapping[str, Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def retention(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scriptCmdletId")
    def script_cmdlet_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedAt")
    def started_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="submittedAt")
    def submitted_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def warnings(self) -> Sequence[_builtins.str]:
        
        ...
    


class AwaitableGetScriptExecutionLogsResult(GetScriptExecutionLogsResult):
    def __await__(self): # -> Generator[Never, Any, GetScriptExecutionLogsResult]:
        ...
    


def get_script_execution_logs(private_cloud_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., script_execution_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetScriptExecutionLogsResult:
    
    ...

def get_script_execution_logs_output(private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., script_execution_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetScriptExecutionLogsResult]:
    
    ...

