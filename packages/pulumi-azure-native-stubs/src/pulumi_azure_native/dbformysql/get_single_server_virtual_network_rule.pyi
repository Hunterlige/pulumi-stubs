

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSingleServerVirtualNetworkRuleResult', 'AwaitableGetSingleServerVirtualNetworkRuleResult', 'get_single_server_virtual_network_rule', 'get_single_server_virtual_network_rule_output']
@pulumi.output_type
class GetSingleServerVirtualNetworkRuleResult:
    
    def __init__(__self__, azure_api_version=..., id=..., ignore_missing_vnet_service_endpoint=..., name=..., state=..., type=..., virtual_network_subnet_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreMissingVnetServiceEndpoint")
    def ignore_missing_vnet_service_endpoint(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkSubnetId")
    def virtual_network_subnet_id(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSingleServerVirtualNetworkRuleResult(GetSingleServerVirtualNetworkRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetSingleServerVirtualNetworkRuleResult]:
        ...
    


def get_single_server_virtual_network_rule(resource_group_name: Optional[_builtins.str] = ..., server_name: Optional[_builtins.str] = ..., virtual_network_rule_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSingleServerVirtualNetworkRuleResult:
    
    ...

def get_single_server_virtual_network_rule_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., server_name: Optional[pulumi.Input[_builtins.str]] = ..., virtual_network_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSingleServerVirtualNetworkRuleResult]:
    
    ...

