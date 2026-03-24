

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['IntegrationAccountArgs', 'IntegrationAccount']
@pulumi.input_type
class IntegrationAccountArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., integration_service_environment: Optional[pulumi.Input[ResourceReferenceArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[IntegrationAccountSkuArgs]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_account_name.setter
    def integration_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @integration_service_environment.setter
    def integration_service_environment(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[IntegrationAccountSkuArgs]]:
        
        ...
    
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[IntegrationAccountSkuArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:logic:IntegrationAccount")
class IntegrationAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., integration_account_name: Optional[pulumi.Input[_builtins.str]] = ..., integration_service_environment: Optional[pulumi.Input[Union[ResourceReferenceArgs, ResourceReferenceArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sku: Optional[pulumi.Input[Union[IntegrationAccountSkuArgs, IntegrationAccountSkuArgsDict]]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IntegrationAccountArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> IntegrationAccount:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationServiceEnvironment")
    def integration_service_environment(self) -> pulumi.Output[Optional[outputs.ResourceReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.IntegrationAccountSkuResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


