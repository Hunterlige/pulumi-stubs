

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppSlotConfigurationNamesResult', 'AwaitableGetWebAppSlotConfigurationNamesResult', 'get_web_app_slot_configuration_names', 'get_web_app_slot_configuration_names_output']
@pulumi.output_type
class GetWebAppSlotConfigurationNamesResult:
    
    def __init__(__self__, app_setting_names=..., azure_api_version=..., azure_storage_config_names=..., connection_string_names=..., id=..., kind=..., name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appSettingNames")
    def app_setting_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureStorageConfigNames")
    def azure_storage_config_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStringNames")
    def connection_string_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebAppSlotConfigurationNamesResult(GetWebAppSlotConfigurationNamesResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppSlotConfigurationNamesResult]:
        ...
    


def get_web_app_slot_configuration_names(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppSlotConfigurationNamesResult:
    
    ...

def get_web_app_slot_configuration_names_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppSlotConfigurationNamesResult]:
    
    ...

