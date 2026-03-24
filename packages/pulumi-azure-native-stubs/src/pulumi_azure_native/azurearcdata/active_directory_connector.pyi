

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
__all__ = ['ActiveDirectoryConnectorArgs', 'ActiveDirectoryConnector']
@pulumi.input_type
class ActiveDirectoryConnectorArgs:
    def __init__(__self__, *, data_controller_name: pulumi.Input[_builtins.str], properties: pulumi.Input[ActiveDirectoryConnectorPropertiesArgs], resource_group_name: pulumi.Input[_builtins.str], active_directory_connector_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataControllerName")
    def data_controller_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_controller_name.setter
    def data_controller_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[ActiveDirectoryConnectorPropertiesArgs]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[ActiveDirectoryConnectorPropertiesArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryConnectorName")
    def active_directory_connector_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @active_directory_connector_name.setter
    def active_directory_connector_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:azurearcdata:ActiveDirectoryConnector")
class ActiveDirectoryConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., active_directory_connector_name: Optional[pulumi.Input[_builtins.str]] = ..., data_controller_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[ActiveDirectoryConnectorPropertiesArgs, ActiveDirectoryConnectorPropertiesArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ActiveDirectoryConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ActiveDirectoryConnector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.ActiveDirectoryConnectorPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


