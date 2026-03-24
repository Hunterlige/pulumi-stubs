

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WebAppSiteContainerArgs', 'WebAppSiteContainer']
@pulumi.input_type
class WebAppSiteContainerArgs:
    def __init__(__self__, *, image: pulumi.Input[_builtins.str], is_main: pulumi.Input[_builtins.bool], name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], auth_type: Optional[pulumi.Input[AuthType]] = ..., container_name: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]] = ..., inherit_app_settings_and_connection_strings: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., password_secret: Optional[pulumi.Input[_builtins.str]] = ..., start_up_command: Optional[pulumi.Input[_builtins.str]] = ..., target_port: Optional[pulumi.Input[_builtins.str]] = ..., user_managed_identity_client_id: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_mounts: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMain")
    def is_main(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @is_main.setter
    def is_main(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[AuthType]]:
        
        ...
    
    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[AuthType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritAppSettingsAndConnectionStrings")
    def inherit_app_settings_and_connection_strings(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @inherit_app_settings_and_connection_strings.setter
    def inherit_app_settings_and_connection_strings(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecret")
    def password_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_secret.setter
    def password_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startUpCommand")
    def start_up_command(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_up_command.setter
    def start_up_command(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_port.setter
    def target_port(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManagedIdentityClientId")
    def user_managed_identity_client_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_managed_identity_client_id.setter
    def user_managed_identity_client_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]:
        
        ...
    
    @volume_mounts.setter
    def volume_mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:web:WebAppSiteContainer")
class WebAppSiteContainer(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auth_type: Optional[pulumi.Input[AuthType]] = ..., container_name: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[Union[EnvironmentVariableArgs, EnvironmentVariableArgsDict]]]]] = ..., image: Optional[pulumi.Input[_builtins.str]] = ..., inherit_app_settings_and_connection_strings: Optional[pulumi.Input[_builtins.bool]] = ..., is_main: Optional[pulumi.Input[_builtins.bool]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., password_secret: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., start_up_command: Optional[pulumi.Input[_builtins.str]] = ..., target_port: Optional[pulumi.Input[_builtins.str]] = ..., user_managed_identity_client_id: Optional[pulumi.Input[_builtins.str]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_mounts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VolumeMountArgs, VolumeMountArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebAppSiteContainerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WebAppSiteContainer:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> pulumi.Output[Optional[Sequence[outputs.EnvironmentVariableResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritAppSettingsAndConnectionStrings")
    def inherit_app_settings_and_connection_strings(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMain")
    def is_main(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecret")
    def password_secret(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startUpCommand")
    def start_up_command(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManagedIdentityClientId")
    def user_managed_identity_client_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> pulumi.Output[Optional[Sequence[outputs.VolumeMountResponse]]]:
        
        ...
    


