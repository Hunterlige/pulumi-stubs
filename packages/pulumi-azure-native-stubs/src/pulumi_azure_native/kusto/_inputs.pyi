import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AcceptedAudiencesArgs",
    "AcceptedAudiencesArgsDict",
    "AzureSkuArgs",
    "AzureSkuArgsDict",
    "CalloutPolicyArgs",
    "CalloutPolicyArgsDict",
    "IdentityArgs",
    "IdentityArgsDict",
    "KeyVaultPropertiesArgs",
    "KeyVaultPropertiesArgsDict",
    "LanguageExtensionsListArgs",
    "LanguageExtensionsListArgsDict",
    "LanguageExtensionArgs",
    "LanguageExtensionArgsDict",
    "OptimizedAutoscaleArgs",
    "OptimizedAutoscaleArgsDict",
    "PrivateLinkServiceConnectionStatePropertyArgs",
    "PrivateLinkServiceConnectionStatePropertyArgsDict",
    "TableLevelSharingPropertiesArgs",
    "TableLevelSharingPropertiesArgsDict",
    "TrustedExternalTenantArgs",
    "TrustedExternalTenantArgsDict",
    "VirtualNetworkConfigurationArgs",
    "VirtualNetworkConfigurationArgsDict",
]

class AcceptedAudiencesArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AcceptedAudiencesArgs:
    def __init__(
        __self__, *, value: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureSkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, AzureSkuName]]
    tier: pulumi.Input[Union[_builtins.str, AzureSkuTier]]
    capacity: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class AzureSkuArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[Union[_builtins.str, AzureSkuName]],
        tier: pulumi.Input[Union[_builtins.str, AzureSkuTier]],
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, AzureSkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, AzureSkuName]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[_builtins.str, AzureSkuTier]]: ...
    @tier.setter
    def tier(self, value: pulumi.Input[Union[_builtins.str, AzureSkuTier]]): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class CalloutPolicyArgsDict(TypedDict):
    callout_type: NotRequired[pulumi.Input[Union[_builtins.str, CalloutType]]]
    callout_uri_regex: NotRequired[pulumi.Input[_builtins.str]]
    outbound_access: NotRequired[pulumi.Input[Union[_builtins.str, OutboundAccess]]]

@pulumi.input_type
class CalloutPolicyArgs:
    def __init__(
        __self__,
        *,
        callout_type: Optional[pulumi.Input[Union[_builtins.str, CalloutType]]] = ...,
        callout_uri_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        outbound_access: Optional[
            pulumi.Input[Union[_builtins.str, OutboundAccess]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="calloutType")
    def callout_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CalloutType]]]: ...
    @callout_type.setter
    def callout_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CalloutType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="calloutUriRegex")
    def callout_uri_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @callout_uri_regex.setter
    def callout_uri_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outboundAccess")
    def outbound_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OutboundAccess]]]: ...
    @outbound_access.setter
    def outbound_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OutboundAccess]]]
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
    user_identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_vault_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        key_version: Optional[pulumi.Input[_builtins.str]] = ...,
        user_identity: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @_builtins.property
    @pulumi.getter(name="userIdentity")
    def user_identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_identity.setter
    def user_identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LanguageExtensionsListArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[Sequence[pulumi.Input[LanguageExtensionArgsDict]]]]

@pulumi.input_type
class LanguageExtensionsListArgs:
    def __init__(
        __self__,
        *,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LanguageExtensionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LanguageExtensionArgs]]]]: ...
    @value.setter
    def value(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LanguageExtensionArgs]]]],
    ): ...

class LanguageExtensionArgsDict(TypedDict):
    language_extension_custom_image_name: NotRequired[pulumi.Input[_builtins.str]]
    language_extension_image_name: NotRequired[
        pulumi.Input[Union[_builtins.str, LanguageExtensionImageName]]
    ]
    language_extension_name: NotRequired[
        pulumi.Input[Union[_builtins.str, LanguageExtensionName]]
    ]

@pulumi.input_type
class LanguageExtensionArgs:
    def __init__(
        __self__,
        *,
        language_extension_custom_image_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        language_extension_image_name: Optional[
            pulumi.Input[Union[_builtins.str, LanguageExtensionImageName]]
        ] = ...,
        language_extension_name: Optional[
            pulumi.Input[Union[_builtins.str, LanguageExtensionName]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageExtensionCustomImageName")
    def language_extension_custom_image_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_extension_custom_image_name.setter
    def language_extension_custom_image_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageExtensionImageName")
    def language_extension_image_name(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LanguageExtensionImageName]]]: ...
    @language_extension_image_name.setter
    def language_extension_image_name(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, LanguageExtensionImageName]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageExtensionName")
    def language_extension_name(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LanguageExtensionName]]]: ...
    @language_extension_name.setter
    def language_extension_name(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LanguageExtensionName]]]
    ): ...

class OptimizedAutoscaleArgsDict(TypedDict):
    is_enabled: pulumi.Input[_builtins.bool]
    maximum: pulumi.Input[_builtins.int]
    minimum: pulumi.Input[_builtins.int]
    version: pulumi.Input[_builtins.int]

@pulumi.input_type
class OptimizedAutoscaleArgs:
    def __init__(
        __self__,
        *,
        is_enabled: pulumi.Input[_builtins.bool],
        maximum: pulumi.Input[_builtins.int],
        minimum: pulumi.Input[_builtins.int],
        version: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> pulumi.Input[_builtins.int]: ...
    @maximum.setter
    def maximum(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> pulumi.Input[_builtins.int]: ...
    @minimum.setter
    def minimum(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.int]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.int]): ...

class PrivateLinkServiceConnectionStatePropertyArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PrivateLinkServiceConnectionStatePropertyArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TableLevelSharingPropertiesArgsDict(TypedDict):
    external_tables_to_exclude: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    external_tables_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    functions_to_exclude: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    functions_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    materialized_views_to_exclude: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    materialized_views_to_include: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    tables_to_exclude: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    tables_to_include: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class TableLevelSharingPropertiesArgs:
    def __init__(
        __self__,
        *,
        external_tables_to_exclude: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        external_tables_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        functions_to_exclude: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        functions_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        materialized_views_to_exclude: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        materialized_views_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tables_to_exclude: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tables_to_include: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalTablesToExclude")
    def external_tables_to_exclude(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_tables_to_exclude.setter
    def external_tables_to_exclude(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="externalTablesToInclude")
    def external_tables_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @external_tables_to_include.setter
    def external_tables_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="functionsToExclude")
    def functions_to_exclude(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @functions_to_exclude.setter
    def functions_to_exclude(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="functionsToInclude")
    def functions_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @functions_to_include.setter
    def functions_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="materializedViewsToExclude")
    def materialized_views_to_exclude(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @materialized_views_to_exclude.setter
    def materialized_views_to_exclude(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="materializedViewsToInclude")
    def materialized_views_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @materialized_views_to_include.setter
    def materialized_views_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tablesToExclude")
    def tables_to_exclude(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tables_to_exclude.setter
    def tables_to_exclude(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tablesToInclude")
    def tables_to_include(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tables_to_include.setter
    def tables_to_include(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TrustedExternalTenantArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TrustedExternalTenantArgs:
    def __init__(
        __self__, *, value: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VirtualNetworkConfigurationArgsDict(TypedDict):
    data_management_public_ip_id: pulumi.Input[_builtins.str]
    engine_public_ip_id: pulumi.Input[_builtins.str]
    subnet_id: pulumi.Input[_builtins.str]
    state: NotRequired[pulumi.Input[Union[_builtins.str, VnetState]]]

@pulumi.input_type
class VirtualNetworkConfigurationArgs:
    def __init__(
        __self__,
        *,
        data_management_public_ip_id: pulumi.Input[_builtins.str],
        engine_public_ip_id: pulumi.Input[_builtins.str],
        subnet_id: pulumi.Input[_builtins.str],
        state: Optional[pulumi.Input[Union[_builtins.str, VnetState]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataManagementPublicIpId")
    def data_management_public_ip_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_management_public_ip_id.setter
    def data_management_public_ip_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="enginePublicIpId")
    def engine_public_ip_id(self) -> pulumi.Input[_builtins.str]: ...
    @engine_public_ip_id.setter
    def engine_public_ip_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[_builtins.str]: ...
    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, VnetState]]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, VnetState]]]): ...
