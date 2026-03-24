

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
__all__ = ['ClusterCapacityProvidersArgs', 'ClusterCapacityProviders']
@pulumi.input_type
class ClusterCapacityProvidersArgs:
    def __init__(__self__, *, cluster_name: pulumi.Input[_builtins.str], capacity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., default_capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCapacityProvidersDefaultCapacityProviderStrategyArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviders")
    def capacity_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @capacity_providers.setter
    def capacity_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCapacityProviderStrategies")
    def default_capacity_provider_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCapacityProvidersDefaultCapacityProviderStrategyArgs]]]]:
        
        ...
    
    @default_capacity_provider_strategies.setter
    def default_capacity_provider_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCapacityProvidersDefaultCapacityProviderStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterCapacityProvidersState:
    def __init__(__self__, *, capacity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., default_capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCapacityProvidersDefaultCapacityProviderStrategyArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviders")
    def capacity_providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @capacity_providers.setter
    def capacity_providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCapacityProviderStrategies")
    def default_capacity_provider_strategies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCapacityProvidersDefaultCapacityProviderStrategyArgs]]]]:
        
        ...
    
    @default_capacity_provider_strategies.setter
    def default_capacity_provider_strategies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterCapacityProvidersDefaultCapacityProviderStrategyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ClusterCapacityProviders(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., capacity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., default_capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterCapacityProvidersDefaultCapacityProviderStrategyArgs, ClusterCapacityProvidersDefaultCapacityProviderStrategyArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterCapacityProvidersArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., capacity_providers: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., default_capacity_provider_strategies: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterCapacityProvidersDefaultCapacityProviderStrategyArgs, ClusterCapacityProvidersDefaultCapacityProviderStrategyArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> ClusterCapacityProviders:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="capacityProviders")
    def capacity_providers(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultCapacityProviderStrategies")
    def default_capacity_provider_strategies(self) -> pulumi.Output[Optional[Sequence[outputs.ClusterCapacityProvidersDefaultCapacityProviderStrategy]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


