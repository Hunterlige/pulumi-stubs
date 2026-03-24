

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EfsLocationEc2ConfigArgs', 'EfsLocationEc2ConfigArgsDict', 'FsxOpenZfsFileSystemProtocolArgs', 'FsxOpenZfsFileSystemProtocolArgsDict', 'FsxOpenZfsFileSystemProtocolNfsArgs', 'FsxOpenZfsFileSystemProtocolNfsArgsDict', 'FsxOpenZfsFileSystemProtocolNfsMountOptionsArgs', ..., 'LocationAzureBlobSasConfigurationArgs', 'LocationAzureBlobSasConfigurationArgsDict', 'LocationFsxOntapFileSystemProtocolArgs', 'LocationFsxOntapFileSystemProtocolArgsDict', 'LocationFsxOntapFileSystemProtocolNfsArgs', 'LocationFsxOntapFileSystemProtocolNfsArgsDict', ..., ..., 'LocationFsxOntapFileSystemProtocolSmbArgs', 'LocationFsxOntapFileSystemProtocolSmbArgsDict', ..., ..., 'LocationHdfsNameNodeArgs', 'LocationHdfsNameNodeArgsDict', 'LocationHdfsQopConfigurationArgs', 'LocationHdfsQopConfigurationArgsDict', 'LocationSmbMountOptionsArgs', 'LocationSmbMountOptionsArgsDict', 'NfsLocationMountOptionsArgs', 'NfsLocationMountOptionsArgsDict', 'NfsLocationOnPremConfigArgs', 'NfsLocationOnPremConfigArgsDict', 'S3LocationS3ConfigArgs', 'S3LocationS3ConfigArgsDict', 'TaskExcludesArgs', 'TaskExcludesArgsDict', 'TaskIncludesArgs', 'TaskIncludesArgsDict', 'TaskOptionsArgs', 'TaskOptionsArgsDict', 'TaskScheduleArgs', 'TaskScheduleArgsDict', 'TaskTaskReportConfigArgs', 'TaskTaskReportConfigArgsDict', 'TaskTaskReportConfigReportOverridesArgs', 'TaskTaskReportConfigReportOverridesArgsDict', 'TaskTaskReportConfigS3DestinationArgs', 'TaskTaskReportConfigS3DestinationArgsDict']
class EfsLocationEc2ConfigArgsDict(TypedDict):
    security_group_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnet_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class EfsLocationEc2ConfigArgs:
    def __init__(__self__, *, security_group_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], subnet_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupArns")
    def security_group_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @security_group_arns.setter
    def security_group_arns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetArn")
    def subnet_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subnet_arn.setter
    def subnet_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FsxOpenZfsFileSystemProtocolArgsDict(TypedDict):
    nfs: pulumi.Input[FsxOpenZfsFileSystemProtocolNfsArgsDict]


@pulumi.input_type
class FsxOpenZfsFileSystemProtocolArgs:
    def __init__(__self__, *, nfs: pulumi.Input[FsxOpenZfsFileSystemProtocolNfsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> pulumi.Input[FsxOpenZfsFileSystemProtocolNfsArgs]:
        
        ...
    
    @nfs.setter
    def nfs(self, value: pulumi.Input[FsxOpenZfsFileSystemProtocolNfsArgs]): # -> None:
        ...
    


class FsxOpenZfsFileSystemProtocolNfsArgsDict(TypedDict):
    mount_options: pulumi.Input[FsxOpenZfsFileSystemProtocolNfsMountOptionsArgsDict]


@pulumi.input_type
class FsxOpenZfsFileSystemProtocolNfsArgs:
    def __init__(__self__, *, mount_options: pulumi.Input[FsxOpenZfsFileSystemProtocolNfsMountOptionsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> pulumi.Input[FsxOpenZfsFileSystemProtocolNfsMountOptionsArgs]:
        
        ...
    
    @mount_options.setter
    def mount_options(self, value: pulumi.Input[FsxOpenZfsFileSystemProtocolNfsMountOptionsArgs]): # -> None:
        ...
    


class FsxOpenZfsFileSystemProtocolNfsMountOptionsArgsDict(TypedDict):
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FsxOpenZfsFileSystemProtocolNfsMountOptionsArgs:
    def __init__(__self__, *, version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LocationAzureBlobSasConfigurationArgsDict(TypedDict):
    token: pulumi.Input[_builtins.str]


@pulumi.input_type
class LocationAzureBlobSasConfigurationArgs:
    def __init__(__self__, *, token: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token.setter
    def token(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class LocationFsxOntapFileSystemProtocolArgsDict(TypedDict):
    nfs: NotRequired[pulumi.Input[LocationFsxOntapFileSystemProtocolNfsArgsDict]]
    smb: NotRequired[pulumi.Input[LocationFsxOntapFileSystemProtocolSmbArgsDict]]


@pulumi.input_type
class LocationFsxOntapFileSystemProtocolArgs:
    def __init__(__self__, *, nfs: Optional[pulumi.Input[LocationFsxOntapFileSystemProtocolNfsArgs]] = ..., smb: Optional[pulumi.Input[LocationFsxOntapFileSystemProtocolSmbArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[pulumi.Input[LocationFsxOntapFileSystemProtocolNfsArgs]]:
        
        ...
    
    @nfs.setter
    def nfs(self, value: Optional[pulumi.Input[LocationFsxOntapFileSystemProtocolNfsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def smb(self) -> Optional[pulumi.Input[LocationFsxOntapFileSystemProtocolSmbArgs]]:
        
        ...
    
    @smb.setter
    def smb(self, value: Optional[pulumi.Input[LocationFsxOntapFileSystemProtocolSmbArgs]]): # -> None:
        ...
    


class LocationFsxOntapFileSystemProtocolNfsArgsDict(TypedDict):
    mount_options: pulumi.Input[LocationFsxOntapFileSystemProtocolNfsMountOptionsArgsDict]


@pulumi.input_type
class LocationFsxOntapFileSystemProtocolNfsArgs:
    def __init__(__self__, *, mount_options: pulumi.Input[LocationFsxOntapFileSystemProtocolNfsMountOptionsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> pulumi.Input[LocationFsxOntapFileSystemProtocolNfsMountOptionsArgs]:
        
        ...
    
    @mount_options.setter
    def mount_options(self, value: pulumi.Input[LocationFsxOntapFileSystemProtocolNfsMountOptionsArgs]): # -> None:
        ...
    


class LocationFsxOntapFileSystemProtocolNfsMountOptionsArgsDict(TypedDict):
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LocationFsxOntapFileSystemProtocolNfsMountOptionsArgs:
    def __init__(__self__, *, version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LocationFsxOntapFileSystemProtocolSmbArgsDict(TypedDict):
    mount_options: pulumi.Input[LocationFsxOntapFileSystemProtocolSmbMountOptionsArgsDict]
    password: pulumi.Input[_builtins.str]
    user: pulumi.Input[_builtins.str]
    domain: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LocationFsxOntapFileSystemProtocolSmbArgs:
    def __init__(__self__, *, mount_options: pulumi.Input[LocationFsxOntapFileSystemProtocolSmbMountOptionsArgs], password: pulumi.Input[_builtins.str], user: pulumi.Input[_builtins.str], domain: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> pulumi.Input[LocationFsxOntapFileSystemProtocolSmbMountOptionsArgs]:
        
        ...
    
    @mount_options.setter
    def mount_options(self, value: pulumi.Input[LocationFsxOntapFileSystemProtocolSmbMountOptionsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def user(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @user.setter
    def user(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LocationFsxOntapFileSystemProtocolSmbMountOptionsArgsDict(TypedDict):
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LocationFsxOntapFileSystemProtocolSmbMountOptionsArgs:
    def __init__(__self__, *, version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LocationHdfsNameNodeArgsDict(TypedDict):
    hostname: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]


@pulumi.input_type
class LocationHdfsNameNodeArgs:
    def __init__(__self__, *, hostname: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hostname.setter
    def hostname(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class LocationHdfsQopConfigurationArgsDict(TypedDict):
    data_transfer_protection: NotRequired[pulumi.Input[_builtins.str]]
    rpc_protection: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LocationHdfsQopConfigurationArgs:
    def __init__(__self__, *, data_transfer_protection: Optional[pulumi.Input[_builtins.str]] = ..., rpc_protection: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTransferProtection")
    def data_transfer_protection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_transfer_protection.setter
    def data_transfer_protection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rpcProtection")
    def rpc_protection(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rpc_protection.setter
    def rpc_protection(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LocationSmbMountOptionsArgsDict(TypedDict):
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LocationSmbMountOptionsArgs:
    def __init__(__self__, *, version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NfsLocationMountOptionsArgsDict(TypedDict):
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NfsLocationMountOptionsArgs:
    def __init__(__self__, *, version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NfsLocationOnPremConfigArgsDict(TypedDict):
    agent_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class NfsLocationOnPremConfigArgs:
    def __init__(__self__, *, agent_arns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentArns")
    def agent_arns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @agent_arns.setter
    def agent_arns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class S3LocationS3ConfigArgsDict(TypedDict):
    bucket_access_role_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class S3LocationS3ConfigArgs:
    def __init__(__self__, *, bucket_access_role_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketAccessRoleArn")
    def bucket_access_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_access_role_arn.setter
    def bucket_access_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TaskExcludesArgsDict(TypedDict):
    filter_type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TaskExcludesArgs:
    def __init__(__self__, *, filter_type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_type.setter
    def filter_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TaskIncludesArgsDict(TypedDict):
    filter_type: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TaskIncludesArgs:
    def __init__(__self__, *, filter_type: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_type.setter
    def filter_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TaskOptionsArgsDict(TypedDict):
    atime: NotRequired[pulumi.Input[_builtins.str]]
    bytes_per_second: NotRequired[pulumi.Input[_builtins.int]]
    gid: NotRequired[pulumi.Input[_builtins.str]]
    log_level: NotRequired[pulumi.Input[_builtins.str]]
    mtime: NotRequired[pulumi.Input[_builtins.str]]
    object_tags: NotRequired[pulumi.Input[_builtins.str]]
    overwrite_mode: NotRequired[pulumi.Input[_builtins.str]]
    posix_permissions: NotRequired[pulumi.Input[_builtins.str]]
    preserve_deleted_files: NotRequired[pulumi.Input[_builtins.str]]
    preserve_devices: NotRequired[pulumi.Input[_builtins.str]]
    security_descriptor_copy_flags: NotRequired[pulumi.Input[_builtins.str]]
    task_queueing: NotRequired[pulumi.Input[_builtins.str]]
    transfer_mode: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]
    verify_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TaskOptionsArgs:
    def __init__(__self__, *, atime: Optional[pulumi.Input[_builtins.str]] = ..., bytes_per_second: Optional[pulumi.Input[_builtins.int]] = ..., gid: Optional[pulumi.Input[_builtins.str]] = ..., log_level: Optional[pulumi.Input[_builtins.str]] = ..., mtime: Optional[pulumi.Input[_builtins.str]] = ..., object_tags: Optional[pulumi.Input[_builtins.str]] = ..., overwrite_mode: Optional[pulumi.Input[_builtins.str]] = ..., posix_permissions: Optional[pulumi.Input[_builtins.str]] = ..., preserve_deleted_files: Optional[pulumi.Input[_builtins.str]] = ..., preserve_devices: Optional[pulumi.Input[_builtins.str]] = ..., security_descriptor_copy_flags: Optional[pulumi.Input[_builtins.str]] = ..., task_queueing: Optional[pulumi.Input[_builtins.str]] = ..., transfer_mode: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., verify_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def atime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @atime.setter
    def atime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesPerSecond")
    def bytes_per_second(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @bytes_per_second.setter
    def bytes_per_second(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gid.setter
    def gid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mtime(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mtime.setter
    def mtime(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectTags")
    def object_tags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @object_tags.setter
    def object_tags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteMode")
    def overwrite_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @overwrite_mode.setter
    def overwrite_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="posixPermissions")
    def posix_permissions(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @posix_permissions.setter
    def posix_permissions(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveDeletedFiles")
    def preserve_deleted_files(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preserve_deleted_files.setter
    def preserve_deleted_files(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveDevices")
    def preserve_devices(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @preserve_devices.setter
    def preserve_devices(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityDescriptorCopyFlags")
    def security_descriptor_copy_flags(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_descriptor_copy_flags.setter
    def security_descriptor_copy_flags(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="taskQueueing")
    def task_queueing(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @task_queueing.setter
    def task_queueing(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferMode")
    def transfer_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transfer_mode.setter
    def transfer_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifyMode")
    def verify_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @verify_mode.setter
    def verify_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TaskScheduleArgsDict(TypedDict):
    schedule_expression: pulumi.Input[_builtins.str]


@pulumi.input_type
class TaskScheduleArgs:
    def __init__(__self__, *, schedule_expression: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schedule_expression.setter
    def schedule_expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class TaskTaskReportConfigArgsDict(TypedDict):
    s3_destination: pulumi.Input[TaskTaskReportConfigS3DestinationArgsDict]
    output_type: NotRequired[pulumi.Input[_builtins.str]]
    report_level: NotRequired[pulumi.Input[_builtins.str]]
    report_overrides: NotRequired[pulumi.Input[TaskTaskReportConfigReportOverridesArgsDict]]
    s3_object_versioning: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TaskTaskReportConfigArgs:
    def __init__(__self__, *, s3_destination: pulumi.Input[TaskTaskReportConfigS3DestinationArgs], output_type: Optional[pulumi.Input[_builtins.str]] = ..., report_level: Optional[pulumi.Input[_builtins.str]] = ..., report_overrides: Optional[pulumi.Input[TaskTaskReportConfigReportOverridesArgs]] = ..., s3_object_versioning: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> pulumi.Input[TaskTaskReportConfigS3DestinationArgs]:
        
        ...
    
    @s3_destination.setter
    def s3_destination(self, value: pulumi.Input[TaskTaskReportConfigS3DestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputType")
    def output_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_type.setter
    def output_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportLevel")
    def report_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @report_level.setter
    def report_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportOverrides")
    def report_overrides(self) -> Optional[pulumi.Input[TaskTaskReportConfigReportOverridesArgs]]:
        
        ...
    
    @report_overrides.setter
    def report_overrides(self, value: Optional[pulumi.Input[TaskTaskReportConfigReportOverridesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ObjectVersioning")
    def s3_object_versioning(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @s3_object_versioning.setter
    def s3_object_versioning(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TaskTaskReportConfigReportOverridesArgsDict(TypedDict):
    deleted_override: NotRequired[pulumi.Input[_builtins.str]]
    skipped_override: NotRequired[pulumi.Input[_builtins.str]]
    transferred_override: NotRequired[pulumi.Input[_builtins.str]]
    verified_override: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TaskTaskReportConfigReportOverridesArgs:
    def __init__(__self__, *, deleted_override: Optional[pulumi.Input[_builtins.str]] = ..., skipped_override: Optional[pulumi.Input[_builtins.str]] = ..., transferred_override: Optional[pulumi.Input[_builtins.str]] = ..., verified_override: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletedOverride")
    def deleted_override(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deleted_override.setter
    def deleted_override(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skippedOverride")
    def skipped_override(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @skipped_override.setter
    def skipped_override(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferredOverride")
    def transferred_override(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transferred_override.setter
    def transferred_override(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedOverride")
    def verified_override(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @verified_override.setter
    def verified_override(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TaskTaskReportConfigS3DestinationArgsDict(TypedDict):
    bucket_access_role_arn: pulumi.Input[_builtins.str]
    s3_bucket_arn: pulumi.Input[_builtins.str]
    subdirectory: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TaskTaskReportConfigS3DestinationArgs:
    def __init__(__self__, *, bucket_access_role_arn: pulumi.Input[_builtins.str], s3_bucket_arn: pulumi.Input[_builtins.str], subdirectory: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketAccessRoleArn")
    def bucket_access_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket_access_role_arn.setter
    def bucket_access_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @s3_bucket_arn.setter
    def s3_bucket_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subdirectory(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subdirectory.setter
    def subdirectory(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


