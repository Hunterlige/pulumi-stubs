

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkInsightsPathResult', 'AwaitableGetNetworkInsightsPathResult', 'get_network_insights_path', 'get_network_insights_path_output']
@pulumi.output_type
class GetNetworkInsightsPathResult:
    
    def __init__(__self__, arn=..., destination=..., destination_arn=..., destination_ip=..., destination_port=..., filter_at_destinations=..., filter_at_sources=..., filters=..., id=..., network_insights_path_id=..., protocol=..., region=..., source=..., source_arn=..., source_ip=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterAtDestinations")
    def filter_at_destinations(self) -> Sequence[outputs.GetNetworkInsightsPathFilterAtDestinationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterAtSources")
    def filter_at_sources(self) -> Sequence[outputs.GetNetworkInsightsPathFilterAtSourceResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetNetworkInsightsPathFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInsightsPathId")
    def network_insights_path_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceArn")
    def source_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetNetworkInsightsPathResult(GetNetworkInsightsPathResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkInsightsPathResult]:
        ...
    


def get_network_insights_path(filters: Optional[Sequence[Union[GetNetworkInsightsPathFilterArgs, GetNetworkInsightsPathFilterArgsDict]]] = ..., network_insights_path_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkInsightsPathResult:
    
    ...

def get_network_insights_path_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetNetworkInsightsPathFilterArgs, GetNetworkInsightsPathFilterArgsDict]]]]] = ..., network_insights_path_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkInsightsPathResult]:
    
    ...

