

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
__all__ = ['ResponsePolicyArgs', 'ResponsePolicy']
@pulumi.input_type
class ResponsePolicyArgs:
    def __init__(__self__, *, response_policy_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyGkeClusterArgs]]]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyNetworkArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsePolicyName")
    def response_policy_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @response_policy_name.setter
    def response_policy_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyGkeClusterArgs]]]]:
        
        ...
    
    @gke_clusters.setter
    def gke_clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyGkeClusterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyNetworkArgs]]]]:
        
        ...
    
    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyNetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ResponsePolicyState:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyGkeClusterArgs]]]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyNetworkArgs]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., response_policy_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyGkeClusterArgs]]]]:
        
        ...
    
    @gke_clusters.setter
    def gke_clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyGkeClusterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyNetworkArgs]]]]:
        
        ...
    
    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResponsePolicyNetworkArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsePolicyName")
    def response_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @response_policy_name.setter
    def response_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:dns/responsePolicy:ResponsePolicy")
class ResponsePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResponsePolicyGkeClusterArgs, ResponsePolicyGkeClusterArgsDict]]]]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResponsePolicyNetworkArgs, ResponsePolicyNetworkArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., response_policy_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ResponsePolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., gke_clusters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResponsePolicyGkeClusterArgs, ResponsePolicyGkeClusterArgsDict]]]]] = ..., networks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ResponsePolicyNetworkArgs, ResponsePolicyNetworkArgsDict]]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., response_policy_name: Optional[pulumi.Input[_builtins.str]] = ...) -> ResponsePolicy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeClusters")
    def gke_clusters(self) -> pulumi.Output[Optional[Sequence[outputs.ResponsePolicyGkeCluster]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def networks(self) -> pulumi.Output[Optional[Sequence[outputs.ResponsePolicyNetwork]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsePolicyName")
    def response_policy_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


