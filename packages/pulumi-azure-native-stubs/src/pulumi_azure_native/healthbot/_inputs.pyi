import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "HealthBotPropertiesArgs",
    "HealthBotPropertiesArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "SkuArgs",
    "SkuArgsDict",
]

class HealthBotPropertiesArgsDict(TypedDict):
    key_vault_properties: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]

@pulumi.input_type
class HealthBotPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_vault_properties: Optional[pulumi.Input[KeyVaultPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(
        self,
    ) -> Optional[pulumi.Input[KeyVaultPropertiesArgs]]: ...
    @key_vault_properties.setter
    def key_vault_properties(
        self, value: Optional[pulumi.Input[KeyVaultPropertiesArgs]]
    ): ...

class IdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[ResourceIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class KeyVaultPropertiesArgsDict(TypedDict):
    key_name: pulumi.Input[_builtins.str]
    key_vault_uri: pulumi.Input[_builtins.str]
    key_version: NotRequired[pulumi.Input[_builtins.str]]
    user_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_name: pulumi.Input[_builtins.str],
        key_vault_uri: pulumi.Input[_builtins.str],
        key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        user_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]: ...
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[_builtins.str]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="userIdentity")
    def user_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_identity.setter
    def user_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[SkuName]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[SkuName]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[SkuName]: ...
    @name.setter
    def name(self, value: pulumi.Input[SkuName]): ...
