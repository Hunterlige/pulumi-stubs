

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FleetspaceAccountArgs', 'FleetspaceAccount']
@pulumi.input_type
class FleetspaceAccountArgs:
    def __init__(__self__, *, fleet_name: pulumi.Input[_builtins.str], fleetspace_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], fleetspace_account_name: Optional[pulumi.Input[_builtins.str]] = ..., global_database_account_properties: Optional[pulumi.Input[FleetspaceAccountPropertiesGlobalDatabaseAccountPropertiesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetName")
    def fleet_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @fleet_name.setter
    def fleet_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetspaceName")
    def fleetspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @fleetspace_name.setter
    def fleetspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetspaceAccountName")
    def fleetspace_account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fleetspace_account_name.setter
    def fleetspace_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalDatabaseAccountProperties")
    def global_database_account_properties(self) -> Optional[pulumi.Input[FleetspaceAccountPropertiesGlobalDatabaseAccountPropertiesArgs]]:
        
        ...
    
    @global_database_account_properties.setter
    def global_database_account_properties(self, value: Optional[pulumi.Input[FleetspaceAccountPropertiesGlobalDatabaseAccountPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:cosmosdb:FleetspaceAccount")
class FleetspaceAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., fleet_name: Optional[pulumi.Input[_builtins.str]] = ..., fleetspace_account_name: Optional[pulumi.Input[_builtins.str]] = ..., fleetspace_name: Optional[pulumi.Input[_builtins.str]] = ..., global_database_account_properties: Optional[pulumi.Input[Union[FleetspaceAccountPropertiesGlobalDatabaseAccountPropertiesArgs, FleetspaceAccountPropertiesGlobalDatabaseAccountPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FleetspaceAccountArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> FleetspaceAccount:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalDatabaseAccountProperties")
    def global_database_account_properties(self) -> pulumi.Output[Optional[outputs.FleetspaceAccountPropertiesResponseGlobalDatabaseAccountProperties]]:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


