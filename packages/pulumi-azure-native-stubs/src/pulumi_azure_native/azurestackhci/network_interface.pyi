

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NetworkInterfaceArgs', 'NetworkInterface']
@pulumi.input_type
class NetworkInterfaceArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], create_from_local: Optional[pulumi.Input[_builtins.bool]] = ..., dns_settings: Optional[pulumi.Input[InterfaceDNSSettingsArgs]] = ..., extended_location: Optional[pulumi.Input[ExtendedLocationArgs]] = ..., ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[IPConfigurationArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mac_address: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_name: Optional[pulumi.Input[_builtins.str]] = ..., network_security_group: Optional[pulumi.Input[NetworkSecurityGroupArmReferenceArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createFromLocal")
    def create_from_local(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_from_local.setter
    def create_from_local(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional[pulumi.Input[InterfaceDNSSettingsArgs]]:
        
        ...
    
    @dns_settings.setter
    def dns_settings(self, value: Optional[pulumi.Input[InterfaceDNSSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input[ExtendedLocationArgs]]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input[ExtendedLocationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IPConfigurationArgs]]]]:
        
        ...
    
    @ip_configurations.setter
    def ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IPConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mac_address.setter
    def mac_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInterfaceName")
    def network_interface_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_interface_name.setter
    def network_interface_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> Optional[pulumi.Input[NetworkSecurityGroupArmReferenceArgs]]:
        
        ...
    
    @network_security_group.setter
    def network_security_group(self, value: Optional[pulumi.Input[NetworkSecurityGroupArmReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azurestackhci:NetworkInterface")
class NetworkInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., create_from_local: Optional[pulumi.Input[_builtins.bool]] = ..., dns_settings: Optional[pulumi.Input[Union[InterfaceDNSSettingsArgs, InterfaceDNSSettingsArgsDict]]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[IPConfigurationArgs, IPConfigurationArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mac_address: Optional[pulumi.Input[_builtins.str]] = ..., network_interface_name: Optional[pulumi.Input[_builtins.str]] = ..., network_security_group: Optional[pulumi.Input[Union[NetworkSecurityGroupArmReferenceArgs, NetworkSecurityGroupArmReferenceArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkInterfaceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> NetworkInterface:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createFromLocal")
    def create_from_local(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> pulumi.Output[Optional[outputs.InterfaceDNSSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional[outputs.ExtendedLocationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.IPConfigurationResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityGroup")
    def network_security_group(self) -> pulumi.Output[Optional[outputs.NetworkSecurityGroupArmReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.NetworkInterfaceStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


