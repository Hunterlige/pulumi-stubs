

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MulticastDomainArgs', 'MulticastDomain']
@pulumi.input_type
class MulticastDomainArgs:
    def __init__(__self__, *, admin_network: pulumi.Input[_builtins.str], connection_config: pulumi.Input[MulticastDomainConnectionConfigArgs], location: pulumi.Input[_builtins.str], multicast_domain_id: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., multicast_domain_group: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ull_multicast_domain: Optional[pulumi.Input[MulticastDomainUllMulticastDomainArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminNetwork")
    def admin_network(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @admin_network.setter
    def admin_network(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionConfig")
    def connection_config(self) -> pulumi.Input[MulticastDomainConnectionConfigArgs]:
        
        ...
    
    @connection_config.setter
    def connection_config(self, value: pulumi.Input[MulticastDomainConnectionConfigArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multicastDomainId")
    def multicast_domain_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @multicast_domain_id.setter
    def multicast_domain_id(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multicastDomainGroup")
    def multicast_domain_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multicast_domain_group.setter
    def multicast_domain_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ullMulticastDomain")
    def ull_multicast_domain(self) -> Optional[pulumi.Input[MulticastDomainUllMulticastDomainArgs]]:
        
        ...
    
    @ull_multicast_domain.setter
    def ull_multicast_domain(self, value: Optional[pulumi.Input[MulticastDomainUllMulticastDomainArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _MulticastDomainState:
    def __init__(__self__, *, admin_network: Optional[pulumi.Input[_builtins.str]] = ..., connection_config: Optional[pulumi.Input[MulticastDomainConnectionConfigArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multicast_domain_group: Optional[pulumi.Input[_builtins.str]] = ..., multicast_domain_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., states: Optional[pulumi.Input[Sequence[pulumi.Input[MulticastDomainStateArgs]]]] = ..., ull_multicast_domain: Optional[pulumi.Input[MulticastDomainUllMulticastDomainArgs]] = ..., unique_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminNetwork")
    def admin_network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @admin_network.setter
    def admin_network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionConfig")
    def connection_config(self) -> Optional[pulumi.Input[MulticastDomainConnectionConfigArgs]]:
        
        ...
    
    @connection_config.setter
    def connection_config(self, value: Optional[pulumi.Input[MulticastDomainConnectionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multicastDomainGroup")
    def multicast_domain_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multicast_domain_group.setter
    def multicast_domain_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multicastDomainId")
    def multicast_domain_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @multicast_domain_id.setter
    def multicast_domain_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def states(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[MulticastDomainStateArgs]]]]:
        
        ...
    
    @states.setter
    def states(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MulticastDomainStateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ullMulticastDomain")
    def ull_multicast_domain(self) -> Optional[pulumi.Input[MulticastDomainUllMulticastDomainArgs]]:
        
        ...
    
    @ull_multicast_domain.setter
    def ull_multicast_domain(self, value: Optional[pulumi.Input[MulticastDomainUllMulticastDomainArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @unique_id.setter
    def unique_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class MulticastDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., admin_network: Optional[pulumi.Input[_builtins.str]] = ..., connection_config: Optional[pulumi.Input[Union[MulticastDomainConnectionConfigArgs, MulticastDomainConnectionConfigArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multicast_domain_group: Optional[pulumi.Input[_builtins.str]] = ..., multicast_domain_id: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., ull_multicast_domain: Optional[pulumi.Input[Union[MulticastDomainUllMulticastDomainArgs, MulticastDomainUllMulticastDomainArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MulticastDomainArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., admin_network: Optional[pulumi.Input[_builtins.str]] = ..., connection_config: Optional[pulumi.Input[Union[MulticastDomainConnectionConfigArgs, MulticastDomainConnectionConfigArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multicast_domain_group: Optional[pulumi.Input[_builtins.str]] = ..., multicast_domain_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., states: Optional[pulumi.Input[Sequence[pulumi.Input[Union[MulticastDomainStateArgs, MulticastDomainStateArgsDict]]]]] = ..., ull_multicast_domain: Optional[pulumi.Input[Union[MulticastDomainUllMulticastDomainArgs, MulticastDomainUllMulticastDomainArgsDict]]] = ..., unique_id: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> MulticastDomain:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminNetwork")
    def admin_network(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionConfig")
    def connection_config(self) -> pulumi.Output[outputs.MulticastDomainConnectionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multicastDomainGroup")
    def multicast_domain_group(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multicastDomainId")
    def multicast_domain_id(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def states(self) -> pulumi.Output[Sequence[outputs.MulticastDomainState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ullMulticastDomain")
    def ull_multicast_domain(self) -> pulumi.Output[Optional[outputs.MulticastDomainUllMulticastDomain]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


