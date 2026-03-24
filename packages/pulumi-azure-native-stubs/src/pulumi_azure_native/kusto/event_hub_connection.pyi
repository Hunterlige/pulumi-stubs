

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EventHubConnectionArgs', 'EventHubConnection']
@pulumi.input_type
class EventHubConnectionArgs:
    def __init__(__self__, *, cluster_name: pulumi.Input[_builtins.str], consumer_group: pulumi.Input[_builtins.str], database_name: pulumi.Input[_builtins.str], event_hub_resource_id: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], data_format: Optional[pulumi.Input[Union[_builtins.str, DataFormat]]] = ..., event_hub_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mapping_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @consumer_group.setter
    def consumer_group(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event_hub_resource_id.setter
    def event_hub_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[pulumi.Input[Union[_builtins.str, DataFormat]]]:
        
        ...
    
    @data_format.setter
    def data_format(self, value: Optional[pulumi.Input[Union[_builtins.str, DataFormat]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubConnectionName")
    def event_hub_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event_hub_connection_name.setter
    def event_hub_connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mapping_rule_name.setter
    def mapping_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:kusto:EventHubConnection")
class EventHubConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., consumer_group: Optional[pulumi.Input[_builtins.str]] = ..., data_format: Optional[pulumi.Input[Union[_builtins.str, DataFormat]]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., event_hub_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., event_hub_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mapping_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EventHubConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> EventHubConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


