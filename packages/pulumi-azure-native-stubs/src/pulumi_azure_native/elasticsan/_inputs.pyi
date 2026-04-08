import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EncryptionIdentityArgs",
    "EncryptionIdentityArgsDict",
    "EncryptionPropertiesArgs",
    "EncryptionPropertiesArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "ManagedByInfoArgs",
    "ManagedByInfoArgsDict",
    "NetworkRuleSetArgs",
    "NetworkRuleSetArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SnapshotCreationDataArgs",
    "SnapshotCreationDataArgsDict",
    "SourceCreationDataArgs",
    "SourceCreationDataArgsDict",
    "VirtualNetworkRuleArgs",
    "VirtualNetworkRuleArgsDict",
]

class EncryptionIdentityArgsDict(TypedDict):
    encryption_user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EncryptionIdentityArgs:
    def __init__(
        __self__,
        *,
        encryption_user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionUserAssignedIdentity")
    def encryption_user_assigned_identity(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_user_assigned_identity.setter
    def encryption_user_assigned_identity(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class EncryptionPropertiesArgsDict(TypedDict):
    encryption_identity: NotRequired[pulumi.Input[EncryptionIdentityArgsDict]]
    key_vault_properties: NotRequired[pulumi.Input[KeyVaultPropertiesArgsDict]]

@pulumi.input_type
class EncryptionPropertiesArgs:
    def __init__(
        __self__,
        *,
        encryption_identity: Optional[pulumi.Input[EncryptionIdentityArgs]] = ...,
        key_vault_properties: Optional[pulumi.Input[KeyVaultPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionIdentity")
    def encryption_identity(self) -> Optional[pulumi.Input[EncryptionIdentityArgs]]: ...
    @encryption_identity.setter
    def encryption_identity(
        self, value: Optional[pulumi.Input[EncryptionIdentityArgs]]
    ): ...
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
    type: pulumi.Input[Union[_builtins.str, IdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[Union[_builtins.str, IdentityType]],
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, IdentityType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, IdentityType]]): ...
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
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]
    key_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ManagedByInfoArgsDict(TypedDict):
    resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ManagedByInfoArgs:
    def __init__(
        __self__, *, resource_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NetworkRuleSetArgsDict(TypedDict):
    virtual_network_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgsDict]]]
    ]

@pulumi.input_type
class NetworkRuleSetArgs:
    def __init__(
        __self__,
        *,
        virtual_network_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgs]]]]: ...
    @virtual_network_rules.setter
    def virtual_network_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[VirtualNetworkRuleArgs]]]],
    ): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ],
    ): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]
    tier: NotRequired[pulumi.Input[Union[_builtins.str, SkuTier]]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[Union[_builtins.str, SkuName]],
        tier: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[_builtins.str, SkuTier]]]): ...

class SnapshotCreationDataArgsDict(TypedDict):
    source_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class SnapshotCreationDataArgs:
    def __init__(__self__, *, source_id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[_builtins.str]: ...
    @source_id.setter
    def source_id(self, value: pulumi.Input[_builtins.str]): ...

class SourceCreationDataArgsDict(TypedDict):
    create_source: NotRequired[pulumi.Input[Union[_builtins.str, VolumeCreateOption]]]
    source_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SourceCreationDataArgs:
    def __init__(
        __self__,
        *,
        create_source: Optional[
            pulumi.Input[Union[_builtins.str, VolumeCreateOption]]
        ] = ...,
        source_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createSource")
    def create_source(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, VolumeCreateOption]]]: ...
    @create_source.setter
    def create_source(
        self, value: Optional[pulumi.Input[Union[_builtins.str, VolumeCreateOption]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_id.setter
    def source_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworkRuleArgsDict(TypedDict):
    virtual_network_resource_id: pulumi.Input[_builtins.str]
    action: NotRequired[pulumi.Input[Union[_builtins.str, Action]]]

@pulumi.input_type
class VirtualNetworkRuleArgs:
    def __init__(
        __self__,
        *,
        virtual_network_resource_id: pulumi.Input[_builtins.str],
        action: Optional[pulumi.Input[Union[_builtins.str, Action]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="virtualNetworkResourceId")
    def virtual_network_resource_id(self) -> pulumi.Input[_builtins.str]: ...
    @virtual_network_resource_id.setter
    def virtual_network_resource_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[_builtins.str, Action]]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[Union[_builtins.str, Action]]]): ...
