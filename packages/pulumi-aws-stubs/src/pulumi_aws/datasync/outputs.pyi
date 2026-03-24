import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EfsLocationEc2Config",
    "FsxOpenZfsFileSystemProtocol",
    "FsxOpenZfsFileSystemProtocolNfs",
    "FsxOpenZfsFileSystemProtocolNfsMountOptions",
    "LocationAzureBlobSasConfiguration",
    "LocationFsxOntapFileSystemProtocol",
    "LocationFsxOntapFileSystemProtocolNfs",
    "LocationFsxOntapFileSystemProtocolNfsMountOptions",
    "LocationFsxOntapFileSystemProtocolSmb",
    "LocationFsxOntapFileSystemProtocolSmbMountOptions",
    "LocationHdfsNameNode",
    "LocationHdfsQopConfiguration",
    "LocationSmbMountOptions",
    "NfsLocationMountOptions",
    "NfsLocationOnPremConfig",
    "S3LocationS3Config",
    "TaskExcludes",
    "TaskIncludes",
    "TaskOptions",
    "TaskSchedule",
    "TaskTaskReportConfig",
    "TaskTaskReportConfigReportOverrides",
    "TaskTaskReportConfigS3Destination",
]

@pulumi.output_type
class EfsLocationEc2Config(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_arns: Sequence[_builtins.str],
        subnet_arn: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> _builtins.str: ...

@pulumi.output_type
class FsxOpenZfsFileSystemProtocol(dict):
    def __init__(__self__, *, nfs: outputs.FsxOpenZfsFileSystemProtocolNfs) -> None: ...
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> outputs.FsxOpenZfsFileSystemProtocolNfs: ...

@pulumi.output_type
class FsxOpenZfsFileSystemProtocolNfs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, mount_options: outputs.FsxOpenZfsFileSystemProtocolNfsMountOptions
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> outputs.FsxOpenZfsFileSystemProtocolNfsMountOptions: ...

@pulumi.output_type
class FsxOpenZfsFileSystemProtocolNfsMountOptions(dict):
    def __init__(__self__, *, version: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LocationAzureBlobSasConfiguration(dict):
    def __init__(__self__, *, token: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> _builtins.str: ...

@pulumi.output_type
class LocationFsxOntapFileSystemProtocol(dict):
    def __init__(
        __self__,
        *,
        nfs: Optional[outputs.LocationFsxOntapFileSystemProtocolNfs] = ...,
        smb: Optional[outputs.LocationFsxOntapFileSystemProtocolSmb] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[outputs.LocationFsxOntapFileSystemProtocolNfs]: ...
    @_builtins.property
    @pulumi.getter
    def smb(self) -> Optional[outputs.LocationFsxOntapFileSystemProtocolSmb]: ...

@pulumi.output_type
class LocationFsxOntapFileSystemProtocolNfs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mount_options: outputs.LocationFsxOntapFileSystemProtocolNfsMountOptions,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(
        self,
    ) -> outputs.LocationFsxOntapFileSystemProtocolNfsMountOptions: ...

@pulumi.output_type
class LocationFsxOntapFileSystemProtocolNfsMountOptions(dict):
    def __init__(__self__, *, version: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LocationFsxOntapFileSystemProtocolSmb(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mount_options: outputs.LocationFsxOntapFileSystemProtocolSmbMountOptions,
        password: _builtins.str,
        user: _builtins.str,
        domain: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(
        self,
    ) -> outputs.LocationFsxOntapFileSystemProtocolSmbMountOptions: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LocationFsxOntapFileSystemProtocolSmbMountOptions(dict):
    def __init__(__self__, *, version: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LocationHdfsNameNode(dict):
    def __init__(__self__, *, hostname: _builtins.str, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class LocationHdfsQopConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_transfer_protection: Optional[_builtins.str] = ...,
        rpc_protection: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataTransferProtection")
    def data_transfer_protection(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rpcProtection")
    def rpc_protection(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class LocationSmbMountOptions(dict):
    def __init__(__self__, *, version: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NfsLocationMountOptions(dict):
    def __init__(__self__, *, version: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class NfsLocationOnPremConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, agent_arns: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class S3LocationS3Config(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, bucket_access_role_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketAccessRoleArn")
    def bucket_access_role_arn(self) -> _builtins.str: ...

@pulumi.output_type
class TaskExcludes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filter_type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskIncludes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filter_type: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        atime: Optional[_builtins.str] = ...,
        bytes_per_second: Optional[_builtins.int] = ...,
        gid: Optional[_builtins.str] = ...,
        log_level: Optional[_builtins.str] = ...,
        mtime: Optional[_builtins.str] = ...,
        object_tags: Optional[_builtins.str] = ...,
        overwrite_mode: Optional[_builtins.str] = ...,
        posix_permissions: Optional[_builtins.str] = ...,
        preserve_deleted_files: Optional[_builtins.str] = ...,
        preserve_devices: Optional[_builtins.str] = ...,
        security_descriptor_copy_flags: Optional[_builtins.str] = ...,
        task_queueing: Optional[_builtins.str] = ...,
        transfer_mode: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
        verify_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def atime(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bytesPerSecond")
    def bytes_per_second(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mtime(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="objectTags")
    def object_tags(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overwriteMode")
    def overwrite_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="posixPermissions")
    def posix_permissions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preserveDeletedFiles")
    def preserve_deleted_files(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="preserveDevices")
    def preserve_devices(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityDescriptorCopyFlags")
    def security_descriptor_copy_flags(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="taskQueueing")
    def task_queueing(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transferMode")
    def transfer_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="verifyMode")
    def verify_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, schedule_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> _builtins.str: ...

@pulumi.output_type
class TaskTaskReportConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_destination: outputs.TaskTaskReportConfigS3Destination,
        output_type: Optional[_builtins.str] = ...,
        report_level: Optional[_builtins.str] = ...,
        report_overrides: Optional[outputs.TaskTaskReportConfigReportOverrides] = ...,
        s3_object_versioning: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> outputs.TaskTaskReportConfigS3Destination: ...
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reportLevel")
    def report_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reportOverrides")
    def report_overrides(
        self,
    ) -> Optional[outputs.TaskTaskReportConfigReportOverrides]: ...
    @_builtins.property
    @pulumi.getter(name="s3ObjectVersioning")
    def s3_object_versioning(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskTaskReportConfigReportOverrides(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deleted_override: Optional[_builtins.str] = ...,
        skipped_override: Optional[_builtins.str] = ...,
        transferred_override: Optional[_builtins.str] = ...,
        verified_override: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deletedOverride")
    def deleted_override(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="skippedOverride")
    def skipped_override(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="transferredOverride")
    def transferred_override(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="verifiedOverride")
    def verified_override(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TaskTaskReportConfigS3Destination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_access_role_arn: _builtins.str,
        s3_bucket_arn: _builtins.str,
        subdirectory: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketAccessRoleArn")
    def bucket_access_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[_builtins.str]: ...
