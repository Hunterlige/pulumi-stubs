import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["V2modelsIntentArgs", "V2modelsIntent"]

@pulumi.input_type
class V2modelsIntentArgs:
    def __init__(
        __self__,
        *,
        bot_id: pulumi.Input[_builtins.str],
        bot_version: pulumi.Input[_builtins.str],
        locale_id: pulumi.Input[_builtins.str],
        closing_setting: Optional[pulumi.Input[V2modelsIntentClosingSettingArgs]] = ...,
        confirmation_setting: Optional[
            pulumi.Input[V2modelsIntentConfirmationSettingArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dialog_code_hook: Optional[
            pulumi.Input[V2modelsIntentDialogCodeHookArgs]
        ] = ...,
        fulfillment_code_hook: Optional[
            pulumi.Input[V2modelsIntentFulfillmentCodeHookArgs]
        ] = ...,
        initial_response_setting: Optional[
            pulumi.Input[V2modelsIntentInitialResponseSettingArgs]
        ] = ...,
        input_contexts: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentInputContextArgs]]]
        ] = ...,
        kendra_configuration: Optional[
            pulumi.Input[V2modelsIntentKendraConfigurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_contexts: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentOutputContextArgs]]]
        ] = ...,
        parent_intent_signature: Optional[pulumi.Input[_builtins.str]] = ...,
        qna_intent_configuration: Optional[
            pulumi.Input[V2modelsIntentQnaIntentConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_utterances: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSampleUtteranceArgs]]]
        ] = ...,
        slot_priorities: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSlotPriorityArgs]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[V2modelsIntentTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Input[_builtins.str]: ...
    @bot_id.setter
    def bot_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Input[_builtins.str]: ...
    @bot_version.setter
    def bot_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> pulumi.Input[_builtins.str]: ...
    @locale_id.setter
    def locale_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="closingSetting")
    def closing_setting(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentClosingSettingArgs]]: ...
    @closing_setting.setter
    def closing_setting(
        self, value: Optional[pulumi.Input[V2modelsIntentClosingSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="confirmationSetting")
    def confirmation_setting(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentConfirmationSettingArgs]]: ...
    @confirmation_setting.setter
    def confirmation_setting(
        self, value: Optional[pulumi.Input[V2modelsIntentConfirmationSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dialogCodeHook")
    def dialog_code_hook(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentDialogCodeHookArgs]]: ...
    @dialog_code_hook.setter
    def dialog_code_hook(
        self, value: Optional[pulumi.Input[V2modelsIntentDialogCodeHookArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fulfillmentCodeHook")
    def fulfillment_code_hook(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentFulfillmentCodeHookArgs]]: ...
    @fulfillment_code_hook.setter
    def fulfillment_code_hook(
        self, value: Optional[pulumi.Input[V2modelsIntentFulfillmentCodeHookArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialResponseSetting")
    def initial_response_setting(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentInitialResponseSettingArgs]]: ...
    @initial_response_setting.setter
    def initial_response_setting(
        self, value: Optional[pulumi.Input[V2modelsIntentInitialResponseSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputContexts")
    def input_contexts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsIntentInputContextArgs]]]
    ]: ...
    @input_contexts.setter
    def input_contexts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentInputContextArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="kendraConfiguration")
    def kendra_configuration(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentKendraConfigurationArgs]]: ...
    @kendra_configuration.setter
    def kendra_configuration(
        self, value: Optional[pulumi.Input[V2modelsIntentKendraConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputContexts")
    def output_contexts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsIntentOutputContextArgs]]]
    ]: ...
    @output_contexts.setter
    def output_contexts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentOutputContextArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parentIntentSignature")
    def parent_intent_signature(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_intent_signature.setter
    def parent_intent_signature(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="qnaIntentConfiguration")
    def qna_intent_configuration(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentQnaIntentConfigurationArgs]]: ...
    @qna_intent_configuration.setter
    def qna_intent_configuration(
        self, value: Optional[pulumi.Input[V2modelsIntentQnaIntentConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleUtterances")
    def sample_utterances(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSampleUtteranceArgs]]]
    ]: ...
    @sample_utterances.setter
    def sample_utterances(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSampleUtteranceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="slotPriorities")
    def slot_priorities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSlotPriorityArgs]]]
    ]: ...
    @slot_priorities.setter
    def slot_priorities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSlotPriorityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsIntentTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsIntentTimeoutsArgs]]): ...

@pulumi.input_type
class _V2modelsIntentState:
    def __init__(
        __self__,
        *,
        bot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        closing_setting: Optional[pulumi.Input[V2modelsIntentClosingSettingArgs]] = ...,
        confirmation_setting: Optional[
            pulumi.Input[V2modelsIntentConfirmationSettingArgs]
        ] = ...,
        creation_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dialog_code_hook: Optional[
            pulumi.Input[V2modelsIntentDialogCodeHookArgs]
        ] = ...,
        fulfillment_code_hook: Optional[
            pulumi.Input[V2modelsIntentFulfillmentCodeHookArgs]
        ] = ...,
        initial_response_setting: Optional[
            pulumi.Input[V2modelsIntentInitialResponseSettingArgs]
        ] = ...,
        input_contexts: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentInputContextArgs]]]
        ] = ...,
        intent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kendra_configuration: Optional[
            pulumi.Input[V2modelsIntentKendraConfigurationArgs]
        ] = ...,
        last_updated_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
        locale_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_contexts: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentOutputContextArgs]]]
        ] = ...,
        parent_intent_signature: Optional[pulumi.Input[_builtins.str]] = ...,
        qna_intent_configuration: Optional[
            pulumi.Input[V2modelsIntentQnaIntentConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_utterances: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSampleUtteranceArgs]]]
        ] = ...,
        slot_priorities: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSlotPriorityArgs]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[V2modelsIntentTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bot_id.setter
    def bot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bot_version.setter
    def bot_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="closingSetting")
    def closing_setting(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentClosingSettingArgs]]: ...
    @closing_setting.setter
    def closing_setting(
        self, value: Optional[pulumi.Input[V2modelsIntentClosingSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="confirmationSetting")
    def confirmation_setting(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentConfirmationSettingArgs]]: ...
    @confirmation_setting.setter
    def confirmation_setting(
        self, value: Optional[pulumi.Input[V2modelsIntentConfirmationSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationDateTime")
    def creation_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_date_time.setter
    def creation_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dialogCodeHook")
    def dialog_code_hook(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentDialogCodeHookArgs]]: ...
    @dialog_code_hook.setter
    def dialog_code_hook(
        self, value: Optional[pulumi.Input[V2modelsIntentDialogCodeHookArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fulfillmentCodeHook")
    def fulfillment_code_hook(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentFulfillmentCodeHookArgs]]: ...
    @fulfillment_code_hook.setter
    def fulfillment_code_hook(
        self, value: Optional[pulumi.Input[V2modelsIntentFulfillmentCodeHookArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialResponseSetting")
    def initial_response_setting(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentInitialResponseSettingArgs]]: ...
    @initial_response_setting.setter
    def initial_response_setting(
        self, value: Optional[pulumi.Input[V2modelsIntentInitialResponseSettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputContexts")
    def input_contexts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsIntentInputContextArgs]]]
    ]: ...
    @input_contexts.setter
    def input_contexts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentInputContextArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="intentId")
    def intent_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @intent_id.setter
    def intent_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kendraConfiguration")
    def kendra_configuration(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentKendraConfigurationArgs]]: ...
    @kendra_configuration.setter
    def kendra_configuration(
        self, value: Optional[pulumi.Input[V2modelsIntentKendraConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDateTime")
    def last_updated_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_date_time.setter
    def last_updated_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locale_id.setter
    def locale_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputContexts")
    def output_contexts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsIntentOutputContextArgs]]]
    ]: ...
    @output_contexts.setter
    def output_contexts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentOutputContextArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="parentIntentSignature")
    def parent_intent_signature(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_intent_signature.setter
    def parent_intent_signature(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="qnaIntentConfiguration")
    def qna_intent_configuration(
        self,
    ) -> Optional[pulumi.Input[V2modelsIntentQnaIntentConfigurationArgs]]: ...
    @qna_intent_configuration.setter
    def qna_intent_configuration(
        self, value: Optional[pulumi.Input[V2modelsIntentQnaIntentConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleUtterances")
    def sample_utterances(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSampleUtteranceArgs]]]
    ]: ...
    @sample_utterances.setter
    def sample_utterances(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSampleUtteranceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="slotPriorities")
    def slot_priorities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSlotPriorityArgs]]]
    ]: ...
    @slot_priorities.setter
    def slot_priorities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsIntentSlotPriorityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsIntentTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsIntentTimeoutsArgs]]): ...

@pulumi.type_token("aws:lex/v2modelsIntent:V2modelsIntent")
class V2modelsIntent(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        closing_setting: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentClosingSettingArgs,
                    V2modelsIntentClosingSettingArgsDict,
                ]
            ]
        ] = ...,
        confirmation_setting: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentConfirmationSettingArgs,
                    V2modelsIntentConfirmationSettingArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dialog_code_hook: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentDialogCodeHookArgs,
                    V2modelsIntentDialogCodeHookArgsDict,
                ]
            ]
        ] = ...,
        fulfillment_code_hook: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentFulfillmentCodeHookArgs,
                    V2modelsIntentFulfillmentCodeHookArgsDict,
                ]
            ]
        ] = ...,
        initial_response_setting: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentInitialResponseSettingArgs,
                    V2modelsIntentInitialResponseSettingArgsDict,
                ]
            ]
        ] = ...,
        input_contexts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsIntentInputContextArgs,
                            V2modelsIntentInputContextArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        kendra_configuration: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentKendraConfigurationArgs,
                    V2modelsIntentKendraConfigurationArgsDict,
                ]
            ]
        ] = ...,
        locale_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_contexts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsIntentOutputContextArgs,
                            V2modelsIntentOutputContextArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        parent_intent_signature: Optional[pulumi.Input[_builtins.str]] = ...,
        qna_intent_configuration: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentQnaIntentConfigurationArgs,
                    V2modelsIntentQnaIntentConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_utterances: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsIntentSampleUtteranceArgs,
                            V2modelsIntentSampleUtteranceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        slot_priorities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsIntentSlotPriorityArgs,
                            V2modelsIntentSlotPriorityArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[V2modelsIntentTimeoutsArgs, V2modelsIntentTimeoutsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: V2modelsIntentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        closing_setting: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentClosingSettingArgs,
                    V2modelsIntentClosingSettingArgsDict,
                ]
            ]
        ] = ...,
        confirmation_setting: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentConfirmationSettingArgs,
                    V2modelsIntentConfirmationSettingArgsDict,
                ]
            ]
        ] = ...,
        creation_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dialog_code_hook: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentDialogCodeHookArgs,
                    V2modelsIntentDialogCodeHookArgsDict,
                ]
            ]
        ] = ...,
        fulfillment_code_hook: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentFulfillmentCodeHookArgs,
                    V2modelsIntentFulfillmentCodeHookArgsDict,
                ]
            ]
        ] = ...,
        initial_response_setting: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentInitialResponseSettingArgs,
                    V2modelsIntentInitialResponseSettingArgsDict,
                ]
            ]
        ] = ...,
        input_contexts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsIntentInputContextArgs,
                            V2modelsIntentInputContextArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        intent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        kendra_configuration: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentKendraConfigurationArgs,
                    V2modelsIntentKendraConfigurationArgsDict,
                ]
            ]
        ] = ...,
        last_updated_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
        locale_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_contexts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsIntentOutputContextArgs,
                            V2modelsIntentOutputContextArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        parent_intent_signature: Optional[pulumi.Input[_builtins.str]] = ...,
        qna_intent_configuration: Optional[
            pulumi.Input[
                Union[
                    V2modelsIntentQnaIntentConfigurationArgs,
                    V2modelsIntentQnaIntentConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        sample_utterances: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsIntentSampleUtteranceArgs,
                            V2modelsIntentSampleUtteranceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        slot_priorities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsIntentSlotPriorityArgs,
                            V2modelsIntentSlotPriorityArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[V2modelsIntentTimeoutsArgs, V2modelsIntentTimeoutsArgsDict]
            ]
        ] = ...,
    ) -> V2modelsIntent: ...
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="closingSetting")
    def closing_setting(
        self,
    ) -> pulumi.Output[Optional[outputs.V2modelsIntentClosingSetting]]: ...
    @_builtins.property
    @pulumi.getter(name="confirmationSetting")
    def confirmation_setting(
        self,
    ) -> pulumi.Output[Optional[outputs.V2modelsIntentConfirmationSetting]]: ...
    @_builtins.property
    @pulumi.getter(name="creationDateTime")
    def creation_date_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dialogCodeHook")
    def dialog_code_hook(
        self,
    ) -> pulumi.Output[Optional[outputs.V2modelsIntentDialogCodeHook]]: ...
    @_builtins.property
    @pulumi.getter(name="fulfillmentCodeHook")
    def fulfillment_code_hook(
        self,
    ) -> pulumi.Output[Optional[outputs.V2modelsIntentFulfillmentCodeHook]]: ...
    @_builtins.property
    @pulumi.getter(name="initialResponseSetting")
    def initial_response_setting(
        self,
    ) -> pulumi.Output[Optional[outputs.V2modelsIntentInitialResponseSetting]]: ...
    @_builtins.property
    @pulumi.getter(name="inputContexts")
    def input_contexts(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.V2modelsIntentInputContext]]]: ...
    @_builtins.property
    @pulumi.getter(name="intentId")
    def intent_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kendraConfiguration")
    def kendra_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.V2modelsIntentKendraConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDateTime")
    def last_updated_date_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputContexts")
    def output_contexts(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.V2modelsIntentOutputContext]]]: ...
    @_builtins.property
    @pulumi.getter(name="parentIntentSignature")
    def parent_intent_signature(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="qnaIntentConfiguration")
    def qna_intent_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.V2modelsIntentQnaIntentConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleUtterances")
    def sample_utterances(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.V2modelsIntentSampleUtterance]]]: ...
    @_builtins.property
    @pulumi.getter(name="slotPriorities")
    def slot_priorities(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.V2modelsIntentSlotPriority]]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.V2modelsIntentTimeouts]]: ...
