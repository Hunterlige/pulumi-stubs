import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FileSharePropertiesArgs",
    "FileSharePropertiesArgsDict",
    "FileShareProvisioningRecommendationInput",
    "FileShareProvisioningRecommendationInputDict",
    "FileShareSnapshotPropertiesArgs",
    "FileShareSnapshotPropertiesArgsDict",
    "NfsProtocolPropertiesArgs",
    "NfsProtocolPropertiesArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "PublicAccessPropertiesArgs",
    "PublicAccessPropertiesArgsDict",
]

class FileSharePropertiesArgsDict(TypedDict):
    media_tier: NotRequired[pulumi.Input[Union[_builtins.str, MediaTier]]]
    mount_name: NotRequired[pulumi.Input[_builtins.str]]
    nfs_protocol_properties: NotRequired[pulumi.Input[NfsProtocolPropertiesArgsDict]]
    protocol: NotRequired[pulumi.Input[Union[_builtins.str, Protocol]]]
    provisioned_io_per_sec: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_storage_gi_b: NotRequired[pulumi.Input[_builtins.int]]
    provisioned_throughput_mi_b_per_sec: NotRequired[pulumi.Input[_builtins.int]]
    public_access_properties: NotRequired[pulumi.Input[PublicAccessPropertiesArgsDict]]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
    ]
    redundancy: NotRequired[pulumi.Input[Union[_builtins.str, Redundancy]]]

@pulumi.input_type
class FileSharePropertiesArgs:
    def __init__(
        __self__,
        *,
        media_tier: Optional[pulumi.Input[Union[_builtins.str, MediaTier]]] = ...,
        mount_name: Optional[pulumi.Input[_builtins.str]] = ...,
        nfs_protocol_properties: Optional[
            pulumi.Input[NfsProtocolPropertiesArgs]
        ] = ...,
        protocol: Optional[pulumi.Input[Union[_builtins.str, Protocol]]] = ...,
        provisioned_io_per_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_storage_gi_b: Optional[pulumi.Input[_builtins.int]] = ...,
        provisioned_throughput_mi_b_per_sec: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        public_access_properties: Optional[
            pulumi.Input[PublicAccessPropertiesArgs]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        redundancy: Optional[pulumi.Input[Union[_builtins.str, Redundancy]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mediaTier")
    def media_tier(self) -> Optional[pulumi.Input[Union[_builtins.str, MediaTier]]]: ...
    @media_tier.setter
    def media_tier(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MediaTier]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mountName")
    def mount_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mount_name.setter
    def mount_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nfsProtocolProperties")
    def nfs_protocol_properties(
        self,
    ) -> Optional[pulumi.Input[NfsProtocolPropertiesArgs]]: ...
    @nfs_protocol_properties.setter
    def nfs_protocol_properties(
        self, value: Optional[pulumi.Input[NfsProtocolPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, Protocol]]]: ...
    @protocol.setter
    def protocol(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Protocol]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionedIOPerSec")
    def provisioned_io_per_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_io_per_sec.setter
    def provisioned_io_per_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="provisionedStorageGiB")
    def provisioned_storage_gi_b(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_storage_gi_b.setter
    def provisioned_storage_gi_b(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionedThroughputMiBPerSec")
    def provisioned_throughput_mi_b_per_sec(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @provisioned_throughput_mi_b_per_sec.setter
    def provisioned_throughput_mi_b_per_sec(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicAccessProperties")
    def public_access_properties(
        self,
    ) -> Optional[pulumi.Input[PublicAccessPropertiesArgs]]: ...
    @public_access_properties.setter
    def public_access_properties(
        self, value: Optional[pulumi.Input[PublicAccessPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def redundancy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, Redundancy]]]: ...
    @redundancy.setter
    def redundancy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, Redundancy]]]
    ): ...

class FileShareProvisioningRecommendationInputDict(TypedDict):
    provisioned_storage_gi_b: _builtins.int

@pulumi.input_type
class FileShareProvisioningRecommendationInput:
    def __init__(__self__, *, provisioned_storage_gi_b: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="provisionedStorageGiB")
    def provisioned_storage_gi_b(self) -> _builtins.int: ...
    @provisioned_storage_gi_b.setter
    def provisioned_storage_gi_b(self, value: _builtins.int): ...

class FileShareSnapshotPropertiesArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class FileShareSnapshotPropertiesArgs:
    def __init__(
        __self__,
        *,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class NfsProtocolPropertiesArgsDict(TypedDict):
    root_squash: NotRequired[pulumi.Input[Union[_builtins.str, ShareRootSquash]]]

@pulumi.input_type
class NfsProtocolPropertiesArgs:
    def __init__(
        __self__,
        *,
        root_squash: Optional[
            pulumi.Input[Union[_builtins.str, ShareRootSquash]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rootSquash")
    def root_squash(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ShareRootSquash]]]: ...
    @root_squash.setter
    def root_squash(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ShareRootSquash]]]
    ): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ],
    ): ...

class PublicAccessPropertiesArgsDict(TypedDict):
    allowed_subnets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class PublicAccessPropertiesArgs:
    def __init__(
        __self__,
        *,
        allowed_subnets: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedSubnets")
    def allowed_subnets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_subnets.setter
    def allowed_subnets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
