import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionalSecretVersionAccessResult",
    "AwaitableGetRegionalSecretVersionAccessResult",
    "get_regional_secret_version_access",
    "get_regional_secret_version_access_output",
]

@pulumi.output_type
class GetRegionalSecretVersionAccessResult:
    def __init__(
        __self__,
        id=...,
        is_secret_data_base64=...,
        location=...,
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
    def location(self) -> _builtins.str: ...
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

class AwaitableGetRegionalSecretVersionAccessResult(
    GetRegionalSecretVersionAccessResult
):
    def __await__(self): ...

def get_regional_secret_version_access(
    is_secret_data_base64: Optional[_builtins.bool] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    secret: Optional[_builtins.str] = ...,
    version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionalSecretVersionAccessResult: ...
def get_regional_secret_version_access_output(
    is_secret_data_base64: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    secret: Optional[pulumi.Input[_builtins.str]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionalSecretVersionAccessResult]: ...
