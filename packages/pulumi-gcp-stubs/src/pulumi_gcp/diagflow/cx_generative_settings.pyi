import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CxGenerativeSettingsArgs", "CxGenerativeSettings"]

@pulumi.input_type
class CxGenerativeSettingsArgs:
    def __init__(
        __self__,
        *,
        language_code: pulumi.Input[_builtins.str],
        fallback_settings: Optional[
            pulumi.Input[CxGenerativeSettingsFallbackSettingsArgs]
        ] = ...,
        generative_safety_settings: Optional[
            pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsArgs]
        ] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[CxGenerativeSettingsKnowledgeConnectorSettingsArgs]
        ] = ...,
        llm_model_settings: Optional[
            pulumi.Input[CxGenerativeSettingsLlmModelSettingsArgs]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]: ...
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fallbackSettings")
    def fallback_settings(
        self,
    ) -> Optional[pulumi.Input[CxGenerativeSettingsFallbackSettingsArgs]]: ...
    @fallback_settings.setter
    def fallback_settings(
        self, value: Optional[pulumi.Input[CxGenerativeSettingsFallbackSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="generativeSafetySettings")
    def generative_safety_settings(
        self,
    ) -> Optional[pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsArgs]]: ...
    @generative_safety_settings.setter
    def generative_safety_settings(
        self,
        value: Optional[pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="knowledgeConnectorSettings")
    def knowledge_connector_settings(
        self,
    ) -> Optional[pulumi.Input[CxGenerativeSettingsKnowledgeConnectorSettingsArgs]]: ...
    @knowledge_connector_settings.setter
    def knowledge_connector_settings(
        self,
        value: Optional[
            pulumi.Input[CxGenerativeSettingsKnowledgeConnectorSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="llmModelSettings")
    def llm_model_settings(
        self,
    ) -> Optional[pulumi.Input[CxGenerativeSettingsLlmModelSettingsArgs]]: ...
    @llm_model_settings.setter
    def llm_model_settings(
        self, value: Optional[pulumi.Input[CxGenerativeSettingsLlmModelSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _CxGenerativeSettingsState:
    def __init__(
        __self__,
        *,
        fallback_settings: Optional[
            pulumi.Input[CxGenerativeSettingsFallbackSettingsArgs]
        ] = ...,
        generative_safety_settings: Optional[
            pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsArgs]
        ] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[CxGenerativeSettingsKnowledgeConnectorSettingsArgs]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        llm_model_settings: Optional[
            pulumi.Input[CxGenerativeSettingsLlmModelSettingsArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fallbackSettings")
    def fallback_settings(
        self,
    ) -> Optional[pulumi.Input[CxGenerativeSettingsFallbackSettingsArgs]]: ...
    @fallback_settings.setter
    def fallback_settings(
        self, value: Optional[pulumi.Input[CxGenerativeSettingsFallbackSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="generativeSafetySettings")
    def generative_safety_settings(
        self,
    ) -> Optional[pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsArgs]]: ...
    @generative_safety_settings.setter
    def generative_safety_settings(
        self,
        value: Optional[pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="knowledgeConnectorSettings")
    def knowledge_connector_settings(
        self,
    ) -> Optional[pulumi.Input[CxGenerativeSettingsKnowledgeConnectorSettingsArgs]]: ...
    @knowledge_connector_settings.setter
    def knowledge_connector_settings(
        self,
        value: Optional[
            pulumi.Input[CxGenerativeSettingsKnowledgeConnectorSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="llmModelSettings")
    def llm_model_settings(
        self,
    ) -> Optional[pulumi.Input[CxGenerativeSettingsLlmModelSettingsArgs]]: ...
    @llm_model_settings.setter
    def llm_model_settings(
        self, value: Optional[pulumi.Input[CxGenerativeSettingsLlmModelSettingsArgs]]
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

@pulumi.type_token(...)
class CxGenerativeSettings(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        fallback_settings: Optional[
            pulumi.Input[
                Union[
                    CxGenerativeSettingsFallbackSettingsArgs,
                    CxGenerativeSettingsFallbackSettingsArgsDict,
                ]
            ]
        ] = ...,
        generative_safety_settings: Optional[
            pulumi.Input[
                Union[
                    CxGenerativeSettingsGenerativeSafetySettingsArgs,
                    CxGenerativeSettingsGenerativeSafetySettingsArgsDict,
                ]
            ]
        ] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[
                Union[
                    CxGenerativeSettingsKnowledgeConnectorSettingsArgs,
                    CxGenerativeSettingsKnowledgeConnectorSettingsArgsDict,
                ]
            ]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        llm_model_settings: Optional[
            pulumi.Input[
                Union[
                    CxGenerativeSettingsLlmModelSettingsArgs,
                    CxGenerativeSettingsLlmModelSettingsArgsDict,
                ]
            ]
        ] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CxGenerativeSettingsArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        fallback_settings: Optional[
            pulumi.Input[
                Union[
                    CxGenerativeSettingsFallbackSettingsArgs,
                    CxGenerativeSettingsFallbackSettingsArgsDict,
                ]
            ]
        ] = ...,
        generative_safety_settings: Optional[
            pulumi.Input[
                Union[
                    CxGenerativeSettingsGenerativeSafetySettingsArgs,
                    CxGenerativeSettingsGenerativeSafetySettingsArgsDict,
                ]
            ]
        ] = ...,
        knowledge_connector_settings: Optional[
            pulumi.Input[
                Union[
                    CxGenerativeSettingsKnowledgeConnectorSettingsArgs,
                    CxGenerativeSettingsKnowledgeConnectorSettingsArgsDict,
                ]
            ]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        llm_model_settings: Optional[
            pulumi.Input[
                Union[
                    CxGenerativeSettingsLlmModelSettingsArgs,
                    CxGenerativeSettingsLlmModelSettingsArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> CxGenerativeSettings: ...
    @_builtins.property
    @pulumi.getter(name="fallbackSettings")
    def fallback_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.CxGenerativeSettingsFallbackSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="generativeSafetySettings")
    def generative_safety_settings(
        self,
    ) -> pulumi.Output[
        Optional[outputs.CxGenerativeSettingsGenerativeSafetySettings]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeConnectorSettings")
    def knowledge_connector_settings(
        self,
    ) -> pulumi.Output[
        Optional[outputs.CxGenerativeSettingsKnowledgeConnectorSettings]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="llmModelSettings")
    def llm_model_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.CxGenerativeSettingsLlmModelSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]: ...
