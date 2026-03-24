import builtins as _builtins
import sys
import pulumi
from typing import Sequence

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GetModelsModelSummaryResult"]

@pulumi.output_type
class GetModelsModelSummaryResult(dict):
    def __init__(
        __self__,
        *,
        customizations_supporteds: Sequence[_builtins.str],
        inference_types_supporteds: Sequence[_builtins.str],
        input_modalities: Sequence[_builtins.str],
        model_arn: _builtins.str,
        model_id: _builtins.str,
        model_name: _builtins.str,
        output_modalities: Sequence[_builtins.str],
        provider_name: _builtins.str,
        response_streaming_supported: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customizationsSupporteds")
    def customizations_supporteds(self) -> Sequence[_builtins.str]: ...
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
    @pulumi.getter(name="responseStreamingSupported")
    def response_streaming_supported(self) -> _builtins.bool: ...
