import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WebAclArgs", "WebAcl"]

@pulumi.input_type
class WebAclArgs:
    def __init__(
        __self__,
        *,
        default_action: pulumi.Input[WebAclDefaultActionArgs],
        scope: pulumi.Input[_builtins.str],
        visibility_config: pulumi.Input[WebAclVisibilityConfigArgs],
        association_config: Optional[pulumi.Input[WebAclAssociationConfigArgs]] = ...,
        captcha_config: Optional[pulumi.Input[WebAclCaptchaConfigArgs]] = ...,
        challenge_config: Optional[pulumi.Input[WebAclChallengeConfigArgs]] = ...,
        custom_response_bodies: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebAclCustomResponseBodyArgs]]]
        ] = ...,
        data_protection_config: Optional[
            pulumi.Input[WebAclDataProtectionConfigArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_json: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        token_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Input[WebAclDefaultActionArgs]: ...
    @default_action.setter
    def default_action(self, value: pulumi.Input[WebAclDefaultActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> pulumi.Input[WebAclVisibilityConfigArgs]: ...
    @visibility_config.setter
    def visibility_config(self, value: pulumi.Input[WebAclVisibilityConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="associationConfig")
    def association_config(
        self,
    ) -> Optional[pulumi.Input[WebAclAssociationConfigArgs]]: ...
    @association_config.setter
    def association_config(
        self, value: Optional[pulumi.Input[WebAclAssociationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="captchaConfig")
    def captcha_config(self) -> Optional[pulumi.Input[WebAclCaptchaConfigArgs]]: ...
    @captcha_config.setter
    def captcha_config(
        self, value: Optional[pulumi.Input[WebAclCaptchaConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="challengeConfig")
    def challenge_config(self) -> Optional[pulumi.Input[WebAclChallengeConfigArgs]]: ...
    @challenge_config.setter
    def challenge_config(
        self, value: Optional[pulumi.Input[WebAclChallengeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebAclCustomResponseBodyArgs]]]
    ]: ...
    @custom_response_bodies.setter
    def custom_response_bodies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebAclCustomResponseBodyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataProtectionConfig")
    def data_protection_config(
        self,
    ) -> Optional[pulumi.Input[WebAclDataProtectionConfigArgs]]: ...
    @data_protection_config.setter
    def data_protection_config(
        self, value: Optional[pulumi.Input[WebAclDataProtectionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleJson")
    def rule_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_json.setter
    def rule_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenDomains")
    def token_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @token_domains.setter
    def token_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _WebAclState:
    def __init__(
        __self__,
        *,
        application_integration_url: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_config: Optional[pulumi.Input[WebAclAssociationConfigArgs]] = ...,
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        captcha_config: Optional[pulumi.Input[WebAclCaptchaConfigArgs]] = ...,
        challenge_config: Optional[pulumi.Input[WebAclChallengeConfigArgs]] = ...,
        custom_response_bodies: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebAclCustomResponseBodyArgs]]]
        ] = ...,
        data_protection_config: Optional[
            pulumi.Input[WebAclDataProtectionConfigArgs]
        ] = ...,
        default_action: Optional[pulumi.Input[WebAclDefaultActionArgs]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        lock_token: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_json: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        token_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        visibility_config: Optional[pulumi.Input[WebAclVisibilityConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationIntegrationUrl")
    def application_integration_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_integration_url.setter
    def application_integration_url(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associationConfig")
    def association_config(
        self,
    ) -> Optional[pulumi.Input[WebAclAssociationConfigArgs]]: ...
    @association_config.setter
    def association_config(
        self, value: Optional[pulumi.Input[WebAclAssociationConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="captchaConfig")
    def captcha_config(self) -> Optional[pulumi.Input[WebAclCaptchaConfigArgs]]: ...
    @captcha_config.setter
    def captcha_config(
        self, value: Optional[pulumi.Input[WebAclCaptchaConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="challengeConfig")
    def challenge_config(self) -> Optional[pulumi.Input[WebAclChallengeConfigArgs]]: ...
    @challenge_config.setter
    def challenge_config(
        self, value: Optional[pulumi.Input[WebAclChallengeConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebAclCustomResponseBodyArgs]]]
    ]: ...
    @custom_response_bodies.setter
    def custom_response_bodies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebAclCustomResponseBodyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataProtectionConfig")
    def data_protection_config(
        self,
    ) -> Optional[pulumi.Input[WebAclDataProtectionConfigArgs]]: ...
    @data_protection_config.setter
    def data_protection_config(
        self, value: Optional[pulumi.Input[WebAclDataProtectionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[WebAclDefaultActionArgs]]: ...
    @default_action.setter
    def default_action(
        self, value: Optional[pulumi.Input[WebAclDefaultActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lockToken")
    def lock_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lock_token.setter
    def lock_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleJson")
    def rule_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rule_json.setter
    def rule_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]]: ...
    @rules.setter
    def rules(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebAclRuleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenDomains")
    def token_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @token_domains.setter
    def token_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(
        self,
    ) -> Optional[pulumi.Input[WebAclVisibilityConfigArgs]]: ...
    @visibility_config.setter
    def visibility_config(
        self, value: Optional[pulumi.Input[WebAclVisibilityConfigArgs]]
    ): ...

@pulumi.type_token("aws:wafv2/webAcl:WebAcl")
class WebAcl(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        association_config: Optional[
            pulumi.Input[
                Union[WebAclAssociationConfigArgs, WebAclAssociationConfigArgsDict]
            ]
        ] = ...,
        captcha_config: Optional[
            pulumi.Input[Union[WebAclCaptchaConfigArgs, WebAclCaptchaConfigArgsDict]]
        ] = ...,
        challenge_config: Optional[
            pulumi.Input[
                Union[WebAclChallengeConfigArgs, WebAclChallengeConfigArgsDict]
            ]
        ] = ...,
        custom_response_bodies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WebAclCustomResponseBodyArgs,
                            WebAclCustomResponseBodyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        data_protection_config: Optional[
            pulumi.Input[
                Union[
                    WebAclDataProtectionConfigArgs, WebAclDataProtectionConfigArgsDict
                ]
            ]
        ] = ...,
        default_action: Optional[
            pulumi.Input[Union[WebAclDefaultActionArgs, WebAclDefaultActionArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_json: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[WebAclRuleArgs, WebAclRuleArgsDict]]]
            ]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        token_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        visibility_config: Optional[
            pulumi.Input[
                Union[WebAclVisibilityConfigArgs, WebAclVisibilityConfigArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WebAclArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        application_integration_url: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_config: Optional[
            pulumi.Input[
                Union[WebAclAssociationConfigArgs, WebAclAssociationConfigArgsDict]
            ]
        ] = ...,
        capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        captcha_config: Optional[
            pulumi.Input[Union[WebAclCaptchaConfigArgs, WebAclCaptchaConfigArgsDict]]
        ] = ...,
        challenge_config: Optional[
            pulumi.Input[
                Union[WebAclChallengeConfigArgs, WebAclChallengeConfigArgsDict]
            ]
        ] = ...,
        custom_response_bodies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WebAclCustomResponseBodyArgs,
                            WebAclCustomResponseBodyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        data_protection_config: Optional[
            pulumi.Input[
                Union[
                    WebAclDataProtectionConfigArgs, WebAclDataProtectionConfigArgsDict
                ]
            ]
        ] = ...,
        default_action: Optional[
            pulumi.Input[Union[WebAclDefaultActionArgs, WebAclDefaultActionArgsDict]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        lock_token: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_json: Optional[pulumi.Input[_builtins.str]] = ...,
        rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[WebAclRuleArgs, WebAclRuleArgsDict]]]
            ]
        ] = ...,
        scope: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        token_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        visibility_config: Optional[
            pulumi.Input[
                Union[WebAclVisibilityConfigArgs, WebAclVisibilityConfigArgsDict]
            ]
        ] = ...,
    ) -> WebAcl: ...
    @_builtins.property
    @pulumi.getter(name="applicationIntegrationUrl")
    def application_integration_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associationConfig")
    def association_config(
        self,
    ) -> pulumi.Output[Optional[outputs.WebAclAssociationConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="captchaConfig")
    def captcha_config(
        self,
    ) -> pulumi.Output[Optional[outputs.WebAclCaptchaConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="challengeConfig")
    def challenge_config(
        self,
    ) -> pulumi.Output[Optional[outputs.WebAclChallengeConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.WebAclCustomResponseBody]]]: ...
    @_builtins.property
    @pulumi.getter(name="dataProtectionConfig")
    def data_protection_config(
        self,
    ) -> pulumi.Output[Optional[outputs.WebAclDataProtectionConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Output[outputs.WebAclDefaultAction]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lockToken")
    def lock_token(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleJson")
    def rule_json(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence[outputs.WebAclRule]]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tokenDomains")
    def token_domains(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> pulumi.Output[outputs.WebAclVisibilityConfig]: ...
