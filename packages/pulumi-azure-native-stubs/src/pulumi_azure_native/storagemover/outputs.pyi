import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AgentPropertiesErrorDetailsResponse",
    "AzureKeyVaultSmbCredentialsResponse",
    ...,
    "AzureStorageSmbFileShareEndpointPropertiesResponse",
    "ConnectionPropertiesResponse",
    "NfsMountEndpointPropertiesResponse",
    "SmbMountEndpointPropertiesResponse",
    "SystemDataResponse",
    "TimeResponse",
    "UploadLimitScheduleResponse",
    "UploadLimitWeeklyRecurrenceResponse",
]

@pulumi.output_type
class AgentPropertiesErrorDetailsResponse(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureKeyVaultSmbCredentialsResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        password_uri: Optional[_builtins.str] = ...,
        username_uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="passwordUri")
    def password_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="usernameUri")
    def username_uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureStorageBlobContainerEndpointPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        blob_container_name: _builtins.str,
        endpoint_type: _builtins.str,
        provisioning_state: _builtins.str,
        storage_account_resource_id: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AzureStorageSmbFileShareEndpointPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_type: _builtins.str,
        file_share_name: _builtins.str,
        provisioning_state: _builtins.str,
        storage_account_resource_id: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectionPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_status: _builtins.str,
        private_endpoint_name: _builtins.str,
        private_endpoint_resource_id: _builtins.str,
        private_link_service_id: _builtins.str,
        provisioning_state: _builtins.str,
        description: Optional[_builtins.str] = ...,
        job_list: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointResourceId")
    def private_endpoint_resource_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceId")
    def private_link_service_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobList")
    def job_list(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class NfsMountEndpointPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_type: _builtins.str,
        export: _builtins.str,
        host: _builtins.str,
        provisioning_state: _builtins.str,
        description: Optional[_builtins.str] = ...,
        nfs_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def export(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nfsVersion")
    def nfs_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SmbMountEndpointPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpoint_type: _builtins.str,
        host: _builtins.str,
        provisioning_state: _builtins.str,
        share_name: _builtins.str,
        credentials: Optional[outputs.AzureKeyVaultSmbCredentialsResponse] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.AzureKeyVaultSmbCredentialsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SystemDataResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        created_at: Optional[_builtins.str] = ...,
        created_by: Optional[_builtins.str] = ...,
        created_by_type: Optional[_builtins.str] = ...,
        last_modified_at: Optional[_builtins.str] = ...,
        last_modified_by: Optional[_builtins.str] = ...,
        last_modified_by_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TimeResponse(dict):
    def __init__(
        __self__, *, hour: _builtins.int, minute: Optional[_builtins.float] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hour(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def minute(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class UploadLimitScheduleResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        weekly_recurrences: Optional[
            Sequence[outputs.UploadLimitWeeklyRecurrenceResponse]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="weeklyRecurrences")
    def weekly_recurrences(
        self,
    ) -> Optional[Sequence[outputs.UploadLimitWeeklyRecurrenceResponse]]: ...

@pulumi.output_type
class UploadLimitWeeklyRecurrenceResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        days: Sequence[_builtins.str],
        end_time: outputs.TimeResponse,
        limit_in_mbps: _builtins.int,
        start_time: outputs.TimeResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def days(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> outputs.TimeResponse: ...
    @_builtins.property
    @pulumi.getter(name="limitInMbps")
    def limit_in_mbps(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> outputs.TimeResponse: ...
