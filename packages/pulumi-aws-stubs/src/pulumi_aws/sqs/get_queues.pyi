

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetQueuesResult', 'AwaitableGetQueuesResult', 'get_queues', 'get_queues_output']
@pulumi.output_type
class GetQueuesResult:
    
    def __init__(__self__, id=..., queue_name_prefix=..., queue_urls=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueNamePrefix")
    def queue_name_prefix(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueUrls")
    def queue_urls(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetQueuesResult(GetQueuesResult):
    def __await__(self): # -> Generator[Never, Any, GetQueuesResult]:
        ...
    


def get_queues(queue_name_prefix: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetQueuesResult:
    
    ...

def get_queues_output(queue_name_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetQueuesResult]:
    
    ...

