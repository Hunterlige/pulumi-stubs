import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSnapshotResult",
    "AwaitableGetSnapshotResult",
    "get_snapshot",
    "get_snapshot_output",
]

@pulumi.output_type
class GetSnapshotResult:
    def __init__(
        __self__,
        chain_name=...,
        creation_timestamp=...,
        description=...,
        disk_size_gb=...,
        effective_labels=...,
        filter=...,
        guest_flush=...,
        id=...,
        label_fingerprint=...,
        labels=...,
        licenses=...,
        most_recent=...,
        name=...,
        project=...,
        pulumi_labels=...,
        self_link=...,
        snapshot_encryption_keys=...,
        snapshot_id=...,
        snapshot_type=...,
        source_disk=...,
        source_disk_encryption_keys=...,
        source_instant_snapshot=...,
        storage_bytes=...,
        storage_locations=...,
        zone=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chainName")
    def chain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="guestFlush")
    def guest_flush(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="snapshotEncryptionKeys")
    def snapshot_encryption_keys(
        self,
    ) -> Sequence[outputs.GetSnapshotSnapshotEncryptionKeyResult]: ...
    @_builtins.property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceDiskEncryptionKeys")
    def source_disk_encryption_keys(
        self,
    ) -> Sequence[outputs.GetSnapshotSourceDiskEncryptionKeyResult]: ...
    @_builtins.property
    @pulumi.getter(name="sourceInstantSnapshot")
    def source_instant_snapshot(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="storageBytes")
    def storage_bytes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

class AwaitableGetSnapshotResult(GetSnapshotResult):
    def __await__(self): ...

def get_snapshot(
    filter: Optional[_builtins.str] = ...,
    most_recent: Optional[_builtins.bool] = ...,
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSnapshotResult: ...
def get_snapshot_output(
    filter: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    most_recent: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSnapshotResult]: ...
