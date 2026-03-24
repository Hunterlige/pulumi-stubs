

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetQueueResult', 'AwaitableGetQueueResult', 'get_queue', 'get_queue_output']
@pulumi.output_type
class GetQueueResult:
    
    def __init__(__self__, arn=..., description=..., hours_of_operation_id=..., id=..., instance_id=..., max_contacts=..., name=..., outbound_caller_configs=..., queue_id=..., region=..., status=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hoursOfOperationId")
    def hours_of_operation_id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="maxContacts")
    def max_contacts(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outboundCallerConfigs")
    def outbound_caller_configs(self) -> Sequence[outputs.GetQueueOutboundCallerConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetQueueResult(GetQueueResult):
    def __await__(self): # -> Generator[Never, Any, GetQueueResult]:
        ...
    


def get_queue(instance_id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., queue_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetQueueResult:
    
    ...

def get_queue_output(instance_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., queue_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetQueueResult]:
    
    ...

