

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOpenZfsSnapshotResult', 'AwaitableGetOpenZfsSnapshotResult', 'get_open_zfs_snapshot', 'get_open_zfs_snapshot_output']
@pulumi.output_type
class GetOpenZfsSnapshotResult:
    
    def __init__(__self__, arn=..., creation_time=..., filters=..., id=..., most_recent=..., name=..., region=..., snapshot_id=..., snapshot_ids=..., tags=..., volume_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetOpenZfsSnapshotFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotIds")
    def snapshot_ids(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetOpenZfsSnapshotResult(GetOpenZfsSnapshotResult):
    def __await__(self): # -> Generator[Never, Any, GetOpenZfsSnapshotResult]:
        ...
    


def get_open_zfs_snapshot(filters: Optional[Sequence[Union[GetOpenZfsSnapshotFilterArgs, GetOpenZfsSnapshotFilterArgsDict]]] = ..., most_recent: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., snapshot_ids: Optional[Sequence[_builtins.str]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOpenZfsSnapshotResult:
    
    ...

def get_open_zfs_snapshot_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetOpenZfsSnapshotFilterArgs, GetOpenZfsSnapshotFilterArgsDict]]]]] = ..., most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., snapshot_ids: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOpenZfsSnapshotResult]:
    
    ...

