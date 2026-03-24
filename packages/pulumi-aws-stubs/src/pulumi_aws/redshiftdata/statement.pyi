

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
__all__ = ['StatementArgs', 'Statement']
@pulumi.input_type
class StatementArgs:
    def __init__(__self__, *, database: pulumi.Input[_builtins.str], sql: pulumi.Input[_builtins.str], cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., db_user: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[StatementParameterArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ..., statement_name: Optional[pulumi.Input[_builtins.str]] = ..., with_event: Optional[pulumi.Input[_builtins.bool]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sql(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sql.setter
    def sql(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_user.setter
    def db_user(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StatementParameterArgs]]]]:
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StatementParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementName")
    def statement_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @statement_name.setter
    def statement_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="withEvent")
    def with_event(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @with_event.setter
    def with_event(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workgroup_name.setter
    def workgroup_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _StatementState:
    def __init__(__self__, *, cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[_builtins.str]] = ..., db_user: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[StatementParameterArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ..., sql: Optional[pulumi.Input[_builtins.str]] = ..., statement_name: Optional[pulumi.Input[_builtins.str]] = ..., with_event: Optional[pulumi.Input[_builtins.bool]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_identifier.setter
    def cluster_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @database.setter
    def database(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @db_user.setter
    def db_user(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StatementParameterArgs]]]]:
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StatementParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sql(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sql.setter
    def sql(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementName")
    def statement_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @statement_name.setter
    def statement_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="withEvent")
    def with_event(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @with_event.setter
    def with_event(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workgroup_name.setter
    def workgroup_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:redshiftdata/statement:Statement")
class Statement(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[_builtins.str]] = ..., db_user: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StatementParameterArgs, StatementParameterArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ..., sql: Optional[pulumi.Input[_builtins.str]] = ..., statement_name: Optional[pulumi.Input[_builtins.str]] = ..., with_event: Optional[pulumi.Input[_builtins.bool]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: StatementArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cluster_identifier: Optional[pulumi.Input[_builtins.str]] = ..., database: Optional[pulumi.Input[_builtins.str]] = ..., db_user: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[StatementParameterArgs, StatementParameterArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., secret_arn: Optional[pulumi.Input[_builtins.str]] = ..., sql: Optional[pulumi.Input[_builtins.str]] = ..., statement_name: Optional[pulumi.Input[_builtins.str]] = ..., with_event: Optional[pulumi.Input[_builtins.bool]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...) -> Statement:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterIdentifier")
    def cluster_identifier(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence[outputs.StatementParameter]]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sql(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statementName")
    def statement_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="withEvent")
    def with_event(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


