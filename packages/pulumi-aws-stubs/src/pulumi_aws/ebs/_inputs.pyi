

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FastSnapshotRestoreTimeoutsArgs', 'FastSnapshotRestoreTimeoutsArgsDict', 'SnapshotImportClientDataArgs', 'SnapshotImportClientDataArgsDict', 'SnapshotImportDiskContainerArgs', 'SnapshotImportDiskContainerArgsDict', 'SnapshotImportDiskContainerUserBucketArgs', 'SnapshotImportDiskContainerUserBucketArgsDict', 'GetEbsVolumesFilterArgs', 'GetEbsVolumesFilterArgsDict', 'GetSnapshotFilterArgs', 'GetSnapshotFilterArgsDict', 'GetSnapshotIdsFilterArgs', 'GetSnapshotIdsFilterArgsDict', 'GetVolumeFilterArgs', 'GetVolumeFilterArgsDict']
class FastSnapshotRestoreTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FastSnapshotRestoreTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SnapshotImportClientDataArgsDict(TypedDict):
    comment: NotRequired[pulumi.Input[_builtins.str]]
    upload_end: NotRequired[pulumi.Input[_builtins.str]]
    upload_size: NotRequired[pulumi.Input[_builtins.float]]
    upload_start: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SnapshotImportClientDataArgs:
    def __init__(__self__, *, comment: Optional[pulumi.Input[_builtins.str]] = ..., upload_end: Optional[pulumi.Input[_builtins.str]] = ..., upload_size: Optional[pulumi.Input[_builtins.float]] = ..., upload_start: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @comment.setter
    def comment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadEnd")
    def upload_end(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @upload_end.setter
    def upload_end(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadSize")
    def upload_size(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @upload_size.setter
    def upload_size(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uploadStart")
    def upload_start(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @upload_start.setter
    def upload_start(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SnapshotImportDiskContainerArgsDict(TypedDict):
    format: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]
    user_bucket: NotRequired[pulumi.Input[SnapshotImportDiskContainerUserBucketArgsDict]]


@pulumi.input_type
class SnapshotImportDiskContainerArgs:
    def __init__(__self__, *, format: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ..., user_bucket: Optional[pulumi.Input[SnapshotImportDiskContainerUserBucketArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userBucket")
    def user_bucket(self) -> Optional[pulumi.Input[SnapshotImportDiskContainerUserBucketArgs]]:
        
        ...
    
    @user_bucket.setter
    def user_bucket(self, value: Optional[pulumi.Input[SnapshotImportDiskContainerUserBucketArgs]]): # -> None:
        ...
    


class SnapshotImportDiskContainerUserBucketArgsDict(TypedDict):
    s3_bucket: pulumi.Input[_builtins.str]
    s3_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class SnapshotImportDiskContainerUserBucketArgs:
    def __init__(__self__, *, s3_bucket: pulumi.Input[_builtins.str], s3_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_bucket.setter
    def s3_bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Key")
    def s3_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_key.setter
    def s3_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class GetEbsVolumesFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetEbsVolumesFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetSnapshotFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetSnapshotFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetSnapshotIdsFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetSnapshotIdsFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


class GetVolumeFilterArgsDict(TypedDict):
    name: _builtins.str
    values: Sequence[_builtins.str]


@pulumi.input_type
class GetVolumeFilterArgs:
    def __init__(__self__, *, name: _builtins.str, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @name.setter
    def name(self, value: _builtins.str): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    
    @values.setter
    def values(self, value: Sequence[_builtins.str]): # -> None:
        ...
    


