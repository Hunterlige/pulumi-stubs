

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
__all__ = ['DiscoveredAssetEndpointProfileArgs', 'DiscoveredAssetEndpointProfile']
@pulumi.input_type
class DiscoveredAssetEndpointProfileArgs:
    def __init__(__self__, *, discovery_id: pulumi.Input[_builtins.str], endpoint_profile_type: pulumi.Input[_builtins.str], extended_location: pulumi.Input[ExtendedLocationArgs], resource_group_name: pulumi.Input[_builtins.str], target_address: pulumi.Input[_builtins.str], version: pulumi.Input[_builtins.float], additional_configuration: Optional[pulumi.Input[_builtins.str]] = ..., discovered_asset_endpoint_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., supported_authentication_methods: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryId")
    def discovery_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @discovery_id.setter
    def discovery_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointProfileType")
    def endpoint_profile_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_profile_type.setter
    def endpoint_profile_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]:
        
        ...
    
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAddress")
    def target_address(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_address.setter
    def target_address(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @additional_configuration.setter
    def additional_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredAssetEndpointProfileName")
    def discovered_asset_endpoint_profile_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @discovered_asset_endpoint_profile_name.setter
    def discovered_asset_endpoint_profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedAuthenticationMethods")
    def supported_authentication_methods(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]]]:
        
        ...
    
    @supported_authentication_methods.setter
    def supported_authentication_methods(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DiscoveredAssetEndpointProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., additional_configuration: Optional[pulumi.Input[_builtins.str]] = ..., discovered_asset_endpoint_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., discovery_id: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_profile_type: Optional[pulumi.Input[_builtins.str]] = ..., extended_location: Optional[pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., supported_authentication_methods: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AuthenticationMethod]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_address: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.float]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DiscoveredAssetEndpointProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DiscoveredAssetEndpointProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryId")
    def discovery_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointProfileType")
    def endpoint_profile_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedAuthenticationMethods")
    def supported_authentication_methods(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
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
    @pulumi.getter(name="targetAddress")
    def target_address(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.float]:
        
        ...
    


