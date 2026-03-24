

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppDiscoverySiteDataSourcesControllerResult', ..., 'get_web_app_discovery_site_data_sources_controller', ...]
@pulumi.output_type
class GetWebAppDiscoverySiteDataSourcesControllerResult:
    
    def __init__(__self__, azure_api_version=..., discovery_site_id=..., id=..., name=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebAppDiscoverySiteDataSourcesControllerResult(GetWebAppDiscoverySiteDataSourcesControllerResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppDiscoverySiteDataSourcesControllerResult]:
        ...
    


def get_web_app_discovery_site_data_sources_controller(discovery_site_data_source_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., site_name: Optional[_builtins.str] = ..., web_app_site_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppDiscoverySiteDataSourcesControllerResult:
    
    ...

def get_web_app_discovery_site_data_sources_controller_output(discovery_site_data_source_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., site_name: Optional[pulumi.Input[_builtins.str]] = ..., web_app_site_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppDiscoverySiteDataSourcesControllerResult]:
    
    ...

