

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRegionDiskResult', 'AwaitableGetRegionDiskResult', 'get_region_disk', 'get_region_disk_output']
@pulumi.output_type
class GetRegionDiskResult:
    
    def __init__(__self__, access_mode=..., async_primary_disks=..., create_snapshot_before_destroy=..., create_snapshot_before_destroy_prefix=..., creation_timestamp=..., description=..., disk_encryption_keys=..., disk_id=..., effective_labels=..., erase_windows_vss_signature=..., guest_os_features=..., id=..., interface=..., label_fingerprint=..., labels=..., last_attach_timestamp=..., last_detach_timestamp=..., licenses=..., name=..., physical_block_size_bytes=..., project=..., provisioned_iops=..., provisioned_throughput=..., pulumi_labels=..., region=..., replica_zones=..., self_link=..., size=..., snapshot=..., source_disk=..., source_disk_id=..., source_snapshot_encryption_keys=..., source_snapshot_id=..., type=..., users=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessMode")
    def access_mode(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="asyncPrimaryDisks")
    def async_primary_disks(self) -> Sequence[outputs.GetRegionDiskAsyncPrimaryDiskResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSnapshotBeforeDestroy")
    def create_snapshot_before_destroy(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createSnapshotBeforeDestroyPrefix")
    def create_snapshot_before_destroy_prefix(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskEncryptionKeys")
    def disk_encryption_keys(self) -> Sequence[outputs.GetRegionDiskDiskEncryptionKeyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskId")
    def disk_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eraseWindowsVssSignature")
    def erase_windows_vss_signature(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Sequence[outputs.GetRegionDiskGuestOsFeatureResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def interface(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastAttachTimestamp")
    def last_attach_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastDetachTimestamp")
    def last_detach_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def licenses(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="physicalBlockSizeBytes")
    def physical_block_size_bytes(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedIops")
    def provisioned_iops(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisionedThroughput")
    def provisioned_throughput(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def snapshot(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskId")
    def source_disk_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotEncryptionKeys")
    def source_snapshot_encryption_keys(self) -> Sequence[outputs.GetRegionDiskSourceSnapshotEncryptionKeyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotId")
    def source_snapshot_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def users(self) -> Sequence[_builtins.str]:
        ...
    


class AwaitableGetRegionDiskResult(GetRegionDiskResult):
    def __await__(self): # -> Generator[Never, Any, GetRegionDiskResult]:
        ...
    


def get_region_disk(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRegionDiskResult:
    
    ...

def get_region_disk_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRegionDiskResult]:
    
    ...

