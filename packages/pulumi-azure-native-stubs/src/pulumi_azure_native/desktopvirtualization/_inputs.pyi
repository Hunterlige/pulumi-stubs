

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AgentUpdatePropertiesArgs', 'AgentUpdatePropertiesArgsDict', 'AppAttachPackageInfoPropertiesArgs', 'AppAttachPackageInfoPropertiesArgsDict', 'AppAttachPackagePropertiesArgs', 'AppAttachPackagePropertiesArgsDict', 'MaintenanceWindowPropertiesArgs', 'MaintenanceWindowPropertiesArgsDict', 'MsixPackageApplicationsArgs', 'MsixPackageApplicationsArgsDict', 'MsixPackageDependenciesArgs', 'MsixPackageDependenciesArgsDict', 'PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict', 'RegistrationInfoArgs', 'RegistrationInfoArgsDict', 'ResourceModelWithAllowedPropertySetIdentityArgs', ..., 'ResourceModelWithAllowedPropertySetPlanArgs', 'ResourceModelWithAllowedPropertySetPlanArgsDict', 'ResourceModelWithAllowedPropertySetSkuArgs', 'ResourceModelWithAllowedPropertySetSkuArgsDict', 'ScalingHostPoolReferenceArgs', 'ScalingHostPoolReferenceArgsDict', 'ScalingScheduleArgs', 'ScalingScheduleArgsDict', 'TimeArgs', 'TimeArgsDict']
class AgentUpdatePropertiesArgsDict(TypedDict):
    
    maintenance_window_time_zone: NotRequired[pulumi.Input[_builtins.str]]
    maintenance_windows: NotRequired[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowPropertiesArgsDict]]]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, SessionHostComponentUpdateType]]]
    use_session_host_local_time: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class AgentUpdatePropertiesArgs:
    def __init__(__self__, *, maintenance_window_time_zone: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowPropertiesArgs]]]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, SessionHostComponentUpdateType]]] = ..., use_session_host_local_time: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindowTimeZone")
    def maintenance_window_time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @maintenance_window_time_zone.setter
    def maintenance_window_time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowPropertiesArgs]]]]:
        
        ...
    
    @maintenance_windows.setter
    def maintenance_windows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MaintenanceWindowPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHostComponentUpdateType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHostComponentUpdateType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useSessionHostLocalTime")
    def use_session_host_local_time(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_session_host_local_time.setter
    def use_session_host_local_time(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class AppAttachPackageInfoPropertiesArgsDict(TypedDict):
    
    certificate_expiry: NotRequired[pulumi.Input[_builtins.str]]
    certificate_name: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    image_path: NotRequired[pulumi.Input[_builtins.str]]
    is_active: NotRequired[pulumi.Input[_builtins.bool]]
    is_package_timestamped: NotRequired[pulumi.Input[Union[_builtins.str, PackageTimestamped]]]
    is_regular_registration: NotRequired[pulumi.Input[_builtins.bool]]
    last_updated: NotRequired[pulumi.Input[_builtins.str]]
    package_alias: NotRequired[pulumi.Input[_builtins.str]]
    package_applications: NotRequired[pulumi.Input[Sequence[pulumi.Input[MsixPackageApplicationsArgsDict]]]]
    package_dependencies: NotRequired[pulumi.Input[Sequence[pulumi.Input[MsixPackageDependenciesArgsDict]]]]
    package_family_name: NotRequired[pulumi.Input[_builtins.str]]
    package_full_name: NotRequired[pulumi.Input[_builtins.str]]
    package_name: NotRequired[pulumi.Input[_builtins.str]]
    package_relative_path: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppAttachPackageInfoPropertiesArgs:
    def __init__(__self__, *, certificate_expiry: Optional[pulumi.Input[_builtins.str]] = ..., certificate_name: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., image_path: Optional[pulumi.Input[_builtins.str]] = ..., is_active: Optional[pulumi.Input[_builtins.bool]] = ..., is_package_timestamped: Optional[pulumi.Input[Union[_builtins.str, PackageTimestamped]]] = ..., is_regular_registration: Optional[pulumi.Input[_builtins.bool]] = ..., last_updated: Optional[pulumi.Input[_builtins.str]] = ..., package_alias: Optional[pulumi.Input[_builtins.str]] = ..., package_applications: Optional[pulumi.Input[Sequence[pulumi.Input[MsixPackageApplicationsArgs]]]] = ..., package_dependencies: Optional[pulumi.Input[Sequence[pulumi.Input[MsixPackageDependenciesArgs]]]] = ..., package_family_name: Optional[pulumi.Input[_builtins.str]] = ..., package_full_name: Optional[pulumi.Input[_builtins.str]] = ..., package_name: Optional[pulumi.Input[_builtins.str]] = ..., package_relative_path: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateExpiry")
    def certificate_expiry(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_expiry.setter
    def certificate_expiry(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imagePath")
    def image_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_path.setter
    def image_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_active.setter
    def is_active(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPackageTimestamped")
    def is_package_timestamped(self) -> Optional[pulumi.Input[Union[_builtins.str, PackageTimestamped]]]:
        
        ...
    
    @is_package_timestamped.setter
    def is_package_timestamped(self, value: Optional[pulumi.Input[Union[_builtins.str, PackageTimestamped]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isRegularRegistration")
    def is_regular_registration(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_regular_registration.setter
    def is_regular_registration(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageAlias")
    def package_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_alias.setter
    def package_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageApplications")
    def package_applications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MsixPackageApplicationsArgs]]]]:
        
        ...
    
    @package_applications.setter
    def package_applications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MsixPackageApplicationsArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageDependencies")
    def package_dependencies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MsixPackageDependenciesArgs]]]]:
        
        ...
    
    @package_dependencies.setter
    def package_dependencies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MsixPackageDependenciesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageFamilyName")
    def package_family_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_family_name.setter
    def package_family_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageFullName")
    def package_full_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_full_name.setter
    def package_full_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageName")
    def package_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_name.setter
    def package_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="packageRelativePath")
    def package_relative_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @package_relative_path.setter
    def package_relative_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AppAttachPackagePropertiesArgsDict(TypedDict):
    
    fail_health_check_on_staging_failure: NotRequired[pulumi.Input[Union[_builtins.str, FailHealthCheckOnStagingFailure]]]
    host_pool_references: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    image: NotRequired[pulumi.Input[AppAttachPackageInfoPropertiesArgsDict]]
    key_vault_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AppAttachPackagePropertiesArgs:
    def __init__(__self__, *, fail_health_check_on_staging_failure: Optional[pulumi.Input[Union[_builtins.str, FailHealthCheckOnStagingFailure]]] = ..., host_pool_references: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., image: Optional[pulumi.Input[AppAttachPackageInfoPropertiesArgs]] = ..., key_vault_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failHealthCheckOnStagingFailure")
    def fail_health_check_on_staging_failure(self) -> Optional[pulumi.Input[Union[_builtins.str, FailHealthCheckOnStagingFailure]]]:
        
        ...
    
    @fail_health_check_on_staging_failure.setter
    def fail_health_check_on_staging_failure(self, value: Optional[pulumi.Input[Union[_builtins.str, FailHealthCheckOnStagingFailure]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPoolReferences")
    def host_pool_references(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @host_pool_references.setter
    def host_pool_references(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[AppAttachPackageInfoPropertiesArgs]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[AppAttachPackageInfoPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVaultURL")
    def key_vault_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_vault_url.setter
    def key_vault_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MaintenanceWindowPropertiesArgsDict(TypedDict):
    
    day_of_week: NotRequired[pulumi.Input[DayOfWeek]]
    hour: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class MaintenanceWindowPropertiesArgs:
    def __init__(__self__, *, day_of_week: Optional[pulumi.Input[DayOfWeek]] = ..., hour: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[DayOfWeek]]:
        
        ...
    
    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[DayOfWeek]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @hour.setter
    def hour(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class MsixPackageApplicationsArgsDict(TypedDict):
    
    app_id: NotRequired[pulumi.Input[_builtins.str]]
    app_user_model_id: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    icon_image_name: NotRequired[pulumi.Input[_builtins.str]]
    raw_icon: NotRequired[pulumi.Input[_builtins.str]]
    raw_png: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MsixPackageApplicationsArgs:
    def __init__(__self__, *, app_id: Optional[pulumi.Input[_builtins.str]] = ..., app_user_model_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., icon_image_name: Optional[pulumi.Input[_builtins.str]] = ..., raw_icon: Optional[pulumi.Input[_builtins.str]] = ..., raw_png: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appUserModelID")
    def app_user_model_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_user_model_id.setter
    def app_user_model_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iconImageName")
    def icon_image_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @icon_image_name.setter
    def icon_image_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawIcon")
    def raw_icon(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @raw_icon.setter
    def raw_icon(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawPng")
    def raw_png(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @raw_png.setter
    def raw_png(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MsixPackageDependenciesArgsDict(TypedDict):
    
    dependency_name: NotRequired[pulumi.Input[_builtins.str]]
    min_version: NotRequired[pulumi.Input[_builtins.str]]
    publisher: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MsixPackageDependenciesArgs:
    def __init__(__self__, *, dependency_name: Optional[pulumi.Input[_builtins.str]] = ..., min_version: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dependencyName")
    def dependency_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dependency_name.setter
    def dependency_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minVersion")
    def min_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @min_version.setter
    def min_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *, actions_required: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]]): # -> None:
        ...
    


class RegistrationInfoArgsDict(TypedDict):
    
    expiration_time: NotRequired[pulumi.Input[_builtins.str]]
    registration_token_operation: NotRequired[pulumi.Input[Union[_builtins.str, RegistrationTokenOperation]]]
    token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegistrationInfoArgs:
    def __init__(__self__, *, expiration_time: Optional[pulumi.Input[_builtins.str]] = ..., registration_token_operation: Optional[pulumi.Input[Union[_builtins.str, RegistrationTokenOperation]]] = ..., token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiration_time.setter
    def expiration_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationTokenOperation")
    def registration_token_operation(self) -> Optional[pulumi.Input[Union[_builtins.str, RegistrationTokenOperation]]]:
        
        ...
    
    @registration_token_operation.setter
    def registration_token_operation(self, value: Optional[pulumi.Input[Union[_builtins.str, RegistrationTokenOperation]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceModelWithAllowedPropertySetIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]


@pulumi.input_type
class ResourceModelWithAllowedPropertySetIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[ResourceIdentityType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): # -> None:
        ...
    


class ResourceModelWithAllowedPropertySetPlanArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    product: pulumi.Input[_builtins.str]
    publisher: pulumi.Input[_builtins.str]
    promotion_code: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceModelWithAllowedPropertySetPlanArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], product: pulumi.Input[_builtins.str], publisher: pulumi.Input[_builtins.str], promotion_code: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @product.setter
    def product(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ResourceModelWithAllowedPropertySetSkuArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    family: NotRequired[pulumi.Input[_builtins.str]]
    size: NotRequired[pulumi.Input[_builtins.str]]
    tier: NotRequired[pulumi.Input[SkuTier]]


@pulumi.input_type
class ResourceModelWithAllowedPropertySetSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], capacity: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.str]] = ..., tier: Optional[pulumi.Input[SkuTier]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[SkuTier]]:
        
        ...
    
    @tier.setter
    def tier(self, value: Optional[pulumi.Input[SkuTier]]): # -> None:
        ...
    


class ScalingHostPoolReferenceArgsDict(TypedDict):
    
    host_pool_arm_path: NotRequired[pulumi.Input[_builtins.str]]
    scaling_plan_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ScalingHostPoolReferenceArgs:
    def __init__(__self__, *, host_pool_arm_path: Optional[pulumi.Input[_builtins.str]] = ..., scaling_plan_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPoolArmPath")
    def host_pool_arm_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @host_pool_arm_path.setter
    def host_pool_arm_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scalingPlanEnabled")
    def scaling_plan_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @scaling_plan_enabled.setter
    def scaling_plan_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ScalingScheduleArgsDict(TypedDict):
    
    days_of_week: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    off_peak_load_balancing_algorithm: NotRequired[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]
    off_peak_start_time: NotRequired[pulumi.Input[TimeArgsDict]]
    peak_load_balancing_algorithm: NotRequired[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]
    peak_start_time: NotRequired[pulumi.Input[TimeArgsDict]]
    ramp_down_capacity_threshold_pct: NotRequired[pulumi.Input[_builtins.int]]
    ramp_down_force_logoff_users: NotRequired[pulumi.Input[_builtins.bool]]
    ramp_down_load_balancing_algorithm: NotRequired[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]
    ramp_down_minimum_hosts_pct: NotRequired[pulumi.Input[_builtins.int]]
    ramp_down_notification_message: NotRequired[pulumi.Input[_builtins.str]]
    ramp_down_start_time: NotRequired[pulumi.Input[TimeArgsDict]]
    ramp_down_stop_hosts_when: NotRequired[pulumi.Input[Union[_builtins.str, StopHostsWhen]]]
    ramp_down_wait_time_minutes: NotRequired[pulumi.Input[_builtins.int]]
    ramp_up_capacity_threshold_pct: NotRequired[pulumi.Input[_builtins.int]]
    ramp_up_load_balancing_algorithm: NotRequired[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]
    ramp_up_minimum_hosts_pct: NotRequired[pulumi.Input[_builtins.int]]
    ramp_up_start_time: NotRequired[pulumi.Input[TimeArgsDict]]


@pulumi.input_type
class ScalingScheduleArgs:
    def __init__(__self__, *, days_of_week: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., off_peak_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., off_peak_start_time: Optional[pulumi.Input[TimeArgs]] = ..., peak_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., peak_start_time: Optional[pulumi.Input[TimeArgs]] = ..., ramp_down_capacity_threshold_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_force_logoff_users: Optional[pulumi.Input[_builtins.bool]] = ..., ramp_down_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., ramp_down_minimum_hosts_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_down_notification_message: Optional[pulumi.Input[_builtins.str]] = ..., ramp_down_start_time: Optional[pulumi.Input[TimeArgs]] = ..., ramp_down_stop_hosts_when: Optional[pulumi.Input[Union[_builtins.str, StopHostsWhen]]] = ..., ramp_down_wait_time_minutes: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_capacity_threshold_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_load_balancing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]] = ..., ramp_up_minimum_hosts_pct: Optional[pulumi.Input[_builtins.int]] = ..., ramp_up_start_time: Optional[pulumi.Input[TimeArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @days_of_week.setter
    def days_of_week(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]:
        
        ...
    
    @off_peak_load_balancing_algorithm.setter
    def off_peak_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @off_peak_start_time.setter
    def off_peak_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]:
        
        ...
    
    @peak_load_balancing_algorithm.setter
    def peak_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @peak_start_time.setter
    def peak_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownCapacityThresholdPct")
    def ramp_down_capacity_threshold_pct(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_down_capacity_threshold_pct.setter
    def ramp_down_capacity_threshold_pct(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ramp_down_force_logoff_users.setter
    def ramp_down_force_logoff_users(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]:
        
        ...
    
    @ramp_down_load_balancing_algorithm.setter
    def ramp_down_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownMinimumHostsPct")
    def ramp_down_minimum_hosts_pct(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_down_minimum_hosts_pct.setter
    def ramp_down_minimum_hosts_pct(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ramp_down_notification_message.setter
    def ramp_down_notification_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @ramp_down_start_time.setter
    def ramp_down_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> Optional[pulumi.Input[Union[_builtins.str, StopHostsWhen]]]:
        
        ...
    
    @ramp_down_stop_hosts_when.setter
    def ramp_down_stop_hosts_when(self, value: Optional[pulumi.Input[Union[_builtins.str, StopHostsWhen]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_down_wait_time_minutes.setter
    def ramp_down_wait_time_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpCapacityThresholdPct")
    def ramp_up_capacity_threshold_pct(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_up_capacity_threshold_pct.setter
    def ramp_up_capacity_threshold_pct(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]:
        
        ...
    
    @ramp_up_load_balancing_algorithm.setter
    def ramp_up_load_balancing_algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, SessionHostLoadBalancingAlgorithm]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpMinimumHostsPct")
    def ramp_up_minimum_hosts_pct(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @ramp_up_minimum_hosts_pct.setter
    def ramp_up_minimum_hosts_pct(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> Optional[pulumi.Input[TimeArgs]]:
        
        ...
    
    @ramp_up_start_time.setter
    def ramp_up_start_time(self, value: Optional[pulumi.Input[TimeArgs]]): # -> None:
        ...
    


class TimeArgsDict(TypedDict):
    
    hour: pulumi.Input[_builtins.int]
    minute: pulumi.Input[_builtins.int]


@pulumi.input_type
class TimeArgs:
    def __init__(__self__, *, hour: pulumi.Input[_builtins.int], minute: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @hour.setter
    def hour(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @minute.setter
    def minute(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


