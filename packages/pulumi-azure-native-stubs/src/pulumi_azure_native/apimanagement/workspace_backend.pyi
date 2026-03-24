

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
__all__ = ['WorkspaceBackendArgs', 'WorkspaceBackend']
@pulumi.input_type
class WorkspaceBackendArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str], workspace_id: pulumi.Input[_builtins.str], backend_id: Optional[pulumi.Input[_builtins.str]] = ..., circuit_breaker: Optional[pulumi.Input[BackendCircuitBreakerArgs]] = ..., credentials: Optional[pulumi.Input[BackendCredentialsContractArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., pool: Optional[pulumi.Input[BackendBaseParametersPoolArgs]] = ..., properties: Optional[pulumi.Input[BackendPropertiesArgs]] = ..., protocol: Optional[pulumi.Input[Union[_builtins.str, BackendProtocol]]] = ..., proxy: Optional[pulumi.Input[BackendProxyContractArgs]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., tls: Optional[pulumi.Input[BackendTlsPropertiesArgs]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, BackendType]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendId")
    def backend_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @backend_id.setter
    def backend_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitBreaker")
    def circuit_breaker(self) -> Optional[pulumi.Input[BackendCircuitBreakerArgs]]:
        
        ...
    
    @circuit_breaker.setter
    def circuit_breaker(self, value: Optional[pulumi.Input[BackendCircuitBreakerArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[BackendCredentialsContractArgs]]:
        
        ...
    
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[BackendCredentialsContractArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[BackendBaseParametersPoolArgs]]:
        ...
    
    @pool.setter
    def pool(self, value: Optional[pulumi.Input[BackendBaseParametersPoolArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[BackendPropertiesArgs]]:
        
        ...
    
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[BackendPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[Union[_builtins.str, BackendProtocol]]]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[Union[_builtins.str, BackendProtocol]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> Optional[pulumi.Input[BackendProxyContractArgs]]:
        
        ...
    
    @proxy.setter
    def proxy(self, value: Optional[pulumi.Input[BackendProxyContractArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tls(self) -> Optional[pulumi.Input[BackendTlsPropertiesArgs]]:
        
        ...
    
    @tls.setter
    def tls(self, value: Optional[pulumi.Input[BackendTlsPropertiesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, BackendType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, BackendType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:apimanagement:WorkspaceBackend")
class WorkspaceBackend(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backend_id: Optional[pulumi.Input[_builtins.str]] = ..., circuit_breaker: Optional[pulumi.Input[Union[BackendCircuitBreakerArgs, BackendCircuitBreakerArgsDict]]] = ..., credentials: Optional[pulumi.Input[Union[BackendCredentialsContractArgs, BackendCredentialsContractArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., pool: Optional[pulumi.Input[Union[BackendBaseParametersPoolArgs, BackendBaseParametersPoolArgsDict]]] = ..., properties: Optional[pulumi.Input[Union[BackendPropertiesArgs, BackendPropertiesArgsDict]]] = ..., protocol: Optional[pulumi.Input[Union[_builtins.str, BackendProtocol]]] = ..., proxy: Optional[pulumi.Input[Union[BackendProxyContractArgs, BackendProxyContractArgsDict]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_id: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., title: Optional[pulumi.Input[_builtins.str]] = ..., tls: Optional[pulumi.Input[Union[BackendTlsPropertiesArgs, BackendTlsPropertiesArgsDict]]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, BackendType]]] = ..., url: Optional[pulumi.Input[_builtins.str]] = ..., workspace_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkspaceBackendArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WorkspaceBackend:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="circuitBreaker")
    def circuit_breaker(self) -> pulumi.Output[Optional[outputs.BackendCircuitBreakerResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[outputs.BackendCredentialsContractResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pool(self) -> pulumi.Output[Optional[outputs.BackendBaseParametersResponsePool]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> pulumi.Output[outputs.BackendPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def proxy(self) -> pulumi.Output[Optional[outputs.BackendProxyContractResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tls(self) -> pulumi.Output[Optional[outputs.BackendTlsPropertiesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


