

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDefaultUserRuleResult', 'AwaitableGetDefaultUserRuleResult', 'get_default_user_rule', 'get_default_user_rule_output']
@pulumi.output_type
class GetDefaultUserRuleResult:
    
    def __init__(__self__, azure_api_version=..., description=..., destination_port_ranges=..., destinations=..., direction=..., etag=..., flag=..., id=..., kind=..., name=..., protocol=..., provisioning_state=..., source_port_ranges=..., sources=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Sequence[outputs.AddressPrefixItemResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Sequence[outputs.AddressPrefixItemResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDefaultUserRuleResult(GetDefaultUserRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetDefaultUserRuleResult]:
        ...
    


def get_default_user_rule(configuration_name: Optional[_builtins.str] = ..., network_manager_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., rule_collection_name: Optional[_builtins.str] = ..., rule_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDefaultUserRuleResult:
    
    ...

def get_default_user_rule_output(configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_collection_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDefaultUserRuleResult]:
    
    ...

