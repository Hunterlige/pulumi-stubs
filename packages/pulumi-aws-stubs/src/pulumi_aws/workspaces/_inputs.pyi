

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectionAliasTimeoutsArgs', 'ConnectionAliasTimeoutsArgsDict', 'DirectoryActiveDirectoryConfigArgs', 'DirectoryActiveDirectoryConfigArgsDict', 'DirectoryCertificateBasedAuthPropertiesArgs', 'DirectoryCertificateBasedAuthPropertiesArgsDict', 'DirectorySamlPropertiesArgs', 'DirectorySamlPropertiesArgsDict', 'DirectorySelfServicePermissionsArgs', 'DirectorySelfServicePermissionsArgsDict', 'DirectoryWorkspaceAccessPropertiesArgs', 'DirectoryWorkspaceAccessPropertiesArgsDict', 'DirectoryWorkspaceCreationPropertiesArgs', 'DirectoryWorkspaceCreationPropertiesArgsDict', 'IpGroupRuleArgs', 'IpGroupRuleArgsDict', 'WorkspaceWorkspacePropertiesArgs', 'WorkspaceWorkspacePropertiesArgsDict']
class ConnectionAliasTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConnectionAliasTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DirectoryActiveDirectoryConfigArgsDict(TypedDict):
    domain_name: pulumi.Input[_builtins.str]
    service_account_secret_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class DirectoryActiveDirectoryConfigArgs:
    def __init__(__self__, *, domain_name: pulumi.Input[_builtins.str], service_account_secret_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain_name.setter
    def domain_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountSecretArn")
    def service_account_secret_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_account_secret_arn.setter
    def service_account_secret_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DirectoryCertificateBasedAuthPropertiesArgsDict(TypedDict):
    certificate_authority_arn: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DirectoryCertificateBasedAuthPropertiesArgs:
    def __init__(__self__, *, certificate_authority_arn: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DirectorySamlPropertiesArgsDict(TypedDict):
    relay_state_parameter_name: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    user_access_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DirectorySamlPropertiesArgs:
    def __init__(__self__, *, relay_state_parameter_name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., user_access_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relayStateParameterName")
    def relay_state_parameter_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @relay_state_parameter_name.setter
    def relay_state_parameter_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAccessUrl")
    def user_access_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_access_url.setter
    def user_access_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DirectorySelfServicePermissionsArgsDict(TypedDict):
    change_compute_type: NotRequired[pulumi.Input[_builtins.bool]]
    increase_volume_size: NotRequired[pulumi.Input[_builtins.bool]]
    rebuild_workspace: NotRequired[pulumi.Input[_builtins.bool]]
    restart_workspace: NotRequired[pulumi.Input[_builtins.bool]]
    switch_running_mode: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DirectorySelfServicePermissionsArgs:
    def __init__(__self__, *, change_compute_type: Optional[pulumi.Input[_builtins.bool]] = ..., increase_volume_size: Optional[pulumi.Input[_builtins.bool]] = ..., rebuild_workspace: Optional[pulumi.Input[_builtins.bool]] = ..., restart_workspace: Optional[pulumi.Input[_builtins.bool]] = ..., switch_running_mode: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changeComputeType")
    def change_compute_type(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @change_compute_type.setter
    def change_compute_type(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="increaseVolumeSize")
    def increase_volume_size(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @increase_volume_size.setter
    def increase_volume_size(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rebuildWorkspace")
    def rebuild_workspace(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @rebuild_workspace.setter
    def rebuild_workspace(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restartWorkspace")
    def restart_workspace(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @restart_workspace.setter
    def restart_workspace(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="switchRunningMode")
    def switch_running_mode(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @switch_running_mode.setter
    def switch_running_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class DirectoryWorkspaceAccessPropertiesArgsDict(TypedDict):
    device_type_android: NotRequired[pulumi.Input[_builtins.str]]
    device_type_chromeos: NotRequired[pulumi.Input[_builtins.str]]
    device_type_ios: NotRequired[pulumi.Input[_builtins.str]]
    device_type_linux: NotRequired[pulumi.Input[_builtins.str]]
    device_type_osx: NotRequired[pulumi.Input[_builtins.str]]
    device_type_web: NotRequired[pulumi.Input[_builtins.str]]
    device_type_windows: NotRequired[pulumi.Input[_builtins.str]]
    device_type_zeroclient: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DirectoryWorkspaceAccessPropertiesArgs:
    def __init__(__self__, *, device_type_android: Optional[pulumi.Input[_builtins.str]] = ..., device_type_chromeos: Optional[pulumi.Input[_builtins.str]] = ..., device_type_ios: Optional[pulumi.Input[_builtins.str]] = ..., device_type_linux: Optional[pulumi.Input[_builtins.str]] = ..., device_type_osx: Optional[pulumi.Input[_builtins.str]] = ..., device_type_web: Optional[pulumi.Input[_builtins.str]] = ..., device_type_windows: Optional[pulumi.Input[_builtins.str]] = ..., device_type_zeroclient: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTypeAndroid")
    def device_type_android(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_type_android.setter
    def device_type_android(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTypeChromeos")
    def device_type_chromeos(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_type_chromeos.setter
    def device_type_chromeos(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTypeIos")
    def device_type_ios(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_type_ios.setter
    def device_type_ios(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTypeLinux")
    def device_type_linux(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_type_linux.setter
    def device_type_linux(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTypeOsx")
    def device_type_osx(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_type_osx.setter
    def device_type_osx(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTypeWeb")
    def device_type_web(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_type_web.setter
    def device_type_web(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTypeWindows")
    def device_type_windows(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_type_windows.setter
    def device_type_windows(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceTypeZeroclient")
    def device_type_zeroclient(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @device_type_zeroclient.setter
    def device_type_zeroclient(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class DirectoryWorkspaceCreationPropertiesArgsDict(TypedDict):
    custom_security_group_id: NotRequired[pulumi.Input[_builtins.str]]
    default_ou: NotRequired[pulumi.Input[_builtins.str]]
    enable_internet_access: NotRequired[pulumi.Input[_builtins.bool]]
    enable_maintenance_mode: NotRequired[pulumi.Input[_builtins.bool]]
    user_enabled_as_local_administrator: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class DirectoryWorkspaceCreationPropertiesArgs:
    def __init__(__self__, *, custom_security_group_id: Optional[pulumi.Input[_builtins.str]] = ..., default_ou: Optional[pulumi.Input[_builtins.str]] = ..., enable_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., enable_maintenance_mode: Optional[pulumi.Input[_builtins.bool]] = ..., user_enabled_as_local_administrator: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customSecurityGroupId")
    def custom_security_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_security_group_id.setter
    def custom_security_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultOu")
    def default_ou(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_ou.setter
    def default_ou(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInternetAccess")
    def enable_internet_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_internet_access.setter
    def enable_internet_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMaintenanceMode")
    def enable_maintenance_mode(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_maintenance_mode.setter
    def enable_maintenance_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userEnabledAsLocalAdministrator")
    def user_enabled_as_local_administrator(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @user_enabled_as_local_administrator.setter
    def user_enabled_as_local_administrator(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class IpGroupRuleArgsDict(TypedDict):
    source: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IpGroupRuleArgs:
    def __init__(__self__, *, source: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkspaceWorkspacePropertiesArgsDict(TypedDict):
    compute_type_name: NotRequired[pulumi.Input[_builtins.str]]
    root_volume_size_gib: NotRequired[pulumi.Input[_builtins.int]]
    running_mode: NotRequired[pulumi.Input[_builtins.str]]
    running_mode_auto_stop_timeout_in_minutes: NotRequired[pulumi.Input[_builtins.int]]
    user_volume_size_gib: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class WorkspaceWorkspacePropertiesArgs:
    def __init__(__self__, *, compute_type_name: Optional[pulumi.Input[_builtins.str]] = ..., root_volume_size_gib: Optional[pulumi.Input[_builtins.int]] = ..., running_mode: Optional[pulumi.Input[_builtins.str]] = ..., running_mode_auto_stop_timeout_in_minutes: Optional[pulumi.Input[_builtins.int]] = ..., user_volume_size_gib: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeTypeName")
    def compute_type_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compute_type_name.setter
    def compute_type_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootVolumeSizeGib")
    def root_volume_size_gib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @root_volume_size_gib.setter
    def root_volume_size_gib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runningMode")
    def running_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @running_mode.setter
    def running_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runningModeAutoStopTimeoutInMinutes")
    def running_mode_auto_stop_timeout_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @running_mode_auto_stop_timeout_in_minutes.setter
    def running_mode_auto_stop_timeout_in_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userVolumeSizeGib")
    def user_volume_size_gib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @user_volume_size_gib.setter
    def user_volume_size_gib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


