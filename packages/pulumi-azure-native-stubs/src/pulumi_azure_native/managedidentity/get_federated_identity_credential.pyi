import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetFederatedIdentityCredentialResult",
    "AwaitableGetFederatedIdentityCredentialResult",
    "get_federated_identity_credential",
    "get_federated_identity_credential_output",
]

@pulumi.output_type
class GetFederatedIdentityCredentialResult:
    def __init__(
        __self__,
        audiences=...,
        azure_api_version=...,
        id=...,
        issuer=...,
        name=...,
        subject=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def audiences(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetFederatedIdentityCredentialResult(
    GetFederatedIdentityCredentialResult
):
    def __await__(self): ...

def get_federated_identity_credential(
    federated_identity_credential_resource_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetFederatedIdentityCredentialResult: ...
def get_federated_identity_credential_output(
    federated_identity_credential_resource_name: Optional[
        pulumi.Input[_builtins.str]
    ] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetFederatedIdentityCredentialResult]: ...
