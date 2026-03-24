import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecretsResult",
    "AwaitableGetSecretsResult",
    "get_secrets",
    "get_secrets_output",
]

@pulumi.output_type
class GetSecretsResult:
    def __init__(__self__, id=..., plaintext=..., region=..., secrets=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def plaintext(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Sequence[outputs.GetSecretsSecretResult]: ...

class AwaitableGetSecretsResult(GetSecretsResult):
    def __await__(self): ...

def get_secrets(
    region: Optional[_builtins.str] = ...,
    secrets: Optional[
        Sequence[Union[GetSecretsSecretArgs, GetSecretsSecretArgsDict]]
    ] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecretsResult: ...
def get_secrets_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    secrets: Optional[
        pulumi.Input[Sequence[Union[GetSecretsSecretArgs, GetSecretsSecretArgsDict]]]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecretsResult]: ...
