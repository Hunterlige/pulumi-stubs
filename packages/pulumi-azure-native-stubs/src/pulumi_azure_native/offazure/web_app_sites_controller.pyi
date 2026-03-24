

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
__all__ = ['WebAppSitesControllerArgs', 'WebAppSitesController']
@pulumi.input_type
class WebAppSitesControllerArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], site_name: pulumi.Input[_builtins.str], discovery_scenario: Optional[pulumi.Input[Union[_builtins.str, WebAppSitePropertiesDiscoveryScenario]]] = ..., site_appliance_properties_collection: Optional[pulumi.Input[Sequence[pulumi.Input[SiteAppliancePropertiesArgs]]]] = ..., web_app_site_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @site_name.setter
    def site_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryScenario")
    def discovery_scenario(self) -> Optional[pulumi.Input[Union[_builtins.str, WebAppSitePropertiesDiscoveryScenario]]]:
        
        ...
    
    @discovery_scenario.setter
    def discovery_scenario(self, value: Optional[pulumi.Input[Union[_builtins.str, WebAppSitePropertiesDiscoveryScenario]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteAppliancePropertiesCollection")
    def site_appliance_properties_collection(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SiteAppliancePropertiesArgs]]]]:
        
        ...
    
    @site_appliance_properties_collection.setter
    def site_appliance_properties_collection(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SiteAppliancePropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webAppSiteName")
    def web_app_site_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @web_app_site_name.setter
    def web_app_site_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:offazure:WebAppSitesController")
class WebAppSitesController(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., discovery_scenario: Optional[pulumi.Input[Union[_builtins.str, WebAppSitePropertiesDiscoveryScenario]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., site_appliance_properties_collection: Optional[pulumi.Input[Sequence[pulumi.Input[Union[SiteAppliancePropertiesArgs, SiteAppliancePropertiesArgsDict]]]]] = ..., site_name: Optional[pulumi.Input[_builtins.str]] = ..., web_app_site_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WebAppSitesControllerArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WebAppSitesController:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryScenario")
    def discovery_scenario(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteAppliancePropertiesCollection")
    def site_appliance_properties_collection(self) -> pulumi.Output[Optional[Sequence[outputs.SiteAppliancePropertiesResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


