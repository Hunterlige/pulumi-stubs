

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
__all__ = ['ClusterUserCreatedConnectionsArgs', 'ClusterUserCreatedConnections']
@pulumi.input_type
class ClusterUserCreatedConnectionsArgs:
    def __init__(__self__, *, region: pulumi.Input[_builtins.str], cluster_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpoints")
    def cluster_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointArgs]]]]:
        
        ...
    
    @cluster_endpoints.setter
    def cluster_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterUserCreatedConnectionsState:
    def __init__(__self__, *, cluster_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpoints")
    def cluster_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointArgs]]]]:
        
        ...
    
    @cluster_endpoints.setter
    def cluster_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterUserCreatedConnectionsClusterEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ClusterUserCreatedConnections(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterUserCreatedConnectionsClusterEndpointArgs, ClusterUserCreatedConnectionsClusterEndpointArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterUserCreatedConnectionsArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cluster_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterUserCreatedConnectionsClusterEndpointArgs, ClusterUserCreatedConnectionsClusterEndpointArgsDict]]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> ClusterUserCreatedConnections:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterEndpoints")
    def cluster_endpoints(self) -> pulumi.Output[Optional[Sequence[outputs.ClusterUserCreatedConnectionsClusterEndpoint]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


