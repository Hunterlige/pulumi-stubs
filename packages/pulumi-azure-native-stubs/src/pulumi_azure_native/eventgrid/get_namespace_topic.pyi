

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNamespaceTopicResult', 'AwaitableGetNamespaceTopicResult', 'get_namespace_topic', 'get_namespace_topic_output']
@pulumi.output_type
class GetNamespaceTopicResult:
    
    def __init__(__self__, azure_api_version=..., event_retention_in_days=..., id=..., input_schema=..., name=..., provisioning_state=..., publisher_type=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventRetentionInDays")
    def event_retention_in_days(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="publisherType")
    def publisher_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNamespaceTopicResult(GetNamespaceTopicResult):
    def __await__(self): # -> Generator[Never, Any, GetNamespaceTopicResult]:
        ...
    


def get_namespace_topic(namespace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., topic_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNamespaceTopicResult:
    
    ...

def get_namespace_topic_output(namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., topic_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNamespaceTopicResult]:
    
    ...

