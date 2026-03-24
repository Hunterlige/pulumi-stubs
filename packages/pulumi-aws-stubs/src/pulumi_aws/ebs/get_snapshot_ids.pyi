

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSnapshotIdsResult', 'AwaitableGetSnapshotIdsResult', 'get_snapshot_ids', 'get_snapshot_ids_output']
@pulumi.output_type
class GetSnapshotIdsResult:
    
    def __init__(__self__, filters=..., id=..., ids=..., owners=..., region=..., restorable_by_user_ids=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetSnapshotIdsFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def owners(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorableByUserIds")
    def restorable_by_user_ids(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


class AwaitableGetSnapshotIdsResult(GetSnapshotIdsResult):
    def __await__(self): # -> Generator[Never, Any, GetSnapshotIdsResult]:
        ...
    


def get_snapshot_ids(filters: Optional[Sequence[Union[GetSnapshotIdsFilterArgs, GetSnapshotIdsFilterArgsDict]]] = ..., owners: Optional[Sequence[_builtins.str]] = ..., region: Optional[_builtins.str] = ..., restorable_by_user_ids: Optional[Sequence[_builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSnapshotIdsResult:
    
    ...

def get_snapshot_ids_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetSnapshotIdsFilterArgs, GetSnapshotIdsFilterArgsDict]]]]] = ..., owners: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., restorable_by_user_ids: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSnapshotIdsResult]:
    
    ...

