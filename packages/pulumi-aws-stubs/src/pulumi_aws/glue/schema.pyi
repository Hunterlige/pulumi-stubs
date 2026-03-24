

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SchemaArgs', 'Schema']
@pulumi.input_type
class SchemaArgs:
    def __init__(__self__, *, compatibility: pulumi.Input[_builtins.str], data_format: pulumi.Input[_builtins.str], schema_definition: pulumi.Input[_builtins.str], schema_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., registry_arn: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compatibility(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @compatibility.setter
    def compatibility(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_format.setter
    def data_format(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schema_definition.setter
    def schema_definition(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schema_name.setter
    def schema_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryArn")
    def registry_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registry_arn.setter
    def registry_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _SchemaState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., compatibility: Optional[pulumi.Input[_builtins.str]] = ..., data_format: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., latest_schema_version: Optional[pulumi.Input[_builtins.int]] = ..., next_schema_version: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., registry_arn: Optional[pulumi.Input[_builtins.str]] = ..., registry_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_checkpoint: Optional[pulumi.Input[_builtins.int]] = ..., schema_definition: Optional[pulumi.Input[_builtins.str]] = ..., schema_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def compatibility(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compatibility.setter
    def compatibility(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_format.setter
    def data_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestSchemaVersion")
    def latest_schema_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @latest_schema_version.setter
    def latest_schema_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextSchemaVersion")
    def next_schema_version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @next_schema_version.setter
    def next_schema_version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryArn")
    def registry_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registry_arn.setter
    def registry_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @registry_name.setter
    def registry_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaCheckpoint")
    def schema_checkpoint(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @schema_checkpoint.setter
    def schema_checkpoint(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema_definition.setter
    def schema_definition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:glue/schema:Schema")
class Schema(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., compatibility: Optional[pulumi.Input[_builtins.str]] = ..., data_format: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., registry_arn: Optional[pulumi.Input[_builtins.str]] = ..., schema_definition: Optional[pulumi.Input[_builtins.str]] = ..., schema_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: SchemaArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., compatibility: Optional[pulumi.Input[_builtins.str]] = ..., data_format: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., latest_schema_version: Optional[pulumi.Input[_builtins.int]] = ..., next_schema_version: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., registry_arn: Optional[pulumi.Input[_builtins.str]] = ..., registry_name: Optional[pulumi.Input[_builtins.str]] = ..., schema_checkpoint: Optional[pulumi.Input[_builtins.int]] = ..., schema_definition: Optional[pulumi.Input[_builtins.str]] = ..., schema_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Schema:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compatibility(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="latestSchemaVersion")
    def latest_schema_version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextSchemaVersion")
    def next_schema_version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryArn")
    def registry_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaCheckpoint")
    def schema_checkpoint(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaDefinition")
    def schema_definition(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


