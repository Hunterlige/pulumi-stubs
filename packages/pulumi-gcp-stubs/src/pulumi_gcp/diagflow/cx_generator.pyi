import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CxGeneratorArgs", "CxGenerator"]

@pulumi.input_type
class CxGeneratorArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        prompt_text: pulumi.Input[CxGeneratorPromptTextArgs],
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        llm_model_settings: Optional[
            pulumi.Input[CxGeneratorLlmModelSettingsArgs]
        ] = ...,
        model_parameter: Optional[pulumi.Input[CxGeneratorModelParameterArgs]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        placeholders: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxGeneratorPlaceholderArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> pulumi.Input[CxGeneratorPromptTextArgs]: ...
    @prompt_text.setter
    def prompt_text(self, value: pulumi.Input[CxGeneratorPromptTextArgs]): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="llmModelSettings")
    def llm_model_settings(
        self,
    ) -> Optional[pulumi.Input[CxGeneratorLlmModelSettingsArgs]]: ...
    @llm_model_settings.setter
    def llm_model_settings(
        self, value: Optional[pulumi.Input[CxGeneratorLlmModelSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelParameter")
    def model_parameter(
        self,
    ) -> Optional[pulumi.Input[CxGeneratorModelParameterArgs]]: ...
    @model_parameter.setter
    def model_parameter(
        self, value: Optional[pulumi.Input[CxGeneratorModelParameterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def placeholders(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxGeneratorPlaceholderArgs]]]]: ...
    @placeholders.setter
    def placeholders(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxGeneratorPlaceholderArgs]]]
        ],
    ): ...

@pulumi.input_type
class _CxGeneratorState:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        llm_model_settings: Optional[
            pulumi.Input[CxGeneratorLlmModelSettingsArgs]
        ] = ...,
        model_parameter: Optional[pulumi.Input[CxGeneratorModelParameterArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        placeholders: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxGeneratorPlaceholderArgs]]]
        ] = ...,
        prompt_text: Optional[pulumi.Input[CxGeneratorPromptTextArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="llmModelSettings")
    def llm_model_settings(
        self,
    ) -> Optional[pulumi.Input[CxGeneratorLlmModelSettingsArgs]]: ...
    @llm_model_settings.setter
    def llm_model_settings(
        self, value: Optional[pulumi.Input[CxGeneratorLlmModelSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelParameter")
    def model_parameter(
        self,
    ) -> Optional[pulumi.Input[CxGeneratorModelParameterArgs]]: ...
    @model_parameter.setter
    def model_parameter(
        self, value: Optional[pulumi.Input[CxGeneratorModelParameterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def placeholders(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxGeneratorPlaceholderArgs]]]]: ...
    @placeholders.setter
    def placeholders(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxGeneratorPlaceholderArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> Optional[pulumi.Input[CxGeneratorPromptTextArgs]]: ...
    @prompt_text.setter
    def prompt_text(self, value: Optional[pulumi.Input[CxGeneratorPromptTextArgs]]): ...

@pulumi.type_token("gcp:diagflow/cxGenerator:CxGenerator")
class CxGenerator(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        llm_model_settings: Optional[
            pulumi.Input[
                Union[
                    CxGeneratorLlmModelSettingsArgs, CxGeneratorLlmModelSettingsArgsDict
                ]
            ]
        ] = ...,
        model_parameter: Optional[
            pulumi.Input[
                Union[CxGeneratorModelParameterArgs, CxGeneratorModelParameterArgsDict]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        placeholders: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CxGeneratorPlaceholderArgs, CxGeneratorPlaceholderArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        prompt_text: Optional[
            pulumi.Input[
                Union[CxGeneratorPromptTextArgs, CxGeneratorPromptTextArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CxGeneratorArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        llm_model_settings: Optional[
            pulumi.Input[
                Union[
                    CxGeneratorLlmModelSettingsArgs, CxGeneratorLlmModelSettingsArgsDict
                ]
            ]
        ] = ...,
        model_parameter: Optional[
            pulumi.Input[
                Union[CxGeneratorModelParameterArgs, CxGeneratorModelParameterArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        placeholders: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CxGeneratorPlaceholderArgs, CxGeneratorPlaceholderArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        prompt_text: Optional[
            pulumi.Input[
                Union[CxGeneratorPromptTextArgs, CxGeneratorPromptTextArgsDict]
            ]
        ] = ...,
    ) -> CxGenerator: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="llmModelSettings")
    def llm_model_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.CxGeneratorLlmModelSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="modelParameter")
    def model_parameter(
        self,
    ) -> pulumi.Output[Optional[outputs.CxGeneratorModelParameter]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def placeholders(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.CxGeneratorPlaceholder]]]: ...
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> pulumi.Output[outputs.CxGeneratorPromptText]: ...
