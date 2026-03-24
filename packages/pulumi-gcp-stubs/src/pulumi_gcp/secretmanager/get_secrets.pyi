import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

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
    def __init__(__self__, filter=..., id=..., project=..., secrets=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Sequence[outputs.GetSecretsSecretResult]: ...

class AwaitableGetSecretsResult(GetSecretsResult):
    def __await__(self): ...

def get_secrets(
    filter: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecretsResult: ...
def get_secrets_output(
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecretsResult]: ...
