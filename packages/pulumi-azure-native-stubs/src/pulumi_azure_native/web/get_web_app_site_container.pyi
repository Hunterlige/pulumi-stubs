

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppSiteContainerResult', 'AwaitableGetWebAppSiteContainerResult', 'get_web_app_site_container', 'get_web_app_site_container_output']
@pulumi.output_type
class GetWebAppSiteContainerResult:
    
    def __init__(__self__, auth_type=..., azure_api_version=..., created_time=..., environment_variables=..., id=..., image=..., inherit_app_settings_and_connection_strings=..., is_main=..., kind=..., last_modified_time=..., name=..., password_secret=..., start_up_command=..., target_port=..., type=..., user_managed_identity_client_id=..., user_name=..., volume_mounts=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Sequence[outputs.EnvironmentVariableResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritAppSettingsAndConnectionStrings")
    def inherit_app_settings_and_connection_strings(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isMain")
    def is_main(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordSecret")
    def password_secret(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startUpCommand")
    def start_up_command(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPort")
    def target_port(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManagedIdentityClientId")
    def user_managed_identity_client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[Sequence[outputs.VolumeMountResponse]]:
        
        ...
    


class AwaitableGetWebAppSiteContainerResult(GetWebAppSiteContainerResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppSiteContainerResult]:
        ...
    


def get_web_app_site_container(container_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppSiteContainerResult:
    
    ...

def get_web_app_site_container_output(container_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppSiteContainerResult]:
    
    ...

