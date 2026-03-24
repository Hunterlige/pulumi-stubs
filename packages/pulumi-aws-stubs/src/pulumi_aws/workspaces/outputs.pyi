import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectionAliasTimeouts",
    "DirectoryActiveDirectoryConfig",
    "DirectoryCertificateBasedAuthProperties",
    "DirectorySamlProperties",
    "DirectorySelfServicePermissions",
    "DirectoryWorkspaceAccessProperties",
    "DirectoryWorkspaceCreationProperties",
    "IpGroupRule",
    "WorkspaceWorkspaceProperties",
    "GetBundleComputeTypeResult",
    "GetBundleRootStorageResult",
    "GetBundleUserStorageResult",
    "GetDirectoryActiveDirectoryConfigResult",
    "GetDirectoryCertificateBasedAuthPropertyResult",
    "GetDirectorySamlPropertyResult",
    "GetDirectorySelfServicePermissionResult",
    "GetDirectoryWorkspaceAccessPropertyResult",
    "GetDirectoryWorkspaceCreationPropertyResult",
    "GetWorkspaceWorkspacePropertyResult",
]

@pulumi.output_type
class ConnectionAliasTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DirectoryActiveDirectoryConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        service_account_secret_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountSecretArn")
    def service_account_secret_arn(self) -> _builtins.str: ...

@pulumi.output_type
class DirectoryCertificateBasedAuthProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        certificate_authority_arn: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DirectorySamlProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        relay_state_parameter_name: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        user_access_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="relayStateParameterName")
    def relay_state_parameter_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userAccessUrl")
    def user_access_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DirectorySelfServicePermissions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        change_compute_type: Optional[_builtins.bool] = ...,
        increase_volume_size: Optional[_builtins.bool] = ...,
        rebuild_workspace: Optional[_builtins.bool] = ...,
        restart_workspace: Optional[_builtins.bool] = ...,
        switch_running_mode: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="changeComputeType")
    def change_compute_type(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="increaseVolumeSize")
    def increase_volume_size(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="rebuildWorkspace")
    def rebuild_workspace(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="restartWorkspace")
    def restart_workspace(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="switchRunningMode")
    def switch_running_mode(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DirectoryWorkspaceAccessProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        device_type_android: Optional[_builtins.str] = ...,
        device_type_chromeos: Optional[_builtins.str] = ...,
        device_type_ios: Optional[_builtins.str] = ...,
        device_type_linux: Optional[_builtins.str] = ...,
        device_type_osx: Optional[_builtins.str] = ...,
        device_type_web: Optional[_builtins.str] = ...,
        device_type_windows: Optional[_builtins.str] = ...,
        device_type_zeroclient: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeAndroid")
    def device_type_android(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeChromeos")
    def device_type_chromeos(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeIos")
    def device_type_ios(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeLinux")
    def device_type_linux(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeOsx")
    def device_type_osx(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeWeb")
    def device_type_web(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeWindows")
    def device_type_windows(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeZeroclient")
    def device_type_zeroclient(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DirectoryWorkspaceCreationProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_security_group_id: Optional[_builtins.str] = ...,
        default_ou: Optional[_builtins.str] = ...,
        enable_internet_access: Optional[_builtins.bool] = ...,
        enable_maintenance_mode: Optional[_builtins.bool] = ...,
        user_enabled_as_local_administrator: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customSecurityGroupId")
    def custom_security_group_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultOu")
    def default_ou(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableInternetAccess")
    def enable_internet_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableMaintenanceMode")
    def enable_maintenance_mode(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="userEnabledAsLocalAdministrator")
    def user_enabled_as_local_administrator(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class IpGroupRule(dict):
    def __init__(
        __self__, *, source: _builtins.str, description: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkspaceWorkspaceProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compute_type_name: Optional[_builtins.str] = ...,
        root_volume_size_gib: Optional[_builtins.int] = ...,
        running_mode: Optional[_builtins.str] = ...,
        running_mode_auto_stop_timeout_in_minutes: Optional[_builtins.int] = ...,
        user_volume_size_gib: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeTypeName")
    def compute_type_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootVolumeSizeGib")
    def root_volume_size_gib(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="runningMode")
    def running_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="runningModeAutoStopTimeoutInMinutes")
    def running_mode_auto_stop_timeout_in_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="userVolumeSizeGib")
    def user_volume_size_gib(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GetBundleComputeTypeResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetBundleRootStorageResult(dict):
    def __init__(__self__, *, capacity: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.str: ...

@pulumi.output_type
class GetBundleUserStorageResult(dict):
    def __init__(__self__, *, capacity: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> _builtins.str: ...

@pulumi.output_type
class GetDirectoryActiveDirectoryConfigResult(dict):
    def __init__(
        __self__,
        *,
        domain_name: _builtins.str,
        service_account_secret_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountSecretArn")
    def service_account_secret_arn(self) -> _builtins.str: ...

@pulumi.output_type
class GetDirectoryCertificateBasedAuthPropertyResult(dict):
    def __init__(
        __self__, *, certificate_authority_arn: _builtins.str, status: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetDirectorySamlPropertyResult(dict):
    def __init__(
        __self__,
        *,
        relay_state_parameter_name: _builtins.str,
        status: _builtins.str,
        user_access_url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="relayStateParameterName")
    def relay_state_parameter_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userAccessUrl")
    def user_access_url(self) -> _builtins.str: ...

@pulumi.output_type
class GetDirectorySelfServicePermissionResult(dict):
    def __init__(
        __self__,
        *,
        change_compute_type: _builtins.bool,
        increase_volume_size: _builtins.bool,
        rebuild_workspace: _builtins.bool,
        restart_workspace: _builtins.bool,
        switch_running_mode: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="changeComputeType")
    def change_compute_type(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="increaseVolumeSize")
    def increase_volume_size(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="rebuildWorkspace")
    def rebuild_workspace(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="restartWorkspace")
    def restart_workspace(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="switchRunningMode")
    def switch_running_mode(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDirectoryWorkspaceAccessPropertyResult(dict):
    def __init__(
        __self__,
        *,
        device_type_android: _builtins.str,
        device_type_chromeos: _builtins.str,
        device_type_ios: _builtins.str,
        device_type_linux: _builtins.str,
        device_type_osx: _builtins.str,
        device_type_web: _builtins.str,
        device_type_windows: _builtins.str,
        device_type_zeroclient: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeAndroid")
    def device_type_android(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeChromeos")
    def device_type_chromeos(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeIos")
    def device_type_ios(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeLinux")
    def device_type_linux(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeOsx")
    def device_type_osx(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeWeb")
    def device_type_web(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeWindows")
    def device_type_windows(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceTypeZeroclient")
    def device_type_zeroclient(self) -> _builtins.str: ...

@pulumi.output_type
class GetDirectoryWorkspaceCreationPropertyResult(dict):
    def __init__(
        __self__,
        *,
        custom_security_group_id: _builtins.str,
        default_ou: _builtins.str,
        enable_internet_access: _builtins.bool,
        enable_maintenance_mode: _builtins.bool,
        user_enabled_as_local_administrator: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customSecurityGroupId")
    def custom_security_group_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultOu")
    def default_ou(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableInternetAccess")
    def enable_internet_access(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="enableMaintenanceMode")
    def enable_maintenance_mode(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="userEnabledAsLocalAdministrator")
    def user_enabled_as_local_administrator(self) -> _builtins.bool: ...

@pulumi.output_type
class GetWorkspaceWorkspacePropertyResult(dict):
    def __init__(
        __self__,
        *,
        compute_type_name: _builtins.str,
        root_volume_size_gib: _builtins.int,
        running_mode: _builtins.str,
        running_mode_auto_stop_timeout_in_minutes: _builtins.int,
        user_volume_size_gib: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeTypeName")
    def compute_type_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootVolumeSizeGib")
    def root_volume_size_gib(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="runningMode")
    def running_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="runningModeAutoStopTimeoutInMinutes")
    def running_mode_auto_stop_timeout_in_minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="userVolumeSizeGib")
    def user_volume_size_gib(self) -> _builtins.int: ...
