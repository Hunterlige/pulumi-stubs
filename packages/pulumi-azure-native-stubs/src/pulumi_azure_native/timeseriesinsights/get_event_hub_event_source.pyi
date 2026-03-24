

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEventHubEventSourceResult', 'AwaitableGetEventHubEventSourceResult', 'get_event_hub_event_source', 'get_event_hub_event_source_output']
@pulumi.output_type
class GetEventHubEventSourceResult:
    
    def __init__(__self__, azure_api_version=..., consumer_group_name=..., creation_time=..., event_hub_name=..., event_source_resource_id=..., id=..., key_name=..., kind=..., local_timestamp=..., location=..., name=..., provisioning_state=..., service_bus_namespace=..., tags=..., time=..., timestamp_property_name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="consumerGroupName")
    def consumer_group_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventSourceResourceId")
    def event_source_resource_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localTimestamp")
    def local_timestamp(self) -> Optional[outputs.LocalTimestampResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
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
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampPropertyName")
    def timestamp_property_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetEventHubEventSourceResult(GetEventHubEventSourceResult):
    def __await__(self): # -> Generator[Never, Any, GetEventHubEventSourceResult]:
        ...
    


def get_event_hub_event_source(environment_name: Optional[_builtins.str] = ..., event_source_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEventHubEventSourceResult:
    
    ...

def get_event_hub_event_source_output(environment_name: Optional[pulumi.Input[_builtins.str]] = ..., event_source_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEventHubEventSourceResult]:
    
    ...

