

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseMigrationsMongoToCosmosDbRUMongoArgs', 'DatabaseMigrationsMongoToCosmosDbRUMongo']
@pulumi.input_type
class DatabaseMigrationsMongoToCosmosDbRUMongoArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], target_resource_name: pulumi.Input[_builtins.str], collection_list: Optional[pulumi.Input[Sequence[pulumi.Input[MongoMigrationCollectionArgs]]]] = ..., migration_name: Optional[pulumi.Input[_builtins.str]] = ..., migration_operation_id: Optional[pulumi.Input[_builtins.str]] = ..., migration_service: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_error: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., source_mongo_connection: Optional[pulumi.Input[MongoConnectionInformationArgs]] = ..., target_mongo_connection: Optional[pulumi.Input[MongoConnectionInformationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetResourceName")
    def target_resource_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_resource_name.setter
    def target_resource_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionList")
    def collection_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MongoMigrationCollectionArgs]]]]:
        
        ...
    
    @collection_list.setter
    def collection_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MongoMigrationCollectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationName")
    def migration_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_name.setter
    def migration_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperationId")
    def migration_operation_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_operation_id.setter
    def migration_operation_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationService")
    def migration_service(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @migration_service.setter
    def migration_service(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @provisioning_error.setter
    def provisioning_error(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceMongoConnection")
    def source_mongo_connection(self) -> Optional[pulumi.Input[MongoConnectionInformationArgs]]:
        
        ...
    
    @source_mongo_connection.setter
    def source_mongo_connection(self, value: Optional[pulumi.Input[MongoConnectionInformationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMongoConnection")
    def target_mongo_connection(self) -> Optional[pulumi.Input[MongoConnectionInformationArgs]]:
        
        ...
    
    @target_mongo_connection.setter
    def target_mongo_connection(self, value: Optional[pulumi.Input[MongoConnectionInformationArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class DatabaseMigrationsMongoToCosmosDbRUMongo(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., collection_list: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MongoMigrationCollectionArgs, MongoMigrationCollectionArgsDict]]]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., migration_name: Optional[pulumi.Input[_builtins.str]] = ..., migration_operation_id: Optional[pulumi.Input[_builtins.str]] = ..., migration_service: Optional[pulumi.Input[_builtins.str]] = ..., provisioning_error: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., source_mongo_connection: Optional[pulumi.Input[Union[MongoConnectionInformationArgs, MongoConnectionInformationArgsDict]]] = ..., target_mongo_connection: Optional[pulumi.Input[Union[MongoConnectionInformationArgs, MongoConnectionInformationArgsDict]]] = ..., target_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DatabaseMigrationsMongoToCosmosDbRUMongoArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DatabaseMigrationsMongoToCosmosDbRUMongo:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionList")
    def collection_list(self) -> pulumi.Output[Optional[Sequence[outputs.MongoMigrationCollectionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationFailureError")
    def migration_failure_error(self) -> pulumi.Output[outputs.ErrorInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperationId")
    def migration_operation_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationService")
    def migration_service(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatus")
    def migration_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceMongoConnection")
    def source_mongo_connection(self) -> pulumi.Output[Optional[outputs.MongoConnectionInformationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMongoConnection")
    def target_mongo_connection(self) -> pulumi.Output[Optional[outputs.MongoConnectionInformationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


