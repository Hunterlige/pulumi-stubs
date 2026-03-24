

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
__all__ = ['GetSnapshotResult', 'AwaitableGetSnapshotResult', 'get_snapshot', 'get_snapshot_output']
@pulumi.output_type
class GetSnapshotResult:
    
    def __init__(__self__, arn=..., data_encryption_key_id=..., description=..., encrypted=..., filters=..., id=..., kms_key_id=..., most_recent=..., outpost_arn=..., owner_alias=..., owner_id=..., owners=..., region=..., restorable_by_user_ids=..., snapshot_id=..., snapshot_ids=..., start_time=..., state=..., storage_tier=..., tags=..., volume_id=..., volume_size=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataEncryptionKeyId")
    def data_encryption_key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetSnapshotFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerAlias")
    def owner_alias(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> _builtins.str:
        
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
    
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotIds")
    def snapshot_ids(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageTier")
    def storage_tier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> _builtins.int:
        
        ...
    


class AwaitableGetSnapshotResult(GetSnapshotResult):
    def __await__(self): # -> Generator[Never, Any, GetSnapshotResult]:
        ...
    


def get_snapshot(filters: Optional[Sequence[Union[GetSnapshotFilterArgs, GetSnapshotFilterArgsDict]]] = ..., most_recent: Optional[_builtins.bool] = ..., owners: Optional[Sequence[_builtins.str]] = ..., region: Optional[_builtins.str] = ..., restorable_by_user_ids: Optional[Sequence[_builtins.str]] = ..., snapshot_ids: Optional[Sequence[_builtins.str]] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSnapshotResult:
    
    ...

def get_snapshot_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetSnapshotFilterArgs, GetSnapshotFilterArgsDict]]]]] = ..., most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., owners: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., restorable_by_user_ids: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., snapshot_ids: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSnapshotResult]:
    
    ...

