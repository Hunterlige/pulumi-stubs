import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecurityPolicyRuleInitArgs", "SecurityPolicyRule"]

@pulumi.input_type
class SecurityPolicyRuleInitArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
        security_policy: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        header_action: Optional[pulumi.Input[SecurityPolicyRuleHeaderActionArgs]] = ...,
        match: Optional[pulumi.Input[SecurityPolicyRuleMatchArgs]] = ...,
        preconfigured_waf_config: Optional[
            pulumi.Input[SecurityPolicyRulePreconfiguredWafConfigArgs]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_limit_options: Optional[
            pulumi.Input[SecurityPolicyRuleRateLimitOptionsArgs]
        ] = ...,
        redirect_options: Optional[
            pulumi.Input[SecurityPolicyRuleRedirectOptionsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]: ...
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]: ...
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> pulumi.Input[_builtins.str]: ...
    @security_policy.setter
    def security_policy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRuleHeaderActionArgs]]: ...
    @header_action.setter
    def header_action(
        self, value: Optional[pulumi.Input[SecurityPolicyRuleHeaderActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[SecurityPolicyRuleMatchArgs]]: ...
    @match.setter
    def match(self, value: Optional[pulumi.Input[SecurityPolicyRuleMatchArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="preconfiguredWafConfig")
    def preconfigured_waf_config(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRulePreconfiguredWafConfigArgs]]: ...
    @preconfigured_waf_config.setter
    def preconfigured_waf_config(
        self,
        value: Optional[pulumi.Input[SecurityPolicyRulePreconfiguredWafConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preview.setter
    def preview(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rateLimitOptions")
    def rate_limit_options(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRuleRateLimitOptionsArgs]]: ...
    @rate_limit_options.setter
    def rate_limit_options(
        self, value: Optional[pulumi.Input[SecurityPolicyRuleRateLimitOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectOptions")
    def redirect_options(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRuleRedirectOptionsArgs]]: ...
    @redirect_options.setter
    def redirect_options(
        self, value: Optional[pulumi.Input[SecurityPolicyRuleRedirectOptionsArgs]]
    ): ...

@pulumi.input_type
class _SecurityPolicyRuleState:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        header_action: Optional[pulumi.Input[SecurityPolicyRuleHeaderActionArgs]] = ...,
        match: Optional[pulumi.Input[SecurityPolicyRuleMatchArgs]] = ...,
        preconfigured_waf_config: Optional[
            pulumi.Input[SecurityPolicyRulePreconfiguredWafConfigArgs]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_limit_options: Optional[
            pulumi.Input[SecurityPolicyRuleRateLimitOptionsArgs]
        ] = ...,
        redirect_options: Optional[
            pulumi.Input[SecurityPolicyRuleRedirectOptionsArgs]
        ] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRuleHeaderActionArgs]]: ...
    @header_action.setter
    def header_action(
        self, value: Optional[pulumi.Input[SecurityPolicyRuleHeaderActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[SecurityPolicyRuleMatchArgs]]: ...
    @match.setter
    def match(self, value: Optional[pulumi.Input[SecurityPolicyRuleMatchArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="preconfiguredWafConfig")
    def preconfigured_waf_config(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRulePreconfiguredWafConfigArgs]]: ...
    @preconfigured_waf_config.setter
    def preconfigured_waf_config(
        self,
        value: Optional[pulumi.Input[SecurityPolicyRulePreconfiguredWafConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preview.setter
    def preview(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @priority.setter
    def priority(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rateLimitOptions")
    def rate_limit_options(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRuleRateLimitOptionsArgs]]: ...
    @rate_limit_options.setter
    def rate_limit_options(
        self, value: Optional[pulumi.Input[SecurityPolicyRuleRateLimitOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectOptions")
    def redirect_options(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRuleRedirectOptionsArgs]]: ...
    @redirect_options.setter
    def redirect_options(
        self, value: Optional[pulumi.Input[SecurityPolicyRuleRedirectOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/securityPolicyRule:SecurityPolicyRule")
class SecurityPolicyRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        header_action: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRuleHeaderActionArgs,
                    SecurityPolicyRuleHeaderActionArgsDict,
                ]
            ]
        ] = ...,
        match: Optional[
            pulumi.Input[
                Union[SecurityPolicyRuleMatchArgs, SecurityPolicyRuleMatchArgsDict]
            ]
        ] = ...,
        preconfigured_waf_config: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRulePreconfiguredWafConfigArgs,
                    SecurityPolicyRulePreconfiguredWafConfigArgsDict,
                ]
            ]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_limit_options: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRuleRateLimitOptionsArgs,
                    SecurityPolicyRuleRateLimitOptionsArgsDict,
                ]
            ]
        ] = ...,
        redirect_options: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRuleRedirectOptionsArgs,
                    SecurityPolicyRuleRedirectOptionsArgsDict,
                ]
            ]
        ] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SecurityPolicyRuleInitArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        header_action: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRuleHeaderActionArgs,
                    SecurityPolicyRuleHeaderActionArgsDict,
                ]
            ]
        ] = ...,
        match: Optional[
            pulumi.Input[
                Union[SecurityPolicyRuleMatchArgs, SecurityPolicyRuleMatchArgsDict]
            ]
        ] = ...,
        preconfigured_waf_config: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRulePreconfiguredWafConfigArgs,
                    SecurityPolicyRulePreconfiguredWafConfigArgsDict,
                ]
            ]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_limit_options: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRuleRateLimitOptionsArgs,
                    SecurityPolicyRuleRateLimitOptionsArgsDict,
                ]
            ]
        ] = ...,
        redirect_options: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRuleRedirectOptionsArgs,
                    SecurityPolicyRuleRedirectOptionsArgsDict,
                ]
            ]
        ] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SecurityPolicyRule: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="headerAction")
    def header_action(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityPolicyRuleHeaderAction]]: ...
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Output[Optional[outputs.SecurityPolicyRuleMatch]]: ...
    @_builtins.property
    @pulumi.getter(name="preconfiguredWafConfig")
    def preconfigured_waf_config(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityPolicyRulePreconfiguredWafConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def preview(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rateLimitOptions")
    def rate_limit_options(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityPolicyRuleRateLimitOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="redirectOptions")
    def redirect_options(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityPolicyRuleRedirectOptions]]: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> pulumi.Output[_builtins.str]: ...
