import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecretResult",
    "AwaitableGetSecretResult",
    "get_secret",
    "get_secret_output",
]

@pulumi.output_type
class GetSecretResult:
    def __init__(__self__, id=..., region=..., secrets=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Sequence[outputs.GetSecretSecretResult]: ...

class AwaitableGetSecretResult(GetSecretResult):
    def __await__(self): ...

def get_secret(
    region: Optional[_builtins.str] = ...,
    secrets: Optional[
        Sequence[Union[GetSecretSecretArgs, GetSecretSecretArgsDict]]
    ] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecretResult: ...
def get_secret_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    secrets: Optional[
        pulumi.Input[Sequence[Union[GetSecretSecretArgs, GetSecretSecretArgsDict]]]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecretResult]: ...
