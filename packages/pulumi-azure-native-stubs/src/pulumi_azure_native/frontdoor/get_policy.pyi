

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPolicyResult', 'AwaitableGetPolicyResult', 'get_policy', 'get_policy_output']
@pulumi.output_type
class GetPolicyResult:
    
    def __init__(__self__, azure_api_version=..., custom_rules=..., etag=..., frontend_endpoint_links=..., id=..., location=..., managed_rules=..., name=..., policy_settings=..., provisioning_state=..., resource_state=..., routing_rule_links=..., security_policy_links=..., sku=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> Optional[outputs.CustomRuleListResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frontendEndpointLinks")
    def frontend_endpoint_links(self) -> Sequence[outputs.FrontendEndpointLinkResponse]:
        
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
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> Optional[outputs.ManagedRuleSetListResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policySettings")
    def policy_settings(self) -> Optional[outputs.PolicySettingsResponse]:
        
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
    @pulumi.getter(name="routingRuleLinks")
    def routing_rule_links(self) -> Sequence[outputs.RoutingRuleLinkResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityPolicyLinks")
    def security_policy_links(self) -> Sequence[outputs.SecurityPolicyLinkResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPolicyResult(GetPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetPolicyResult]:
        ...
    


def get_policy(policy_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPolicyResult:
    
    ...

def get_policy_output(policy_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPolicyResult]:
    
    ...

