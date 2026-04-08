import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [..., ..., ..., ...]

@pulumi.output_type
class GetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult:
    def __init__(
        __self__,
        azure_api_version=...,
        certificate_url=...,
        dns_suffix=...,
        id=...,
        key_vault_reference_identity=...,
        kind=...,
        name=...,
        provisioning_details=...,
        provisioning_state=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateUrl")
    def certificate_url(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningDetails")
    def provisioning_details(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult(
    GetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult
):
    def __await__(self): ...

def get_app_service_environment_ase_custom_dns_suffix_configuration(
    name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult: ...
def get_app_service_environment_ase_custom_dns_suffix_configuration_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAppServiceEnvironmentAseCustomDnsSuffixConfigurationResult]: ...
