import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegionSecurityPolicyRuleInitArgs", "RegionSecurityPolicyRule"]

@pulumi.input_type
class RegionSecurityPolicyRuleInitArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[_builtins.str],
        priority: pulumi.Input[_builtins.int],
        region: pulumi.Input[_builtins.str],
        security_policy: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        match: Optional[pulumi.Input[RegionSecurityPolicyRuleMatchArgs]] = ...,
        network_match: Optional[
            pulumi.Input[RegionSecurityPolicyRuleNetworkMatchArgs]
        ] = ...,
        preconfigured_waf_config: Optional[
            pulumi.Input[RegionSecurityPolicyRulePreconfiguredWafConfigArgs]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_limit_options: Optional[
            pulumi.Input[RegionSecurityPolicyRuleRateLimitOptionsArgs]
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
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[RegionSecurityPolicyRuleMatchArgs]]: ...
    @match.setter
    def match(
        self, value: Optional[pulumi.Input[RegionSecurityPolicyRuleMatchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkMatch")
    def network_match(
        self,
    ) -> Optional[pulumi.Input[RegionSecurityPolicyRuleNetworkMatchArgs]]: ...
    @network_match.setter
    def network_match(
        self, value: Optional[pulumi.Input[RegionSecurityPolicyRuleNetworkMatchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preconfiguredWafConfig")
    def preconfigured_waf_config(
        self,
    ) -> Optional[pulumi.Input[RegionSecurityPolicyRulePreconfiguredWafConfigArgs]]: ...
    @preconfigured_waf_config.setter
    def preconfigured_waf_config(
        self,
        value: Optional[
            pulumi.Input[RegionSecurityPolicyRulePreconfiguredWafConfigArgs]
        ],
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
    ) -> Optional[pulumi.Input[RegionSecurityPolicyRuleRateLimitOptionsArgs]]: ...
    @rate_limit_options.setter
    def rate_limit_options(
        self,
        value: Optional[pulumi.Input[RegionSecurityPolicyRuleRateLimitOptionsArgs]],
    ): ...

@pulumi.input_type
class _RegionSecurityPolicyRuleState:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        match: Optional[pulumi.Input[RegionSecurityPolicyRuleMatchArgs]] = ...,
        network_match: Optional[
            pulumi.Input[RegionSecurityPolicyRuleNetworkMatchArgs]
        ] = ...,
        preconfigured_waf_config: Optional[
            pulumi.Input[RegionSecurityPolicyRulePreconfiguredWafConfigArgs]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_limit_options: Optional[
            pulumi.Input[RegionSecurityPolicyRuleRateLimitOptionsArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter
    def match(self) -> Optional[pulumi.Input[RegionSecurityPolicyRuleMatchArgs]]: ...
    @match.setter
    def match(
        self, value: Optional[pulumi.Input[RegionSecurityPolicyRuleMatchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkMatch")
    def network_match(
        self,
    ) -> Optional[pulumi.Input[RegionSecurityPolicyRuleNetworkMatchArgs]]: ...
    @network_match.setter
    def network_match(
        self, value: Optional[pulumi.Input[RegionSecurityPolicyRuleNetworkMatchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preconfiguredWafConfig")
    def preconfigured_waf_config(
        self,
    ) -> Optional[pulumi.Input[RegionSecurityPolicyRulePreconfiguredWafConfigArgs]]: ...
    @preconfigured_waf_config.setter
    def preconfigured_waf_config(
        self,
        value: Optional[
            pulumi.Input[RegionSecurityPolicyRulePreconfiguredWafConfigArgs]
        ],
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
    ) -> Optional[pulumi.Input[RegionSecurityPolicyRuleRateLimitOptionsArgs]]: ...
    @rate_limit_options.setter
    def rate_limit_options(
        self,
        value: Optional[pulumi.Input[RegionSecurityPolicyRuleRateLimitOptionsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class RegionSecurityPolicyRule(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        match: Optional[
            pulumi.Input[
                Union[
                    RegionSecurityPolicyRuleMatchArgs,
                    RegionSecurityPolicyRuleMatchArgsDict,
                ]
            ]
        ] = ...,
        network_match: Optional[
            pulumi.Input[
                Union[
                    RegionSecurityPolicyRuleNetworkMatchArgs,
                    RegionSecurityPolicyRuleNetworkMatchArgsDict,
                ]
            ]
        ] = ...,
        preconfigured_waf_config: Optional[
            pulumi.Input[
                Union[
                    RegionSecurityPolicyRulePreconfiguredWafConfigArgs,
                    RegionSecurityPolicyRulePreconfiguredWafConfigArgsDict,
                ]
            ]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_limit_options: Optional[
            pulumi.Input[
                Union[
                    RegionSecurityPolicyRuleRateLimitOptionsArgs,
                    RegionSecurityPolicyRuleRateLimitOptionsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RegionSecurityPolicyRuleInitArgs,
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
        match: Optional[
            pulumi.Input[
                Union[
                    RegionSecurityPolicyRuleMatchArgs,
                    RegionSecurityPolicyRuleMatchArgsDict,
                ]
            ]
        ] = ...,
        network_match: Optional[
            pulumi.Input[
                Union[
                    RegionSecurityPolicyRuleNetworkMatchArgs,
                    RegionSecurityPolicyRuleNetworkMatchArgsDict,
                ]
            ]
        ] = ...,
        preconfigured_waf_config: Optional[
            pulumi.Input[
                Union[
                    RegionSecurityPolicyRulePreconfiguredWafConfigArgs,
                    RegionSecurityPolicyRulePreconfiguredWafConfigArgsDict,
                ]
            ]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        rate_limit_options: Optional[
            pulumi.Input[
                Union[
                    RegionSecurityPolicyRuleRateLimitOptionsArgs,
                    RegionSecurityPolicyRuleRateLimitOptionsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> RegionSecurityPolicyRule: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def match(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionSecurityPolicyRuleMatch]]: ...
    @_builtins.property
    @pulumi.getter(name="networkMatch")
    def network_match(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionSecurityPolicyRuleNetworkMatch]]: ...
    @_builtins.property
    @pulumi.getter(name="preconfiguredWafConfig")
    def preconfigured_waf_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RegionSecurityPolicyRulePreconfiguredWafConfig]
    ]: ...
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
    ) -> pulumi.Output[Optional[outputs.RegionSecurityPolicyRuleRateLimitOptions]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> pulumi.Output[_builtins.str]: ...
