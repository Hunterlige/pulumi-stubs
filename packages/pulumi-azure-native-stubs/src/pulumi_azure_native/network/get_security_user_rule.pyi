

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSecurityUserRuleResult', 'AwaitableGetSecurityUserRuleResult', 'get_security_user_rule', 'get_security_user_rule_output']
@pulumi.output_type
class GetSecurityUserRuleResult:
    
    def __init__(__self__, azure_api_version=..., description=..., destination_port_ranges=..., destinations=..., direction=..., etag=..., id=..., name=..., protocol=..., provisioning_state=..., resource_guid=..., source_port_ranges=..., sources=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence[outputs.AddressPrefixItemResponse]]:
        
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
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[Sequence[outputs.AddressPrefixItemResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSecurityUserRuleResult(GetSecurityUserRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetSecurityUserRuleResult]:
        ...
    


def get_security_user_rule(configuration_name: Optional[_builtins.str] = ..., network_manager_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., rule_collection_name: Optional[_builtins.str] = ..., rule_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSecurityUserRuleResult:
    
    ...

def get_security_user_rule_output(configuration_name: Optional[pulumi.Input[_builtins.str]] = ..., network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_collection_name: Optional[pulumi.Input[_builtins.str]] = ..., rule_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSecurityUserRuleResult]:
    
    ...

