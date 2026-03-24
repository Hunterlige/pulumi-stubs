import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SecurityPolicyArgs", "SecurityPolicy"]

@pulumi.input_type
class SecurityPolicyArgs:
    def __init__(
        __self__,
        *,
        adaptive_protection_config: Optional[
            pulumi.Input[SecurityPolicyAdaptiveProtectionConfigArgs]
        ] = ...,
        advanced_options_config: Optional[
            pulumi.Input[SecurityPolicyAdvancedOptionsConfigArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recaptcha_options_config: Optional[
            pulumi.Input[SecurityPolicyRecaptchaOptionsConfigArgs]
        ] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[SecurityPolicyRuleArgs]]]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adaptiveProtectionConfig")
    def adaptive_protection_config(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyAdaptiveProtectionConfigArgs]]: ...
    @adaptive_protection_config.setter
    def adaptive_protection_config(
        self, value: Optional[pulumi.Input[SecurityPolicyAdaptiveProtectionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="advancedOptionsConfig")
    def advanced_options_config(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyAdvancedOptionsConfigArgs]]: ...
    @advanced_options_config.setter
    def advanced_options_config(
        self, value: Optional[pulumi.Input[SecurityPolicyAdvancedOptionsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recaptchaOptionsConfig")
    def recaptcha_options_config(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRecaptchaOptionsConfigArgs]]: ...
    @recaptcha_options_config.setter
    def recaptcha_options_config(
        self, value: Optional[pulumi.Input[SecurityPolicyRecaptchaOptionsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityPolicyRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityPolicyRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SecurityPolicyState:
    def __init__(
        __self__,
        *,
        adaptive_protection_config: Optional[
            pulumi.Input[SecurityPolicyAdaptiveProtectionConfigArgs]
        ] = ...,
        advanced_options_config: Optional[
            pulumi.Input[SecurityPolicyAdvancedOptionsConfigArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        recaptcha_options_config: Optional[
            pulumi.Input[SecurityPolicyRecaptchaOptionsConfigArgs]
        ] = ...,
        rules: Optional[
            pulumi.Input[Sequence[pulumi.Input[SecurityPolicyRuleArgs]]]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adaptiveProtectionConfig")
    def adaptive_protection_config(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyAdaptiveProtectionConfigArgs]]: ...
    @adaptive_protection_config.setter
    def adaptive_protection_config(
        self, value: Optional[pulumi.Input[SecurityPolicyAdaptiveProtectionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="advancedOptionsConfig")
    def advanced_options_config(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyAdvancedOptionsConfigArgs]]: ...
    @advanced_options_config.setter
    def advanced_options_config(
        self, value: Optional[pulumi.Input[SecurityPolicyAdvancedOptionsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label_fingerprint.setter
    def label_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="recaptchaOptionsConfig")
    def recaptcha_options_config(
        self,
    ) -> Optional[pulumi.Input[SecurityPolicyRecaptchaOptionsConfigArgs]]: ...
    @recaptcha_options_config.setter
    def recaptcha_options_config(
        self, value: Optional[pulumi.Input[SecurityPolicyRecaptchaOptionsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SecurityPolicyRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SecurityPolicyRuleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:compute/securityPolicy:SecurityPolicy")
class SecurityPolicy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        adaptive_protection_config: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyAdaptiveProtectionConfigArgs,
                    SecurityPolicyAdaptiveProtectionConfigArgsDict,
                ]
            ]
        ] = ...,
        advanced_options_config: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyAdvancedOptionsConfigArgs,
                    SecurityPolicyAdvancedOptionsConfigArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        recaptcha_options_config: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRecaptchaOptionsConfigArgs,
                    SecurityPolicyRecaptchaOptionsConfigArgsDict,
                ]
            ]
        ] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[SecurityPolicyRuleArgs, SecurityPolicyRuleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[SecurityPolicyArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        adaptive_protection_config: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyAdaptiveProtectionConfigArgs,
                    SecurityPolicyAdaptiveProtectionConfigArgsDict,
                ]
            ]
        ] = ...,
        advanced_options_config: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyAdvancedOptionsConfigArgs,
                    SecurityPolicyAdvancedOptionsConfigArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        label_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        recaptcha_options_config: Optional[
            pulumi.Input[
                Union[
                    SecurityPolicyRecaptchaOptionsConfigArgs,
                    SecurityPolicyRecaptchaOptionsConfigArgsDict,
                ]
            ]
        ] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[SecurityPolicyRuleArgs, SecurityPolicyRuleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SecurityPolicy: ...
    @_builtins.property
    @pulumi.getter(name="adaptiveProtectionConfig")
    def adaptive_protection_config(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityPolicyAdaptiveProtectionConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="advancedOptionsConfig")
    def advanced_options_config(
        self,
    ) -> pulumi.Output[outputs.SecurityPolicyAdvancedOptionsConfig]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="labelFingerprint")
    def label_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="recaptchaOptionsConfig")
    def recaptcha_options_config(
        self,
    ) -> pulumi.Output[Optional[outputs.SecurityPolicyRecaptchaOptionsConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence[outputs.SecurityPolicyRule]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
