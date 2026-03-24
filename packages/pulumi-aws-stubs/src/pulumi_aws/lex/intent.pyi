import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IntentArgs", "Intent"]

@pulumi.input_type
class IntentArgs:
    def __init__(
        __self__,
        *,
        fulfillment_activity: pulumi.Input[IntentFulfillmentActivityArgs],
        conclusion_statement: Optional[
            pulumi.Input[IntentConclusionStatementArgs]
        ] = ...,
        confirmation_prompt: Optional[pulumi.Input[IntentConfirmationPromptArgs]] = ...,
        create_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dialog_code_hook: Optional[pulumi.Input[IntentDialogCodeHookArgs]] = ...,
        follow_up_prompt: Optional[pulumi.Input[IntentFollowUpPromptArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_intent_signature: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rejection_statement: Optional[pulumi.Input[IntentRejectionStatementArgs]] = ...,
        sample_utterances: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        slots: Optional[pulumi.Input[Sequence[pulumi.Input[IntentSlotArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fulfillmentActivity")
    def fulfillment_activity(self) -> pulumi.Input[IntentFulfillmentActivityArgs]: ...
    @fulfillment_activity.setter
    def fulfillment_activity(
        self, value: pulumi.Input[IntentFulfillmentActivityArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="conclusionStatement")
    def conclusion_statement(
        self,
    ) -> Optional[pulumi.Input[IntentConclusionStatementArgs]]: ...
    @conclusion_statement.setter
    def conclusion_statement(
        self, value: Optional[pulumi.Input[IntentConclusionStatementArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="confirmationPrompt")
    def confirmation_prompt(
        self,
    ) -> Optional[pulumi.Input[IntentConfirmationPromptArgs]]: ...
    @confirmation_prompt.setter
    def confirmation_prompt(
        self, value: Optional[pulumi.Input[IntentConfirmationPromptArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createVersion")
    def create_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_version.setter
    def create_version(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dialogCodeHook")
    def dialog_code_hook(self) -> Optional[pulumi.Input[IntentDialogCodeHookArgs]]: ...
    @dialog_code_hook.setter
    def dialog_code_hook(
        self, value: Optional[pulumi.Input[IntentDialogCodeHookArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="followUpPrompt")
    def follow_up_prompt(self) -> Optional[pulumi.Input[IntentFollowUpPromptArgs]]: ...
    @follow_up_prompt.setter
    def follow_up_prompt(
        self, value: Optional[pulumi.Input[IntentFollowUpPromptArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentIntentSignature")
    def parent_intent_signature(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_intent_signature.setter
    def parent_intent_signature(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rejectionStatement")
    def rejection_statement(
        self,
    ) -> Optional[pulumi.Input[IntentRejectionStatementArgs]]: ...
    @rejection_statement.setter
    def rejection_statement(
        self, value: Optional[pulumi.Input[IntentRejectionStatementArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sampleUtterances")
    def sample_utterances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @sample_utterances.setter
    def sample_utterances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def slots(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IntentSlotArgs]]]]: ...
    @slots.setter
    def slots(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IntentSlotArgs]]]]
    ): ...

@pulumi.input_type
class _IntentState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum: Optional[pulumi.Input[_builtins.str]] = ...,
        conclusion_statement: Optional[
            pulumi.Input[IntentConclusionStatementArgs]
        ] = ...,
        confirmation_prompt: Optional[pulumi.Input[IntentConfirmationPromptArgs]] = ...,
        create_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dialog_code_hook: Optional[pulumi.Input[IntentDialogCodeHookArgs]] = ...,
        follow_up_prompt: Optional[pulumi.Input[IntentFollowUpPromptArgs]] = ...,
        fulfillment_activity: Optional[
            pulumi.Input[IntentFulfillmentActivityArgs]
        ] = ...,
        last_updated_date: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_intent_signature: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rejection_statement: Optional[pulumi.Input[IntentRejectionStatementArgs]] = ...,
        sample_utterances: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        slots: Optional[pulumi.Input[Sequence[pulumi.Input[IntentSlotArgs]]]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @checksum.setter
    def checksum(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="conclusionStatement")
    def conclusion_statement(
        self,
    ) -> Optional[pulumi.Input[IntentConclusionStatementArgs]]: ...
    @conclusion_statement.setter
    def conclusion_statement(
        self, value: Optional[pulumi.Input[IntentConclusionStatementArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="confirmationPrompt")
    def confirmation_prompt(
        self,
    ) -> Optional[pulumi.Input[IntentConfirmationPromptArgs]]: ...
    @confirmation_prompt.setter
    def confirmation_prompt(
        self, value: Optional[pulumi.Input[IntentConfirmationPromptArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createVersion")
    def create_version(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_version.setter
    def create_version(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dialogCodeHook")
    def dialog_code_hook(self) -> Optional[pulumi.Input[IntentDialogCodeHookArgs]]: ...
    @dialog_code_hook.setter
    def dialog_code_hook(
        self, value: Optional[pulumi.Input[IntentDialogCodeHookArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="followUpPrompt")
    def follow_up_prompt(self) -> Optional[pulumi.Input[IntentFollowUpPromptArgs]]: ...
    @follow_up_prompt.setter
    def follow_up_prompt(
        self, value: Optional[pulumi.Input[IntentFollowUpPromptArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fulfillmentActivity")
    def fulfillment_activity(
        self,
    ) -> Optional[pulumi.Input[IntentFulfillmentActivityArgs]]: ...
    @fulfillment_activity.setter
    def fulfillment_activity(
        self, value: Optional[pulumi.Input[IntentFulfillmentActivityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_updated_date.setter
    def last_updated_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentIntentSignature")
    def parent_intent_signature(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_intent_signature.setter
    def parent_intent_signature(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rejectionStatement")
    def rejection_statement(
        self,
    ) -> Optional[pulumi.Input[IntentRejectionStatementArgs]]: ...
    @rejection_statement.setter
    def rejection_statement(
        self, value: Optional[pulumi.Input[IntentRejectionStatementArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sampleUtterances")
    def sample_utterances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @sample_utterances.setter
    def sample_utterances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def slots(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[IntentSlotArgs]]]]: ...
    @slots.setter
    def slots(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IntentSlotArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:lex/intent:Intent")
class Intent(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        conclusion_statement: Optional[
            pulumi.Input[
                Union[IntentConclusionStatementArgs, IntentConclusionStatementArgsDict]
            ]
        ] = ...,
        confirmation_prompt: Optional[
            pulumi.Input[
                Union[IntentConfirmationPromptArgs, IntentConfirmationPromptArgsDict]
            ]
        ] = ...,
        create_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dialog_code_hook: Optional[
            pulumi.Input[Union[IntentDialogCodeHookArgs, IntentDialogCodeHookArgsDict]]
        ] = ...,
        follow_up_prompt: Optional[
            pulumi.Input[Union[IntentFollowUpPromptArgs, IntentFollowUpPromptArgsDict]]
        ] = ...,
        fulfillment_activity: Optional[
            pulumi.Input[
                Union[IntentFulfillmentActivityArgs, IntentFulfillmentActivityArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_intent_signature: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rejection_statement: Optional[
            pulumi.Input[
                Union[IntentRejectionStatementArgs, IntentRejectionStatementArgsDict]
            ]
        ] = ...,
        sample_utterances: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        slots: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[IntentSlotArgs, IntentSlotArgsDict]]]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IntentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        checksum: Optional[pulumi.Input[_builtins.str]] = ...,
        conclusion_statement: Optional[
            pulumi.Input[
                Union[IntentConclusionStatementArgs, IntentConclusionStatementArgsDict]
            ]
        ] = ...,
        confirmation_prompt: Optional[
            pulumi.Input[
                Union[IntentConfirmationPromptArgs, IntentConfirmationPromptArgsDict]
            ]
        ] = ...,
        create_version: Optional[pulumi.Input[_builtins.bool]] = ...,
        created_date: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dialog_code_hook: Optional[
            pulumi.Input[Union[IntentDialogCodeHookArgs, IntentDialogCodeHookArgsDict]]
        ] = ...,
        follow_up_prompt: Optional[
            pulumi.Input[Union[IntentFollowUpPromptArgs, IntentFollowUpPromptArgsDict]]
        ] = ...,
        fulfillment_activity: Optional[
            pulumi.Input[
                Union[IntentFulfillmentActivityArgs, IntentFulfillmentActivityArgsDict]
            ]
        ] = ...,
        last_updated_date: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_intent_signature: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        rejection_statement: Optional[
            pulumi.Input[
                Union[IntentRejectionStatementArgs, IntentRejectionStatementArgsDict]
            ]
        ] = ...,
        sample_utterances: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        slots: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[IntentSlotArgs, IntentSlotArgsDict]]]
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Intent: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conclusionStatement")
    def conclusion_statement(
        self,
    ) -> pulumi.Output[Optional[outputs.IntentConclusionStatement]]: ...
    @_builtins.property
    @pulumi.getter(name="confirmationPrompt")
    def confirmation_prompt(
        self,
    ) -> pulumi.Output[Optional[outputs.IntentConfirmationPrompt]]: ...
    @_builtins.property
    @pulumi.getter(name="createVersion")
    def create_version(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dialogCodeHook")
    def dialog_code_hook(
        self,
    ) -> pulumi.Output[Optional[outputs.IntentDialogCodeHook]]: ...
    @_builtins.property
    @pulumi.getter(name="followUpPrompt")
    def follow_up_prompt(
        self,
    ) -> pulumi.Output[Optional[outputs.IntentFollowUpPrompt]]: ...
    @_builtins.property
    @pulumi.getter(name="fulfillmentActivity")
    def fulfillment_activity(
        self,
    ) -> pulumi.Output[outputs.IntentFulfillmentActivity]: ...
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parentIntentSignature")
    def parent_intent_signature(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rejectionStatement")
    def rejection_statement(
        self,
    ) -> pulumi.Output[Optional[outputs.IntentRejectionStatement]]: ...
    @_builtins.property
    @pulumi.getter(name="sampleUtterances")
    def sample_utterances(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def slots(self) -> pulumi.Output[Optional[Sequence[outputs.IntentSlot]]]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]: ...
