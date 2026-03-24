

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
__all__ = ['MaintenanceConfigurationArgs', 'MaintenanceConfiguration']
@pulumi.input_type
class MaintenanceConfigurationArgs:
    def __init__(__self__, *, environment_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], scheduled_entries: pulumi.Input[Sequence[pulumi.Input[ScheduledEntryArgs]]], config_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @environment_name.setter
    def environment_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduledEntries")
    def scheduled_entries(self) -> pulumi.Input[Sequence[pulumi.Input[ScheduledEntryArgs]]]:
        
        ...
    
    @scheduled_entries.setter
    def scheduled_entries(self, value: pulumi.Input[Sequence[pulumi.Input[ScheduledEntryArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configName")
    def config_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @config_name.setter
    def config_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:app:MaintenanceConfiguration")
class MaintenanceConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., config_name: Optional[pulumi.Input[_builtins.str]] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scheduled_entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ScheduledEntryArgs, ScheduledEntryArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MaintenanceConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> MaintenanceConfiguration:
        
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
    @pulumi.getter(name="scheduledEntries")
    def scheduled_entries(self) -> pulumi.Output[Sequence[outputs.ScheduledEntryResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


