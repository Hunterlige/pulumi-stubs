import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SnapshotArgs", "Snapshot"]

@pulumi.input_type
class SnapshotArgs:
    def __init__(
        __self__,
        *,
        chain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        guest_flush: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_encryption_key: Optional[
            pulumi.Input[SnapshotSnapshotEncryptionKeyArgs]
        ] = ...,
        snapshot_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_disk: Optional[pulumi.Input[_builtins.str]] = ...,
        source_disk_encryption_key: Optional[
            pulumi.Input[SnapshotSourceDiskEncryptionKeyArgs]
        ] = ...,
        source_instant_snapshot: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @chain_name.setter
    def chain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @guest_flush.setter
    def guest_flush(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotEncryptionKey")
    def snapshot_encryption_key(
        self,
    ) -> Optional[pulumi.Input[SnapshotSnapshotEncryptionKeyArgs]]: ...
    @snapshot_encryption_key.setter
    def snapshot_encryption_key(
        self, value: Optional[pulumi.Input[SnapshotSnapshotEncryptionKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_type.setter
    def snapshot_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_disk.setter
    def source_disk(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(
        self,
    ) -> Optional[pulumi.Input[SnapshotSourceDiskEncryptionKeyArgs]]: ...
    @source_disk_encryption_key.setter
    def source_disk_encryption_key(
        self, value: Optional[pulumi.Input[SnapshotSourceDiskEncryptionKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceInstantSnapshot")
    def source_instant_snapshot(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_instant_snapshot.setter
    def source_instant_snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_locations.setter
    def storage_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SnapshotState:
    def __init__(
        __self__,
        *,
        chain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        guest_flush: Optional[pulumi.Input[_builtins.bool]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_encryption_key: Optional[
            pulumi.Input[SnapshotSnapshotEncryptionKeyArgs]
        ] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_disk: Optional[pulumi.Input[_builtins.str]] = ...,
        source_disk_encryption_key: Optional[
            pulumi.Input[SnapshotSourceDiskEncryptionKeyArgs]
        ] = ...,
        source_instant_snapshot: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @chain_name.setter
    def chain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @guest_flush.setter
    def guest_flush(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label_fingerprint.setter
    def label_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def licenses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @licenses.setter
    def licenses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotEncryptionKey")
    def snapshot_encryption_key(
        self,
    ) -> Optional[pulumi.Input[SnapshotSnapshotEncryptionKeyArgs]]: ...
    @snapshot_encryption_key.setter
    def snapshot_encryption_key(
        self, value: Optional[pulumi.Input[SnapshotSnapshotEncryptionKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @snapshot_type.setter
    def snapshot_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_disk.setter
    def source_disk(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(
        self,
    ) -> Optional[pulumi.Input[SnapshotSourceDiskEncryptionKeyArgs]]: ...
    @source_disk_encryption_key.setter
    def source_disk_encryption_key(
        self, value: Optional[pulumi.Input[SnapshotSourceDiskEncryptionKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceInstantSnapshot")
    def source_instant_snapshot(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_instant_snapshot.setter
    def source_instant_snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageBytes")
    def storage_bytes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @storage_bytes.setter
    def storage_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @storage_locations.setter
    def storage_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/snapshot:Snapshot")
class Snapshot(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        chain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        guest_flush: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_encryption_key: Optional[
            pulumi.Input[
                Union[
                    SnapshotSnapshotEncryptionKeyArgs,
                    SnapshotSnapshotEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        snapshot_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_disk: Optional[pulumi.Input[_builtins.str]] = ...,
        source_disk_encryption_key: Optional[
            pulumi.Input[
                Union[
                    SnapshotSourceDiskEncryptionKeyArgs,
                    SnapshotSourceDiskEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        source_instant_snapshot: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[SnapshotArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        chain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        guest_flush: Optional[pulumi.Input[_builtins.bool]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        snapshot_encryption_key: Optional[
            pulumi.Input[
                Union[
                    SnapshotSnapshotEncryptionKeyArgs,
                    SnapshotSnapshotEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        snapshot_id: Optional[pulumi.Input[_builtins.int]] = ...,
        snapshot_type: Optional[pulumi.Input[_builtins.str]] = ...,
        source_disk: Optional[pulumi.Input[_builtins.str]] = ...,
        source_disk_encryption_key: Optional[
            pulumi.Input[
                Union[
                    SnapshotSourceDiskEncryptionKeyArgs,
                    SnapshotSourceDiskEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        source_instant_snapshot: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_bytes: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Snapshot: ...
    @_builtins.property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotEncryptionKey")
    def snapshot_encryption_key(
        self,
    ) -> pulumi.Output[Optional[outputs.SnapshotSnapshotEncryptionKey]]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(
        self,
    ) -> pulumi.Output[Optional[outputs.SnapshotSourceDiskEncryptionKey]]: ...
    @_builtins.property
    @pulumi.getter(name="sourceInstantSnapshot")
    def source_instant_snapshot(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="storageBytes")
    def storage_bytes(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]: ...
