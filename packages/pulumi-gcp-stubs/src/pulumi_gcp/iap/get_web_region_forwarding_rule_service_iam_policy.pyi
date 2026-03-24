import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetWebRegionForwardingRuleServiceIamPolicyResult",
    ...,
    "get_web_region_forwarding_rule_service_iam_policy",
    ...,
]

@pulumi.output_type
class GetWebRegionForwardingRuleServiceIamPolicyResult:
    def __init__(
        __self__,
        etag=...,
        forwarding_rule_region_service_name=...,
        id=...,
        policy_data=...,
        project=...,
        region=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRuleRegionServiceName")
    def forwarding_rule_region_service_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyData")
    def policy_data(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetWebRegionForwardingRuleServiceIamPolicyResult(
    GetWebRegionForwardingRuleServiceIamPolicyResult
):
    def __await__(self): ...

def get_web_region_forwarding_rule_service_iam_policy(
    forwarding_rule_region_service_name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetWebRegionForwardingRuleServiceIamPolicyResult: ...
def get_web_region_forwarding_rule_service_iam_policy_output(
    forwarding_rule_region_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetWebRegionForwardingRuleServiceIamPolicyResult]: ...
