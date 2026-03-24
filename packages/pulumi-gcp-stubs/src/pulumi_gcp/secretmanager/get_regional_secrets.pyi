import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionalSecretsResult",
    "AwaitableGetRegionalSecretsResult",
    "get_regional_secrets",
    "get_regional_secrets_output",
]

@pulumi.output_type
class GetRegionalSecretsResult:
    def __init__(
        __self__, filter=..., id=..., location=..., project=..., secrets=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Sequence[outputs.GetRegionalSecretsSecretResult]: ...

class AwaitableGetRegionalSecretsResult(GetRegionalSecretsResult):
    def __await__(self): ...

def get_regional_secrets(
    filter: Optional[_builtins.str] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionalSecretsResult: ...
def get_regional_secrets_output(
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    location: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionalSecretsResult]: ...
