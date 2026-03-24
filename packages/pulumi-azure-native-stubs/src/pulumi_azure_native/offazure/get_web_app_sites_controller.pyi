

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppSitesControllerResult', 'AwaitableGetWebAppSitesControllerResult', 'get_web_app_sites_controller', 'get_web_app_sites_controller_output']
@pulumi.output_type
class GetWebAppSitesControllerResult:
    
    def __init__(__self__, azure_api_version=..., discovery_scenario=..., id=..., name=..., provisioning_state=..., service_endpoint=..., site_appliance_properties_collection=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryScenario")
    def discovery_scenario(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteAppliancePropertiesCollection")
    def site_appliance_properties_collection(self) -> Optional[Sequence[outputs.SiteAppliancePropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebAppSitesControllerResult(GetWebAppSitesControllerResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppSitesControllerResult]:
        ...
    


def get_web_app_sites_controller(resource_group_name: Optional[_builtins.str] = ..., site_name: Optional[_builtins.str] = ..., web_app_site_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppSitesControllerResult:
    
    ...

def get_web_app_sites_controller_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., site_name: Optional[pulumi.Input[_builtins.str]] = ..., web_app_site_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppSitesControllerResult]:
    
    ...

