import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInferenceGroupDeltaModelsStatusAsyncResult",
    ...,
    "get_inference_group_delta_models_status_async",
    ...,
]

@pulumi.output_type
class GetInferenceGroupDeltaModelsStatusAsyncResult:
    def __init__(
        __self__,
        actual_instance_count=...,
        delta_models=...,
        expected_instance_count=...,
        revision_id=...,
        target_base_model=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actualInstanceCount")
    def actual_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="deltaModels")
    def delta_models(
        self,
    ) -> Optional[Mapping[str, Sequence[outputs.DeltaModelCurrentStateResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="expectedInstanceCount")
    def expected_instance_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="revisionId")
    def revision_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetBaseModel")
    def target_base_model(self) -> Optional[_builtins.str]: ...

class AwaitableGetInferenceGroupDeltaModelsStatusAsyncResult(
    GetInferenceGroupDeltaModelsStatusAsyncResult
):
    def __await__(self): ...

def get_inference_group_delta_models_status_async(
    delta_models: Optional[Sequence[_builtins.str]] = ...,
    group_name: Optional[_builtins.str] = ...,
    pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    target_base_model: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInferenceGroupDeltaModelsStatusAsyncResult: ...
def get_inference_group_delta_models_status_async_output(
    delta_models: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ...,
    group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    target_base_model: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInferenceGroupDeltaModelsStatusAsyncResult]: ...
