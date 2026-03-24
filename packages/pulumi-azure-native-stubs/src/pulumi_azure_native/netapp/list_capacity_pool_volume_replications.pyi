

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListCapacityPoolVolumeReplicationsResult', 'AwaitableListCapacityPoolVolumeReplicationsResult', 'list_capacity_pool_volume_replications', 'list_capacity_pool_volume_replications_output']
@pulumi.output_type
class ListCapacityPoolVolumeReplicationsResult:
    
    def __init__(__self__, value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.ReplicationResponse]]:
        
        ...
    


class AwaitableListCapacityPoolVolumeReplicationsResult(ListCapacityPoolVolumeReplicationsResult):
    def __await__(self): # -> Generator[Never, Any, ListCapacityPoolVolumeReplicationsResult]:
        ...
    


def list_capacity_pool_volume_replications(account_name: Optional[_builtins.str] = ..., pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., volume_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListCapacityPoolVolumeReplicationsResult:
    
    ...

def list_capacity_pool_volume_replications_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListCapacityPoolVolumeReplicationsResult]:
    
    ...

