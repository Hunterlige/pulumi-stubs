

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProjectArgs', 'Project']
@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *, group_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str], source_platform: pulumi.Input[Union[_builtins.str, ProjectSourcePlatform]], target_platform: pulumi.Input[Union[_builtins.str, ProjectTargetPlatform]], azure_authentication_info: Optional[pulumi.Input[AzureActiveDirectoryAppArgs]] = ..., databases_info: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInfoArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., source_connection_info: Optional[pulumi.Input[Union[MiSqlConnectionInfoArgs, MongoDbConnectionInfoArgs, MySqlConnectionInfoArgs, OracleConnectionInfoArgs, PostgreSqlConnectionInfoArgs, SqlConnectionInfoArgs]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_connection_info: Optional[pulumi.Input[Union[MiSqlConnectionInfoArgs, MongoDbConnectionInfoArgs, MySqlConnectionInfoArgs, OracleConnectionInfoArgs, PostgreSqlConnectionInfoArgs, SqlConnectionInfoArgs]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_name.setter
    def group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePlatform")
    def source_platform(self) -> pulumi.Input[Union[_builtins.str, ProjectSourcePlatform]]:
        
        ...
    
    @source_platform.setter
    def source_platform(self, value: pulumi.Input[Union[_builtins.str, ProjectSourcePlatform]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPlatform")
    def target_platform(self) -> pulumi.Input[Union[_builtins.str, ProjectTargetPlatform]]:
        
        ...
    
    @target_platform.setter
    def target_platform(self, value: pulumi.Input[Union[_builtins.str, ProjectTargetPlatform]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureAuthenticationInfo")
    def azure_authentication_info(self) -> Optional[pulumi.Input[AzureActiveDirectoryAppArgs]]:
        
        ...
    
    @azure_authentication_info.setter
    def azure_authentication_info(self, value: Optional[pulumi.Input[AzureActiveDirectoryAppArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databasesInfo")
    def databases_info(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInfoArgs]]]]:
        
        ...
    
    @databases_info.setter
    def databases_info(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DatabaseInfoArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> Optional[pulumi.Input[Union[MiSqlConnectionInfoArgs, MongoDbConnectionInfoArgs, MySqlConnectionInfoArgs, OracleConnectionInfoArgs, PostgreSqlConnectionInfoArgs, SqlConnectionInfoArgs]]]:
        
        ...
    
    @source_connection_info.setter
    def source_connection_info(self, value: Optional[pulumi.Input[Union[MiSqlConnectionInfoArgs, MongoDbConnectionInfoArgs, MySqlConnectionInfoArgs, OracleConnectionInfoArgs, PostgreSqlConnectionInfoArgs, SqlConnectionInfoArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> Optional[pulumi.Input[Union[MiSqlConnectionInfoArgs, MongoDbConnectionInfoArgs, MySqlConnectionInfoArgs, OracleConnectionInfoArgs, PostgreSqlConnectionInfoArgs, SqlConnectionInfoArgs]]]:
        
        ...
    
    @target_connection_info.setter
    def target_connection_info(self, value: Optional[pulumi.Input[Union[MiSqlConnectionInfoArgs, MongoDbConnectionInfoArgs, MySqlConnectionInfoArgs, OracleConnectionInfoArgs, PostgreSqlConnectionInfoArgs, SqlConnectionInfoArgs]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:datamigration:Project")
class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., azure_authentication_info: Optional[pulumi.Input[Union[AzureActiveDirectoryAppArgs, AzureActiveDirectoryAppArgsDict]]] = ..., databases_info: Optional[pulumi.Input[Sequence[pulumi.Input[Union[DatabaseInfoArgs, DatabaseInfoArgsDict]]]]] = ..., group_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., source_connection_info: Optional[pulumi.Input[Union[Union[MiSqlConnectionInfoArgs, MiSqlConnectionInfoArgsDict], Union[MongoDbConnectionInfoArgs, MongoDbConnectionInfoArgsDict], Union[MySqlConnectionInfoArgs, MySqlConnectionInfoArgsDict], Union[OracleConnectionInfoArgs, OracleConnectionInfoArgsDict], Union[PostgreSqlConnectionInfoArgs, PostgreSqlConnectionInfoArgsDict], Union[SqlConnectionInfoArgs, SqlConnectionInfoArgsDict]]]] = ..., source_platform: Optional[pulumi.Input[Union[_builtins.str, ProjectSourcePlatform]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., target_connection_info: Optional[pulumi.Input[Union[Union[MiSqlConnectionInfoArgs, MiSqlConnectionInfoArgsDict], Union[MongoDbConnectionInfoArgs, MongoDbConnectionInfoArgsDict], Union[MySqlConnectionInfoArgs, MySqlConnectionInfoArgsDict], Union[OracleConnectionInfoArgs, OracleConnectionInfoArgsDict], Union[PostgreSqlConnectionInfoArgs, PostgreSqlConnectionInfoArgsDict], Union[SqlConnectionInfoArgs, SqlConnectionInfoArgsDict]]]] = ..., target_platform: Optional[pulumi.Input[Union[_builtins.str, ProjectTargetPlatform]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ProjectArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Project:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureAuthenticationInfo")
    def azure_authentication_info(self) -> pulumi.Output[Optional[outputs.AzureActiveDirectoryAppResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databasesInfo")
    def databases_info(self) -> pulumi.Output[Optional[Sequence[outputs.DatabaseInfoResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
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
    @pulumi.getter(name="sourceConnectionInfo")
    def source_connection_info(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePlatform")
    def source_platform(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetConnectionInfo")
    def target_connection_info(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPlatform")
    def target_platform(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        ...
    


