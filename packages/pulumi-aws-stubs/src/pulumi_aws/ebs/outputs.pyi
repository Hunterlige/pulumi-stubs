

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FastSnapshotRestoreTimeouts', 'SnapshotImportClientData', 'SnapshotImportDiskContainer', 'SnapshotImportDiskContainerUserBucket', 'GetEbsVolumesFilterResult', 'GetSnapshotFilterResult', 'GetSnapshotIdsFilterResult', 'GetVolumeFilterResult']
@pulumi.output_type
class FastSnapshotRestoreTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SnapshotImportClientData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, comment: Optional[_builtins.str] = ..., upload_end: Optional[_builtins.str] = ..., upload_size: Optional[_builtins.float] = ..., upload_start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadEnd")
    def upload_end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadSize")
    def upload_size(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadStart")
    def upload_start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SnapshotImportDiskContainer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, format: _builtins.str, description: Optional[_builtins.str] = ..., url: Optional[_builtins.str] = ..., user_bucket: Optional[outputs.SnapshotImportDiskContainerUserBucket] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userBucket")
    def user_bucket(self) -> Optional[outputs.SnapshotImportDiskContainerUserBucket]:
        
        ...
    


@pulumi.output_type
class SnapshotImportDiskContainerUserBucket(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, s3_bucket: _builtins.str, s3_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetEbsVolumesFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetSnapshotFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetSnapshotIdsFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetVolumeFilterResult(dict):
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


