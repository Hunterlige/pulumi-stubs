

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
__all__ = ['ConnectorArgs', 'Connector']
@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *, connector_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[ConnectorPropertiesArgs]] = ...) -> None:
        
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
    def properties(self) -> Optional[pulumi.Input[ConnectorPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[ConnectorPropertiesArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:impact:Connector")
class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connector_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[ConnectorPropertiesArgs, ConnectorPropertiesArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ConnectorArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
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
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.ConnectorPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


