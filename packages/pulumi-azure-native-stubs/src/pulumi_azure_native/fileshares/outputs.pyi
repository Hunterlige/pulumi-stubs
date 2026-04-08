import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FileShareLimitsOutputResponse",
    "FileShareLimitsResponse",
    "FileSharePropertiesResponse",
    "FileShareProvisioningConstantsResponse",
    "FileShareProvisioningRecommendationOutputResponse",
    "FileShareSnapshotPropertiesResponse",
    "FileShareUsageDataOutputResponse",
    "LiveSharesUsageDataResponse",
    "NfsProtocolPropertiesResponse",
    "PrivateEndpointConnectionResponse",
    "PrivateEndpointResponse",
    "PrivateLinkServiceConnectionStateResponse",
    "PublicAccessPropertiesResponse",
    "SystemDataResponse",
]

@pulumi.output_type
class FileShareLimitsOutputResponse(dict):
    def __init__(
        __self__,
        *,
        limits: outputs.FileShareLimitsResponse,
        provisioning_constants: outputs.FileShareProvisioningConstantsResponse,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> outputs.FileShareLimitsResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningConstants")
    def provisioning_constants(
        self,
    ) -> outputs.FileShareProvisioningConstantsResponse: ...

@pulumi.output_type
class FileShareLimitsResponse(dict):
    def __init__(
        __self__,
        *,
        max_file_share_private_endpoint_connections: _builtins.int,
        max_file_share_snapshots: _builtins.int,
        max_file_share_subnets: _builtins.int,
        max_file_shares: _builtins.int,
        max_provisioned_io_per_sec: _builtins.int,
        max_provisioned_storage_gi_b: _builtins.int,
        max_provisioned_throughput_mi_b_per_sec: _builtins.int,
        min_provisioned_io_per_sec: _builtins.int,
        min_provisioned_storage_gi_b: _builtins.int,
        min_provisioned_throughput_mi_b_per_sec: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxFileSharePrivateEndpointConnections")
    def max_file_share_private_endpoint_connections(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxFileShareSnapshots")
    def max_file_share_snapshots(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxFileShareSubnets")
    def max_file_share_subnets(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxFileShares")
    def max_file_shares(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxProvisionedIOPerSec")
    def max_provisioned_io_per_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxProvisionedStorageGiB")
    def max_provisioned_storage_gi_b(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxProvisionedThroughputMiBPerSec")
    def max_provisioned_throughput_mi_b_per_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minProvisionedIOPerSec")
    def min_provisioned_io_per_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minProvisionedStorageGiB")
    def min_provisioned_storage_gi_b(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="minProvisionedThroughputMiBPerSec")
    def min_provisioned_throughput_mi_b_per_sec(self) -> _builtins.int: ...

@pulumi.output_type
class FileSharePropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host_name: _builtins.str,
        included_burst_io_per_sec: _builtins.int,
        max_burst_io_per_sec_credits: _builtins.float,
        private_endpoint_connections: Sequence[
            outputs.PrivateEndpointConnectionResponse
        ],
        provisioned_io_per_sec_next_allowed_downgrade: _builtins.str,
        provisioned_storage_next_allowed_downgrade: _builtins.str,
        provisioned_throughput_next_allowed_downgrade: _builtins.str,
        provisioning_state: _builtins.str,
        media_tier: Optional[_builtins.str] = ...,
        mount_name: Optional[_builtins.str] = ...,
        nfs_protocol_properties: Optional[outputs.NfsProtocolPropertiesResponse] = ...,
        protocol: Optional[_builtins.str] = ...,
        provisioned_io_per_sec: Optional[_builtins.int] = ...,
        provisioned_storage_gi_b: Optional[_builtins.int] = ...,
        provisioned_throughput_mi_b_per_sec: Optional[_builtins.int] = ...,
        public_access_properties: Optional[
            outputs.PublicAccessPropertiesResponse
        ] = ...,
        public_network_access: Optional[_builtins.str] = ...,
        redundancy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="includedBurstIOPerSec")
    def included_burst_io_per_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxBurstIOPerSecCredits")
    def max_burst_io_per_sec_credits(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIOPerSecNextAllowedDowngrade")
    def provisioned_io_per_sec_next_allowed_downgrade(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedStorageNextAllowedDowngrade")
    def provisioned_storage_next_allowed_downgrade(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughputNextAllowedDowngrade")
    def provisioned_throughput_next_allowed_downgrade(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mediaTier")
    def media_tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mountName")
    def mount_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="nfsProtocolProperties")
    def nfs_protocol_properties(
        self,
    ) -> Optional[outputs.NfsProtocolPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIOPerSec")
    def provisioned_io_per_sec(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedStorageGiB")
    def provisioned_storage_gi_b(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughputMiBPerSec")
    def provisioned_throughput_mi_b_per_sec(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="publicAccessProperties")
    def public_access_properties(
        self,
    ) -> Optional[outputs.PublicAccessPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def redundancy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FileShareProvisioningConstantsResponse(dict):
    def __init__(
        __self__,
        *,
        base_io_per_sec: _builtins.int,
        base_throughput_mi_b_per_sec: _builtins.int,
        scalar_io_per_sec: _builtins.float,
        scalar_throughput_mi_b_per_sec: _builtins.float,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseIOPerSec")
    def base_io_per_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="baseThroughputMiBPerSec")
    def base_throughput_mi_b_per_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scalarIOPerSec")
    def scalar_io_per_sec(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="scalarThroughputMiBPerSec")
    def scalar_throughput_mi_b_per_sec(self) -> _builtins.float: ...

@pulumi.output_type
class FileShareProvisioningRecommendationOutputResponse(dict):
    def __init__(
        __self__,
        *,
        available_redundancy_options: Sequence[_builtins.str],
        provisioned_io_per_sec: _builtins.int,
        provisioned_throughput_mi_b_per_sec: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availableRedundancyOptions")
    def available_redundancy_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedIOPerSec")
    def provisioned_io_per_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughputMiBPerSec")
    def provisioned_throughput_mi_b_per_sec(self) -> _builtins.int: ...

@pulumi.output_type
class FileShareSnapshotPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        initiator_id: _builtins.str,
        snapshot_time: _builtins.str,
        metadata: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="initiatorId")
    def initiator_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="snapshotTime")
    def snapshot_time(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class FileShareUsageDataOutputResponse(dict):
    def __init__(
        __self__, *, live_shares: outputs.LiveSharesUsageDataResponse
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="liveShares")
    def live_shares(self) -> outputs.LiveSharesUsageDataResponse: ...

@pulumi.output_type
class LiveSharesUsageDataResponse(dict):
    def __init__(__self__, *, file_share_count: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileShareCount")
    def file_share_count(self) -> _builtins.int: ...

@pulumi.output_type
class NfsProtocolPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, root_squash: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rootSquash")
    def root_squash(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_ids: Sequence[_builtins.str],
        id: _builtins.str,
        name: _builtins.str,
        private_link_service_connection_state: outputs.PrivateLinkServiceConnectionStateResponse,
        provisioning_state: _builtins.str,
        system_data: outputs.SystemDataResponse,
        type: _builtins.str,
        private_endpoint: Optional[outputs.PrivateEndpointResponse] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(
        self,
    ) -> outputs.PrivateLinkServiceConnectionStateResponse: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[outputs.PrivateEndpointResponse]: ...

@pulumi.output_type
class PrivateEndpointResponse(dict):
    def __init__(__self__, *, id: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions_required: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PublicAccessPropertiesResponse(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, allowed_subnets: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSubnets")
    def allowed_subnets(self) -> Optional[Sequence[_builtins.str]]: ...

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
