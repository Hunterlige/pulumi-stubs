

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ContainerServiceDeploymentVersionArgs', 'ContainerServiceDeploymentVersion']
@pulumi.input_type
class ContainerServiceDeploymentVersionArgs:
    def __init__(__self__, *, containers: pulumi.Input[Sequence[pulumi.Input[ContainerServiceDeploymentVersionContainerArgs]]], service_name: pulumi.Input[_builtins.str], public_endpoint: Optional[pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> pulumi.Input[Sequence[pulumi.Input[ContainerServiceDeploymentVersionContainerArgs]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: pulumi.Input[Sequence[pulumi.Input[ContainerServiceDeploymentVersionContainerArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> Optional[pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointArgs]]:
        
        ...
    
    @public_endpoint.setter
    def public_endpoint(self, value: Optional[pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ContainerServiceDeploymentVersionState:
    def __init__(__self__, *, containers: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerServiceDeploymentVersionContainerArgs]]]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., public_endpoint: Optional[pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerServiceDeploymentVersionContainerArgs]]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerServiceDeploymentVersionContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> Optional[pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointArgs]]:
        
        ...
    
    @public_endpoint.setter
    def public_endpoint(self, value: Optional[pulumi.Input[ContainerServiceDeploymentVersionPublicEndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ContainerServiceDeploymentVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., containers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ContainerServiceDeploymentVersionContainerArgs, ContainerServiceDeploymentVersionContainerArgsDict]]]]] = ..., public_endpoint: Optional[pulumi.Input[Union[ContainerServiceDeploymentVersionPublicEndpointArgs, ContainerServiceDeploymentVersionPublicEndpointArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ContainerServiceDeploymentVersionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., containers: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ContainerServiceDeploymentVersionContainerArgs, ContainerServiceDeploymentVersionContainerArgsDict]]]]] = ..., created_at: Optional[pulumi.Input[_builtins.str]] = ..., public_endpoint: Optional[pulumi.Input[Union[ContainerServiceDeploymentVersionPublicEndpointArgs, ContainerServiceDeploymentVersionPublicEndpointArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., service_name: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.int]] = ...) -> ContainerServiceDeploymentVersion:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> pulumi.Output[Sequence[outputs.ContainerServiceDeploymentVersionContainer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicEndpoint")
    def public_endpoint(self) -> pulumi.Output[Optional[outputs.ContainerServiceDeploymentVersionPublicEndpoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.int]:
        
        ...
    


