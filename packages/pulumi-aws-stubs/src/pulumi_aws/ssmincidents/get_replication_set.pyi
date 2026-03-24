

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReplicationSetResult', 'AwaitableGetReplicationSetResult', 'get_replication_set', 'get_replication_set_output']
@pulumi.output_type
class GetReplicationSetResult:
    
    def __init__(__self__, arn=..., created_by=..., deletion_protected=..., id=..., last_modified_by=..., region=..., regions=..., status=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtected")
    def deletion_protected(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated("""region is deprecated. Use regions instead.""")
    def region(self) -> Sequence[outputs.GetReplicationSetRegionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Sequence[outputs.GetReplicationSetRegionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetReplicationSetResult(GetReplicationSetResult):
    def __await__(self): # -> Generator[Never, Any, GetReplicationSetResult]:
        ...
    


def get_replication_set(tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReplicationSetResult:
    
    ...

def get_replication_set_output(tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReplicationSetResult]:
    
    ...

