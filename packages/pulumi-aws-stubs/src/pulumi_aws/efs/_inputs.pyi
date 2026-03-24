import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessPointPosixUserArgs",
    "AccessPointPosixUserArgsDict",
    "AccessPointRootDirectoryArgs",
    "AccessPointRootDirectoryArgsDict",
    "AccessPointRootDirectoryCreationInfoArgs",
    "AccessPointRootDirectoryCreationInfoArgsDict",
    "BackupPolicyBackupPolicyArgs",
    "BackupPolicyBackupPolicyArgsDict",
    "FileSystemLifecyclePolicyArgs",
    "FileSystemLifecyclePolicyArgsDict",
    "FileSystemProtectionArgs",
    "FileSystemProtectionArgsDict",
    "FileSystemSizeInByteArgs",
    "FileSystemSizeInByteArgsDict",
    "ReplicationConfigurationDestinationArgs",
    "ReplicationConfigurationDestinationArgsDict",
]

class AccessPointPosixUserArgsDict(TypedDict):
    gid: pulumi.Input[_builtins.int]
    uid: pulumi.Input[_builtins.int]
    secondary_gids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class AccessPointPosixUserArgs:
    def __init__(
        __self__,
        *,
        gid: pulumi.Input[_builtins.int],
        uid: pulumi.Input[_builtins.int],
        secondary_gids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> pulumi.Input[_builtins.int]: ...
    @gid.setter
    def gid(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Input[_builtins.int]: ...
    @uid.setter
    def uid(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @secondary_gids.setter
    def secondary_gids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class AccessPointRootDirectoryArgsDict(TypedDict):
    creation_info: NotRequired[
        pulumi.Input[AccessPointRootDirectoryCreationInfoArgsDict]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AccessPointRootDirectoryArgs:
    def __init__(
        __self__,
        *,
        creation_info: Optional[
            pulumi.Input[AccessPointRootDirectoryCreationInfoArgs]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="creationInfo")
    def creation_info(
        self,
    ) -> Optional[pulumi.Input[AccessPointRootDirectoryCreationInfoArgs]]: ...
    @creation_info.setter
    def creation_info(
        self, value: Optional[pulumi.Input[AccessPointRootDirectoryCreationInfoArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AccessPointRootDirectoryCreationInfoArgsDict(TypedDict):
    owner_gid: pulumi.Input[_builtins.int]
    owner_uid: pulumi.Input[_builtins.int]
    permissions: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AccessPointRootDirectoryCreationInfoArgs:
    def __init__(
        __self__,
        *,
        owner_gid: pulumi.Input[_builtins.int],
        owner_uid: pulumi.Input[_builtins.int],
        permissions: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ownerGid")
    def owner_gid(self) -> pulumi.Input[_builtins.int]: ...
    @owner_gid.setter
    def owner_gid(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="ownerUid")
    def owner_uid(self) -> pulumi.Input[_builtins.int]: ...
    @owner_uid.setter
    def owner_uid(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[_builtins.str]: ...
    @permissions.setter
    def permissions(self, value: pulumi.Input[_builtins.str]): ...

class BackupPolicyBackupPolicyArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class BackupPolicyBackupPolicyArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class FileSystemLifecyclePolicyArgsDict(TypedDict):
    transition_to_archive: NotRequired[pulumi.Input[_builtins.str]]
    transition_to_ia: NotRequired[pulumi.Input[_builtins.str]]
    transition_to_primary_storage_class: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FileSystemLifecyclePolicyArgs:
    def __init__(
        __self__,
        *,
        transition_to_archive: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_to_ia: Optional[pulumi.Input[_builtins.str]] = ...,
        transition_to_primary_storage_class: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="transitionToArchive")
    def transition_to_archive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transition_to_archive.setter
    def transition_to_archive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitionToIa")
    def transition_to_ia(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transition_to_ia.setter
    def transition_to_ia(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="transitionToPrimaryStorageClass")
    def transition_to_primary_storage_class(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @transition_to_primary_storage_class.setter
    def transition_to_primary_storage_class(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class FileSystemProtectionArgsDict(TypedDict):
    replication_overwrite: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FileSystemProtectionArgs:
    def __init__(
        __self__, *, replication_overwrite: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replicationOverwrite")
    def replication_overwrite(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replication_overwrite.setter
    def replication_overwrite(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FileSystemSizeInByteArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[_builtins.int]]
    value_in_ia: NotRequired[pulumi.Input[_builtins.int]]
    value_in_standard: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class FileSystemSizeInByteArgs:
    def __init__(
        __self__,
        *,
        value: Optional[pulumi.Input[_builtins.int]] = ...,
        value_in_ia: Optional[pulumi.Input[_builtins.int]] = ...,
        value_in_standard: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="valueInIa")
    def value_in_ia(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @value_in_ia.setter
    def value_in_ia(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="valueInStandard")
    def value_in_standard(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @value_in_standard.setter
    def value_in_standard(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ReplicationConfigurationDestinationArgsDict(TypedDict):
    availability_zone_name: NotRequired[pulumi.Input[_builtins.str]]
    file_system_id: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_id: NotRequired[pulumi.Input[_builtins.str]]
    region: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ReplicationConfigurationDestinationArgs:
    def __init__(
        __self__,
        *,
        availability_zone_name: Optional[pulumi.Input[_builtins.str]] = ...,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone_name.setter
    def availability_zone_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
