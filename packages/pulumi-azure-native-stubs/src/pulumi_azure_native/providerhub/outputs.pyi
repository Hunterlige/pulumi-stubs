import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AdditionalAuthorizationResponse",
    "AllowedResourceNameResponse",
    "AllowedUnauthorizedActionsExtensionResponse",
    "ApiProfileResponse",
    "ApplicationDataAuthorizationResponse",
    "ApplicationProviderAuthorizationResponse",
    "AsyncOperationPollingRulesResponse",
    "AsyncTimeoutRuleResponse",
    "AuthorizationActionMappingResponse",
    "AuthorizedApplicationPropertiesResponse",
    "CustomRolloutPropertiesResponse",
    "CustomRolloutPropertiesSpecificationResponse",
    "CustomRolloutPropertiesStatusResponse",
    ...,
    "CustomRolloutSpecificationCanaryResponse",
    ...,
    "CustomRolloutStatusManifestCheckinStatusResponse",
    "DefaultRolloutPropertiesResponse",
    "DefaultRolloutPropertiesSpecificationResponse",
    "DefaultRolloutPropertiesStatusResponse",
    ...,
    "DefaultRolloutSpecificationCanaryResponse",
    ...,
    "DefaultRolloutSpecificationHighTrafficResponse",
    "DefaultRolloutSpecificationLowTrafficResponse",
    "DefaultRolloutSpecificationMediumTrafficResponse",
    ...,
    ...,
    ...,
    "DefaultRolloutStatusManifestCheckinStatusResponse",
    "DeleteDependencyResponse",
    "EndpointInformationResponse",
    "ExtendedErrorInfoResponse",
    "ExtendedLocationOptionsResponse",
    ...,
    "FanoutLinkedNotificationRuleResponse",
    "FilterRuleResponse",
    "LegacyDisallowedConditionResponse",
    "LightHouseAuthorizationResponse",
    "LinkedAccessCheckResponse",
    "LinkedNotificationRuleResponse",
    "LinkedOperationRuleResponse",
    "LocationQuotaRuleResponse",
    "LoggingRuleHiddenPropertyPathsResponse",
    "LoggingRuleResponse",
    "NotificationEndpointResponse",
    "NotificationRegistrationPropertiesResponse",
    "NotificationResponse",
    "OpenApiConfigurationResponse",
    "OpenApiValidationResponse",
    "ProviderHubMetadataProviderAuthenticationResponse",
    ...,
    "ProviderMonitorSettingPropertiesResponse",
    ...,
    ...,
    "ProviderRegistrationPropertiesResponse",
    ...,
    "QuotaRuleResponse",
    "ResourceAccessRoleResponse",
    "ResourceConcurrencyControlOptionResponse",
    "ResourceHydrationAccountResponse",
    ...,
    "ResourceProviderAuthorizationResponse",
    "ResourceProviderAuthorizationRulesResponse",
    "ResourceProviderCapabilitiesResponse",
    "ResourceProviderEndpointFeaturesRuleResponse",
    "ResourceProviderEndpointResponse",
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
    "ResourceProviderServiceResponse",
    "ResourceTypeEndpointDstsConfigurationResponse",
    "ResourceTypeEndpointFeaturesRuleResponse",
    "ResourceTypeEndpointResponse",
    ...,
    "ResourceTypeExtensionResponse",
    "ResourceTypeOnBehalfOfTokenResponse",
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
    "ResourceTypeRegistrationPropertiesResponse",
    ...,
    ...,
    ...,
    ...,
    "ResourceTypeRegistrationResponse",
    "ServiceTreeInfoResponse",
    "SkuCapabilityResponse",
    "SkuCostResponse",
    "SkuLocationInfoResponse",
    "SkuResourcePropertiesResponse",
    "SkuSettingCapacityResponse",
    "SkuSettingResponse",
    "SkuZoneDetailResponse",
    "SubscriberSettingResponse",
    "SubscriptionStateOverrideActionResponse",
    "SubscriptionStateRuleResponse",
    "SwaggerSpecificationResponse",
    "SystemDataResponse",
    "ThirdPartyExtensionResponse",
    "ThrottlingMetricResponse",
    "ThrottlingRuleResponse",
    "TokenAuthConfigurationResponse",
    "TypedErrorInfoResponse",
]

@pulumi.output_type
class AdditionalAuthorizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_id: Optional[_builtins.str] = ...,
        role_definition_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AllowedResourceNameResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        get_action_verb: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="getActionVerb")
    def get_action_verb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AllowedUnauthorizedActionsExtensionResponse(dict):
    def __init__(
        __self__,
        *,
        action: Optional[_builtins.str] = ...,
        intent: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApiProfileResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_version: Optional[_builtins.str] = ...,
        profile_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationDataAuthorizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        role: _builtins.str,
        resource_types: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ApplicationProviderAuthorizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        managed_by_role_definition_id: Optional[_builtins.str] = ...,
        role_definition_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="managedByRoleDefinitionId")
    def managed_by_role_definition_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AsyncOperationPollingRulesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_options: Optional[_builtins.str] = ...,
        authorization_actions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalOptions")
    def additional_options(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationActions")
    def authorization_actions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class AsyncTimeoutRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_name: Optional[_builtins.str] = ...,
        timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AuthorizationActionMappingResponse(dict):
    def __init__(
        __self__,
        *,
        desired: Optional[_builtins.str] = ...,
        original: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def desired(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def original(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AuthorizedApplicationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        data_authorizations: Optional[
            Sequence[outputs.ApplicationDataAuthorizationResponse]
        ] = ...,
        provider_authorization: Optional[
            outputs.ApplicationProviderAuthorizationResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataAuthorizations")
    def data_authorizations(
        self,
    ) -> Optional[Sequence[outputs.ApplicationDataAuthorizationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="providerAuthorization")
    def provider_authorization(
        self,
    ) -> Optional[outputs.ApplicationProviderAuthorizationResponse]: ...

@pulumi.output_type
class CustomRolloutPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        specification: outputs.CustomRolloutPropertiesSpecificationResponse,
        status: Optional[outputs.CustomRolloutPropertiesStatusResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def specification(self) -> outputs.CustomRolloutPropertiesSpecificationResponse: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.CustomRolloutPropertiesStatusResponse]: ...

@pulumi.output_type
class CustomRolloutPropertiesSpecificationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_provision_config: Optional[
            outputs.CustomRolloutSpecificationAutoProvisionConfigResponse
        ] = ...,
        canary: Optional[outputs.CustomRolloutSpecificationCanaryResponse] = ...,
        provider_registration: Optional[
            outputs.CustomRolloutSpecificationProviderRegistrationResponse
        ] = ...,
        refresh_subscription_registration: Optional[_builtins.bool] = ...,
        release_scopes: Optional[Sequence[_builtins.str]] = ...,
        resource_type_registrations: Optional[
            Sequence[outputs.ResourceTypeRegistrationResponse]
        ] = ...,
        skip_release_scope_validation: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisionConfig")
    def auto_provision_config(
        self,
    ) -> Optional[outputs.CustomRolloutSpecificationAutoProvisionConfigResponse]: ...
    @_builtins.property
    @pulumi.getter
    def canary(self) -> Optional[outputs.CustomRolloutSpecificationCanaryResponse]: ...
    @_builtins.property
    @pulumi.getter(name="providerRegistration")
    def provider_registration(
        self,
    ) -> Optional[outputs.CustomRolloutSpecificationProviderRegistrationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="refreshSubscriptionRegistration")
    def refresh_subscription_registration(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="releaseScopes")
    def release_scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeRegistrations")
    def resource_type_registrations(
        self,
    ) -> Optional[Sequence[outputs.ResourceTypeRegistrationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="skipReleaseScopeValidation")
    def skip_release_scope_validation(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CustomRolloutPropertiesStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        completed_regions: Optional[Sequence[_builtins.str]] = ...,
        failed_or_skipped_regions: Optional[
            Mapping[str, outputs.ExtendedErrorInfoResponse]
        ] = ...,
        manifest_checkin_status: Optional[
            outputs.CustomRolloutStatusManifestCheckinStatusResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completedRegions")
    def completed_regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="failedOrSkippedRegions")
    def failed_or_skipped_regions(
        self,
    ) -> Optional[Mapping[str, outputs.ExtendedErrorInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="manifestCheckinStatus")
    def manifest_checkin_status(
        self,
    ) -> Optional[outputs.CustomRolloutStatusManifestCheckinStatusResponse]: ...

@pulumi.output_type
class CustomRolloutSpecificationAutoProvisionConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_graph: Optional[_builtins.bool] = ...,
        storage: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGraph")
    def resource_graph(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CustomRolloutSpecificationCanaryResponse(dict):
    def __init__(
        __self__, *, regions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CustomRolloutSpecificationProviderRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        kind: Optional[_builtins.str] = ...,
        properties: Optional[outputs.ProviderRegistrationPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[outputs.ProviderRegistrationPropertiesResponse]: ...

@pulumi.output_type
class CustomRolloutStatusManifestCheckinStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_checked_in: _builtins.bool,
        status_message: _builtins.str,
        commit_id: Optional[_builtins.str] = ...,
        pull_request: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCheckedIn")
    def is_checked_in(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="commitId")
    def commit_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefaultRolloutPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        specification: Optional[
            outputs.DefaultRolloutPropertiesSpecificationResponse
        ] = ...,
        status: Optional[outputs.DefaultRolloutPropertiesStatusResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def specification(
        self,
    ) -> Optional[outputs.DefaultRolloutPropertiesSpecificationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[outputs.DefaultRolloutPropertiesStatusResponse]: ...

@pulumi.output_type
class DefaultRolloutPropertiesSpecificationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        auto_provision_config: Optional[
            outputs.DefaultRolloutSpecificationAutoProvisionConfigResponse
        ] = ...,
        canary: Optional[outputs.DefaultRolloutSpecificationCanaryResponse] = ...,
        expedited_rollout: Optional[
            outputs.DefaultRolloutSpecificationExpeditedRolloutResponse
        ] = ...,
        high_traffic: Optional[
            outputs.DefaultRolloutSpecificationHighTrafficResponse
        ] = ...,
        low_traffic: Optional[
            outputs.DefaultRolloutSpecificationLowTrafficResponse
        ] = ...,
        medium_traffic: Optional[
            outputs.DefaultRolloutSpecificationMediumTrafficResponse
        ] = ...,
        provider_registration: Optional[
            outputs.DefaultRolloutSpecificationProviderRegistrationResponse
        ] = ...,
        resource_type_registrations: Optional[
            Sequence[outputs.ResourceTypeRegistrationResponse]
        ] = ...,
        rest_of_the_world_group_one: Optional[
            outputs.DefaultRolloutSpecificationRestOfTheWorldGroupOneResponse
        ] = ...,
        rest_of_the_world_group_two: Optional[
            outputs.DefaultRolloutSpecificationRestOfTheWorldGroupTwoResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoProvisionConfig")
    def auto_provision_config(
        self,
    ) -> Optional[outputs.DefaultRolloutSpecificationAutoProvisionConfigResponse]: ...
    @_builtins.property
    @pulumi.getter
    def canary(self) -> Optional[outputs.DefaultRolloutSpecificationCanaryResponse]: ...
    @_builtins.property
    @pulumi.getter(name="expeditedRollout")
    def expedited_rollout(
        self,
    ) -> Optional[outputs.DefaultRolloutSpecificationExpeditedRolloutResponse]: ...
    @_builtins.property
    @pulumi.getter(name="highTraffic")
    def high_traffic(
        self,
    ) -> Optional[outputs.DefaultRolloutSpecificationHighTrafficResponse]: ...
    @_builtins.property
    @pulumi.getter(name="lowTraffic")
    def low_traffic(
        self,
    ) -> Optional[outputs.DefaultRolloutSpecificationLowTrafficResponse]: ...
    @_builtins.property
    @pulumi.getter(name="mediumTraffic")
    def medium_traffic(
        self,
    ) -> Optional[outputs.DefaultRolloutSpecificationMediumTrafficResponse]: ...
    @_builtins.property
    @pulumi.getter(name="providerRegistration")
    def provider_registration(
        self,
    ) -> Optional[outputs.DefaultRolloutSpecificationProviderRegistrationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeRegistrations")
    def resource_type_registrations(
        self,
    ) -> Optional[Sequence[outputs.ResourceTypeRegistrationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="restOfTheWorldGroupOne")
    def rest_of_the_world_group_one(
        self,
    ) -> Optional[
        outputs.DefaultRolloutSpecificationRestOfTheWorldGroupOneResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="restOfTheWorldGroupTwo")
    def rest_of_the_world_group_two(
        self,
    ) -> Optional[
        outputs.DefaultRolloutSpecificationRestOfTheWorldGroupTwoResponse
    ]: ...

@pulumi.output_type
class DefaultRolloutPropertiesStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        completed_regions: Optional[Sequence[_builtins.str]] = ...,
        failed_or_skipped_regions: Optional[
            Mapping[str, outputs.ExtendedErrorInfoResponse]
        ] = ...,
        manifest_checkin_status: Optional[
            outputs.DefaultRolloutStatusManifestCheckinStatusResponse
        ] = ...,
        next_traffic_region: Optional[_builtins.str] = ...,
        next_traffic_region_scheduled_time: Optional[_builtins.str] = ...,
        subscription_reregistration_result: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completedRegions")
    def completed_regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="failedOrSkippedRegions")
    def failed_or_skipped_regions(
        self,
    ) -> Optional[Mapping[str, outputs.ExtendedErrorInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="manifestCheckinStatus")
    def manifest_checkin_status(
        self,
    ) -> Optional[outputs.DefaultRolloutStatusManifestCheckinStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="nextTrafficRegion")
    def next_traffic_region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nextTrafficRegionScheduledTime")
    def next_traffic_region_scheduled_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionReregistrationResult")
    def subscription_reregistration_result(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefaultRolloutSpecificationAutoProvisionConfigResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_graph: Optional[_builtins.bool] = ...,
        storage: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGraph")
    def resource_graph(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefaultRolloutSpecificationCanaryResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regions: Optional[Sequence[_builtins.str]] = ...,
        skip_regions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="skipRegions")
    def skip_regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DefaultRolloutSpecificationExpeditedRolloutResponse(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DefaultRolloutSpecificationHighTrafficResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regions: Optional[Sequence[_builtins.str]] = ...,
        wait_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefaultRolloutSpecificationLowTrafficResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regions: Optional[Sequence[_builtins.str]] = ...,
        wait_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefaultRolloutSpecificationMediumTrafficResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regions: Optional[Sequence[_builtins.str]] = ...,
        wait_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefaultRolloutSpecificationProviderRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        kind: Optional[_builtins.str] = ...,
        properties: Optional[outputs.ProviderRegistrationPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[outputs.ProviderRegistrationPropertiesResponse]: ...

@pulumi.output_type
class DefaultRolloutSpecificationRestOfTheWorldGroupOneResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regions: Optional[Sequence[_builtins.str]] = ...,
        wait_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefaultRolloutSpecificationRestOfTheWorldGroupTwoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        regions: Optional[Sequence[_builtins.str]] = ...,
        wait_duration: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="waitDuration")
    def wait_duration(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DefaultRolloutStatusManifestCheckinStatusResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        is_checked_in: _builtins.bool,
        status_message: _builtins.str,
        commit_id: Optional[_builtins.str] = ...,
        pull_request: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isCheckedIn")
    def is_checked_in(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="commitId")
    def commit_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pullRequest")
    def pull_request(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DeleteDependencyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        linked_property: Optional[_builtins.str] = ...,
        linked_type: Optional[_builtins.str] = ...,
        required_features: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedProperty")
    def linked_property(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkedType")
    def linked_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class EndpointInformationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint: Optional[_builtins.str] = ...,
        endpoint_type: Optional[_builtins.str] = ...,
        schema_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExtendedErrorInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_info: Optional[Sequence[outputs.TypedErrorInfoResponse]] = ...,
        code: Optional[_builtins.str] = ...,
        details: Optional[Sequence[outputs.ExtendedErrorInfoResponse]] = ...,
        message: Optional[_builtins.str] = ...,
        target: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Optional[Sequence[outputs.TypedErrorInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[outputs.ExtendedErrorInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ExtendedLocationOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        supported_policy: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportedPolicy")
    def supported_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FanoutLinkedNotificationRuleDstsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: _builtins.str,
        service_dns_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FanoutLinkedNotificationRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Optional[Sequence[_builtins.str]] = ...,
        dsts_configuration: Optional[
            outputs.FanoutLinkedNotificationRuleDstsConfigurationResponse
        ] = ...,
        endpoints: Optional[Sequence[outputs.ResourceProviderEndpointResponse]] = ...,
        token_auth_configuration: Optional[
            outputs.TokenAuthConfigurationResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dstsConfiguration")
    def dsts_configuration(
        self,
    ) -> Optional[outputs.FanoutLinkedNotificationRuleDstsConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[Sequence[outputs.ResourceProviderEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="tokenAuthConfiguration")
    def token_auth_configuration(
        self,
    ) -> Optional[outputs.TokenAuthConfigurationResponse]: ...

@pulumi.output_type
class FilterRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_information: Optional[
            Sequence[outputs.EndpointInformationResponse]
        ] = ...,
        filter_query: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointInformation")
    def endpoint_information(
        self,
    ) -> Optional[Sequence[outputs.EndpointInformationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="filterQuery")
    def filter_query(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LegacyDisallowedConditionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disallowed_legacy_operations: Optional[Sequence[_builtins.str]] = ...,
        feature: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disallowedLegacyOperations")
    def disallowed_legacy_operations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def feature(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LightHouseAuthorizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, principal_id: _builtins.str, role_definition_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> _builtins.str: ...

@pulumi.output_type
class LinkedAccessCheckResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_name: Optional[_builtins.str] = ...,
        linked_action: Optional[_builtins.str] = ...,
        linked_action_verb: Optional[_builtins.str] = ...,
        linked_property: Optional[_builtins.str] = ...,
        linked_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkedAction")
    def linked_action(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkedActionVerb")
    def linked_action_verb(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkedProperty")
    def linked_property(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkedType")
    def linked_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LinkedNotificationRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Optional[Sequence[_builtins.str]] = ...,
        actions_on_failed_operation: Optional[Sequence[_builtins.str]] = ...,
        fast_path_actions: Optional[Sequence[_builtins.str]] = ...,
        fast_path_actions_on_failed_operation: Optional[Sequence[_builtins.str]] = ...,
        linked_notification_timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="actionsOnFailedOperation")
    def actions_on_failed_operation(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fastPathActions")
    def fast_path_actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="fastPathActionsOnFailedOperation")
    def fast_path_actions_on_failed_operation(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedNotificationTimeout")
    def linked_notification_timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LinkedOperationRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        linked_action: _builtins.str,
        linked_operation: _builtins.str,
        depends_on_types: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedAction")
    def linked_action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkedOperation")
    def linked_operation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dependsOnTypes")
    def depends_on_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class LocationQuotaRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        policy: Optional[_builtins.str] = ...,
        quota_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LoggingRuleHiddenPropertyPathsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hidden_paths_on_request: Optional[Sequence[_builtins.str]] = ...,
        hidden_paths_on_response: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hiddenPathsOnRequest")
    def hidden_paths_on_request(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hiddenPathsOnResponse")
    def hidden_paths_on_response(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class LoggingRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        detail_level: _builtins.str,
        direction: _builtins.str,
        hidden_property_paths: Optional[
            outputs.LoggingRuleHiddenPropertyPathsResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="detailLevel")
    def detail_level(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hiddenPropertyPaths")
    def hidden_property_paths(
        self,
    ) -> Optional[outputs.LoggingRuleHiddenPropertyPathsResponse]: ...

@pulumi.output_type
class NotificationEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        locations: Optional[Sequence[_builtins.str]] = ...,
        notification_destination: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationDestination")
    def notification_destination(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NotificationRegistrationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        included_events: Optional[Sequence[_builtins.str]] = ...,
        message_scope: Optional[_builtins.str] = ...,
        notification_endpoints: Optional[
            Sequence[outputs.NotificationEndpointResponse]
        ] = ...,
        notification_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includedEvents")
    def included_events(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="messageScope")
    def message_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationEndpoints")
    def notification_endpoints(
        self,
    ) -> Optional[Sequence[outputs.NotificationEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="notificationMode")
    def notification_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NotificationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        notification_type: Optional[_builtins.str] = ...,
        skip_notifications: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="notificationType")
    def notification_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skipNotifications")
    def skip_notifications(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class OpenApiConfigurationResponse(dict):
    def __init__(
        __self__, *, validation: Optional[outputs.OpenApiValidationResponse] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def validation(self) -> Optional[outputs.OpenApiValidationResponse]: ...

@pulumi.output_type
class OpenApiValidationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_noncompliant_collection_response: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowNoncompliantCollectionResponse")
    def allow_noncompliant_collection_response(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ProviderHubMetadataProviderAuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, allowed_audiences: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ProviderHubMetadataThirdPartyProviderAuthorizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorizations: Optional[
            Sequence[outputs.LightHouseAuthorizationResponse]
        ] = ...,
        managed_by_tenant_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authorizations(
        self,
    ) -> Optional[Sequence[outputs.LightHouseAuthorizationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="managedByTenantId")
    def managed_by_tenant_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProviderMonitorSettingPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, provisioning_state: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...

@pulumi.output_type
class ProviderRegistrationPropertiesPrivateResourceProviderConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_subscriptions: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSubscriptions")
    def allowed_subscriptions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ProviderRegistrationPropertiesProviderHubMetadataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        direct_rp_role_definition_id: Optional[_builtins.str] = ...,
        global_async_operation_resource_type_name: Optional[_builtins.str] = ...,
        provider_authentication: Optional[
            outputs.ProviderHubMetadataProviderAuthenticationResponse
        ] = ...,
        provider_authorizations: Optional[
            Sequence[outputs.ResourceProviderAuthorizationResponse]
        ] = ...,
        regional_async_operation_resource_type_name: Optional[_builtins.str] = ...,
        third_party_provider_authorization: Optional[
            outputs.ProviderHubMetadataThirdPartyProviderAuthorizationResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directRpRoleDefinitionId")
    def direct_rp_role_definition_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="globalAsyncOperationResourceTypeName")
    def global_async_operation_resource_type_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerAuthentication")
    def provider_authentication(
        self,
    ) -> Optional[outputs.ProviderHubMetadataProviderAuthenticationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="providerAuthorizations")
    def provider_authorizations(
        self,
    ) -> Optional[Sequence[outputs.ResourceProviderAuthorizationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="regionalAsyncOperationResourceTypeName")
    def regional_async_operation_resource_type_name(
        self,
    ) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="thirdPartyProviderAuthorization")
    def third_party_provider_authorization(
        self,
    ) -> Optional[
        outputs.ProviderHubMetadataThirdPartyProviderAuthorizationResponse
    ]: ...

@pulumi.output_type
class ProviderRegistrationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        capabilities: Optional[
            Sequence[outputs.ResourceProviderCapabilitiesResponse]
        ] = ...,
        cross_tenant_token_validation: Optional[_builtins.str] = ...,
        custom_manifest_version: Optional[_builtins.str] = ...,
        dsts_configuration: Optional[
            outputs.ResourceProviderManifestPropertiesDstsConfigurationResponse
        ] = ...,
        enable_tenant_linked_notification: Optional[_builtins.bool] = ...,
        features_rule: Optional[
            outputs.ResourceProviderManifestPropertiesFeaturesRuleResponse
        ] = ...,
        global_notification_endpoints: Optional[
            Sequence[outputs.ResourceProviderEndpointResponse]
        ] = ...,
        legacy_namespace: Optional[_builtins.str] = ...,
        legacy_registrations: Optional[Sequence[_builtins.str]] = ...,
        linked_notification_rules: Optional[
            Sequence[outputs.FanoutLinkedNotificationRuleResponse]
        ] = ...,
        management: Optional[
            outputs.ResourceProviderManifestPropertiesManagementResponse
        ] = ...,
        management_group_global_notification_endpoints: Optional[
            Sequence[outputs.ResourceProviderEndpointResponse]
        ] = ...,
        metadata: Optional[Any] = ...,
        namespace: Optional[_builtins.str] = ...,
        notification_options: Optional[_builtins.str] = ...,
        notification_settings: Optional[
            outputs.ResourceProviderManifestPropertiesNotificationSettingsResponse
        ] = ...,
        notifications: Optional[Sequence[outputs.NotificationResponse]] = ...,
        optional_features: Optional[Sequence[_builtins.str]] = ...,
        private_resource_provider_configuration: Optional[
            outputs.ProviderRegistrationPropertiesPrivateResourceProviderConfigurationResponse
        ] = ...,
        provider_authentication: Optional[
            outputs.ResourceProviderManifestPropertiesProviderAuthenticationResponse
        ] = ...,
        provider_authorizations: Optional[
            Sequence[outputs.ResourceProviderAuthorizationResponse]
        ] = ...,
        provider_hub_metadata: Optional[
            outputs.ProviderRegistrationPropertiesProviderHubMetadataResponse
        ] = ...,
        provider_type: Optional[_builtins.str] = ...,
        provider_version: Optional[_builtins.str] = ...,
        request_header_options: Optional[
            outputs.ResourceProviderManifestPropertiesRequestHeaderOptionsResponse
        ] = ...,
        required_features: Optional[Sequence[_builtins.str]] = ...,
        resource_group_lock_option_during_move: Optional[
            outputs.ResourceProviderManifestPropertiesResourceGroupLockOptionDuringMoveResponse
        ] = ...,
        resource_hydration_accounts: Optional[
            Sequence[outputs.ResourceHydrationAccountResponse]
        ] = ...,
        resource_provider_authorization_rules: Optional[
            outputs.ResourceProviderAuthorizationRulesResponse
        ] = ...,
        response_options: Optional[
            outputs.ResourceProviderManifestPropertiesResponseOptionsResponse
        ] = ...,
        service_name: Optional[_builtins.str] = ...,
        services: Optional[Sequence[outputs.ResourceProviderServiceResponse]] = ...,
        subscription_lifecycle_notification_specifications: Optional[
            outputs.ProviderRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsResponse
        ] = ...,
        template_deployment_options: Optional[
            outputs.ResourceProviderManifestPropertiesTemplateDeploymentOptionsResponse
        ] = ...,
        token_auth_configuration: Optional[
            outputs.TokenAuthConfigurationResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> Optional[Sequence[outputs.ResourceProviderCapabilitiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="crossTenantTokenValidation")
    def cross_tenant_token_validation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customManifestVersion")
    def custom_manifest_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dstsConfiguration")
    def dsts_configuration(
        self,
    ) -> Optional[
        outputs.ResourceProviderManifestPropertiesDstsConfigurationResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableTenantLinkedNotification")
    def enable_tenant_linked_notification(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="featuresRule")
    def features_rule(
        self,
    ) -> Optional[outputs.ResourceProviderManifestPropertiesFeaturesRuleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="globalNotificationEndpoints")
    def global_notification_endpoints(
        self,
    ) -> Optional[Sequence[outputs.ResourceProviderEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="legacyNamespace")
    def legacy_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="legacyRegistrations")
    def legacy_registrations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedNotificationRules")
    def linked_notification_rules(
        self,
    ) -> Optional[Sequence[outputs.FanoutLinkedNotificationRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def management(
        self,
    ) -> Optional[outputs.ResourceProviderManifestPropertiesManagementResponse]: ...
    @_builtins.property
    @pulumi.getter(name="managementGroupGlobalNotificationEndpoints")
    def management_group_global_notification_endpoints(
        self,
    ) -> Optional[Sequence[outputs.ResourceProviderEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationOptions")
    def notification_options(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> Optional[
        outputs.ResourceProviderManifestPropertiesNotificationSettingsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[Sequence[outputs.NotificationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="optionalFeatures")
    def optional_features(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateResourceProviderConfiguration")
    def private_resource_provider_configuration(
        self,
    ) -> Optional[
        outputs.ProviderRegistrationPropertiesPrivateResourceProviderConfigurationResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="providerAuthentication")
    def provider_authentication(
        self,
    ) -> Optional[
        outputs.ResourceProviderManifestPropertiesProviderAuthenticationResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="providerAuthorizations")
    def provider_authorizations(
        self,
    ) -> Optional[Sequence[outputs.ResourceProviderAuthorizationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="providerHubMetadata")
    def provider_hub_metadata(
        self,
    ) -> Optional[
        outputs.ProviderRegistrationPropertiesProviderHubMetadataResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerVersion")
    def provider_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderOptions")
    def request_header_options(
        self,
    ) -> Optional[
        outputs.ResourceProviderManifestPropertiesRequestHeaderOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupLockOptionDuringMove")
    def resource_group_lock_option_during_move(
        self,
    ) -> Optional[
        outputs.ResourceProviderManifestPropertiesResourceGroupLockOptionDuringMoveResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceHydrationAccounts")
    def resource_hydration_accounts(
        self,
    ) -> Optional[Sequence[outputs.ResourceHydrationAccountResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderAuthorizationRules")
    def resource_provider_authorization_rules(
        self,
    ) -> Optional[outputs.ResourceProviderAuthorizationRulesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="responseOptions")
    def response_options(
        self,
    ) -> Optional[
        outputs.ResourceProviderManifestPropertiesResponseOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def services(
        self,
    ) -> Optional[Sequence[outputs.ResourceProviderServiceResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionLifecycleNotificationSpecifications")
    def subscription_lifecycle_notification_specifications(
        self,
    ) -> Optional[
        outputs.ProviderRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="templateDeploymentOptions")
    def template_deployment_options(
        self,
    ) -> Optional[
        outputs.ResourceProviderManifestPropertiesTemplateDeploymentOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tokenAuthConfiguration")
    def token_auth_configuration(
        self,
    ) -> Optional[outputs.TokenAuthConfigurationResponse]: ...

@pulumi.output_type
class ProviderRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsResponse(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        soft_delete_ttl: Optional[_builtins.str] = ...,
        subscription_state_override_actions: Optional[
            Sequence[outputs.SubscriptionStateOverrideActionResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="softDeleteTTL")
    def soft_delete_ttl(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionStateOverrideActions")
    def subscription_state_override_actions(
        self,
    ) -> Optional[Sequence[outputs.SubscriptionStateOverrideActionResponse]]: ...

@pulumi.output_type
class QuotaRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location_rules: Optional[Sequence[outputs.LocationQuotaRuleResponse]] = ...,
        quota_policy: Optional[_builtins.str] = ...,
        required_features: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="locationRules")
    def location_rules(
        self,
    ) -> Optional[Sequence[outputs.LocationQuotaRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="quotaPolicy")
    def quota_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResourceAccessRoleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Optional[Sequence[_builtins.str]] = ...,
        allowed_group_claims: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedGroupClaims")
    def allowed_group_claims(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResourceConcurrencyControlOptionResponse(dict):
    def __init__(__self__, *, policy: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceHydrationAccountResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        account_name: Optional[_builtins.str] = ...,
        encrypted_key: Optional[_builtins.str] = ...,
        max_child_resource_consistency_job_limit: Optional[_builtins.float] = ...,
        subscription_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptedKey")
    def encrypted_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxChildResourceConsistencyJobLimit")
    def max_child_resource_consistency_job_limit(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderAuthorizationManagedByAuthorizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_authorizations: Optional[
            Sequence[outputs.AdditionalAuthorizationResponse]
        ] = ...,
        allow_managed_by_inheritance: Optional[_builtins.bool] = ...,
        managed_by_resource_role_definition_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalAuthorizations")
    def additional_authorizations(
        self,
    ) -> Optional[Sequence[outputs.AdditionalAuthorizationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="allowManagedByInheritance")
    def allow_managed_by_inheritance(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="managedByResourceRoleDefinitionId")
    def managed_by_resource_role_definition_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderAuthorizationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_third_party_extensions: Optional[
            Sequence[outputs.ThirdPartyExtensionResponse]
        ] = ...,
        application_id: Optional[_builtins.str] = ...,
        grouping_tag: Optional[_builtins.str] = ...,
        managed_by_authorization: Optional[
            outputs.ResourceProviderAuthorizationManagedByAuthorizationResponse
        ] = ...,
        managed_by_role_definition_id: Optional[_builtins.str] = ...,
        role_definition_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedThirdPartyExtensions")
    def allowed_third_party_extensions(
        self,
    ) -> Optional[Sequence[outputs.ThirdPartyExtensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupingTag")
    def grouping_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="managedByAuthorization")
    def managed_by_authorization(
        self,
    ) -> Optional[
        outputs.ResourceProviderAuthorizationManagedByAuthorizationResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="managedByRoleDefinitionId")
    def managed_by_role_definition_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderAuthorizationRulesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        async_operation_polling_rules: Optional[
            outputs.AsyncOperationPollingRulesResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="asyncOperationPollingRules")
    def async_operation_polling_rules(
        self,
    ) -> Optional[outputs.AsyncOperationPollingRulesResponse]: ...

@pulumi.output_type
class ResourceProviderCapabilitiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        effect: _builtins.str,
        quota_id: _builtins.str,
        required_features: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def effect(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResourceProviderEndpointFeaturesRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, required_features_policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeaturesPolicy")
    def required_features_policy(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceProviderEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_versions: Optional[Sequence[_builtins.str]] = ...,
        enabled: Optional[_builtins.bool] = ...,
        endpoint_type: Optional[_builtins.str] = ...,
        endpoint_uri: Optional[_builtins.str] = ...,
        features_rule: Optional[
            outputs.ResourceProviderEndpointFeaturesRuleResponse
        ] = ...,
        locations: Optional[Sequence[_builtins.str]] = ...,
        required_features: Optional[Sequence[_builtins.str]] = ...,
        sku_link: Optional[_builtins.str] = ...,
        timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersions")
    def api_versions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="featuresRule")
    def features_rule(
        self,
    ) -> Optional[outputs.ResourceProviderEndpointFeaturesRuleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="skuLink")
    def sku_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderManagementErrorResponseMessageOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, server_failure_response_message_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverFailureResponseMessageType")
    def server_failure_response_message_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderManagementExpeditedRolloutMetadataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        expedited_rollout_intent: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutIntent")
    def expedited_rollout_intent(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderManifestPropertiesDstsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: _builtins.str,
        service_dns_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderManifestPropertiesFeaturesRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, required_features_policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeaturesPolicy")
    def required_features_policy(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceProviderManifestPropertiesManagementResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_owners: Optional[Sequence[_builtins.str]] = ...,
        canary_manifest_owners: Optional[Sequence[_builtins.str]] = ...,
        error_response_message_options: Optional[
            outputs.ResourceProviderManagementErrorResponseMessageOptionsResponse
        ] = ...,
        expedited_rollout_metadata: Optional[
            outputs.ResourceProviderManagementExpeditedRolloutMetadataResponse
        ] = ...,
        expedited_rollout_submitters: Optional[Sequence[_builtins.str]] = ...,
        incident_contact_email: Optional[_builtins.str] = ...,
        incident_routing_service: Optional[_builtins.str] = ...,
        incident_routing_team: Optional[_builtins.str] = ...,
        manifest_owners: Optional[Sequence[_builtins.str]] = ...,
        pc_code: Optional[_builtins.str] = ...,
        profit_center_program_id: Optional[_builtins.str] = ...,
        resource_access_policy: Optional[_builtins.str] = ...,
        resource_access_roles: Optional[
            Sequence[outputs.ResourceAccessRoleResponse]
        ] = ...,
        schema_owners: Optional[Sequence[_builtins.str]] = ...,
        service_tree_infos: Optional[Sequence[outputs.ServiceTreeInfoResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationOwners")
    def authorization_owners(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="canaryManifestOwners")
    def canary_manifest_owners(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="errorResponseMessageOptions")
    def error_response_message_options(
        self,
    ) -> Optional[
        outputs.ResourceProviderManagementErrorResponseMessageOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutMetadata")
    def expedited_rollout_metadata(
        self,
    ) -> Optional[
        outputs.ResourceProviderManagementExpeditedRolloutMetadataResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutSubmitters")
    def expedited_rollout_submitters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="incidentContactEmail")
    def incident_contact_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="incidentRoutingService")
    def incident_routing_service(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="incidentRoutingTeam")
    def incident_routing_team(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manifestOwners")
    def manifest_owners(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pcCode")
    def pc_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profitCenterProgramId")
    def profit_center_program_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessPolicy")
    def resource_access_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRoles")
    def resource_access_roles(
        self,
    ) -> Optional[Sequence[outputs.ResourceAccessRoleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="schemaOwners")
    def schema_owners(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceTreeInfos")
    def service_tree_infos(
        self,
    ) -> Optional[Sequence[outputs.ServiceTreeInfoResponse]]: ...

@pulumi.output_type
class ResourceProviderManifestPropertiesNotificationSettingsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        subscriber_settings: Optional[
            Sequence[outputs.SubscriberSettingResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subscriberSettings")
    def subscriber_settings(
        self,
    ) -> Optional[Sequence[outputs.SubscriberSettingResponse]]: ...

@pulumi.output_type
class ResourceProviderManifestPropertiesProviderAuthenticationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, allowed_audiences: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedAudiences")
    def allowed_audiences(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderManifestPropertiesRequestHeaderOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        opt_in_headers: Optional[_builtins.str] = ...,
        opt_out_headers: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optInHeaders")
    def opt_in_headers(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="optOutHeaders")
    def opt_out_headers(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderManifestPropertiesResourceGroupLockOptionDuringMoveResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, block_action_verb: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockActionVerb")
    def block_action_verb(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderManifestPropertiesResponseOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, service_client_options_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceClientOptionsType")
    def service_client_options_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceProviderManifestPropertiesTemplateDeploymentOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        preflight_options: Optional[Sequence[_builtins.str]] = ...,
        preflight_supported: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preflightOptions")
    def preflight_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="preflightSupported")
    def preflight_supported(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ResourceProviderServiceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeEndpointDstsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: _builtins.str,
        service_dns_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeEndpointFeaturesRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, required_features_policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeaturesPolicy")
    def required_features_policy(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceTypeEndpointResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_version: Optional[_builtins.str] = ...,
        api_versions: Optional[Sequence[_builtins.str]] = ...,
        data_boundary: Optional[_builtins.str] = ...,
        dsts_configuration: Optional[
            outputs.ResourceTypeEndpointDstsConfigurationResponse
        ] = ...,
        enabled: Optional[_builtins.bool] = ...,
        endpoint_type: Optional[_builtins.str] = ...,
        endpoint_uri: Optional[_builtins.str] = ...,
        extensions: Optional[Sequence[outputs.ResourceTypeExtensionResponse]] = ...,
        features_rule: Optional[outputs.ResourceTypeEndpointFeaturesRuleResponse] = ...,
        kind: Optional[_builtins.str] = ...,
        locations: Optional[Sequence[_builtins.str]] = ...,
        required_features: Optional[Sequence[_builtins.str]] = ...,
        sku_link: Optional[_builtins.str] = ...,
        timeout: Optional[_builtins.str] = ...,
        token_auth_configuration: Optional[
            outputs.TokenAuthConfigurationResponse
        ] = ...,
        zones: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="apiVersions")
    def api_versions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dataBoundary")
    def data_boundary(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dstsConfiguration")
    def dsts_configuration(
        self,
    ) -> Optional[outputs.ResourceTypeEndpointDstsConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Optional[Sequence[outputs.ResourceTypeExtensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="featuresRule")
    def features_rule(
        self,
    ) -> Optional[outputs.ResourceTypeEndpointFeaturesRuleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="skuLink")
    def sku_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tokenAuthConfiguration")
    def token_auth_configuration(
        self,
    ) -> Optional[outputs.TokenAuthConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResourceTypeExtensionOptionsResourceCreationBeginResponse(dict):
    def __init__(
        __self__,
        *,
        request: Optional[Sequence[_builtins.str]] = ...,
        response: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def request(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResourceTypeExtensionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_uri: Optional[_builtins.str] = ...,
        extension_categories: Optional[Sequence[_builtins.str]] = ...,
        timeout: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="extensionCategories")
    def extension_categories(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeOnBehalfOfTokenResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_name: Optional[_builtins.str] = ...,
        life_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionName")
    def action_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lifeTime")
    def life_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesAvailabilityZoneRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_zone_policy: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZonePolicy")
    def availability_zone_policy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesCapacityRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_policy: Optional[_builtins.str] = ...,
        sku_alias: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityPolicy")
    def capacity_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skuAlias")
    def sku_alias(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesCheckNameAvailabilitySpecificationsResponse(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_default_validation: Optional[_builtins.bool] = ...,
        resource_types_with_custom_validation: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableDefaultValidation")
    def enable_default_validation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypesWithCustomValidation")
    def resource_types_with_custom_validation(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesDstsConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_name: _builtins.str,
        service_dns_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceDnsName")
    def service_dns_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesExtensionOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_creation_begin: Optional[
            outputs.ResourceTypeExtensionOptionsResourceCreationBeginResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceCreationBegin")
    def resource_creation_begin(
        self,
    ) -> Optional[
        outputs.ResourceTypeExtensionOptionsResourceCreationBeginResponse
    ]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesFeaturesRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, required_features_policy: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeaturesPolicy")
    def required_features_policy(self) -> _builtins.str: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesIdentityManagementResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        application_id: Optional[_builtins.str] = ...,
        application_ids: Optional[Sequence[_builtins.str]] = ...,
        delegation_app_ids: Optional[Sequence[_builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="applicationIds")
    def application_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="delegationAppIds")
    def delegation_app_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesLegacyPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disallowed_conditions: Optional[
            Sequence[outputs.LegacyDisallowedConditionResponse]
        ] = ...,
        disallowed_legacy_operations: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disallowedConditions")
    def disallowed_conditions(
        self,
    ) -> Optional[Sequence[outputs.LegacyDisallowedConditionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="disallowedLegacyOperations")
    def disallowed_legacy_operations(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesManagementResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authorization_owners: Optional[Sequence[_builtins.str]] = ...,
        canary_manifest_owners: Optional[Sequence[_builtins.str]] = ...,
        error_response_message_options: Optional[
            outputs.ResourceProviderManagementErrorResponseMessageOptionsResponse
        ] = ...,
        expedited_rollout_metadata: Optional[
            outputs.ResourceProviderManagementExpeditedRolloutMetadataResponse
        ] = ...,
        expedited_rollout_submitters: Optional[Sequence[_builtins.str]] = ...,
        incident_contact_email: Optional[_builtins.str] = ...,
        incident_routing_service: Optional[_builtins.str] = ...,
        incident_routing_team: Optional[_builtins.str] = ...,
        manifest_owners: Optional[Sequence[_builtins.str]] = ...,
        pc_code: Optional[_builtins.str] = ...,
        profit_center_program_id: Optional[_builtins.str] = ...,
        resource_access_policy: Optional[_builtins.str] = ...,
        resource_access_roles: Optional[
            Sequence[outputs.ResourceAccessRoleResponse]
        ] = ...,
        schema_owners: Optional[Sequence[_builtins.str]] = ...,
        service_tree_infos: Optional[Sequence[outputs.ServiceTreeInfoResponse]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationOwners")
    def authorization_owners(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="canaryManifestOwners")
    def canary_manifest_owners(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="errorResponseMessageOptions")
    def error_response_message_options(
        self,
    ) -> Optional[
        outputs.ResourceProviderManagementErrorResponseMessageOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutMetadata")
    def expedited_rollout_metadata(
        self,
    ) -> Optional[
        outputs.ResourceProviderManagementExpeditedRolloutMetadataResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="expeditedRolloutSubmitters")
    def expedited_rollout_submitters(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="incidentContactEmail")
    def incident_contact_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="incidentRoutingService")
    def incident_routing_service(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="incidentRoutingTeam")
    def incident_routing_team(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="manifestOwners")
    def manifest_owners(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pcCode")
    def pc_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profitCenterProgramId")
    def profit_center_program_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessPolicy")
    def resource_access_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceAccessRoles")
    def resource_access_roles(
        self,
    ) -> Optional[Sequence[outputs.ResourceAccessRoleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="schemaOwners")
    def schema_owners(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceTreeInfos")
    def service_tree_infos(
        self,
    ) -> Optional[Sequence[outputs.ServiceTreeInfoResponse]]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesMarketplaceOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, add_on_plan_conversion_allowed: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addOnPlanConversionAllowed")
    def add_on_plan_conversion_allowed(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesRequestHeaderOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        opt_in_headers: Optional[_builtins.str] = ...,
        opt_out_headers: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optInHeaders")
    def opt_in_headers(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="optOutHeaders")
    def opt_out_headers(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesResourceCacheResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_resource_cache: Optional[_builtins.bool] = ...,
        resource_cache_expiration_timespan: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableResourceCache")
    def enable_resource_cache(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="resourceCacheExpirationTimespan")
    def resource_cache_expiration_timespan(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesResourceGraphConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_version: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesResourceManagementOptionsBatchProvisioningSupportResponse(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, supported_operations: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="supportedOperations")
    def supported_operations(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesResourceManagementOptionsNestedProvisioningSupportResponse(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, minimum_api_version: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumApiVersion")
    def minimum_api_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesResourceManagementOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        batch_provisioning_support: Optional[
            outputs.ResourceTypeRegistrationPropertiesResourceManagementOptionsBatchProvisioningSupportResponse
        ] = ...,
        delete_dependencies: Optional[Sequence[outputs.DeleteDependencyResponse]] = ...,
        nested_provisioning_support: Optional[
            outputs.ResourceTypeRegistrationPropertiesResourceManagementOptionsNestedProvisioningSupportResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="batchProvisioningSupport")
    def batch_provisioning_support(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesResourceManagementOptionsBatchProvisioningSupportResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="deleteDependencies")
    def delete_dependencies(
        self,
    ) -> Optional[Sequence[outputs.DeleteDependencyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="nestedProvisioningSupport")
    def nested_provisioning_support(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesResourceManagementOptionsNestedProvisioningSupportResponse
    ]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesResourceMovePolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cross_resource_group_move_enabled: Optional[_builtins.bool] = ...,
        cross_subscription_move_enabled: Optional[_builtins.bool] = ...,
        validation_required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="crossResourceGroupMoveEnabled")
    def cross_resource_group_move_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="crossSubscriptionMoveEnabled")
    def cross_subscription_move_enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="validationRequired")
    def validation_required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesResourceQueryManagementResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, filter_option: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterOption")
    def filter_option(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesResourceTypeCommonAttributeManagementResponse(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, common_api_versions_merge_mode: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonApiVersionsMergeMode")
    def common_api_versions_merge_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        add_resource_list_target_locations: Optional[_builtins.bool] = ...,
        additional_options: Optional[_builtins.str] = ...,
        allow_empty_role_assignments: Optional[_builtins.bool] = ...,
        allowed_resource_names: Optional[
            Sequence[outputs.AllowedResourceNameResponse]
        ] = ...,
        allowed_template_deployment_reference_actions: Optional[
            Sequence[_builtins.str]
        ] = ...,
        allowed_unauthorized_actions: Optional[Sequence[_builtins.str]] = ...,
        allowed_unauthorized_actions_extensions: Optional[
            Sequence[outputs.AllowedUnauthorizedActionsExtensionResponse]
        ] = ...,
        api_profiles: Optional[Sequence[outputs.ApiProfileResponse]] = ...,
        async_operation_resource_type_name: Optional[_builtins.str] = ...,
        async_timeout_rules: Optional[Sequence[outputs.AsyncTimeoutRuleResponse]] = ...,
        authorization_action_mappings: Optional[
            Sequence[outputs.AuthorizationActionMappingResponse]
        ] = ...,
        availability_zone_rule: Optional[
            outputs.ResourceTypeRegistrationPropertiesAvailabilityZoneRuleResponse
        ] = ...,
        capacity_rule: Optional[
            outputs.ResourceTypeRegistrationPropertiesCapacityRuleResponse
        ] = ...,
        category: Optional[_builtins.str] = ...,
        check_name_availability_specifications: Optional[
            outputs.ResourceTypeRegistrationPropertiesCheckNameAvailabilitySpecificationsResponse
        ] = ...,
        common_api_versions: Optional[Sequence[_builtins.str]] = ...,
        cross_tenant_token_validation: Optional[_builtins.str] = ...,
        default_api_version: Optional[_builtins.str] = ...,
        disallowed_action_verbs: Optional[Sequence[_builtins.str]] = ...,
        disallowed_end_user_operations: Optional[Sequence[_builtins.str]] = ...,
        dsts_configuration: Optional[
            outputs.ResourceTypeRegistrationPropertiesDstsConfigurationResponse
        ] = ...,
        enable_async_operation: Optional[_builtins.bool] = ...,
        enable_third_party_s2_s: Optional[_builtins.bool] = ...,
        endpoints: Optional[Sequence[outputs.ResourceTypeEndpointResponse]] = ...,
        extended_locations: Optional[
            Sequence[outputs.ExtendedLocationOptionsResponse]
        ] = ...,
        extension_options: Optional[
            outputs.ResourceTypeRegistrationPropertiesExtensionOptionsResponse
        ] = ...,
        features_rule: Optional[
            outputs.ResourceTypeRegistrationPropertiesFeaturesRuleResponse
        ] = ...,
        frontdoor_request_mode: Optional[_builtins.str] = ...,
        grouping_tag: Optional[_builtins.str] = ...,
        identity_management: Optional[
            outputs.ResourceTypeRegistrationPropertiesIdentityManagementResponse
        ] = ...,
        is_pure_proxy: Optional[_builtins.bool] = ...,
        legacy_name: Optional[_builtins.str] = ...,
        legacy_names: Optional[Sequence[_builtins.str]] = ...,
        legacy_policy: Optional[
            outputs.ResourceTypeRegistrationPropertiesLegacyPolicyResponse
        ] = ...,
        linked_access_checks: Optional[
            Sequence[outputs.LinkedAccessCheckResponse]
        ] = ...,
        linked_notification_rules: Optional[
            Sequence[outputs.LinkedNotificationRuleResponse]
        ] = ...,
        linked_operation_rules: Optional[
            Sequence[outputs.LinkedOperationRuleResponse]
        ] = ...,
        logging_rules: Optional[Sequence[outputs.LoggingRuleResponse]] = ...,
        management: Optional[
            outputs.ResourceTypeRegistrationPropertiesManagementResponse
        ] = ...,
        manifest_link: Optional[_builtins.str] = ...,
        marketplace_options: Optional[
            outputs.ResourceTypeRegistrationPropertiesMarketplaceOptionsResponse
        ] = ...,
        marketplace_type: Optional[_builtins.str] = ...,
        metadata: Optional[Any] = ...,
        notifications: Optional[Sequence[outputs.NotificationResponse]] = ...,
        on_behalf_of_tokens: Optional[
            outputs.ResourceTypeOnBehalfOfTokenResponse
        ] = ...,
        open_api_configuration: Optional[outputs.OpenApiConfigurationResponse] = ...,
        policy_execution_type: Optional[_builtins.str] = ...,
        quota_rule: Optional[outputs.QuotaRuleResponse] = ...,
        regionality: Optional[_builtins.str] = ...,
        request_header_options: Optional[
            outputs.ResourceTypeRegistrationPropertiesRequestHeaderOptionsResponse
        ] = ...,
        required_features: Optional[Sequence[_builtins.str]] = ...,
        resource_cache: Optional[
            outputs.ResourceTypeRegistrationPropertiesResourceCacheResponse
        ] = ...,
        resource_concurrency_control_options: Optional[
            Mapping[str, outputs.ResourceConcurrencyControlOptionResponse]
        ] = ...,
        resource_deletion_policy: Optional[_builtins.str] = ...,
        resource_graph_configuration: Optional[
            outputs.ResourceTypeRegistrationPropertiesResourceGraphConfigurationResponse
        ] = ...,
        resource_management_options: Optional[
            outputs.ResourceTypeRegistrationPropertiesResourceManagementOptionsResponse
        ] = ...,
        resource_move_policy: Optional[
            outputs.ResourceTypeRegistrationPropertiesResourceMovePolicyResponse
        ] = ...,
        resource_provider_authorization_rules: Optional[
            outputs.ResourceProviderAuthorizationRulesResponse
        ] = ...,
        resource_query_management: Optional[
            outputs.ResourceTypeRegistrationPropertiesResourceQueryManagementResponse
        ] = ...,
        resource_sub_type: Optional[_builtins.str] = ...,
        resource_type_common_attribute_management: Optional[
            outputs.ResourceTypeRegistrationPropertiesResourceTypeCommonAttributeManagementResponse
        ] = ...,
        resource_validation: Optional[_builtins.str] = ...,
        routing_rule: Optional[
            outputs.ResourceTypeRegistrationPropertiesRoutingRuleResponse
        ] = ...,
        routing_type: Optional[_builtins.str] = ...,
        service_tree_infos: Optional[Sequence[outputs.ServiceTreeInfoResponse]] = ...,
        sku_link: Optional[_builtins.str] = ...,
        subscription_lifecycle_notification_specifications: Optional[
            outputs.ResourceTypeRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsResponse
        ] = ...,
        subscription_state_rules: Optional[
            Sequence[outputs.SubscriptionStateRuleResponse]
        ] = ...,
        supports_tags: Optional[_builtins.bool] = ...,
        swagger_specifications: Optional[
            Sequence[outputs.SwaggerSpecificationResponse]
        ] = ...,
        template_deployment_options: Optional[
            outputs.ResourceTypeRegistrationPropertiesTemplateDeploymentOptionsResponse
        ] = ...,
        template_deployment_policy: Optional[
            outputs.ResourceTypeRegistrationPropertiesTemplateDeploymentPolicyResponse
        ] = ...,
        throttling_rules: Optional[Sequence[outputs.ThrottlingRuleResponse]] = ...,
        token_auth_configuration: Optional[
            outputs.TokenAuthConfigurationResponse
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="addResourceListTargetLocations")
    def add_resource_list_target_locations(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="additionalOptions")
    def additional_options(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allowEmptyRoleAssignments")
    def allow_empty_role_assignments(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowedResourceNames")
    def allowed_resource_names(
        self,
    ) -> Optional[Sequence[outputs.AllowedResourceNameResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedTemplateDeploymentReferenceActions")
    def allowed_template_deployment_reference_actions(
        self,
    ) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnauthorizedActions")
    def allowed_unauthorized_actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="allowedUnauthorizedActionsExtensions")
    def allowed_unauthorized_actions_extensions(
        self,
    ) -> Optional[Sequence[outputs.AllowedUnauthorizedActionsExtensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="apiProfiles")
    def api_profiles(self) -> Optional[Sequence[outputs.ApiProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="asyncOperationResourceTypeName")
    def async_operation_resource_type_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="asyncTimeoutRules")
    def async_timeout_rules(
        self,
    ) -> Optional[Sequence[outputs.AsyncTimeoutRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="authorizationActionMappings")
    def authorization_action_mappings(
        self,
    ) -> Optional[Sequence[outputs.AuthorizationActionMappingResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneRule")
    def availability_zone_rule(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesAvailabilityZoneRuleResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="capacityRule")
    def capacity_rule(
        self,
    ) -> Optional[outputs.ResourceTypeRegistrationPropertiesCapacityRuleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="checkNameAvailabilitySpecifications")
    def check_name_availability_specifications(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesCheckNameAvailabilitySpecificationsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="commonApiVersions")
    def common_api_versions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="crossTenantTokenValidation")
    def cross_tenant_token_validation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultApiVersion")
    def default_api_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disallowedActionVerbs")
    def disallowed_action_verbs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="disallowedEndUserOperations")
    def disallowed_end_user_operations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dstsConfiguration")
    def dsts_configuration(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesDstsConfigurationResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableAsyncOperation")
    def enable_async_operation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableThirdPartyS2S")
    def enable_third_party_s2_s(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[outputs.ResourceTypeEndpointResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocations")
    def extended_locations(
        self,
    ) -> Optional[Sequence[outputs.ExtendedLocationOptionsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="extensionOptions")
    def extension_options(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesExtensionOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="featuresRule")
    def features_rule(
        self,
    ) -> Optional[outputs.ResourceTypeRegistrationPropertiesFeaturesRuleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="frontdoorRequestMode")
    def frontdoor_request_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="groupingTag")
    def grouping_tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="identityManagement")
    def identity_management(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesIdentityManagementResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="isPureProxy")
    def is_pure_proxy(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="legacyName")
    def legacy_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="legacyNames")
    def legacy_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="legacyPolicy")
    def legacy_policy(
        self,
    ) -> Optional[outputs.ResourceTypeRegistrationPropertiesLegacyPolicyResponse]: ...
    @_builtins.property
    @pulumi.getter(name="linkedAccessChecks")
    def linked_access_checks(
        self,
    ) -> Optional[Sequence[outputs.LinkedAccessCheckResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedNotificationRules")
    def linked_notification_rules(
        self,
    ) -> Optional[Sequence[outputs.LinkedNotificationRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedOperationRules")
    def linked_operation_rules(
        self,
    ) -> Optional[Sequence[outputs.LinkedOperationRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="loggingRules")
    def logging_rules(self) -> Optional[Sequence[outputs.LoggingRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def management(
        self,
    ) -> Optional[outputs.ResourceTypeRegistrationPropertiesManagementResponse]: ...
    @_builtins.property
    @pulumi.getter(name="manifestLink")
    def manifest_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceOptions")
    def marketplace_options(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesMarketplaceOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="marketplaceType")
    def marketplace_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]: ...
    @_builtins.property
    @pulumi.getter
    def notifications(self) -> Optional[Sequence[outputs.NotificationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="onBehalfOfTokens")
    def on_behalf_of_tokens(
        self,
    ) -> Optional[outputs.ResourceTypeOnBehalfOfTokenResponse]: ...
    @_builtins.property
    @pulumi.getter(name="openApiConfiguration")
    def open_api_configuration(
        self,
    ) -> Optional[outputs.OpenApiConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="policyExecutionType")
    def policy_execution_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="quotaRule")
    def quota_rule(self) -> Optional[outputs.QuotaRuleResponse]: ...
    @_builtins.property
    @pulumi.getter
    def regionality(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaderOptions")
    def request_header_options(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesRequestHeaderOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceCache")
    def resource_cache(
        self,
    ) -> Optional[outputs.ResourceTypeRegistrationPropertiesResourceCacheResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceConcurrencyControlOptions")
    def resource_concurrency_control_options(
        self,
    ) -> Optional[Mapping[str, outputs.ResourceConcurrencyControlOptionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceDeletionPolicy")
    def resource_deletion_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceGraphConfiguration")
    def resource_graph_configuration(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesResourceGraphConfigurationResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceManagementOptions")
    def resource_management_options(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesResourceManagementOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceMovePolicy")
    def resource_move_policy(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesResourceMovePolicyResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceProviderAuthorizationRules")
    def resource_provider_authorization_rules(
        self,
    ) -> Optional[outputs.ResourceProviderAuthorizationRulesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceQueryManagement")
    def resource_query_management(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesResourceQueryManagementResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceSubType")
    def resource_sub_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypeCommonAttributeManagement")
    def resource_type_common_attribute_management(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesResourceTypeCommonAttributeManagementResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="resourceValidation")
    def resource_validation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingRule")
    def routing_rule(
        self,
    ) -> Optional[outputs.ResourceTypeRegistrationPropertiesRoutingRuleResponse]: ...
    @_builtins.property
    @pulumi.getter(name="routingType")
    def routing_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceTreeInfos")
    def service_tree_infos(
        self,
    ) -> Optional[Sequence[outputs.ServiceTreeInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="skuLink")
    def sku_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionLifecycleNotificationSpecifications")
    def subscription_lifecycle_notification_specifications(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionStateRules")
    def subscription_state_rules(
        self,
    ) -> Optional[Sequence[outputs.SubscriptionStateRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="supportsTags")
    def supports_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="swaggerSpecifications")
    def swagger_specifications(
        self,
    ) -> Optional[Sequence[outputs.SwaggerSpecificationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="templateDeploymentOptions")
    def template_deployment_options(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesTemplateDeploymentOptionsResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="templateDeploymentPolicy")
    def template_deployment_policy(
        self,
    ) -> Optional[
        outputs.ResourceTypeRegistrationPropertiesTemplateDeploymentPolicyResponse
    ]: ...
    @_builtins.property
    @pulumi.getter(name="throttlingRules")
    def throttling_rules(
        self,
    ) -> Optional[Sequence[outputs.ThrottlingRuleResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="tokenAuthConfiguration")
    def token_auth_configuration(
        self,
    ) -> Optional[outputs.TokenAuthConfigurationResponse]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesRoutingRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, host_resource_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostResourceType")
    def host_resource_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesSubscriptionLifecycleNotificationSpecificationsResponse(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        soft_delete_ttl: Optional[_builtins.str] = ...,
        subscription_state_override_actions: Optional[
            Sequence[outputs.SubscriptionStateOverrideActionResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="softDeleteTTL")
    def soft_delete_ttl(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionStateOverrideActions")
    def subscription_state_override_actions(
        self,
    ) -> Optional[Sequence[outputs.SubscriptionStateOverrideActionResponse]]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesTemplateDeploymentOptionsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        preflight_options: Optional[Sequence[_builtins.str]] = ...,
        preflight_supported: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="preflightOptions")
    def preflight_options(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="preflightSupported")
    def preflight_supported(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ResourceTypeRegistrationPropertiesTemplateDeploymentPolicyResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capabilities: _builtins.str,
        preflight_options: _builtins.str,
        preflight_notifications: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preflightOptions")
    def preflight_options(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="preflightNotifications")
    def preflight_notifications(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceTypeRegistrationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        name: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        kind: Optional[_builtins.str] = ...,
        properties: Optional[outputs.ResourceTypeRegistrationPropertiesResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[outputs.ResourceTypeRegistrationPropertiesResponse]: ...

@pulumi.output_type
class ServiceTreeInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        component_id: Optional[_builtins.str] = ...,
        readiness: Optional[_builtins.str] = ...,
        service_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="componentId")
    def component_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def readiness(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuCapabilityResponse(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class SkuCostResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        meter_id: _builtins.str,
        extended_unit: Optional[_builtins.str] = ...,
        quantity: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="meterId")
    def meter_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedUnit")
    def extended_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def quantity(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class SkuLocationInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: _builtins.str,
        extended_locations: Optional[Sequence[_builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
        zone_details: Optional[Sequence[outputs.SkuZoneDetailResponse]] = ...,
        zones: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocations")
    def extended_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneDetails")
    def zone_details(self) -> Optional[Sequence[outputs.SkuZoneDetailResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SkuResourcePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        sku_settings: Sequence[outputs.SkuSettingResponse],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="skuSettings")
    def sku_settings(self) -> Sequence[outputs.SkuSettingResponse]: ...

@pulumi.output_type
class SkuSettingCapacityResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        minimum: _builtins.int,
        default: Optional[_builtins.int] = ...,
        maximum: Optional[_builtins.int] = ...,
        scale_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        capabilities: Optional[Sequence[outputs.SkuCapabilityResponse]] = ...,
        capacity: Optional[outputs.SkuSettingCapacityResponse] = ...,
        costs: Optional[Sequence[outputs.SkuCostResponse]] = ...,
        family: Optional[_builtins.str] = ...,
        kind: Optional[_builtins.str] = ...,
        location_info: Optional[Sequence[outputs.SkuLocationInfoResponse]] = ...,
        locations: Optional[Sequence[_builtins.str]] = ...,
        required_features: Optional[Sequence[_builtins.str]] = ...,
        required_quota_ids: Optional[Sequence[_builtins.str]] = ...,
        size: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[outputs.SkuCapabilityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[outputs.SkuSettingCapacityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def costs(self) -> Optional[Sequence[outputs.SkuCostResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="locationInfo")
    def location_info(self) -> Optional[Sequence[outputs.SkuLocationInfoResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requiredQuotaIds")
    def required_quota_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SkuZoneDetailResponse(dict):
    def __init__(
        __self__,
        *,
        capabilities: Optional[Sequence[outputs.SkuCapabilityResponse]] = ...,
        name: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capabilities(self) -> Optional[Sequence[outputs.SkuCapabilityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SubscriberSettingResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter_rules: Optional[Sequence[outputs.FilterRuleResponse]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterRules")
    def filter_rules(self) -> Optional[Sequence[outputs.FilterRuleResponse]]: ...

@pulumi.output_type
class SubscriptionStateOverrideActionResponse(dict):
    def __init__(__self__, *, action: _builtins.str, state: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class SubscriptionStateRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allowed_actions: Optional[Sequence[_builtins.str]] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedActions")
    def allowed_actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SwaggerSpecificationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_versions: Optional[Sequence[_builtins.str]] = ...,
        swagger_spec_folder_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiVersions")
    def api_versions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="swaggerSpecFolderUri")
    def swagger_spec_folder_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ThirdPartyExtensionResponse(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ThrottlingMetricResponse(dict):
    def __init__(
        __self__,
        *,
        limit: _builtins.float,
        type: _builtins.str,
        interval: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limit(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ThrottlingRuleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        metrics: Sequence[outputs.ThrottlingMetricResponse],
        application_id: Optional[Sequence[_builtins.str]] = ...,
        required_features: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metrics(self) -> Sequence[outputs.ThrottlingMetricResponse]: ...
    @_builtins.property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requiredFeatures")
    def required_features(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class TokenAuthConfigurationResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        authentication_scheme: Optional[_builtins.str] = ...,
        disable_certificate_authentication_fallback: Optional[_builtins.bool] = ...,
        signed_request_scope: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authenticationScheme")
    def authentication_scheme(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableCertificateAuthenticationFallback")
    def disable_certificate_authentication_fallback(
        self,
    ) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="signedRequestScope")
    def signed_request_scope(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TypedErrorInfoResponse(dict):
    def __init__(__self__, *, info: Any, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def info(self) -> Any: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
