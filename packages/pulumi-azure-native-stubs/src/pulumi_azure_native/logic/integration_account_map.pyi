

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IntegrationAccountMapArgs', 'IntegrationAccountMap']
@pulumi.input_type
class IntegrationAccountMapArgs:
    def __init__(__self__, *, integration_account_name: pulumi.Input[_builtins.str], map_type: pulumi.Input[Union[_builtins.str, MapType]], resource_group_name: pulumi.Input[_builtins.str], content: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., map_name: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[Any] = ..., parameters_schema: Optional[pulumi.Input[IntegrationAccountMapPropertiesParametersSchemaArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapType")
    def map_type(self) -> pulumi.Input[Union[_builtins.str, MapType]]:
        
        ...
    
    @map_type.setter
    def map_type(self, value: pulumi.Input[Union[_builtins.str, MapType]]): # -> None:
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
    def content(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content.setter
    def content(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapName")
    def map_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @map_name.setter
    def map_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parametersSchema")
    def parameters_schema(self) -> Optional[pulumi.Input[IntegrationAccountMapPropertiesParametersSchemaArgs]]:
        
        ...
    
    @parameters_schema.setter
    def parameters_schema(self, value: Optional[pulumi.Input[IntegrationAccountMapPropertiesParametersSchemaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:logic:IntegrationAccountMap")
class IntegrationAccountMap(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., content: Optional[pulumi.Input[_builtins.str]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., map_name: Optional[pulumi.Input[_builtins.str]] = ..., map_type: Optional[pulumi.Input[Union[_builtins.str, MapType]]] = ..., metadata: Optional[Any] = ..., parameters_schema: Optional[pulumi.Input[Union[IntegrationAccountMapPropertiesParametersSchemaArgs, IntegrationAccountMapPropertiesParametersSchemaArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IntegrationAccountMapArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> IntegrationAccountMap:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> pulumi.Output[outputs.ContentLinkResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapType")
    def map_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parametersSchema")
    def parameters_schema(self) -> pulumi.Output[Optional[outputs.IntegrationAccountMapPropertiesResponseParametersSchema]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


