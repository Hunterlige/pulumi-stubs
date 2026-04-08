import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SignalRCustomCertificateArgs", "SignalRCustomCertificate"]

@pulumi.input_type
class SignalRCustomCertificateArgs:
    def __init__(
        __self__,
        *,
        key_vault_base_uri: pulumi.Input[_builtins.str],
        key_vault_secret_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        resource_name: pulumi.Input[_builtins.str],
        certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultBaseUri")
    def key_vault_base_uri(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_base_uri.setter
    def key_vault_base_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_secret_name.setter
    def key_vault_secret_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretVersion")
    def key_vault_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_secret_version.setter
    def key_vault_secret_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

@pulumi.type_token(...)
class SignalRCustomCertificate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        certificate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_base_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_secret_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_name_: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SignalRCustomCertificateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> SignalRCustomCertificate: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultBaseUri")
    def key_vault_base_uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultSecretVersion")
    def key_vault_secret_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
