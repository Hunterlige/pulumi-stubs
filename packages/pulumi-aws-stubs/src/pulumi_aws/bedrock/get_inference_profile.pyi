import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInferenceProfileResult",
    "AwaitableGetInferenceProfileResult",
    "get_inference_profile",
    "get_inference_profile_output",
]

@pulumi.output_type
class GetInferenceProfileResult:
    def __init__(
        __self__,
        created_at=...,
        description=...,
        id=...,
        inference_profile_arn=...,
        inference_profile_id=...,
        inference_profile_name=...,
        models=...,
        region=...,
        status=...,
        type=...,
        updated_at=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceProfileArn")
    def inference_profile_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceProfileId")
    def inference_profile_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceProfileName")
    def inference_profile_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def models(self) -> Sequence[outputs.GetInferenceProfileModelResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str: ...

class AwaitableGetInferenceProfileResult(GetInferenceProfileResult):
    def __await__(self): ...

def get_inference_profile(
    inference_profile_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInferenceProfileResult: ...
def get_inference_profile_output(
    inference_profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInferenceProfileResult]: ...
