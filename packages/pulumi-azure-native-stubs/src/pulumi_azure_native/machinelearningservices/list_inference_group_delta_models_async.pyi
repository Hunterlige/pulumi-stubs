import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListInferenceGroupDeltaModelsAsyncResult",
    "AwaitableListInferenceGroupDeltaModelsAsyncResult",
    "list_inference_group_delta_models_async",
    "list_inference_group_delta_models_async_output",
]

@pulumi.output_type
class ListInferenceGroupDeltaModelsAsyncResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[_builtins.str]]: ...

class AwaitableListInferenceGroupDeltaModelsAsyncResult(
    ListInferenceGroupDeltaModelsAsyncResult
):
    def __await__(self): ...

def list_inference_group_delta_models_async(
    count: Optional[_builtins.int] = ...,
    group_name: Optional[_builtins.str] = ...,
    pool_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    skip_token: Optional[_builtins.str] = ...,
    target_base_model: Optional[_builtins.str] = ...,
    workspace_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListInferenceGroupDeltaModelsAsyncResult: ...
def list_inference_group_delta_models_async_output(
    count: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    skip_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    target_base_model: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    workspace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListInferenceGroupDeltaModelsAsyncResult]: ...
