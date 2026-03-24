

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ServiceArgs', 'Service']
@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], properties: Optional[pulumi.Input[Union[DataTransferServiceResourceCreateUpdatePropertiesArgs, GraphAPIComputeServiceResourceCreateUpdatePropertiesArgs, MaterializedViewsBuilderServiceResourceCreateUpdatePropertiesArgs, SqlDedicatedGatewayServiceResourceCreateUpdatePropertiesArgs]]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def properties(self) -> Optional[pulumi.Input[Union[DataTransferServiceResourceCreateUpdatePropertiesArgs, GraphAPIComputeServiceResourceCreateUpdatePropertiesArgs, MaterializedViewsBuilderServiceResourceCreateUpdatePropertiesArgs, SqlDedicatedGatewayServiceResourceCreateUpdatePropertiesArgs]]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Union[DataTransferServiceResourceCreateUpdatePropertiesArgs, GraphAPIComputeServiceResourceCreateUpdatePropertiesArgs, MaterializedViewsBuilderServiceResourceCreateUpdatePropertiesArgs, SqlDedicatedGatewayServiceResourceCreateUpdatePropertiesArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:cosmosdb:Service")
class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[Union[DataTransferServiceResourceCreateUpdatePropertiesArgs, DataTransferServiceResourceCreateUpdatePropertiesArgsDict], Union[GraphAPIComputeServiceResourceCreateUpdatePropertiesArgs, GraphAPIComputeServiceResourceCreateUpdatePropertiesArgsDict], Union[MaterializedViewsBuilderServiceResourceCreateUpdatePropertiesArgs, MaterializedViewsBuilderServiceResourceCreateUpdatePropertiesArgsDict], Union[SqlDedicatedGatewayServiceResourceCreateUpdatePropertiesArgs, SqlDedicatedGatewayServiceResourceCreateUpdatePropertiesArgsDict]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ServiceArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Service:
        
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
    def properties(self) -> pulumi.Output[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


