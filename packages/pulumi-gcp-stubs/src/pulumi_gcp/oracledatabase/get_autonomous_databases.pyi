import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAutonomousDatabasesResult",
    "AwaitableGetAutonomousDatabasesResult",
    "get_autonomous_databases",
    "get_autonomous_databases_output",
]

@pulumi.output_type
class GetAutonomousDatabasesResult:
    def __init__(
        __self__, autonomous_databases=..., id=..., location=..., project=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autonomousDatabases")
    def autonomous_databases(
        self,
    ) -> Sequence[outputs.GetAutonomousDatabasesAutonomousDatabaseResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

class AwaitableGetAutonomousDatabasesResult(GetAutonomousDatabasesResult):
    def __await__(self): ...

def get_autonomous_databases(
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAutonomousDatabasesResult: ...
def get_autonomous_databases_output(
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAutonomousDatabasesResult]: ...
