

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['EnvironmentArgs', 'Environment']
@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *, kind: pulumi.Input[Union[_builtins.str, EnvironmentKind]], resource_group_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], custom_properties: Optional[Any] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., onboarding: Optional[pulumi.Input[OnboardingArgs]] = ..., server: Optional[pulumi.Input[EnvironmentServerArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[Union[_builtins.str, EnvironmentKind]]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[Union[_builtins.str, EnvironmentKind]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Any]:
        
        ...
    
    @custom_properties.setter
    def custom_properties(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def onboarding(self) -> Optional[pulumi.Input[OnboardingArgs]]:
        
        ...
    
    @onboarding.setter
    def onboarding(self, value: Optional[pulumi.Input[OnboardingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[EnvironmentServerArgs]]:
        
        ...
    
    @server.setter
    def server(self, value: Optional[pulumi.Input[EnvironmentServerArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:apicenter:Environment")
class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., custom_properties: Optional[Any] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., environment_name: Optional[pulumi.Input[_builtins.str]] = ..., kind: Optional[pulumi.Input[Union[_builtins.str, EnvironmentKind]]] = ..., onboarding: Optional[pulumi.Input[Union[OnboardingArgs, OnboardingArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server: Optional[pulumi.Input[Union[EnvironmentServerArgs, EnvironmentServerArgsDict]]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: EnvironmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Environment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> pulumi.Output[Optional[Any]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter
    def onboarding(self) -> pulumi.Output[Optional[outputs.OnboardingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Output[Optional[outputs.EnvironmentServerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


