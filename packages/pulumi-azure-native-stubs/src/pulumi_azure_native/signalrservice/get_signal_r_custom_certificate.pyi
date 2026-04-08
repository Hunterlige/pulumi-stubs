import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSignalRCustomCertificateResult",
    "AwaitableGetSignalRCustomCertificateResult",
    "get_signal_r_custom_certificate",
    "get_signal_r_custom_certificate_output",
]

@pulumi.output_type
class GetSignalRCustomCertificateResult:
    def __init__(
        __self__,
        azure_api_version=...,
        id=...,
        key_vault_base_uri=...,
        key_vault_secret_name=...,
        key_vault_secret_version=...,
        name=...,
        provisioning_state=...,
        system_data=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultBaseUri")
    def key_vault_base_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretVersion")
    def key_vault_secret_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSignalRCustomCertificateResult(GetSignalRCustomCertificateResult):
    def __await__(self): ...

def get_signal_r_custom_certificate(
    certificate_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    resource_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSignalRCustomCertificateResult: ...
def get_signal_r_custom_certificate_output(
    certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSignalRCustomCertificateResult]: ...
