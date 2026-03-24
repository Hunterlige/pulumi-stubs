

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMongoDBResourceMongoRoleDefinitionResult', ..., 'get_mongo_db_resource_mongo_role_definition', 'get_mongo_db_resource_mongo_role_definition_output']
@pulumi.output_type
class GetMongoDBResourceMongoRoleDefinitionResult:
    
    def __init__(__self__, azure_api_version=..., database_name=..., id=..., name=..., privileges=..., role_name=..., roles=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def privileges(self) -> Optional[Sequence[outputs.PrivilegeResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[outputs.RoleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetMongoDBResourceMongoRoleDefinitionResult(GetMongoDBResourceMongoRoleDefinitionResult):
    def __await__(self): # -> Generator[Never, Any, GetMongoDBResourceMongoRoleDefinitionResult]:
        ...
    


def get_mongo_db_resource_mongo_role_definition(account_name: Optional[_builtins.str] = ..., mongo_role_definition_id: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMongoDBResourceMongoRoleDefinitionResult:
    
    ...

def get_mongo_db_resource_mongo_role_definition_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., mongo_role_definition_id: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMongoDBResourceMongoRoleDefinitionResult]:
    
    ...

