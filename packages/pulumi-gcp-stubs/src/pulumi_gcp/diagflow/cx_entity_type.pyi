import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["CxEntityTypeArgs", "CxEntityType"]

@pulumi.input_type
class CxEntityTypeArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        entities: pulumi.Input[Sequence[pulumi.Input[CxEntityTypeEntityArgs]]],
        kind: pulumi.Input[_builtins.str],
        auto_expansion_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fuzzy_extraction: Optional[pulumi.Input[_builtins.bool]] = ...,
        excluded_phrases: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxEntityTypeExcludedPhraseArgs]]]
        ] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        redact: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def entities(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[CxEntityTypeEntityArgs]]]: ...
    @entities.setter
    def entities(
        self, value: pulumi.Input[Sequence[pulumi.Input[CxEntityTypeEntityArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="autoExpansionMode")
    def auto_expansion_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_expansion_mode.setter
    def auto_expansion_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_fuzzy_extraction.setter
    def enable_fuzzy_extraction(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedPhrases")
    def excluded_phrases(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CxEntityTypeExcludedPhraseArgs]]]
    ]: ...
    @excluded_phrases.setter
    def excluded_phrases(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxEntityTypeExcludedPhraseArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent.setter
    def parent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def redact(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @redact.setter
    def redact(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _CxEntityTypeState:
    def __init__(
        __self__,
        *,
        auto_expansion_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fuzzy_extraction: Optional[pulumi.Input[_builtins.bool]] = ...,
        entities: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxEntityTypeEntityArgs]]]
        ] = ...,
        excluded_phrases: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxEntityTypeExcludedPhraseArgs]]]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        redact: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoExpansionMode")
    def auto_expansion_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auto_expansion_mode.setter
    def auto_expansion_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_fuzzy_extraction.setter
    def enable_fuzzy_extraction(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def entities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxEntityTypeEntityArgs]]]]: ...
    @entities.setter
    def entities(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CxEntityTypeEntityArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedPhrases")
    def excluded_phrases(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[CxEntityTypeExcludedPhraseArgs]]]
    ]: ...
    @excluded_phrases.setter
    def excluded_phrases(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[CxEntityTypeExcludedPhraseArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def redact(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @redact.setter
    def redact(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("gcp:diagflow/cxEntityType:CxEntityType")
class CxEntityType(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_expansion_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fuzzy_extraction: Optional[pulumi.Input[_builtins.bool]] = ...,
        entities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxEntityTypeEntityArgs, CxEntityTypeEntityArgsDict]
                    ]
                ]
            ]
        ] = ...,
        excluded_phrases: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CxEntityTypeExcludedPhraseArgs,
                            CxEntityTypeExcludedPhraseArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        redact: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: CxEntityTypeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        auto_expansion_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fuzzy_extraction: Optional[pulumi.Input[_builtins.bool]] = ...,
        entities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CxEntityTypeEntityArgs, CxEntityTypeEntityArgsDict]
                    ]
                ]
            ]
        ] = ...,
        excluded_phrases: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            CxEntityTypeExcludedPhraseArgs,
                            CxEntityTypeExcludedPhraseArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parent: Optional[pulumi.Input[_builtins.str]] = ...,
        redact: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> CxEntityType: ...
    @_builtins.property
    @pulumi.getter(name="autoExpansionMode")
    def auto_expansion_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def entities(self) -> pulumi.Output[Sequence[outputs.CxEntityTypeEntity]]: ...
    @_builtins.property
    @pulumi.getter(name="excludedPhrases")
    def excluded_phrases(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.CxEntityTypeExcludedPhrase]]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def redact(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
