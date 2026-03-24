import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetLocationsResult",
    "AwaitableGetLocationsResult",
    "get_locations",
    "get_locations_output",
]

@pulumi.output_type
class GetLocationsResult:
    def __init__(__self__, id=..., locations=..., project=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[outputs.GetLocationsLocationResult]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

class AwaitableGetLocationsResult(GetLocationsResult):
    def __await__(self): ...

def get_locations(
    project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetLocationsResult: ...
def get_locations_output(
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetLocationsResult]: ...
