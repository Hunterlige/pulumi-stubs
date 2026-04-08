import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIntegrationRuntimeConnectionInfoResult",
    "AwaitableGetIntegrationRuntimeConnectionInfoResult",
    "get_integration_runtime_connection_info",
    "get_integration_runtime_connection_info_output",
]

@pulumi.output_type
class GetIntegrationRuntimeConnectionInfoResult:
    def __init__(
        __self__,
        host_service_uri=...,
        identity_cert_thumbprint=...,
        is_identity_cert_exprired=...,
        public_key=...,
        service_token=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostServiceUri")
    def host_service_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="identityCertThumbprint")
    def identity_cert_thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isIdentityCertExprired")
    def is_identity_cert_exprired(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceToken")
    def service_token(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

class AwaitableGetIntegrationRuntimeConnectionInfoResult(
    GetIntegrationRuntimeConnectionInfoResult
):
    def __await__(self): ...

def get_integration_runtime_connection_info(
    factory_name: Optional[_builtins.str] = ...,
    integration_runtime_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIntegrationRuntimeConnectionInfoResult: ...
def get_integration_runtime_connection_info_output(
    factory_name: Optional[pulumi.Input[_builtins.str]] = ...,
    integration_runtime_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIntegrationRuntimeConnectionInfoResult]: ...
