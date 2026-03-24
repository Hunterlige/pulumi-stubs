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
        display_name: pulumi.Input[_builtins.str],
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        default_response_platforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        input_context_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_fallback: Optional[pulumi.Input[_builtins.bool]] = ...,
        ml_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        parent_followup_intent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reset_contexts: Optional[pulumi.Input[_builtins.bool]] = ...,
        webhook_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultResponsePlatforms")
    def default_response_platforms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @default_response_platforms.setter
    def default_response_platforms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @events.setter
    def events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputContextNames")
    def input_context_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @input_context_names.setter
    def input_context_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isFallback")
    def is_fallback(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_fallback.setter
    def is_fallback(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="mlDisabled")
    def ml_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ml_disabled.setter
    def ml_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="parentFollowupIntentName")
    def parent_followup_intent_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_followup_intent_name.setter
    def parent_followup_intent_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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
    @pulumi.getter(name="resetContexts")
    def reset_contexts(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reset_contexts.setter
    def reset_contexts(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="webhookState")
    def webhook_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webhook_state.setter
    def webhook_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _IntentState:
    def __init__(
        __self__,
        *,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        default_response_platforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        followup_intent_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[IntentFollowupIntentInfoArgs]]]
        ] = ...,
        input_context_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_fallback: Optional[pulumi.Input[_builtins.bool]] = ...,
        ml_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_followup_intent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reset_contexts: Optional[pulumi.Input[_builtins.bool]] = ...,
        root_followup_intent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        webhook_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @action.setter
    def action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultResponsePlatforms")
    def default_response_platforms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @default_response_platforms.setter
    def default_response_platforms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @events.setter
    def events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="followupIntentInfos")
    def followup_intent_infos(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[IntentFollowupIntentInfoArgs]]]
    ]: ...
    @followup_intent_infos.setter
    def followup_intent_infos(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[IntentFollowupIntentInfoArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputContextNames")
    def input_context_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @input_context_names.setter
    def input_context_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isFallback")
    def is_fallback(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_fallback.setter
    def is_fallback(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="mlDisabled")
    def ml_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ml_disabled.setter
    def ml_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentFollowupIntentName")
    def parent_followup_intent_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_followup_intent_name.setter
    def parent_followup_intent_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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
    @pulumi.getter(name="resetContexts")
    def reset_contexts(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reset_contexts.setter
    def reset_contexts(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="rootFollowupIntentName")
    def root_followup_intent_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_followup_intent_name.setter
    def root_followup_intent_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="webhookState")
    def webhook_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @webhook_state.setter
    def webhook_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:diagflow/intent:Intent")
class Intent(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        default_response_platforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        input_context_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_fallback: Optional[pulumi.Input[_builtins.bool]] = ...,
        ml_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        parent_followup_intent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reset_contexts: Optional[pulumi.Input[_builtins.bool]] = ...,
        webhook_state: Optional[pulumi.Input[_builtins.str]] = ...,
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
        action: Optional[pulumi.Input[_builtins.str]] = ...,
        default_response_platforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        events: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        followup_intent_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            IntentFollowupIntentInfoArgs,
                            IntentFollowupIntentInfoArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        input_context_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        is_fallback: Optional[pulumi.Input[_builtins.bool]] = ...,
        ml_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_followup_intent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        priority: Optional[pulumi.Input[_builtins.int]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        reset_contexts: Optional[pulumi.Input[_builtins.bool]] = ...,
        root_followup_intent_name: Optional[pulumi.Input[_builtins.str]] = ...,
        webhook_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Intent: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="defaultResponsePlatforms")
    def default_response_platforms(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def events(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="followupIntentInfos")
    def followup_intent_infos(
        self,
    ) -> pulumi.Output[Sequence[outputs.IntentFollowupIntentInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="inputContextNames")
    def input_context_names(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="isFallback")
    def is_fallback(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="mlDisabled")
    def ml_disabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parentFollowupIntentName")
    def parent_followup_intent_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resetContexts")
    def reset_contexts(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="rootFollowupIntentName")
    def root_followup_intent_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webhookState")
    def webhook_state(self) -> pulumi.Output[_builtins.str]: ...
