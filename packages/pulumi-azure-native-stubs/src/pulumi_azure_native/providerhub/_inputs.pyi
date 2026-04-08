import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AdditionalAuthorizationArgs",
    "AdditionalAuthorizationArgsDict",
    "AllowedResourceNameArgs",
    "AllowedResourceNameArgsDict",
    "AllowedUnauthorizedActionsExtensionArgs",
    "AllowedUnauthorizedActionsExtensionArgsDict",
    "ApiProfileArgs",
    "ApiProfileArgsDict",
    "ApplicationDataAuthorizationArgs",
    "ApplicationDataAuthorizationArgsDict",
    "ApplicationProviderAuthorizationArgs",
    "ApplicationProviderAuthorizationArgsDict",
    "AsyncOperationPollingRulesArgs",
    "AsyncOperationPollingRulesArgsDict",
    "AsyncTimeoutRuleArgs",
    "AsyncTimeoutRuleArgsDict",
    "AuthorizationActionMappingArgs",
    "AuthorizationActionMappingArgsDict",
    "AuthorizedApplicationPropertiesArgs",
    "AuthorizedApplicationPropertiesArgsDict",
    "CustomRolloutPropertiesSpecificationArgs",
    "CustomRolloutPropertiesSpecificationArgsDict",
    "CustomRolloutPropertiesStatusArgs",
    "CustomRolloutPropertiesStatusArgsDict",
    "CustomRolloutPropertiesArgs",
    "CustomRolloutPropertiesArgsDict",
    "CustomRolloutSpecificationAutoProvisionConfigArgs",
    ...,
    "CustomRolloutSpecificationCanaryArgs",
    "CustomRolloutSpecificationCanaryArgsDict",
    "CustomRolloutSpecificationProviderRegistrationArgs",
    ...,
    "CustomRolloutStatusManifestCheckinStatusArgs",
    "CustomRolloutStatusManifestCheckinStatusArgsDict",
    "DefaultRolloutPropertiesSpecificationArgs",
    "DefaultRolloutPropertiesSpecificationArgsDict",
    "DefaultRolloutPropertiesStatusArgs",
    "DefaultRolloutPropertiesStatusArgsDict",
    "DefaultRolloutPropertiesArgs",
    "DefaultRolloutPropertiesArgsDict",
    "DefaultRolloutSpecificationAutoProvisionConfigArgs",
    ...,
    "DefaultRolloutSpecificationCanaryArgs",
    "DefaultRolloutSpecificationCanaryArgsDict",
    "DefaultRolloutSpecificationExpeditedRolloutArgs",
    ...,
    "DefaultRolloutSpecificationHighTrafficArgs",
    "DefaultRolloutSpecificationHighTrafficArgsDict",
    "DefaultRolloutSpecificationLowTrafficArgs",
    "DefaultRolloutSpecificationLowTrafficArgsDict",
    "DefaultRolloutSpecificationMediumTrafficArgs",
    "DefaultRolloutSpecificationMediumTrafficArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DefaultRolloutStatusManifestCheckinStatusArgs",
    "DefaultRolloutStatusManifestCheckinStatusArgsDict",
    "DeleteDependencyArgs",
    "DeleteDependencyArgsDict",
    "EndpointInformationArgs",
    "EndpointInformationArgsDict",
    "ExtendedErrorInfoArgs",
    "ExtendedErrorInfoArgsDict",
    "ExtendedLocationOptionsArgs",
    "ExtendedLocationOptionsArgsDict",
    "FanoutLinkedNotificationRuleDstsConfigurationArgs",
    ...,
    "FanoutLinkedNotificationRuleArgs",
    "FanoutLinkedNotificationRuleArgsDict",
    "FilterRuleArgs",
    "FilterRuleArgsDict",
    "LegacyDisallowedConditionArgs",
    "LegacyDisallowedConditionArgsDict",
    "LightHouseAuthorizationArgs",
    "LightHouseAuthorizationArgsDict",
    "LinkedAccessCheckArgs",
    "LinkedAccessCheckArgsDict",
    "LinkedNotificationRuleArgs",
    "LinkedNotificationRuleArgsDict",
    "LinkedOperationRuleArgs",
    "LinkedOperationRuleArgsDict",
    "LocationQuotaRuleArgs",
    "LocationQuotaRuleArgsDict",
    "LoggingRuleHiddenPropertyPathsArgs",
    "LoggingRuleHiddenPropertyPathsArgsDict",
    "LoggingRuleArgs",
    "LoggingRuleArgsDict",
    "NotificationEndpointArgs",
    "NotificationEndpointArgsDict",
    "NotificationRegistrationPropertiesArgs",
    "NotificationRegistrationPropertiesArgsDict",
    "NotificationArgs",
    "NotificationArgsDict",
    "OpenApiConfigurationArgs",
    "OpenApiConfigurationArgsDict",
    "OpenApiValidationArgs",
    "OpenApiValidationArgsDict",
    "ProviderHubMetadataProviderAuthenticationArgs",
    "ProviderHubMetadataProviderAuthenticationArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ProviderRegistrationPropertiesArgs",
    "ProviderRegistrationPropertiesArgsDict",
    "QuotaRuleArgs",
    "QuotaRuleArgsDict",
    "ResourceAccessRoleArgs",
    "ResourceAccessRoleArgsDict",
    "ResourceConcurrencyControlOptionArgs",
    "ResourceConcurrencyControlOptionArgsDict",
    "ResourceHydrationAccountArgs",
    "ResourceHydrationAccountArgsDict",
    ...,
    ...,
    "ResourceProviderAuthorizationRulesArgs",
    "ResourceProviderAuthorizationRulesArgsDict",
    "ResourceProviderAuthorizationArgs",
    "ResourceProviderAuthorizationArgsDict",
    "ResourceProviderCapabilitiesArgs",
    "ResourceProviderCapabilitiesArgsDict",
    "ResourceProviderEndpointFeaturesRuleArgs",
    "ResourceProviderEndpointFeaturesRuleArgsDict",
    "ResourceProviderEndpointArgs",
    "ResourceProviderEndpointArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ResourceProviderManifestPropertiesFeaturesRuleArgs",
    ...,
    "ResourceProviderManifestPropertiesManagementArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ResourceProviderServiceArgs",
    "ResourceProviderServiceArgsDict",
    "ResourceTypeEndpointDstsConfigurationArgs",
    "ResourceTypeEndpointDstsConfigurationArgsDict",
    "ResourceTypeEndpointFeaturesRuleArgs",
    "ResourceTypeEndpointFeaturesRuleArgsDict",
    "ResourceTypeEndpointArgs",
    "ResourceTypeEndpointArgsDict",
    ...,
    ...,
    "ResourceTypeExtensionArgs",
    "ResourceTypeExtensionArgsDict",
    "ResourceTypeOnBehalfOfTokenArgs",
    "ResourceTypeOnBehalfOfTokenArgsDict",
    ...,
    ...,
    "ResourceTypeRegistrationPropertiesCapacityRuleArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ResourceTypeRegistrationPropertiesFeaturesRuleArgs",
    ...,
    ...,
    ...,
    "ResourceTypeRegistrationPropertiesLegacyPolicyArgs",
    ...,
    "ResourceTypeRegistrationPropertiesManagementArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ResourceTypeRegistrationPropertiesRoutingRuleArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ResourceTypeRegistrationPropertiesArgs",
    "ResourceTypeRegistrationPropertiesArgsDict",
    "ResourceTypeRegistrationArgs",
    "ResourceTypeRegistrationArgsDict",
    "ServiceTreeInfoArgs",
    "ServiceTreeInfoArgsDict",
    "SkuCapabilityArgs",
    "SkuCapabilityArgsDict",
    "SkuCostArgs",
    "SkuCostArgsDict",
    "SkuLocationInfoArgs",
    "SkuLocationInfoArgsDict",
    "SkuResourcePropertiesArgs",
    "SkuResourcePropertiesArgsDict",
    "SkuSettingCapacityArgs",
    "SkuSettingCapacityArgsDict",
    "SkuSettingArgs",
    "SkuSettingArgsDict",
    "SkuZoneDetailArgs",
    "SkuZoneDetailArgsDict",
    "SubscriberSettingArgs",
    "SubscriberSettingArgsDict",
    "SubscriptionStateOverrideActionArgs",
    "SubscriptionStateOverrideActionArgsDict",
    "SubscriptionStateRuleArgs",
    "SubscriptionStateRuleArgsDict",
    "SwaggerSpecificationArgs",
    "SwaggerSpecificationArgsDict",
    "ThirdPartyExtensionArgs",
    "ThirdPartyExtensionArgsDict",
    "ThrottlingMetricArgs",
    "ThrottlingMetricArgsDict",
    "ThrottlingRuleArgs",
    "ThrottlingRuleArgsDict",
    "TokenAuthConfigurationArgs",
    "TokenAuthConfigurationArgsDict",
    "TypedErrorInfoArgs",
    "TypedErrorInfoArgsDict",
]

class AdditionalAuthorizationArgsDict(TypedDict):
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    role_definition_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AdditionalAuthorizationArgs:
    def __init__(
        __self__,
        *,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AllowedResourceNameArgsDict(TypedDict):
    get_action_verb: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AllowedResourceNameArgs:
    def __init__(
        __self__,
        *,
        get_action_verb: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="getActionVerb")
    def get_action_verb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @get_action_verb.setter
    def get_action_verb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AllowedUnauthorizedActionsExtensionArgsDict(TypedDict):
    action: NotRequired[pulumi.Input[_builtins.str]]
    intent: NotRequired[pulumi.Input[Union[_builtins.str, Intent]]]

@pulumi.input_type
class AllowedUnauthorizedActionsExtensionArgs:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        intent: Optional[pulumi.Input[Union[_builtins.str, Intent]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[pulumi.Input[Union[_builtins.str, Intent]]]: ...
    @intent.setter
    def intent(self, value: Optional[pulumi.Input[Union[_builtins.str, Intent]]]): ...

class ApiProfileArgsDict(TypedDict):
    api_version: NotRequired[pulumi.Input[_builtins.str]]
    profile_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiProfileArgs:
    def __init__(
        __self__,
        *,
        api_version: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_version.setter
    def profile_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationDataAuthorizationArgsDict(TypedDict):
    role: pulumi.Input[Union[_builtins.str, Role]]
    resource_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ApplicationDataAuthorizationArgs:
    def __init__(
        __self__,
        *,
        role: pulumi.Input[Union[_builtins.str, Role]],
        resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[Union[_builtins.str, Role]]: ...
    @role.setter
    def role(self, value: pulumi.Input[Union[_builtins.str, Role]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_types.setter
    def resource_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ApplicationProviderAuthorizationArgsDict(TypedDict):
    managed_by_role_definition_id: NotRequired[pulumi.Input[_builtins.str]]
    role_definition_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationProviderAuthorizationArgs:
    def __init__(
        __self__,
        *,
        managed_by_role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedByRoleDefinitionId")
    def managed_by_role_definition_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by_role_definition_id.setter
    def managed_by_role_definition_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AsyncOperationPollingRulesArgsDict(TypedDict):
    additional_options: NotRequired[
        pulumi.Input[Union[_builtins.str, AdditionalOptionsAsyncOperation]]
    ]
    authorization_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class AsyncOperationPollingRulesArgs:
    def __init__(
        __self__,
        *,
        additional_options: Optional[
            pulumi.Input[Union[_builtins.str, AdditionalOptionsAsyncOperation]]
        ] = ...,
        authorization_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalOptions")
    def additional_options(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, AdditionalOptionsAsyncOperation]]
    ]: ...
    @additional_options.setter
    def additional_options(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, AdditionalOptionsAsyncOperation]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authorizationActions")
    def authorization_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @authorization_actions.setter
    def authorization_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AsyncTimeoutRuleArgsDict(TypedDict):
    action_name: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AsyncTimeoutRuleArgs:
    def __init__(
        __self__,
        *,
        action_name: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_name.setter
    def action_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthorizationActionMappingArgsDict(TypedDict):
    desired: NotRequired[pulumi.Input[_builtins.str]]
    original: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AuthorizationActionMappingArgs:
    def __init__(
        __self__,
        *,
        desired: Optional[pulumi.Input[_builtins.str]] = ...,
        original: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def desired(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired.setter
    def desired(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def original(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @original.setter
    def original(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AuthorizedApplicationPropertiesArgsDict(TypedDict):
    data_authorizations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ApplicationDataAuthorizationArgsDict]]]
    ]
    provider_authorization: NotRequired[
        pulumi.Input[ApplicationProviderAuthorizationArgsDict]
    ]

@pulumi.input_type
class AuthorizedApplicationPropertiesArgs:
    def __init__(
        __self__,
        *,
        data_authorizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationDataAuthorizationArgs]]]
        ] = ...,
        provider_authorization: Optional[
            pulumi.Input[ApplicationProviderAuthorizationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataAuthorizations")
    def data_authorizations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationDataAuthorizationArgs]]]
    ]: ...
    @data_authorizations.setter
    def data_authorizations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationDataAuthorizationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerAuthorization")
    def provider_authorization(
        self,
    ) -> Optional[pulumi.Input[ApplicationProviderAuthorizationArgs]]: ...
    @provider_authorization.setter
    def provider_authorization(
        self, value: Optional[pulumi.Input[ApplicationProviderAuthorizationArgs]]
    ): ...

class CustomRolloutPropertiesSpecificationArgsDict(TypedDict):
    auto_provision_config: NotRequired[
        pulumi.Input[CustomRolloutSpecificationAutoProvisionConfigArgsDict]
    ]
    canary: NotRequired[pulumi.Input[CustomRolloutSpecificationCanaryArgsDict]]
    provider_registration: NotRequired[
        pulumi.Input[CustomRolloutSpecificationProviderRegistrationArgsDict]
    ]
    refresh_subscription_registration: NotRequired[pulumi.Input[_builtins.bool]]
    release_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_type_registrations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceTypeRegistrationArgsDict]]]
    ]
    skip_release_scope_validation: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class CustomRolloutPropertiesSpecificationArgs:
    def __init__(
        __self__,
        *,
        auto_provision_config: Optional[
            pulumi.Input[CustomRolloutSpecificationAutoProvisionConfigArgs]
        ] = ...,
        canary: Optional[pulumi.Input[CustomRolloutSpecificationCanaryArgs]] = ...,
        provider_registration: Optional[
            pulumi.Input[CustomRolloutSpecificationProviderRegistrationArgs]
        ] = ...,
        refresh_subscription_registration: Optional[pulumi.Input[_builtins.bool]] = ...,
        release_scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_type_registrations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceTypeRegistrationArgs]]]
        ] = ...,
        skip_release_scope_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisionConfig")
    def auto_provision_config(
        self,
    ) -> Optional[pulumi.Input[CustomRolloutSpecificationAutoProvisionConfigArgs]]: ...
    @auto_provision_config.setter
    def auto_provision_config(
        self,
        value: Optional[
            pulumi.Input[CustomRolloutSpecificationAutoProvisionConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def canary(
        self,
    ) -> Optional[pulumi.Input[CustomRolloutSpecificationCanaryArgs]]: ...
    @canary.setter
    def canary(
        self, value: Optional[pulumi.Input[CustomRolloutSpecificationCanaryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerRegistration")
    def provider_registration(
        self,
    ) -> Optional[pulumi.Input[CustomRolloutSpecificationProviderRegistrationArgs]]: ...
    @provider_registration.setter
    def provider_registration(
        self,
        value: Optional[
            pulumi.Input[CustomRolloutSpecificationProviderRegistrationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="refreshSubscriptionRegistration")
    def refresh_subscription_registration(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @refresh_subscription_registration.setter
    def refresh_subscription_registration(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="releaseScopes")
    def release_scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @release_scopes.setter
    def release_scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeRegistrations")
    def resource_type_registrations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceTypeRegistrationArgs]]]
    ]: ...
    @resource_type_registrations.setter
    def resource_type_registrations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceTypeRegistrationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipReleaseScopeValidation")
    def skip_release_scope_validation(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_release_scope_validation.setter
    def skip_release_scope_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class CustomRolloutPropertiesStatusArgsDict(TypedDict):
    completed_regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    failed_or_skipped_regions: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ExtendedErrorInfoArgsDict]]]
    ]
    manifest_checkin_status: NotRequired[
        pulumi.Input[CustomRolloutStatusManifestCheckinStatusArgsDict]
    ]

@pulumi.input_type
class CustomRolloutPropertiesStatusArgs:
    def __init__(
        __self__,
        *,
        completed_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        failed_or_skipped_regions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ExtendedErrorInfoArgs]]]
        ] = ...,
        manifest_checkin_status: Optional[
            pulumi.Input[CustomRolloutStatusManifestCheckinStatusArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completedRegions")
    def completed_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @completed_regions.setter
    def completed_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failedOrSkippedRegions")
    def failed_or_skipped_regions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[ExtendedErrorInfoArgs]]]]: ...
    @failed_or_skipped_regions.setter
    def failed_or_skipped_regions(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ExtendedErrorInfoArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manifestCheckinStatus")
    def manifest_checkin_status(
        self,
    ) -> Optional[pulumi.Input[CustomRolloutStatusManifestCheckinStatusArgs]]: ...
    @manifest_checkin_status.setter
    def manifest_checkin_status(
        self,
        value: Optional[pulumi.Input[CustomRolloutStatusManifestCheckinStatusArgs]],
    ): ...

class CustomRolloutPropertiesArgsDict(TypedDict):
    specification: pulumi.Input[CustomRolloutPropertiesSpecificationArgsDict]
    status: NotRequired[pulumi.Input[CustomRolloutPropertiesStatusArgsDict]]

@pulumi.input_type
class CustomRolloutPropertiesArgs:
    def __init__(
        __self__,
        *,
        specification: pulumi.Input[CustomRolloutPropertiesSpecificationArgs],
        status: Optional[pulumi.Input[CustomRolloutPropertiesStatusArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def specification(
        self,
    ) -> pulumi.Input[CustomRolloutPropertiesSpecificationArgs]: ...
    @specification.setter
    def specification(
        self, value: pulumi.Input[CustomRolloutPropertiesSpecificationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[CustomRolloutPropertiesStatusArgs]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[CustomRolloutPropertiesStatusArgs]]
    ): ...

class CustomRolloutSpecificationAutoProvisionConfigArgsDict(TypedDict):
    resource_graph: NotRequired[pulumi.Input[_builtins.bool]]
    storage: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class CustomRolloutSpecificationAutoProvisionConfigArgs:
    def __init__(
        __self__,
        *,
        resource_graph: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGraph")
    def resource_graph(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @resource_graph.setter
    def resource_graph(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class CustomRolloutSpecificationCanaryArgsDict(TypedDict):
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class CustomRolloutSpecificationCanaryArgs:
    def __init__(
        __self__,
        *,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class CustomRolloutSpecificationProviderRegistrationArgsDict(TypedDict):
    kind: NotRequired[pulumi.Input[Union[_builtins.str, ProviderRegistrationKind]]]
    properties: NotRequired[pulumi.Input[ProviderRegistrationPropertiesArgsDict]]

@pulumi.input_type
class CustomRolloutSpecificationProviderRegistrationArgs:
    def __init__(
        __self__,
        *,
        kind: Optional[
            pulumi.Input[Union[_builtins.str, ProviderRegistrationKind]]
        ] = ...,
        properties: Optional[pulumi.Input[ProviderRegistrationPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProviderRegistrationKind]]]: ...
    @kind.setter
    def kind(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ProviderRegistrationKind]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[ProviderRegistrationPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[ProviderRegistrationPropertiesArgs]]
    ): ...

class CustomRolloutStatusManifestCheckinStatusArgsDict(TypedDict):
    is_checked_in: pulumi.Input[_builtins.bool]
    status_message: pulumi.Input[_builtins.str]
    commit_id: NotRequired[pulumi.Input[_builtins.str]]
    pull_request: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class CustomRolloutStatusManifestCheckinStatusArgs:
    def __init__(
        __self__,
        *,
        is_checked_in: pulumi.Input[_builtins.bool],
        status_message: pulumi.Input[_builtins.str],
        commit_id: Optional[pulumi.Input[_builtins.str]] = ...,
        pull_request: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCheckedIn")
    def is_checked_in(self) -> pulumi.Input[_builtins.bool]: ...
    @is_checked_in.setter
    def is_checked_in(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Input[_builtins.str]: ...
    @status_message.setter
    def status_message(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="commitId")
    def commit_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commit_id.setter
    def commit_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pull_request.setter
    def pull_request(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DefaultRolloutPropertiesSpecificationArgsDict(TypedDict):
    auto_provision_config: NotRequired[
        pulumi.Input[DefaultRolloutSpecificationAutoProvisionConfigArgsDict]
    ]
    canary: NotRequired[pulumi.Input[DefaultRolloutSpecificationCanaryArgsDict]]
    expedited_rollout: NotRequired[
        pulumi.Input[DefaultRolloutSpecificationExpeditedRolloutArgsDict]
    ]
    high_traffic: NotRequired[
        pulumi.Input[DefaultRolloutSpecificationHighTrafficArgsDict]
    ]
    low_traffic: NotRequired[
        pulumi.Input[DefaultRolloutSpecificationLowTrafficArgsDict]
    ]
    medium_traffic: NotRequired[
        pulumi.Input[DefaultRolloutSpecificationMediumTrafficArgsDict]
    ]
    provider_registration: NotRequired[
        pulumi.Input[DefaultRolloutSpecificationProviderRegistrationArgsDict]
    ]
    resource_type_registrations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceTypeRegistrationArgsDict]]]
    ]
    rest_of_the_world_group_one: NotRequired[
        pulumi.Input[DefaultRolloutSpecificationRestOfTheWorldGroupOneArgsDict]
    ]
    rest_of_the_world_group_two: NotRequired[
        pulumi.Input[DefaultRolloutSpecificationRestOfTheWorldGroupTwoArgsDict]
    ]

@pulumi.input_type
class DefaultRolloutPropertiesSpecificationArgs:
    def __init__(
        __self__,
        *,
        auto_provision_config: Optional[
            pulumi.Input[DefaultRolloutSpecificationAutoProvisionConfigArgs]
        ] = ...,
        canary: Optional[pulumi.Input[DefaultRolloutSpecificationCanaryArgs]] = ...,
        expedited_rollout: Optional[
            pulumi.Input[DefaultRolloutSpecificationExpeditedRolloutArgs]
        ] = ...,
        high_traffic: Optional[
            pulumi.Input[DefaultRolloutSpecificationHighTrafficArgs]
        ] = ...,
        low_traffic: Optional[
            pulumi.Input[DefaultRolloutSpecificationLowTrafficArgs]
        ] = ...,
        medium_traffic: Optional[
            pulumi.Input[DefaultRolloutSpecificationMediumTrafficArgs]
        ] = ...,
        provider_registration: Optional[
            pulumi.Input[DefaultRolloutSpecificationProviderRegistrationArgs]
        ] = ...,
        resource_type_registrations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceTypeRegistrationArgs]]]
        ] = ...,
        rest_of_the_world_group_one: Optional[
            pulumi.Input[DefaultRolloutSpecificationRestOfTheWorldGroupOneArgs]
        ] = ...,
        rest_of_the_world_group_two: Optional[
            pulumi.Input[DefaultRolloutSpecificationRestOfTheWorldGroupTwoArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisionConfig")
    def auto_provision_config(
        self,
    ) -> Optional[pulumi.Input[DefaultRolloutSpecificationAutoProvisionConfigArgs]]: ...
    @auto_provision_config.setter
    def auto_provision_config(
        self,
        value: Optional[
            pulumi.Input[DefaultRolloutSpecificationAutoProvisionConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def canary(
        self,
    ) -> Optional[pulumi.Input[DefaultRolloutSpecificationCanaryArgs]]: ...
    @canary.setter
    def canary(
        self, value: Optional[pulumi.Input[DefaultRolloutSpecificationCanaryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="expeditedRollout")
    def expedited_rollout(
        self,
    ) -> Optional[pulumi.Input[DefaultRolloutSpecificationExpeditedRolloutArgs]]: ...
    @expedited_rollout.setter
    def expedited_rollout(
        self,
        value: Optional[pulumi.Input[DefaultRolloutSpecificationExpeditedRolloutArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="highTraffic")
    def high_traffic(
        self,
    ) -> Optional[pulumi.Input[DefaultRolloutSpecificationHighTrafficArgs]]: ...
    @high_traffic.setter
    def high_traffic(
        self, value: Optional[pulumi.Input[DefaultRolloutSpecificationHighTrafficArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lowTraffic")
    def low_traffic(
        self,
    ) -> Optional[pulumi.Input[DefaultRolloutSpecificationLowTrafficArgs]]: ...
    @low_traffic.setter
    def low_traffic(
        self, value: Optional[pulumi.Input[DefaultRolloutSpecificationLowTrafficArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mediumTraffic")
    def medium_traffic(
        self,
    ) -> Optional[pulumi.Input[DefaultRolloutSpecificationMediumTrafficArgs]]: ...
    @medium_traffic.setter
    def medium_traffic(
        self,
        value: Optional[pulumi.Input[DefaultRolloutSpecificationMediumTrafficArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerRegistration")
    def provider_registration(
        self,
    ) -> Optional[
        pulumi.Input[DefaultRolloutSpecificationProviderRegistrationArgs]
    ]: ...
    @provider_registration.setter
    def provider_registration(
        self,
        value: Optional[
            pulumi.Input[DefaultRolloutSpecificationProviderRegistrationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeRegistrations")
    def resource_type_registrations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceTypeRegistrationArgs]]]
    ]: ...
    @resource_type_registrations.setter
    def resource_type_registrations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceTypeRegistrationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="restOfTheWorldGroupOne")
    def rest_of_the_world_group_one(
        self,
    ) -> Optional[
        pulumi.Input[DefaultRolloutSpecificationRestOfTheWorldGroupOneArgs]
    ]: ...
    @rest_of_the_world_group_one.setter
    def rest_of_the_world_group_one(
        self,
        value: Optional[
            pulumi.Input[DefaultRolloutSpecificationRestOfTheWorldGroupOneArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="restOfTheWorldGroupTwo")
    def rest_of_the_world_group_two(
        self,
    ) -> Optional[
        pulumi.Input[DefaultRolloutSpecificationRestOfTheWorldGroupTwoArgs]
    ]: ...
    @rest_of_the_world_group_two.setter
    def rest_of_the_world_group_two(
        self,
        value: Optional[
            pulumi.Input[DefaultRolloutSpecificationRestOfTheWorldGroupTwoArgs]
        ],
    ): ...

class DefaultRolloutPropertiesStatusArgsDict(TypedDict):
    completed_regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    failed_or_skipped_regions: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[ExtendedErrorInfoArgsDict]]]
    ]
    manifest_checkin_status: NotRequired[
        pulumi.Input[DefaultRolloutStatusManifestCheckinStatusArgsDict]
    ]
    next_traffic_region: NotRequired[
        pulumi.Input[Union[_builtins.str, TrafficRegionCategory]]
    ]
    next_traffic_region_scheduled_time: NotRequired[pulumi.Input[_builtins.str]]
    subscription_reregistration_result: NotRequired[
        pulumi.Input[Union[_builtins.str, SubscriptionReregistrationResult]]
    ]

@pulumi.input_type
class DefaultRolloutPropertiesStatusArgs:
    def __init__(
        __self__,
        *,
        completed_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        failed_or_skipped_regions: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ExtendedErrorInfoArgs]]]
        ] = ...,
        manifest_checkin_status: Optional[
            pulumi.Input[DefaultRolloutStatusManifestCheckinStatusArgs]
        ] = ...,
        next_traffic_region: Optional[
            pulumi.Input[Union[_builtins.str, TrafficRegionCategory]]
        ] = ...,
        next_traffic_region_scheduled_time: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_reregistration_result: Optional[
            pulumi.Input[Union[_builtins.str, SubscriptionReregistrationResult]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completedRegions")
    def completed_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @completed_regions.setter
    def completed_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="failedOrSkippedRegions")
    def failed_or_skipped_regions(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[ExtendedErrorInfoArgs]]]]: ...
    @failed_or_skipped_regions.setter
    def failed_or_skipped_regions(
        self,
        value: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[ExtendedErrorInfoArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manifestCheckinStatus")
    def manifest_checkin_status(
        self,
    ) -> Optional[pulumi.Input[DefaultRolloutStatusManifestCheckinStatusArgs]]: ...
    @manifest_checkin_status.setter
    def manifest_checkin_status(
        self,
        value: Optional[pulumi.Input[DefaultRolloutStatusManifestCheckinStatusArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nextTrafficRegion")
    def next_traffic_region(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TrafficRegionCategory]]]: ...
    @next_traffic_region.setter
    def next_traffic_region(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TrafficRegionCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nextTrafficRegionScheduledTime")
    def next_traffic_region_scheduled_time(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @next_traffic_region_scheduled_time.setter
    def next_traffic_region_scheduled_time(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionReregistrationResult")
    def subscription_reregistration_result(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, SubscriptionReregistrationResult]]
    ]: ...
    @subscription_reregistration_result.setter
    def subscription_reregistration_result(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, SubscriptionReregistrationResult]]
        ],
    ): ...

class DefaultRolloutPropertiesArgsDict(TypedDict):
    specification: NotRequired[
        pulumi.Input[DefaultRolloutPropertiesSpecificationArgsDict]
    ]
    status: NotRequired[pulumi.Input[DefaultRolloutPropertiesStatusArgsDict]]

@pulumi.input_type
class DefaultRolloutPropertiesArgs:
    def __init__(
        __self__,
        *,
        specification: Optional[
            pulumi.Input[DefaultRolloutPropertiesSpecificationArgs]
        ] = ...,
        status: Optional[pulumi.Input[DefaultRolloutPropertiesStatusArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def specification(
        self,
    ) -> Optional[pulumi.Input[DefaultRolloutPropertiesSpecificationArgs]]: ...
    @specification.setter
    def specification(
        self, value: Optional[pulumi.Input[DefaultRolloutPropertiesSpecificationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[DefaultRolloutPropertiesStatusArgs]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[DefaultRolloutPropertiesStatusArgs]]
    ): ...

class DefaultRolloutSpecificationAutoProvisionConfigArgsDict(TypedDict):
    resource_graph: NotRequired[pulumi.Input[_builtins.bool]]
    storage: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DefaultRolloutSpecificationAutoProvisionConfigArgs:
    def __init__(
        __self__,
        *,
        resource_graph: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGraph")
    def resource_graph(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @resource_graph.setter
    def resource_graph(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @storage.setter
    def storage(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DefaultRolloutSpecificationCanaryArgsDict(TypedDict):
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    skip_regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DefaultRolloutSpecificationCanaryArgs:
    def __init__(
        __self__,
        *,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        skip_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipRegions")
    def skip_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @skip_regions.setter
    def skip_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DefaultRolloutSpecificationExpeditedRolloutArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DefaultRolloutSpecificationExpeditedRolloutArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DefaultRolloutSpecificationHighTrafficArgsDict(TypedDict):
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    wait_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DefaultRolloutSpecificationHighTrafficArgs:
    def __init__(
        __self__,
        *,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        wait_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_duration.setter
    def wait_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DefaultRolloutSpecificationLowTrafficArgsDict(TypedDict):
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    wait_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DefaultRolloutSpecificationLowTrafficArgs:
    def __init__(
        __self__,
        *,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        wait_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_duration.setter
    def wait_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DefaultRolloutSpecificationMediumTrafficArgsDict(TypedDict):
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    wait_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DefaultRolloutSpecificationMediumTrafficArgs:
    def __init__(
        __self__,
        *,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        wait_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_duration.setter
    def wait_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DefaultRolloutSpecificationProviderRegistrationArgsDict(TypedDict):
    kind: NotRequired[pulumi.Input[Union[_builtins.str, ProviderRegistrationKind]]]
    properties: NotRequired[pulumi.Input[ProviderRegistrationPropertiesArgsDict]]

@pulumi.input_type
class DefaultRolloutSpecificationProviderRegistrationArgs:
    def __init__(
        __self__,
        *,
        kind: Optional[
            pulumi.Input[Union[_builtins.str, ProviderRegistrationKind]]
        ] = ...,
        properties: Optional[pulumi.Input[ProviderRegistrationPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ProviderRegistrationKind]]]: ...
    @kind.setter
    def kind(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ProviderRegistrationKind]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[ProviderRegistrationPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[ProviderRegistrationPropertiesArgs]]
    ): ...

class DefaultRolloutSpecificationRestOfTheWorldGroupOneArgsDict(TypedDict):
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    wait_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DefaultRolloutSpecificationRestOfTheWorldGroupOneArgs:
    def __init__(
        __self__,
        *,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        wait_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_duration.setter
    def wait_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DefaultRolloutSpecificationRestOfTheWorldGroupTwoArgsDict(TypedDict):
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    wait_duration: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DefaultRolloutSpecificationRestOfTheWorldGroupTwoArgs:
    def __init__(
        __self__,
        *,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        wait_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_duration.setter
    def wait_duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DefaultRolloutStatusManifestCheckinStatusArgsDict(TypedDict):
    is_checked_in: pulumi.Input[_builtins.bool]
    status_message: pulumi.Input[_builtins.str]
    commit_id: NotRequired[pulumi.Input[_builtins.str]]
    pull_request: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DefaultRolloutStatusManifestCheckinStatusArgs:
    def __init__(
        __self__,
        *,
        is_checked_in: pulumi.Input[_builtins.bool],
        status_message: pulumi.Input[_builtins.str],
        commit_id: Optional[pulumi.Input[_builtins.str]] = ...,
        pull_request: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCheckedIn")
    def is_checked_in(self) -> pulumi.Input[_builtins.bool]: ...
    @is_checked_in.setter
    def is_checked_in(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Input[_builtins.str]: ...
    @status_message.setter
    def status_message(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="commitId")
    def commit_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commit_id.setter
    def commit_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pull_request.setter
    def pull_request(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeleteDependencyArgsDict(TypedDict):
    linked_property: NotRequired[pulumi.Input[_builtins.str]]
    linked_type: NotRequired[pulumi.Input[_builtins.str]]
    required_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DeleteDependencyArgs:
    def __init__(
        __self__,
        *,
        linked_property: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_type: Optional[pulumi.Input[_builtins.str]] = ...,
        required_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedProperty")
    def linked_property(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_property.setter
    def linked_property(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedType")
    def linked_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_type.setter
    def linked_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_features.setter
    def required_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class EndpointInformationArgsDict(TypedDict):
    endpoint: NotRequired[pulumi.Input[_builtins.str]]
    endpoint_type: NotRequired[
        pulumi.Input[Union[_builtins.str, NotificationEndpointType]]
    ]
    schema_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EndpointInformationArgs:
    def __init__(
        __self__,
        *,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_type: Optional[
            pulumi.Input[Union[_builtins.str, NotificationEndpointType]]
        ] = ...,
        schema_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NotificationEndpointType]]]: ...
    @endpoint_type.setter
    def endpoint_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, NotificationEndpointType]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_version.setter
    def schema_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExtendedErrorInfoArgsDict(TypedDict):
    additional_info: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TypedErrorInfoArgsDict]]]
    ]
    code: NotRequired[pulumi.Input[_builtins.str]]
    details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ExtendedErrorInfoArgsDict]]]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ExtendedErrorInfoArgs:
    def __init__(
        __self__,
        *,
        additional_info: Optional[
            pulumi.Input[Sequence[pulumi.Input[TypedErrorInfoArgs]]]
        ] = ...,
        code: Optional[pulumi.Input[_builtins.str]] = ...,
        details: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExtendedErrorInfoArgs]]]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TypedErrorInfoArgs]]]]: ...
    @additional_info.setter
    def additional_info(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TypedErrorInfoArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExtendedErrorInfoArgs]]]]: ...
    @details.setter
    def details(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ExtendedErrorInfoArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExtendedLocationOptionsArgsDict(TypedDict):
    supported_policy: NotRequired[
        pulumi.Input[Union[_builtins.str, ResourceTypeExtendedLocationPolicy]]
    ]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]]

@pulumi.input_type
class ExtendedLocationOptionsArgs:
    def __init__(
        __self__,
        *,
        supported_policy: Optional[
            pulumi.Input[Union[_builtins.str, ResourceTypeExtendedLocationPolicy]]
        ] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportedPolicy")
    def supported_policy(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ResourceTypeExtendedLocationPolicy]]
    ]: ...
    @supported_policy.setter
    def supported_policy(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ResourceTypeExtendedLocationPolicy]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]]
    ): ...

class FanoutLinkedNotificationRuleDstsConfigurationArgsDict(TypedDict):
    service_name: pulumi.Input[_builtins.str]
    service_dns_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FanoutLinkedNotificationRuleDstsConfigurationArgs:
    def __init__(
        __self__,
        *,
        service_name: pulumi.Input[_builtins.str],
        service_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_dns_name.setter
    def service_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FanoutLinkedNotificationRuleArgsDict(TypedDict):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    dsts_configuration: NotRequired[
        pulumi.Input[FanoutLinkedNotificationRuleDstsConfigurationArgsDict]
    ]
    endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgsDict]]]
    ]
    token_auth_configuration: NotRequired[pulumi.Input[TokenAuthConfigurationArgsDict]]

@pulumi.input_type
class FanoutLinkedNotificationRuleArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        dsts_configuration: Optional[
            pulumi.Input[FanoutLinkedNotificationRuleDstsConfigurationArgs]
        ] = ...,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgs]]]
        ] = ...,
        token_auth_configuration: Optional[
            pulumi.Input[TokenAuthConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dstsConfiguration")
    def dsts_configuration(
        self,
    ) -> Optional[pulumi.Input[FanoutLinkedNotificationRuleDstsConfigurationArgs]]: ...
    @dsts_configuration.setter
    def dsts_configuration(
        self,
        value: Optional[
            pulumi.Input[FanoutLinkedNotificationRuleDstsConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgs]]]
    ]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenAuthConfiguration")
    def token_auth_configuration(
        self,
    ) -> Optional[pulumi.Input[TokenAuthConfigurationArgs]]: ...
    @token_auth_configuration.setter
    def token_auth_configuration(
        self, value: Optional[pulumi.Input[TokenAuthConfigurationArgs]]
    ): ...

class FilterRuleArgsDict(TypedDict):
    endpoint_information: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EndpointInformationArgsDict]]]
    ]
    filter_query: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FilterRuleArgs:
    def __init__(
        __self__,
        *,
        endpoint_information: Optional[
            pulumi.Input[Sequence[pulumi.Input[EndpointInformationArgs]]]
        ] = ...,
        filter_query: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointInformation")
    def endpoint_information(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointInformationArgs]]]]: ...
    @endpoint_information.setter
    def endpoint_information(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointInformationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterQuery")
    def filter_query(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter_query.setter
    def filter_query(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LegacyDisallowedConditionArgsDict(TypedDict):
    disallowed_legacy_operations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LegacyOperation]]]]
    ]
    feature: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LegacyDisallowedConditionArgs:
    def __init__(
        __self__,
        *,
        disallowed_legacy_operations: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LegacyOperation]]]]
        ] = ...,
        feature: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disallowedLegacyOperations")
    def disallowed_legacy_operations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LegacyOperation]]]]
    ]: ...
    @disallowed_legacy_operations.setter
    def disallowed_legacy_operations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LegacyOperation]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def feature(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @feature.setter
    def feature(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LightHouseAuthorizationArgsDict(TypedDict):
    principal_id: pulumi.Input[_builtins.str]
    role_definition_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class LightHouseAuthorizationArgs:
    def __init__(
        __self__,
        *,
        principal_id: pulumi.Input[_builtins.str],
        role_definition_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[_builtins.str]: ...
    @principal_id.setter
    def principal_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> pulumi.Input[_builtins.str]: ...
    @role_definition_id.setter
    def role_definition_id(self, value: pulumi.Input[_builtins.str]): ...

class LinkedAccessCheckArgsDict(TypedDict):
    action_name: NotRequired[pulumi.Input[_builtins.str]]
    linked_action: NotRequired[pulumi.Input[_builtins.str]]
    linked_action_verb: NotRequired[pulumi.Input[_builtins.str]]
    linked_property: NotRequired[pulumi.Input[_builtins.str]]
    linked_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LinkedAccessCheckArgs:
    def __init__(
        __self__,
        *,
        action_name: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_action: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_action_verb: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_property: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_name.setter
    def action_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedAction")
    def linked_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_action.setter
    def linked_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedActionVerb")
    def linked_action_verb(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_action_verb.setter
    def linked_action_verb(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedProperty")
    def linked_property(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_property.setter
    def linked_property(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedType")
    def linked_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_type.setter
    def linked_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LinkedNotificationRuleArgsDict(TypedDict):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    actions_on_failed_operation: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    fast_path_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    fast_path_actions_on_failed_operation: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    linked_notification_timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LinkedNotificationRuleArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        actions_on_failed_operation: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        fast_path_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        fast_path_actions_on_failed_operation: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        linked_notification_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="actionsOnFailedOperation")
    def actions_on_failed_operation(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions_on_failed_operation.setter
    def actions_on_failed_operation(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fastPathActions")
    def fast_path_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @fast_path_actions.setter
    def fast_path_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fastPathActionsOnFailedOperation")
    def fast_path_actions_on_failed_operation(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @fast_path_actions_on_failed_operation.setter
    def fast_path_actions_on_failed_operation(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedNotificationTimeout")
    def linked_notification_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_notification_timeout.setter
    def linked_notification_timeout(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class LinkedOperationRuleArgsDict(TypedDict):
    linked_action: pulumi.Input[Union[_builtins.str, LinkedAction]]
    linked_operation: pulumi.Input[Union[_builtins.str, LinkedOperation]]
    depends_on_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class LinkedOperationRuleArgs:
    def __init__(
        __self__,
        *,
        linked_action: pulumi.Input[Union[_builtins.str, LinkedAction]],
        linked_operation: pulumi.Input[Union[_builtins.str, LinkedOperation]],
        depends_on_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedAction")
    def linked_action(self) -> pulumi.Input[Union[_builtins.str, LinkedAction]]: ...
    @linked_action.setter
    def linked_action(
        self, value: pulumi.Input[Union[_builtins.str, LinkedAction]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedOperation")
    def linked_operation(
        self,
    ) -> pulumi.Input[Union[_builtins.str, LinkedOperation]]: ...
    @linked_operation.setter
    def linked_operation(
        self, value: pulumi.Input[Union[_builtins.str, LinkedOperation]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOnTypes")
    def depends_on_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @depends_on_types.setter
    def depends_on_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class LocationQuotaRuleArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    policy: NotRequired[pulumi.Input[Union[_builtins.str, QuotaPolicy]]]
    quota_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LocationQuotaRuleArgs:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[Union[_builtins.str, QuotaPolicy]]] = ...,
        quota_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[Union[_builtins.str, QuotaPolicy]]]: ...
    @policy.setter
    def policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, QuotaPolicy]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @quota_id.setter
    def quota_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LoggingRuleHiddenPropertyPathsArgsDict(TypedDict):
    hidden_paths_on_request: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    hidden_paths_on_response: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class LoggingRuleHiddenPropertyPathsArgs:
    def __init__(
        __self__,
        *,
        hidden_paths_on_request: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        hidden_paths_on_response: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hiddenPathsOnRequest")
    def hidden_paths_on_request(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @hidden_paths_on_request.setter
    def hidden_paths_on_request(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hiddenPathsOnResponse")
    def hidden_paths_on_response(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @hidden_paths_on_response.setter
    def hidden_paths_on_response(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class LoggingRuleArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    detail_level: pulumi.Input[Union[_builtins.str, LoggingDetails]]
    direction: pulumi.Input[Union[_builtins.str, LoggingDirections]]
    hidden_property_paths: NotRequired[
        pulumi.Input[LoggingRuleHiddenPropertyPathsArgsDict]
    ]

@pulumi.input_type
class LoggingRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        detail_level: pulumi.Input[Union[_builtins.str, LoggingDetails]],
        direction: pulumi.Input[Union[_builtins.str, LoggingDirections]],
        hidden_property_paths: Optional[
            pulumi.Input[LoggingRuleHiddenPropertyPathsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="detailLevel")
    def detail_level(self) -> pulumi.Input[Union[_builtins.str, LoggingDetails]]: ...
    @detail_level.setter
    def detail_level(
        self, value: pulumi.Input[Union[_builtins.str, LoggingDetails]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> pulumi.Input[Union[_builtins.str, LoggingDirections]]: ...
    @direction.setter
    def direction(
        self, value: pulumi.Input[Union[_builtins.str, LoggingDirections]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hiddenPropertyPaths")
    def hidden_property_paths(
        self,
    ) -> Optional[pulumi.Input[LoggingRuleHiddenPropertyPathsArgs]]: ...
    @hidden_property_paths.setter
    def hidden_property_paths(
        self, value: Optional[pulumi.Input[LoggingRuleHiddenPropertyPathsArgs]]
    ): ...

class NotificationEndpointArgsDict(TypedDict):
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    notification_destination: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class NotificationEndpointArgs:
    def __init__(
        __self__,
        *,
        locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        notification_destination: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @locations.setter
    def locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationDestination")
    def notification_destination(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @notification_destination.setter
    def notification_destination(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class NotificationRegistrationPropertiesArgsDict(TypedDict):
    included_events: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    message_scope: NotRequired[pulumi.Input[Union[_builtins.str, MessageScope]]]
    notification_endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NotificationEndpointArgsDict]]]
    ]
    notification_mode: NotRequired[pulumi.Input[Union[_builtins.str, NotificationMode]]]

@pulumi.input_type
class NotificationRegistrationPropertiesArgs:
    def __init__(
        __self__,
        *,
        included_events: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        message_scope: Optional[pulumi.Input[Union[_builtins.str, MessageScope]]] = ...,
        notification_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[NotificationEndpointArgs]]]
        ] = ...,
        notification_mode: Optional[
            pulumi.Input[Union[_builtins.str, NotificationMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedEvents")
    def included_events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_events.setter
    def included_events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="messageScope")
    def message_scope(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MessageScope]]]: ...
    @message_scope.setter
    def message_scope(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MessageScope]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationEndpoints")
    def notification_endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NotificationEndpointArgs]]]]: ...
    @notification_endpoints.setter
    def notification_endpoints(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[NotificationEndpointArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationMode")
    def notification_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NotificationMode]]]: ...
    @notification_mode.setter
    def notification_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NotificationMode]]]
    ): ...

class NotificationArgsDict(TypedDict):
    notification_type: NotRequired[pulumi.Input[Union[_builtins.str, NotificationType]]]
    skip_notifications: NotRequired[
        pulumi.Input[Union[_builtins.str, SkipNotifications]]
    ]

@pulumi.input_type
class NotificationArgs:
    def __init__(
        __self__,
        *,
        notification_type: Optional[
            pulumi.Input[Union[_builtins.str, NotificationType]]
        ] = ...,
        skip_notifications: Optional[
            pulumi.Input[Union[_builtins.str, SkipNotifications]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NotificationType]]]: ...
    @notification_type.setter
    def notification_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NotificationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipNotifications")
    def skip_notifications(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SkipNotifications]]]: ...
    @skip_notifications.setter
    def skip_notifications(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SkipNotifications]]]
    ): ...

class OpenApiConfigurationArgsDict(TypedDict):
    validation: NotRequired[pulumi.Input[OpenApiValidationArgsDict]]

@pulumi.input_type
class OpenApiConfigurationArgs:
    def __init__(
        __self__, *, validation: Optional[pulumi.Input[OpenApiValidationArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[pulumi.Input[OpenApiValidationArgs]]: ...
    @validation.setter
    def validation(self, value: Optional[pulumi.Input[OpenApiValidationArgs]]): ...

class OpenApiValidationArgsDict(TypedDict):
    allow_noncompliant_collection_response: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class OpenApiValidationArgs:
    def __init__(
        __self__,
        *,
        allow_noncompliant_collection_response: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowNoncompliantCollectionResponse")
    def allow_noncompliant_collection_response(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_noncompliant_collection_response.setter
    def allow_noncompliant_collection_response(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ProviderHubMetadataProviderAuthenticationArgsDict(TypedDict):
    allowed_audiences: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ProviderHubMetadataProviderAuthenticationArgs:
    def __init__(
        __self__,
        *,
        allowed_audiences: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_audiences.setter
    def allowed_audiences(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ProviderHubMetadataThirdPartyProviderAuthorizationArgsDict(TypedDict):
    authorizations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LightHouseAuthorizationArgsDict]]]
    ]
    managed_by_tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProviderHubMetadataThirdPartyProviderAuthorizationArgs:
    def __init__(
        __self__,
        *,
        authorizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[LightHouseAuthorizationArgs]]]
        ] = ...,
        managed_by_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorizations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LightHouseAuthorizationArgs]]]
    ]: ...
    @authorizations.setter
    def authorizations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LightHouseAuthorizationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedByTenantId")
    def managed_by_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by_tenant_id.setter
    def managed_by_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProviderRegistrationPropertiesPrivateResourceProviderConfigurationArgsDict(
    TypedDict
):
    allowed_subscriptions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ProviderRegistrationPropertiesPrivateResourceProviderConfigurationArgs:
    def __init__(
        __self__,
        *,
        allowed_subscriptions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSubscriptions")
    def allowed_subscriptions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_subscriptions.setter
    def allowed_subscriptions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ProviderRegistrationPropertiesProviderHubMetadataArgsDict(TypedDict):
    direct_rp_role_definition_id: NotRequired[pulumi.Input[_builtins.str]]
    global_async_operation_resource_type_name: NotRequired[pulumi.Input[_builtins.str]]
    provider_authentication: NotRequired[
        pulumi.Input[ProviderHubMetadataProviderAuthenticationArgsDict]
    ]
    provider_authorizations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderAuthorizationArgsDict]]]
    ]
    regional_async_operation_resource_type_name: NotRequired[
        pulumi.Input[_builtins.str]
    ]
    third_party_provider_authorization: NotRequired[
        pulumi.Input[ProviderHubMetadataThirdPartyProviderAuthorizationArgsDict]
    ]

@pulumi.input_type
class ProviderRegistrationPropertiesProviderHubMetadataArgs:
    def __init__(
        __self__,
        *,
        direct_rp_role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        global_async_operation_resource_type_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        provider_authentication: Optional[
            pulumi.Input[ProviderHubMetadataProviderAuthenticationArgs]
        ] = ...,
        provider_authorizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderAuthorizationArgs]]]
        ] = ...,
        regional_async_operation_resource_type_name: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        third_party_provider_authorization: Optional[
            pulumi.Input[ProviderHubMetadataThirdPartyProviderAuthorizationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directRpRoleDefinitionId")
    def direct_rp_role_definition_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @direct_rp_role_definition_id.setter
    def direct_rp_role_definition_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalAsyncOperationResourceTypeName")
    def global_async_operation_resource_type_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_async_operation_resource_type_name.setter
    def global_async_operation_resource_type_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerAuthentication")
    def provider_authentication(
        self,
    ) -> Optional[pulumi.Input[ProviderHubMetadataProviderAuthenticationArgs]]: ...
    @provider_authentication.setter
    def provider_authentication(
        self,
        value: Optional[pulumi.Input[ProviderHubMetadataProviderAuthenticationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerAuthorizations")
    def provider_authorizations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderAuthorizationArgs]]]
    ]: ...
    @provider_authorizations.setter
    def provider_authorizations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderAuthorizationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="regionalAsyncOperationResourceTypeName")
    def regional_async_operation_resource_type_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regional_async_operation_resource_type_name.setter
    def regional_async_operation_resource_type_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="thirdPartyProviderAuthorization")
    def third_party_provider_authorization(
        self,
    ) -> Optional[
        pulumi.Input[ProviderHubMetadataThirdPartyProviderAuthorizationArgs]
    ]: ...
    @third_party_provider_authorization.setter
    def third_party_provider_authorization(
        self,
        value: Optional[
            pulumi.Input[ProviderHubMetadataThirdPartyProviderAuthorizationArgs]
        ],
    ): ...

class ProviderRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgsDict(
    TypedDict
):
    soft_delete_ttl: NotRequired[pulumi.Input[_builtins.str]]
    subscription_state_override_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubscriptionStateOverrideActionArgsDict]]]
    ]

@pulumi.input_type
class ProviderRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgs:
    def __init__(
        __self__,
        *,
        soft_delete_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_state_override_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionStateOverrideActionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="softDeleteTTL")
    def soft_delete_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @soft_delete_ttl.setter
    def soft_delete_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionStateOverrideActions")
    def subscription_state_override_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SubscriptionStateOverrideActionArgs]]]
    ]: ...
    @subscription_state_override_actions.setter
    def subscription_state_override_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionStateOverrideActionArgs]]]
        ],
    ): ...

class ProviderRegistrationPropertiesArgsDict(TypedDict):
    capabilities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderCapabilitiesArgsDict]]]
    ]
    cross_tenant_token_validation: NotRequired[
        pulumi.Input[Union[_builtins.str, CrossTenantTokenValidation]]
    ]
    custom_manifest_version: NotRequired[pulumi.Input[_builtins.str]]
    dsts_configuration: NotRequired[
        pulumi.Input[ResourceProviderManifestPropertiesDstsConfigurationArgsDict]
    ]
    enable_tenant_linked_notification: NotRequired[pulumi.Input[_builtins.bool]]
    features_rule: NotRequired[
        pulumi.Input[ResourceProviderManifestPropertiesFeaturesRuleArgsDict]
    ]
    global_notification_endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgsDict]]]
    ]
    legacy_namespace: NotRequired[pulumi.Input[_builtins.str]]
    legacy_registrations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    linked_notification_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FanoutLinkedNotificationRuleArgsDict]]]
    ]
    management: NotRequired[
        pulumi.Input[ResourceProviderManifestPropertiesManagementArgsDict]
    ]
    management_group_global_notification_endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgsDict]]]
    ]
    metadata: NotRequired[Any]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    notification_options: NotRequired[
        pulumi.Input[Union[_builtins.str, NotificationOptions]]
    ]
    notification_settings: NotRequired[
        pulumi.Input[ResourceProviderManifestPropertiesNotificationSettingsArgsDict]
    ]
    notifications: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NotificationArgsDict]]]
    ]
    optional_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    private_resource_provider_configuration: NotRequired[
        pulumi.Input[
            ProviderRegistrationPropertiesPrivateResourceProviderConfigurationArgsDict
        ]
    ]
    provider_authentication: NotRequired[
        pulumi.Input[ResourceProviderManifestPropertiesProviderAuthenticationArgsDict]
    ]
    provider_authorizations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderAuthorizationArgsDict]]]
    ]
    provider_hub_metadata: NotRequired[
        pulumi.Input[ProviderRegistrationPropertiesProviderHubMetadataArgsDict]
    ]
    provider_type: NotRequired[pulumi.Input[Union[_builtins.str, ResourceProviderType]]]
    provider_version: NotRequired[pulumi.Input[_builtins.str]]
    request_header_options: NotRequired[
        pulumi.Input[ResourceProviderManifestPropertiesRequestHeaderOptionsArgsDict]
    ]
    required_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_group_lock_option_during_move: NotRequired[
        pulumi.Input[
            ResourceProviderManifestPropertiesResourceGroupLockOptionDuringMoveArgsDict
        ]
    ]
    resource_hydration_accounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceHydrationAccountArgsDict]]]
    ]
    resource_provider_authorization_rules: NotRequired[
        pulumi.Input[ResourceProviderAuthorizationRulesArgsDict]
    ]
    response_options: NotRequired[
        pulumi.Input[ResourceProviderManifestPropertiesResponseOptionsArgsDict]
    ]
    service_name: NotRequired[pulumi.Input[_builtins.str]]
    services: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderServiceArgsDict]]]
    ]
    subscription_lifecycle_notification_specifications: NotRequired[
        pulumi.Input[
            ProviderRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgsDict
        ]
    ]
    template_deployment_options: NotRequired[
        pulumi.Input[
            ResourceProviderManifestPropertiesTemplateDeploymentOptionsArgsDict
        ]
    ]
    token_auth_configuration: NotRequired[pulumi.Input[TokenAuthConfigurationArgsDict]]

@pulumi.input_type
class ProviderRegistrationPropertiesArgs:
    def __init__(
        __self__,
        *,
        capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderCapabilitiesArgs]]]
        ] = ...,
        cross_tenant_token_validation: Optional[
            pulumi.Input[Union[_builtins.str, CrossTenantTokenValidation]]
        ] = ...,
        custom_manifest_version: Optional[pulumi.Input[_builtins.str]] = ...,
        dsts_configuration: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesDstsConfigurationArgs]
        ] = ...,
        enable_tenant_linked_notification: Optional[pulumi.Input[_builtins.bool]] = ...,
        features_rule: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesFeaturesRuleArgs]
        ] = ...,
        global_notification_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgs]]]
        ] = ...,
        legacy_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        legacy_registrations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        linked_notification_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[FanoutLinkedNotificationRuleArgs]]]
        ] = ...,
        management: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesManagementArgs]
        ] = ...,
        management_group_global_notification_endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgs]]]
        ] = ...,
        metadata: Optional[Any] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_options: Optional[
            pulumi.Input[Union[_builtins.str, NotificationOptions]]
        ] = ...,
        notification_settings: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesNotificationSettingsArgs]
        ] = ...,
        notifications: Optional[
            pulumi.Input[Sequence[pulumi.Input[NotificationArgs]]]
        ] = ...,
        optional_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        private_resource_provider_configuration: Optional[
            pulumi.Input[
                ProviderRegistrationPropertiesPrivateResourceProviderConfigurationArgs
            ]
        ] = ...,
        provider_authentication: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesProviderAuthenticationArgs]
        ] = ...,
        provider_authorizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderAuthorizationArgs]]]
        ] = ...,
        provider_hub_metadata: Optional[
            pulumi.Input[ProviderRegistrationPropertiesProviderHubMetadataArgs]
        ] = ...,
        provider_type: Optional[
            pulumi.Input[Union[_builtins.str, ResourceProviderType]]
        ] = ...,
        provider_version: Optional[pulumi.Input[_builtins.str]] = ...,
        request_header_options: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesRequestHeaderOptionsArgs]
        ] = ...,
        required_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_group_lock_option_during_move: Optional[
            pulumi.Input[
                ResourceProviderManifestPropertiesResourceGroupLockOptionDuringMoveArgs
            ]
        ] = ...,
        resource_hydration_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceHydrationAccountArgs]]]
        ] = ...,
        resource_provider_authorization_rules: Optional[
            pulumi.Input[ResourceProviderAuthorizationRulesArgs]
        ] = ...,
        response_options: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesResponseOptionsArgs]
        ] = ...,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        services: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderServiceArgs]]]
        ] = ...,
        subscription_lifecycle_notification_specifications: Optional[
            pulumi.Input[
                ProviderRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgs
            ]
        ] = ...,
        template_deployment_options: Optional[
            pulumi.Input[
                ResourceProviderManifestPropertiesTemplateDeploymentOptionsArgs
            ]
        ] = ...,
        token_auth_configuration: Optional[
            pulumi.Input[TokenAuthConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderCapabilitiesArgs]]]
    ]: ...
    @capabilities.setter
    def capabilities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderCapabilitiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="crossTenantTokenValidation")
    def cross_tenant_token_validation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CrossTenantTokenValidation]]]: ...
    @cross_tenant_token_validation.setter
    def cross_tenant_token_validation(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, CrossTenantTokenValidation]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customManifestVersion")
    def custom_manifest_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_manifest_version.setter
    def custom_manifest_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dstsConfiguration")
    def dsts_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManifestPropertiesDstsConfigurationArgs]
    ]: ...
    @dsts_configuration.setter
    def dsts_configuration(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesDstsConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableTenantLinkedNotification")
    def enable_tenant_linked_notification(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_tenant_linked_notification.setter
    def enable_tenant_linked_notification(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="featuresRule")
    def features_rule(
        self,
    ) -> Optional[pulumi.Input[ResourceProviderManifestPropertiesFeaturesRuleArgs]]: ...
    @features_rule.setter
    def features_rule(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesFeaturesRuleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalNotificationEndpoints")
    def global_notification_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgs]]]
    ]: ...
    @global_notification_endpoints.setter
    def global_notification_endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="legacyNamespace")
    def legacy_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @legacy_namespace.setter
    def legacy_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="legacyRegistrations")
    def legacy_registrations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @legacy_registrations.setter
    def legacy_registrations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedNotificationRules")
    def linked_notification_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FanoutLinkedNotificationRuleArgs]]]
    ]: ...
    @linked_notification_rules.setter
    def linked_notification_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FanoutLinkedNotificationRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def management(
        self,
    ) -> Optional[pulumi.Input[ResourceProviderManifestPropertiesManagementArgs]]: ...
    @management.setter
    def management(
        self,
        value: Optional[pulumi.Input[ResourceProviderManifestPropertiesManagementArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managementGroupGlobalNotificationEndpoints")
    def management_group_global_notification_endpoints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgs]]]
    ]: ...
    @management_group_global_notification_endpoints.setter
    def management_group_global_notification_endpoints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderEndpointArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @metadata.setter
    def metadata(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationOptions")
    def notification_options(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NotificationOptions]]]: ...
    @notification_options.setter
    def notification_options(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NotificationOptions]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManifestPropertiesNotificationSettingsArgs]
    ]: ...
    @notification_settings.setter
    def notification_settings(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesNotificationSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def notifications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NotificationArgs]]]]: ...
    @notifications.setter
    def notifications(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NotificationArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="optionalFeatures")
    def optional_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @optional_features.setter
    def optional_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateResourceProviderConfiguration")
    def private_resource_provider_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            ProviderRegistrationPropertiesPrivateResourceProviderConfigurationArgs
        ]
    ]: ...
    @private_resource_provider_configuration.setter
    def private_resource_provider_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ProviderRegistrationPropertiesPrivateResourceProviderConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerAuthentication")
    def provider_authentication(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManifestPropertiesProviderAuthenticationArgs]
    ]: ...
    @provider_authentication.setter
    def provider_authentication(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesProviderAuthenticationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerAuthorizations")
    def provider_authorizations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderAuthorizationArgs]]]
    ]: ...
    @provider_authorizations.setter
    def provider_authorizations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderAuthorizationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerHubMetadata")
    def provider_hub_metadata(
        self,
    ) -> Optional[
        pulumi.Input[ProviderRegistrationPropertiesProviderHubMetadataArgs]
    ]: ...
    @provider_hub_metadata.setter
    def provider_hub_metadata(
        self,
        value: Optional[
            pulumi.Input[ProviderRegistrationPropertiesProviderHubMetadataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceProviderType]]]: ...
    @provider_type.setter
    def provider_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceProviderType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="providerVersion")
    def provider_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_version.setter
    def provider_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderOptions")
    def request_header_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManifestPropertiesRequestHeaderOptionsArgs]
    ]: ...
    @request_header_options.setter
    def request_header_options(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesRequestHeaderOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_features.setter
    def required_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupLockOptionDuringMove")
    def resource_group_lock_option_during_move(
        self,
    ) -> Optional[
        pulumi.Input[
            ResourceProviderManifestPropertiesResourceGroupLockOptionDuringMoveArgs
        ]
    ]: ...
    @resource_group_lock_option_during_move.setter
    def resource_group_lock_option_during_move(
        self,
        value: Optional[
            pulumi.Input[
                ResourceProviderManifestPropertiesResourceGroupLockOptionDuringMoveArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceHydrationAccounts")
    def resource_hydration_accounts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceHydrationAccountArgs]]]
    ]: ...
    @resource_hydration_accounts.setter
    def resource_hydration_accounts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceHydrationAccountArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderAuthorizationRules")
    def resource_provider_authorization_rules(
        self,
    ) -> Optional[pulumi.Input[ResourceProviderAuthorizationRulesArgs]]: ...
    @resource_provider_authorization_rules.setter
    def resource_provider_authorization_rules(
        self, value: Optional[pulumi.Input[ResourceProviderAuthorizationRulesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="responseOptions")
    def response_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManifestPropertiesResponseOptionsArgs]
    ]: ...
    @response_options.setter
    def response_options(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManifestPropertiesResponseOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ResourceProviderServiceArgs]]]
    ]: ...
    @services.setter
    def services(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceProviderServiceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionLifecycleNotificationSpecifications")
    def subscription_lifecycle_notification_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            ProviderRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgs
        ]
    ]: ...
    @subscription_lifecycle_notification_specifications.setter
    def subscription_lifecycle_notification_specifications(
        self,
        value: Optional[
            pulumi.Input[
                ProviderRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateDeploymentOptions")
    def template_deployment_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManifestPropertiesTemplateDeploymentOptionsArgs]
    ]: ...
    @template_deployment_options.setter
    def template_deployment_options(
        self,
        value: Optional[
            pulumi.Input[
                ResourceProviderManifestPropertiesTemplateDeploymentOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenAuthConfiguration")
    def token_auth_configuration(
        self,
    ) -> Optional[pulumi.Input[TokenAuthConfigurationArgs]]: ...
    @token_auth_configuration.setter
    def token_auth_configuration(
        self, value: Optional[pulumi.Input[TokenAuthConfigurationArgs]]
    ): ...

class QuotaRuleArgsDict(TypedDict):
    location_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LocationQuotaRuleArgsDict]]]
    ]
    quota_policy: NotRequired[pulumi.Input[Union[_builtins.str, QuotaPolicy]]]
    required_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class QuotaRuleArgs:
    def __init__(
        __self__,
        *,
        location_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[LocationQuotaRuleArgs]]]
        ] = ...,
        quota_policy: Optional[pulumi.Input[Union[_builtins.str, QuotaPolicy]]] = ...,
        required_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationRules")
    def location_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LocationQuotaRuleArgs]]]]: ...
    @location_rules.setter
    def location_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LocationQuotaRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="quotaPolicy")
    def quota_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, QuotaPolicy]]]: ...
    @quota_policy.setter
    def quota_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, QuotaPolicy]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_features.setter
    def required_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ResourceAccessRoleArgsDict(TypedDict):
    actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    allowed_group_claims: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ResourceAccessRoleArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        allowed_group_claims: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @actions.setter
    def actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedGroupClaims")
    def allowed_group_claims(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_group_claims.setter
    def allowed_group_claims(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ResourceConcurrencyControlOptionArgsDict(TypedDict):
    policy: NotRequired[pulumi.Input[Union[_builtins.str, Policy]]]

@pulumi.input_type
class ResourceConcurrencyControlOptionArgs:
    def __init__(
        __self__, *, policy: Optional[pulumi.Input[Union[_builtins.str, Policy]]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[Union[_builtins.str, Policy]]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[Union[_builtins.str, Policy]]]): ...

class ResourceHydrationAccountArgsDict(TypedDict):
    account_name: NotRequired[pulumi.Input[_builtins.str]]
    encrypted_key: NotRequired[pulumi.Input[_builtins.str]]
    max_child_resource_consistency_job_limit: NotRequired[pulumi.Input[_builtins.float]]
    subscription_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceHydrationAccountArgs:
    def __init__(
        __self__,
        *,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encrypted_key: Optional[pulumi.Input[_builtins.str]] = ...,
        max_child_resource_consistency_job_limit: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptedKey")
    def encrypted_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encrypted_key.setter
    def encrypted_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxChildResourceConsistencyJobLimit")
    def max_child_resource_consistency_job_limit(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @max_child_resource_consistency_job_limit.setter
    def max_child_resource_consistency_job_limit(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceProviderAuthorizationManagedByAuthorizationArgsDict(TypedDict):
    additional_authorizations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AdditionalAuthorizationArgsDict]]]
    ]
    allow_managed_by_inheritance: NotRequired[pulumi.Input[_builtins.bool]]
    managed_by_resource_role_definition_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceProviderAuthorizationManagedByAuthorizationArgs:
    def __init__(
        __self__,
        *,
        additional_authorizations: Optional[
            pulumi.Input[Sequence[pulumi.Input[AdditionalAuthorizationArgs]]]
        ] = ...,
        allow_managed_by_inheritance: Optional[pulumi.Input[_builtins.bool]] = ...,
        managed_by_resource_role_definition_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalAuthorizations")
    def additional_authorizations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AdditionalAuthorizationArgs]]]
    ]: ...
    @additional_authorizations.setter
    def additional_authorizations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AdditionalAuthorizationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowManagedByInheritance")
    def allow_managed_by_inheritance(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_managed_by_inheritance.setter
    def allow_managed_by_inheritance(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedByResourceRoleDefinitionId")
    def managed_by_resource_role_definition_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by_resource_role_definition_id.setter
    def managed_by_resource_role_definition_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ResourceProviderAuthorizationRulesArgsDict(TypedDict):
    async_operation_polling_rules: NotRequired[
        pulumi.Input[AsyncOperationPollingRulesArgsDict]
    ]

@pulumi.input_type
class ResourceProviderAuthorizationRulesArgs:
    def __init__(
        __self__,
        *,
        async_operation_polling_rules: Optional[
            pulumi.Input[AsyncOperationPollingRulesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asyncOperationPollingRules")
    def async_operation_polling_rules(
        self,
    ) -> Optional[pulumi.Input[AsyncOperationPollingRulesArgs]]: ...
    @async_operation_polling_rules.setter
    def async_operation_polling_rules(
        self, value: Optional[pulumi.Input[AsyncOperationPollingRulesArgs]]
    ): ...

class ResourceProviderAuthorizationArgsDict(TypedDict):
    allowed_third_party_extensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ThirdPartyExtensionArgsDict]]]
    ]
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    grouping_tag: NotRequired[pulumi.Input[_builtins.str]]
    managed_by_authorization: NotRequired[
        pulumi.Input[ResourceProviderAuthorizationManagedByAuthorizationArgsDict]
    ]
    managed_by_role_definition_id: NotRequired[pulumi.Input[_builtins.str]]
    role_definition_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceProviderAuthorizationArgs:
    def __init__(
        __self__,
        *,
        allowed_third_party_extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ThirdPartyExtensionArgs]]]
        ] = ...,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        grouping_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        managed_by_authorization: Optional[
            pulumi.Input[ResourceProviderAuthorizationManagedByAuthorizationArgs]
        ] = ...,
        managed_by_role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        role_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedThirdPartyExtensions")
    def allowed_third_party_extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ThirdPartyExtensionArgs]]]]: ...
    @allowed_third_party_extensions.setter
    def allowed_third_party_extensions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ThirdPartyExtensionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="groupingTag")
    def grouping_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grouping_tag.setter
    def grouping_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="managedByAuthorization")
    def managed_by_authorization(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderAuthorizationManagedByAuthorizationArgs]
    ]: ...
    @managed_by_authorization.setter
    def managed_by_authorization(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderAuthorizationManagedByAuthorizationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="managedByRoleDefinitionId")
    def managed_by_role_definition_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @managed_by_role_definition_id.setter
    def managed_by_role_definition_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceProviderCapabilitiesArgsDict(TypedDict):
    effect: pulumi.Input[Union[_builtins.str, ResourceProviderCapabilitiesEffect]]
    quota_id: pulumi.Input[_builtins.str]
    required_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ResourceProviderCapabilitiesArgs:
    def __init__(
        __self__,
        *,
        effect: pulumi.Input[Union[_builtins.str, ResourceProviderCapabilitiesEffect]],
        quota_id: pulumi.Input[_builtins.str],
        required_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ResourceProviderCapabilitiesEffect]]: ...
    @effect.setter
    def effect(
        self,
        value: pulumi.Input[Union[_builtins.str, ResourceProviderCapabilitiesEffect]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> pulumi.Input[_builtins.str]: ...
    @quota_id.setter
    def quota_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_features.setter
    def required_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ResourceProviderEndpointFeaturesRuleArgsDict(TypedDict):
    required_features_policy: pulumi.Input[Union[_builtins.str, FeaturesPolicy]]

@pulumi.input_type
class ResourceProviderEndpointFeaturesRuleArgs:
    def __init__(
        __self__,
        *,
        required_features_policy: pulumi.Input[Union[_builtins.str, FeaturesPolicy]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeaturesPolicy")
    def required_features_policy(
        self,
    ) -> pulumi.Input[Union[_builtins.str, FeaturesPolicy]]: ...
    @required_features_policy.setter
    def required_features_policy(
        self, value: pulumi.Input[Union[_builtins.str, FeaturesPolicy]]
    ): ...

class ResourceProviderEndpointArgsDict(TypedDict):
    api_versions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    endpoint_type: NotRequired[pulumi.Input[Union[_builtins.str, EndpointType]]]
    endpoint_uri: NotRequired[pulumi.Input[_builtins.str]]
    features_rule: NotRequired[
        pulumi.Input[ResourceProviderEndpointFeaturesRuleArgsDict]
    ]
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    required_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    sku_link: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceProviderEndpointArgs:
    def __init__(
        __self__,
        *,
        api_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_type: Optional[pulumi.Input[Union[_builtins.str, EndpointType]]] = ...,
        endpoint_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        features_rule: Optional[
            pulumi.Input[ResourceProviderEndpointFeaturesRuleArgs]
        ] = ...,
        locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        required_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        sku_link: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersions")
    def api_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @api_versions.setter
    def api_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EndpointType]]]: ...
    @endpoint_type.setter
    def endpoint_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, EndpointType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_uri.setter
    def endpoint_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="featuresRule")
    def features_rule(
        self,
    ) -> Optional[pulumi.Input[ResourceProviderEndpointFeaturesRuleArgs]]: ...
    @features_rule.setter
    def features_rule(
        self, value: Optional[pulumi.Input[ResourceProviderEndpointFeaturesRuleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @locations.setter
    def locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_features.setter
    def required_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skuLink")
    def sku_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku_link.setter
    def sku_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceProviderManagementErrorResponseMessageOptionsArgsDict(TypedDict):
    server_failure_response_message_type: NotRequired[
        pulumi.Input[Union[_builtins.str, ServerFailureResponseMessageType]]
    ]

@pulumi.input_type
class ResourceProviderManagementErrorResponseMessageOptionsArgs:
    def __init__(
        __self__,
        *,
        server_failure_response_message_type: Optional[
            pulumi.Input[Union[_builtins.str, ServerFailureResponseMessageType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverFailureResponseMessageType")
    def server_failure_response_message_type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ServerFailureResponseMessageType]]
    ]: ...
    @server_failure_response_message_type.setter
    def server_failure_response_message_type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ServerFailureResponseMessageType]]
        ],
    ): ...

class ResourceProviderManagementExpeditedRolloutMetadataArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    expedited_rollout_intent: NotRequired[
        pulumi.Input[Union[_builtins.str, ExpeditedRolloutIntent]]
    ]

@pulumi.input_type
class ResourceProviderManagementExpeditedRolloutMetadataArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        expedited_rollout_intent: Optional[
            pulumi.Input[Union[_builtins.str, ExpeditedRolloutIntent]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutIntent")
    def expedited_rollout_intent(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ExpeditedRolloutIntent]]]: ...
    @expedited_rollout_intent.setter
    def expedited_rollout_intent(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ExpeditedRolloutIntent]]],
    ): ...

class ResourceProviderManifestPropertiesDstsConfigurationArgsDict(TypedDict):
    service_name: pulumi.Input[_builtins.str]
    service_dns_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceProviderManifestPropertiesDstsConfigurationArgs:
    def __init__(
        __self__,
        *,
        service_name: pulumi.Input[_builtins.str],
        service_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_dns_name.setter
    def service_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceProviderManifestPropertiesFeaturesRuleArgsDict(TypedDict):
    required_features_policy: pulumi.Input[Union[_builtins.str, FeaturesPolicy]]

@pulumi.input_type
class ResourceProviderManifestPropertiesFeaturesRuleArgs:
    def __init__(
        __self__,
        *,
        required_features_policy: pulumi.Input[Union[_builtins.str, FeaturesPolicy]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeaturesPolicy")
    def required_features_policy(
        self,
    ) -> pulumi.Input[Union[_builtins.str, FeaturesPolicy]]: ...
    @required_features_policy.setter
    def required_features_policy(
        self, value: pulumi.Input[Union[_builtins.str, FeaturesPolicy]]
    ): ...

class ResourceProviderManifestPropertiesManagementArgsDict(TypedDict):
    authorization_owners: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    canary_manifest_owners: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    error_response_message_options: NotRequired[
        pulumi.Input[ResourceProviderManagementErrorResponseMessageOptionsArgsDict]
    ]
    expedited_rollout_metadata: NotRequired[
        pulumi.Input[ResourceProviderManagementExpeditedRolloutMetadataArgsDict]
    ]
    expedited_rollout_submitters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    incident_contact_email: NotRequired[pulumi.Input[_builtins.str]]
    incident_routing_service: NotRequired[pulumi.Input[_builtins.str]]
    incident_routing_team: NotRequired[pulumi.Input[_builtins.str]]
    manifest_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    pc_code: NotRequired[pulumi.Input[_builtins.str]]
    profit_center_program_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_access_policy: NotRequired[pulumi.Input[ResourceAccessPolicy]]
    resource_access_roles: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceAccessRoleArgsDict]]]
    ]
    schema_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    service_tree_infos: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgsDict]]]
    ]

@pulumi.input_type
class ResourceProviderManifestPropertiesManagementArgs:
    def __init__(
        __self__,
        *,
        authorization_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        canary_manifest_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        error_response_message_options: Optional[
            pulumi.Input[ResourceProviderManagementErrorResponseMessageOptionsArgs]
        ] = ...,
        expedited_rollout_metadata: Optional[
            pulumi.Input[ResourceProviderManagementExpeditedRolloutMetadataArgs]
        ] = ...,
        expedited_rollout_submitters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        incident_contact_email: Optional[pulumi.Input[_builtins.str]] = ...,
        incident_routing_service: Optional[pulumi.Input[_builtins.str]] = ...,
        incident_routing_team: Optional[pulumi.Input[_builtins.str]] = ...,
        manifest_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        pc_code: Optional[pulumi.Input[_builtins.str]] = ...,
        profit_center_program_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_access_policy: Optional[pulumi.Input[ResourceAccessPolicy]] = ...,
        resource_access_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceAccessRoleArgs]]]
        ] = ...,
        schema_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_tree_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationOwners")
    def authorization_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @authorization_owners.setter
    def authorization_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="canaryManifestOwners")
    def canary_manifest_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @canary_manifest_owners.setter
    def canary_manifest_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorResponseMessageOptions")
    def error_response_message_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManagementErrorResponseMessageOptionsArgs]
    ]: ...
    @error_response_message_options.setter
    def error_response_message_options(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManagementErrorResponseMessageOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutMetadata")
    def expedited_rollout_metadata(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManagementExpeditedRolloutMetadataArgs]
    ]: ...
    @expedited_rollout_metadata.setter
    def expedited_rollout_metadata(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManagementExpeditedRolloutMetadataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutSubmitters")
    def expedited_rollout_submitters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @expedited_rollout_submitters.setter
    def expedited_rollout_submitters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="incidentContactEmail")
    def incident_contact_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @incident_contact_email.setter
    def incident_contact_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="incidentRoutingService")
    def incident_routing_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @incident_routing_service.setter
    def incident_routing_service(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="incidentRoutingTeam")
    def incident_routing_team(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @incident_routing_team.setter
    def incident_routing_team(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manifestOwners")
    def manifest_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @manifest_owners.setter
    def manifest_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pcCode")
    def pc_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pc_code.setter
    def pc_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profitCenterProgramId")
    def profit_center_program_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profit_center_program_id.setter
    def profit_center_program_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessPolicy")
    def resource_access_policy(
        self,
    ) -> Optional[pulumi.Input[ResourceAccessPolicy]]: ...
    @resource_access_policy.setter
    def resource_access_policy(
        self, value: Optional[pulumi.Input[ResourceAccessPolicy]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRoles")
    def resource_access_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceAccessRoleArgs]]]]: ...
    @resource_access_roles.setter
    def resource_access_roles(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceAccessRoleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schemaOwners")
    def schema_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @schema_owners.setter
    def schema_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceTreeInfos")
    def service_tree_infos(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgs]]]]: ...
    @service_tree_infos.setter
    def service_tree_infos(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgs]]]]
    ): ...

class ResourceProviderManifestPropertiesNotificationSettingsArgsDict(TypedDict):
    subscriber_settings: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubscriberSettingArgsDict]]]
    ]

@pulumi.input_type
class ResourceProviderManifestPropertiesNotificationSettingsArgs:
    def __init__(
        __self__,
        *,
        subscriber_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriberSettingArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subscriberSettings")
    def subscriber_settings(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSettingArgs]]]]: ...
    @subscriber_settings.setter
    def subscriber_settings(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SubscriberSettingArgs]]]],
    ): ...

class ResourceProviderManifestPropertiesProviderAuthenticationArgsDict(TypedDict):
    allowed_audiences: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ResourceProviderManifestPropertiesProviderAuthenticationArgs:
    def __init__(
        __self__,
        *,
        allowed_audiences: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @allowed_audiences.setter
    def allowed_audiences(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ResourceProviderManifestPropertiesRequestHeaderOptionsArgsDict(TypedDict):
    opt_in_headers: NotRequired[pulumi.Input[Union[_builtins.str, OptInHeaderType]]]
    opt_out_headers: NotRequired[pulumi.Input[Union[_builtins.str, OptOutHeaderType]]]

@pulumi.input_type
class ResourceProviderManifestPropertiesRequestHeaderOptionsArgs:
    def __init__(
        __self__,
        *,
        opt_in_headers: Optional[
            pulumi.Input[Union[_builtins.str, OptInHeaderType]]
        ] = ...,
        opt_out_headers: Optional[
            pulumi.Input[Union[_builtins.str, OptOutHeaderType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optInHeaders")
    def opt_in_headers(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OptInHeaderType]]]: ...
    @opt_in_headers.setter
    def opt_in_headers(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OptInHeaderType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="optOutHeaders")
    def opt_out_headers(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OptOutHeaderType]]]: ...
    @opt_out_headers.setter
    def opt_out_headers(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OptOutHeaderType]]]
    ): ...

class ResourceProviderManifestPropertiesResourceGroupLockOptionDuringMoveArgsDict(
    TypedDict
):
    block_action_verb: NotRequired[pulumi.Input[Union[_builtins.str, BlockActionVerb]]]

@pulumi.input_type
class ResourceProviderManifestPropertiesResourceGroupLockOptionDuringMoveArgs:
    def __init__(
        __self__,
        *,
        block_action_verb: Optional[
            pulumi.Input[Union[_builtins.str, BlockActionVerb]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockActionVerb")
    def block_action_verb(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, BlockActionVerb]]]: ...
    @block_action_verb.setter
    def block_action_verb(
        self, value: Optional[pulumi.Input[Union[_builtins.str, BlockActionVerb]]]
    ): ...

class ResourceProviderManifestPropertiesResponseOptionsArgsDict(TypedDict):
    service_client_options_type: NotRequired[
        pulumi.Input[Union[_builtins.str, ServiceClientOptionsType]]
    ]

@pulumi.input_type
class ResourceProviderManifestPropertiesResponseOptionsArgs:
    def __init__(
        __self__,
        *,
        service_client_options_type: Optional[
            pulumi.Input[Union[_builtins.str, ServiceClientOptionsType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceClientOptionsType")
    def service_client_options_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ServiceClientOptionsType]]]: ...
    @service_client_options_type.setter
    def service_client_options_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ServiceClientOptionsType]]],
    ): ...

class ResourceProviderManifestPropertiesTemplateDeploymentOptionsArgsDict(TypedDict):
    preflight_options: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreflightOption]]]]
    ]
    preflight_supported: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ResourceProviderManifestPropertiesTemplateDeploymentOptionsArgs:
    def __init__(
        __self__,
        *,
        preflight_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreflightOption]]]]
        ] = ...,
        preflight_supported: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preflightOptions")
    def preflight_options(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreflightOption]]]]
    ]: ...
    @preflight_options.setter
    def preflight_options(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreflightOption]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="preflightSupported")
    def preflight_supported(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preflight_supported.setter
    def preflight_supported(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ResourceProviderServiceArgsDict(TypedDict):
    service_name: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, ServiceStatus]]]

@pulumi.input_type
class ResourceProviderServiceArgs:
    def __init__(
        __self__,
        *,
        service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[Union[_builtins.str, ServiceStatus]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, ServiceStatus]]]: ...
    @status.setter
    def status(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ServiceStatus]]]
    ): ...

class ResourceTypeEndpointDstsConfigurationArgsDict(TypedDict):
    service_name: pulumi.Input[_builtins.str]
    service_dns_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceTypeEndpointDstsConfigurationArgs:
    def __init__(
        __self__,
        *,
        service_name: pulumi.Input[_builtins.str],
        service_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_dns_name.setter
    def service_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceTypeEndpointFeaturesRuleArgsDict(TypedDict):
    required_features_policy: pulumi.Input[Union[_builtins.str, FeaturesPolicy]]

@pulumi.input_type
class ResourceTypeEndpointFeaturesRuleArgs:
    def __init__(
        __self__,
        *,
        required_features_policy: pulumi.Input[Union[_builtins.str, FeaturesPolicy]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeaturesPolicy")
    def required_features_policy(
        self,
    ) -> pulumi.Input[Union[_builtins.str, FeaturesPolicy]]: ...
    @required_features_policy.setter
    def required_features_policy(
        self, value: pulumi.Input[Union[_builtins.str, FeaturesPolicy]]
    ): ...

class ResourceTypeEndpointArgsDict(TypedDict):
    api_version: NotRequired[pulumi.Input[_builtins.str]]
    api_versions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    data_boundary: NotRequired[pulumi.Input[Union[_builtins.str, DataBoundary]]]
    dsts_configuration: NotRequired[
        pulumi.Input[ResourceTypeEndpointDstsConfigurationArgsDict]
    ]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    endpoint_type: NotRequired[
        pulumi.Input[Union[_builtins.str, EndpointTypeResourceType]]
    ]
    endpoint_uri: NotRequired[pulumi.Input[_builtins.str]]
    extensions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceTypeExtensionArgsDict]]]
    ]
    features_rule: NotRequired[pulumi.Input[ResourceTypeEndpointFeaturesRuleArgsDict]]
    kind: NotRequired[pulumi.Input[Union[_builtins.str, ResourceTypeEndpointKind]]]
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    required_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    sku_link: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    token_auth_configuration: NotRequired[pulumi.Input[TokenAuthConfigurationArgsDict]]
    zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ResourceTypeEndpointArgs:
    def __init__(
        __self__,
        *,
        api_version: Optional[pulumi.Input[_builtins.str]] = ...,
        api_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        data_boundary: Optional[pulumi.Input[Union[_builtins.str, DataBoundary]]] = ...,
        dsts_configuration: Optional[
            pulumi.Input[ResourceTypeEndpointDstsConfigurationArgs]
        ] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoint_type: Optional[
            pulumi.Input[Union[_builtins.str, EndpointTypeResourceType]]
        ] = ...,
        endpoint_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceTypeExtensionArgs]]]
        ] = ...,
        features_rule: Optional[
            pulumi.Input[ResourceTypeEndpointFeaturesRuleArgs]
        ] = ...,
        kind: Optional[
            pulumi.Input[Union[_builtins.str, ResourceTypeEndpointKind]]
        ] = ...,
        locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        required_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        sku_link: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        token_auth_configuration: Optional[
            pulumi.Input[TokenAuthConfigurationArgs]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="apiVersions")
    def api_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @api_versions.setter
    def api_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataBoundary")
    def data_boundary(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DataBoundary]]]: ...
    @data_boundary.setter
    def data_boundary(
        self, value: Optional[pulumi.Input[Union[_builtins.str, DataBoundary]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dstsConfiguration")
    def dsts_configuration(
        self,
    ) -> Optional[pulumi.Input[ResourceTypeEndpointDstsConfigurationArgs]]: ...
    @dsts_configuration.setter
    def dsts_configuration(
        self, value: Optional[pulumi.Input[ResourceTypeEndpointDstsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, EndpointTypeResourceType]]]: ...
    @endpoint_type.setter
    def endpoint_type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, EndpointTypeResourceType]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_uri.setter
    def endpoint_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceTypeExtensionArgs]]]]: ...
    @extensions.setter
    def extensions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceTypeExtensionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="featuresRule")
    def features_rule(
        self,
    ) -> Optional[pulumi.Input[ResourceTypeEndpointFeaturesRuleArgs]]: ...
    @features_rule.setter
    def features_rule(
        self, value: Optional[pulumi.Input[ResourceTypeEndpointFeaturesRuleArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceTypeEndpointKind]]]: ...
    @kind.setter
    def kind(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ResourceTypeEndpointKind]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @locations.setter
    def locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_features.setter
    def required_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skuLink")
    def sku_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku_link.setter
    def sku_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenAuthConfiguration")
    def token_auth_configuration(
        self,
    ) -> Optional[pulumi.Input[TokenAuthConfigurationArgs]]: ...
    @token_auth_configuration.setter
    def token_auth_configuration(
        self, value: Optional[pulumi.Input[TokenAuthConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ResourceTypeExtensionOptionsResourceCreationBeginArgsDict(TypedDict):
    request: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExtensionOptionType]]]]
    ]
    response: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExtensionOptionType]]]]
    ]

@pulumi.input_type
class ResourceTypeExtensionOptionsResourceCreationBeginArgs:
    def __init__(
        __self__,
        *,
        request: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExtensionOptionType]]]
            ]
        ] = ...,
        response: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExtensionOptionType]]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def request(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExtensionOptionType]]]]
    ]: ...
    @request.setter
    def request(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExtensionOptionType]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def response(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExtensionOptionType]]]]
    ]: ...
    @response.setter
    def response(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExtensionOptionType]]]
            ]
        ],
    ): ...

class ResourceTypeExtensionArgsDict(TypedDict):
    endpoint_uri: NotRequired[pulumi.Input[_builtins.str]]
    extension_categories: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExtensionCategory]]]]
    ]
    timeout: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceTypeExtensionArgs:
    def __init__(
        __self__,
        *,
        endpoint_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        extension_categories: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExtensionCategory]]]
            ]
        ] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_uri.setter
    def endpoint_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="extensionCategories")
    def extension_categories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, ExtensionCategory]]]]
    ]: ...
    @extension_categories.setter
    def extension_categories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, ExtensionCategory]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceTypeOnBehalfOfTokenArgsDict(TypedDict):
    action_name: NotRequired[pulumi.Input[_builtins.str]]
    life_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceTypeOnBehalfOfTokenArgs:
    def __init__(
        __self__,
        *,
        action_name: Optional[pulumi.Input[_builtins.str]] = ...,
        life_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action_name.setter
    def action_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lifeTime")
    def life_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @life_time.setter
    def life_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceTypeRegistrationPropertiesAvailabilityZoneRuleArgsDict(TypedDict):
    availability_zone_policy: NotRequired[
        pulumi.Input[Union[_builtins.str, AvailabilityZonePolicy]]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesAvailabilityZoneRuleArgs:
    def __init__(
        __self__,
        *,
        availability_zone_policy: Optional[
            pulumi.Input[Union[_builtins.str, AvailabilityZonePolicy]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZonePolicy")
    def availability_zone_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AvailabilityZonePolicy]]]: ...
    @availability_zone_policy.setter
    def availability_zone_policy(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, AvailabilityZonePolicy]]],
    ): ...

class ResourceTypeRegistrationPropertiesCapacityRuleArgsDict(TypedDict):
    capacity_policy: NotRequired[pulumi.Input[Union[_builtins.str, CapacityPolicy]]]
    sku_alias: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesCapacityRuleArgs:
    def __init__(
        __self__,
        *,
        capacity_policy: Optional[
            pulumi.Input[Union[_builtins.str, CapacityPolicy]]
        ] = ...,
        sku_alias: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityPolicy")
    def capacity_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CapacityPolicy]]]: ...
    @capacity_policy.setter
    def capacity_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CapacityPolicy]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skuAlias")
    def sku_alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku_alias.setter
    def sku_alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceTypeRegistrationPropertiesCheckNameAvailabilitySpecificationsArgsDict(
    TypedDict
):
    enable_default_validation: NotRequired[pulumi.Input[_builtins.bool]]
    resource_types_with_custom_validation: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesCheckNameAvailabilitySpecificationsArgs:
    def __init__(
        __self__,
        *,
        enable_default_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        resource_types_with_custom_validation: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableDefaultValidation")
    def enable_default_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_default_validation.setter
    def enable_default_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypesWithCustomValidation")
    def resource_types_with_custom_validation(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resource_types_with_custom_validation.setter
    def resource_types_with_custom_validation(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ResourceTypeRegistrationPropertiesDstsConfigurationArgsDict(TypedDict):
    service_name: pulumi.Input[_builtins.str]
    service_dns_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesDstsConfigurationArgs:
    def __init__(
        __self__,
        *,
        service_name: pulumi.Input[_builtins.str],
        service_dns_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]: ...
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_dns_name.setter
    def service_dns_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceTypeRegistrationPropertiesExtensionOptionsArgsDict(TypedDict):
    resource_creation_begin: NotRequired[
        pulumi.Input[ResourceTypeExtensionOptionsResourceCreationBeginArgsDict]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesExtensionOptionsArgs:
    def __init__(
        __self__,
        *,
        resource_creation_begin: Optional[
            pulumi.Input[ResourceTypeExtensionOptionsResourceCreationBeginArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceCreationBegin")
    def resource_creation_begin(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeExtensionOptionsResourceCreationBeginArgs]
    ]: ...
    @resource_creation_begin.setter
    def resource_creation_begin(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeExtensionOptionsResourceCreationBeginArgs]
        ],
    ): ...

class ResourceTypeRegistrationPropertiesFeaturesRuleArgsDict(TypedDict):
    required_features_policy: pulumi.Input[Union[_builtins.str, FeaturesPolicy]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesFeaturesRuleArgs:
    def __init__(
        __self__,
        *,
        required_features_policy: pulumi.Input[Union[_builtins.str, FeaturesPolicy]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeaturesPolicy")
    def required_features_policy(
        self,
    ) -> pulumi.Input[Union[_builtins.str, FeaturesPolicy]]: ...
    @required_features_policy.setter
    def required_features_policy(
        self, value: pulumi.Input[Union[_builtins.str, FeaturesPolicy]]
    ): ...

class ResourceTypeRegistrationPropertiesIdentityManagementArgsDict(TypedDict):
    application_id: NotRequired[pulumi.Input[_builtins.str]]
    application_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    delegation_app_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, IdentityManagementTypes]]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesIdentityManagementArgs:
    def __init__(
        __self__,
        *,
        application_id: Optional[pulumi.Input[_builtins.str]] = ...,
        application_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        delegation_app_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[
            pulumi.Input[Union[_builtins.str, IdentityManagementTypes]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="applicationIds")
    def application_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @application_ids.setter
    def application_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="delegationAppIds")
    def delegation_app_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @delegation_app_ids.setter
    def delegation_app_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, IdentityManagementTypes]]]: ...
    @type.setter
    def type(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, IdentityManagementTypes]]],
    ): ...

class ResourceTypeRegistrationPropertiesLegacyPolicyArgsDict(TypedDict):
    disallowed_conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LegacyDisallowedConditionArgsDict]]]
    ]
    disallowed_legacy_operations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LegacyOperation]]]]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesLegacyPolicyArgs:
    def __init__(
        __self__,
        *,
        disallowed_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[LegacyDisallowedConditionArgs]]]
        ] = ...,
        disallowed_legacy_operations: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LegacyOperation]]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disallowedConditions")
    def disallowed_conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LegacyDisallowedConditionArgs]]]
    ]: ...
    @disallowed_conditions.setter
    def disallowed_conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LegacyDisallowedConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="disallowedLegacyOperations")
    def disallowed_legacy_operations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LegacyOperation]]]]
    ]: ...
    @disallowed_legacy_operations.setter
    def disallowed_legacy_operations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, LegacyOperation]]]]
        ],
    ): ...

class ResourceTypeRegistrationPropertiesManagementArgsDict(TypedDict):
    authorization_owners: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    canary_manifest_owners: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    error_response_message_options: NotRequired[
        pulumi.Input[ResourceProviderManagementErrorResponseMessageOptionsArgsDict]
    ]
    expedited_rollout_metadata: NotRequired[
        pulumi.Input[ResourceProviderManagementExpeditedRolloutMetadataArgsDict]
    ]
    expedited_rollout_submitters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    incident_contact_email: NotRequired[pulumi.Input[_builtins.str]]
    incident_routing_service: NotRequired[pulumi.Input[_builtins.str]]
    incident_routing_team: NotRequired[pulumi.Input[_builtins.str]]
    manifest_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    pc_code: NotRequired[pulumi.Input[_builtins.str]]
    profit_center_program_id: NotRequired[pulumi.Input[_builtins.str]]
    resource_access_policy: NotRequired[pulumi.Input[ResourceAccessPolicy]]
    resource_access_roles: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceAccessRoleArgsDict]]]
    ]
    schema_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    service_tree_infos: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgsDict]]]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesManagementArgs:
    def __init__(
        __self__,
        *,
        authorization_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        canary_manifest_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        error_response_message_options: Optional[
            pulumi.Input[ResourceProviderManagementErrorResponseMessageOptionsArgs]
        ] = ...,
        expedited_rollout_metadata: Optional[
            pulumi.Input[ResourceProviderManagementExpeditedRolloutMetadataArgs]
        ] = ...,
        expedited_rollout_submitters: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        incident_contact_email: Optional[pulumi.Input[_builtins.str]] = ...,
        incident_routing_service: Optional[pulumi.Input[_builtins.str]] = ...,
        incident_routing_team: Optional[pulumi.Input[_builtins.str]] = ...,
        manifest_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        pc_code: Optional[pulumi.Input[_builtins.str]] = ...,
        profit_center_program_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_access_policy: Optional[pulumi.Input[ResourceAccessPolicy]] = ...,
        resource_access_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceAccessRoleArgs]]]
        ] = ...,
        schema_owners: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        service_tree_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationOwners")
    def authorization_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @authorization_owners.setter
    def authorization_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="canaryManifestOwners")
    def canary_manifest_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @canary_manifest_owners.setter
    def canary_manifest_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="errorResponseMessageOptions")
    def error_response_message_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManagementErrorResponseMessageOptionsArgs]
    ]: ...
    @error_response_message_options.setter
    def error_response_message_options(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManagementErrorResponseMessageOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutMetadata")
    def expedited_rollout_metadata(
        self,
    ) -> Optional[
        pulumi.Input[ResourceProviderManagementExpeditedRolloutMetadataArgs]
    ]: ...
    @expedited_rollout_metadata.setter
    def expedited_rollout_metadata(
        self,
        value: Optional[
            pulumi.Input[ResourceProviderManagementExpeditedRolloutMetadataArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutSubmitters")
    def expedited_rollout_submitters(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @expedited_rollout_submitters.setter
    def expedited_rollout_submitters(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="incidentContactEmail")
    def incident_contact_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @incident_contact_email.setter
    def incident_contact_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="incidentRoutingService")
    def incident_routing_service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @incident_routing_service.setter
    def incident_routing_service(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="incidentRoutingTeam")
    def incident_routing_team(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @incident_routing_team.setter
    def incident_routing_team(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manifestOwners")
    def manifest_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @manifest_owners.setter
    def manifest_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pcCode")
    def pc_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pc_code.setter
    def pc_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profitCenterProgramId")
    def profit_center_program_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profit_center_program_id.setter
    def profit_center_program_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessPolicy")
    def resource_access_policy(
        self,
    ) -> Optional[pulumi.Input[ResourceAccessPolicy]]: ...
    @resource_access_policy.setter
    def resource_access_policy(
        self, value: Optional[pulumi.Input[ResourceAccessPolicy]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRoles")
    def resource_access_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceAccessRoleArgs]]]]: ...
    @resource_access_roles.setter
    def resource_access_roles(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceAccessRoleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schemaOwners")
    def schema_owners(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @schema_owners.setter
    def schema_owners(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceTreeInfos")
    def service_tree_infos(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgs]]]]: ...
    @service_tree_infos.setter
    def service_tree_infos(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgs]]]]
    ): ...

class ResourceTypeRegistrationPropertiesMarketplaceOptionsArgsDict(TypedDict):
    add_on_plan_conversion_allowed: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesMarketplaceOptionsArgs:
    def __init__(
        __self__,
        *,
        add_on_plan_conversion_allowed: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addOnPlanConversionAllowed")
    def add_on_plan_conversion_allowed(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @add_on_plan_conversion_allowed.setter
    def add_on_plan_conversion_allowed(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class ResourceTypeRegistrationPropertiesRequestHeaderOptionsArgsDict(TypedDict):
    opt_in_headers: NotRequired[pulumi.Input[Union[_builtins.str, OptInHeaderType]]]
    opt_out_headers: NotRequired[pulumi.Input[Union[_builtins.str, OptOutHeaderType]]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesRequestHeaderOptionsArgs:
    def __init__(
        __self__,
        *,
        opt_in_headers: Optional[
            pulumi.Input[Union[_builtins.str, OptInHeaderType]]
        ] = ...,
        opt_out_headers: Optional[
            pulumi.Input[Union[_builtins.str, OptOutHeaderType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optInHeaders")
    def opt_in_headers(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OptInHeaderType]]]: ...
    @opt_in_headers.setter
    def opt_in_headers(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OptInHeaderType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="optOutHeaders")
    def opt_out_headers(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, OptOutHeaderType]]]: ...
    @opt_out_headers.setter
    def opt_out_headers(
        self, value: Optional[pulumi.Input[Union[_builtins.str, OptOutHeaderType]]]
    ): ...

class ResourceTypeRegistrationPropertiesResourceCacheArgsDict(TypedDict):
    enable_resource_cache: NotRequired[pulumi.Input[_builtins.bool]]
    resource_cache_expiration_timespan: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesResourceCacheArgs:
    def __init__(
        __self__,
        *,
        enable_resource_cache: Optional[pulumi.Input[_builtins.bool]] = ...,
        resource_cache_expiration_timespan: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableResourceCache")
    def enable_resource_cache(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_resource_cache.setter
    def enable_resource_cache(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceCacheExpirationTimespan")
    def resource_cache_expiration_timespan(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_cache_expiration_timespan.setter
    def resource_cache_expiration_timespan(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ResourceTypeRegistrationPropertiesResourceGraphConfigurationArgsDict(TypedDict):
    api_version: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesResourceGraphConfigurationArgs:
    def __init__(
        __self__,
        *,
        api_version: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ResourceTypeRegistrationPropertiesResourceManagementOptionsBatchProvisioningSupportArgsDict(
    TypedDict
):
    supported_operations: NotRequired[
        pulumi.Input[Union[_builtins.str, SupportedOperations]]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesResourceManagementOptionsBatchProvisioningSupportArgs:
    def __init__(
        __self__,
        *,
        supported_operations: Optional[
            pulumi.Input[Union[_builtins.str, SupportedOperations]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportedOperations")
    def supported_operations(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SupportedOperations]]]: ...
    @supported_operations.setter
    def supported_operations(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SupportedOperations]]]
    ): ...

class ResourceTypeRegistrationPropertiesResourceManagementOptionsNestedProvisioningSupportArgsDict(
    TypedDict
):
    minimum_api_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesResourceManagementOptionsNestedProvisioningSupportArgs:
    def __init__(
        __self__, *, minimum_api_version: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumApiVersion")
    def minimum_api_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_api_version.setter
    def minimum_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceTypeRegistrationPropertiesResourceManagementOptionsArgsDict(TypedDict):
    batch_provisioning_support: NotRequired[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesResourceManagementOptionsBatchProvisioningSupportArgsDict
        ]
    ]
    delete_dependencies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DeleteDependencyArgsDict]]]
    ]
    nested_provisioning_support: NotRequired[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesResourceManagementOptionsNestedProvisioningSupportArgsDict
        ]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesResourceManagementOptionsArgs:
    def __init__(
        __self__,
        *,
        batch_provisioning_support: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceManagementOptionsBatchProvisioningSupportArgs
            ]
        ] = ...,
        delete_dependencies: Optional[
            pulumi.Input[Sequence[pulumi.Input[DeleteDependencyArgs]]]
        ] = ...,
        nested_provisioning_support: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceManagementOptionsNestedProvisioningSupportArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchProvisioningSupport")
    def batch_provisioning_support(
        self,
    ) -> Optional[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesResourceManagementOptionsBatchProvisioningSupportArgs
        ]
    ]: ...
    @batch_provisioning_support.setter
    def batch_provisioning_support(
        self,
        value: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceManagementOptionsBatchProvisioningSupportArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteDependencies")
    def delete_dependencies(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DeleteDependencyArgs]]]]: ...
    @delete_dependencies.setter
    def delete_dependencies(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DeleteDependencyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nestedProvisioningSupport")
    def nested_provisioning_support(
        self,
    ) -> Optional[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesResourceManagementOptionsNestedProvisioningSupportArgs
        ]
    ]: ...
    @nested_provisioning_support.setter
    def nested_provisioning_support(
        self,
        value: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceManagementOptionsNestedProvisioningSupportArgs
            ]
        ],
    ): ...

class ResourceTypeRegistrationPropertiesResourceMovePolicyArgsDict(TypedDict):
    cross_resource_group_move_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    cross_subscription_move_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    validation_required: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesResourceMovePolicyArgs:
    def __init__(
        __self__,
        *,
        cross_resource_group_move_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        cross_subscription_move_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        validation_required: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossResourceGroupMoveEnabled")
    def cross_resource_group_move_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cross_resource_group_move_enabled.setter
    def cross_resource_group_move_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crossSubscriptionMoveEnabled")
    def cross_subscription_move_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cross_subscription_move_enabled.setter
    def cross_subscription_move_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="validationRequired")
    def validation_required(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @validation_required.setter
    def validation_required(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ResourceTypeRegistrationPropertiesResourceQueryManagementArgsDict(TypedDict):
    filter_option: NotRequired[pulumi.Input[Union[_builtins.str, FilterOption]]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesResourceQueryManagementArgs:
    def __init__(
        __self__,
        *,
        filter_option: Optional[pulumi.Input[Union[_builtins.str, FilterOption]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterOption")
    def filter_option(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FilterOption]]]: ...
    @filter_option.setter
    def filter_option(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FilterOption]]]
    ): ...

class ResourceTypeRegistrationPropertiesResourceTypeCommonAttributeManagementArgsDict(
    TypedDict
):
    common_api_versions_merge_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, CommonApiVersionsMergeMode]]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesResourceTypeCommonAttributeManagementArgs:
    def __init__(
        __self__,
        *,
        common_api_versions_merge_mode: Optional[
            pulumi.Input[Union[_builtins.str, CommonApiVersionsMergeMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonApiVersionsMergeMode")
    def common_api_versions_merge_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CommonApiVersionsMergeMode]]]: ...
    @common_api_versions_merge_mode.setter
    def common_api_versions_merge_mode(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, CommonApiVersionsMergeMode]]],
    ): ...

class ResourceTypeRegistrationPropertiesRoutingRuleArgsDict(TypedDict):
    host_resource_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesRoutingRuleArgs:
    def __init__(
        __self__, *, host_resource_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostResourceType")
    def host_resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_resource_type.setter
    def host_resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ResourceTypeRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgsDict(
    TypedDict
):
    soft_delete_ttl: NotRequired[pulumi.Input[_builtins.str]]
    subscription_state_override_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubscriptionStateOverrideActionArgsDict]]]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgs:
    def __init__(
        __self__,
        *,
        soft_delete_ttl: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_state_override_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionStateOverrideActionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="softDeleteTTL")
    def soft_delete_ttl(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @soft_delete_ttl.setter
    def soft_delete_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionStateOverrideActions")
    def subscription_state_override_actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SubscriptionStateOverrideActionArgs]]]
    ]: ...
    @subscription_state_override_actions.setter
    def subscription_state_override_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionStateOverrideActionArgs]]]
        ],
    ): ...

class ResourceTypeRegistrationPropertiesTemplateDeploymentOptionsArgsDict(TypedDict):
    preflight_options: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreflightOption]]]]
    ]
    preflight_supported: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesTemplateDeploymentOptionsArgs:
    def __init__(
        __self__,
        *,
        preflight_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreflightOption]]]]
        ] = ...,
        preflight_supported: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preflightOptions")
    def preflight_options(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreflightOption]]]]
    ]: ...
    @preflight_options.setter
    def preflight_options(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, PreflightOption]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="preflightSupported")
    def preflight_supported(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preflight_supported.setter
    def preflight_supported(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ResourceTypeRegistrationPropertiesTemplateDeploymentPolicyArgsDict(TypedDict):
    capabilities: pulumi.Input[Union[_builtins.str, TemplateDeploymentCapabilities]]
    preflight_options: pulumi.Input[
        Union[_builtins.str, TemplateDeploymentPreflightOptions]
    ]
    preflight_notifications: NotRequired[
        pulumi.Input[Union[_builtins.str, TemplateDeploymentPreflightNotifications]]
    ]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesTemplateDeploymentPolicyArgs:
    def __init__(
        __self__,
        *,
        capabilities: pulumi.Input[
            Union[_builtins.str, TemplateDeploymentCapabilities]
        ],
        preflight_options: pulumi.Input[
            Union[_builtins.str, TemplateDeploymentPreflightOptions]
        ],
        preflight_notifications: Optional[
            pulumi.Input[Union[_builtins.str, TemplateDeploymentPreflightNotifications]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> pulumi.Input[Union[_builtins.str, TemplateDeploymentCapabilities]]: ...
    @capabilities.setter
    def capabilities(
        self, value: pulumi.Input[Union[_builtins.str, TemplateDeploymentCapabilities]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preflightOptions")
    def preflight_options(
        self,
    ) -> pulumi.Input[Union[_builtins.str, TemplateDeploymentPreflightOptions]]: ...
    @preflight_options.setter
    def preflight_options(
        self,
        value: pulumi.Input[Union[_builtins.str, TemplateDeploymentPreflightOptions]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="preflightNotifications")
    def preflight_notifications(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, TemplateDeploymentPreflightNotifications]]
    ]: ...
    @preflight_notifications.setter
    def preflight_notifications(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, TemplateDeploymentPreflightNotifications]]
        ],
    ): ...

class ResourceTypeRegistrationPropertiesArgsDict(TypedDict):
    add_resource_list_target_locations: NotRequired[pulumi.Input[_builtins.bool]]
    additional_options: NotRequired[
        pulumi.Input[Union[_builtins.str, AdditionalOptionsResourceTypeRegistration]]
    ]
    allow_empty_role_assignments: NotRequired[pulumi.Input[_builtins.bool]]
    allowed_resource_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AllowedResourceNameArgsDict]]]
    ]
    allowed_template_deployment_reference_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    allowed_unauthorized_actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    allowed_unauthorized_actions_extensions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AllowedUnauthorizedActionsExtensionArgsDict]]
        ]
    ]
    api_profiles: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApiProfileArgsDict]]]]
    async_operation_resource_type_name: NotRequired[pulumi.Input[_builtins.str]]
    async_timeout_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AsyncTimeoutRuleArgsDict]]]
    ]
    authorization_action_mappings: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AuthorizationActionMappingArgsDict]]]
    ]
    availability_zone_rule: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesAvailabilityZoneRuleArgsDict]
    ]
    capacity_rule: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesCapacityRuleArgsDict]
    ]
    category: NotRequired[pulumi.Input[Union[_builtins.str, ResourceTypeCategory]]]
    check_name_availability_specifications: NotRequired[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesCheckNameAvailabilitySpecificationsArgsDict
        ]
    ]
    common_api_versions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    cross_tenant_token_validation: NotRequired[
        pulumi.Input[Union[_builtins.str, CrossTenantTokenValidation]]
    ]
    default_api_version: NotRequired[pulumi.Input[_builtins.str]]
    disallowed_action_verbs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    disallowed_end_user_operations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    dsts_configuration: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesDstsConfigurationArgsDict]
    ]
    enable_async_operation: NotRequired[pulumi.Input[_builtins.bool]]
    enable_third_party_s2_s: NotRequired[pulumi.Input[_builtins.bool]]
    endpoints: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ResourceTypeEndpointArgsDict]]]
    ]
    extended_locations: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ExtendedLocationOptionsArgsDict]]]
    ]
    extension_options: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesExtensionOptionsArgsDict]
    ]
    features_rule: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesFeaturesRuleArgsDict]
    ]
    frontdoor_request_mode: NotRequired[
        pulumi.Input[Union[_builtins.str, FrontdoorRequestMode]]
    ]
    grouping_tag: NotRequired[pulumi.Input[_builtins.str]]
    identity_management: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesIdentityManagementArgsDict]
    ]
    is_pure_proxy: NotRequired[pulumi.Input[_builtins.bool]]
    legacy_name: NotRequired[pulumi.Input[_builtins.str]]
    legacy_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    legacy_policy: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesLegacyPolicyArgsDict]
    ]
    linked_access_checks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LinkedAccessCheckArgsDict]]]
    ]
    linked_notification_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LinkedNotificationRuleArgsDict]]]
    ]
    linked_operation_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LinkedOperationRuleArgsDict]]]
    ]
    logging_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LoggingRuleArgsDict]]]
    ]
    management: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesManagementArgsDict]
    ]
    manifest_link: NotRequired[pulumi.Input[_builtins.str]]
    marketplace_options: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesMarketplaceOptionsArgsDict]
    ]
    marketplace_type: NotRequired[pulumi.Input[MarketplaceType]]
    metadata: NotRequired[Any]
    notifications: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NotificationArgsDict]]]
    ]
    on_behalf_of_tokens: NotRequired[pulumi.Input[ResourceTypeOnBehalfOfTokenArgsDict]]
    open_api_configuration: NotRequired[pulumi.Input[OpenApiConfigurationArgsDict]]
    policy_execution_type: NotRequired[
        pulumi.Input[Union[_builtins.str, PolicyExecutionType]]
    ]
    quota_rule: NotRequired[pulumi.Input[QuotaRuleArgsDict]]
    regionality: NotRequired[pulumi.Input[Union[_builtins.str, Regionality]]]
    request_header_options: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesRequestHeaderOptionsArgsDict]
    ]
    required_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_cache: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesResourceCacheArgsDict]
    ]
    resource_concurrency_control_options: NotRequired[
        pulumi.Input[
            Mapping[str, pulumi.Input[ResourceConcurrencyControlOptionArgsDict]]
        ]
    ]
    resource_deletion_policy: NotRequired[
        pulumi.Input[Union[_builtins.str, ResourceDeletionPolicy]]
    ]
    resource_graph_configuration: NotRequired[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesResourceGraphConfigurationArgsDict
        ]
    ]
    resource_management_options: NotRequired[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesResourceManagementOptionsArgsDict
        ]
    ]
    resource_move_policy: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesResourceMovePolicyArgsDict]
    ]
    resource_provider_authorization_rules: NotRequired[
        pulumi.Input[ResourceProviderAuthorizationRulesArgsDict]
    ]
    resource_query_management: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesResourceQueryManagementArgsDict]
    ]
    resource_sub_type: NotRequired[pulumi.Input[Union[_builtins.str, ResourceSubType]]]
    resource_type_common_attribute_management: NotRequired[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesResourceTypeCommonAttributeManagementArgsDict
        ]
    ]
    resource_validation: NotRequired[
        pulumi.Input[Union[_builtins.str, ResourceValidation]]
    ]
    routing_rule: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesRoutingRuleArgsDict]
    ]
    routing_type: NotRequired[pulumi.Input[Union[_builtins.str, RoutingType]]]
    service_tree_infos: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgsDict]]]
    ]
    sku_link: NotRequired[pulumi.Input[_builtins.str]]
    subscription_lifecycle_notification_specifications: NotRequired[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgsDict
        ]
    ]
    subscription_state_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SubscriptionStateRuleArgsDict]]]
    ]
    supports_tags: NotRequired[pulumi.Input[_builtins.bool]]
    swagger_specifications: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SwaggerSpecificationArgsDict]]]
    ]
    template_deployment_options: NotRequired[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesTemplateDeploymentOptionsArgsDict
        ]
    ]
    template_deployment_policy: NotRequired[
        pulumi.Input[ResourceTypeRegistrationPropertiesTemplateDeploymentPolicyArgsDict]
    ]
    throttling_rules: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ThrottlingRuleArgsDict]]]
    ]
    token_auth_configuration: NotRequired[pulumi.Input[TokenAuthConfigurationArgsDict]]

@pulumi.input_type
class ResourceTypeRegistrationPropertiesArgs:
    def __init__(
        __self__,
        *,
        add_resource_list_target_locations: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        additional_options: Optional[
            pulumi.Input[
                Union[_builtins.str, AdditionalOptionsResourceTypeRegistration]
            ]
        ] = ...,
        allow_empty_role_assignments: Optional[pulumi.Input[_builtins.bool]] = ...,
        allowed_resource_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[AllowedResourceNameArgs]]]
        ] = ...,
        allowed_template_deployment_reference_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_unauthorized_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        allowed_unauthorized_actions_extensions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AllowedUnauthorizedActionsExtensionArgs]]
            ]
        ] = ...,
        api_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApiProfileArgs]]]
        ] = ...,
        async_operation_resource_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
        async_timeout_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[AsyncTimeoutRuleArgs]]]
        ] = ...,
        authorization_action_mappings: Optional[
            pulumi.Input[Sequence[pulumi.Input[AuthorizationActionMappingArgs]]]
        ] = ...,
        availability_zone_rule: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesAvailabilityZoneRuleArgs]
        ] = ...,
        capacity_rule: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesCapacityRuleArgs]
        ] = ...,
        category: Optional[
            pulumi.Input[Union[_builtins.str, ResourceTypeCategory]]
        ] = ...,
        check_name_availability_specifications: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesCheckNameAvailabilitySpecificationsArgs
            ]
        ] = ...,
        common_api_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        cross_tenant_token_validation: Optional[
            pulumi.Input[Union[_builtins.str, CrossTenantTokenValidation]]
        ] = ...,
        default_api_version: Optional[pulumi.Input[_builtins.str]] = ...,
        disallowed_action_verbs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        disallowed_end_user_operations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dsts_configuration: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesDstsConfigurationArgs]
        ] = ...,
        enable_async_operation: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_third_party_s2_s: Optional[pulumi.Input[_builtins.bool]] = ...,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ResourceTypeEndpointArgs]]]
        ] = ...,
        extended_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExtendedLocationOptionsArgs]]]
        ] = ...,
        extension_options: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesExtensionOptionsArgs]
        ] = ...,
        features_rule: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesFeaturesRuleArgs]
        ] = ...,
        frontdoor_request_mode: Optional[
            pulumi.Input[Union[_builtins.str, FrontdoorRequestMode]]
        ] = ...,
        grouping_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_management: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesIdentityManagementArgs]
        ] = ...,
        is_pure_proxy: Optional[pulumi.Input[_builtins.bool]] = ...,
        legacy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        legacy_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        legacy_policy: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesLegacyPolicyArgs]
        ] = ...,
        linked_access_checks: Optional[
            pulumi.Input[Sequence[pulumi.Input[LinkedAccessCheckArgs]]]
        ] = ...,
        linked_notification_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[LinkedNotificationRuleArgs]]]
        ] = ...,
        linked_operation_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[LinkedOperationRuleArgs]]]
        ] = ...,
        logging_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoggingRuleArgs]]]
        ] = ...,
        management: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesManagementArgs]
        ] = ...,
        manifest_link: Optional[pulumi.Input[_builtins.str]] = ...,
        marketplace_options: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesMarketplaceOptionsArgs]
        ] = ...,
        marketplace_type: Optional[pulumi.Input[MarketplaceType]] = ...,
        metadata: Optional[Any] = ...,
        notifications: Optional[
            pulumi.Input[Sequence[pulumi.Input[NotificationArgs]]]
        ] = ...,
        on_behalf_of_tokens: Optional[
            pulumi.Input[ResourceTypeOnBehalfOfTokenArgs]
        ] = ...,
        open_api_configuration: Optional[pulumi.Input[OpenApiConfigurationArgs]] = ...,
        policy_execution_type: Optional[
            pulumi.Input[Union[_builtins.str, PolicyExecutionType]]
        ] = ...,
        quota_rule: Optional[pulumi.Input[QuotaRuleArgs]] = ...,
        regionality: Optional[pulumi.Input[Union[_builtins.str, Regionality]]] = ...,
        request_header_options: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesRequestHeaderOptionsArgs]
        ] = ...,
        required_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_cache: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesResourceCacheArgs]
        ] = ...,
        resource_concurrency_control_options: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[ResourceConcurrencyControlOptionArgs]]
            ]
        ] = ...,
        resource_deletion_policy: Optional[
            pulumi.Input[Union[_builtins.str, ResourceDeletionPolicy]]
        ] = ...,
        resource_graph_configuration: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceGraphConfigurationArgs
            ]
        ] = ...,
        resource_management_options: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceManagementOptionsArgs
            ]
        ] = ...,
        resource_move_policy: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesResourceMovePolicyArgs]
        ] = ...,
        resource_provider_authorization_rules: Optional[
            pulumi.Input[ResourceProviderAuthorizationRulesArgs]
        ] = ...,
        resource_query_management: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesResourceQueryManagementArgs]
        ] = ...,
        resource_sub_type: Optional[
            pulumi.Input[Union[_builtins.str, ResourceSubType]]
        ] = ...,
        resource_type_common_attribute_management: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceTypeCommonAttributeManagementArgs
            ]
        ] = ...,
        resource_validation: Optional[
            pulumi.Input[Union[_builtins.str, ResourceValidation]]
        ] = ...,
        routing_rule: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesRoutingRuleArgs]
        ] = ...,
        routing_type: Optional[pulumi.Input[Union[_builtins.str, RoutingType]]] = ...,
        service_tree_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgs]]]
        ] = ...,
        sku_link: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_lifecycle_notification_specifications: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgs
            ]
        ] = ...,
        subscription_state_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionStateRuleArgs]]]
        ] = ...,
        supports_tags: Optional[pulumi.Input[_builtins.bool]] = ...,
        swagger_specifications: Optional[
            pulumi.Input[Sequence[pulumi.Input[SwaggerSpecificationArgs]]]
        ] = ...,
        template_deployment_options: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesTemplateDeploymentOptionsArgs
            ]
        ] = ...,
        template_deployment_policy: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesTemplateDeploymentPolicyArgs]
        ] = ...,
        throttling_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[ThrottlingRuleArgs]]]
        ] = ...,
        token_auth_configuration: Optional[
            pulumi.Input[TokenAuthConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addResourceListTargetLocations")
    def add_resource_list_target_locations(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @add_resource_list_target_locations.setter
    def add_resource_list_target_locations(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalOptions")
    def additional_options(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, AdditionalOptionsResourceTypeRegistration]]
    ]: ...
    @additional_options.setter
    def additional_options(
        self,
        value: Optional[
            pulumi.Input[
                Union[_builtins.str, AdditionalOptionsResourceTypeRegistration]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowEmptyRoleAssignments")
    def allow_empty_role_assignments(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_empty_role_assignments.setter
    def allow_empty_role_assignments(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedResourceNames")
    def allowed_resource_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AllowedResourceNameArgs]]]]: ...
    @allowed_resource_names.setter
    def allowed_resource_names(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AllowedResourceNameArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedTemplateDeploymentReferenceActions")
    def allowed_template_deployment_reference_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_template_deployment_reference_actions.setter
    def allowed_template_deployment_reference_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedUnauthorizedActions")
    def allowed_unauthorized_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_unauthorized_actions.setter
    def allowed_unauthorized_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedUnauthorizedActionsExtensions")
    def allowed_unauthorized_actions_extensions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AllowedUnauthorizedActionsExtensionArgs]]]
    ]: ...
    @allowed_unauthorized_actions_extensions.setter
    def allowed_unauthorized_actions_extensions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AllowedUnauthorizedActionsExtensionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="apiProfiles")
    def api_profiles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApiProfileArgs]]]]: ...
    @api_profiles.setter
    def api_profiles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApiProfileArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="asyncOperationResourceTypeName")
    def async_operation_resource_type_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @async_operation_resource_type_name.setter
    def async_operation_resource_type_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="asyncTimeoutRules")
    def async_timeout_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AsyncTimeoutRuleArgs]]]]: ...
    @async_timeout_rules.setter
    def async_timeout_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AsyncTimeoutRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="authorizationActionMappings")
    def authorization_action_mappings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AuthorizationActionMappingArgs]]]
    ]: ...
    @authorization_action_mappings.setter
    def authorization_action_mappings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AuthorizationActionMappingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRule")
    def availability_zone_rule(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesAvailabilityZoneRuleArgs]
    ]: ...
    @availability_zone_rule.setter
    def availability_zone_rule(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesAvailabilityZoneRuleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="capacityRule")
    def capacity_rule(
        self,
    ) -> Optional[pulumi.Input[ResourceTypeRegistrationPropertiesCapacityRuleArgs]]: ...
    @capacity_rule.setter
    def capacity_rule(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesCapacityRuleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def category(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceTypeCategory]]]: ...
    @category.setter
    def category(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceTypeCategory]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="checkNameAvailabilitySpecifications")
    def check_name_availability_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesCheckNameAvailabilitySpecificationsArgs
        ]
    ]: ...
    @check_name_availability_specifications.setter
    def check_name_availability_specifications(
        self,
        value: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesCheckNameAvailabilitySpecificationsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="commonApiVersions")
    def common_api_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @common_api_versions.setter
    def common_api_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="crossTenantTokenValidation")
    def cross_tenant_token_validation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, CrossTenantTokenValidation]]]: ...
    @cross_tenant_token_validation.setter
    def cross_tenant_token_validation(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, CrossTenantTokenValidation]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultApiVersion")
    def default_api_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_api_version.setter
    def default_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disallowedActionVerbs")
    def disallowed_action_verbs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @disallowed_action_verbs.setter
    def disallowed_action_verbs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disallowedEndUserOperations")
    def disallowed_end_user_operations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @disallowed_end_user_operations.setter
    def disallowed_end_user_operations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dstsConfiguration")
    def dsts_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesDstsConfigurationArgs]
    ]: ...
    @dsts_configuration.setter
    def dsts_configuration(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesDstsConfigurationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAsyncOperation")
    def enable_async_operation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_async_operation.setter
    def enable_async_operation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableThirdPartyS2S")
    def enable_third_party_s2_s(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_third_party_s2_s.setter
    def enable_third_party_s2_s(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceTypeEndpointArgs]]]]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceTypeEndpointArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocations")
    def extended_locations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ExtendedLocationOptionsArgs]]]
    ]: ...
    @extended_locations.setter
    def extended_locations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExtendedLocationOptionsArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="extensionOptions")
    def extension_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesExtensionOptionsArgs]
    ]: ...
    @extension_options.setter
    def extension_options(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesExtensionOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="featuresRule")
    def features_rule(
        self,
    ) -> Optional[pulumi.Input[ResourceTypeRegistrationPropertiesFeaturesRuleArgs]]: ...
    @features_rule.setter
    def features_rule(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesFeaturesRuleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="frontdoorRequestMode")
    def frontdoor_request_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FrontdoorRequestMode]]]: ...
    @frontdoor_request_mode.setter
    def frontdoor_request_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FrontdoorRequestMode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="groupingTag")
    def grouping_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grouping_tag.setter
    def grouping_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityManagement")
    def identity_management(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesIdentityManagementArgs]
    ]: ...
    @identity_management.setter
    def identity_management(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesIdentityManagementArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="isPureProxy")
    def is_pure_proxy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_pure_proxy.setter
    def is_pure_proxy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="legacyName")
    def legacy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @legacy_name.setter
    def legacy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="legacyNames")
    def legacy_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @legacy_names.setter
    def legacy_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="legacyPolicy")
    def legacy_policy(
        self,
    ) -> Optional[pulumi.Input[ResourceTypeRegistrationPropertiesLegacyPolicyArgs]]: ...
    @legacy_policy.setter
    def legacy_policy(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesLegacyPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedAccessChecks")
    def linked_access_checks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LinkedAccessCheckArgs]]]]: ...
    @linked_access_checks.setter
    def linked_access_checks(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LinkedAccessCheckArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedNotificationRules")
    def linked_notification_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LinkedNotificationRuleArgs]]]]: ...
    @linked_notification_rules.setter
    def linked_notification_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LinkedNotificationRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedOperationRules")
    def linked_operation_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LinkedOperationRuleArgs]]]]: ...
    @linked_operation_rules.setter
    def linked_operation_rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[LinkedOperationRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingRules")
    def logging_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[LoggingRuleArgs]]]]: ...
    @logging_rules.setter
    def logging_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LoggingRuleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def management(
        self,
    ) -> Optional[pulumi.Input[ResourceTypeRegistrationPropertiesManagementArgs]]: ...
    @management.setter
    def management(
        self,
        value: Optional[pulumi.Input[ResourceTypeRegistrationPropertiesManagementArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="manifestLink")
    def manifest_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manifest_link.setter
    def manifest_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="marketplaceOptions")
    def marketplace_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesMarketplaceOptionsArgs]
    ]: ...
    @marketplace_options.setter
    def marketplace_options(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesMarketplaceOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="marketplaceType")
    def marketplace_type(self) -> Optional[pulumi.Input[MarketplaceType]]: ...
    @marketplace_type.setter
    def marketplace_type(self, value: Optional[pulumi.Input[MarketplaceType]]): ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @metadata.setter
    def metadata(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def notifications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NotificationArgs]]]]: ...
    @notifications.setter
    def notifications(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NotificationArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onBehalfOfTokens")
    def on_behalf_of_tokens(
        self,
    ) -> Optional[pulumi.Input[ResourceTypeOnBehalfOfTokenArgs]]: ...
    @on_behalf_of_tokens.setter
    def on_behalf_of_tokens(
        self, value: Optional[pulumi.Input[ResourceTypeOnBehalfOfTokenArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="openApiConfiguration")
    def open_api_configuration(
        self,
    ) -> Optional[pulumi.Input[OpenApiConfigurationArgs]]: ...
    @open_api_configuration.setter
    def open_api_configuration(
        self, value: Optional[pulumi.Input[OpenApiConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyExecutionType")
    def policy_execution_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PolicyExecutionType]]]: ...
    @policy_execution_type.setter
    def policy_execution_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PolicyExecutionType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="quotaRule")
    def quota_rule(self) -> Optional[pulumi.Input[QuotaRuleArgs]]: ...
    @quota_rule.setter
    def quota_rule(self, value: Optional[pulumi.Input[QuotaRuleArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def regionality(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, Regionality]]]: ...
    @regionality.setter
    def regionality(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Regionality]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderOptions")
    def request_header_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesRequestHeaderOptionsArgs]
    ]: ...
    @request_header_options.setter
    def request_header_options(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesRequestHeaderOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_features.setter
    def required_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceCache")
    def resource_cache(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesResourceCacheArgs]
    ]: ...
    @resource_cache.setter
    def resource_cache(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesResourceCacheArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceConcurrencyControlOptions")
    def resource_concurrency_control_options(
        self,
    ) -> Optional[
        pulumi.Input[Mapping[str, pulumi.Input[ResourceConcurrencyControlOptionArgs]]]
    ]: ...
    @resource_concurrency_control_options.setter
    def resource_concurrency_control_options(
        self,
        value: Optional[
            pulumi.Input[
                Mapping[str, pulumi.Input[ResourceConcurrencyControlOptionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceDeletionPolicy")
    def resource_deletion_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceDeletionPolicy]]]: ...
    @resource_deletion_policy.setter
    def resource_deletion_policy(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ResourceDeletionPolicy]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceGraphConfiguration")
    def resource_graph_configuration(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesResourceGraphConfigurationArgs]
    ]: ...
    @resource_graph_configuration.setter
    def resource_graph_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceGraphConfigurationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceManagementOptions")
    def resource_management_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesResourceManagementOptionsArgs]
    ]: ...
    @resource_management_options.setter
    def resource_management_options(
        self,
        value: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceManagementOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceMovePolicy")
    def resource_move_policy(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesResourceMovePolicyArgs]
    ]: ...
    @resource_move_policy.setter
    def resource_move_policy(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesResourceMovePolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderAuthorizationRules")
    def resource_provider_authorization_rules(
        self,
    ) -> Optional[pulumi.Input[ResourceProviderAuthorizationRulesArgs]]: ...
    @resource_provider_authorization_rules.setter
    def resource_provider_authorization_rules(
        self, value: Optional[pulumi.Input[ResourceProviderAuthorizationRulesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceQueryManagement")
    def resource_query_management(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesResourceQueryManagementArgs]
    ]: ...
    @resource_query_management.setter
    def resource_query_management(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesResourceQueryManagementArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceSubType")
    def resource_sub_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceSubType]]]: ...
    @resource_sub_type.setter
    def resource_sub_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceSubType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeCommonAttributeManagement")
    def resource_type_common_attribute_management(
        self,
    ) -> Optional[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesResourceTypeCommonAttributeManagementArgs
        ]
    ]: ...
    @resource_type_common_attribute_management.setter
    def resource_type_common_attribute_management(
        self,
        value: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesResourceTypeCommonAttributeManagementArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceValidation")
    def resource_validation(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceValidation]]]: ...
    @resource_validation.setter
    def resource_validation(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ResourceValidation]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingRule")
    def routing_rule(
        self,
    ) -> Optional[pulumi.Input[ResourceTypeRegistrationPropertiesRoutingRuleArgs]]: ...
    @routing_rule.setter
    def routing_rule(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesRoutingRuleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="routingType")
    def routing_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, RoutingType]]]: ...
    @routing_type.setter
    def routing_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, RoutingType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceTreeInfos")
    def service_tree_infos(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgs]]]]: ...
    @service_tree_infos.setter
    def service_tree_infos(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTreeInfoArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skuLink")
    def sku_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku_link.setter
    def sku_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionLifecycleNotificationSpecifications")
    def subscription_lifecycle_notification_specifications(
        self,
    ) -> Optional[
        pulumi.Input[
            ResourceTypeRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgs
        ]
    ]: ...
    @subscription_lifecycle_notification_specifications.setter
    def subscription_lifecycle_notification_specifications(
        self,
        value: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionStateRules")
    def subscription_state_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SubscriptionStateRuleArgs]]]]: ...
    @subscription_state_rules.setter
    def subscription_state_rules(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SubscriptionStateRuleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportsTags")
    def supports_tags(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @supports_tags.setter
    def supports_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="swaggerSpecifications")
    def swagger_specifications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SwaggerSpecificationArgs]]]]: ...
    @swagger_specifications.setter
    def swagger_specifications(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SwaggerSpecificationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateDeploymentOptions")
    def template_deployment_options(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesTemplateDeploymentOptionsArgs]
    ]: ...
    @template_deployment_options.setter
    def template_deployment_options(
        self,
        value: Optional[
            pulumi.Input[
                ResourceTypeRegistrationPropertiesTemplateDeploymentOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="templateDeploymentPolicy")
    def template_deployment_policy(
        self,
    ) -> Optional[
        pulumi.Input[ResourceTypeRegistrationPropertiesTemplateDeploymentPolicyArgs]
    ]: ...
    @template_deployment_policy.setter
    def template_deployment_policy(
        self,
        value: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesTemplateDeploymentPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="throttlingRules")
    def throttling_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ThrottlingRuleArgs]]]]: ...
    @throttling_rules.setter
    def throttling_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ThrottlingRuleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenAuthConfiguration")
    def token_auth_configuration(
        self,
    ) -> Optional[pulumi.Input[TokenAuthConfigurationArgs]]: ...
    @token_auth_configuration.setter
    def token_auth_configuration(
        self, value: Optional[pulumi.Input[TokenAuthConfigurationArgs]]
    ): ...

class ResourceTypeRegistrationArgsDict(TypedDict):
    kind: NotRequired[pulumi.Input[Union[_builtins.str, ResourceTypeRegistrationKind]]]
    properties: NotRequired[pulumi.Input[ResourceTypeRegistrationPropertiesArgsDict]]

@pulumi.input_type
class ResourceTypeRegistrationArgs:
    def __init__(
        __self__,
        *,
        kind: Optional[
            pulumi.Input[Union[_builtins.str, ResourceTypeRegistrationKind]]
        ] = ...,
        properties: Optional[
            pulumi.Input[ResourceTypeRegistrationPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ResourceTypeRegistrationKind]]]: ...
    @kind.setter
    def kind(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ResourceTypeRegistrationKind]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[ResourceTypeRegistrationPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[ResourceTypeRegistrationPropertiesArgs]]
    ): ...

class ServiceTreeInfoArgsDict(TypedDict):
    component_id: NotRequired[pulumi.Input[_builtins.str]]
    readiness: NotRequired[pulumi.Input[Union[_builtins.str, Readiness]]]
    service_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTreeInfoArgs:
    def __init__(
        __self__,
        *,
        component_id: Optional[pulumi.Input[_builtins.str]] = ...,
        readiness: Optional[pulumi.Input[Union[_builtins.str, Readiness]]] = ...,
        service_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @component_id.setter
    def component_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def readiness(self) -> Optional[pulumi.Input[Union[_builtins.str, Readiness]]]: ...
    @readiness.setter
    def readiness(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Readiness]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_id.setter
    def service_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SkuCapabilityArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class SkuCapabilityArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class SkuCostArgsDict(TypedDict):
    meter_id: pulumi.Input[_builtins.str]
    extended_unit: NotRequired[pulumi.Input[_builtins.str]]
    quantity: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class SkuCostArgs:
    def __init__(
        __self__,
        *,
        meter_id: pulumi.Input[_builtins.str],
        extended_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        quantity: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="meterId")
    def meter_id(self) -> pulumi.Input[_builtins.str]: ...
    @meter_id.setter
    def meter_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="extendedUnit")
    def extended_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extended_unit.setter
    def extended_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @quantity.setter
    def quantity(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class SkuLocationInfoArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    extended_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]]
    zone_details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SkuZoneDetailArgsDict]]]
    ]
    zones: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SkuLocationInfoArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        extended_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        type: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]] = ...,
        zone_details: Optional[
            pulumi.Input[Sequence[pulumi.Input[SkuZoneDetailArgs]]]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocations")
    def extended_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @extended_locations.setter
    def extended_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]]: ...
    @type.setter
    def type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ExtendedLocationType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="zoneDetails")
    def zone_details(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SkuZoneDetailArgs]]]]: ...
    @zone_details.setter
    def zone_details(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SkuZoneDetailArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SkuResourcePropertiesArgsDict(TypedDict):
    sku_settings: pulumi.Input[Sequence[pulumi.Input[SkuSettingArgsDict]]]

@pulumi.input_type
class SkuResourcePropertiesArgs:
    def __init__(
        __self__, *, sku_settings: pulumi.Input[Sequence[pulumi.Input[SkuSettingArgs]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="skuSettings")
    def sku_settings(self) -> pulumi.Input[Sequence[pulumi.Input[SkuSettingArgs]]]: ...
    @sku_settings.setter
    def sku_settings(
        self, value: pulumi.Input[Sequence[pulumi.Input[SkuSettingArgs]]]
    ): ...

class SkuSettingCapacityArgsDict(TypedDict):
    minimum: pulumi.Input[_builtins.int]
    default: NotRequired[pulumi.Input[_builtins.int]]
    maximum: NotRequired[pulumi.Input[_builtins.int]]
    scale_type: NotRequired[pulumi.Input[Union[_builtins.str, SkuScaleType]]]

@pulumi.input_type
class SkuSettingCapacityArgs:
    def __init__(
        __self__,
        *,
        minimum: pulumi.Input[_builtins.int],
        default: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum: Optional[pulumi.Input[_builtins.int]] = ...,
        scale_type: Optional[pulumi.Input[Union[_builtins.str, SkuScaleType]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> pulumi.Input[_builtins.int]: ...
    @minimum.setter
    def minimum(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default.setter
    def default(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum.setter
    def maximum(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scaleType")
    def scale_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SkuScaleType]]]: ...
    @scale_type.setter
    def scale_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SkuScaleType]]]
    ): ...

class SkuSettingArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    capabilities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SkuCapabilityArgsDict]]]
    ]
    capacity: NotRequired[pulumi.Input[SkuSettingCapacityArgsDict]]
    costs: NotRequired[pulumi.Input[Sequence[pulumi.Input[SkuCostArgsDict]]]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    kind: NotRequired[pulumi.Input[_builtins.str]]
    location_info: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SkuLocationInfoArgsDict]]]
    ]
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    required_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    required_quota_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SkuSettingArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[SkuCapabilityArgs]]]
        ] = ...,
        capacity: Optional[pulumi.Input[SkuSettingCapacityArgs]] = ...,
        costs: Optional[pulumi.Input[Sequence[pulumi.Input[SkuCostArgs]]]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location_info: Optional[
            pulumi.Input[Sequence[pulumi.Input[SkuLocationInfoArgs]]]
        ] = ...,
        locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        required_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        required_quota_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        size: Optional[pulumi.Input[_builtins.str]] = ...,
        tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SkuCapabilityArgs]]]]: ...
    @capabilities.setter
    def capabilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SkuCapabilityArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[SkuSettingCapacityArgs]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[SkuSettingCapacityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def costs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SkuCostArgs]]]]: ...
    @costs.setter
    def costs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SkuCostArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="locationInfo")
    def location_info(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SkuLocationInfoArgs]]]]: ...
    @location_info.setter
    def location_info(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SkuLocationInfoArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @locations.setter
    def locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_features.setter
    def required_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredQuotaIds")
    def required_quota_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_quota_ids.setter
    def required_quota_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SkuZoneDetailArgsDict(TypedDict):
    capabilities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[SkuCapabilityArgsDict]]]
    ]
    name: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SkuZoneDetailArgs:
    def __init__(
        __self__,
        *,
        capabilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[SkuCapabilityArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SkuCapabilityArgs]]]]: ...
    @capabilities.setter
    def capabilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SkuCapabilityArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @name.setter
    def name(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SubscriberSettingArgsDict(TypedDict):
    filter_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input[FilterRuleArgsDict]]]]

@pulumi.input_type
class SubscriberSettingArgs:
    def __init__(
        __self__,
        *,
        filter_rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterRuleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterRules")
    def filter_rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FilterRuleArgs]]]]: ...
    @filter_rules.setter
    def filter_rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FilterRuleArgs]]]]
    ): ...

class SubscriptionStateOverrideActionArgsDict(TypedDict):
    action: pulumi.Input[Union[_builtins.str, SubscriptionNotificationOperation]]
    state: pulumi.Input[Union[_builtins.str, SubscriptionTransitioningState]]

@pulumi.input_type
class SubscriptionStateOverrideActionArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[Union[_builtins.str, SubscriptionNotificationOperation]],
        state: pulumi.Input[Union[_builtins.str, SubscriptionTransitioningState]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SubscriptionNotificationOperation]]: ...
    @action.setter
    def action(
        self,
        value: pulumi.Input[Union[_builtins.str, SubscriptionNotificationOperation]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> pulumi.Input[Union[_builtins.str, SubscriptionTransitioningState]]: ...
    @state.setter
    def state(
        self, value: pulumi.Input[Union[_builtins.str, SubscriptionTransitioningState]]
    ): ...

class SubscriptionStateRuleArgsDict(TypedDict):
    allowed_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, SubscriptionState]]]

@pulumi.input_type
class SubscriptionStateRuleArgs:
    def __init__(
        __self__,
        *,
        allowed_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        state: Optional[pulumi.Input[Union[_builtins.str, SubscriptionState]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedActions")
    def allowed_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_actions.setter
    def allowed_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SubscriptionState]]]: ...
    @state.setter
    def state(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SubscriptionState]]]
    ): ...

class SwaggerSpecificationArgsDict(TypedDict):
    api_versions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    swagger_spec_folder_uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SwaggerSpecificationArgs:
    def __init__(
        __self__,
        *,
        api_versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        swagger_spec_folder_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersions")
    def api_versions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @api_versions.setter
    def api_versions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="swaggerSpecFolderUri")
    def swagger_spec_folder_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @swagger_spec_folder_uri.setter
    def swagger_spec_folder_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ThirdPartyExtensionArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ThirdPartyExtensionArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ThrottlingMetricArgsDict(TypedDict):
    limit: pulumi.Input[_builtins.float]
    type: pulumi.Input[Union[_builtins.str, ThrottlingMetricType]]
    interval: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ThrottlingMetricArgs:
    def __init__(
        __self__,
        *,
        limit: pulumi.Input[_builtins.float],
        type: pulumi.Input[Union[_builtins.str, ThrottlingMetricType]],
        interval: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limit(self) -> pulumi.Input[_builtins.float]: ...
    @limit.setter
    def limit(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ThrottlingMetricType]]: ...
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ThrottlingMetricType]]): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ThrottlingRuleArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    metrics: pulumi.Input[Sequence[pulumi.Input[ThrottlingMetricArgsDict]]]
    application_id: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    required_features: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ThrottlingRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        metrics: pulumi.Input[Sequence[pulumi.Input[ThrottlingMetricArgs]]],
        application_id: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        required_features: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> pulumi.Input[Sequence[pulumi.Input[ThrottlingMetricArgs]]]: ...
    @metrics.setter
    def metrics(
        self, value: pulumi.Input[Sequence[pulumi.Input[ThrottlingMetricArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @application_id.setter
    def application_id(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_features.setter
    def required_features(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class TokenAuthConfigurationArgsDict(TypedDict):
    authentication_scheme: NotRequired[
        pulumi.Input[Union[_builtins.str, AuthenticationScheme]]
    ]
    disable_certificate_authentication_fallback: NotRequired[
        pulumi.Input[_builtins.bool]
    ]
    signed_request_scope: NotRequired[
        pulumi.Input[Union[_builtins.str, SignedRequestScope]]
    ]

@pulumi.input_type
class TokenAuthConfigurationArgs:
    def __init__(
        __self__,
        *,
        authentication_scheme: Optional[
            pulumi.Input[Union[_builtins.str, AuthenticationScheme]]
        ] = ...,
        disable_certificate_authentication_fallback: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        signed_request_scope: Optional[
            pulumi.Input[Union[_builtins.str, SignedRequestScope]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationScheme")
    def authentication_scheme(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, AuthenticationScheme]]]: ...
    @authentication_scheme.setter
    def authentication_scheme(
        self, value: Optional[pulumi.Input[Union[_builtins.str, AuthenticationScheme]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableCertificateAuthenticationFallback")
    def disable_certificate_authentication_fallback(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_certificate_authentication_fallback.setter
    def disable_certificate_authentication_fallback(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="signedRequestScope")
    def signed_request_scope(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, SignedRequestScope]]]: ...
    @signed_request_scope.setter
    def signed_request_scope(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SignedRequestScope]]]
    ): ...

class TypedErrorInfoArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class TypedErrorInfoArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
