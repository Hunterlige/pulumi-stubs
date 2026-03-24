

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FrontDoorArgs', 'FrontDoor']
@pulumi.input_type
class FrontDoorArgs:
    def __init__(__self__, *, resource_group_name: pulumi.Input[_builtins.str], backend_pools: Optional[pulumi.Input[Sequence[pulumi.Input[BackendPoolArgs]]]] = ..., backend_pools_settings: Optional[pulumi.Input[BackendPoolsSettingsArgs]] = ..., enabled_state: Optional[pulumi.Input[Union[_builtins.str, FrontDoorEnabledState]]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., front_door_name: Optional[pulumi.Input[_builtins.str]] = ..., frontend_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[FrontendEndpointArgs]]]] = ..., health_probe_settings: Optional[pulumi.Input[Sequence[pulumi.Input[HealthProbeSettingsModelArgs]]]] = ..., load_balancing_settings: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancingSettingsModelArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[RoutingRuleArgs]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendPools")
    def backend_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BackendPoolArgs]]]]:
        
        ...
    
    @backend_pools.setter
    def backend_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BackendPoolArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendPoolsSettings")
    def backend_pools_settings(self) -> Optional[pulumi.Input[BackendPoolsSettingsArgs]]:
        
        ...
    
    @backend_pools_settings.setter
    def backend_pools_settings(self, value: Optional[pulumi.Input[BackendPoolsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[_builtins.str, FrontDoorEnabledState]]]:
        
        ...
    
    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[_builtins.str, FrontDoorEnabledState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontDoorName")
    def front_door_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @front_door_name.setter
    def front_door_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendEndpoints")
    def frontend_endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FrontendEndpointArgs]]]]:
        
        ...
    
    @frontend_endpoints.setter
    def frontend_endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FrontendEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HealthProbeSettingsModelArgs]]]]:
        
        ...
    
    @health_probe_settings.setter
    def health_probe_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HealthProbeSettingsModelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancingSettingsModelArgs]]]]:
        
        ...
    
    @load_balancing_settings.setter
    def load_balancing_settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[LoadBalancingSettingsModelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoutingRuleArgs]]]]:
        
        ...
    
    @routing_rules.setter
    def routing_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RoutingRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:frontdoor:FrontDoor")
class FrontDoor(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., backend_pools: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BackendPoolArgs, BackendPoolArgsDict]]]]] = ..., backend_pools_settings: Optional[pulumi.Input[Union[BackendPoolsSettingsArgs, BackendPoolsSettingsArgsDict]]] = ..., enabled_state: Optional[pulumi.Input[Union[_builtins.str, FrontDoorEnabledState]]] = ..., friendly_name: Optional[pulumi.Input[_builtins.str]] = ..., front_door_name: Optional[pulumi.Input[_builtins.str]] = ..., frontend_endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[FrontendEndpointArgs, FrontendEndpointArgsDict]]]]] = ..., health_probe_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[HealthProbeSettingsModelArgs, HealthProbeSettingsModelArgsDict]]]]] = ..., load_balancing_settings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[LoadBalancingSettingsModelArgs, LoadBalancingSettingsModelArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RoutingRuleArgs, RoutingRuleArgsDict]]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FrontDoorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> FrontDoor:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendPools")
    def backend_pools(self) -> pulumi.Output[Optional[Sequence[outputs.BackendPoolResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendPoolsSettings")
    def backend_pools_settings(self) -> pulumi.Output[Optional[outputs.BackendPoolsSettingsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cname(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontdoorId")
    def frontdoor_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendEndpoints")
    def frontend_endpoints(self) -> pulumi.Output[Optional[Sequence[outputs.FrontendEndpointResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> pulumi.Output[Optional[Sequence[outputs.HealthProbeSettingsModelResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> pulumi.Output[Optional[Sequence[outputs.LoadBalancingSettingsModelResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> pulumi.Output[Optional[Sequence[outputs.RoutingRuleResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesEngines")
    def rules_engines(self) -> pulumi.Output[Sequence[outputs.RulesEngineResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


