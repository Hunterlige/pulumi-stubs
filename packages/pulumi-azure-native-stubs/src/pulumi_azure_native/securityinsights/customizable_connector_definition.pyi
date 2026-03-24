

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CustomizableConnectorDefinitionArgs', 'CustomizableConnectorDefinition']
@pulumi.input_type
class CustomizableConnectorDefinitionArgs:
    def __init__(__self__, *, connector_ui_config: pulumi.Input[CustomizableConnectorUiConfigArgs], kind: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], connections_config: Optional[pulumi.Input[CustomizableConnectionsConfigArgs]] = ..., created_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., data_connector_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_utc: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorUiConfig")
    def connector_ui_config(self) -> pulumi.Input[CustomizableConnectorUiConfigArgs]:
        
        ...
    
    @connector_ui_config.setter
    def connector_ui_config(self, value: pulumi.Input[CustomizableConnectorUiConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionsConfig")
    def connections_config(self) -> Optional[pulumi.Input[CustomizableConnectionsConfigArgs]]:
        
        ...
    
    @connections_config.setter
    def connections_config(self, value: Optional[pulumi.Input[CustomizableConnectionsConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_time_utc.setter
    def created_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataConnectorDefinitionName")
    def data_connector_definition_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_connector_definition_name.setter
    def data_connector_definition_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_modified_utc.setter
    def last_modified_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class CustomizableConnectorDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connections_config: Optional[pulumi.Input[Union[CustomizableConnectionsConfigArgs, CustomizableConnectionsConfigArgsDict]]] = ..., connector_ui_config: Optional[pulumi.Input[Union[CustomizableConnectorUiConfigArgs, CustomizableConnectorUiConfigArgsDict]]] = ..., created_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., data_connector_definition_name: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_utc: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CustomizableConnectorDefinitionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> CustomizableConnectorDefinition:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionsConfig")
    def connections_config(self) -> pulumi.Output[Optional[outputs.CustomizableConnectionsConfigResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorUiConfig")
    def connector_ui_config(self) -> pulumi.Output[outputs.CustomizableConnectorUiConfigResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


