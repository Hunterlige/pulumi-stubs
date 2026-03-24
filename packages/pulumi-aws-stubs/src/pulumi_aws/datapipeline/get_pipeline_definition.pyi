import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetPipelineDefinitionResult",
    "AwaitableGetPipelineDefinitionResult",
    "get_pipeline_definition",
    "get_pipeline_definition_output",
]

@pulumi.output_type
class GetPipelineDefinitionResult:
    def __init__(
        __self__,
        id=...,
        parameter_objects=...,
        parameter_values=...,
        pipeline_id=...,
        pipeline_objects=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterObjects")
    def parameter_objects(
        self,
    ) -> Sequence[outputs.GetPipelineDefinitionParameterObjectResult]: ...
    @_builtins.property
    @pulumi.getter(name="parameterValues")
    def parameter_values(
        self,
    ) -> Optional[Sequence[outputs.GetPipelineDefinitionParameterValueResult]]: ...
    @_builtins.property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pipelineObjects")
    def pipeline_objects(
        self,
    ) -> Sequence[outputs.GetPipelineDefinitionPipelineObjectResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetPipelineDefinitionResult(GetPipelineDefinitionResult):
    def __await__(self): ...

def get_pipeline_definition(
    parameter_values: Optional[
        Sequence[
            Union[
                GetPipelineDefinitionParameterValueArgs,
                GetPipelineDefinitionParameterValueArgsDict,
            ]
        ]
    ] = ...,
    pipeline_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetPipelineDefinitionResult: ...
def get_pipeline_definition_output(
    parameter_values: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetPipelineDefinitionParameterValueArgs,
                        GetPipelineDefinitionParameterValueArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    pipeline_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetPipelineDefinitionResult]: ...
