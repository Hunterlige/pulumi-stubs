

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
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], resource_name: pulumi.Input[_builtins.str], config_name: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[MaintenanceWindowArgs]] = ..., not_allowed_time: Optional[pulumi.Input[Sequence[pulumi.Input[TimeSpanArgs]]]] = ..., time_in_week: Optional[pulumi.Input[Sequence[pulumi.Input[TimeInWeekArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configName")
    def config_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @config_name.setter
    def config_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[MaintenanceWindowArgs]]:
        
        ...
    
    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[MaintenanceWindowArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAllowedTime")
    def not_allowed_time(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TimeSpanArgs]]]]:
        
        ...
    
    @not_allowed_time.setter
    def not_allowed_time(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TimeSpanArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeInWeek")
    def time_in_week(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[TimeInWeekArgs]]]]:
        
        ...
    
    @time_in_week.setter
    def time_in_week(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[TimeInWeekArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class MaintenanceConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., config_name: Optional[pulumi.Input[_builtins.str]] = ..., maintenance_window: Optional[pulumi.Input[Union[MaintenanceWindowArgs, MaintenanceWindowArgsDict]]] = ..., not_allowed_time: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TimeSpanArgs, TimeSpanArgsDict]]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name_: Optional[pulumi.Input[_builtins.str]] = ..., time_in_week: Optional[pulumi.Input[Sequence[pulumi.Input[Union[TimeInWeekArgs, TimeInWeekArgsDict]]]]] = ..., __props__=...) -> None:
        
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
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[Optional[outputs.MaintenanceWindowResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notAllowedTime")
    def not_allowed_time(self) -> pulumi.Output[Optional[Sequence[outputs.TimeSpanResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeInWeek")
    def time_in_week(self) -> pulumi.Output[Optional[Sequence[outputs.TimeInWeekResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


