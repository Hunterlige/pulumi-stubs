

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegionDiskArgs', 'RegionDisk']
@pulumi.input_type
class RegionDiskArgs:
    def __init__(__self__, *, replica_zones: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], access_mode: Optional[pulumi.Input[_builtins.str]] = ..., async_primary_disk: Optional[pulumi.Input[RegionDiskAsyncPrimaryDiskArgs]] = ..., create_snapshot_before_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., create_snapshot_before_destroy_prefix: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_encryption_key: Optional[pulumi.Input[RegionDiskDiskEncryptionKeyArgs]] = ..., erase_windows_vss_signature: Optional[pulumi.Input[_builtins.bool]] = ..., guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[RegionDiskGuestOsFeatureArgs]]]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., physical_block_size_bytes: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_throughput: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.int]] = ..., snapshot: Optional[pulumi.Input[_builtins.str]] = ..., source_disk: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot_encryption_key: Optional[pulumi.Input[RegionDiskSourceSnapshotEncryptionKeyArgs]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @replica_zones.setter
    def replica_zones(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncPrimaryDisk")
    def async_primary_disk(self) -> Optional[pulumi.Input[RegionDiskAsyncPrimaryDiskArgs]]:
        
        ...
    
    @async_primary_disk.setter
    def async_primary_disk(self, value: Optional[pulumi.Input[RegionDiskAsyncPrimaryDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSnapshotBeforeDestroy")
    def create_snapshot_before_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_snapshot_before_destroy.setter
    def create_snapshot_before_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSnapshotBeforeDestroyPrefix")
    def create_snapshot_before_destroy_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_snapshot_before_destroy_prefix.setter
    def create_snapshot_before_destroy_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(self) -> Optional[pulumi.Input[RegionDiskDiskEncryptionKeyArgs]]:
        
        ...
    
    @disk_encryption_key.setter
    def disk_encryption_key(self, value: Optional[pulumi.Input[RegionDiskDiskEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eraseWindowsVssSignature")
    def erase_windows_vss_signature(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @erase_windows_vss_signature.setter
    def erase_windows_vss_signature(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionDiskGuestOsFeatureArgs]]]]:
        
        ...
    
    @guest_os_features.setter
    def guest_os_features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionDiskGuestOsFeatureArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def interface(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface.setter
    def interface(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @licenses.setter
    def licenses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalBlockSizeBytes")
    def physical_block_size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @physical_block_size_bytes.setter
    def physical_block_size_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_iops.setter
    def provisioned_iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot.setter
    def snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_disk.setter
    def source_disk(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotEncryptionKey")
    def source_snapshot_encryption_key(self) -> Optional[pulumi.Input[RegionDiskSourceSnapshotEncryptionKeyArgs]]:
        
        ...
    
    @source_snapshot_encryption_key.setter
    def source_snapshot_encryption_key(self, value: Optional[pulumi.Input[RegionDiskSourceSnapshotEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _RegionDiskState:
    def __init__(__self__, *, access_mode: Optional[pulumi.Input[_builtins.str]] = ..., async_primary_disk: Optional[pulumi.Input[RegionDiskAsyncPrimaryDiskArgs]] = ..., create_snapshot_before_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., create_snapshot_before_destroy_prefix: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_encryption_key: Optional[pulumi.Input[RegionDiskDiskEncryptionKeyArgs]] = ..., disk_id: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., erase_windows_vss_signature: Optional[pulumi.Input[_builtins.bool]] = ..., guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[RegionDiskGuestOsFeatureArgs]]]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., last_attach_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., last_detach_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., physical_block_size_bytes: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_throughput: Optional[pulumi.Input[_builtins.int]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.int]] = ..., snapshot: Optional[pulumi.Input[_builtins.str]] = ..., source_disk: Optional[pulumi.Input[_builtins.str]] = ..., source_disk_id: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot_encryption_key: Optional[pulumi.Input[RegionDiskSourceSnapshotEncryptionKeyArgs]] = ..., source_snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., users: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_mode.setter
    def access_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncPrimaryDisk")
    def async_primary_disk(self) -> Optional[pulumi.Input[RegionDiskAsyncPrimaryDiskArgs]]:
        
        ...
    
    @async_primary_disk.setter
    def async_primary_disk(self, value: Optional[pulumi.Input[RegionDiskAsyncPrimaryDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSnapshotBeforeDestroy")
    def create_snapshot_before_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_snapshot_before_destroy.setter
    def create_snapshot_before_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSnapshotBeforeDestroyPrefix")
    def create_snapshot_before_destroy_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_snapshot_before_destroy_prefix.setter
    def create_snapshot_before_destroy_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(self) -> Optional[pulumi.Input[RegionDiskDiskEncryptionKeyArgs]]:
        
        ...
    
    @disk_encryption_key.setter
    def disk_encryption_key(self, value: Optional[pulumi.Input[RegionDiskDiskEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_id.setter
    def disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eraseWindowsVssSignature")
    def erase_windows_vss_signature(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @erase_windows_vss_signature.setter
    def erase_windows_vss_signature(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RegionDiskGuestOsFeatureArgs]]]]:
        
        ...
    
    @guest_os_features.setter
    def guest_os_features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RegionDiskGuestOsFeatureArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def interface(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interface.setter
    def interface(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @label_fingerprint.setter
    def label_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAttachTimestamp")
    def last_attach_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_attach_timestamp.setter
    def last_attach_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDetachTimestamp")
    def last_detach_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_detach_timestamp.setter
    def last_detach_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @licenses.setter
    def licenses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalBlockSizeBytes")
    def physical_block_size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @physical_block_size_bytes.setter
    def physical_block_size_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_iops.setter
    def provisioned_iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @provisioned_throughput.setter
    def provisioned_throughput(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @replica_zones.setter
    def replica_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @size.setter
    def size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @snapshot.setter
    def snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_disk.setter
    def source_disk(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_disk_id.setter
    def source_disk_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotEncryptionKey")
    def source_snapshot_encryption_key(self) -> Optional[pulumi.Input[RegionDiskSourceSnapshotEncryptionKeyArgs]]:
        
        ...
    
    @source_snapshot_encryption_key.setter
    def source_snapshot_encryption_key(self, value: Optional[pulumi.Input[RegionDiskSourceSnapshotEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotId")
    def source_snapshot_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_snapshot_id.setter
    def source_snapshot_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/regionDisk:RegionDisk")
class RegionDisk(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_mode: Optional[pulumi.Input[_builtins.str]] = ..., async_primary_disk: Optional[pulumi.Input[Union[RegionDiskAsyncPrimaryDiskArgs, RegionDiskAsyncPrimaryDiskArgsDict]]] = ..., create_snapshot_before_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., create_snapshot_before_destroy_prefix: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_encryption_key: Optional[pulumi.Input[Union[RegionDiskDiskEncryptionKeyArgs, RegionDiskDiskEncryptionKeyArgsDict]]] = ..., erase_windows_vss_signature: Optional[pulumi.Input[_builtins.bool]] = ..., guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionDiskGuestOsFeatureArgs, RegionDiskGuestOsFeatureArgsDict]]]]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., physical_block_size_bytes: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_throughput: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., size: Optional[pulumi.Input[_builtins.int]] = ..., snapshot: Optional[pulumi.Input[_builtins.str]] = ..., source_disk: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot_encryption_key: Optional[pulumi.Input[Union[RegionDiskSourceSnapshotEncryptionKeyArgs, RegionDiskSourceSnapshotEncryptionKeyArgsDict]]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RegionDiskArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_mode: Optional[pulumi.Input[_builtins.str]] = ..., async_primary_disk: Optional[pulumi.Input[Union[RegionDiskAsyncPrimaryDiskArgs, RegionDiskAsyncPrimaryDiskArgsDict]]] = ..., create_snapshot_before_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., create_snapshot_before_destroy_prefix: Optional[pulumi.Input[_builtins.str]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_encryption_key: Optional[pulumi.Input[Union[RegionDiskDiskEncryptionKeyArgs, RegionDiskDiskEncryptionKeyArgsDict]]] = ..., disk_id: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., erase_windows_vss_signature: Optional[pulumi.Input[_builtins.bool]] = ..., guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RegionDiskGuestOsFeatureArgs, RegionDiskGuestOsFeatureArgsDict]]]]] = ..., interface: Optional[pulumi.Input[_builtins.str]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., last_attach_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., last_detach_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., physical_block_size_bytes: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., provisioned_iops: Optional[pulumi.Input[_builtins.int]] = ..., provisioned_throughput: Optional[pulumi.Input[_builtins.int]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., replica_zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., size: Optional[pulumi.Input[_builtins.int]] = ..., snapshot: Optional[pulumi.Input[_builtins.str]] = ..., source_disk: Optional[pulumi.Input[_builtins.str]] = ..., source_disk_id: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot_encryption_key: Optional[pulumi.Input[Union[RegionDiskSourceSnapshotEncryptionKeyArgs, RegionDiskSourceSnapshotEncryptionKeyArgsDict]]] = ..., source_snapshot_id: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., users: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> RegionDisk:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncPrimaryDisk")
    def async_primary_disk(self) -> pulumi.Output[Optional[outputs.RegionDiskAsyncPrimaryDisk]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSnapshotBeforeDestroy")
    def create_snapshot_before_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSnapshotBeforeDestroyPrefix")
    def create_snapshot_before_destroy_prefix(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKey")
    def disk_encryption_key(self) -> pulumi.Output[Optional[outputs.RegionDiskDiskEncryptionKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eraseWindowsVssSignature")
    def erase_windows_vss_signature(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> pulumi.Output[Sequence[outputs.RegionDiskGuestOsFeature]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    @_utilities.deprecated(...)
    def interface(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAttachTimestamp")
    def last_attach_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDetachTimestamp")
    def last_detach_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalBlockSizeBytes")
    def physical_block_size_bytes(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotEncryptionKey")
    def source_snapshot_encryption_key(self) -> pulumi.Output[Optional[outputs.RegionDiskSourceSnapshotEncryptionKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotId")
    def source_snapshot_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


