

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
__all__ = ['IntegrationRuntimeArgs', 'IntegrationRuntime']
@pulumi.input_type
class IntegrationRuntimeArgs:
    def __init__(__self__, *, factory_name: pulumi.Input[_builtins.str], properties: pulumi.Input[Union[ManagedIntegrationRuntimeArgs, SelfHostedIntegrationRuntimeArgs]], resource_group_name: pulumi.Input[_builtins.str], integration_runtime_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @factory_name.setter
    def factory_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union[ManagedIntegrationRuntimeArgs, SelfHostedIntegrationRuntimeArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[Union[ManagedIntegrationRuntimeArgs, SelfHostedIntegrationRuntimeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationRuntimeName")
    def integration_runtime_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_runtime_name.setter
    def integration_runtime_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:datafactory:IntegrationRuntime")
class IntegrationRuntime(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., factory_name: Optional[pulumi.Input[_builtins.str]] = ..., integration_runtime_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[Union[ManagedIntegrationRuntimeArgs, ManagedIntegrationRuntimeArgsDict], Union[SelfHostedIntegrationRuntimeArgs, SelfHostedIntegrationRuntimeArgsDict]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: IntegrationRuntimeArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> IntegrationRuntime:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
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
    


