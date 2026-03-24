

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMongoClusterFirewallRuleResult', 'AwaitableGetMongoClusterFirewallRuleResult', 'get_mongo_cluster_firewall_rule', 'get_mongo_cluster_firewall_rule_output']
@pulumi.output_type
class GetMongoClusterFirewallRuleResult:
    
    def __init__(__self__, azure_api_version=..., end_ip_address=..., id=..., name=..., provisioning_state=..., start_ip_address=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endIpAddress")
    def end_ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="startIpAddress")
    def start_ip_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetMongoClusterFirewallRuleResult(GetMongoClusterFirewallRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetMongoClusterFirewallRuleResult]:
        ...
    


def get_mongo_cluster_firewall_rule(firewall_rule_name: Optional[_builtins.str] = ..., mongo_cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMongoClusterFirewallRuleResult:
    
    ...

def get_mongo_cluster_firewall_rule_output(firewall_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., mongo_cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMongoClusterFirewallRuleResult]:
    
    ...

