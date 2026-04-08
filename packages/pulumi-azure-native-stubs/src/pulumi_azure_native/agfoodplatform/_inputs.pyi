import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApiKeyAuthCredentialsArgs",
    "ApiKeyAuthCredentialsArgsDict",
    "ApiPropertiesArgs",
    "ApiPropertiesArgsDict",
    "DataConnectorPropertiesArgs",
    "DataConnectorPropertiesArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "OAuthClientCredentialsArgs",
    "OAuthClientCredentialsArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "SensorIntegrationArgs",
    "SensorIntegrationArgsDict",
    "SolutionPropertiesArgs",
    "SolutionPropertiesArgsDict",
]

class ApiKeyAuthCredentialsArgsDict(TypedDict):
    api_key: pulumi.Input[KeyVaultPropertiesArgsDict]
    kind: pulumi.Input[_builtins.str]

@pulumi.input_type
class ApiKeyAuthCredentialsArgs:
    def __init__(
        __self__,
        *,
        api_key: pulumi.Input[KeyVaultPropertiesArgs],
        kind: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[KeyVaultPropertiesArgs]: ...
    @api_key.setter
    def api_key(self, value: pulumi.Input[KeyVaultPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...

class ApiPropertiesArgsDict(TypedDict):
    api_freshness_time_in_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ApiPropertiesArgs:
    def __init__(
        __self__,
        *,
        api_freshness_time_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiFreshnessTimeInMinutes")
    def api_freshness_time_in_minutes(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @api_freshness_time_in_minutes.setter
    def api_freshness_time_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class DataConnectorPropertiesArgsDict(TypedDict):
    credentials: pulumi.Input[
        Union[ApiKeyAuthCredentialsArgsDict, OAuthClientCredentialsArgsDict]
    ]

@pulumi.input_type
class DataConnectorPropertiesArgs:
    def __init__(
        __self__,
        *,
        credentials: pulumi.Input[
            Union[ApiKeyAuthCredentialsArgs, OAuthClientCredentialsArgs]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credentials(
        self,
    ) -> pulumi.Input[Union[ApiKeyAuthCredentialsArgs, OAuthClientCredentialsArgs]]: ...
    @credentials.setter
    def credentials(
        self,
        value: pulumi.Input[
            Union[ApiKeyAuthCredentialsArgs, OAuthClientCredentialsArgs]
        ],
    ): ...

class IdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]

@pulumi.input_type
class IdentityArgs:
    def __init__(
        __self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...

class KeyVaultPropertiesArgsDict(TypedDict):
    key_name: pulumi.Input[_builtins.str]
    key_vault_uri: pulumi.Input[_builtins.str]
    key_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_name: pulumi.Input[_builtins.str],
        key_vault_uri: pulumi.Input[_builtins.str],
        key_version: pulumi.Input[_builtins.str],
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
    def key_version(self) -> pulumi.Input[_builtins.str]: ...
    @key_version.setter
    def key_version(self, value: pulumi.Input[_builtins.str]): ...

class OAuthClientCredentialsArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret: pulumi.Input[KeyVaultPropertiesArgsDict]
    kind: pulumi.Input[_builtins.str]

@pulumi.input_type
class OAuthClientCredentialsArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        client_secret: pulumi.Input[KeyVaultPropertiesArgs],
        kind: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[KeyVaultPropertiesArgs]: ...
    @client_secret.setter
    def client_secret(self, value: pulumi.Input[KeyVaultPropertiesArgs]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...

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

class SensorIntegrationArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SensorIntegrationArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SolutionPropertiesArgsDict(TypedDict):
    marketplace_publisher_id: pulumi.Input[_builtins.str]
    offer_id: pulumi.Input[_builtins.str]
    plan_id: pulumi.Input[_builtins.str]
    saas_subscription_id: pulumi.Input[_builtins.str]
    saas_subscription_name: pulumi.Input[_builtins.str]
    term_id: pulumi.Input[_builtins.str]
    role_assignment_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SolutionPropertiesArgs:
    def __init__(
        __self__,
        *,
        marketplace_publisher_id: pulumi.Input[_builtins.str],
        offer_id: pulumi.Input[_builtins.str],
        plan_id: pulumi.Input[_builtins.str],
        saas_subscription_id: pulumi.Input[_builtins.str],
        saas_subscription_name: pulumi.Input[_builtins.str],
        term_id: pulumi.Input[_builtins.str],
        role_assignment_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="marketplacePublisherId")
    def marketplace_publisher_id(self) -> pulumi.Input[_builtins.str]: ...
    @marketplace_publisher_id.setter
    def marketplace_publisher_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> pulumi.Input[_builtins.str]: ...
    @offer_id.setter
    def offer_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> pulumi.Input[_builtins.str]: ...
    @plan_id.setter
    def plan_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="saasSubscriptionId")
    def saas_subscription_id(self) -> pulumi.Input[_builtins.str]: ...
    @saas_subscription_id.setter
    def saas_subscription_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="saasSubscriptionName")
    def saas_subscription_name(self) -> pulumi.Input[_builtins.str]: ...
    @saas_subscription_name.setter
    def saas_subscription_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="termId")
    def term_id(self) -> pulumi.Input[_builtins.str]: ...
    @term_id.setter
    def term_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleAssignmentId")
    def role_assignment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_assignment_id.setter
    def role_assignment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
