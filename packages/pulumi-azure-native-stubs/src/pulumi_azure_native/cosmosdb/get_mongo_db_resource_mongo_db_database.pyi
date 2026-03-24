

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMongoDBResourceMongoDBDatabaseResult', 'AwaitableGetMongoDBResourceMongoDBDatabaseResult', 'get_mongo_db_resource_mongo_db_database', 'get_mongo_db_resource_mongo_db_database_output']
@pulumi.output_type
class GetMongoDBResourceMongoDBDatabaseResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., options=..., resource=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[outputs.MongoDBDatabaseGetPropertiesResponseOptions]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[outputs.MongoDBDatabaseGetPropertiesResponseResource]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetMongoDBResourceMongoDBDatabaseResult(GetMongoDBResourceMongoDBDatabaseResult):
    def __await__(self): # -> Generator[Never, Any, GetMongoDBResourceMongoDBDatabaseResult]:
        ...
    


def get_mongo_db_resource_mongo_db_database(account_name: Optional[_builtins.str] = ..., database_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMongoDBResourceMongoDBDatabaseResult:
    
    ...

def get_mongo_db_resource_mongo_db_database_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMongoDBResourceMongoDBDatabaseResult]:
    
    ...

