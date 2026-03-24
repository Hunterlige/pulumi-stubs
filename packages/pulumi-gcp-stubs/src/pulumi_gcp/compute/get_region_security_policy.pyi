import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionSecurityPolicyResult",
    "AwaitableGetRegionSecurityPolicyResult",
    "get_region_security_policy",
    "get_region_security_policy_output",
]

@pulumi.output_type
class GetRegionSecurityPolicyResult:
    def __init__(
        __self__,
        advanced_options_configs=...,
        ddos_protection_configs=...,
        description=...,
        fingerprint=...,
        id=...,
        name=...,
        policy_id=...,
        project=...,
        region=...,
        rules=...,
        self_link=...,
        self_link_with_policy_id=...,
        type=...,
        user_defined_fields=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedOptionsConfigs")
    def advanced_options_configs(
        self,
    ) -> Sequence[outputs.GetRegionSecurityPolicyAdvancedOptionsConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="ddosProtectionConfigs")
    def ddos_protection_configs(
        self,
    ) -> Sequence[outputs.GetRegionSecurityPolicyDdosProtectionConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetRegionSecurityPolicyRuleResult]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLinkWithPolicyId")
    def self_link_with_policy_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(
        self,
    ) -> Sequence[outputs.GetRegionSecurityPolicyUserDefinedFieldResult]: ...

class AwaitableGetRegionSecurityPolicyResult(GetRegionSecurityPolicyResult):
    def __await__(self): ...

def get_region_security_policy(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionSecurityPolicyResult: ...
def get_region_security_policy_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionSecurityPolicyResult]: ...
