

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatabaseMigrationsSqlMiArgs', 'DatabaseMigrationsSqlMi']
@pulumi.input_type
class DatabaseMigrationsSqlMiArgs:
    def __init__(__self__, *, managed_instance_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], properties: Optional[pulumi.Input[DatabaseMigrationPropertiesSqlMiArgs]] = ..., target_db_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[DatabaseMigrationPropertiesSqlMiArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[DatabaseMigrationPropertiesSqlMiArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetDbName")
    def target_db_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_db_name.setter
    def target_db_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:datamigration:DatabaseMigrationsSqlMi")
class DatabaseMigrationsSqlMi(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., managed_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[DatabaseMigrationPropertiesSqlMiArgs, DatabaseMigrationPropertiesSqlMiArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., target_db_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: DatabaseMigrationsSqlMiArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> DatabaseMigrationsSqlMi:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.DatabaseMigrationPropertiesSqlMiResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


