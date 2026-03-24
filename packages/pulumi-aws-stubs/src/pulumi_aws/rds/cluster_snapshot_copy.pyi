

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
__all__ = ['ClusterSnapshotCopyArgs', 'ClusterSnapshotCopy']
@pulumi.input_type
class ClusterSnapshotCopyArgs:
    def __init__(__self__, *, source_db_cluster_snapshot_identifier: pulumi.Input[_builtins.str], target_db_cluster_snapshot_identifier: pulumi.Input[_builtins.str], copy_tags: Optional[pulumi.Input[_builtins.bool]] = ..., destination_region: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., presigned_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[ClusterSnapshotCopyTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDbClusterSnapshotIdentifier")
    def source_db_cluster_snapshot_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_db_cluster_snapshot_identifier.setter
    def source_db_cluster_snapshot_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDbClusterSnapshotIdentifier")
    def target_db_cluster_snapshot_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_db_cluster_snapshot_identifier.setter
    def target_db_cluster_snapshot_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @copy_tags.setter
    def copy_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_region.setter
    def destination_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="presignedUrl")
    def presigned_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @presigned_url.setter
    def presigned_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedAccounts")
    def shared_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @shared_accounts.setter
    def shared_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ClusterSnapshotCopyTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ClusterSnapshotCopyTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterSnapshotCopyState:
    def __init__(__self__, *, allocated_storage: Optional[pulumi.Input[_builtins.int]] = ..., copy_tags: Optional[pulumi.Input[_builtins.bool]] = ..., db_cluster_snapshot_arn: Optional[pulumi.Input[_builtins.str]] = ..., destination_region: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., presigned_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_type: Optional[pulumi.Input[_builtins.str]] = ..., source_db_cluster_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_db_cluster_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[ClusterSnapshotCopyTimeoutsArgs]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @allocated_storage.setter
    def allocated_storage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @copy_tags.setter
    def copy_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterSnapshotArn")
    def db_cluster_snapshot_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_cluster_snapshot_arn.setter
    def db_cluster_snapshot_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_region.setter
    def destination_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @license_model.setter
    def license_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="presignedUrl")
    def presigned_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @presigned_url.setter
    def presigned_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedAccounts")
    def shared_accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @shared_accounts.setter
    def shared_accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @snapshot_type.setter
    def snapshot_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDbClusterSnapshotIdentifier")
    def source_db_cluster_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_db_cluster_snapshot_identifier.setter
    def source_db_cluster_snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @storage_encrypted.setter
    def storage_encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="targetDbClusterSnapshotIdentifier")
    def target_db_cluster_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_db_cluster_snapshot_identifier.setter
    def target_db_cluster_snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ClusterSnapshotCopyTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[ClusterSnapshotCopyTimeoutsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:rds/clusterSnapshotCopy:ClusterSnapshotCopy")
class ClusterSnapshotCopy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., copy_tags: Optional[pulumi.Input[_builtins.bool]] = ..., destination_region: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., presigned_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., source_db_cluster_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_db_cluster_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ClusterSnapshotCopyTimeoutsArgs, ClusterSnapshotCopyTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterSnapshotCopyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allocated_storage: Optional[pulumi.Input[_builtins.int]] = ..., copy_tags: Optional[pulumi.Input[_builtins.bool]] = ..., db_cluster_snapshot_arn: Optional[pulumi.Input[_builtins.str]] = ..., destination_region: Optional[pulumi.Input[_builtins.str]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., presigned_url: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_type: Optional[pulumi.Input[_builtins.str]] = ..., source_db_cluster_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., storage_encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_db_cluster_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[ClusterSnapshotCopyTimeoutsArgs, ClusterSnapshotCopyTimeoutsArgsDict]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> ClusterSnapshotCopy:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyTags")
    def copy_tags(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbClusterSnapshotArn")
    def db_cluster_snapshot_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationRegion")
    def destination_region(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="presignedUrl")
    def presigned_url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharedAccounts")
    def shared_accounts(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDbClusterSnapshotIdentifier")
    def source_db_cluster_snapshot_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageEncrypted")
    def storage_encrypted(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="targetDbClusterSnapshotIdentifier")
    def target_db_cluster_snapshot_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.ClusterSnapshotCopyTimeouts]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


