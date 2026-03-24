import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetInferenceProfilesResult",
    "AwaitableGetInferenceProfilesResult",
    "get_inference_profiles",
    "get_inference_profiles_output",
]

@pulumi.output_type
class GetInferenceProfilesResult:
    def __init__(
        __self__, id=..., inference_profile_summaries=..., region=..., type=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inferenceProfileSummaries")
    def inference_profile_summaries(
        self,
    ) -> Sequence[outputs.GetInferenceProfilesInferenceProfileSummaryResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

class AwaitableGetInferenceProfilesResult(GetInferenceProfilesResult):
    def __await__(self): ...

def get_inference_profiles(
    region: Optional[_builtins.str] = ...,
    type: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetInferenceProfilesResult: ...
def get_inference_profiles_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetInferenceProfilesResult]: ...
