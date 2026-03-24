import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["GuardrailArgs", "Guardrail"]

@pulumi.input_type
class GuardrailArgs:
    def __init__(
        __self__,
        *,
        blocked_input_messaging: pulumi.Input[_builtins.str],
        blocked_outputs_messaging: pulumi.Input[_builtins.str],
        content_policy_config: Optional[
            pulumi.Input[GuardrailContentPolicyConfigArgs]
        ] = ...,
        contextual_grounding_policy_config: Optional[
            pulumi.Input[GuardrailContextualGroundingPolicyConfigArgs]
        ] = ...,
        cross_region_config: Optional[
            pulumi.Input[GuardrailCrossRegionConfigArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitive_information_policy_config: Optional[
            pulumi.Input[GuardrailSensitiveInformationPolicyConfigArgs]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[GuardrailTimeoutsArgs]] = ...,
        topic_policy_config: Optional[
            pulumi.Input[GuardrailTopicPolicyConfigArgs]
        ] = ...,
        word_policy_config: Optional[pulumi.Input[GuardrailWordPolicyConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockedInputMessaging")
    def blocked_input_messaging(self) -> pulumi.Input[_builtins.str]: ...
    @blocked_input_messaging.setter
    def blocked_input_messaging(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="blockedOutputsMessaging")
    def blocked_outputs_messaging(self) -> pulumi.Input[_builtins.str]: ...
    @blocked_outputs_messaging.setter
    def blocked_outputs_messaging(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contentPolicyConfig")
    def content_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailContentPolicyConfigArgs]]: ...
    @content_policy_config.setter
    def content_policy_config(
        self, value: Optional[pulumi.Input[GuardrailContentPolicyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contextualGroundingPolicyConfig")
    def contextual_grounding_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailContextualGroundingPolicyConfigArgs]]: ...
    @contextual_grounding_policy_config.setter
    def contextual_grounding_policy_config(
        self,
        value: Optional[pulumi.Input[GuardrailContextualGroundingPolicyConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="crossRegionConfig")
    def cross_region_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailCrossRegionConfigArgs]]: ...
    @cross_region_config.setter
    def cross_region_config(
        self, value: Optional[pulumi.Input[GuardrailCrossRegionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sensitiveInformationPolicyConfig")
    def sensitive_information_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailSensitiveInformationPolicyConfigArgs]]: ...
    @sensitive_information_policy_config.setter
    def sensitive_information_policy_config(
        self,
        value: Optional[pulumi.Input[GuardrailSensitiveInformationPolicyConfigArgs]],
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[GuardrailTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[GuardrailTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="topicPolicyConfig")
    def topic_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailTopicPolicyConfigArgs]]: ...
    @topic_policy_config.setter
    def topic_policy_config(
        self, value: Optional[pulumi.Input[GuardrailTopicPolicyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="wordPolicyConfig")
    def word_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailWordPolicyConfigArgs]]: ...
    @word_policy_config.setter
    def word_policy_config(
        self, value: Optional[pulumi.Input[GuardrailWordPolicyConfigArgs]]
    ): ...

@pulumi.input_type
class _GuardrailState:
    def __init__(
        __self__,
        *,
        blocked_input_messaging: Optional[pulumi.Input[_builtins.str]] = ...,
        blocked_outputs_messaging: Optional[pulumi.Input[_builtins.str]] = ...,
        content_policy_config: Optional[
            pulumi.Input[GuardrailContentPolicyConfigArgs]
        ] = ...,
        contextual_grounding_policy_config: Optional[
            pulumi.Input[GuardrailContextualGroundingPolicyConfigArgs]
        ] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_region_config: Optional[
            pulumi.Input[GuardrailCrossRegionConfigArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrail_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrail_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitive_information_policy_config: Optional[
            pulumi.Input[GuardrailSensitiveInformationPolicyConfigArgs]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[GuardrailTimeoutsArgs]] = ...,
        topic_policy_config: Optional[
            pulumi.Input[GuardrailTopicPolicyConfigArgs]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        word_policy_config: Optional[pulumi.Input[GuardrailWordPolicyConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="blockedInputMessaging")
    def blocked_input_messaging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blocked_input_messaging.setter
    def blocked_input_messaging(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="blockedOutputsMessaging")
    def blocked_outputs_messaging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @blocked_outputs_messaging.setter
    def blocked_outputs_messaging(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contentPolicyConfig")
    def content_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailContentPolicyConfigArgs]]: ...
    @content_policy_config.setter
    def content_policy_config(
        self, value: Optional[pulumi.Input[GuardrailContentPolicyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contextualGroundingPolicyConfig")
    def contextual_grounding_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailContextualGroundingPolicyConfigArgs]]: ...
    @contextual_grounding_policy_config.setter
    def contextual_grounding_policy_config(
        self,
        value: Optional[pulumi.Input[GuardrailContextualGroundingPolicyConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="crossRegionConfig")
    def cross_region_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailCrossRegionConfigArgs]]: ...
    @cross_region_config.setter
    def cross_region_config(
        self, value: Optional[pulumi.Input[GuardrailCrossRegionConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="guardrailArn")
    def guardrail_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @guardrail_arn.setter
    def guardrail_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="guardrailId")
    def guardrail_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @guardrail_id.setter
    def guardrail_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sensitiveInformationPolicyConfig")
    def sensitive_information_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailSensitiveInformationPolicyConfigArgs]]: ...
    @sensitive_information_policy_config.setter
    def sensitive_information_policy_config(
        self,
        value: Optional[pulumi.Input[GuardrailSensitiveInformationPolicyConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[GuardrailTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[GuardrailTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="topicPolicyConfig")
    def topic_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailTopicPolicyConfigArgs]]: ...
    @topic_policy_config.setter
    def topic_policy_config(
        self, value: Optional[pulumi.Input[GuardrailTopicPolicyConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="wordPolicyConfig")
    def word_policy_config(
        self,
    ) -> Optional[pulumi.Input[GuardrailWordPolicyConfigArgs]]: ...
    @word_policy_config.setter
    def word_policy_config(
        self, value: Optional[pulumi.Input[GuardrailWordPolicyConfigArgs]]
    ): ...

@pulumi.type_token("aws:bedrock/guardrail:Guardrail")
class Guardrail(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        blocked_input_messaging: Optional[pulumi.Input[_builtins.str]] = ...,
        blocked_outputs_messaging: Optional[pulumi.Input[_builtins.str]] = ...,
        content_policy_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailContentPolicyConfigArgs,
                    GuardrailContentPolicyConfigArgsDict,
                ]
            ]
        ] = ...,
        contextual_grounding_policy_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailContextualGroundingPolicyConfigArgs,
                    GuardrailContextualGroundingPolicyConfigArgsDict,
                ]
            ]
        ] = ...,
        cross_region_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailCrossRegionConfigArgs, GuardrailCrossRegionConfigArgsDict
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitive_information_policy_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailSensitiveInformationPolicyConfigArgs,
                    GuardrailSensitiveInformationPolicyConfigArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[Union[GuardrailTimeoutsArgs, GuardrailTimeoutsArgsDict]]
        ] = ...,
        topic_policy_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailTopicPolicyConfigArgs, GuardrailTopicPolicyConfigArgsDict
                ]
            ]
        ] = ...,
        word_policy_config: Optional[
            pulumi.Input[
                Union[GuardrailWordPolicyConfigArgs, GuardrailWordPolicyConfigArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: GuardrailArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        blocked_input_messaging: Optional[pulumi.Input[_builtins.str]] = ...,
        blocked_outputs_messaging: Optional[pulumi.Input[_builtins.str]] = ...,
        content_policy_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailContentPolicyConfigArgs,
                    GuardrailContentPolicyConfigArgsDict,
                ]
            ]
        ] = ...,
        contextual_grounding_policy_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailContextualGroundingPolicyConfigArgs,
                    GuardrailContextualGroundingPolicyConfigArgsDict,
                ]
            ]
        ] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        cross_region_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailCrossRegionConfigArgs, GuardrailCrossRegionConfigArgsDict
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrail_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrail_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitive_information_policy_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailSensitiveInformationPolicyConfigArgs,
                    GuardrailSensitiveInformationPolicyConfigArgsDict,
                ]
            ]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[GuardrailTimeoutsArgs, GuardrailTimeoutsArgsDict]]
        ] = ...,
        topic_policy_config: Optional[
            pulumi.Input[
                Union[
                    GuardrailTopicPolicyConfigArgs, GuardrailTopicPolicyConfigArgsDict
                ]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
        word_policy_config: Optional[
            pulumi.Input[
                Union[GuardrailWordPolicyConfigArgs, GuardrailWordPolicyConfigArgsDict]
            ]
        ] = ...,
    ) -> Guardrail: ...
    @_builtins.property
    @pulumi.getter(name="blockedInputMessaging")
    def blocked_input_messaging(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="blockedOutputsMessaging")
    def blocked_outputs_messaging(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentPolicyConfig")
    def content_policy_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GuardrailContentPolicyConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="contextualGroundingPolicyConfig")
    def contextual_grounding_policy_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GuardrailContextualGroundingPolicyConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="crossRegionConfig")
    def cross_region_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GuardrailCrossRegionConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="guardrailArn")
    def guardrail_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="guardrailId")
    def guardrail_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sensitiveInformationPolicyConfig")
    def sensitive_information_policy_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GuardrailSensitiveInformationPolicyConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.GuardrailTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="topicPolicyConfig")
    def topic_policy_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GuardrailTopicPolicyConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="wordPolicyConfig")
    def word_policy_config(
        self,
    ) -> pulumi.Output[Optional[outputs.GuardrailWordPolicyConfig]]: ...
