

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetContainerAppsAuthConfigResult', 'AwaitableGetContainerAppsAuthConfigResult', 'get_container_apps_auth_config', 'get_container_apps_auth_config_output']
@pulumi.output_type
class GetContainerAppsAuthConfigResult:
    
    def __init__(__self__, azure_api_version=..., encryption_settings=..., global_validation=..., http_settings=..., id=..., identity_providers=..., login=..., name=..., platform=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionSettings")
    def encryption_settings(self) -> Optional[outputs.EncryptionSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalValidation")
    def global_validation(self) -> Optional[outputs.GlobalValidationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpSettings")
    def http_settings(self) -> Optional[outputs.HttpSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityProviders")
    def identity_providers(self) -> Optional[outputs.IdentityProvidersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def login(self) -> Optional[outputs.LoginResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[outputs.AuthPlatformResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetContainerAppsAuthConfigResult(GetContainerAppsAuthConfigResult):
    def __await__(self): # -> Generator[Never, Any, GetContainerAppsAuthConfigResult]:
        ...
    


def get_container_apps_auth_config(auth_config_name: Optional[_builtins.str] = ..., container_app_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetContainerAppsAuthConfigResult:
    
    ...

def get_container_apps_auth_config_output(auth_config_name: Optional[pulumi.Input[_builtins.str]] = ..., container_app_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetContainerAppsAuthConfigResult]:
    
    ...

