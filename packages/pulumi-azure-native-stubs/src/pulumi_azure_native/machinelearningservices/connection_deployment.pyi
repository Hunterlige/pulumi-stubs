

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
__all__ = ['ConnectionDeploymentArgs', 'ConnectionDeployment']
@pulumi.input_type
class ConnectionDeploymentArgs:
    def __init__(__self__, *, connection_name: pulumi.Input[_builtins.str], properties: pulumi.Input[Union[ContentSafetyEndpointDeploymentResourcePropertiesArgs, ManagedOnlineEndpointDeploymentResourcePropertiesArgs, OpenAIEndpointDeploymentResourcePropertiesArgs, SpeechEndpointDeploymentResourcePropertiesArgs]], resource_group_name: pulumi.Input[_builtins.str], workspace_name: pulumi.Input[_builtins.str], deployment_name: Optional[pulumi.Input[_builtins.str]] = ..., proxy_api_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @connection_name.setter
    def connection_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Input[Union[ContentSafetyEndpointDeploymentResourcePropertiesArgs, ManagedOnlineEndpointDeploymentResourcePropertiesArgs, OpenAIEndpointDeploymentResourcePropertiesArgs, SpeechEndpointDeploymentResourcePropertiesArgs]]:
        ...
    
    @properties.setter
    def properties(self, value: pulumi.Input[Union[ContentSafetyEndpointDeploymentResourcePropertiesArgs, ManagedOnlineEndpointDeploymentResourcePropertiesArgs, OpenAIEndpointDeploymentResourcePropertiesArgs, SpeechEndpointDeploymentResourcePropertiesArgs]]): # -> None:
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
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyApiVersion")
    def proxy_api_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @proxy_api_version.setter
    def proxy_api_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ConnectionDeployment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connection_name: Optional[pulumi.Input[_builtins.str]] = ..., deployment_name: Optional[pulumi.Input[_builtins.str]] = ..., properties: Optional[pulumi.Input[Union[Union[ContentSafetyEndpointDeploymentResourcePropertiesArgs, ContentSafetyEndpointDeploymentResourcePropertiesArgsDict], Union[ManagedOnlineEndpointDeploymentResourcePropertiesArgs, ManagedOnlineEndpointDeploymentResourcePropertiesArgsDict], Union[OpenAIEndpointDeploymentResourcePropertiesArgs, OpenAIEndpointDeploymentResourcePropertiesArgsDict], Union[SpeechEndpointDeploymentResourcePropertiesArgs, SpeechEndpointDeploymentResourcePropertiesArgsDict]]]] = ..., proxy_api_version: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectionDeploymentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ConnectionDeployment:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


