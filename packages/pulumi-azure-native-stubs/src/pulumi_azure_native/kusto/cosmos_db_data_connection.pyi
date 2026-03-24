

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CosmosDbDataConnectionArgs', 'CosmosDbDataConnection']
@pulumi.input_type
class CosmosDbDataConnectionArgs:
    def __init__(__self__, *, cluster_name: pulumi.Input[_builtins.str], cosmos_db_account_resource_id: pulumi.Input[_builtins.str], cosmos_db_container: pulumi.Input[_builtins.str], cosmos_db_database: pulumi.Input[_builtins.str], database_name: pulumi.Input[_builtins.str], kind: pulumi.Input[_builtins.str], managed_identity_resource_id: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], table_name: pulumi.Input[_builtins.str], data_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., mapping_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., retrieval_start_date: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cosmosDbAccountResourceId")
    def cosmos_db_account_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cosmos_db_account_resource_id.setter
    def cosmos_db_account_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cosmosDbContainer")
    def cosmos_db_container(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cosmos_db_container.setter
    def cosmos_db_container(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cosmosDbDatabase")
    def cosmos_db_database(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cosmos_db_database.setter
    def cosmos_db_database(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @managed_identity_resource_id.setter
    def managed_identity_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @table_name.setter
    def table_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataConnectionName")
    def data_connection_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_connection_name.setter
    def data_connection_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mapping_rule_name.setter
    def mapping_rule_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @retrieval_start_date.setter
    def retrieval_start_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:kusto:CosmosDbDataConnection")
class CosmosDbDataConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., cosmos_db_account_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., cosmos_db_container: Optional[pulumi.Input[_builtins.str]] = ..., cosmos_db_database: Optional[pulumi.Input[_builtins.str]] = ..., data_connection_name: Optional[pulumi.Input[_builtins.str]] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., managed_identity_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., mapping_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., retrieval_start_date: Optional[pulumi.Input[_builtins.str]] = ..., table_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CosmosDbDataConnectionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> CosmosDbDataConnection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cosmosDbAccountResourceId")
    def cosmos_db_account_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cosmosDbContainer")
    def cosmos_db_container(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cosmosDbDatabase")
    def cosmos_db_database(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityObjectId")
    def managed_identity_object_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


