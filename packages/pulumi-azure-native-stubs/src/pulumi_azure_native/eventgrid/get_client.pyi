import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetClientResult",
    "AwaitableGetClientResult",
    "get_client",
    "get_client_output",
]

@pulumi.output_type
class GetClientResult:
    def __init__(
        __self__,
        attributes=...,
        authentication_name=...,
        azure_api_version=...,
        client_certificate_authentication=...,
        description=...,
        id=...,
        name=...,
        provisioning_state=...,
        state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attributes(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter(name="authenticationName")
    def authentication_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateAuthentication")
    def client_certificate_authentication(
        self,
    ) -> Optional[outputs.ClientCertificateAuthenticationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetClientResult(GetClientResult):
    def __await__(self): ...

def get_client(
    client_name: Optional[_builtins.str] = ...,
    namespace_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetClientResult: ...
def get_client_output(
    client_name: Optional[pulumi.Input[_builtins.str]] = ...,
    namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetClientResult]: ...
