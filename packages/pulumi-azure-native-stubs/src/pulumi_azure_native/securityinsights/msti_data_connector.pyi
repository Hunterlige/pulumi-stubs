

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
__all__ = ['MSTIDataConnectorArgs', 'MSTIDataConnector']
@pulumi.input_type
class MSTIDataConnectorArgs:
    def __init__(__self__, *, data_types: pulumi.Input[MSTIDataConnectorDataTypesArgs], kind: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], tenant_id: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], data_connector_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> pulumi.Input[MSTIDataConnectorDataTypesArgs]:
        
        ...
    
    @data_types.setter
    def data_types(self, value: pulumi.Input[MSTIDataConnectorDataTypesArgs]): # -> None:
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
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataConnectorId")
    def data_connector_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_connector_id.setter
    def data_connector_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:securityinsights:MSTIDataConnector")
class MSTIDataConnector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., data_connector_id: Optional[pulumi.Input[_builtins.str]] = ..., data_types: Optional[pulumi.Input[Union[MSTIDataConnectorDataTypesArgs, MSTIDataConnectorDataTypesArgsDict]]] = ..., kind: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tenant_id: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MSTIDataConnectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> MSTIDataConnector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataTypes")
    def data_types(self) -> pulumi.Output[outputs.MSTIDataConnectorDataTypesResponse]:
        
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
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


