import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWorkspaceCertificateResult",
    "AwaitableGetWorkspaceCertificateResult",
    "get_workspace_certificate",
    "get_workspace_certificate_output",
]

@pulumi.output_type
class GetWorkspaceCertificateResult:
    def __init__(
        __self__,
        azure_api_version=...,
        expiration_date=...,
        id=...,
        key_vault=...,
        name=...,
        subject=...,
        thumbprint=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[outputs.KeyVaultContractPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetWorkspaceCertificateResult(GetWorkspaceCertificateResult):
    def __await__(self): ...

def get_workspace_certificate(
    certificate_id: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    service_name: Optional[_builtins.str] = ...,
    workspace_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWorkspaceCertificateResult: ...
def get_workspace_certificate_output(
    certificate_id: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    workspace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWorkspaceCertificateResult]: ...
