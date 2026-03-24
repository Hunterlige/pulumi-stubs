import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTablesResult",
    "AwaitableGetTablesResult",
    "get_tables",
    "get_tables_output",
]

@pulumi.output_type
class GetTablesResult:
    def __init__(__self__, dataset_id=..., id=..., project=..., tables=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tables(self) -> Sequence[outputs.GetTablesTableResult]: ...

class AwaitableGetTablesResult(GetTablesResult):
    def __await__(self): ...

def get_tables(
    dataset_id: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTablesResult: ...
def get_tables_output(
    dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTablesResult]: ...
