import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSecurityPolicyResult",
    "AwaitableGetSecurityPolicyResult",
    "get_security_policy",
    "get_security_policy_output",
]

@pulumi.output_type
class GetSecurityPolicyResult:
    def __init__(
        __self__,
        adaptive_protection_configs=...,
        advanced_options_configs=...,
        description=...,
        effective_labels=...,
        fingerprint=...,
        id=...,
        label_fingerprint=...,
        labels=...,
        name=...,
        project=...,
        pulumi_labels=...,
        recaptcha_options_configs=...,
        rules=...,
        self_link=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adaptiveProtectionConfigs")
    def adaptive_protection_configs(
        self,
    ) -> Sequence[outputs.GetSecurityPolicyAdaptiveProtectionConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="advancedOptionsConfigs")
    def advanced_options_configs(
        self,
    ) -> Sequence[outputs.GetSecurityPolicyAdvancedOptionsConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recaptchaOptionsConfigs")
    def recaptcha_options_configs(
        self,
    ) -> Sequence[outputs.GetSecurityPolicyRecaptchaOptionsConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.GetSecurityPolicyRuleResult]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetSecurityPolicyResult(GetSecurityPolicyResult):
    def __await__(self): ...

def get_security_policy(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    self_link: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSecurityPolicyResult: ...
def get_security_policy_output(
    name: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    self_link: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSecurityPolicyResult]: ...
