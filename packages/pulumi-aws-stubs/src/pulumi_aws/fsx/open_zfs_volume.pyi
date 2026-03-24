

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
__all__ = ['OpenZfsVolumeArgs', 'OpenZfsVolume']
@pulumi.input_type
class OpenZfsVolumeArgs:
    def __init__(__self__, *, parent_volume_id: pulumi.Input[_builtins.str], copy_tags_to_snapshots: Optional[pulumi.Input[_builtins.bool]] = ..., data_compression_type: Optional[pulumi.Input[_builtins.str]] = ..., delete_volume_options: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nfs_exports: Optional[pulumi.Input[OpenZfsVolumeNfsExportsArgs]] = ..., origin_snapshot: Optional[pulumi.Input[OpenZfsVolumeOriginSnapshotArgs]] = ..., read_only: Optional[pulumi.Input[_builtins.bool]] = ..., record_size_kib: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_capacity_quota_gib: Optional[pulumi.Input[_builtins.int]] = ..., storage_capacity_reservation_gib: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_and_group_quotas: Optional[pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeUserAndGroupQuotaArgs]]]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentVolumeId")
    def parent_volume_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent_volume_id.setter
    def parent_volume_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshots")
    def copy_tags_to_snapshots(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @copy_tags_to_snapshots.setter
    def copy_tags_to_snapshots(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCompressionType")
    def data_compression_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_compression_type.setter
    def data_compression_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteVolumeOptions")
    def delete_volume_options(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_volume_options.setter
    def delete_volume_options(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsExports")
    def nfs_exports(self) -> Optional[pulumi.Input[OpenZfsVolumeNfsExportsArgs]]:
        
        ...
    
    @nfs_exports.setter
    def nfs_exports(self, value: Optional[pulumi.Input[OpenZfsVolumeNfsExportsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originSnapshot")
    def origin_snapshot(self) -> Optional[pulumi.Input[OpenZfsVolumeOriginSnapshotArgs]]:
        
        ...
    
    @origin_snapshot.setter
    def origin_snapshot(self, value: Optional[pulumi.Input[OpenZfsVolumeOriginSnapshotArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordSizeKib")
    def record_size_kib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @record_size_kib.setter
    def record_size_kib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_capacity_quota_gib.setter
    def storage_capacity_quota_gib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityReservationGib")
    def storage_capacity_reservation_gib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_capacity_reservation_gib.setter
    def storage_capacity_reservation_gib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAndGroupQuotas")
    def user_and_group_quotas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeUserAndGroupQuotaArgs]]]]:
        
        ...
    
    @user_and_group_quotas.setter
    def user_and_group_quotas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeUserAndGroupQuotaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _OpenZfsVolumeState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., copy_tags_to_snapshots: Optional[pulumi.Input[_builtins.bool]] = ..., data_compression_type: Optional[pulumi.Input[_builtins.str]] = ..., delete_volume_options: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nfs_exports: Optional[pulumi.Input[OpenZfsVolumeNfsExportsArgs]] = ..., origin_snapshot: Optional[pulumi.Input[OpenZfsVolumeOriginSnapshotArgs]] = ..., parent_volume_id: Optional[pulumi.Input[_builtins.str]] = ..., read_only: Optional[pulumi.Input[_builtins.bool]] = ..., record_size_kib: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_capacity_quota_gib: Optional[pulumi.Input[_builtins.int]] = ..., storage_capacity_reservation_gib: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_and_group_quotas: Optional[pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeUserAndGroupQuotaArgs]]]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshots")
    def copy_tags_to_snapshots(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @copy_tags_to_snapshots.setter
    def copy_tags_to_snapshots(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCompressionType")
    def data_compression_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_compression_type.setter
    def data_compression_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteVolumeOptions")
    def delete_volume_options(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_volume_options.setter
    def delete_volume_options(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsExports")
    def nfs_exports(self) -> Optional[pulumi.Input[OpenZfsVolumeNfsExportsArgs]]:
        
        ...
    
    @nfs_exports.setter
    def nfs_exports(self, value: Optional[pulumi.Input[OpenZfsVolumeNfsExportsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="originSnapshot")
    def origin_snapshot(self) -> Optional[pulumi.Input[OpenZfsVolumeOriginSnapshotArgs]]:
        
        ...
    
    @origin_snapshot.setter
    def origin_snapshot(self, value: Optional[pulumi.Input[OpenZfsVolumeOriginSnapshotArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentVolumeId")
    def parent_volume_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_volume_id.setter
    def parent_volume_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordSizeKib")
    def record_size_kib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @record_size_kib.setter
    def record_size_kib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_capacity_quota_gib.setter
    def storage_capacity_quota_gib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityReservationGib")
    def storage_capacity_reservation_gib(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @storage_capacity_reservation_gib.setter
    def storage_capacity_reservation_gib(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAndGroupQuotas")
    def user_and_group_quotas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeUserAndGroupQuotaArgs]]]]:
        
        ...
    
    @user_and_group_quotas.setter
    def user_and_group_quotas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OpenZfsVolumeUserAndGroupQuotaArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:fsx/openZfsVolume:OpenZfsVolume")
class OpenZfsVolume(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., copy_tags_to_snapshots: Optional[pulumi.Input[_builtins.bool]] = ..., data_compression_type: Optional[pulumi.Input[_builtins.str]] = ..., delete_volume_options: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nfs_exports: Optional[pulumi.Input[Union[OpenZfsVolumeNfsExportsArgs, OpenZfsVolumeNfsExportsArgsDict]]] = ..., origin_snapshot: Optional[pulumi.Input[Union[OpenZfsVolumeOriginSnapshotArgs, OpenZfsVolumeOriginSnapshotArgsDict]]] = ..., parent_volume_id: Optional[pulumi.Input[_builtins.str]] = ..., read_only: Optional[pulumi.Input[_builtins.bool]] = ..., record_size_kib: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_capacity_quota_gib: Optional[pulumi.Input[_builtins.int]] = ..., storage_capacity_reservation_gib: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_and_group_quotas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OpenZfsVolumeUserAndGroupQuotaArgs, OpenZfsVolumeUserAndGroupQuotaArgsDict]]]]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: OpenZfsVolumeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., copy_tags_to_snapshots: Optional[pulumi.Input[_builtins.bool]] = ..., data_compression_type: Optional[pulumi.Input[_builtins.str]] = ..., delete_volume_options: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nfs_exports: Optional[pulumi.Input[Union[OpenZfsVolumeNfsExportsArgs, OpenZfsVolumeNfsExportsArgsDict]]] = ..., origin_snapshot: Optional[pulumi.Input[Union[OpenZfsVolumeOriginSnapshotArgs, OpenZfsVolumeOriginSnapshotArgsDict]]] = ..., parent_volume_id: Optional[pulumi.Input[_builtins.str]] = ..., read_only: Optional[pulumi.Input[_builtins.bool]] = ..., record_size_kib: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., storage_capacity_quota_gib: Optional[pulumi.Input[_builtins.int]] = ..., storage_capacity_reservation_gib: Optional[pulumi.Input[_builtins.int]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., user_and_group_quotas: Optional[pulumi.Input[Sequence[pulumi.Input[Union[OpenZfsVolumeUserAndGroupQuotaArgs, OpenZfsVolumeUserAndGroupQuotaArgsDict]]]]] = ..., volume_type: Optional[pulumi.Input[_builtins.str]] = ...) -> OpenZfsVolume:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTagsToSnapshots")
    def copy_tags_to_snapshots(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCompressionType")
    def data_compression_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteVolumeOptions")
    def delete_volume_options(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nfsExports")
    def nfs_exports(self) -> pulumi.Output[Optional[outputs.OpenZfsVolumeNfsExports]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originSnapshot")
    def origin_snapshot(self) -> pulumi.Output[Optional[outputs.OpenZfsVolumeOriginSnapshot]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentVolumeId")
    def parent_volume_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordSizeKib")
    def record_size_kib(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityQuotaGib")
    def storage_capacity_quota_gib(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCapacityReservationGib")
    def storage_capacity_reservation_gib(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAndGroupQuotas")
    def user_and_group_quotas(self) -> pulumi.Output[Sequence[outputs.OpenZfsVolumeUserAndGroupQuota]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    


