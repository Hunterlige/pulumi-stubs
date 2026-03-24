

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFrontDoorResult', 'AwaitableGetFrontDoorResult', 'get_front_door', 'get_front_door_output']
@pulumi.output_type
class GetFrontDoorResult:
    
    def __init__(__self__, azure_api_version=..., backend_pools=..., backend_pools_settings=..., cname=..., enabled_state=..., extended_properties=..., friendly_name=..., frontdoor_id=..., frontend_endpoints=..., health_probe_settings=..., id=..., load_balancing_settings=..., location=..., name=..., provisioning_state=..., resource_state=..., routing_rules=..., rules_engines=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendPools")
    def backend_pools(self) -> Optional[Sequence[outputs.BackendPoolResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendPoolsSettings")
    def backend_pools_settings(self) -> Optional[outputs.BackendPoolsSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cname(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontdoorId")
    def frontdoor_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendEndpoints")
    def frontend_endpoints(self) -> Optional[Sequence[outputs.FrontendEndpointResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional[Sequence[outputs.HealthProbeSettingsModelResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> Optional[Sequence[outputs.LoadBalancingSettingsModelResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routingRules")
    def routing_rules(self) -> Optional[Sequence[outputs.RoutingRuleResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rulesEngines")
    def rules_engines(self) -> Sequence[outputs.RulesEngineResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFrontDoorResult(GetFrontDoorResult):
    def __await__(self): # -> Generator[Never, Any, GetFrontDoorResult]:
        ...
    


def get_front_door(front_door_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFrontDoorResult:
    
    ...

def get_front_door_output(front_door_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFrontDoorResult]:
    
    ...

