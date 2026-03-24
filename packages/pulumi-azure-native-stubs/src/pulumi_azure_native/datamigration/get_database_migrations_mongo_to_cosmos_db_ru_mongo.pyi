

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDatabaseMigrationsMongoToCosmosDbRUMongoResult', ..., ..., ...]
@pulumi.output_type
class GetDatabaseMigrationsMongoToCosmosDbRUMongoResult:
    
    def __init__(__self__, azure_api_version=..., collection_list=..., ended_on=..., id=..., kind=..., migration_failure_error=..., migration_operation_id=..., migration_service=..., migration_status=..., name=..., provisioning_error=..., provisioning_state=..., scope=..., source_mongo_connection=..., started_on=..., system_data=..., target_mongo_connection=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionList")
    def collection_list(self) -> Optional[Sequence[outputs.MongoMigrationCollectionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endedOn")
    def ended_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationFailureError")
    def migration_failure_error(self) -> outputs.ErrorInfoResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationOperationId")
    def migration_operation_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationService")
    def migration_service(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationStatus")
    def migration_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceMongoConnection")
    def source_mongo_connection(self) -> Optional[outputs.MongoConnectionInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startedOn")
    def started_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetMongoConnection")
    def target_mongo_connection(self) -> Optional[outputs.MongoConnectionInformationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDatabaseMigrationsMongoToCosmosDbRUMongoResult(GetDatabaseMigrationsMongoToCosmosDbRUMongoResult):
    def __await__(self): # -> Generator[Never, Any, GetDatabaseMigrationsMongoToCosmosDbRUMongoResult]:
        ...
    


def get_database_migrations_mongo_to_cosmos_db_ru_mongo(migration_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., target_resource_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDatabaseMigrationsMongoToCosmosDbRUMongoResult:
    
    ...

def get_database_migrations_mongo_to_cosmos_db_ru_mongo_output(migration_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., target_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDatabaseMigrationsMongoToCosmosDbRUMongoResult]:
    
    ...

