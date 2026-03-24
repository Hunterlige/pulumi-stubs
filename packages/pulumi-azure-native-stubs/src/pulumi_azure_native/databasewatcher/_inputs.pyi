

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DatastoreArgs', 'DatastoreArgsDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'SqlDbElasticPoolTargetPropertiesArgs', 'SqlDbElasticPoolTargetPropertiesArgsDict', 'SqlDbSingleDatabaseTargetPropertiesArgs', 'SqlDbSingleDatabaseTargetPropertiesArgsDict', 'SqlMiTargetPropertiesArgs', 'SqlMiTargetPropertiesArgsDict', 'SqlVmTargetPropertiesArgs', 'SqlVmTargetPropertiesArgsDict', 'VaultSecretArgs', 'VaultSecretArgsDict']
class DatastoreArgsDict(TypedDict):
    
    kusto_cluster_uri: pulumi.Input[_builtins.str]
    kusto_data_ingestion_uri: pulumi.Input[_builtins.str]
    kusto_database_name: pulumi.Input[_builtins.str]
    kusto_management_url: pulumi.Input[_builtins.str]
    kusto_offering_type: pulumi.Input[Union[_builtins.str, KustoOfferingType]]
    adx_cluster_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    kusto_cluster_display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class DatastoreArgs:
    def __init__(__self__, *, kusto_cluster_uri: pulumi.Input[_builtins.str], kusto_data_ingestion_uri: pulumi.Input[_builtins.str], kusto_database_name: pulumi.Input[_builtins.str], kusto_management_url: pulumi.Input[_builtins.str], kusto_offering_type: pulumi.Input[Union[_builtins.str, KustoOfferingType]], adx_cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., kusto_cluster_display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoClusterUri")
    def kusto_cluster_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kusto_cluster_uri.setter
    def kusto_cluster_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoDataIngestionUri")
    def kusto_data_ingestion_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kusto_data_ingestion_uri.setter
    def kusto_data_ingestion_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoDatabaseName")
    def kusto_database_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kusto_database_name.setter
    def kusto_database_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoManagementUrl")
    def kusto_management_url(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kusto_management_url.setter
    def kusto_management_url(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoOfferingType")
    def kusto_offering_type(self) -> pulumi.Input[Union[_builtins.str, KustoOfferingType]]:
        
        ...
    
    @kusto_offering_type.setter
    def kusto_offering_type(self, value: pulumi.Input[Union[_builtins.str, KustoOfferingType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adxClusterResourceId")
    def adx_cluster_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @adx_cluster_resource_id.setter
    def adx_cluster_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kustoClusterDisplayName")
    def kusto_cluster_display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kusto_cluster_display_name.setter
    def kusto_cluster_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class SqlDbElasticPoolTargetPropertiesArgsDict(TypedDict):
    
    anchor_database_resource_id: pulumi.Input[_builtins.str]
    connection_server_name: pulumi.Input[_builtins.str]
    sql_ep_resource_id: pulumi.Input[_builtins.str]
    target_authentication_type: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]
    target_type: pulumi.Input[_builtins.str]
    read_intent: NotRequired[pulumi.Input[_builtins.bool]]
    target_vault: NotRequired[pulumi.Input[VaultSecretArgsDict]]


@pulumi.input_type
class SqlDbElasticPoolTargetPropertiesArgs:
    def __init__(__self__, *, anchor_database_resource_id: pulumi.Input[_builtins.str], connection_server_name: pulumi.Input[_builtins.str], sql_ep_resource_id: pulumi.Input[_builtins.str], target_authentication_type: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]], target_type: pulumi.Input[_builtins.str], read_intent: Optional[pulumi.Input[_builtins.bool]] = ..., target_vault: Optional[pulumi.Input[VaultSecretArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anchorDatabaseResourceId")
    def anchor_database_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @anchor_database_resource_id.setter
    def anchor_database_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionServerName")
    def connection_server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_server_name.setter
    def connection_server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlEpResourceId")
    def sql_ep_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_ep_resource_id.setter
    def sql_ep_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAuthenticationType")
    def target_authentication_type(self) -> pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]:
        
        ...
    
    @target_authentication_type.setter
    def target_authentication_type(self, value: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_type.setter
    def target_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readIntent")
    def read_intent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read_intent.setter
    def read_intent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVault")
    def target_vault(self) -> Optional[pulumi.Input[VaultSecretArgs]]:
        
        ...
    
    @target_vault.setter
    def target_vault(self, value: Optional[pulumi.Input[VaultSecretArgs]]): # -> None:
        ...
    


class SqlDbSingleDatabaseTargetPropertiesArgsDict(TypedDict):
    
    connection_server_name: pulumi.Input[_builtins.str]
    sql_db_resource_id: pulumi.Input[_builtins.str]
    target_authentication_type: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]
    target_type: pulumi.Input[_builtins.str]
    read_intent: NotRequired[pulumi.Input[_builtins.bool]]
    target_vault: NotRequired[pulumi.Input[VaultSecretArgsDict]]


@pulumi.input_type
class SqlDbSingleDatabaseTargetPropertiesArgs:
    def __init__(__self__, *, connection_server_name: pulumi.Input[_builtins.str], sql_db_resource_id: pulumi.Input[_builtins.str], target_authentication_type: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]], target_type: pulumi.Input[_builtins.str], read_intent: Optional[pulumi.Input[_builtins.bool]] = ..., target_vault: Optional[pulumi.Input[VaultSecretArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionServerName")
    def connection_server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_server_name.setter
    def connection_server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlDbResourceId")
    def sql_db_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_db_resource_id.setter
    def sql_db_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAuthenticationType")
    def target_authentication_type(self) -> pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]:
        
        ...
    
    @target_authentication_type.setter
    def target_authentication_type(self, value: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_type.setter
    def target_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readIntent")
    def read_intent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read_intent.setter
    def read_intent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVault")
    def target_vault(self) -> Optional[pulumi.Input[VaultSecretArgs]]:
        
        ...
    
    @target_vault.setter
    def target_vault(self, value: Optional[pulumi.Input[VaultSecretArgs]]): # -> None:
        ...
    


class SqlMiTargetPropertiesArgsDict(TypedDict):
    
    connection_server_name: pulumi.Input[_builtins.str]
    sql_mi_resource_id: pulumi.Input[_builtins.str]
    target_authentication_type: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]
    target_type: pulumi.Input[_builtins.str]
    connection_tcp_port: NotRequired[pulumi.Input[_builtins.int]]
    read_intent: NotRequired[pulumi.Input[_builtins.bool]]
    target_vault: NotRequired[pulumi.Input[VaultSecretArgsDict]]


@pulumi.input_type
class SqlMiTargetPropertiesArgs:
    def __init__(__self__, *, connection_server_name: pulumi.Input[_builtins.str], sql_mi_resource_id: pulumi.Input[_builtins.str], target_authentication_type: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]], target_type: pulumi.Input[_builtins.str], connection_tcp_port: Optional[pulumi.Input[_builtins.int]] = ..., read_intent: Optional[pulumi.Input[_builtins.bool]] = ..., target_vault: Optional[pulumi.Input[VaultSecretArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionServerName")
    def connection_server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_server_name.setter
    def connection_server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlMiResourceId")
    def sql_mi_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_mi_resource_id.setter
    def sql_mi_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAuthenticationType")
    def target_authentication_type(self) -> pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]:
        
        ...
    
    @target_authentication_type.setter
    def target_authentication_type(self, value: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_type.setter
    def target_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTcpPort")
    def connection_tcp_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_tcp_port.setter
    def connection_tcp_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readIntent")
    def read_intent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read_intent.setter
    def read_intent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVault")
    def target_vault(self) -> Optional[pulumi.Input[VaultSecretArgs]]:
        
        ...
    
    @target_vault.setter
    def target_vault(self, value: Optional[pulumi.Input[VaultSecretArgs]]): # -> None:
        ...
    


class SqlVmTargetPropertiesArgsDict(TypedDict):
    
    connection_server_name: pulumi.Input[_builtins.str]
    sql_vm_resource_id: pulumi.Input[_builtins.str]
    target_authentication_type: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]
    target_type: pulumi.Input[_builtins.str]
    connection_tcp_port: NotRequired[pulumi.Input[_builtins.int]]
    sql_named_instance_name: NotRequired[pulumi.Input[_builtins.str]]
    target_vault: NotRequired[pulumi.Input[VaultSecretArgsDict]]


@pulumi.input_type
class SqlVmTargetPropertiesArgs:
    def __init__(__self__, *, connection_server_name: pulumi.Input[_builtins.str], sql_vm_resource_id: pulumi.Input[_builtins.str], target_authentication_type: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]], target_type: pulumi.Input[_builtins.str], connection_tcp_port: Optional[pulumi.Input[_builtins.int]] = ..., sql_named_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., target_vault: Optional[pulumi.Input[VaultSecretArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionServerName")
    def connection_server_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_server_name.setter
    def connection_server_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlVmResourceId")
    def sql_vm_resource_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql_vm_resource_id.setter
    def sql_vm_resource_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAuthenticationType")
    def target_authentication_type(self) -> pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]:
        
        ...
    
    @target_authentication_type.setter
    def target_authentication_type(self, value: pulumi.Input[Union[_builtins.str, TargetAuthenticationType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_type.setter
    def target_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTcpPort")
    def connection_tcp_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @connection_tcp_port.setter
    def connection_tcp_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlNamedInstanceName")
    def sql_named_instance_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql_named_instance_name.setter
    def sql_named_instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetVault")
    def target_vault(self) -> Optional[pulumi.Input[VaultSecretArgs]]:
        
        ...
    
    @target_vault.setter
    def target_vault(self, value: Optional[pulumi.Input[VaultSecretArgs]]): # -> None:
        ...
    


class VaultSecretArgsDict(TypedDict):
    
    akv_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    akv_target_password: NotRequired[pulumi.Input[_builtins.str]]
    akv_target_user: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VaultSecretArgs:
    def __init__(__self__, *, akv_resource_id: Optional[pulumi.Input[_builtins.str]] = ..., akv_target_password: Optional[pulumi.Input[_builtins.str]] = ..., akv_target_user: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="akvResourceId")
    def akv_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @akv_resource_id.setter
    def akv_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="akvTargetPassword")
    def akv_target_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @akv_target_password.setter
    def akv_target_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="akvTargetUser")
    def akv_target_user(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @akv_target_user.setter
    def akv_target_user(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


