

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., 'get_virtual_network_gateway_resiliency_information', ...]
@pulumi.output_type
class GetVirtualNetworkGatewayResiliencyInformationResult:
    
    def __init__(__self__, components=..., last_computed_time=..., max_score_from_recommendations=..., min_score_from_recommendations=..., next_eligible_compute_time=..., overall_score=..., score_change=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def components(self) -> Optional[Sequence[outputs.ResiliencyRecommendationComponentsResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastComputedTime")
    def last_computed_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxScoreFromRecommendations")
    def max_score_from_recommendations(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minScoreFromRecommendations")
    def min_score_from_recommendations(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextEligibleComputeTime")
    def next_eligible_compute_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overallScore")
    def overall_score(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scoreChange")
    def score_change(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetVirtualNetworkGatewayResiliencyInformationResult(GetVirtualNetworkGatewayResiliencyInformationResult):
    def __await__(self): # -> Generator[Never, Any, GetVirtualNetworkGatewayResiliencyInformationResult]:
        ...
    


def get_virtual_network_gateway_resiliency_information(attempt_refresh: Optional[_builtins.bool] = ..., resource_group_name: Optional[_builtins.str] = ..., virtual_network_gateway_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVirtualNetworkGatewayResiliencyInformationResult:
    
    ...

def get_virtual_network_gateway_resiliency_information_output(attempt_refresh: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_gateway_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVirtualNetworkGatewayResiliencyInformationResult]:
    
    ...

