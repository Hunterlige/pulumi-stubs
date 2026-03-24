

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebForwardingRuleServiceIamPolicyResult', ..., 'get_web_forwarding_rule_service_iam_policy', 'get_web_forwarding_rule_service_iam_policy_output']
@pulumi.output_type
class GetWebForwardingRuleServiceIamPolicyResult:
    
    def __init__(__self__, etag=..., forwarding_rule_service_name=..., id=..., policy_data=..., project=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardingRuleServiceName")
    def forwarding_rule_service_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        ...
    


class AwaitableGetWebForwardingRuleServiceIamPolicyResult(GetWebForwardingRuleServiceIamPolicyResult):
    def __await__(self): # -> Generator[Never, Any, GetWebForwardingRuleServiceIamPolicyResult]:
        ...
    


def get_web_forwarding_rule_service_iam_policy(forwarding_rule_service_name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebForwardingRuleServiceIamPolicyResult:
    
    ...

def get_web_forwarding_rule_service_iam_policy_output(forwarding_rule_service_name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebForwardingRuleServiceIamPolicyResult]:
    
    ...

