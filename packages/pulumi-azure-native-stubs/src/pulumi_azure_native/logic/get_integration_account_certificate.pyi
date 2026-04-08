import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetIntegrationAccountCertificateResult",
    "AwaitableGetIntegrationAccountCertificateResult",
    "get_integration_account_certificate",
    "get_integration_account_certificate_output",
]

@pulumi.output_type
class GetIntegrationAccountCertificateResult:
    def __init__(
        __self__,
        azure_api_version=...,
        changed_time=...,
        created_time=...,
        id=...,
        key=...,
        location=...,
        metadata=...,
        name=...,
        public_certificate=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[outputs.KeyVaultKeyReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicCertificate")
    def public_certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetIntegrationAccountCertificateResult(
    GetIntegrationAccountCertificateResult
):
    def __await__(self): ...

def get_integration_account_certificate(
    certificate_name: Optional[_builtins.str] = ...,
    integration_account_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetIntegrationAccountCertificateResult: ...
def get_integration_account_certificate_output(
    certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
    integration_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetIntegrationAccountCertificateResult]: ...
