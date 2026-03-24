

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVpnSiteResult', 'AwaitableGetVpnSiteResult', 'get_vpn_site', 'get_vpn_site_output']
@pulumi.output_type
class GetVpnSiteResult:
    
    def __init__(__self__, address_space=..., azure_api_version=..., bgp_properties=..., device_properties=..., etag=..., id=..., ip_address=..., is_security_site=..., location=..., name=..., o365_policy=..., provisioning_state=..., site_key=..., tags=..., type=..., virtual_wan=..., vpn_site_links=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional[outputs.AddressSpaceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpProperties")
    def bgp_properties(self) -> Optional[outputs.BgpSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceProperties")
    def device_properties(self) -> Optional[outputs.DevicePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSecuritySite")
    def is_security_site(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="o365Policy")
    def o365_policy(self) -> Optional[outputs.O365PolicyPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteKey")
    def site_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnSiteLinks")
    def vpn_site_links(self) -> Optional[Sequence[outputs.VpnSiteLinkResponse]]:
        
        ...
    


class AwaitableGetVpnSiteResult(GetVpnSiteResult):
    def __await__(self): # -> Generator[Never, Any, GetVpnSiteResult]:
        ...
    


def get_vpn_site(resource_group_name: Optional[_builtins.str] = ..., vpn_site_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVpnSiteResult:
    
    ...

def get_vpn_site_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., vpn_site_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVpnSiteResult]:
    
    ...

