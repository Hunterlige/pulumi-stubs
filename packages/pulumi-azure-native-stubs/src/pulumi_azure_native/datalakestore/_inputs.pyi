import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CreateFirewallRuleWithAccountParametersArgs",
    "CreateFirewallRuleWithAccountParametersArgsDict",
    "CreateTrustedIdProviderWithAccountParametersArgs",
    ...,
    "CreateVirtualNetworkRuleWithAccountParametersArgs",
    ...,
    "EncryptionConfigArgs",
    "EncryptionConfigArgsDict",
    "EncryptionIdentityArgs",
    "EncryptionIdentityArgsDict",
    "KeyVaultMetaInfoArgs",
    "KeyVaultMetaInfoArgsDict",
]

class CreateFirewallRuleWithAccountParametersArgsDict(TypedDict):
    end_ip_address: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    start_ip_address: pulumi.Input[_builtins.str]

@pulumi.input_type
class CreateFirewallRuleWithAccountParametersArgs:
    def __init__(
        __self__,
        *,
        end_ip_address: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        start_ip_address: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> pulumi.Input[_builtins.str]: ...
    @end_ip_address.setter
    def end_ip_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> pulumi.Input[_builtins.str]: ...
    @start_ip_address.setter
    def start_ip_address(self, value: pulumi.Input[_builtins.str]): ...

class CreateTrustedIdProviderWithAccountParametersArgsDict(TypedDict):
    id_provider: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class CreateTrustedIdProviderWithAccountParametersArgs:
    def __init__(
        __self__,
        *,
        id_provider: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="idProvider")
    def id_provider(self) -> pulumi.Input[_builtins.str]: ...
    @id_provider.setter
    def id_provider(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class CreateVirtualNetworkRuleWithAccountParametersArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    subnet_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class CreateVirtualNetworkRuleWithAccountParametersArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        subnet_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...

class EncryptionConfigArgsDict(TypedDict):
    type: pulumi.Input[EncryptionConfigType]
    key_vault_meta_info: NotRequired[pulumi.Input[KeyVaultMetaInfoArgsDict]]

@pulumi.input_type
class EncryptionConfigArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[EncryptionConfigType],
        key_vault_meta_info: Optional[pulumi.Input[KeyVaultMetaInfoArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[EncryptionConfigType]: ...
    @type.setter
    def type(self, value: pulumi.Input[EncryptionConfigType]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultMetaInfo")
    def key_vault_meta_info(self) -> Optional[pulumi.Input[KeyVaultMetaInfoArgs]]: ...
    @key_vault_meta_info.setter
    def key_vault_meta_info(
        self, value: Optional[pulumi.Input[KeyVaultMetaInfoArgs]]
    ): ...

class EncryptionIdentityArgsDict(TypedDict):
    type: pulumi.Input[EncryptionIdentityType]

@pulumi.input_type
class EncryptionIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[EncryptionIdentityType]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[EncryptionIdentityType]: ...
    @type.setter
    def type(self, value: pulumi.Input[EncryptionIdentityType]): ...

class KeyVaultMetaInfoArgsDict(TypedDict):
    encryption_key_name: pulumi.Input[_builtins.str]
    encryption_key_version: pulumi.Input[_builtins.str]
    key_vault_resource_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class KeyVaultMetaInfoArgs:
    def __init__(
        __self__,
        *,
        encryption_key_name: pulumi.Input[_builtins.str],
        encryption_key_version: pulumi.Input[_builtins.str],
        key_vault_resource_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyName")
    def encryption_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @encryption_key_name.setter
    def encryption_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyVersion")
    def encryption_key_version(self) -> pulumi.Input[_builtins.str]: ...
    @encryption_key_version.setter
    def encryption_key_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultResourceId")
    def key_vault_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_resource_id.setter
    def key_vault_resource_id(self, value: pulumi.Input[_builtins.str]): ...
