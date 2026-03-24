

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWorkerPoolResult', 'AwaitableGetWorkerPoolResult', 'get_worker_pool', 'get_worker_pool_output']
@pulumi.output_type
class GetWorkerPoolResult:
    
    def __init__(__self__, annotations=..., binary_authorizations=..., client=..., client_version=..., conditions=..., create_time=..., creator=..., custom_audiences=..., delete_time=..., deletion_protection=..., description=..., effective_annotations=..., effective_labels=..., etag=..., expire_time=..., generation=..., id=..., instance_split_statuses=..., instance_splits=..., labels=..., last_modifier=..., latest_created_revision=..., latest_ready_revision=..., launch_stage=..., location=..., name=..., observed_generation=..., project=..., pulumi_labels=..., reconciling=..., scalings=..., templates=..., terminal_conditions=..., uid=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizations")
    def binary_authorizations(self) -> Sequence[outputs.GetWorkerPoolBinaryAuthorizationResult]:
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
    def conditions(self) -> Sequence[outputs.GetWorkerPoolConditionResult]:
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
    @pulumi.getter(name="customAudiences")
    def custom_audiences(self) -> Sequence[_builtins.str]:
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
    @pulumi.getter
    def description(self) -> _builtins.str:
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
    @pulumi.getter(name="instanceSplitStatuses")
    def instance_split_statuses(self) -> Sequence[outputs.GetWorkerPoolInstanceSplitStatusResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceSplits")
    def instance_splits(self) -> Sequence[outputs.GetWorkerPoolInstanceSplitResult]:
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
    @pulumi.getter(name="latestCreatedRevision")
    def latest_created_revision(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestReadyRevision")
    def latest_ready_revision(self) -> _builtins.str:
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
    @pulumi.getter
    def scalings(self) -> Sequence[outputs.GetWorkerPoolScalingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def templates(self) -> Sequence[outputs.GetWorkerPoolTemplateResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminalConditions")
    def terminal_conditions(self) -> Sequence[outputs.GetWorkerPoolTerminalConditionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetWorkerPoolResult(GetWorkerPoolResult):
    def __await__(self): # -> Generator[Never, Any, GetWorkerPoolResult]:
        ...
    


def get_worker_pool(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWorkerPoolResult:
    
    ...

def get_worker_pool_output(location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWorkerPoolResult]:
    
    ...

