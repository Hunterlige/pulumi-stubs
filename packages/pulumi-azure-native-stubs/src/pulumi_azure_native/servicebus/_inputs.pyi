import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ActionArgs",
    "ActionArgsDict",
    "ConnectionStateArgs",
    "ConnectionStateArgsDict",
    "CorrelationFilterArgs",
    "CorrelationFilterArgsDict",
    "EncryptionArgs",
    "EncryptionArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "NWRuleSetIpRulesArgs",
    "NWRuleSetIpRulesArgsDict",
    "NWRuleSetVirtualNetworkRulesArgs",
    "NWRuleSetVirtualNetworkRulesArgsDict",
    "PrivateEndpointConnectionArgs",
    "PrivateEndpointConnectionArgsDict",
    "PrivateEndpointArgs",
    "PrivateEndpointArgsDict",
    "SBClientAffinePropertiesArgs",
    "SBClientAffinePropertiesArgsDict",
    "SBSkuArgs",
    "SBSkuArgsDict",
    "SqlFilterArgs",
    "SqlFilterArgsDict",
    "SubnetArgs",
    "SubnetArgsDict",
    "UserAssignedIdentityPropertiesArgs",
    "UserAssignedIdentityPropertiesArgsDict",
]

class ActionArgsDict(TypedDict):
    compatibility_level: NotRequired[pulumi.Input[_builtins.int]]
    requires_preprocessing: NotRequired[pulumi.Input[_builtins.bool]]
    sql_expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ActionArgs:
    def __init__(
        __self__,
        *,
        compatibility_level: Optional[pulumi.Input[_builtins.int]] = ...,
        requires_preprocessing: Optional[pulumi.Input[_builtins.bool]] = ...,
        sql_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compatibilityLevel")
    def compatibility_level(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @compatibility_level.setter
    def compatibility_level(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="requiresPreprocessing")
    def requires_preprocessing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @requires_preprocessing.setter
    def requires_preprocessing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sqlExpression")
    def sql_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sql_expression.setter
    def sql_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionStateArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]]

@pulumi.input_type
class ConnectionStateArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]
        ] = ...,
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
    ) -> Optional[pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateLinkConnectionStatus]]
        ],
    ): ...

class CorrelationFilterArgsDict(TypedDict):
    content_type: NotRequired[pulumi.Input[_builtins.str]]
    correlation_id: NotRequired[pulumi.Input[_builtins.str]]
    label: NotRequired[pulumi.Input[_builtins.str]]
    message_id: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    reply_to: NotRequired[pulumi.Input[_builtins.str]]
    reply_to_session_id: NotRequired[pulumi.Input[_builtins.str]]
    requires_preprocessing: NotRequired[pulumi.Input[_builtins.bool]]
    session_id: NotRequired[pulumi.Input[_builtins.str]]
    to: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CorrelationFilterArgs:
    def __init__(
        __self__,
        *,
        content_type: Optional[pulumi.Input[_builtins.str]] = ...,
        correlation_id: Optional[pulumi.Input[_builtins.str]] = ...,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        message_id: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reply_to: Optional[pulumi.Input[_builtins.str]] = ...,
        reply_to_session_id: Optional[pulumi.Input[_builtins.str]] = ...,
        requires_preprocessing: Optional[pulumi.Input[_builtins.bool]] = ...,
        session_id: Optional[pulumi.Input[_builtins.str]] = ...,
        to: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @correlation_id.setter
    def correlation_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_id.setter
    def message_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replyTo")
    def reply_to(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reply_to.setter
    def reply_to(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replyToSessionId")
    def reply_to_session_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reply_to_session_id.setter
    def reply_to_session_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiresPreprocessing")
    def requires_preprocessing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @requires_preprocessing.setter
    def requires_preprocessing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionId")
    def session_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_id.setter
    def session_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def to(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @to.setter
    def to(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EncryptionArgsDict(TypedDict):
    key_source: NotRequired[pulumi.Input[KeySource]]
    key_vault_properties: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[KeyVaultPropertiesArgsDict]]]
    ]
    require_infrastructure_encryption: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class EncryptionArgs:
    def __init__(
        __self__,
        *,
        key_source: Optional[pulumi.Input[KeySource]] = ...,
        key_vault_properties: Optional[
            pulumi.Input[Sequence[pulumi.Input[KeyVaultPropertiesArgs]]]
        ] = ...,
        require_infrastructure_encryption: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keySource")
    def key_source(self) -> Optional[pulumi.Input[KeySource]]: ...
    @key_source.setter
    def key_source(self, value: Optional[pulumi.Input[KeySource]]): ...
    @_builtins.property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[KeyVaultPropertiesArgs]]]]: ...
    @key_vault_properties.setter
    def key_vault_properties(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[KeyVaultPropertiesArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requireInfrastructureEncryption")
    def require_infrastructure_encryption(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @require_infrastructure_encryption.setter
    def require_infrastructure_encryption(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class IdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[ManagedServiceIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ManagedServiceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ManagedServiceIdentityType]]): ...
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
    identity: NotRequired[pulumi.Input[UserAssignedIdentityPropertiesArgsDict]]
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    key_vault_uri: NotRequired[pulumi.Input[_builtins.str]]
    key_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        identity: Optional[pulumi.Input[UserAssignedIdentityPropertiesArgs]] = ...,
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        key_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> Optional[pulumi.Input[UserAssignedIdentityPropertiesArgs]]: ...
    @identity.setter
    def identity(
        self, value: Optional[pulumi.Input[UserAssignedIdentityPropertiesArgs]]
    ): ...
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

class NWRuleSetIpRulesArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[Union[_builtins.str, NetworkRuleIPAction]]]
    ip_mask: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NWRuleSetIpRulesArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleIPAction]]] = ...,
        ip_mask: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NetworkRuleIPAction]]]: ...
    @action.setter
    def action(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NetworkRuleIPAction]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_mask.setter
    def ip_mask(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NWRuleSetVirtualNetworkRulesArgsDict(TypedDict):
    ignore_missing_vnet_service_endpoint: NotRequired[pulumi.Input[_builtins.bool]]
    subnet: NotRequired[pulumi.Input[SubnetArgsDict]]

@pulumi.input_type
class NWRuleSetVirtualNetworkRulesArgs:
    def __init__(
        __self__,
        *,
        ignore_missing_vnet_service_endpoint: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        subnet: Optional[pulumi.Input[SubnetArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_missing_vnet_service_endpoint.setter
    def ignore_missing_vnet_service_endpoint(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[SubnetArgs]]: ...
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[SubnetArgs]]): ...

class PrivateEndpointConnectionArgsDict(TypedDict):
    private_endpoint: NotRequired[pulumi.Input[PrivateEndpointArgsDict]]
    private_link_service_connection_state: NotRequired[
        pulumi.Input[ConnectionStateArgsDict]
    ]
    provisioning_state: NotRequired[
        pulumi.Input[Union[_builtins.str, EndPointProvisioningState]]
    ]

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        private_endpoint: Optional[pulumi.Input[PrivateEndpointArgs]] = ...,
        private_link_service_connection_state: Optional[
            pulumi.Input[ConnectionStateArgs]
        ] = ...,
        provisioning_state: Optional[
            pulumi.Input[Union[_builtins.str, EndPointProvisioningState]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input[PrivateEndpointArgs]]: ...
    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input[PrivateEndpointArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> Optional[pulumi.Input[ConnectionStateArgs]]: ...
    @private_link_service_connection_state.setter
    def private_link_service_connection_state(
        self, value: Optional[pulumi.Input[ConnectionStateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EndPointProvisioningState]]]: ...
    @provisioning_state.setter
    def provisioning_state(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, EndPointProvisioningState]]],
    ): ...

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

class SBClientAffinePropertiesArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    is_durable: NotRequired[pulumi.Input[_builtins.bool]]
    is_shared: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class SBClientAffinePropertiesArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        is_durable: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_shared: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isDurable")
    def is_durable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_durable.setter
    def is_durable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isShared")
    def is_shared(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_shared.setter
    def is_shared(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class SBSkuArgsDict(TypedDict):
    name: pulumi.Input[SkuName]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    tier: NotRequired[pulumi.Input[SkuTier]]

@pulumi.input_type
class SBSkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[SkuName],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        tier: Optional[pulumi.Input[SkuTier]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[SkuName]: ...
    @name.setter
    def name(self, value: pulumi.Input[SkuName]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[SkuTier]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[SkuTier]]): ...

class SqlFilterArgsDict(TypedDict):
    compatibility_level: NotRequired[pulumi.Input[_builtins.int]]
    requires_preprocessing: NotRequired[pulumi.Input[_builtins.bool]]
    sql_expression: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SqlFilterArgs:
    def __init__(
        __self__,
        *,
        compatibility_level: Optional[pulumi.Input[_builtins.int]] = ...,
        requires_preprocessing: Optional[pulumi.Input[_builtins.bool]] = ...,
        sql_expression: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="compatibilityLevel")
    def compatibility_level(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @compatibility_level.setter
    def compatibility_level(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="requiresPreprocessing")
    def requires_preprocessing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @requires_preprocessing.setter
    def requires_preprocessing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="sqlExpression")
    def sql_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sql_expression.setter
    def sql_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SubnetArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class SubnetArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class UserAssignedIdentityPropertiesArgsDict(TypedDict):
    user_assigned_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UserAssignedIdentityPropertiesArgs:
    def __init__(
        __self__, *, user_assigned_identity: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
