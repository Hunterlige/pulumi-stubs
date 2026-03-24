

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEventHubDataConnectionResult', 'AwaitableGetEventHubDataConnectionResult', 'get_event_hub_data_connection', 'get_event_hub_data_connection_output']
@pulumi.output_type
class GetEventHubDataConnectionResult:
    
    def __init__(__self__, azure_api_version=..., compression=..., consumer_group=..., data_format=..., database_routing=..., event_hub_resource_id=..., event_system_properties=..., id=..., kind=..., location=..., managed_identity_object_id=..., managed_identity_resource_id=..., mapping_rule_name=..., name=..., provisioning_state=..., retrieval_start_date=..., table_name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseRouting")
    def database_routing(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSystemProperties")
    def event_system_properties(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityObjectId")
    def managed_identity_object_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEventHubDataConnectionResult(GetEventHubDataConnectionResult):
    def __await__(self): # -> Generator[Never, Any, GetEventHubDataConnectionResult]:
        ...
    


def get_event_hub_data_connection(cluster_name: Optional[_builtins.str] = ..., data_connection_name: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEventHubDataConnectionResult:
    
    ...

def get_event_hub_data_connection_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., data_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEventHubDataConnectionResult]:
    
    ...

