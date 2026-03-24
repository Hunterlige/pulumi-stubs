import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDatabasesResult",
    "AwaitableGetDatabasesResult",
    "get_databases",
    "get_databases_output",
]

@pulumi.output_type
class GetDatabasesResult:
    def __init__(
        __self__, databases=..., id=..., instance=..., project=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def databases(self) -> Sequence[outputs.GetDatabasesDatabaseResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

class AwaitableGetDatabasesResult(GetDatabasesResult):
    def __await__(self): ...

def get_databases(
    instance: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDatabasesResult: ...
def get_databases_output(
    instance: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDatabasesResult]: ...
