import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetKeyRingsResult",
    "AwaitableGetKeyRingsResult",
    "get_key_rings",
    "get_key_rings_output",
]

@pulumi.output_type
class GetKeyRingsResult:
    def __init__(
        __self__, filter=..., id=..., key_rings=..., location=..., project=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyRings")
    def key_rings(self) -> Sequence[outputs.GetKeyRingsKeyRingResult]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...

class AwaitableGetKeyRingsResult(GetKeyRingsResult):
    def __await__(self): ...

def get_key_rings(
    filter: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetKeyRingsResult: ...
def get_key_rings_output(
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetKeyRingsResult]: ...
