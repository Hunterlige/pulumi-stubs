

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRouteFilterRuleResult', 'AwaitableGetRouteFilterRuleResult', 'get_route_filter_rule', 'get_route_filter_rule_output']
@pulumi.output_type
class GetRouteFilterRuleResult:
    
    def __init__(__self__, access=..., azure_api_version=..., communities=..., etag=..., id=..., location=..., name=..., provisioning_state=..., route_filter_rule_type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def access(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def communities(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routeFilterRuleType")
    def route_filter_rule_type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetRouteFilterRuleResult(GetRouteFilterRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetRouteFilterRuleResult]:
        ...
    


def get_route_filter_rule(resource_group_name: Optional[_builtins.str] = ..., route_filter_name: Optional[_builtins.str] = ..., rule_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetRouteFilterRuleResult:
    
    ...

def get_route_filter_rule_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., route_filter_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetRouteFilterRuleResult]:
    
    ...

