

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LandingZoneConfigurationOperationArgs', 'LandingZoneConfigurationOperation']
@pulumi.input_type
class LandingZoneConfigurationOperationArgs:
    def __init__(__self__, *, landing_zone_account_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], landing_zone_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[LandingZoneConfigurationResourcePropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="landingZoneAccountName")
    def landing_zone_account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @landing_zone_account_name.setter
    def landing_zone_account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="landingZoneConfigurationName")
    def landing_zone_configuration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @landing_zone_configuration_name.setter
    def landing_zone_configuration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[LandingZoneConfigurationResourcePropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[LandingZoneConfigurationResourcePropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class LandingZoneConfigurationOperation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., landing_zone_account_name: Optional[pulumi.Input[_builtins.str]] = ..., landing_zone_configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[LandingZoneConfigurationResourcePropertiesArgs, LandingZoneConfigurationResourcePropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LandingZoneConfigurationOperationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> LandingZoneConfigurationOperation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.LandingZoneConfigurationResourcePropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


