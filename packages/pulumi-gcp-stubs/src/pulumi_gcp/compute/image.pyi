

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ImageArgs', 'Image']
@pulumi.input_type
class ImageArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[ImageGuestOsFeatureArgs]]]] = ..., image_encryption_key: Optional[pulumi.Input[ImageImageEncryptionKeyArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., raw_disk: Optional[pulumi.Input[ImageRawDiskArgs]] = ..., shielded_instance_initial_state: Optional[pulumi.Input[ImageShieldedInstanceInitialStateArgs]] = ..., source_disk: Optional[pulumi.Input[_builtins.str]] = ..., source_disk_encryption_key: Optional[pulumi.Input[ImageSourceDiskEncryptionKeyArgs]] = ..., source_image: Optional[pulumi.Input[_builtins.str]] = ..., source_image_encryption_key: Optional[pulumi.Input[ImageSourceImageEncryptionKeyArgs]] = ..., source_snapshot: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot_encryption_key: Optional[pulumi.Input[ImageSourceSnapshotEncryptionKeyArgs]] = ..., storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageGuestOsFeatureArgs]]]]:
        
        ...
    
    @guest_os_features.setter
    def guest_os_features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageGuestOsFeatureArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageEncryptionKey")
    def image_encryption_key(self) -> Optional[pulumi.Input[ImageImageEncryptionKeyArgs]]:
        
        ...
    
    @image_encryption_key.setter
    def image_encryption_key(self, value: Optional[pulumi.Input[ImageImageEncryptionKeyArgs]]): # -> None:
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawDisk")
    def raw_disk(self) -> Optional[pulumi.Input[ImageRawDiskArgs]]:
        
        ...
    
    @raw_disk.setter
    def raw_disk(self, value: Optional[pulumi.Input[ImageRawDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceInitialState")
    def shielded_instance_initial_state(self) -> Optional[pulumi.Input[ImageShieldedInstanceInitialStateArgs]]:
        
        ...
    
    @shielded_instance_initial_state.setter
    def shielded_instance_initial_state(self, value: Optional[pulumi.Input[ImageShieldedInstanceInitialStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_disk.setter
    def source_disk(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(self) -> Optional[pulumi.Input[ImageSourceDiskEncryptionKeyArgs]]:
        
        ...
    
    @source_disk_encryption_key.setter
    def source_disk_encryption_key(self, value: Optional[pulumi.Input[ImageSourceDiskEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_image.setter
    def source_image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceImageEncryptionKey")
    def source_image_encryption_key(self) -> Optional[pulumi.Input[ImageSourceImageEncryptionKeyArgs]]:
        
        ...
    
    @source_image_encryption_key.setter
    def source_image_encryption_key(self, value: Optional[pulumi.Input[ImageSourceImageEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_snapshot.setter
    def source_snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotEncryptionKey")
    def source_snapshot_encryption_key(self) -> Optional[pulumi.Input[ImageSourceSnapshotEncryptionKeyArgs]]:
        
        ...
    
    @source_snapshot_encryption_key.setter
    def source_snapshot_encryption_key(self, value: Optional[pulumi.Input[ImageSourceSnapshotEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @storage_locations.setter
    def storage_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ImageState:
    def __init__(__self__, *, archive_size_bytes: Optional[pulumi.Input[_builtins.int]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[ImageGuestOsFeatureArgs]]]] = ..., image_encryption_key: Optional[pulumi.Input[ImageImageEncryptionKeyArgs]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., raw_disk: Optional[pulumi.Input[ImageRawDiskArgs]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., shielded_instance_initial_state: Optional[pulumi.Input[ImageShieldedInstanceInitialStateArgs]] = ..., source_disk: Optional[pulumi.Input[_builtins.str]] = ..., source_disk_encryption_key: Optional[pulumi.Input[ImageSourceDiskEncryptionKeyArgs]] = ..., source_image: Optional[pulumi.Input[_builtins.str]] = ..., source_image_encryption_key: Optional[pulumi.Input[ImageSourceImageEncryptionKeyArgs]] = ..., source_snapshot: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot_encryption_key: Optional[pulumi.Input[ImageSourceSnapshotEncryptionKeyArgs]] = ..., storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveSizeBytes")
    def archive_size_bytes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @archive_size_bytes.setter
    def archive_size_bytes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disk_size_gb.setter
    def disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ImageGuestOsFeatureArgs]]]]:
        
        ...
    
    @guest_os_features.setter
    def guest_os_features(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ImageGuestOsFeatureArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageEncryptionKey")
    def image_encryption_key(self) -> Optional[pulumi.Input[ImageImageEncryptionKeyArgs]]:
        
        ...
    
    @image_encryption_key.setter
    def image_encryption_key(self, value: Optional[pulumi.Input[ImageImageEncryptionKeyArgs]]): # -> None:
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawDisk")
    def raw_disk(self) -> Optional[pulumi.Input[ImageRawDiskArgs]]:
        
        ...
    
    @raw_disk.setter
    def raw_disk(self, value: Optional[pulumi.Input[ImageRawDiskArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceInitialState")
    def shielded_instance_initial_state(self) -> Optional[pulumi.Input[ImageShieldedInstanceInitialStateArgs]]:
        
        ...
    
    @shielded_instance_initial_state.setter
    def shielded_instance_initial_state(self, value: Optional[pulumi.Input[ImageShieldedInstanceInitialStateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_disk.setter
    def source_disk(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(self) -> Optional[pulumi.Input[ImageSourceDiskEncryptionKeyArgs]]:
        
        ...
    
    @source_disk_encryption_key.setter
    def source_disk_encryption_key(self, value: Optional[pulumi.Input[ImageSourceDiskEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_image.setter
    def source_image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceImageEncryptionKey")
    def source_image_encryption_key(self) -> Optional[pulumi.Input[ImageSourceImageEncryptionKeyArgs]]:
        
        ...
    
    @source_image_encryption_key.setter
    def source_image_encryption_key(self, value: Optional[pulumi.Input[ImageSourceImageEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_snapshot.setter
    def source_snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotEncryptionKey")
    def source_snapshot_encryption_key(self) -> Optional[pulumi.Input[ImageSourceSnapshotEncryptionKeyArgs]]:
        
        ...
    
    @source_snapshot_encryption_key.setter
    def source_snapshot_encryption_key(self, value: Optional[pulumi.Input[ImageSourceSnapshotEncryptionKeyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @storage_locations.setter
    def storage_locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/image:Image")
class Image(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ImageGuestOsFeatureArgs, ImageGuestOsFeatureArgsDict]]]]] = ..., image_encryption_key: Optional[pulumi.Input[Union[ImageImageEncryptionKeyArgs, ImageImageEncryptionKeyArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., raw_disk: Optional[pulumi.Input[Union[ImageRawDiskArgs, ImageRawDiskArgsDict]]] = ..., shielded_instance_initial_state: Optional[pulumi.Input[Union[ImageShieldedInstanceInitialStateArgs, ImageShieldedInstanceInitialStateArgsDict]]] = ..., source_disk: Optional[pulumi.Input[_builtins.str]] = ..., source_disk_encryption_key: Optional[pulumi.Input[Union[ImageSourceDiskEncryptionKeyArgs, ImageSourceDiskEncryptionKeyArgsDict]]] = ..., source_image: Optional[pulumi.Input[_builtins.str]] = ..., source_image_encryption_key: Optional[pulumi.Input[Union[ImageSourceImageEncryptionKeyArgs, ImageSourceImageEncryptionKeyArgsDict]]] = ..., source_snapshot: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot_encryption_key: Optional[pulumi.Input[Union[ImageSourceSnapshotEncryptionKeyArgs, ImageSourceSnapshotEncryptionKeyArgsDict]]] = ..., storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ImageArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., archive_size_bytes: Optional[pulumi.Input[_builtins.int]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., family: Optional[pulumi.Input[_builtins.str]] = ..., guest_os_features: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ImageGuestOsFeatureArgs, ImageGuestOsFeatureArgsDict]]]]] = ..., image_encryption_key: Optional[pulumi.Input[Union[ImageImageEncryptionKeyArgs, ImageImageEncryptionKeyArgsDict]]] = ..., label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., licenses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., raw_disk: Optional[pulumi.Input[Union[ImageRawDiskArgs, ImageRawDiskArgsDict]]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., shielded_instance_initial_state: Optional[pulumi.Input[Union[ImageShieldedInstanceInitialStateArgs, ImageShieldedInstanceInitialStateArgsDict]]] = ..., source_disk: Optional[pulumi.Input[_builtins.str]] = ..., source_disk_encryption_key: Optional[pulumi.Input[Union[ImageSourceDiskEncryptionKeyArgs, ImageSourceDiskEncryptionKeyArgsDict]]] = ..., source_image: Optional[pulumi.Input[_builtins.str]] = ..., source_image_encryption_key: Optional[pulumi.Input[Union[ImageSourceImageEncryptionKeyArgs, ImageSourceImageEncryptionKeyArgsDict]]] = ..., source_snapshot: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot_encryption_key: Optional[pulumi.Input[Union[ImageSourceSnapshotEncryptionKeyArgs, ImageSourceSnapshotEncryptionKeyArgsDict]]] = ..., storage_locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> Image:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="archiveSizeBytes")
    def archive_size_bytes(self) -> pulumi.Output[_builtins.int]:
        
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
    @pulumi.getter(name="diskSizeGb")
    def disk_size_gb(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def family(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guestOsFeatures")
    def guest_os_features(self) -> pulumi.Output[Sequence[outputs.ImageGuestOsFeature]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageEncryptionKey")
    def image_encryption_key(self) -> pulumi.Output[Optional[outputs.ImageImageEncryptionKey]]:
        
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
    @pulumi.getter
    def licenses(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rawDisk")
    def raw_disk(self) -> pulumi.Output[Optional[outputs.ImageRawDisk]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceInitialState")
    def shielded_instance_initial_state(self) -> pulumi.Output[outputs.ImageShieldedInstanceInitialState]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDiskEncryptionKey")
    def source_disk_encryption_key(self) -> pulumi.Output[Optional[outputs.ImageSourceDiskEncryptionKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceImageEncryptionKey")
    def source_image_encryption_key(self) -> pulumi.Output[Optional[outputs.ImageSourceImageEncryptionKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshotEncryptionKey")
    def source_snapshot_encryption_key(self) -> pulumi.Output[Optional[outputs.ImageSourceSnapshotEncryptionKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocations")
    def storage_locations(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    


