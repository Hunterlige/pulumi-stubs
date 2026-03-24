

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAzureServersSettingResult', 'AwaitableGetAzureServersSettingResult', 'get_azure_servers_setting', 'get_azure_servers_setting_output']
@pulumi.output_type
class GetAzureServersSettingResult:
    
    def __init__(__self__, azure_api_version=..., id=..., kind=..., name=..., selected_provider=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedProvider")
    def selected_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAzureServersSettingResult(GetAzureServersSettingResult):
    def __await__(self): # -> Generator[Never, Any, GetAzureServersSettingResult]:
        ...
    


def get_azure_servers_setting(setting_kind: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAzureServersSettingResult:
    
    ...

def get_azure_servers_setting_output(setting_kind: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAzureServersSettingResult]:
    
    ...

