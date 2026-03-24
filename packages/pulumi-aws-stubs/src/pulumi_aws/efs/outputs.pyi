import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessPointPosixUser",
    "AccessPointRootDirectory",
    "AccessPointRootDirectoryCreationInfo",
    "BackupPolicyBackupPolicy",
    "FileSystemLifecyclePolicy",
    "FileSystemProtection",
    "FileSystemSizeInByte",
    "ReplicationConfigurationDestination",
    "GetAccessPointPosixUserResult",
    "GetAccessPointRootDirectoryResult",
    "GetAccessPointRootDirectoryCreationInfoResult",
    "GetFileSystemLifecyclePolicyResult",
    "GetFileSystemProtectionResult",
]

@pulumi.output_type
class AccessPointPosixUser(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        gid: _builtins.int,
        uid: _builtins.int,
        secondary_gids: Optional[Sequence[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Optional[Sequence[_builtins.int]]: ...

@pulumi.output_type
class AccessPointRootDirectory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        creation_info: Optional[outputs.AccessPointRootDirectoryCreationInfo] = ...,
        path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationInfo")
    def creation_info(
        self,
    ) -> Optional[outputs.AccessPointRootDirectoryCreationInfo]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AccessPointRootDirectoryCreationInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        owner_gid: _builtins.int,
        owner_uid: _builtins.int,
        permissions: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ownerGid")
    def owner_gid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ownerUid")
    def owner_uid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> _builtins.str: ...

@pulumi.output_type
class BackupPolicyBackupPolicy(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class FileSystemLifecyclePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        transition_to_archive: Optional[_builtins.str] = ...,
        transition_to_ia: Optional[_builtins.str] = ...,
        transition_to_primary_storage_class: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transitionToArchive")
    def transition_to_archive(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitionToIa")
    def transition_to_ia(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transitionToPrimaryStorageClass")
    def transition_to_primary_storage_class(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FileSystemProtection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, replication_overwrite: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicationOverwrite")
    def replication_overwrite(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FileSystemSizeInByte(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        value: Optional[_builtins.int] = ...,
        value_in_ia: Optional[_builtins.int] = ...,
        value_in_standard: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="valueInIa")
    def value_in_ia(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="valueInStandard")
    def value_in_standard(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ReplicationConfigurationDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        availability_zone_name: Optional[_builtins.str] = ...,
        file_system_id: Optional[_builtins.str] = ...,
        kms_key_id: Optional[_builtins.str] = ...,
        region: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetAccessPointPosixUserResult(dict):
    def __init__(
        __self__,
        *,
        gid: _builtins.int,
        secondary_gids: Sequence[_builtins.int],
        uid: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Sequence[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.int: ...

@pulumi.output_type
class GetAccessPointRootDirectoryResult(dict):
    def __init__(
        __self__,
        *,
        creation_infos: Sequence[outputs.GetAccessPointRootDirectoryCreationInfoResult],
        path: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationInfos")
    def creation_infos(
        self,
    ) -> Sequence[outputs.GetAccessPointRootDirectoryCreationInfoResult]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...

@pulumi.output_type
class GetAccessPointRootDirectoryCreationInfoResult(dict):
    def __init__(
        __self__,
        *,
        owner_gid: _builtins.int,
        owner_uid: _builtins.int,
        permissions: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ownerGid")
    def owner_gid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ownerUid")
    def owner_uid(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> _builtins.str: ...

@pulumi.output_type
class GetFileSystemLifecyclePolicyResult(dict):
    def __init__(
        __self__,
        *,
        transition_to_archive: _builtins.str,
        transition_to_ia: _builtins.str,
        transition_to_primary_storage_class: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transitionToArchive")
    def transition_to_archive(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitionToIa")
    def transition_to_ia(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitionToPrimaryStorageClass")
    def transition_to_primary_storage_class(self) -> _builtins.str: ...

@pulumi.output_type
class GetFileSystemProtectionResult(dict):
    def __init__(__self__, *, replication_overwrite: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicationOverwrite")
    def replication_overwrite(self) -> _builtins.str: ...
