import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetJobDefinitionResult",
    "AwaitableGetJobDefinitionResult",
    "get_job_definition",
    "get_job_definition_output",
]

@pulumi.output_type
class GetJobDefinitionResult:
    def __init__(
        __self__,
        arn=...,
        arn_prefix=...,
        container_orchestration_type=...,
        eks_properties=...,
        id=...,
        name=...,
        node_properties=...,
        region=...,
        retry_strategies=...,
        revision=...,
        scheduling_priority=...,
        status=...,
        tags=...,
        timeouts=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="arnPrefix")
    def arn_prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerOrchestrationType")
    def container_orchestration_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="eksProperties")
    def eks_properties(self) -> Sequence[outputs.GetJobDefinitionEksPropertyResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nodeProperties")
    def node_properties(
        self,
    ) -> Sequence[outputs.GetJobDefinitionNodePropertyResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="retryStrategies")
    def retry_strategies(
        self,
    ) -> Sequence[outputs.GetJobDefinitionRetryStrategyResult]: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="schedulingPriority")
    def scheduling_priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Sequence[outputs.GetJobDefinitionTimeoutResult]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetJobDefinitionResult(GetJobDefinitionResult):
    def __await__(self): ...

def get_job_definition(
    arn: Optional[_builtins.str] = ...,
    name: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    revision: Optional[_builtins.int] = ...,
    status: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetJobDefinitionResult: ...
def get_job_definition_output(
    arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    revision: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    status: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetJobDefinitionResult]: ...
