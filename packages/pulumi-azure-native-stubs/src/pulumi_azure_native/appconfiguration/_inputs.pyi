import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataPlaneProxyPropertiesArgs",
    "DataPlaneProxyPropertiesArgsDict",
    "EncryptionPropertiesArgs",
    "EncryptionPropertiesArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "PrivateEndpointArgs",
    "PrivateEndpointArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "ResourceIdentityArgs",
    "ResourceIdentityArgsDict",
    "SkuArgs",
    "SkuArgsDict",
]

class DataPlaneProxyPropertiesArgsDict(TypedDict):
    authentication_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, AuthenticationMode]]
    ]
    private_link_delegation: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateLinkDelegation]]
    ]

@pulumi.input_type
class DataPlaneProxyPropertiesArgs:
    def __init__(
        __self__,
        *,
        authentication_mode: Optional[
            pulumi.Input[Union[_builtins.str, AuthenticationMode]]
        ] = ...,
        private_link_delegation: Optional[
            pulumi.Input[Union[_builtins.str, PrivateLinkDelegation]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationMode")
    def authentication_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationMode]]]: ...
    @authentication_mode.setter
    def authentication_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkDelegation")
    def private_link_delegation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrivateLinkDelegation]]]: ...
    @private_link_delegation.setter
    def private_link_delegation(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateLinkDelegation]]]
    ): ...

class EncryptionPropertiesArgsDict(TypedDict):
    key_vault_properties: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]

@pulumi.input_type
class EncryptionPropertiesArgs:
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

class KeyVaultPropertiesArgsDict(TypedDict):
    identity_client_id: NotRequired[pulumi.Input[_builtins.str]]
    key_identifier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        identity_client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_client_id.setter
    def identity_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_identifier.setter
    def key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateEndpointArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, ConnectionStatus]]]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, ConnectionStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ConnectionStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ConnectionStatus]]]
    ): ...

class ResourceIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[Union[_builtins.str, IdentityType]]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ResourceIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, IdentityType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
