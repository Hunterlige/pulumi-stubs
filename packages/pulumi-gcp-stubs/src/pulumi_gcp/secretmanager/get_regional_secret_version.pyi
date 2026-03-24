import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionalSecretVersionResult",
    "AwaitableGetRegionalSecretVersionResult",
    "get_regional_secret_version",
    "get_regional_secret_version_output",
]

@pulumi.output_type
class GetRegionalSecretVersionResult:
    def __init__(
        __self__,
        create_time=...,
        customer_managed_encryptions=...,
        destroy_time=...,
        enabled=...,
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
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptions")
    def customer_managed_encryptions(
        self,
    ) -> Sequence[outputs.GetRegionalSecretVersionCustomerManagedEncryptionResult]: ...
    @_builtins.property
    @pulumi.getter(name="destroyTime")
    def destroy_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
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

class AwaitableGetRegionalSecretVersionResult(GetRegionalSecretVersionResult):
    def __await__(self): ...

def get_regional_secret_version(
    is_secret_data_base64: Optional[_builtins.bool] = ...,
    location: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    secret: Optional[_builtins.str] = ...,
    version: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionalSecretVersionResult: ...
def get_regional_secret_version_output(
    is_secret_data_base64: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    location: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    secret: Optional[pulumi.Input[_builtins.str]] = ...,
    version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionalSecretVersionResult]: ...
