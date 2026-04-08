import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AgentUpdatePropertiesResponse",
    "AppAttachPackageInfoPropertiesResponse",
    "AppAttachPackagePropertiesResponse",
    "MaintenanceWindowPropertiesResponse",
    "MsixPackageApplicationsResponse",
    "MsixPackageDependenciesResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "RegistrationInfoResponse",
    "RegistrationTokenMinimalResponse",
    ...,
    "ResourceModelWithAllowedPropertySetResponsePlan",
    "ResourceModelWithAllowedPropertySetResponseSku",
    "ScalingHostPoolReferenceResponse",
    "ScalingScheduleResponse",
    "SessionHostHealthCheckFailureDetailsResponse",
    "SessionHostHealthCheckReportResponse",
    "SystemDataResponse",
    "TimeResponse",
]

@pulumi.output_type
class AgentUpdatePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maintenance_window_time_zone: Optional[_builtins.str] = ...,
        maintenance_windows: Optional[
            Sequence[outputs.MaintenanceWindowPropertiesResponse]
        ] = ...,
        type: Optional[_builtins.str] = ...,
        use_session_host_local_time: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowTimeZone")
    def maintenance_window_time_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(
        self,
    ) -> Optional[Sequence[outputs.MaintenanceWindowPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useSessionHostLocalTime")
    def use_session_host_local_time(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class AppAttachPackageInfoPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_expiry: Optional[_builtins.str] = ...,
        certificate_name: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        image_path: Optional[_builtins.str] = ...,
        is_active: Optional[_builtins.bool] = ...,
        is_package_timestamped: Optional[_builtins.str] = ...,
        is_regular_registration: Optional[_builtins.bool] = ...,
        last_updated: Optional[_builtins.str] = ...,
        package_alias: Optional[_builtins.str] = ...,
        package_applications: Optional[
            Sequence[outputs.MsixPackageApplicationsResponse]
        ] = ...,
        package_dependencies: Optional[
            Sequence[outputs.MsixPackageDependenciesResponse]
        ] = ...,
        package_family_name: Optional[_builtins.str] = ...,
        package_full_name: Optional[_builtins.str] = ...,
        package_name: Optional[_builtins.str] = ...,
        package_relative_path: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateExpiry")
    def certificate_expiry(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imagePath")
    def image_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isPackageTimestamped")
    def is_package_timestamped(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isRegularRegistration")
    def is_regular_registration(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageAlias")
    def package_alias(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageApplications")
    def package_applications(
        self,
    ) -> Optional[Sequence[outputs.MsixPackageApplicationsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="packageDependencies")
    def package_dependencies(
        self,
    ) -> Optional[Sequence[outputs.MsixPackageDependenciesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="packageFamilyName")
    def package_family_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageFullName")
    def package_full_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="packageRelativePath")
    def package_relative_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppAttachPackagePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        provisioning_state: _builtins.str,
        fail_health_check_on_staging_failure: Optional[_builtins.str] = ...,
        host_pool_references: Optional[Sequence[_builtins.str]] = ...,
        image: Optional[outputs.AppAttachPackageInfoPropertiesResponse] = ...,
        key_vault_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failHealthCheckOnStagingFailure")
    def fail_health_check_on_staging_failure(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostPoolReferences")
    def host_pool_references(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[outputs.AppAttachPackageInfoPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="keyVaultURL")
    def key_vault_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MaintenanceWindowPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day_of_week: Optional[_builtins.str] = ...,
        hour: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class MsixPackageApplicationsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_id: Optional[_builtins.str] = ...,
        app_user_model_id: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        friendly_name: Optional[_builtins.str] = ...,
        icon_image_name: Optional[_builtins.str] = ...,
        raw_icon: Optional[_builtins.str] = ...,
        raw_png: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="appUserModelID")
    def app_user_model_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iconImageName")
    def icon_image_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rawIcon")
    def raw_icon(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rawPng")
    def raw_png(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MsixPackageDependenciesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dependency_name: Optional[_builtins.str] = ...,
        min_version: Optional[_builtins.str] = ...,
        publisher: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dependencyName")
    def dependency_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minVersion")
    def min_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_ids: Sequence[_builtins.str],
        id: _builtins.str,
        name: _builtins.str,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...

@pulumi.output_type
class PrivateEndpointResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegistrationInfoResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        expiration_time: Optional[_builtins.str] = ...,
        registration_token_operation: Optional[_builtins.str] = ...,
        token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registrationTokenOperation")
    def registration_token_operation(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RegistrationTokenMinimalResponse(dict):
    def __init__(
        __self__,
        *,
        expiration_time: Optional[_builtins.str] = ...,
        token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceModelWithAllowedPropertySetResponseIdentity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        principal_id: _builtins.str,
        tenant_id: _builtins.str,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceModelWithAllowedPropertySetResponsePlan(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        product: _builtins.str,
        publisher: _builtins.str,
        promotion_code: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ResourceModelWithAllowedPropertySetResponseSku(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        capacity: Optional[_builtins.int] = ...,
        family: Optional[_builtins.str] = ...,
        size: Optional[_builtins.str] = ...,
        tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ScalingHostPoolReferenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_pool_arm_path: Optional[_builtins.str] = ...,
        scaling_plan_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostPoolArmPath")
    def host_pool_arm_path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scalingPlanEnabled")
    def scaling_plan_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ScalingScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days_of_week: Optional[Sequence[_builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        off_peak_load_balancing_algorithm: Optional[_builtins.str] = ...,
        off_peak_start_time: Optional[outputs.TimeResponse] = ...,
        peak_load_balancing_algorithm: Optional[_builtins.str] = ...,
        peak_start_time: Optional[outputs.TimeResponse] = ...,
        ramp_down_capacity_threshold_pct: Optional[_builtins.int] = ...,
        ramp_down_force_logoff_users: Optional[_builtins.bool] = ...,
        ramp_down_load_balancing_algorithm: Optional[_builtins.str] = ...,
        ramp_down_minimum_hosts_pct: Optional[_builtins.int] = ...,
        ramp_down_notification_message: Optional[_builtins.str] = ...,
        ramp_down_start_time: Optional[outputs.TimeResponse] = ...,
        ramp_down_stop_hosts_when: Optional[_builtins.str] = ...,
        ramp_down_wait_time_minutes: Optional[_builtins.int] = ...,
        ramp_up_capacity_threshold_pct: Optional[_builtins.int] = ...,
        ramp_up_load_balancing_algorithm: Optional[_builtins.str] = ...,
        ramp_up_minimum_hosts_pct: Optional[_builtins.int] = ...,
        ramp_up_start_time: Optional[outputs.TimeResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> Optional[outputs.TimeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> Optional[outputs.TimeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownCapacityThresholdPct")
    def ramp_down_capacity_threshold_pct(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownMinimumHostsPct")
    def ramp_down_minimum_hosts_pct(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> Optional[outputs.TimeResponse]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampUpCapacityThresholdPct")
    def ramp_up_capacity_threshold_pct(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rampUpMinimumHostsPct")
    def ramp_up_minimum_hosts_pct(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> Optional[outputs.TimeResponse]: ...

@pulumi.output_type
class SessionHostHealthCheckFailureDetailsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        error_code: _builtins.int,
        last_health_check_date_time: _builtins.str,
        message: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="lastHealthCheckDateTime")
    def last_health_check_date_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...

@pulumi.output_type
class SessionHostHealthCheckReportResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        additional_failure_details: outputs.SessionHostHealthCheckFailureDetailsResponse,
        health_check_name: _builtins.str,
        health_check_result: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalFailureDetails")
    def additional_failure_details(
        self,
    ) -> outputs.SessionHostHealthCheckFailureDetailsResponse: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckName")
    def health_check_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckResult")
    def health_check_result(self) -> _builtins.str: ...

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
class TimeResponse(dict):
    def __init__(__self__, *, hour: _builtins.int, minute: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hour(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minute(self) -> _builtins.int: ...
