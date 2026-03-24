import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatasetsResult",
    "AwaitableGetDatasetsResult",
    "get_datasets",
    "get_datasets_output",
]

@pulumi.output_type
class GetDatasetsResult:
    def __init__(__self__, datasets=..., id=..., project=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def datasets(self) -> Sequence[outputs.GetDatasetsDatasetResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

class AwaitableGetDatasetsResult(GetDatasetsResult):
    def __await__(self): ...

def get_datasets(
    project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetDatasetsResult: ...
def get_datasets_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatasetsResult]: ...
