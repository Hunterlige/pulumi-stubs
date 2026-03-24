import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetModelResult", "AwaitableGetModelResult", "get_model", "get_model_output"]

@pulumi.output_type
class GetModelResult:
    def __init__(
        __self__,
        customizations_supporteds=...,
        id=...,
        inference_types_supporteds=...,
        input_modalities=...,
        model_arn=...,
        model_id=...,
        model_name=...,
        output_modalities=...,
        provider_name=...,
        region=...,
        response_streaming_supported=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customizationsSupporteds")
    def customizations_supporteds(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceTypesSupporteds")
    def inference_types_supporteds(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputModalities")
    def input_modalities(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelId")
    def model_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelName")
    def model_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outputModalities")
    def output_modalities(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="responseStreamingSupported")
    def response_streaming_supported(self) -> _builtins.bool: ...

class AwaitableGetModelResult(GetModelResult):
    def __await__(self): ...

def get_model(
    model_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetModelResult: ...
def get_model_output(
    model_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetModelResult]: ...
