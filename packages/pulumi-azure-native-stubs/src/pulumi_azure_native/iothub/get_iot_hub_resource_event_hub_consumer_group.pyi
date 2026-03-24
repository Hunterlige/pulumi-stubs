

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetIotHubResourceEventHubConsumerGroupResult', ..., 'get_iot_hub_resource_event_hub_consumer_group', ...]
@pulumi.output_type
class GetIotHubResourceEventHubConsumerGroupResult:
    
    def __init__(__self__, azure_api_version=..., etag=..., id=..., name=..., properties=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Any:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetIotHubResourceEventHubConsumerGroupResult(GetIotHubResourceEventHubConsumerGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetIotHubResourceEventHubConsumerGroupResult]:
        ...
    


def get_iot_hub_resource_event_hub_consumer_group(event_hub_endpoint_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIotHubResourceEventHubConsumerGroupResult:
    
    ...

def get_iot_hub_resource_event_hub_consumer_group_output(event_hub_endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIotHubResourceEventHubConsumerGroupResult]:
    
    ...

