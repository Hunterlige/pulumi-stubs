

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetJobResult', 'AwaitableGetJobResult', 'get_job', 'get_job_output']
@pulumi.output_type
class GetJobResult:
    
    def __init__(__self__, annotations=..., binary_authorizations=..., client=..., client_version=..., conditions=..., create_time=..., creator=..., delete_time=..., deletion_protection=..., effective_annotations=..., effective_labels=..., etag=..., execution_count=..., expire_time=..., generation=..., id=..., labels=..., last_modifier=..., latest_created_executions=..., launch_stage=..., location=..., name=..., observed_generation=..., project=..., pulumi_labels=..., reconciling=..., run_execution_token=..., start_execution_token=..., templates=..., terminal_conditions=..., uid=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizations")
    def binary_authorizations(self) -> Sequence[outputs.GetJobBinaryAuthorizationResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def client(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.GetJobConditionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def creator(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionCount")
    def execution_count(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def generation(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifier")
    def last_modifier(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestCreatedExecutions")
    def latest_created_executions(self) -> Sequence[outputs.GetJobLatestCreatedExecutionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runExecutionToken")
    def run_execution_token(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startExecutionToken")
    def start_execution_token(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def templates(self) -> Sequence[outputs.GetJobTemplateResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminalConditions")
    def terminal_conditions(self) -> Sequence[outputs.GetJobTerminalConditionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetJobResult(GetJobResult):
    def __await__(self): # -> Generator[Never, Any, GetJobResult]:
        ...
    


def get_job(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetJobResult:
    
    ...

def get_job_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetJobResult]:
    
    ...

