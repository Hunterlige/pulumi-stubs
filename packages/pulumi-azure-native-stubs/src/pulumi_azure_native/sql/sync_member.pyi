

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SyncMemberArgs', 'SyncMember']
@pulumi.input_type
class SyncMemberArgs:
    def __init__(__self__, *, database_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], server_name: pulumi.Input[_builtins.str], sync_group_name: pulumi.Input[_builtins.str], database_type: Optional[pulumi.Input[Union[_builtins.str, SyncMemberDbType]]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., sql_server_database_id: Optional[pulumi.Input[_builtins.str]] = ..., sync_agent_id: Optional[pulumi.Input[_builtins.str]] = ..., sync_direction: Optional[pulumi.Input[Union[_builtins.str, SyncDirection]]] = ..., sync_member_azure_database_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., sync_member_name: Optional[pulumi.Input[_builtins.str]] = ..., use_private_link_connection: Optional[pulumi.Input[_builtins.bool]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database_name.setter
    def database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server_name.setter
    def server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncGroupName")
    def sync_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sync_group_name.setter
    def sync_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[pulumi.Input[Union[_builtins.str, SyncMemberDbType]]]:
        
        ...
    
    @database_type.setter
    def database_type(self, value: Optional[pulumi.Input[Union[_builtins.str, SyncMemberDbType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerDatabaseId")
    def sql_server_database_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_server_database_id.setter
    def sql_server_database_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncAgentId")
    def sync_agent_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_agent_id.setter
    def sync_agent_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncDirection")
    def sync_direction(self) -> Optional[pulumi.Input[Union[_builtins.str, SyncDirection]]]:
        
        ...
    
    @sync_direction.setter
    def sync_direction(self, value: Optional[pulumi.Input[Union[_builtins.str, SyncDirection]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncMemberAzureDatabaseResourceId")
    def sync_member_azure_database_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_member_azure_database_resource_id.setter
    def sync_member_azure_database_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncMemberName")
    def sync_member_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sync_member_name.setter
    def sync_member_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePrivateLinkConnection")
    def use_private_link_connection(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_private_link_connection.setter
    def use_private_link_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:sql:SyncMember")
class SyncMember(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., database_name: Optional[pulumi.Input[_builtins.str]] = ..., database_type: Optional[pulumi.Input[Union[_builtins.str, SyncMemberDbType]]] = ..., password: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., sql_server_database_id: Optional[pulumi.Input[_builtins.str]] = ..., sync_agent_id: Optional[pulumi.Input[_builtins.str]] = ..., sync_direction: Optional[pulumi.Input[Union[_builtins.str, SyncDirection]]] = ..., sync_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sync_member_azure_database_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., sync_member_name: Optional[pulumi.Input[_builtins.str]] = ..., use_private_link_connection: Optional[pulumi.Input[_builtins.bool]] = ..., user_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SyncMemberArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> SyncMember:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlServerDatabaseId")
    def sql_server_database_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncAgentId")
    def sync_agent_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncDirection")
    def sync_direction(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncMemberAzureDatabaseResourceId")
    def sync_member_azure_database_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="syncState")
    def sync_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usePrivateLinkConnection")
    def use_private_link_connection(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


