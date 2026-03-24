

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectorArgs', 'Connector']
@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *, connector_properties: pulumi.Input[Mapping[str, Any]], connector_type: pulumi.Input[Union[_builtins.str, ConnectorTypes]], hub_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], connector_name: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., is_internal: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorProperties")
    def connector_properties(self) -> pulumi.Input[Mapping[str, Any]]:
        
        ...
    
    @connector_properties.setter
    def connector_properties(self, value: pulumi.Input[Mapping[str, Any]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Input[Union[_builtins.str, ConnectorTypes]]:
        
        ...
    
    @connector_type.setter
    def connector_type(self, value: pulumi.Input[Union[_builtins.str, ConnectorTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hub_name.setter
    def hub_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connector_name.setter
    def connector_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isInternal")
    def is_internal(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_internal.setter
    def is_internal(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:customerinsights:Connector")
class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connector_name: Optional[pulumi.Input[_builtins.str]] = ..., connector_properties: Optional[pulumi.Input[Mapping[str, Any]]] = ..., connector_type: Optional[pulumi.Input[Union[_builtins.str, ConnectorTypes]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., hub_name: Optional[pulumi.Input[_builtins.str]] = ..., is_internal: Optional[pulumi.Input[_builtins.bool]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Connector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorProperties")
    def connector_properties(self) -> pulumi.Output[Mapping[str, Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorType")
    def connector_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def created(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isInternal")
    def is_internal(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


