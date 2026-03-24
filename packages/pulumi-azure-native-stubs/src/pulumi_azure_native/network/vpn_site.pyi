

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['VpnSiteArgs', 'VpnSite']
@pulumi.input_type
class VpnSiteArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], address_space: Optional[pulumi.Input[AddressSpaceArgs]] = ..., bgp_properties: Optional[pulumi.Input[BgpSettingsArgs]] = ..., device_properties: Optional[pulumi.Input[DevicePropertiesArgs]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., is_security_site: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., o365_policy: Optional[pulumi.Input[O365PolicyPropertiesArgs]] = ..., site_key: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_wan: Optional[pulumi.Input[SubResourceArgs]] = ..., vpn_site_links: Optional[pulumi.Input[Sequence[pulumi.Input[VpnSiteLinkArgs]]]] = ..., vpn_site_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> Optional[pulumi.Input[AddressSpaceArgs]]:
        
        ...
    
    @address_space.setter
    def address_space(self, value: Optional[pulumi.Input[AddressSpaceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpProperties")
    def bgp_properties(self) -> Optional[pulumi.Input[BgpSettingsArgs]]:
        
        ...
    
    @bgp_properties.setter
    def bgp_properties(self, value: Optional[pulumi.Input[BgpSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceProperties")
    def device_properties(self) -> Optional[pulumi.Input[DevicePropertiesArgs]]:
        
        ...
    
    @device_properties.setter
    def device_properties(self, value: Optional[pulumi.Input[DevicePropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSecuritySite")
    def is_security_site(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_security_site.setter
    def is_security_site(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="o365Policy")
    def o365_policy(self) -> Optional[pulumi.Input[O365PolicyPropertiesArgs]]:
        
        ...
    
    @o365_policy.setter
    def o365_policy(self, value: Optional[pulumi.Input[O365PolicyPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteKey")
    def site_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @site_key.setter
    def site_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> Optional[pulumi.Input[SubResourceArgs]]:
        
        ...
    
    @virtual_wan.setter
    def virtual_wan(self, value: Optional[pulumi.Input[SubResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnSiteLinks")
    def vpn_site_links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VpnSiteLinkArgs]]]]:
        
        ...
    
    @vpn_site_links.setter
    def vpn_site_links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VpnSiteLinkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnSiteName")
    def vpn_site_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpn_site_name.setter
    def vpn_site_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:network:VpnSite")
class VpnSite(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., address_space: Optional[pulumi.Input[Union[AddressSpaceArgs, AddressSpaceArgsDict]]] = ..., bgp_properties: Optional[pulumi.Input[Union[BgpSettingsArgs, BgpSettingsArgsDict]]] = ..., device_properties: Optional[pulumi.Input[Union[DevicePropertiesArgs, DevicePropertiesArgsDict]]] = ..., id: Optional[pulumi.Input[_builtins.str]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., is_security_site: Optional[pulumi.Input[_builtins.bool]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., o365_policy: Optional[pulumi.Input[Union[O365PolicyPropertiesArgs, O365PolicyPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., site_key: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., virtual_wan: Optional[pulumi.Input[Union[SubResourceArgs, SubResourceArgsDict]]] = ..., vpn_site_links: Optional[pulumi.Input[Sequence[pulumi.Input[Union[VpnSiteLinkArgs, VpnSiteLinkArgsDict]]]]] = ..., vpn_site_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: VpnSiteArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> VpnSite:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressSpace")
    def address_space(self) -> pulumi.Output[Optional[outputs.AddressSpaceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bgpProperties")
    def bgp_properties(self) -> pulumi.Output[Optional[outputs.BgpSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceProperties")
    def device_properties(self) -> pulumi.Output[Optional[outputs.DevicePropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSecuritySite")
    def is_security_site(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="o365Policy")
    def o365_policy(self) -> pulumi.Output[Optional[outputs.O365PolicyPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteKey")
    def site_key(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> pulumi.Output[Optional[outputs.SubResourceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpnSiteLinks")
    def vpn_site_links(self) -> pulumi.Output[Optional[Sequence[outputs.VpnSiteLinkResponse]]]:
        
        ...
    


