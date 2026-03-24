

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AzureKeyVaultSmbCredentialsArgs', 'AzureKeyVaultSmbCredentialsArgsDict', 'AzureStorageBlobContainerEndpointPropertiesArgs', ..., 'AzureStorageSmbFileShareEndpointPropertiesArgs', 'AzureStorageSmbFileShareEndpointPropertiesArgsDict', 'ConnectionPropertiesArgs', 'ConnectionPropertiesArgsDict', 'NfsMountEndpointPropertiesArgs', 'NfsMountEndpointPropertiesArgsDict', 'SmbMountEndpointPropertiesArgs', 'SmbMountEndpointPropertiesArgsDict', 'TimeArgs', 'TimeArgsDict', 'UploadLimitScheduleArgs', 'UploadLimitScheduleArgsDict', 'UploadLimitWeeklyRecurrenceArgs', 'UploadLimitWeeklyRecurrenceArgsDict']
class AzureKeyVaultSmbCredentialsArgsDict(TypedDict):
    
    type: pulumi.Input[_builtins.str]
    password_uri: NotRequired[pulumi.Input[_builtins.str]]
    username_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureKeyVaultSmbCredentialsArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], password_uri: Optional[pulumi.Input[_builtins.str]] = ..., username_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordUri")
    def password_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_uri.setter
    def password_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernameUri")
    def username_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username_uri.setter
    def username_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AzureStorageBlobContainerEndpointPropertiesArgsDict(TypedDict):
    
    blob_container_name: pulumi.Input[_builtins.str]
    endpoint_type: pulumi.Input[_builtins.str]
    storage_account_resource_id: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureStorageBlobContainerEndpointPropertiesArgs:
    def __init__(__self__, *, blob_container_name: pulumi.Input[_builtins.str], endpoint_type: pulumi.Input[_builtins.str], storage_account_resource_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @blob_container_name.setter
    def blob_container_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_account_resource_id.setter
    def storage_account_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AzureStorageSmbFileShareEndpointPropertiesArgsDict(TypedDict):
    
    endpoint_type: pulumi.Input[_builtins.str]
    file_share_name: pulumi.Input[_builtins.str]
    storage_account_resource_id: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureStorageSmbFileShareEndpointPropertiesArgs:
    def __init__(__self__, *, endpoint_type: pulumi.Input[_builtins.str], file_share_name: pulumi.Input[_builtins.str], storage_account_resource_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_share_name.setter
    def file_share_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @storage_account_resource_id.setter
    def storage_account_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConnectionPropertiesArgsDict(TypedDict):
    
    private_link_service_id: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    job_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConnectionPropertiesArgs:
    def __init__(__self__, *, private_link_service_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., job_list: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceId")
    def private_link_service_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_link_service_id.setter
    def private_link_service_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobList")
    def job_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @job_list.setter
    def job_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class NfsMountEndpointPropertiesArgsDict(TypedDict):
    
    endpoint_type: pulumi.Input[_builtins.str]
    export: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    nfs_version: NotRequired[pulumi.Input[Union[_builtins.str, NfsVersion]]]


@pulumi.input_type
class NfsMountEndpointPropertiesArgs:
    def __init__(__self__, *, endpoint_type: pulumi.Input[_builtins.str], export: pulumi.Input[_builtins.str], host: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., nfs_version: Optional[pulumi.Input[Union[_builtins.str, NfsVersion]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def export(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @export.setter
    def export(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsVersion")
    def nfs_version(self) -> Optional[pulumi.Input[Union[_builtins.str, NfsVersion]]]:
        
        ...
    
    @nfs_version.setter
    def nfs_version(self, value: Optional[pulumi.Input[Union[_builtins.str, NfsVersion]]]): # -> None:
        ...
    


class SmbMountEndpointPropertiesArgsDict(TypedDict):
    
    endpoint_type: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    share_name: pulumi.Input[_builtins.str]
    credentials: NotRequired[pulumi.Input[AzureKeyVaultSmbCredentialsArgsDict]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SmbMountEndpointPropertiesArgs:
    def __init__(__self__, *, endpoint_type: pulumi.Input[_builtins.str], host: pulumi.Input[_builtins.str], share_name: pulumi.Input[_builtins.str], credentials: Optional[pulumi.Input[AzureKeyVaultSmbCredentialsArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @share_name.setter
    def share_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[AzureKeyVaultSmbCredentialsArgs]]:
        
        ...
    
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[AzureKeyVaultSmbCredentialsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TimeArgsDict(TypedDict):
    
    hour: pulumi.Input[_builtins.int]
    minute: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class TimeArgs:
    def __init__(__self__, *, hour: pulumi.Input[_builtins.int], minute: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hour(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @hour.setter
    def hour(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @minute.setter
    def minute(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class UploadLimitScheduleArgsDict(TypedDict):
    
    weekly_recurrences: NotRequired[pulumi.Input[Sequence[pulumi.Input[UploadLimitWeeklyRecurrenceArgsDict]]]]


@pulumi.input_type
class UploadLimitScheduleArgs:
    def __init__(__self__, *, weekly_recurrences: Optional[pulumi.Input[Sequence[pulumi.Input[UploadLimitWeeklyRecurrenceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrences")
    def weekly_recurrences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[UploadLimitWeeklyRecurrenceArgs]]]]:
        
        ...
    
    @weekly_recurrences.setter
    def weekly_recurrences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UploadLimitWeeklyRecurrenceArgs]]]]): # -> None:
        ...
    


class UploadLimitWeeklyRecurrenceArgsDict(TypedDict):
    
    days: pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]
    end_time: pulumi.Input[TimeArgsDict]
    limit_in_mbps: pulumi.Input[_builtins.int]
    start_time: pulumi.Input[TimeArgsDict]


@pulumi.input_type
class UploadLimitWeeklyRecurrenceArgs:
    def __init__(__self__, *, days: pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]], end_time: pulumi.Input[TimeArgs], limit_in_mbps: pulumi.Input[_builtins.int], start_time: pulumi.Input[TimeArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def days(self) -> pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]:
        
        ...
    
    @days.setter
    def days(self, value: pulumi.Input[Sequence[pulumi.Input[DayOfWeek]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Input[TimeArgs]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: pulumi.Input[TimeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="limitInMbps")
    def limit_in_mbps(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @limit_in_mbps.setter
    def limit_in_mbps(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input[TimeArgs]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: pulumi.Input[TimeArgs]): # -> None:
        ...
    


