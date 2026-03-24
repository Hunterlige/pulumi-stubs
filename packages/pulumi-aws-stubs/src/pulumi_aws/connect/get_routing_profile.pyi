

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRoutingProfileResult', 'AwaitableGetRoutingProfileResult', 'get_routing_profile', 'get_routing_profile_output']
@pulumi.output_type
class GetRoutingProfileResult:
    
    def __init__(__self__, arn=..., default_outbound_queue_id=..., description=..., id=..., instance_id=..., media_concurrencies=..., name=..., queue_configs=..., region=..., routing_profile_id=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultOutboundQueueId")
    def default_outbound_queue_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mediaConcurrencies")
    def media_concurrencies(self) -> Sequence[outputs.GetRoutingProfileMediaConcurrencyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueConfigs")
    def queue_configs(self) -> Sequence[outputs.GetRoutingProfileQueueConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingProfileId")
    def routing_profile_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetRoutingProfileResult(GetRoutingProfileResult):
    def __await__(self): # -> Generator[Never, Any, GetRoutingProfileResult]:
        ...
    


def get_routing_profile(instance_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., routing_profile_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRoutingProfileResult:
    
    ...

def get_routing_profile_output(instance_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., routing_profile_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRoutingProfileResult]:
    
    ...

