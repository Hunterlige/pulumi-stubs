import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetCustomModelsResult",
    "AwaitableGetCustomModelsResult",
    "get_custom_models",
    "get_custom_models_output",
]

@pulumi.output_type
class GetCustomModelsResult:
    def __init__(__self__, id=..., model_summaries=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="modelSummaries")
    def model_summaries(
        self,
    ) -> Sequence[outputs.GetCustomModelsModelSummaryResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetCustomModelsResult(GetCustomModelsResult):
    def __await__(self): ...

def get_custom_models(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetCustomModelsResult: ...
def get_custom_models_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetCustomModelsResult]: ...
