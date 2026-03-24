

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
__all__ = ['WatchlistArgs', 'Watchlist']
@pulumi.input_type
class WatchlistArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], entity_population_mechanism: pulumi.Input[WatchlistEntityPopulationMechanismArgs], instance: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., multiplying_factor: Optional[pulumi.Input[_builtins.float]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_id: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_user_preferences: Optional[pulumi.Input[WatchlistWatchlistUserPreferencesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityPopulationMechanism")
    def entity_population_mechanism(self) -> pulumi.Input[WatchlistEntityPopulationMechanismArgs]:
        
        ...
    
    @entity_population_mechanism.setter
    def entity_population_mechanism(self, value: pulumi.Input[WatchlistEntityPopulationMechanismArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiplyingFactor")
    def multiplying_factor(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @multiplying_factor.setter
    def multiplying_factor(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @watchlist_id.setter
    def watchlist_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistUserPreferences")
    def watchlist_user_preferences(self) -> Optional[pulumi.Input[WatchlistWatchlistUserPreferencesArgs]]:
        
        ...
    
    @watchlist_user_preferences.setter
    def watchlist_user_preferences(self, value: Optional[pulumi.Input[WatchlistWatchlistUserPreferencesArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _WatchlistState:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., entity_counts: Optional[pulumi.Input[Sequence[pulumi.Input[WatchlistEntityCountArgs]]]] = ..., entity_population_mechanism: Optional[pulumi.Input[WatchlistEntityPopulationMechanismArgs]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multiplying_factor: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_id: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_user_preferences: Optional[pulumi.Input[WatchlistWatchlistUserPreferencesArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityCounts")
    def entity_counts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WatchlistEntityCountArgs]]]]:
        
        ...
    
    @entity_counts.setter
    def entity_counts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WatchlistEntityCountArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityPopulationMechanism")
    def entity_population_mechanism(self) -> Optional[pulumi.Input[WatchlistEntityPopulationMechanismArgs]]:
        
        ...
    
    @entity_population_mechanism.setter
    def entity_population_mechanism(self, value: Optional[pulumi.Input[WatchlistEntityPopulationMechanismArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiplyingFactor")
    def multiplying_factor(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @multiplying_factor.setter
    def multiplying_factor(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @watchlist_id.setter
    def watchlist_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistUserPreferences")
    def watchlist_user_preferences(self) -> Optional[pulumi.Input[WatchlistWatchlistUserPreferencesArgs]]:
        
        ...
    
    @watchlist_user_preferences.setter
    def watchlist_user_preferences(self, value: Optional[pulumi.Input[WatchlistWatchlistUserPreferencesArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:chronicle/watchlist:Watchlist")
class Watchlist(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., entity_population_mechanism: Optional[pulumi.Input[Union[WatchlistEntityPopulationMechanismArgs, WatchlistEntityPopulationMechanismArgsDict]]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multiplying_factor: Optional[pulumi.Input[_builtins.float]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_id: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_user_preferences: Optional[pulumi.Input[Union[WatchlistWatchlistUserPreferencesArgs, WatchlistWatchlistUserPreferencesArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WatchlistArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., entity_counts: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WatchlistEntityCountArgs, WatchlistEntityCountArgsDict]]]]] = ..., entity_population_mechanism: Optional[pulumi.Input[Union[WatchlistEntityPopulationMechanismArgs, WatchlistEntityPopulationMechanismArgsDict]]] = ..., instance: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., multiplying_factor: Optional[pulumi.Input[_builtins.float]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_id: Optional[pulumi.Input[_builtins.str]] = ..., watchlist_user_preferences: Optional[pulumi.Input[Union[WatchlistWatchlistUserPreferencesArgs, WatchlistWatchlistUserPreferencesArgsDict]]] = ...) -> Watchlist:
        
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
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityCounts")
    def entity_counts(self) -> pulumi.Output[Sequence[outputs.WatchlistEntityCount]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityPopulationMechanism")
    def entity_population_mechanism(self) -> pulumi.Output[outputs.WatchlistEntityPopulationMechanism]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiplyingFactor")
    def multiplying_factor(self) -> pulumi.Output[Optional[_builtins.float]]:
        
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="watchlistUserPreferences")
    def watchlist_user_preferences(self) -> pulumi.Output[outputs.WatchlistWatchlistUserPreferences]:
        
        ...
    


