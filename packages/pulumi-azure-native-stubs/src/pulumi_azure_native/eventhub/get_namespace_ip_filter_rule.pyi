

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNamespaceIpFilterRuleResult', 'AwaitableGetNamespaceIpFilterRuleResult', 'get_namespace_ip_filter_rule', 'get_namespace_ip_filter_rule_output']
@pulumi.output_type
class GetNamespaceIpFilterRuleResult:
    
    def __init__(__self__, action=..., azure_api_version=..., filter_name=..., id=..., ip_mask=..., name=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterName")
    def filter_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipMask")
    def ip_mask(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNamespaceIpFilterRuleResult(GetNamespaceIpFilterRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetNamespaceIpFilterRuleResult]:
        ...
    


def get_namespace_ip_filter_rule(ip_filter_rule_name: Optional[_builtins.str] = ..., namespace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNamespaceIpFilterRuleResult:
    
    ...

def get_namespace_ip_filter_rule_output(ip_filter_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNamespaceIpFilterRuleResult]:
    
    ...

