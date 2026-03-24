

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListAgentPoolQueueStatusResult', 'AwaitableListAgentPoolQueueStatusResult', 'list_agent_pool_queue_status', 'list_agent_pool_queue_status_output']
@pulumi.output_type
class ListAgentPoolQueueStatusResult:
    
    def __init__(__self__, count=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[_builtins.int]:
        
        ...
    


class AwaitableListAgentPoolQueueStatusResult(ListAgentPoolQueueStatusResult):
    def __await__(self): # -> Generator[Never, Any, ListAgentPoolQueueStatusResult]:
        ...
    


def list_agent_pool_queue_status(agent_pool_name: Optional[_builtins.str] = ..., registry_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListAgentPoolQueueStatusResult:
    
    ...

def list_agent_pool_queue_status_output(agent_pool_name: Optional[pulumi.Input[_builtins.str]] = ..., registry_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListAgentPoolQueueStatusResult]:
    
    ...

