

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectionTypeArgs', 'ConnectionType']
@pulumi.input_type
class ConnectionTypeArgs:
    def __init__(__self__, *, automation_account_name: pulumi.Input[_builtins.str], field_definitions: pulumi.Input[Mapping[str, pulumi.Input[FieldDefinitionArgs]]], name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], connection_type_name: Optional[pulumi.Input[_builtins.str]] = ..., is_global: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldDefinitions")
    def field_definitions(self) -> pulumi.Input[Mapping[str, pulumi.Input[FieldDefinitionArgs]]]:
        
        ...
    
    @field_definitions.setter
    def field_definitions(self, value: pulumi.Input[Mapping[str, pulumi.Input[FieldDefinitionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTypeName")
    def connection_type_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_type_name.setter
    def connection_type_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_global.setter
    def is_global(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:automation:ConnectionType")
class ConnectionType(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., automation_account_name: Optional[pulumi.Input[_builtins.str]] = ..., connection_type_name: Optional[pulumi.Input[_builtins.str]] = ..., field_definitions: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union[FieldDefinitionArgs, FieldDefinitionArgsDict]]]]] = ..., is_global: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectionTypeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ConnectionType:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldDefinitions")
    def field_definitions(self) -> pulumi.Output[Mapping[str, outputs.FieldDefinitionResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


