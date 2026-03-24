import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecretVersionAccessResult",
    "AwaitableGetSecretVersionAccessResult",
    "get_secret_version_access",
    "get_secret_version_access_output",
]

@pulumi.output_type
class GetSecretVersionAccessResult:
    def __init__(
        __self__,
        id=...,
        is_secret_data_base64=...,
        name=...,
        project=...,
        secret=...,
        secret_data=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isSecretDataBase64")
    def is_secret_data_base64(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretData")
    def secret_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetSecretVersionAccessResult(GetSecretVersionAccessResult):
    def __await__(self): ...

def get_secret_version_access(
    is_secret_data_base64: Optional[_builtins.bool] = ...,
    project: Optional[_builtins.str] = ...,
    secret: Optional[_builtins.str] = ...,
    version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecretVersionAccessResult: ...
def get_secret_version_access_output(
    is_secret_data_base64: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    secret: Optional[pulumi.Input[_builtins.str]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecretVersionAccessResult]: ...
