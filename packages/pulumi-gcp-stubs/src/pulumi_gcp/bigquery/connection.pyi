

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectionArgs', 'Connection']
@pulumi.input_type
class ConnectionArgs:
    def __init__(__self__, *, aws: Optional[pulumi.Input[ConnectionAwsArgs]] = ..., azure: Optional[pulumi.Input[ConnectionAzureArgs]] = ..., cloud_resource: Optional[pulumi.Input[ConnectionCloudResourceArgs]] = ..., cloud_spanner: Optional[pulumi.Input[ConnectionCloudSpannerArgs]] = ..., cloud_sql: Optional[pulumi.Input[ConnectionCloudSqlArgs]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., spark: Optional[pulumi.Input[ConnectionSparkArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aws(self) -> Optional[pulumi.Input[ConnectionAwsArgs]]:
        
        ...
    
    @aws.setter
    def aws(self, value: Optional[pulumi.Input[ConnectionAwsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def azure(self) -> Optional[pulumi.Input[ConnectionAzureArgs]]:
        
        ...
    
    @azure.setter
    def azure(self, value: Optional[pulumi.Input[ConnectionAzureArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudResource")
    def cloud_resource(self) -> Optional[pulumi.Input[ConnectionCloudResourceArgs]]:
        
        ...
    
    @cloud_resource.setter
    def cloud_resource(self, value: Optional[pulumi.Input[ConnectionCloudResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSpanner")
    def cloud_spanner(self) -> Optional[pulumi.Input[ConnectionCloudSpannerArgs]]:
        
        ...
    
    @cloud_spanner.setter
    def cloud_spanner(self, value: Optional[pulumi.Input[ConnectionCloudSpannerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSql")
    def cloud_sql(self) -> Optional[pulumi.Input[ConnectionCloudSqlArgs]]:
        
        ...
    
    @cloud_sql.setter
    def cloud_sql(self, value: Optional[pulumi.Input[ConnectionCloudSqlArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def spark(self) -> Optional[pulumi.Input[ConnectionSparkArgs]]:
        
        ...
    
    @spark.setter
    def spark(self, value: Optional[pulumi.Input[ConnectionSparkArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ConnectionState:
    def __init__(__self__, *, aws: Optional[pulumi.Input[ConnectionAwsArgs]] = ..., azure: Optional[pulumi.Input[ConnectionAzureArgs]] = ..., cloud_resource: Optional[pulumi.Input[ConnectionCloudResourceArgs]] = ..., cloud_spanner: Optional[pulumi.Input[ConnectionCloudSpannerArgs]] = ..., cloud_sql: Optional[pulumi.Input[ConnectionCloudSqlArgs]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., has_credential: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., spark: Optional[pulumi.Input[ConnectionSparkArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aws(self) -> Optional[pulumi.Input[ConnectionAwsArgs]]:
        
        ...
    
    @aws.setter
    def aws(self, value: Optional[pulumi.Input[ConnectionAwsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def azure(self) -> Optional[pulumi.Input[ConnectionAzureArgs]]:
        
        ...
    
    @azure.setter
    def azure(self, value: Optional[pulumi.Input[ConnectionAzureArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudResource")
    def cloud_resource(self) -> Optional[pulumi.Input[ConnectionCloudResourceArgs]]:
        
        ...
    
    @cloud_resource.setter
    def cloud_resource(self, value: Optional[pulumi.Input[ConnectionCloudResourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSpanner")
    def cloud_spanner(self) -> Optional[pulumi.Input[ConnectionCloudSpannerArgs]]:
        
        ...
    
    @cloud_spanner.setter
    def cloud_spanner(self, value: Optional[pulumi.Input[ConnectionCloudSpannerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSql")
    def cloud_sql(self) -> Optional[pulumi.Input[ConnectionCloudSqlArgs]]:
        
        ...
    
    @cloud_sql.setter
    def cloud_sql(self, value: Optional[pulumi.Input[ConnectionCloudSqlArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_id.setter
    def connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasCredential")
    def has_credential(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @has_credential.setter
    def has_credential(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def spark(self) -> Optional[pulumi.Input[ConnectionSparkArgs]]:
        
        ...
    
    @spark.setter
    def spark(self, value: Optional[pulumi.Input[ConnectionSparkArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:bigquery/connection:Connection")
class Connection(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., aws: Optional[pulumi.Input[Union[ConnectionAwsArgs, ConnectionAwsArgsDict]]] = ..., azure: Optional[pulumi.Input[Union[ConnectionAzureArgs, ConnectionAzureArgsDict]]] = ..., cloud_resource: Optional[pulumi.Input[Union[ConnectionCloudResourceArgs, ConnectionCloudResourceArgsDict]]] = ..., cloud_spanner: Optional[pulumi.Input[Union[ConnectionCloudSpannerArgs, ConnectionCloudSpannerArgsDict]]] = ..., cloud_sql: Optional[pulumi.Input[Union[ConnectionCloudSqlArgs, ConnectionCloudSqlArgsDict]]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., spark: Optional[pulumi.Input[Union[ConnectionSparkArgs, ConnectionSparkArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ConnectionArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., aws: Optional[pulumi.Input[Union[ConnectionAwsArgs, ConnectionAwsArgsDict]]] = ..., azure: Optional[pulumi.Input[Union[ConnectionAzureArgs, ConnectionAzureArgsDict]]] = ..., cloud_resource: Optional[pulumi.Input[Union[ConnectionCloudResourceArgs, ConnectionCloudResourceArgsDict]]] = ..., cloud_spanner: Optional[pulumi.Input[Union[ConnectionCloudSpannerArgs, ConnectionCloudSpannerArgsDict]]] = ..., cloud_sql: Optional[pulumi.Input[Union[ConnectionCloudSqlArgs, ConnectionCloudSqlArgsDict]]] = ..., connection_id: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., has_credential: Optional[pulumi.Input[_builtins.bool]] = ..., kms_key_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., spark: Optional[pulumi.Input[Union[ConnectionSparkArgs, ConnectionSparkArgsDict]]] = ...) -> Connection:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def aws(self) -> pulumi.Output[Optional[outputs.ConnectionAws]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def azure(self) -> pulumi.Output[Optional[outputs.ConnectionAzure]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudResource")
    def cloud_resource(self) -> pulumi.Output[Optional[outputs.ConnectionCloudResource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSpanner")
    def cloud_spanner(self) -> pulumi.Output[Optional[outputs.ConnectionCloudSpanner]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSql")
    def cloud_sql(self) -> pulumi.Output[Optional[outputs.ConnectionCloudSql]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionId")
    def connection_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hasCredential")
    def has_credential(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def spark(self) -> pulumi.Output[Optional[outputs.ConnectionSpark]]:
        
        ...
    


