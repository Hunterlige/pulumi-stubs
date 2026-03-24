

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ManagedDatabaseArgs', 'ManagedDatabase']
@pulumi.input_type
class ManagedDatabaseArgs:
    def __init__(__self__, *, managed_instance_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], auto_complete_restore: Optional[pulumi.Input[_builtins.bool]] = ..., catalog_collation: Optional[pulumi.Input[Union[_builtins.str, CatalogCollationType]]] = ..., collation: Optional[pulumi.Input[_builtins.str]] = ..., create_mode: Optional[pulumi.Input[Union[_builtins.str, ManagedDatabaseCreateMode]]] = ..., cross_subscription_restorable_dropped_database_id: Optional[pulumi.Input[_builtins.str]] = ..., cross_subscription_source_database_id: Optional[pulumi.Input[_builtins.str]] = ..., cross_subscription_target_managed_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., is_ledger_on: Optional[pulumi.Input[_builtins.bool]] = ..., last_backup_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., long_term_retention_backup_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., recoverable_database_id: Optional[pulumi.Input[_builtins.str]] = ..., restorable_dropped_database_id: Optional[pulumi.Input[_builtins.str]] = ..., restore_point_in_time: Optional[pulumi.Input[_builtins.str]] = ..., source_database_id: Optional[pulumi.Input[_builtins.str]] = ..., storage_container_identity: Optional[pulumi.Input[_builtins.str]] = ..., storage_container_sas_token: Optional[pulumi.Input[_builtins.str]] = ..., storage_container_uri: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoCompleteRestore")
    def auto_complete_restore(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @auto_complete_restore.setter
    def auto_complete_restore(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogCollation")
    def catalog_collation(self) -> Optional[pulumi.Input[Union[_builtins.str, CatalogCollationType]]]:
        
        ...
    
    @catalog_collation.setter
    def catalog_collation(self, value: Optional[pulumi.Input[Union[_builtins.str, CatalogCollationType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collation.setter
    def collation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[_builtins.str, ManagedDatabaseCreateMode]]]:
        
        ...
    
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[_builtins.str, ManagedDatabaseCreateMode]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSubscriptionRestorableDroppedDatabaseId")
    def cross_subscription_restorable_dropped_database_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cross_subscription_restorable_dropped_database_id.setter
    def cross_subscription_restorable_dropped_database_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSubscriptionSourceDatabaseId")
    def cross_subscription_source_database_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cross_subscription_source_database_id.setter
    def cross_subscription_source_database_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="crossSubscriptionTargetManagedInstanceId")
    def cross_subscription_target_managed_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cross_subscription_target_managed_instance_id.setter
    def cross_subscription_target_managed_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLedgerOn")
    def is_ledger_on(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_ledger_on.setter
    def is_ledger_on(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastBackupName")
    def last_backup_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_backup_name.setter
    def last_backup_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="longTermRetentionBackupResourceId")
    def long_term_retention_backup_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @long_term_retention_backup_resource_id.setter
    def long_term_retention_backup_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoverableDatabaseId")
    def recoverable_database_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recoverable_database_id.setter
    def recoverable_database_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorableDroppedDatabaseId")
    def restorable_dropped_database_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restorable_dropped_database_id.setter
    def restorable_dropped_database_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @restore_point_in_time.setter
    def restore_point_in_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDatabaseId")
    def source_database_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_database_id.setter
    def source_database_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerIdentity")
    def storage_container_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_container_identity.setter
    def storage_container_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerSasToken")
    def storage_container_sas_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_container_sas_token.setter
    def storage_container_sas_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageContainerUri")
    def storage_container_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @storage_container_uri.setter
    def storage_container_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:ManagedDatabase")
class ManagedDatabase(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., auto_complete_restore: Optional[pulumi.Input[_builtins.bool]] = ..., catalog_collation: Optional[pulumi.Input[Union[_builtins.str, CatalogCollationType]]] = ..., collation: Optional[pulumi.Input[_builtins.str]] = ..., create_mode: Optional[pulumi.Input[Union[_builtins.str, ManagedDatabaseCreateMode]]] = ..., cross_subscription_restorable_dropped_database_id: Optional[pulumi.Input[_builtins.str]] = ..., cross_subscription_source_database_id: Optional[pulumi.Input[_builtins.str]] = ..., cross_subscription_target_managed_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., is_ledger_on: Optional[pulumi.Input[_builtins.bool]] = ..., last_backup_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., long_term_retention_backup_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., recoverable_database_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., restorable_dropped_database_id: Optional[pulumi.Input[_builtins.str]] = ..., restore_point_in_time: Optional[pulumi.Input[_builtins.str]] = ..., source_database_id: Optional[pulumi.Input[_builtins.str]] = ..., storage_container_identity: Optional[pulumi.Input[_builtins.str]] = ..., storage_container_sas_token: Optional[pulumi.Input[_builtins.str]] = ..., storage_container_uri: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ManagedDatabaseArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ManagedDatabase:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="catalogCollation")
    def catalog_collation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSecondaryLocation")
    def default_secondary_location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="earliestRestorePoint")
    def earliest_restore_point(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failoverGroupId")
    def failover_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isLedgerOn")
    def is_ledger_on(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


