

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SnapshotArgs', 'Snapshot']
@pulumi.input_type
class SnapshotArgs:
    def __init__(__self__, *, db_instance_identifier: pulumi.Input[_builtins.str], db_snapshot_identifier: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ..., shared_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @db_instance_identifier.setter
    def db_instance_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSnapshotIdentifier")
    def db_snapshot_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @db_snapshot_identifier.setter
    def db_snapshot_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    


@pulumi.input_type
class _SnapshotState:
    def __init__(__self__, *, allocated_storage: Optional[pulumi.Input[_builtins.int]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., db_instance_identifier: Optional[pulumi.Input[_builtins.str]] = ..., db_snapshot_arn: Optional[pulumi.Input[_builtins.str]] = ..., db_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., option_group_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_type: Optional[pulumi.Input[_builtins.str]] = ..., source_db_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., source_region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @allocated_storage.setter
    def allocated_storage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_instance_identifier.setter
    def db_instance_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSnapshotArn")
    def db_snapshot_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_snapshot_arn.setter
    def db_snapshot_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSnapshotIdentifier")
    def db_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_snapshot_identifier.setter
    def db_snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
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
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @iops.setter
    def iops(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @option_group_name.setter
    def option_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    @pulumi.getter(name="sourceDbSnapshotIdentifier")
    def source_db_snapshot_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_db_snapshot_identifier.setter
    def source_db_snapshot_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_region.setter
    def source_region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:rds/snapshot:Snapshot")
class Snapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., db_instance_identifier: Optional[pulumi.Input[_builtins.str]] = ..., db_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SnapshotArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allocated_storage: Optional[pulumi.Input[_builtins.int]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., db_instance_identifier: Optional[pulumi.Input[_builtins.str]] = ..., db_snapshot_arn: Optional[pulumi.Input[_builtins.str]] = ..., db_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., encrypted: Optional[pulumi.Input[_builtins.bool]] = ..., engine: Optional[pulumi.Input[_builtins.str]] = ..., engine_version: Optional[pulumi.Input[_builtins.str]] = ..., iops: Optional[pulumi.Input[_builtins.int]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., license_model: Optional[pulumi.Input[_builtins.str]] = ..., option_group_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., shared_accounts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., snapshot_type: Optional[pulumi.Input[_builtins.str]] = ..., source_db_snapshot_identifier: Optional[pulumi.Input[_builtins.str]] = ..., source_region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., storage_type: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Snapshot:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbInstanceIdentifier")
    def db_instance_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSnapshotArn")
    def db_snapshot_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbSnapshotIdentifier")
    def db_snapshot_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[_builtins.bool]:
        
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
    @pulumi.getter
    def iops(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]:
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
    @pulumi.getter(name="sourceDbSnapshotIdentifier")
    def source_db_snapshot_identifier(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRegion")
    def source_region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


