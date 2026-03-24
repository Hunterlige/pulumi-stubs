

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
__all__ = ['TimeSeriesDatabaseConnectionArgs', 'TimeSeriesDatabaseConnection']
@pulumi.input_type
class TimeSeriesDatabaseConnectionArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], resource_name: pulumi.Input[_builtins.str], properties: Optional[pulumi.Input[AzureDataExplorerConnectionPropertiesArgs]] = ..., time_series_database_connection_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[AzureDataExplorerConnectionPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[AzureDataExplorerConnectionPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeSeriesDatabaseConnectionName")
    def time_series_database_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_series_database_connection_name.setter
    def time_series_database_connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class TimeSeriesDatabaseConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., properties: Optional[pulumi.Input[Union[AzureDataExplorerConnectionPropertiesArgs, AzureDataExplorerConnectionPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name_: Optional[pulumi.Input[_builtins.str]] = ..., time_series_database_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: TimeSeriesDatabaseConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> TimeSeriesDatabaseConnection:
        
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
    def properties(self) -> pulumi.Output[outputs.AzureDataExplorerConnectionPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


