

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkSecurityPerimeterAccessRuleResult', ..., 'get_network_security_perimeter_access_rule', 'get_network_security_perimeter_access_rule_output']
@pulumi.output_type
class GetNetworkSecurityPerimeterAccessRuleResult:
    
    def __init__(__self__, address_prefixes=..., azure_api_version=..., direction=..., email_addresses=..., fully_qualified_domain_names=..., id=..., location=..., name=..., network_security_perimeters=..., phone_numbers=..., provisioning_state=..., service_tags=..., subscriptions=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressPrefixes")
    def address_prefixes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def direction(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainNames")
    def fully_qualified_domain_names(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="networkSecurityPerimeters")
    def network_security_perimeters(self) -> Sequence[outputs.PerimeterBasedAccessRuleResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceTags")
    def service_tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subscriptions(self) -> Optional[Sequence[outputs.SubscriptionIdResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNetworkSecurityPerimeterAccessRuleResult(GetNetworkSecurityPerimeterAccessRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkSecurityPerimeterAccessRuleResult]:
        ...
    


def get_network_security_perimeter_access_rule(access_rule_name: Optional[_builtins.str] = ..., network_security_perimeter_name: Optional[_builtins.str] = ..., profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkSecurityPerimeterAccessRuleResult:
    
    ...

def get_network_security_perimeter_access_rule_output(access_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., network_security_perimeter_name: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkSecurityPerimeterAccessRuleResult]:
    
    ...

