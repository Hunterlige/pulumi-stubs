import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "PreventionDeidentifyTemplateDeidentifyConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionDiscoveryConfigActionArgs",
    "PreventionDiscoveryConfigActionArgsDict",
    "PreventionDiscoveryConfigActionExportDataArgs",
    "PreventionDiscoveryConfigActionExportDataArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionDiscoveryConfigActionPublishToSccArgs",
    ...,
    "PreventionDiscoveryConfigActionTagResourcesArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionDiscoveryConfigErrorArgs",
    "PreventionDiscoveryConfigErrorArgsDict",
    "PreventionDiscoveryConfigErrorDetailsArgs",
    "PreventionDiscoveryConfigErrorDetailsArgsDict",
    "PreventionDiscoveryConfigOrgConfigArgs",
    "PreventionDiscoveryConfigOrgConfigArgsDict",
    "PreventionDiscoveryConfigOrgConfigLocationArgs",
    "PreventionDiscoveryConfigOrgConfigLocationArgsDict",
    ...,
    ...,
    ...,
    ...,
    "PreventionDiscoveryConfigTargetArgs",
    "PreventionDiscoveryConfigTargetArgsDict",
    "PreventionDiscoveryConfigTargetBigQueryTargetArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionDiscoveryConfigTargetCloudSqlTargetArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionDiscoveryConfigTargetSecretsTargetArgs",
    ...,
    "PreventionInspectTemplateInspectConfigArgs",
    "PreventionInspectTemplateInspectConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionInspectTemplateInspectConfigInfoTypeArgs",
    ...,
    ...,
    ...,
    "PreventionInspectTemplateInspectConfigLimitsArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionInspectTemplateInspectConfigRuleSetArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionJobTriggerInspectJobArgs",
    "PreventionJobTriggerInspectJobArgsDict",
    "PreventionJobTriggerInspectJobActionArgs",
    "PreventionJobTriggerInspectJobActionArgsDict",
    "PreventionJobTriggerInspectJobActionDeidentifyArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionJobTriggerInspectJobActionPubSubArgs",
    "PreventionJobTriggerInspectJobActionPubSubArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionJobTriggerInspectJobInspectConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionJobTriggerInspectJobStorageConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionJobTriggerTriggerArgs",
    "PreventionJobTriggerTriggerArgsDict",
    "PreventionJobTriggerTriggerManualArgs",
    "PreventionJobTriggerTriggerManualArgsDict",
    "PreventionJobTriggerTriggerScheduleArgs",
    "PreventionJobTriggerTriggerScheduleArgsDict",
    "PreventionStoredInfoTypeDictionaryArgs",
    "PreventionStoredInfoTypeDictionaryArgsDict",
    ...,
    ...,
    "PreventionStoredInfoTypeDictionaryWordListArgs",
    "PreventionStoredInfoTypeDictionaryWordListArgsDict",
    "PreventionStoredInfoTypeLargeCustomDictionaryArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "PreventionStoredInfoTypeRegexArgs",
    "PreventionStoredInfoTypeRegexArgsDict",
]

class PreventionDeidentifyTemplateDeidentifyConfigArgsDict(TypedDict):
    image_transformations: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsArgsDict
        ]
    ]
    info_type_transformations: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsArgsDict
        ]
    ]
    record_transformations: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigArgs:
    def __init__(
        __self__,
        *,
        image_transformations: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsArgs
            ]
        ] = ...,
        info_type_transformations: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsArgs
            ]
        ] = ...,
        record_transformations: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageTransformations")
    def image_transformations(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsArgs
        ]
    ]: ...
    @image_transformations.setter
    def image_transformations(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="infoTypeTransformations")
    def info_type_transformations(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsArgs
        ]
    ]: ...
    @info_type_transformations.setter
    def info_type_transformations(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recordTransformations")
    def record_transformations(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsArgs
        ]
    ]: ...
    @record_transformations.setter
    def record_transformations(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsArgsDict(
    TypedDict
):
    transforms: pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsArgs:
    def __init__(
        __self__,
        *,
        transforms: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def transforms(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformArgs
            ]
        ]
    ]: ...
    @transforms.setter
    def transforms(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformArgs
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformArgsDict(
    TypedDict
):
    all_info_types: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllInfoTypesArgsDict
        ]
    ]
    all_text: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllTextArgsDict
        ]
    ]
    redaction_color: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformRedactionColorArgsDict
        ]
    ]
    selected_info_types: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformArgs:
    def __init__(
        __self__,
        *,
        all_info_types: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllInfoTypesArgs
            ]
        ] = ...,
        all_text: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllTextArgs
            ]
        ] = ...,
        redaction_color: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformRedactionColorArgs
            ]
        ] = ...,
        selected_info_types: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allInfoTypes")
    def all_info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllInfoTypesArgs
        ]
    ]: ...
    @all_info_types.setter
    def all_info_types(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllInfoTypesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allText")
    def all_text(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllTextArgs
        ]
    ]: ...
    @all_text.setter
    def all_text(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllTextArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redactionColor")
    def redaction_color(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformRedactionColorArgs
        ]
    ]: ...
    @redaction_color.setter
    def redaction_color(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformRedactionColorArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectedInfoTypes")
    def selected_info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesArgs
        ]
    ]: ...
    @selected_info_types.setter
    def selected_info_types(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllInfoTypesArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllInfoTypesArgs:
    def __init__(__self__) -> None: ...

class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllTextArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllTextArgs:
    def __init__(__self__) -> None: ...

class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformRedactionColorArgsDict(
    TypedDict
):
    blue: NotRequired[pulumi.Input[_builtins.float]]
    green: NotRequired[pulumi.Input[_builtins.float]]
    red: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformRedactionColorArgs:
    def __init__(
        __self__,
        *,
        blue: Optional[pulumi.Input[_builtins.float]] = ...,
        green: Optional[pulumi.Input[_builtins.float]] = ...,
        red: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def blue(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @blue.setter
    def blue(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def green(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @green.setter
    def green(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def red(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @red.setter
    def red(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesArgsDict(
    TypedDict
):
    info_types: pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesArgs:
    def __init__(
        __self__,
        *,
        info_types: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeArgs
            ]
        ]
    ]: ...
    @info_types.setter
    def info_types(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeArgs
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsArgsDict(
    TypedDict
):
    transformations: pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsArgs:
    def __init__(
        __self__,
        *,
        transformations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def transformations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationArgs
            ]
        ]
    ]: ...
    @transformations.setter
    def transformations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationArgs
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationArgsDict(
    TypedDict
):
    primitive_transformation: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationArgsDict
    ]
    info_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationArgs:
    def __init__(
        __self__,
        *,
        primitive_transformation: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationArgs
        ],
        info_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primitiveTransformation")
    def primitive_transformation(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationArgs
    ]: ...
    @primitive_transformation.setter
    def primitive_transformation(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeArgs
                ]
            ]
        ]
    ]: ...
    @info_types.setter
    def info_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationArgsDict(
    TypedDict
):
    bucketing_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgsDict
        ]
    ]
    character_mask_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgsDict
        ]
    ]
    crypto_deterministic_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgsDict
        ]
    ]
    crypto_hash_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgsDict
        ]
    ]
    crypto_replace_ffx_fpe_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgsDict
        ]
    ]
    date_shift_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgsDict
        ]
    ]
    fixed_size_bucketing_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgsDict
        ]
    ]
    redact_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgsDict
        ]
    ]
    replace_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgsDict
        ]
    ]
    replace_dictionary_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgsDict
        ]
    ]
    replace_with_info_type_config: NotRequired[pulumi.Input[_builtins.bool]]
    time_part_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationArgs:
    def __init__(
        __self__,
        *,
        bucketing_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgs
            ]
        ] = ...,
        character_mask_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgs
            ]
        ] = ...,
        crypto_deterministic_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgs
            ]
        ] = ...,
        crypto_hash_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgs
            ]
        ] = ...,
        crypto_replace_ffx_fpe_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs
            ]
        ] = ...,
        date_shift_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgs
            ]
        ] = ...,
        fixed_size_bucketing_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs
            ]
        ] = ...,
        redact_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgs
            ]
        ] = ...,
        replace_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgs
            ]
        ] = ...,
        replace_dictionary_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgs
            ]
        ] = ...,
        replace_with_info_type_config: Optional[pulumi.Input[_builtins.bool]] = ...,
        time_part_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketingConfig")
    def bucketing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgs
        ]
    ]: ...
    @bucketing_config.setter
    def bucketing_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="characterMaskConfig")
    def character_mask_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgs
        ]
    ]: ...
    @character_mask_config.setter
    def character_mask_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoDeterministicConfig")
    def crypto_deterministic_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgs
        ]
    ]: ...
    @crypto_deterministic_config.setter
    def crypto_deterministic_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoHashConfig")
    def crypto_hash_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgs
        ]
    ]: ...
    @crypto_hash_config.setter
    def crypto_hash_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoReplaceFfxFpeConfig")
    def crypto_replace_ffx_fpe_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs
        ]
    ]: ...
    @crypto_replace_ffx_fpe_config.setter
    def crypto_replace_ffx_fpe_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dateShiftConfig")
    def date_shift_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgs
        ]
    ]: ...
    @date_shift_config.setter
    def date_shift_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fixedSizeBucketingConfig")
    def fixed_size_bucketing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs
        ]
    ]: ...
    @fixed_size_bucketing_config.setter
    def fixed_size_bucketing_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redactConfig")
    def redact_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgs
        ]
    ]: ...
    @redact_config.setter
    def redact_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replaceConfig")
    def replace_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgs
        ]
    ]: ...
    @replace_config.setter
    def replace_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replaceDictionaryConfig")
    def replace_dictionary_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgs
        ]
    ]: ...
    @replace_dictionary_config.setter
    def replace_dictionary_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replaceWithInfoTypeConfig")
    def replace_with_info_type_config(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @replace_with_info_type_config.setter
    def replace_with_info_type_config(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timePartConfig")
    def time_part_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgs
        ]
    ]: ...
    @time_part_config.setter
    def time_part_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgsDict(
    TypedDict
):
    buckets: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgs:
    def __init__(
        __self__,
        *,
        buckets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def buckets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgs
                ]
            ]
        ]
    ]: ...
    @buckets.setter
    def buckets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgsDict(
    TypedDict
):
    replacement_value: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgsDict
    ]
    max: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgsDict
        ]
    ]
    min: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgs:
    def __init__(
        __self__,
        *,
        replacement_value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs
        ],
        max: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs
            ]
        ] = ...,
        min: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replacementValue")
    def replacement_value(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs
    ]: ...
    @replacement_value.setter
    def replacement_value(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def max(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs
        ]
    ]: ...
    @max.setter
    def max(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def min(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgs
        ]
    ]: ...
    @min.setter
    def min(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgsDict(
    TypedDict
):
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgsDict(
    TypedDict
):
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgsDict(
    TypedDict
):
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgsDict(
    TypedDict
):
    characters_to_ignores: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgsDict
                ]
            ]
        ]
    ]
    masking_character: NotRequired[pulumi.Input[_builtins.str]]
    number_to_mask: NotRequired[pulumi.Input[_builtins.int]]
    reverse_order: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgs:
    def __init__(
        __self__,
        *,
        characters_to_ignores: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs
                    ]
                ]
            ]
        ] = ...,
        masking_character: Optional[pulumi.Input[_builtins.str]] = ...,
        number_to_mask: Optional[pulumi.Input[_builtins.int]] = ...,
        reverse_order: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="charactersToIgnores")
    def characters_to_ignores(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs
                ]
            ]
        ]
    ]: ...
    @characters_to_ignores.setter
    def characters_to_ignores(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maskingCharacter")
    def masking_character(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @masking_character.setter
    def masking_character(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberToMask")
    def number_to_mask(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_to_mask.setter
    def number_to_mask(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="reverseOrder")
    def reverse_order(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reverse_order.setter
    def reverse_order(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgsDict(
    TypedDict
):
    characters_to_skip: NotRequired[pulumi.Input[_builtins.str]]
    common_characters_to_ignore: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs:
    def __init__(
        __self__,
        *,
        characters_to_skip: Optional[pulumi.Input[_builtins.str]] = ...,
        common_characters_to_ignore: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="charactersToSkip")
    def characters_to_skip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @characters_to_skip.setter
    def characters_to_skip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commonCharactersToIgnore")
    def common_characters_to_ignore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @common_characters_to_ignore.setter
    def common_characters_to_ignore(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgsDict(
    TypedDict
):
    context: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgsDict
        ]
    ]
    crypto_key: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgsDict
        ]
    ]
    surrogate_info_type: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgs:
    def __init__(
        __self__,
        *,
        context: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs
            ]
        ] = ...,
        crypto_key: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs
            ]
        ] = ...,
        surrogate_info_type: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs
        ]
    ]: ...
    @context.setter
    def context(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs
        ]
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs
        ]
    ]: ...
    @surrogate_info_type.setter
    def surrogate_info_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgsDict(
    TypedDict
):
    crypto_key: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgs:
    def __init__(
        __self__,
        *,
        crypto_key: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs
        ]
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgsDict(
    TypedDict
):
    common_alphabet: NotRequired[pulumi.Input[_builtins.str]]
    context: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgsDict
        ]
    ]
    crypto_key: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgsDict
        ]
    ]
    custom_alphabet: NotRequired[pulumi.Input[_builtins.str]]
    radix: NotRequired[pulumi.Input[_builtins.int]]
    surrogate_info_type: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs:
    def __init__(
        __self__,
        *,
        common_alphabet: Optional[pulumi.Input[_builtins.str]] = ...,
        context: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs
            ]
        ] = ...,
        crypto_key: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs
            ]
        ] = ...,
        custom_alphabet: Optional[pulumi.Input[_builtins.str]] = ...,
        radix: Optional[pulumi.Input[_builtins.int]] = ...,
        surrogate_info_type: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonAlphabet")
    def common_alphabet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @common_alphabet.setter
    def common_alphabet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs
        ]
    ]: ...
    @context.setter
    def context(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs
        ]
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customAlphabet")
    def custom_alphabet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_alphabet.setter
    def custom_alphabet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def radix(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @radix.setter
    def radix(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs
        ]
    ]: ...
    @surrogate_info_type.setter
    def surrogate_info_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgsDict(
    TypedDict
):
    lower_bound_days: pulumi.Input[_builtins.int]
    upper_bound_days: pulumi.Input[_builtins.int]
    context: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgsDict
        ]
    ]
    crypto_key: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgs:
    def __init__(
        __self__,
        *,
        lower_bound_days: pulumi.Input[_builtins.int],
        upper_bound_days: pulumi.Input[_builtins.int],
        context: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgs
            ]
        ] = ...,
        crypto_key: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerBoundDays")
    def lower_bound_days(self) -> pulumi.Input[_builtins.int]: ...
    @lower_bound_days.setter
    def lower_bound_days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="upperBoundDays")
    def upper_bound_days(self) -> pulumi.Input[_builtins.int]: ...
    @upper_bound_days.setter
    def upper_bound_days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgs
        ]
    ]: ...
    @context.setter
    def context(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs
        ]
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgsDict(
    TypedDict
):
    bucket_size: pulumi.Input[_builtins.float]
    lower_bound: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgsDict
    ]
    upper_bound: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgsDict
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs:
    def __init__(
        __self__,
        *,
        bucket_size: pulumi.Input[_builtins.float],
        lower_bound: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs
        ],
        upper_bound: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketSize")
    def bucket_size(self) -> pulumi.Input[_builtins.float]: ...
    @bucket_size.setter
    def bucket_size(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="lowerBound")
    def lower_bound(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs
    ]: ...
    @lower_bound.setter
    def lower_bound(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="upperBound")
    def upper_bound(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs
    ]: ...
    @upper_bound.setter
    def upper_bound(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgsDict(
    TypedDict
):
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs:
    def __init__(
        __self__,
        *,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgsDict(
    TypedDict
):
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs:
    def __init__(
        __self__,
        *,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgs:
    def __init__(__self__) -> None: ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgsDict(
    TypedDict
):
    new_value: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgsDict
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgs:
    def __init__(
        __self__,
        *,
        new_value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newValue")
    def new_value(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgs
    ]: ...
    @new_value.setter
    def new_value(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgs
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.int]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.int]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgsDict(
    TypedDict
):
    word_list: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgsDict
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgs:
    def __init__(
        __self__,
        *,
        word_list: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs
    ]: ...
    @word_list.setter
    def word_list(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgsDict(
    TypedDict
):
    words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs:
    def __init__(
        __self__, *, words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def words(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @words.setter
    def words(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgsDict(
    TypedDict
):
    part_to_extract: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgs:
    def __init__(
        __self__, *, part_to_extract: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partToExtract")
    def part_to_extract(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @part_to_extract.setter
    def part_to_extract(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsArgsDict(
    TypedDict
):
    field_transformations: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationArgsDict
                ]
            ]
        ]
    ]
    record_suppressions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsArgs:
    def __init__(
        __self__,
        *,
        field_transformations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationArgs
                    ]
                ]
            ]
        ] = ...,
        record_suppressions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldTransformations")
    def field_transformations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationArgs
                ]
            ]
        ]
    ]: ...
    @field_transformations.setter
    def field_transformations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recordSuppressions")
    def record_suppressions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionArgs
                ]
            ]
        ]
    ]: ...
    @record_suppressions.setter
    def record_suppressions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationArgsDict(
    TypedDict
):
    fields: pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationFieldArgsDict
            ]
        ]
    ]
    condition: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionArgsDict
        ]
    ]
    info_type_transformations: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsArgsDict
        ]
    ]
    primitive_transformation: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationArgs:
    def __init__(
        __self__,
        *,
        fields: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationFieldArgs
                ]
            ]
        ],
        condition: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionArgs
            ]
        ] = ...,
        info_type_transformations: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsArgs
            ]
        ] = ...,
        primitive_transformation: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def fields(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationFieldArgs
            ]
        ]
    ]: ...
    @fields.setter
    def fields(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationFieldArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionArgs
        ]
    ]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="infoTypeTransformations")
    def info_type_transformations(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsArgs
        ]
    ]: ...
    @info_type_transformations.setter
    def info_type_transformations(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="primitiveTransformation")
    def primitive_transformation(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationArgs
        ]
    ]: ...
    @primitive_transformation.setter
    def primitive_transformation(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionArgsDict(
    TypedDict
):
    expressions: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionArgs:
    def __init__(
        __self__,
        *,
        expressions: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expressions(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsArgs
        ]
    ]: ...
    @expressions.setter
    def expressions(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsArgsDict(
    TypedDict
):
    conditions: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsArgsDict
        ]
    ]
    logical_operator: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsArgs
            ]
        ] = ...,
        logical_operator: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsArgs
        ]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logicalOperator")
    def logical_operator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logical_operator.setter
    def logical_operator(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsArgsDict(
    TypedDict
):
    conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionArgs
                ]
            ]
        ]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionArgsDict(
    TypedDict
):
    field: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionFieldArgsDict
    ]
    operator: pulumi.Input[_builtins.str]
    value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionArgs:
    def __init__(
        __self__,
        *,
        field: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionFieldArgs
        ],
        operator: pulumi.Input[_builtins.str],
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionFieldArgs
    ]: ...
    @field.setter
    def field(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionFieldArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[_builtins.str]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueArgs
        ]
    ]: ...
    @value.setter
    def value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionFieldArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionFieldArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationFieldArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationFieldArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsArgsDict(
    TypedDict
):
    transformations: pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsArgs:
    def __init__(
        __self__,
        *,
        transformations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def transformations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationArgs
            ]
        ]
    ]: ...
    @transformations.setter
    def transformations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationArgs
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationArgsDict(
    TypedDict
):
    primitive_transformation: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationArgsDict
    ]
    info_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationArgs:
    def __init__(
        __self__,
        *,
        primitive_transformation: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationArgs
        ],
        info_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primitiveTransformation")
    def primitive_transformation(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationArgs
    ]: ...
    @primitive_transformation.setter
    def primitive_transformation(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeArgs
                ]
            ]
        ]
    ]: ...
    @info_types.setter
    def info_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationArgsDict(
    TypedDict
):
    bucketing_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgsDict
        ]
    ]
    character_mask_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgsDict
        ]
    ]
    crypto_deterministic_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgsDict
        ]
    ]
    crypto_hash_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgsDict
        ]
    ]
    crypto_replace_ffx_fpe_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgsDict
        ]
    ]
    date_shift_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgsDict
        ]
    ]
    fixed_size_bucketing_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgsDict
        ]
    ]
    redact_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgsDict
        ]
    ]
    replace_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgsDict
        ]
    ]
    replace_dictionary_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgsDict
        ]
    ]
    replace_with_info_type_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceWithInfoTypeConfigArgsDict
        ]
    ]
    time_part_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationArgs:
    def __init__(
        __self__,
        *,
        bucketing_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgs
            ]
        ] = ...,
        character_mask_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgs
            ]
        ] = ...,
        crypto_deterministic_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgs
            ]
        ] = ...,
        crypto_hash_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgs
            ]
        ] = ...,
        crypto_replace_ffx_fpe_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs
            ]
        ] = ...,
        date_shift_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgs
            ]
        ] = ...,
        fixed_size_bucketing_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs
            ]
        ] = ...,
        redact_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgs
            ]
        ] = ...,
        replace_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgs
            ]
        ] = ...,
        replace_dictionary_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgs
            ]
        ] = ...,
        replace_with_info_type_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceWithInfoTypeConfigArgs
            ]
        ] = ...,
        time_part_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketingConfig")
    def bucketing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgs
        ]
    ]: ...
    @bucketing_config.setter
    def bucketing_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="characterMaskConfig")
    def character_mask_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgs
        ]
    ]: ...
    @character_mask_config.setter
    def character_mask_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoDeterministicConfig")
    def crypto_deterministic_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgs
        ]
    ]: ...
    @crypto_deterministic_config.setter
    def crypto_deterministic_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoHashConfig")
    def crypto_hash_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgs
        ]
    ]: ...
    @crypto_hash_config.setter
    def crypto_hash_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoReplaceFfxFpeConfig")
    def crypto_replace_ffx_fpe_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs
        ]
    ]: ...
    @crypto_replace_ffx_fpe_config.setter
    def crypto_replace_ffx_fpe_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dateShiftConfig")
    def date_shift_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgs
        ]
    ]: ...
    @date_shift_config.setter
    def date_shift_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fixedSizeBucketingConfig")
    def fixed_size_bucketing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs
        ]
    ]: ...
    @fixed_size_bucketing_config.setter
    def fixed_size_bucketing_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redactConfig")
    def redact_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgs
        ]
    ]: ...
    @redact_config.setter
    def redact_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replaceConfig")
    def replace_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgs
        ]
    ]: ...
    @replace_config.setter
    def replace_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replaceDictionaryConfig")
    def replace_dictionary_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgs
        ]
    ]: ...
    @replace_dictionary_config.setter
    def replace_dictionary_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replaceWithInfoTypeConfig")
    def replace_with_info_type_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceWithInfoTypeConfigArgs
        ]
    ]: ...
    @replace_with_info_type_config.setter
    def replace_with_info_type_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceWithInfoTypeConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timePartConfig")
    def time_part_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgs
        ]
    ]: ...
    @time_part_config.setter
    def time_part_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgsDict(
    TypedDict
):
    buckets: pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigArgs:
    def __init__(
        __self__,
        *,
        buckets: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def buckets(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgs
            ]
        ]
    ]: ...
    @buckets.setter
    def buckets(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgs
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgsDict(
    TypedDict
):
    replacement_value: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgsDict
    ]
    max: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgsDict
        ]
    ]
    min: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketArgs:
    def __init__(
        __self__,
        *,
        replacement_value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs
        ],
        max: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs
            ]
        ] = ...,
        min: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replacementValue")
    def replacement_value(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs
    ]: ...
    @replacement_value.setter
    def replacement_value(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def max(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs
        ]
    ]: ...
    @max.setter
    def max(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def min(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgs
        ]
    ]: ...
    @min.setter
    def min(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgsDict(
    TypedDict
):
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgsDict(
    TypedDict
):
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgsDict(
    TypedDict
):
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs:
    def __init__(
        __self__,
        *,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgsDict(
    TypedDict
):
    characters_to_ignores: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgsDict
                ]
            ]
        ]
    ]
    masking_character: NotRequired[pulumi.Input[_builtins.str]]
    number_to_mask: NotRequired[pulumi.Input[_builtins.int]]
    reverse_order: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigArgs:
    def __init__(
        __self__,
        *,
        characters_to_ignores: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs
                    ]
                ]
            ]
        ] = ...,
        masking_character: Optional[pulumi.Input[_builtins.str]] = ...,
        number_to_mask: Optional[pulumi.Input[_builtins.int]] = ...,
        reverse_order: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="charactersToIgnores")
    def characters_to_ignores(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs
                ]
            ]
        ]
    ]: ...
    @characters_to_ignores.setter
    def characters_to_ignores(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maskingCharacter")
    def masking_character(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @masking_character.setter
    def masking_character(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberToMask")
    def number_to_mask(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_to_mask.setter
    def number_to_mask(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="reverseOrder")
    def reverse_order(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reverse_order.setter
    def reverse_order(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgsDict(
    TypedDict
):
    characters_to_skip: NotRequired[pulumi.Input[_builtins.str]]
    common_characters_to_ignore: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs:
    def __init__(
        __self__,
        *,
        characters_to_skip: Optional[pulumi.Input[_builtins.str]] = ...,
        common_characters_to_ignore: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="charactersToSkip")
    def characters_to_skip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @characters_to_skip.setter
    def characters_to_skip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commonCharactersToIgnore")
    def common_characters_to_ignore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @common_characters_to_ignore.setter
    def common_characters_to_ignore(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgsDict(
    TypedDict
):
    crypto_key: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgsDict
    ]
    surrogate_info_type: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgsDict
    ]
    context: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigArgs:
    def __init__(
        __self__,
        *,
        crypto_key: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs
        ],
        surrogate_info_type: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs
        ],
        context: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs
    ]: ...
    @surrogate_info_type.setter
    def surrogate_info_type(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs
        ]
    ]: ...
    @context.setter
    def context(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgsDict(
    TypedDict
):
    crypto_key: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgsDict
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigArgs:
    def __init__(
        __self__,
        *,
        crypto_key: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgsDict(
    TypedDict
):
    crypto_key: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgsDict
    ]
    common_alphabet: NotRequired[pulumi.Input[_builtins.str]]
    context: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgsDict
        ]
    ]
    custom_alphabet: NotRequired[pulumi.Input[_builtins.str]]
    radix: NotRequired[pulumi.Input[_builtins.int]]
    surrogate_info_type: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs:
    def __init__(
        __self__,
        *,
        crypto_key: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs
        ],
        common_alphabet: Optional[pulumi.Input[_builtins.str]] = ...,
        context: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs
            ]
        ] = ...,
        custom_alphabet: Optional[pulumi.Input[_builtins.str]] = ...,
        radix: Optional[pulumi.Input[_builtins.int]] = ...,
        surrogate_info_type: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="commonAlphabet")
    def common_alphabet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @common_alphabet.setter
    def common_alphabet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs
        ]
    ]: ...
    @context.setter
    def context(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customAlphabet")
    def custom_alphabet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_alphabet.setter
    def custom_alphabet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def radix(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @radix.setter
    def radix(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs
        ]
    ]: ...
    @surrogate_info_type.setter
    def surrogate_info_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgsDict(
    TypedDict
):
    lower_bound_days: pulumi.Input[_builtins.int]
    upper_bound_days: pulumi.Input[_builtins.int]
    context: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgsDict
        ]
    ]
    crypto_key: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigArgs:
    def __init__(
        __self__,
        *,
        lower_bound_days: pulumi.Input[_builtins.int],
        upper_bound_days: pulumi.Input[_builtins.int],
        context: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgs
            ]
        ] = ...,
        crypto_key: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerBoundDays")
    def lower_bound_days(self) -> pulumi.Input[_builtins.int]: ...
    @lower_bound_days.setter
    def lower_bound_days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="upperBoundDays")
    def upper_bound_days(self) -> pulumi.Input[_builtins.int]: ...
    @upper_bound_days.setter
    def upper_bound_days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgs
        ]
    ]: ...
    @context.setter
    def context(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs
        ]
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContextArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgsDict(
    TypedDict
):
    bucket_size: pulumi.Input[_builtins.float]
    lower_bound: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgsDict
    ]
    upper_bound: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgsDict
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs:
    def __init__(
        __self__,
        *,
        bucket_size: pulumi.Input[_builtins.float],
        lower_bound: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs
        ],
        upper_bound: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketSize")
    def bucket_size(self) -> pulumi.Input[_builtins.float]: ...
    @bucket_size.setter
    def bucket_size(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="lowerBound")
    def lower_bound(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs
    ]: ...
    @lower_bound.setter
    def lower_bound(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="upperBound")
    def upper_bound(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs
    ]: ...
    @upper_bound.setter
    def upper_bound(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgsDict(
    TypedDict
):
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs:
    def __init__(
        __self__,
        *,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgsDict(
    TypedDict
):
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs:
    def __init__(
        __self__,
        *,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfigArgs:
    def __init__(__self__) -> None: ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgsDict(
    TypedDict
):
    new_value: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgsDict
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigArgs:
    def __init__(
        __self__,
        *,
        new_value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newValue")
    def new_value(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgs
    ]: ...
    @new_value.setter
    def new_value(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgs
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgsDict(
    TypedDict
):
    word_list: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgsDict
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigArgs:
    def __init__(
        __self__,
        *,
        word_list: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs
    ]: ...
    @word_list.setter
    def word_list(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgsDict(
    TypedDict
):
    words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs:
    def __init__(
        __self__, *, words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def words(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @words.setter
    def words(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceWithInfoTypeConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceWithInfoTypeConfigArgs:
    def __init__(__self__) -> None: ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgsDict(
    TypedDict
):
    part_to_extract: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfigArgs:
    def __init__(__self__, *, part_to_extract: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partToExtract")
    def part_to_extract(self) -> pulumi.Input[_builtins.str]: ...
    @part_to_extract.setter
    def part_to_extract(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationArgsDict(
    TypedDict
):
    bucketing_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigArgsDict
        ]
    ]
    character_mask_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigArgsDict
        ]
    ]
    crypto_deterministic_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigArgsDict
        ]
    ]
    crypto_hash_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigArgsDict
        ]
    ]
    crypto_replace_ffx_fpe_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgsDict
        ]
    ]
    date_shift_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigArgsDict
        ]
    ]
    fixed_size_bucketing_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigArgsDict
        ]
    ]
    redact_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationRedactConfigArgsDict
        ]
    ]
    replace_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigArgsDict
        ]
    ]
    replace_dictionary_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigArgsDict
        ]
    ]
    time_part_config: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationTimePartConfigArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationArgs:
    def __init__(
        __self__,
        *,
        bucketing_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigArgs
            ]
        ] = ...,
        character_mask_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigArgs
            ]
        ] = ...,
        crypto_deterministic_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigArgs
            ]
        ] = ...,
        crypto_hash_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigArgs
            ]
        ] = ...,
        crypto_replace_ffx_fpe_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs
            ]
        ] = ...,
        date_shift_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigArgs
            ]
        ] = ...,
        fixed_size_bucketing_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs
            ]
        ] = ...,
        redact_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationRedactConfigArgs
            ]
        ] = ...,
        replace_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigArgs
            ]
        ] = ...,
        replace_dictionary_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigArgs
            ]
        ] = ...,
        time_part_config: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationTimePartConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketingConfig")
    def bucketing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigArgs
        ]
    ]: ...
    @bucketing_config.setter
    def bucketing_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="characterMaskConfig")
    def character_mask_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigArgs
        ]
    ]: ...
    @character_mask_config.setter
    def character_mask_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoDeterministicConfig")
    def crypto_deterministic_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigArgs
        ]
    ]: ...
    @crypto_deterministic_config.setter
    def crypto_deterministic_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoHashConfig")
    def crypto_hash_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigArgs
        ]
    ]: ...
    @crypto_hash_config.setter
    def crypto_hash_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoReplaceFfxFpeConfig")
    def crypto_replace_ffx_fpe_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs
        ]
    ]: ...
    @crypto_replace_ffx_fpe_config.setter
    def crypto_replace_ffx_fpe_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dateShiftConfig")
    def date_shift_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigArgs
        ]
    ]: ...
    @date_shift_config.setter
    def date_shift_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fixedSizeBucketingConfig")
    def fixed_size_bucketing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs
        ]
    ]: ...
    @fixed_size_bucketing_config.setter
    def fixed_size_bucketing_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redactConfig")
    def redact_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationRedactConfigArgs
        ]
    ]: ...
    @redact_config.setter
    def redact_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationRedactConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replaceConfig")
    def replace_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigArgs
        ]
    ]: ...
    @replace_config.setter
    def replace_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replaceDictionaryConfig")
    def replace_dictionary_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigArgs
        ]
    ]: ...
    @replace_dictionary_config.setter
    def replace_dictionary_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timePartConfig")
    def time_part_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationTimePartConfigArgs
        ]
    ]: ...
    @time_part_config.setter
    def time_part_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationTimePartConfigArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigArgsDict(
    TypedDict
):
    buckets: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigArgs:
    def __init__(
        __self__,
        *,
        buckets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def buckets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketArgs
                ]
            ]
        ]
    ]: ...
    @buckets.setter
    def buckets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketArgsDict(
    TypedDict
):
    replacement_value: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgsDict
    ]
    max: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxArgsDict
        ]
    ]
    min: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketArgs:
    def __init__(
        __self__,
        *,
        replacement_value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs
        ],
        max: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs
            ]
        ] = ...,
        min: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="replacementValue")
    def replacement_value(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs
    ]: ...
    @replacement_value.setter
    def replacement_value(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def max(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs
        ]
    ]: ...
    @max.setter
    def max(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def min(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinArgs
        ]
    ]: ...
    @min.setter
    def min(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigArgsDict(
    TypedDict
):
    characters_to_ignores: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgsDict
                ]
            ]
        ]
    ]
    masking_character: NotRequired[pulumi.Input[_builtins.str]]
    number_to_mask: NotRequired[pulumi.Input[_builtins.int]]
    reverse_order: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigArgs:
    def __init__(
        __self__,
        *,
        characters_to_ignores: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs
                    ]
                ]
            ]
        ] = ...,
        masking_character: Optional[pulumi.Input[_builtins.str]] = ...,
        number_to_mask: Optional[pulumi.Input[_builtins.int]] = ...,
        reverse_order: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="charactersToIgnores")
    def characters_to_ignores(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs
                ]
            ]
        ]
    ]: ...
    @characters_to_ignores.setter
    def characters_to_ignores(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maskingCharacter")
    def masking_character(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @masking_character.setter
    def masking_character(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="numberToMask")
    def number_to_mask(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @number_to_mask.setter
    def number_to_mask(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="reverseOrder")
    def reverse_order(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reverse_order.setter
    def reverse_order(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgsDict(
    TypedDict
):
    characters_to_skip: NotRequired[pulumi.Input[_builtins.str]]
    common_characters_to_ignore: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnoreArgs:
    def __init__(
        __self__,
        *,
        characters_to_skip: Optional[pulumi.Input[_builtins.str]] = ...,
        common_characters_to_ignore: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="charactersToSkip")
    def characters_to_skip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @characters_to_skip.setter
    def characters_to_skip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commonCharactersToIgnore")
    def common_characters_to_ignore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @common_characters_to_ignore.setter
    def common_characters_to_ignore(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigArgsDict(
    TypedDict
):
    context: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgsDict
        ]
    ]
    crypto_key: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgsDict
        ]
    ]
    surrogate_info_type: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigArgs:
    def __init__(
        __self__,
        *,
        context: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs
            ]
        ] = ...,
        crypto_key: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs
            ]
        ] = ...,
        surrogate_info_type: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs
        ]
    ]: ...
    @context.setter
    def context(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs
        ]
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs
        ]
    ]: ...
    @surrogate_info_type.setter
    def surrogate_info_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigContextArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigArgsDict(
    TypedDict
):
    crypto_key: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigArgs:
    def __init__(
        __self__,
        *,
        crypto_key: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs
        ]
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgsDict(
    TypedDict
):
    common_alphabet: NotRequired[pulumi.Input[_builtins.str]]
    context: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgsDict
        ]
    ]
    crypto_key: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgsDict
        ]
    ]
    custom_alphabet: NotRequired[pulumi.Input[_builtins.str]]
    radix: NotRequired[pulumi.Input[_builtins.int]]
    surrogate_info_type: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigArgs:
    def __init__(
        __self__,
        *,
        common_alphabet: Optional[pulumi.Input[_builtins.str]] = ...,
        context: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs
            ]
        ] = ...,
        crypto_key: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs
            ]
        ] = ...,
        custom_alphabet: Optional[pulumi.Input[_builtins.str]] = ...,
        radix: Optional[pulumi.Input[_builtins.int]] = ...,
        surrogate_info_type: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commonAlphabet")
    def common_alphabet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @common_alphabet.setter
    def common_alphabet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs
        ]
    ]: ...
    @context.setter
    def context(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs
        ]
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customAlphabet")
    def custom_alphabet(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_alphabet.setter
    def custom_alphabet(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def radix(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @radix.setter
    def radix(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs
        ]
    ]: ...
    @surrogate_info_type.setter
    def surrogate_info_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContextArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigArgsDict(
    TypedDict
):
    lower_bound_days: pulumi.Input[_builtins.int]
    upper_bound_days: pulumi.Input[_builtins.int]
    context: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigContextArgsDict
        ]
    ]
    crypto_key: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigArgs:
    def __init__(
        __self__,
        *,
        lower_bound_days: pulumi.Input[_builtins.int],
        upper_bound_days: pulumi.Input[_builtins.int],
        context: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigContextArgs
            ]
        ] = ...,
        crypto_key: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerBoundDays")
    def lower_bound_days(self) -> pulumi.Input[_builtins.int]: ...
    @lower_bound_days.setter
    def lower_bound_days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="upperBoundDays")
    def upper_bound_days(self) -> pulumi.Input[_builtins.int]: ...
    @upper_bound_days.setter
    def upper_bound_days(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def context(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigContextArgs
        ]
    ]: ...
    @context.setter
    def context(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigContextArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs
        ]
    ]: ...
    @crypto_key.setter
    def crypto_key(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigContextArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigContextArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgsDict(
    TypedDict
):
    kms_wrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgsDict
        ]
    ]
    transient: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgsDict
        ]
    ]
    unwrapped: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyArgs:
    def __init__(
        __self__,
        *,
        kms_wrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs
            ]
        ] = ...,
        transient: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs
            ]
        ] = ...,
        unwrapped: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs
        ]
    ]: ...
    @kms_wrapped.setter
    def kms_wrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def transient(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs
        ]
    ]: ...
    @transient.setter
    def transient(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def unwrapped(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs
        ]
    ]: ...
    @unwrapped.setter
    def unwrapped(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgsDict(
    TypedDict
):
    crypto_key_name: pulumi.Input[_builtins.str]
    wrapped_key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrappedArgs:
    def __init__(
        __self__,
        *,
        crypto_key_name: pulumi.Input[_builtins.str],
        wrapped_key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Input[_builtins.str]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> pulumi.Input[_builtins.str]: ...
    @wrapped_key.setter
    def wrapped_key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransientArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgsDict(
    TypedDict
):
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrappedArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigArgsDict(
    TypedDict
):
    bucket_size: pulumi.Input[_builtins.float]
    lower_bound: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgsDict
    ]
    upper_bound: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgsDict
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigArgs:
    def __init__(
        __self__,
        *,
        bucket_size: pulumi.Input[_builtins.float],
        lower_bound: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs
        ],
        upper_bound: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketSize")
    def bucket_size(self) -> pulumi.Input[_builtins.float]: ...
    @bucket_size.setter
    def bucket_size(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="lowerBound")
    def lower_bound(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs
    ]: ...
    @lower_bound.setter
    def lower_bound(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="upperBound")
    def upper_bound(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs
    ]: ...
    @upper_bound.setter
    def upper_bound(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationRedactConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationRedactConfigArgs:
    def __init__(__self__) -> None: ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigArgsDict(
    TypedDict
):
    new_value: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueArgsDict
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigArgs:
    def __init__(
        __self__,
        *,
        new_value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newValue")
    def new_value(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueArgs
    ]: ...
    @new_value.setter
    def new_value(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueArgs
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigArgsDict(
    TypedDict
):
    word_list: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigArgs:
    def __init__(
        __self__,
        *,
        word_list: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs
        ]
    ]: ...
    @word_list.setter
    def word_list(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgsDict(
    TypedDict
):
    words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigWordListArgs:
    def __init__(
        __self__, *, words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def words(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @words.setter
    def words(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationTimePartConfigArgsDict(
    TypedDict
):
    part_to_extract: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationTimePartConfigArgs:
    def __init__(
        __self__, *, part_to_extract: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="partToExtract")
    def part_to_extract(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @part_to_extract.setter
    def part_to_extract(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionArgsDict(
    TypedDict
):
    condition: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionArgs:
    def __init__(
        __self__,
        *,
        condition: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionArgs
        ]
    ]: ...
    @condition.setter
    def condition(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionArgsDict(
    TypedDict
):
    expressions: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionArgs:
    def __init__(
        __self__,
        *,
        expressions: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expressions(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsArgs
        ]
    ]: ...
    @expressions.setter
    def expressions(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsArgsDict(
    TypedDict
):
    conditions: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsArgsDict
        ]
    ]
    logical_operator: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsArgs
            ]
        ] = ...,
        logical_operator: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsArgs
        ]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logicalOperator")
    def logical_operator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logical_operator.setter
    def logical_operator(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsArgsDict(
    TypedDict
):
    conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionArgs
                ]
            ]
        ]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionArgsDict(
    TypedDict
):
    field: pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionFieldArgsDict
    ]
    operator: pulumi.Input[_builtins.str]
    value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionArgs:
    def __init__(
        __self__,
        *,
        field: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionFieldArgs
        ],
        operator: pulumi.Input[_builtins.str],
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(
        self,
    ) -> pulumi.Input[
        PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionFieldArgs
    ]: ...
    @field.setter
    def field(
        self,
        value: pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionFieldArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[_builtins.str]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueArgs
        ]
    ]: ...
    @value.setter
    def value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueArgs
            ]
        ],
    ): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionFieldArgsDict(
    TypedDict
):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionFieldArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueArgsDict(
    TypedDict
):
    boolean_value: NotRequired[pulumi.Input[_builtins.bool]]
    date_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueDateValueArgsDict
        ]
    ]
    day_of_week_value: NotRequired[pulumi.Input[_builtins.str]]
    float_value: NotRequired[pulumi.Input[_builtins.float]]
    integer_value: NotRequired[pulumi.Input[_builtins.str]]
    string_value: NotRequired[pulumi.Input[_builtins.str]]
    time_value: NotRequired[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueTimeValueArgsDict
        ]
    ]
    timestamp_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueArgs:
    def __init__(
        __self__,
        *,
        boolean_value: Optional[pulumi.Input[_builtins.bool]] = ...,
        date_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueDateValueArgs
            ]
        ] = ...,
        day_of_week_value: Optional[pulumi.Input[_builtins.str]] = ...,
        float_value: Optional[pulumi.Input[_builtins.float]] = ...,
        integer_value: Optional[pulumi.Input[_builtins.str]] = ...,
        string_value: Optional[pulumi.Input[_builtins.str]] = ...,
        time_value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueTimeValueArgs
            ]
        ] = ...,
        timestamp_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @boolean_value.setter
    def boolean_value(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueDateValueArgs
        ]
    ]: ...
    @date_value.setter
    def date_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueDateValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week_value.setter
    def day_of_week_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @float_value.setter
    def float_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @integer_value.setter
    def integer_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @string_value.setter
    def string_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueTimeValueArgs
        ]
    ]: ...
    @time_value.setter
    def time_value(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueTimeValueArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp_value.setter
    def timestamp_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueDateValueArgsDict(
    TypedDict
):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueDateValueArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueTimeValueArgsDict(
    TypedDict
):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueTimeValueArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDiscoveryConfigActionArgsDict(TypedDict):
    export_data: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigActionExportDataArgsDict]
    ]
    pub_sub_notification: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigActionPubSubNotificationArgsDict]
    ]
    publish_to_chronicle: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigActionPublishToChronicleArgsDict]
    ]
    publish_to_dataplex_catalog: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigActionPublishToDataplexCatalogArgsDict]
    ]
    publish_to_scc: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigActionPublishToSccArgsDict]
    ]
    tag_resources: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigActionTagResourcesArgsDict]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionArgs:
    def __init__(
        __self__,
        *,
        export_data: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionExportDataArgs]
        ] = ...,
        pub_sub_notification: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionPubSubNotificationArgs]
        ] = ...,
        publish_to_chronicle: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionPublishToChronicleArgs]
        ] = ...,
        publish_to_dataplex_catalog: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionPublishToDataplexCatalogArgs]
        ] = ...,
        publish_to_scc: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionPublishToSccArgs]
        ] = ...,
        tag_resources: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionTagResourcesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exportData")
    def export_data(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigActionExportDataArgs]]: ...
    @export_data.setter
    def export_data(
        self,
        value: Optional[pulumi.Input[PreventionDiscoveryConfigActionExportDataArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pubSubNotification")
    def pub_sub_notification(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigActionPubSubNotificationArgs]
    ]: ...
    @pub_sub_notification.setter
    def pub_sub_notification(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionPubSubNotificationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishToChronicle")
    def publish_to_chronicle(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigActionPublishToChronicleArgs]
    ]: ...
    @publish_to_chronicle.setter
    def publish_to_chronicle(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionPublishToChronicleArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishToDataplexCatalog")
    def publish_to_dataplex_catalog(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigActionPublishToDataplexCatalogArgs]
    ]: ...
    @publish_to_dataplex_catalog.setter
    def publish_to_dataplex_catalog(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionPublishToDataplexCatalogArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishToScc")
    def publish_to_scc(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigActionPublishToSccArgs]]: ...
    @publish_to_scc.setter
    def publish_to_scc(
        self,
        value: Optional[pulumi.Input[PreventionDiscoveryConfigActionPublishToSccArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagResources")
    def tag_resources(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigActionTagResourcesArgs]]: ...
    @tag_resources.setter
    def tag_resources(
        self,
        value: Optional[pulumi.Input[PreventionDiscoveryConfigActionTagResourcesArgs]],
    ): ...

class PreventionDiscoveryConfigActionExportDataArgsDict(TypedDict):
    profile_table: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigActionExportDataProfileTableArgsDict]
    ]
    sample_findings_table: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigActionExportDataSampleFindingsTableArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionExportDataArgs:
    def __init__(
        __self__,
        *,
        profile_table: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionExportDataProfileTableArgs]
        ] = ...,
        sample_findings_table: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigActionExportDataSampleFindingsTableArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="profileTable")
    def profile_table(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigActionExportDataProfileTableArgs]
    ]: ...
    @profile_table.setter
    def profile_table(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionExportDataProfileTableArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sampleFindingsTable")
    def sample_findings_table(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigActionExportDataSampleFindingsTableArgs]
    ]: ...
    @sample_findings_table.setter
    def sample_findings_table(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigActionExportDataSampleFindingsTableArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigActionExportDataProfileTableArgsDict(TypedDict):
    dataset_id: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    table_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionExportDataProfileTableArgs:
    def __init__(
        __self__,
        *,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_id.setter
    def table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigActionExportDataSampleFindingsTableArgsDict(TypedDict):
    dataset_id: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    table_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionExportDataSampleFindingsTableArgs:
    def __init__(
        __self__,
        *,
        dataset_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_id.setter
    def table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigActionPubSubNotificationArgsDict(TypedDict):
    detail_of_message: NotRequired[pulumi.Input[_builtins.str]]
    event: NotRequired[pulumi.Input[_builtins.str]]
    pubsub_condition: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionArgsDict
        ]
    ]
    topic: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionPubSubNotificationArgs:
    def __init__(
        __self__,
        *,
        detail_of_message: Optional[pulumi.Input[_builtins.str]] = ...,
        event: Optional[pulumi.Input[_builtins.str]] = ...,
        pubsub_condition: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionArgs
            ]
        ] = ...,
        topic: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="detailOfMessage")
    def detail_of_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detail_of_message.setter
    def detail_of_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @event.setter
    def event(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pubsubCondition")
    def pubsub_condition(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionArgs
        ]
    ]: ...
    @pubsub_condition.setter
    def pubsub_condition(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionArgsDict(
    TypedDict
):
    expressions: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionArgs:
    def __init__(
        __self__,
        *,
        expressions: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expressions(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsArgs
        ]
    ]: ...
    @expressions.setter
    def expressions(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsArgsDict(
    TypedDict
):
    conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsConditionArgsDict
                ]
            ]
        ]
    ]
    logical_operator: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsConditionArgs
                    ]
                ]
            ]
        ] = ...,
        logical_operator: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsConditionArgs
                ]
            ]
        ]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsConditionArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="logicalOperator")
    def logical_operator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logical_operator.setter
    def logical_operator(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsConditionArgsDict(
    TypedDict
):
    minimum_risk_score: NotRequired[pulumi.Input[_builtins.str]]
    minimum_sensitivity_score: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsConditionArgs:
    def __init__(
        __self__,
        *,
        minimum_risk_score: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_sensitivity_score: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minimumRiskScore")
    def minimum_risk_score(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_risk_score.setter
    def minimum_risk_score(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumSensitivityScore")
    def minimum_sensitivity_score(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_sensitivity_score.setter
    def minimum_sensitivity_score(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PreventionDiscoveryConfigActionPublishToChronicleArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionDiscoveryConfigActionPublishToChronicleArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigActionPublishToDataplexCatalogArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionDiscoveryConfigActionPublishToDataplexCatalogArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigActionPublishToSccArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionDiscoveryConfigActionPublishToSccArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigActionTagResourcesArgsDict(TypedDict):
    lower_data_risk_to_low: NotRequired[pulumi.Input[_builtins.bool]]
    profile_generations_to_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    tag_conditions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigActionTagResourcesTagConditionArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionTagResourcesArgs:
    def __init__(
        __self__,
        *,
        lower_data_risk_to_low: Optional[pulumi.Input[_builtins.bool]] = ...,
        profile_generations_to_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tag_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigActionTagResourcesTagConditionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerDataRiskToLow")
    def lower_data_risk_to_low(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @lower_data_risk_to_low.setter
    def lower_data_risk_to_low(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="profileGenerationsToTags")
    def profile_generations_to_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @profile_generations_to_tags.setter
    def profile_generations_to_tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagConditions")
    def tag_conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigActionTagResourcesTagConditionArgs
                ]
            ]
        ]
    ]: ...
    @tag_conditions.setter
    def tag_conditions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigActionTagResourcesTagConditionArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDiscoveryConfigActionTagResourcesTagConditionArgsDict(TypedDict):
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigActionTagResourcesTagConditionSensitivityScoreArgsDict
        ]
    ]
    tag: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigActionTagResourcesTagConditionTagArgsDict]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionTagResourcesTagConditionArgs:
    def __init__(
        __self__,
        *,
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigActionTagResourcesTagConditionSensitivityScoreArgs
            ]
        ] = ...,
        tag: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionTagResourcesTagConditionTagArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigActionTagResourcesTagConditionSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigActionTagResourcesTagConditionSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tag(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigActionTagResourcesTagConditionTagArgs]
    ]: ...
    @tag.setter
    def tag(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigActionTagResourcesTagConditionTagArgs]
        ],
    ): ...

class PreventionDiscoveryConfigActionTagResourcesTagConditionSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionTagResourcesTagConditionSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDiscoveryConfigActionTagResourcesTagConditionTagArgsDict(TypedDict):
    namespaced_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigActionTagResourcesTagConditionTagArgs:
    def __init__(
        __self__, *, namespaced_value: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespacedValue")
    def namespaced_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespaced_value.setter
    def namespaced_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigErrorArgsDict(TypedDict):
    details: NotRequired[pulumi.Input[PreventionDiscoveryConfigErrorDetailsArgsDict]]
    timestamp: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigErrorArgs:
    def __init__(
        __self__,
        *,
        details: Optional[
            pulumi.Input[PreventionDiscoveryConfigErrorDetailsArgs]
        ] = ...,
        timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigErrorDetailsArgs]]: ...
    @details.setter
    def details(
        self, value: Optional[pulumi.Input[PreventionDiscoveryConfigErrorDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timestamp.setter
    def timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigErrorDetailsArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigErrorDetailsArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]
    ]: ...
    @details.setter
    def details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigOrgConfigArgsDict(TypedDict):
    location: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigOrgConfigLocationArgsDict]
    ]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigOrgConfigArgs:
    def __init__(
        __self__,
        *,
        location: Optional[
            pulumi.Input[PreventionDiscoveryConfigOrgConfigLocationArgs]
        ] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigOrgConfigLocationArgs]]: ...
    @location.setter
    def location(
        self,
        value: Optional[pulumi.Input[PreventionDiscoveryConfigOrgConfigLocationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigOrgConfigLocationArgsDict(TypedDict):
    folder_id: NotRequired[pulumi.Input[_builtins.str]]
    organization_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigOrgConfigLocationArgs:
    def __init__(
        __self__,
        *,
        folder_id: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigOtherCloudStartingLocationArgsDict(TypedDict):
    aws_location: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigOtherCloudStartingLocationAwsLocationArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigOtherCloudStartingLocationArgs:
    def __init__(
        __self__,
        *,
        aws_location: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigOtherCloudStartingLocationAwsLocationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsLocation")
    def aws_location(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigOtherCloudStartingLocationAwsLocationArgs]
    ]: ...
    @aws_location.setter
    def aws_location(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigOtherCloudStartingLocationAwsLocationArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigOtherCloudStartingLocationAwsLocationArgsDict(TypedDict):
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    all_asset_inventory_assets: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigOtherCloudStartingLocationAwsLocationArgs:
    def __init__(
        __self__,
        *,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        all_asset_inventory_assets: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="allAssetInventoryAssets")
    def all_asset_inventory_assets(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all_asset_inventory_assets.setter
    def all_asset_inventory_assets(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class PreventionDiscoveryConfigTargetArgsDict(TypedDict):
    big_query_target: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetArgsDict]
    ]
    cloud_sql_target: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetArgsDict]
    ]
    cloud_storage_target: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetArgsDict]
    ]
    other_cloud_target: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetArgsDict]
    ]
    secrets_target: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetSecretsTargetArgsDict]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetArgs:
    def __init__(
        __self__,
        *,
        big_query_target: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetArgs]
        ] = ...,
        cloud_sql_target: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetArgs]
        ] = ...,
        cloud_storage_target: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetArgs]
        ] = ...,
        other_cloud_target: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetArgs]
        ] = ...,
        secrets_target: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetSecretsTargetArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigQueryTarget")
    def big_query_target(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetArgs]]: ...
    @big_query_target.setter
    def big_query_target(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlTarget")
    def cloud_sql_target(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetArgs]]: ...
    @cloud_sql_target.setter
    def cloud_sql_target(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageTarget")
    def cloud_storage_target(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetArgs]
    ]: ...
    @cloud_storage_target.setter
    def cloud_storage_target(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="otherCloudTarget")
    def other_cloud_target(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetArgs]
    ]: ...
    @other_cloud_target.setter
    def other_cloud_target(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretsTarget")
    def secrets_target(
        self,
    ) -> Optional[pulumi.Input[PreventionDiscoveryConfigTargetSecretsTargetArgs]]: ...
    @secrets_target.setter
    def secrets_target(
        self,
        value: Optional[pulumi.Input[PreventionDiscoveryConfigTargetSecretsTargetArgs]],
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetArgsDict(TypedDict):
    cadence: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetCadenceArgsDict]
    ]
    conditions: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetConditionsArgsDict]
    ]
    disabled: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetDisabledArgsDict]
    ]
    filter: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetFilterArgsDict]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetArgs:
    def __init__(
        __self__,
        *,
        cadence: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetCadenceArgs]
        ] = ...,
        conditions: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetConditionsArgs]
        ] = ...,
        disabled: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetDisabledArgs]
        ] = ...,
        filter: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetFilterArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cadence(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetCadenceArgs]
    ]: ...
    @cadence.setter
    def cadence(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetCadenceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetConditionsArgs]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetConditionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetDisabledArgs]
    ]: ...
    @disabled.setter
    def disabled(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetDisabledArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetFilterArgs]
    ]: ...
    @filter.setter
    def filter(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetFilterArgs]
        ],
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetCadenceArgsDict(TypedDict):
    inspect_template_modified_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetCadenceInspectTemplateModifiedCadenceArgsDict
        ]
    ]
    schema_modified_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetCadenceSchemaModifiedCadenceArgsDict
        ]
    ]
    table_modified_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetCadenceTableModifiedCadenceArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetCadenceArgs:
    def __init__(
        __self__,
        *,
        inspect_template_modified_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetCadenceInspectTemplateModifiedCadenceArgs
            ]
        ] = ...,
        schema_modified_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetCadenceSchemaModifiedCadenceArgs
            ]
        ] = ...,
        table_modified_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetCadenceTableModifiedCadenceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplateModifiedCadence")
    def inspect_template_modified_cadence(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetCadenceInspectTemplateModifiedCadenceArgs
        ]
    ]: ...
    @inspect_template_modified_cadence.setter
    def inspect_template_modified_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetCadenceInspectTemplateModifiedCadenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="schemaModifiedCadence")
    def schema_modified_cadence(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetCadenceSchemaModifiedCadenceArgs
        ]
    ]: ...
    @schema_modified_cadence.setter
    def schema_modified_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetCadenceSchemaModifiedCadenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableModifiedCadence")
    def table_modified_cadence(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetCadenceTableModifiedCadenceArgs
        ]
    ]: ...
    @table_modified_cadence.setter
    def table_modified_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetCadenceTableModifiedCadenceArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetCadenceInspectTemplateModifiedCadenceArgsDict(
    TypedDict
):
    frequency: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetCadenceInspectTemplateModifiedCadenceArgs:
    def __init__(
        __self__, *, frequency: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetBigQueryTargetCadenceSchemaModifiedCadenceArgsDict(
    TypedDict
):
    frequency: NotRequired[pulumi.Input[_builtins.str]]
    types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetCadenceSchemaModifiedCadenceArgs:
    def __init__(
        __self__,
        *,
        frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @types.setter
    def types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetCadenceTableModifiedCadenceArgsDict(
    TypedDict
):
    frequency: NotRequired[pulumi.Input[_builtins.str]]
    types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetCadenceTableModifiedCadenceArgs:
    def __init__(
        __self__,
        *,
        frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @types.setter
    def types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetConditionsArgsDict(TypedDict):
    created_after: NotRequired[pulumi.Input[_builtins.str]]
    or_conditions: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetConditionsOrConditionsArgsDict
        ]
    ]
    type_collection: NotRequired[pulumi.Input[_builtins.str]]
    types: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetConditionsTypesArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetConditionsArgs:
    def __init__(
        __self__,
        *,
        created_after: Optional[pulumi.Input[_builtins.str]] = ...,
        or_conditions: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetConditionsOrConditionsArgs
            ]
        ] = ...,
        type_collection: Optional[pulumi.Input[_builtins.str]] = ...,
        types: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetConditionsTypesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createdAfter")
    def created_after(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_after.setter
    def created_after(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="orConditions")
    def or_conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetConditionsOrConditionsArgs
        ]
    ]: ...
    @or_conditions.setter
    def or_conditions(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetConditionsOrConditionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="typeCollection")
    def type_collection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type_collection.setter
    def type_collection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def types(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetConditionsTypesArgs]
    ]: ...
    @types.setter
    def types(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetConditionsTypesArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetConditionsOrConditionsArgsDict(
    TypedDict
):
    min_age: NotRequired[pulumi.Input[_builtins.str]]
    min_row_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetConditionsOrConditionsArgs:
    def __init__(
        __self__,
        *,
        min_age: Optional[pulumi.Input[_builtins.str]] = ...,
        min_row_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="minAge")
    def min_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_age.setter
    def min_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minRowCount")
    def min_row_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_row_count.setter
    def min_row_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionDiscoveryConfigTargetBigQueryTargetConditionsTypesArgsDict(TypedDict):
    types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetConditionsTypesArgs:
    def __init__(
        __self__,
        *,
        types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @types.setter
    def types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetDisabledArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetDisabledArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigTargetBigQueryTargetFilterArgsDict(TypedDict):
    other_tables: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetFilterOtherTablesArgsDict
        ]
    ]
    table_reference: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetFilterTableReferenceArgsDict
        ]
    ]
    tables: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesArgsDict]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterArgs:
    def __init__(
        __self__,
        *,
        other_tables: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetFilterOtherTablesArgs
            ]
        ] = ...,
        table_reference: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetFilterTableReferenceArgs
            ]
        ] = ...,
        tables: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="otherTables")
    def other_tables(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetFilterOtherTablesArgs]
    ]: ...
    @other_tables.setter
    def other_tables(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetFilterOtherTablesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableReference")
    def table_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetFilterTableReferenceArgs
        ]
    ]: ...
    @table_reference.setter
    def table_reference(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetFilterTableReferenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tables(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesArgs]
    ]: ...
    @tables.setter
    def tables(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesArgs]
        ],
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetFilterOtherTablesArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterOtherTablesArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigTargetBigQueryTargetFilterTableReferenceArgsDict(
    TypedDict
):
    dataset_id: pulumi.Input[_builtins.str]
    table_id: pulumi.Input[_builtins.str]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterTableReferenceArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        table_id: pulumi.Input[_builtins.str],
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesArgsDict(TypedDict):
    include_regexes: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesArgs:
    def __init__(
        __self__,
        *,
        include_regexes: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesArgs
        ]
    ]: ...
    @include_regexes.setter
    def include_regexes(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesArgsDict(
    TypedDict
):
    patterns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesPatternArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesArgs:
    def __init__(
        __self__,
        *,
        patterns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesPatternArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def patterns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesPatternArgs
                ]
            ]
        ]
    ]: ...
    @patterns.setter
    def patterns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesPatternArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesPatternArgsDict(
    TypedDict
):
    dataset_id_regex: NotRequired[pulumi.Input[_builtins.str]]
    project_id_regex: NotRequired[pulumi.Input[_builtins.str]]
    table_id_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesPatternArgs:
    def __init__(
        __self__,
        *,
        dataset_id_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        table_id_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetIdRegex")
    def dataset_id_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset_id_regex.setter
    def dataset_id_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectIdRegex")
    def project_id_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id_regex.setter
    def project_id_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tableIdRegex")
    def table_id_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_id_regex.setter
    def table_id_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetArgsDict(TypedDict):
    filter: pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetFilterArgsDict]
    conditions: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetConditionsArgsDict]
    ]
    disabled: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetDisabledArgsDict]
    ]
    generation_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetArgs:
    def __init__(
        __self__,
        *,
        filter: pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetFilterArgs],
        conditions: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetConditionsArgs]
        ] = ...,
        disabled: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetDisabledArgs]
        ] = ...,
        generation_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetFilterArgs]: ...
    @filter.setter
    def filter(
        self,
        value: pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetFilterArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetConditionsArgs]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetConditionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetDisabledArgs]
    ]: ...
    @disabled.setter
    def disabled(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetDisabledArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="generationCadence")
    def generation_cadence(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceArgs]
    ]: ...
    @generation_cadence.setter
    def generation_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetConditionsArgsDict(TypedDict):
    database_engines: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetConditionsArgs:
    def __init__(
        __self__,
        *,
        database_engines: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseEngines")
    def database_engines(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @database_engines.setter
    def database_engines(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @types.setter
    def types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetDisabledArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetDisabledArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigTargetCloudSqlTargetFilterArgsDict(TypedDict):
    collection: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionArgsDict
        ]
    ]
    database_resource_reference: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetFilterDatabaseResourceReferenceArgsDict
        ]
    ]
    others: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetFilterOthersArgsDict]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterArgs:
    def __init__(
        __self__,
        *,
        collection: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionArgs
            ]
        ] = ...,
        database_resource_reference: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetFilterDatabaseResourceReferenceArgs
            ]
        ] = ...,
        others: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetFilterOthersArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionArgs]
    ]: ...
    @collection.setter
    def collection(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="databaseResourceReference")
    def database_resource_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetFilterDatabaseResourceReferenceArgs
        ]
    ]: ...
    @database_resource_reference.setter
    def database_resource_reference(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetFilterDatabaseResourceReferenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def others(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetFilterOthersArgs]
    ]: ...
    @others.setter
    def others(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudSqlTargetFilterOthersArgs]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionArgsDict(TypedDict):
    include_regexes: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionArgs:
    def __init__(
        __self__,
        *,
        include_regexes: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesArgs
        ]
    ]: ...
    @include_regexes.setter
    def include_regexes(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesArgsDict(
    TypedDict
):
    patterns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesPatternArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesArgs:
    def __init__(
        __self__,
        *,
        patterns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesPatternArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def patterns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesPatternArgs
                ]
            ]
        ]
    ]: ...
    @patterns.setter
    def patterns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesPatternArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesPatternArgsDict(
    TypedDict
):
    database_regex: NotRequired[pulumi.Input[_builtins.str]]
    database_resource_name_regex: NotRequired[pulumi.Input[_builtins.str]]
    instance_regex: NotRequired[pulumi.Input[_builtins.str]]
    project_id_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesPatternArgs:
    def __init__(
        __self__,
        *,
        database_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        database_resource_name_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="databaseRegex")
    def database_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_regex.setter
    def database_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="databaseResourceNameRegex")
    def database_resource_name_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @database_resource_name_regex.setter
    def database_resource_name_regex(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceRegex")
    def instance_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_regex.setter
    def instance_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectIdRegex")
    def project_id_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id_regex.setter
    def project_id_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetFilterDatabaseResourceReferenceArgsDict(
    TypedDict
):
    database: pulumi.Input[_builtins.str]
    database_resource: pulumi.Input[_builtins.str]
    instance: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterDatabaseResourceReferenceArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        database_resource: pulumi.Input[_builtins.str],
        instance: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="databaseResource")
    def database_resource(self) -> pulumi.Input[_builtins.str]: ...
    @database_resource.setter
    def database_resource(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> pulumi.Input[_builtins.str]: ...
    @instance.setter
    def instance(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetFilterOthersArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterOthersArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceArgsDict(TypedDict):
    inspect_template_modified_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceInspectTemplateModifiedCadenceArgsDict
        ]
    ]
    refresh_frequency: NotRequired[pulumi.Input[_builtins.str]]
    schema_modified_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceSchemaModifiedCadenceArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceArgs:
    def __init__(
        __self__,
        *,
        inspect_template_modified_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceInspectTemplateModifiedCadenceArgs
            ]
        ] = ...,
        refresh_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_modified_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceSchemaModifiedCadenceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplateModifiedCadence")
    def inspect_template_modified_cadence(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceInspectTemplateModifiedCadenceArgs
        ]
    ]: ...
    @inspect_template_modified_cadence.setter
    def inspect_template_modified_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceInspectTemplateModifiedCadenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="refreshFrequency")
    def refresh_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refresh_frequency.setter
    def refresh_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaModifiedCadence")
    def schema_modified_cadence(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceSchemaModifiedCadenceArgs
        ]
    ]: ...
    @schema_modified_cadence.setter
    def schema_modified_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceSchemaModifiedCadenceArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceInspectTemplateModifiedCadenceArgsDict(
    TypedDict
):
    frequency: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceInspectTemplateModifiedCadenceArgs:
    def __init__(__self__, *, frequency: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[_builtins.str]: ...
    @frequency.setter
    def frequency(self, value: pulumi.Input[_builtins.str]): ...

class PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceSchemaModifiedCadenceArgsDict(
    TypedDict
):
    frequency: NotRequired[pulumi.Input[_builtins.str]]
    types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceSchemaModifiedCadenceArgs:
    def __init__(
        __self__,
        *,
        frequency: Optional[pulumi.Input[_builtins.str]] = ...,
        types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @types.setter
    def types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetArgsDict(TypedDict):
    filter: pulumi.Input[
        PreventionDiscoveryConfigTargetCloudStorageTargetFilterArgsDict
    ]
    conditions: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetConditionsArgsDict
        ]
    ]
    disabled: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetDisabledArgsDict]
    ]
    generation_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetArgs:
    def __init__(
        __self__,
        *,
        filter: pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterArgs
        ],
        conditions: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetConditionsArgs
            ]
        ] = ...,
        disabled: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetDisabledArgs]
        ] = ...,
        generation_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetFilterArgs]: ...
    @filter.setter
    def filter(
        self,
        value: pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetConditionsArgs]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetConditionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetDisabledArgs]
    ]: ...
    @disabled.setter
    def disabled(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetDisabledArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="generationCadence")
    def generation_cadence(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceArgs
        ]
    ]: ...
    @generation_cadence.setter
    def generation_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetConditionsArgsDict(TypedDict):
    cloud_storage_conditions: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetConditionsCloudStorageConditionsArgsDict
        ]
    ]
    created_after: NotRequired[pulumi.Input[_builtins.str]]
    min_age: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetConditionsArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_conditions: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetConditionsCloudStorageConditionsArgs
            ]
        ] = ...,
        created_after: Optional[pulumi.Input[_builtins.str]] = ...,
        min_age: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageConditions")
    def cloud_storage_conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetConditionsCloudStorageConditionsArgs
        ]
    ]: ...
    @cloud_storage_conditions.setter
    def cloud_storage_conditions(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetConditionsCloudStorageConditionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdAfter")
    def created_after(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_after.setter
    def created_after(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minAge")
    def min_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_age.setter
    def min_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetConditionsCloudStorageConditionsArgsDict(
    TypedDict
):
    included_bucket_attributes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    included_object_attributes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetConditionsCloudStorageConditionsArgs:
    def __init__(
        __self__,
        *,
        included_bucket_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        included_object_attributes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includedBucketAttributes")
    def included_bucket_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_bucket_attributes.setter
    def included_bucket_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedObjectAttributes")
    def included_object_attributes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @included_object_attributes.setter
    def included_object_attributes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetDisabledArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetDisabledArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigTargetCloudStorageTargetFilterArgsDict(TypedDict):
    cloud_storage_resource_reference: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCloudStorageResourceReferenceArgsDict
        ]
    ]
    collection: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionArgsDict
        ]
    ]
    others: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterOthersArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_resource_reference: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCloudStorageResourceReferenceArgs
            ]
        ] = ...,
        collection: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionArgs
            ]
        ] = ...,
        others: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterOthersArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageResourceReference")
    def cloud_storage_resource_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCloudStorageResourceReferenceArgs
        ]
    ]: ...
    @cloud_storage_resource_reference.setter
    def cloud_storage_resource_reference(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCloudStorageResourceReferenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def collection(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionArgs
        ]
    ]: ...
    @collection.setter
    def collection(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def others(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetCloudStorageTargetFilterOthersArgs]
    ]: ...
    @others.setter
    def others(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterOthersArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCloudStorageResourceReferenceArgsDict(
    TypedDict
):
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCloudStorageResourceReferenceArgs:
    def __init__(
        __self__,
        *,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionArgsDict(
    TypedDict
):
    include_regexes: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesArgsDict
        ]
    ]
    include_tags: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionArgs:
    def __init__(
        __self__,
        *,
        include_regexes: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesArgs
            ]
        ] = ...,
        include_tags: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesArgs
        ]
    ]: ...
    @include_regexes.setter
    def include_regexes(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeTags")
    def include_tags(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsArgs
        ]
    ]: ...
    @include_tags.setter
    def include_tags(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesArgsDict(
    TypedDict
):
    patterns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesArgs:
    def __init__(
        __self__,
        *,
        patterns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def patterns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternArgs
                ]
            ]
        ]
    ]: ...
    @patterns.setter
    def patterns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternArgsDict(
    TypedDict
):
    cloud_storage_regex: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternCloudStorageRegexArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_regex: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternCloudStorageRegexArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageRegex")
    def cloud_storage_regex(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternCloudStorageRegexArgs
        ]
    ]: ...
    @cloud_storage_regex.setter
    def cloud_storage_regex(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternCloudStorageRegexArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternCloudStorageRegexArgsDict(
    TypedDict
):
    bucket_name_regex: NotRequired[pulumi.Input[_builtins.str]]
    project_id_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternCloudStorageRegexArgs:
    def __init__(
        __self__,
        *,
        bucket_name_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketNameRegex")
    def bucket_name_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name_regex.setter
    def bucket_name_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectIdRegex")
    def project_id_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id_regex.setter
    def project_id_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsArgsDict(
    TypedDict
):
    tag_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsTagFilterArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsArgs:
    def __init__(
        __self__,
        *,
        tag_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsTagFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tagFilters")
    def tag_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsTagFilterArgs
                ]
            ]
        ]
    ]: ...
    @tag_filters.setter
    def tag_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsTagFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsTagFilterArgsDict(
    TypedDict
):
    namespaced_tag_key: NotRequired[pulumi.Input[_builtins.str]]
    namespaced_tag_value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsTagFilterArgs:
    def __init__(
        __self__,
        *,
        namespaced_tag_key: Optional[pulumi.Input[_builtins.str]] = ...,
        namespaced_tag_value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="namespacedTagKey")
    def namespaced_tag_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespaced_tag_key.setter
    def namespaced_tag_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namespacedTagValue")
    def namespaced_tag_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespaced_tag_value.setter
    def namespaced_tag_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetFilterOthersArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterOthersArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceArgsDict(
    TypedDict
):
    inspect_template_modified_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceInspectTemplateModifiedCadenceArgsDict
        ]
    ]
    refresh_frequency: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceArgs:
    def __init__(
        __self__,
        *,
        inspect_template_modified_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceInspectTemplateModifiedCadenceArgs
            ]
        ] = ...,
        refresh_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplateModifiedCadence")
    def inspect_template_modified_cadence(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceInspectTemplateModifiedCadenceArgs
        ]
    ]: ...
    @inspect_template_modified_cadence.setter
    def inspect_template_modified_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceInspectTemplateModifiedCadenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="refreshFrequency")
    def refresh_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refresh_frequency.setter
    def refresh_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceInspectTemplateModifiedCadenceArgsDict(
    TypedDict
):
    frequency: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceInspectTemplateModifiedCadenceArgs:
    def __init__(
        __self__, *, frequency: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetArgsDict(TypedDict):
    filter: pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetFilterArgsDict]
    conditions: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetConditionsArgsDict]
    ]
    data_source_type: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetDataSourceTypeArgsDict
        ]
    ]
    disabled: NotRequired[
        pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetDisabledArgsDict]
    ]
    generation_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetArgs:
    def __init__(
        __self__,
        *,
        filter: pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetFilterArgs],
        conditions: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetConditionsArgs]
        ] = ...,
        data_source_type: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetDataSourceTypeArgs
            ]
        ] = ...,
        disabled: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetDisabledArgs]
        ] = ...,
        generation_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(
        self,
    ) -> pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetFilterArgs]: ...
    @filter.setter
    def filter(
        self,
        value: pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetFilterArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetConditionsArgs]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetConditionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetDataSourceTypeArgs]
    ]: ...
    @data_source_type.setter
    def data_source_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetDataSourceTypeArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetDisabledArgs]
    ]: ...
    @disabled.setter
    def disabled(
        self,
        value: Optional[
            pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetDisabledArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="generationCadence")
    def generation_cadence(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceArgs
        ]
    ]: ...
    @generation_cadence.setter
    def generation_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetConditionsArgsDict(TypedDict):
    amazon_s3_bucket_conditions: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetConditionsAmazonS3BucketConditionsArgsDict
        ]
    ]
    min_age: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetConditionsArgs:
    def __init__(
        __self__,
        *,
        amazon_s3_bucket_conditions: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetConditionsAmazonS3BucketConditionsArgs
            ]
        ] = ...,
        min_age: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonS3BucketConditions")
    def amazon_s3_bucket_conditions(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetConditionsAmazonS3BucketConditionsArgs
        ]
    ]: ...
    @amazon_s3_bucket_conditions.setter
    def amazon_s3_bucket_conditions(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetConditionsAmazonS3BucketConditionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minAge")
    def min_age(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_age.setter
    def min_age(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetConditionsAmazonS3BucketConditionsArgsDict(
    TypedDict
):
    bucket_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    object_storage_classes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetConditionsAmazonS3BucketConditionsArgs:
    def __init__(
        __self__,
        *,
        bucket_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        object_storage_classes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketTypes")
    def bucket_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @bucket_types.setter
    def bucket_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="objectStorageClasses")
    def object_storage_classes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @object_storage_classes.setter
    def object_storage_classes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetDataSourceTypeArgsDict(TypedDict):
    data_source: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetDataSourceTypeArgs:
    def __init__(
        __self__, *, data_source: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetDisabledArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetDisabledArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterArgsDict(TypedDict):
    collection: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionArgsDict
        ]
    ]
    others: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterOthersArgsDict
        ]
    ]
    single_resource: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterArgs:
    def __init__(
        __self__,
        *,
        collection: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionArgs
            ]
        ] = ...,
        others: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterOthersArgs
            ]
        ] = ...,
        single_resource: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionArgs
        ]
    ]: ...
    @collection.setter
    def collection(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def others(
        self,
    ) -> Optional[
        pulumi.Input[PreventionDiscoveryConfigTargetOtherCloudTargetFilterOthersArgs]
    ]: ...
    @others.setter
    def others(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterOthersArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="singleResource")
    def single_resource(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceArgs
        ]
    ]: ...
    @single_resource.setter
    def single_resource(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionArgsDict(
    TypedDict
):
    include_regexes: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionArgs:
    def __init__(
        __self__,
        *,
        include_regexes: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesArgs
        ]
    ]: ...
    @include_regexes.setter
    def include_regexes(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesArgsDict(
    TypedDict
):
    patterns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesArgs:
    def __init__(
        __self__,
        *,
        patterns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def patterns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternArgs
                ]
            ]
        ]
    ]: ...
    @patterns.setter
    def patterns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternArgsDict(
    TypedDict
):
    amazon_s3_bucket_regex: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternArgs:
    def __init__(
        __self__,
        *,
        amazon_s3_bucket_regex: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonS3BucketRegex")
    def amazon_s3_bucket_regex(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexArgs
        ]
    ]: ...
    @amazon_s3_bucket_regex.setter
    def amazon_s3_bucket_regex(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexArgsDict(
    TypedDict
):
    aws_account_regex: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexAwsAccountRegexArgsDict
        ]
    ]
    bucket_name_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexArgs:
    def __init__(
        __self__,
        *,
        aws_account_regex: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexAwsAccountRegexArgs
            ]
        ] = ...,
        bucket_name_regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountRegex")
    def aws_account_regex(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexAwsAccountRegexArgs
        ]
    ]: ...
    @aws_account_regex.setter
    def aws_account_regex(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexAwsAccountRegexArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bucketNameRegex")
    def bucket_name_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name_regex.setter
    def bucket_name_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexAwsAccountRegexArgsDict(
    TypedDict
):
    account_id_regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexAwsAccountRegexArgs:
    def __init__(
        __self__, *, account_id_regex: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountIdRegex")
    def account_id_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id_regex.setter
    def account_id_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterOthersArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterOthersArgs:
    def __init__(__self__) -> None: ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceArgsDict(
    TypedDict
):
    amazon_s3_bucket: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceArgs:
    def __init__(
        __self__,
        *,
        amazon_s3_bucket: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonS3Bucket")
    def amazon_s3_bucket(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketArgs
        ]
    ]: ...
    @amazon_s3_bucket.setter
    def amazon_s3_bucket(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketArgs
            ]
        ],
    ): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketArgsDict(
    TypedDict
):
    aws_account: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketAwsAccountArgsDict
        ]
    ]
    bucket_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketArgs:
    def __init__(
        __self__,
        *,
        aws_account: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketAwsAccountArgs
            ]
        ] = ...,
        bucket_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccount")
    def aws_account(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketAwsAccountArgs
        ]
    ]: ...
    @aws_account.setter
    def aws_account(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketAwsAccountArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketAwsAccountArgsDict(
    TypedDict
):
    account_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketAwsAccountArgs:
    def __init__(
        __self__, *, account_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceArgsDict(
    TypedDict
):
    inspect_template_modified_cadence: NotRequired[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceInspectTemplateModifiedCadenceArgsDict
        ]
    ]
    refresh_frequency: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceArgs:
    def __init__(
        __self__,
        *,
        inspect_template_modified_cadence: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceInspectTemplateModifiedCadenceArgs
            ]
        ] = ...,
        refresh_frequency: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplateModifiedCadence")
    def inspect_template_modified_cadence(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceInspectTemplateModifiedCadenceArgs
        ]
    ]: ...
    @inspect_template_modified_cadence.setter
    def inspect_template_modified_cadence(
        self,
        value: Optional[
            pulumi.Input[
                PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceInspectTemplateModifiedCadenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="refreshFrequency")
    def refresh_frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @refresh_frequency.setter
    def refresh_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceInspectTemplateModifiedCadenceArgsDict(
    TypedDict
):
    frequency: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceInspectTemplateModifiedCadenceArgs:
    def __init__(
        __self__, *, frequency: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionDiscoveryConfigTargetSecretsTargetArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionDiscoveryConfigTargetSecretsTargetArgs:
    def __init__(__self__) -> None: ...

class PreventionInspectTemplateInspectConfigArgsDict(TypedDict):
    content_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    custom_info_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionInspectTemplateInspectConfigCustomInfoTypeArgsDict
                ]
            ]
        ]
    ]
    exclude_info_types: NotRequired[pulumi.Input[_builtins.bool]]
    include_quote: NotRequired[pulumi.Input[_builtins.bool]]
    info_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PreventionInspectTemplateInspectConfigInfoTypeArgsDict]
            ]
        ]
    ]
    limits: NotRequired[
        pulumi.Input[PreventionInspectTemplateInspectConfigLimitsArgsDict]
    ]
    min_likelihood: NotRequired[pulumi.Input[_builtins.str]]
    rule_sets: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigArgs:
    def __init__(
        __self__,
        *,
        content_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_info_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionInspectTemplateInspectConfigCustomInfoTypeArgs
                    ]
                ]
            ]
        ] = ...,
        exclude_info_types: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_quote: Optional[pulumi.Input[_builtins.bool]] = ...,
        info_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PreventionInspectTemplateInspectConfigInfoTypeArgs]
                ]
            ]
        ] = ...,
        limits: Optional[
            pulumi.Input[PreventionInspectTemplateInspectConfigLimitsArgs]
        ] = ...,
        min_likelihood: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_sets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contentOptions")
    def content_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @content_options.setter
    def content_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customInfoTypes")
    def custom_info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PreventionInspectTemplateInspectConfigCustomInfoTypeArgs]
            ]
        ]
    ]: ...
    @custom_info_types.setter
    def custom_info_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionInspectTemplateInspectConfigCustomInfoTypeArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeInfoTypes")
    def exclude_info_types(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exclude_info_types.setter
    def exclude_info_types(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeQuote")
    def include_quote(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_quote.setter
    def include_quote(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PreventionInspectTemplateInspectConfigInfoTypeArgs]]
        ]
    ]: ...
    @info_types.setter
    def info_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PreventionInspectTemplateInspectConfigInfoTypeArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Optional[pulumi.Input[PreventionInspectTemplateInspectConfigLimitsArgs]]: ...
    @limits.setter
    def limits(
        self,
        value: Optional[pulumi.Input[PreventionInspectTemplateInspectConfigLimitsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minLikelihood")
    def min_likelihood(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_likelihood.setter
    def min_likelihood(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetArgs]]
        ]
    ]: ...
    @rule_sets.setter
    def rule_sets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetArgs]
                ]
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeArgsDict(TypedDict):
    info_type: pulumi.Input[
        PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeArgsDict
    ]
    dictionary: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryArgsDict
        ]
    ]
    exclusion_type: NotRequired[pulumi.Input[_builtins.str]]
    likelihood: NotRequired[pulumi.Input[_builtins.str]]
    regex: NotRequired[
        pulumi.Input[PreventionInspectTemplateInspectConfigCustomInfoTypeRegexArgsDict]
    ]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeSensitivityScoreArgsDict
        ]
    ]
    stored_type: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeStoredTypeArgsDict
        ]
    ]
    surrogate_type: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeSurrogateTypeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeArgs:
    def __init__(
        __self__,
        *,
        info_type: pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeArgs
        ],
        dictionary: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryArgs
            ]
        ] = ...,
        exclusion_type: Optional[pulumi.Input[_builtins.str]] = ...,
        likelihood: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[
            pulumi.Input[PreventionInspectTemplateInspectConfigCustomInfoTypeRegexArgs]
        ] = ...,
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        stored_type: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeStoredTypeArgs
            ]
        ] = ...,
        surrogate_type: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeSurrogateTypeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infoType")
    def info_type(
        self,
    ) -> pulumi.Input[
        PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeArgs
    ]: ...
    @info_type.setter
    def info_type(
        self,
        value: pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dictionary(
        self,
    ) -> Optional[
        pulumi.Input[PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryArgs]
    ]: ...
    @dictionary.setter
    def dictionary(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="exclusionType")
    def exclusion_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exclusion_type.setter
    def exclusion_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def likelihood(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @likelihood.setter
    def likelihood(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(
        self,
    ) -> Optional[
        pulumi.Input[PreventionInspectTemplateInspectConfigCustomInfoTypeRegexArgs]
    ]: ...
    @regex.setter
    def regex(
        self,
        value: Optional[
            pulumi.Input[PreventionInspectTemplateInspectConfigCustomInfoTypeRegexArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storedType")
    def stored_type(
        self,
    ) -> Optional[
        pulumi.Input[PreventionInspectTemplateInspectConfigCustomInfoTypeStoredTypeArgs]
    ]: ...
    @stored_type.setter
    def stored_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeStoredTypeArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="surrogateType")
    def surrogate_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeSurrogateTypeArgs
        ]
    ]: ...
    @surrogate_type.setter
    def surrogate_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeSurrogateTypeArgs
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryArgsDict(TypedDict):
    cloud_storage_path: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgsDict
        ]
    ]
    word_list: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryWordListArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_path: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgs
            ]
        ] = ...,
        word_list: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryWordListArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgs
        ]
    ]: ...
    @cloud_storage_path.setter
    def cloud_storage_path(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryWordListArgs
        ]
    ]: ...
    @word_list.setter
    def word_list(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryWordListArgs
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgsDict(
    TypedDict
):
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryWordListArgsDict(
    TypedDict
):
    words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryWordListArgs:
    def __init__(
        __self__, *, words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def words(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @words.setter
    def words(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeRegexArgsDict(TypedDict):
    pattern: pulumi.Input[_builtins.str]
    group_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeRegexArgs:
    def __init__(
        __self__,
        *,
        pattern: pulumi.Input[_builtins.str],
        group_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @group_indexes.setter
    def group_indexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeStoredTypeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeStoredTypeArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionInspectTemplateInspectConfigCustomInfoTypeSurrogateTypeArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeSurrogateTypeArgs:
    def __init__(__self__) -> None: ...

class PreventionInspectTemplateInspectConfigInfoTypeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[PreventionInspectTemplateInspectConfigInfoTypeSensitivityScoreArgs]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionInspectTemplateInspectConfigInfoTypeSensitivityScoreArgsDict(TypedDict):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionInspectTemplateInspectConfigLimitsArgsDict(TypedDict):
    max_findings_per_item: pulumi.Input[_builtins.int]
    max_findings_per_request: pulumi.Input[_builtins.int]
    max_findings_per_info_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigLimitsArgs:
    def __init__(
        __self__,
        *,
        max_findings_per_item: pulumi.Input[_builtins.int],
        max_findings_per_request: pulumi.Input[_builtins.int],
        max_findings_per_info_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerItem")
    def max_findings_per_item(self) -> pulumi.Input[_builtins.int]: ...
    @max_findings_per_item.setter
    def max_findings_per_item(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerRequest")
    def max_findings_per_request(self) -> pulumi.Input[_builtins.int]: ...
    @max_findings_per_request.setter
    def max_findings_per_request(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerInfoTypes")
    def max_findings_per_info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeArgs
                ]
            ]
        ]
    ]: ...
    @max_findings_per_info_types.setter
    def max_findings_per_info_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeArgsDict(
    TypedDict
):
    max_findings: pulumi.Input[_builtins.int]
    info_type: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeArgs:
    def __init__(
        __self__,
        *,
        max_findings: pulumi.Input[_builtins.int],
        info_type: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxFindings")
    def max_findings(self) -> pulumi.Input[_builtins.int]: ...
    @max_findings.setter
    def max_findings(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="infoType")
    def info_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgs
        ]
    ]: ...
    @info_type.setter
    def info_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgs
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionInspectTemplateInspectConfigRuleSetArgsDict(TypedDict):
    info_types: pulumi.Input[
        Sequence[
            pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgsDict]
        ]
    ]
    rules: pulumi.Input[
        Sequence[
            pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetRuleArgsDict]
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetArgs:
    def __init__(
        __self__,
        *,
        info_types: pulumi.Input[
            Sequence[
                pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs]
            ]
        ],
        rules: pulumi.Input[
            Sequence[
                pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetRuleArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs]
        ]
    ]: ...
    @info_types.setter
    def info_types(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetRuleArgs]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetRuleArgs]
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionInspectTemplateInspectConfigRuleSetInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleArgsDict(TypedDict):
    exclusion_rule: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleArgsDict
        ]
    ]
    hotword_rule: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleArgs:
    def __init__(
        __self__,
        *,
        exclusion_rule: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleArgs
            ]
        ] = ...,
        hotword_rule: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exclusionRule")
    def exclusion_rule(
        self,
    ) -> Optional[
        pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleArgs]
    ]: ...
    @exclusion_rule.setter
    def exclusion_rule(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hotwordRule")
    def hotword_rule(
        self,
    ) -> Optional[
        pulumi.Input[PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleArgs]
    ]: ...
    @hotword_rule.setter
    def hotword_rule(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleArgs
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleArgsDict(TypedDict):
    matching_type: pulumi.Input[_builtins.str]
    dictionary: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryArgsDict
        ]
    ]
    exclude_by_hotword: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgsDict
        ]
    ]
    exclude_info_types: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgsDict
        ]
    ]
    regex: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegexArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleArgs:
    def __init__(
        __self__,
        *,
        matching_type: pulumi.Input[_builtins.str],
        dictionary: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryArgs
            ]
        ] = ...,
        exclude_by_hotword: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgs
            ]
        ] = ...,
        exclude_info_types: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgs
            ]
        ] = ...,
        regex: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegexArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchingType")
    def matching_type(self) -> pulumi.Input[_builtins.str]: ...
    @matching_type.setter
    def matching_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dictionary(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryArgs
        ]
    ]: ...
    @dictionary.setter
    def dictionary(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeByHotword")
    def exclude_by_hotword(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgs
        ]
    ]: ...
    @exclude_by_hotword.setter
    def exclude_by_hotword(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeInfoTypes")
    def exclude_info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgs
        ]
    ]: ...
    @exclude_info_types.setter
    def exclude_info_types(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regex(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegexArgs
        ]
    ]: ...
    @regex.setter
    def regex(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegexArgs
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryArgsDict(
    TypedDict
):
    cloud_storage_path: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgsDict
        ]
    ]
    word_list: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_path: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgs
            ]
        ] = ...,
        word_list: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgs
        ]
    ]: ...
    @cloud_storage_path.setter
    def cloud_storage_path(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgs
        ]
    ]: ...
    @word_list.setter
    def word_list(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgs
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgsDict(
    TypedDict
):
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgsDict(
    TypedDict
):
    words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgs:
    def __init__(
        __self__, *, words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def words(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @words.setter
    def words(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgsDict(
    TypedDict
):
    hotword_regex: pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgsDict
    ]
    proximity: pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgsDict
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgs:
    def __init__(
        __self__,
        *,
        hotword_regex: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgs
        ],
        proximity: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hotwordRegex")
    def hotword_regex(
        self,
    ) -> pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgs
    ]: ...
    @hotword_regex.setter
    def hotword_regex(
        self,
        value: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def proximity(
        self,
    ) -> pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgs
    ]: ...
    @proximity.setter
    def proximity(
        self,
        value: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgs
        ],
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgsDict(
    TypedDict
):
    pattern: pulumi.Input[_builtins.str]
    group_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgs:
    def __init__(
        __self__,
        *,
        pattern: pulumi.Input[_builtins.str],
        group_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @group_indexes.setter
    def group_indexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgsDict(
    TypedDict
):
    window_after: NotRequired[pulumi.Input[_builtins.int]]
    window_before: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgs:
    def __init__(
        __self__,
        *,
        window_after: Optional[pulumi.Input[_builtins.int]] = ...,
        window_before: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="windowAfter")
    def window_after(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @window_after.setter
    def window_after(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="windowBefore")
    def window_before(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @window_before.setter
    def window_before(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgsDict(
    TypedDict
):
    info_types: pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgs:
    def __init__(
        __self__,
        *,
        info_types: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgs
            ]
        ]
    ]: ...
    @info_types.setter
    def info_types(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgs
                ]
            ]
        ],
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegexArgsDict(
    TypedDict
):
    pattern: pulumi.Input[_builtins.str]
    group_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegexArgs:
    def __init__(
        __self__,
        *,
        pattern: pulumi.Input[_builtins.str],
        group_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @group_indexes.setter
    def group_indexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleArgsDict(TypedDict):
    hotword_regex: pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgsDict
    ]
    likelihood_adjustment: pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgsDict
    ]
    proximity: pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximityArgsDict
    ]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleArgs:
    def __init__(
        __self__,
        *,
        hotword_regex: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs
        ],
        likelihood_adjustment: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs
        ],
        proximity: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximityArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hotwordRegex")
    def hotword_regex(
        self,
    ) -> pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs
    ]: ...
    @hotword_regex.setter
    def hotword_regex(
        self,
        value: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="likelihoodAdjustment")
    def likelihood_adjustment(
        self,
    ) -> pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs
    ]: ...
    @likelihood_adjustment.setter
    def likelihood_adjustment(
        self,
        value: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def proximity(
        self,
    ) -> pulumi.Input[
        PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximityArgs
    ]: ...
    @proximity.setter
    def proximity(
        self,
        value: pulumi.Input[
            PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximityArgs
        ],
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgsDict(
    TypedDict
):
    pattern: pulumi.Input[_builtins.str]
    group_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs:
    def __init__(
        __self__,
        *,
        pattern: pulumi.Input[_builtins.str],
        group_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @group_indexes.setter
    def group_indexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgsDict(
    TypedDict
):
    fixed_likelihood: NotRequired[pulumi.Input[_builtins.str]]
    relative_likelihood: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs:
    def __init__(
        __self__,
        *,
        fixed_likelihood: Optional[pulumi.Input[_builtins.str]] = ...,
        relative_likelihood: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedLikelihood")
    def fixed_likelihood(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fixed_likelihood.setter
    def fixed_likelihood(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relativeLikelihood")
    def relative_likelihood(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @relative_likelihood.setter
    def relative_likelihood(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximityArgsDict(
    TypedDict
):
    window_after: NotRequired[pulumi.Input[_builtins.int]]
    window_before: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximityArgs:
    def __init__(
        __self__,
        *,
        window_after: Optional[pulumi.Input[_builtins.int]] = ...,
        window_before: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="windowAfter")
    def window_after(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @window_after.setter
    def window_after(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="windowBefore")
    def window_before(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @window_before.setter
    def window_before(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionJobTriggerInspectJobArgsDict(TypedDict):
    storage_config: pulumi.Input[PreventionJobTriggerInspectJobStorageConfigArgsDict]
    actions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[PreventionJobTriggerInspectJobActionArgsDict]]
        ]
    ]
    inspect_config: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobInspectConfigArgsDict]
    ]
    inspect_template_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobArgs:
    def __init__(
        __self__,
        *,
        storage_config: pulumi.Input[PreventionJobTriggerInspectJobStorageConfigArgs],
        actions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PreventionJobTriggerInspectJobActionArgs]]
            ]
        ] = ...,
        inspect_config: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobInspectConfigArgs]
        ] = ...,
        inspect_template_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="storageConfig")
    def storage_config(
        self,
    ) -> pulumi.Input[PreventionJobTriggerInspectJobStorageConfigArgs]: ...
    @storage_config.setter
    def storage_config(
        self, value: pulumi.Input[PreventionJobTriggerInspectJobStorageConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PreventionJobTriggerInspectJobActionArgs]]]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[PreventionJobTriggerInspectJobActionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inspectConfig")
    def inspect_config(
        self,
    ) -> Optional[pulumi.Input[PreventionJobTriggerInspectJobInspectConfigArgs]]: ...
    @inspect_config.setter
    def inspect_config(
        self,
        value: Optional[pulumi.Input[PreventionJobTriggerInspectJobInspectConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplateName")
    def inspect_template_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inspect_template_name.setter
    def inspect_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobActionArgsDict(TypedDict):
    deidentify: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobActionDeidentifyArgsDict]
    ]
    job_notification_emails: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobActionJobNotificationEmailsArgsDict]
    ]
    pub_sub: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobActionPubSubArgsDict]
    ]
    publish_findings_to_cloud_data_catalog: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionPublishFindingsToCloudDataCatalogArgsDict
        ]
    ]
    publish_findings_to_dataplex_catalog: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionPublishFindingsToDataplexCatalogArgsDict
        ]
    ]
    publish_summary_to_cscc: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobActionPublishSummaryToCsccArgsDict]
    ]
    publish_to_stackdriver: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobActionPublishToStackdriverArgsDict]
    ]
    save_findings: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobActionSaveFindingsArgsDict]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionArgs:
    def __init__(
        __self__,
        *,
        deidentify: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionDeidentifyArgs]
        ] = ...,
        job_notification_emails: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionJobNotificationEmailsArgs]
        ] = ...,
        pub_sub: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionPubSubArgs]
        ] = ...,
        publish_findings_to_cloud_data_catalog: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionPublishFindingsToCloudDataCatalogArgs
            ]
        ] = ...,
        publish_findings_to_dataplex_catalog: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionPublishFindingsToDataplexCatalogArgs
            ]
        ] = ...,
        publish_summary_to_cscc: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionPublishSummaryToCsccArgs]
        ] = ...,
        publish_to_stackdriver: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionPublishToStackdriverArgs]
        ] = ...,
        save_findings: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionSaveFindingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def deidentify(
        self,
    ) -> Optional[pulumi.Input[PreventionJobTriggerInspectJobActionDeidentifyArgs]]: ...
    @deidentify.setter
    def deidentify(
        self,
        value: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionDeidentifyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobNotificationEmails")
    def job_notification_emails(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobActionJobNotificationEmailsArgs]
    ]: ...
    @job_notification_emails.setter
    def job_notification_emails(
        self,
        value: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionJobNotificationEmailsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pubSub")
    def pub_sub(
        self,
    ) -> Optional[pulumi.Input[PreventionJobTriggerInspectJobActionPubSubArgs]]: ...
    @pub_sub.setter
    def pub_sub(
        self,
        value: Optional[pulumi.Input[PreventionJobTriggerInspectJobActionPubSubArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishFindingsToCloudDataCatalog")
    @_utilities.deprecated(...)
    def publish_findings_to_cloud_data_catalog(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionPublishFindingsToCloudDataCatalogArgs
        ]
    ]: ...
    @publish_findings_to_cloud_data_catalog.setter
    def publish_findings_to_cloud_data_catalog(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionPublishFindingsToCloudDataCatalogArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishFindingsToDataplexCatalog")
    def publish_findings_to_dataplex_catalog(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionPublishFindingsToDataplexCatalogArgs
        ]
    ]: ...
    @publish_findings_to_dataplex_catalog.setter
    def publish_findings_to_dataplex_catalog(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionPublishFindingsToDataplexCatalogArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishSummaryToCscc")
    def publish_summary_to_cscc(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobActionPublishSummaryToCsccArgs]
    ]: ...
    @publish_summary_to_cscc.setter
    def publish_summary_to_cscc(
        self,
        value: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionPublishSummaryToCsccArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishToStackdriver")
    def publish_to_stackdriver(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobActionPublishToStackdriverArgs]
    ]: ...
    @publish_to_stackdriver.setter
    def publish_to_stackdriver(
        self,
        value: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionPublishToStackdriverArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="saveFindings")
    def save_findings(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobActionSaveFindingsArgs]
    ]: ...
    @save_findings.setter
    def save_findings(
        self,
        value: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobActionSaveFindingsArgs]
        ],
    ): ...

class PreventionJobTriggerInspectJobActionDeidentifyArgsDict(TypedDict):
    cloud_storage_output: pulumi.Input[_builtins.str]
    file_types_to_transforms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    transformation_config: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionDeidentifyTransformationConfigArgsDict
        ]
    ]
    transformation_details_storage_config: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionDeidentifyArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_output: pulumi.Input[_builtins.str],
        file_types_to_transforms: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        transformation_config: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionDeidentifyTransformationConfigArgs
            ]
        ] = ...,
        transformation_details_storage_config: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageOutput")
    def cloud_storage_output(self) -> pulumi.Input[_builtins.str]: ...
    @cloud_storage_output.setter
    def cloud_storage_output(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fileTypesToTransforms")
    def file_types_to_transforms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_types_to_transforms.setter
    def file_types_to_transforms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transformationConfig")
    def transformation_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionDeidentifyTransformationConfigArgs
        ]
    ]: ...
    @transformation_config.setter
    def transformation_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionDeidentifyTransformationConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="transformationDetailsStorageConfig")
    def transformation_details_storage_config(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigArgs
        ]
    ]: ...
    @transformation_details_storage_config.setter
    def transformation_details_storage_config(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobActionDeidentifyTransformationConfigArgsDict(
    TypedDict
):
    deidentify_template: NotRequired[pulumi.Input[_builtins.str]]
    image_redact_template: NotRequired[pulumi.Input[_builtins.str]]
    structured_deidentify_template: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionDeidentifyTransformationConfigArgs:
    def __init__(
        __self__,
        *,
        deidentify_template: Optional[pulumi.Input[_builtins.str]] = ...,
        image_redact_template: Optional[pulumi.Input[_builtins.str]] = ...,
        structured_deidentify_template: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deidentify_template.setter
    def deidentify_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageRedactTemplate")
    def image_redact_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_redact_template.setter
    def image_redact_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="structuredDeidentifyTemplate")
    def structured_deidentify_template(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @structured_deidentify_template.setter
    def structured_deidentify_template(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigArgsDict(
    TypedDict
):
    table: pulumi.Input[
        PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigTableArgsDict
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigArgs:
    def __init__(
        __self__,
        *,
        table: pulumi.Input[
            PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigTableArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def table(
        self,
    ) -> pulumi.Input[
        PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigTableArgs
    ]: ...
    @table.setter
    def table(
        self,
        value: pulumi.Input[
            PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigTableArgs
        ],
    ): ...

class PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigTableArgsDict(
    TypedDict
):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    table_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigTableArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_id.setter
    def table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobActionJobNotificationEmailsArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionJobNotificationEmailsArgs:
    def __init__(__self__) -> None: ...

class PreventionJobTriggerInspectJobActionPubSubArgsDict(TypedDict):
    topic: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionPubSubArgs:
    def __init__(__self__, *, topic: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobActionPublishFindingsToCloudDataCatalogArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionPublishFindingsToCloudDataCatalogArgs:
    def __init__(__self__) -> None: ...

class PreventionJobTriggerInspectJobActionPublishFindingsToDataplexCatalogArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionPublishFindingsToDataplexCatalogArgs:
    def __init__(__self__) -> None: ...

class PreventionJobTriggerInspectJobActionPublishSummaryToCsccArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionPublishSummaryToCsccArgs:
    def __init__(__self__) -> None: ...

class PreventionJobTriggerInspectJobActionPublishToStackdriverArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionPublishToStackdriverArgs:
    def __init__(__self__) -> None: ...

class PreventionJobTriggerInspectJobActionSaveFindingsArgsDict(TypedDict):
    output_config: pulumi.Input[
        PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigArgsDict
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionSaveFindingsArgs:
    def __init__(
        __self__,
        *,
        output_config: pulumi.Input[
            PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(
        self,
    ) -> pulumi.Input[
        PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigArgs
    ]: ...
    @output_config.setter
    def output_config(
        self,
        value: pulumi.Input[
            PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigArgs
        ],
    ): ...

class PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigArgsDict(TypedDict):
    output_schema: NotRequired[pulumi.Input[_builtins.str]]
    storage_path: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigStoragePathArgsDict
        ]
    ]
    table: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigTableArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigArgs:
    def __init__(
        __self__,
        *,
        output_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_path: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigStoragePathArgs
            ]
        ] = ...,
        table: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigTableArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputSchema")
    def output_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @output_schema.setter
    def output_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storagePath")
    def storage_path(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigStoragePathArgs
        ]
    ]: ...
    @storage_path.setter
    def storage_path(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigStoragePathArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def table(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigTableArgs
        ]
    ]: ...
    @table.setter
    def table(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigTableArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigStoragePathArgsDict(
    TypedDict
):
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigStoragePathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigTableArgsDict(
    TypedDict
):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    table_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigTableArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table_id.setter
    def table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobInspectConfigArgsDict(TypedDict):
    custom_info_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeArgsDict
                ]
            ]
        ]
    ]
    exclude_info_types: NotRequired[pulumi.Input[_builtins.bool]]
    include_quote: NotRequired[pulumi.Input[_builtins.bool]]
    info_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobInspectConfigInfoTypeArgsDict
                ]
            ]
        ]
    ]
    limits: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobInspectConfigLimitsArgsDict]
    ]
    min_likelihood: NotRequired[pulumi.Input[_builtins.str]]
    rule_sets: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[PreventionJobTriggerInspectJobInspectConfigRuleSetArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigArgs:
    def __init__(
        __self__,
        *,
        custom_info_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeArgs
                    ]
                ]
            ]
        ] = ...,
        exclude_info_types: Optional[pulumi.Input[_builtins.bool]] = ...,
        include_quote: Optional[pulumi.Input[_builtins.bool]] = ...,
        info_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobInspectConfigInfoTypeArgs
                    ]
                ]
            ]
        ] = ...,
        limits: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobInspectConfigLimitsArgs]
        ] = ...,
        min_likelihood: Optional[pulumi.Input[_builtins.str]] = ...,
        rule_sets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PreventionJobTriggerInspectJobInspectConfigRuleSetArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customInfoTypes")
    def custom_info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeArgs
                ]
            ]
        ]
    ]: ...
    @custom_info_types.setter
    def custom_info_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeInfoTypes")
    def exclude_info_types(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exclude_info_types.setter
    def exclude_info_types(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="includeQuote")
    def include_quote(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_quote.setter
    def include_quote(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PreventionJobTriggerInspectJobInspectConfigInfoTypeArgs]
            ]
        ]
    ]: ...
    @info_types.setter
    def info_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobInspectConfigInfoTypeArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobInspectConfigLimitsArgs]
    ]: ...
    @limits.setter
    def limits(
        self,
        value: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobInspectConfigLimitsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="minLikelihood")
    def min_likelihood(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @min_likelihood.setter
    def min_likelihood(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[PreventionJobTriggerInspectJobInspectConfigRuleSetArgs]
            ]
        ]
    ]: ...
    @rule_sets.setter
    def rule_sets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[PreventionJobTriggerInspectJobInspectConfigRuleSetArgs]
                ]
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeArgsDict(TypedDict):
    info_type: pulumi.Input[
        PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeArgsDict
    ]
    dictionary: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryArgsDict
        ]
    ]
    exclusion_type: NotRequired[pulumi.Input[_builtins.str]]
    likelihood: NotRequired[pulumi.Input[_builtins.str]]
    regex: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeRegexArgsDict
        ]
    ]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSensitivityScoreArgsDict
        ]
    ]
    stored_type: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeStoredTypeArgsDict
        ]
    ]
    surrogate_type: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSurrogateTypeArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeArgs:
    def __init__(
        __self__,
        *,
        info_type: pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeArgs
        ],
        dictionary: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryArgs
            ]
        ] = ...,
        exclusion_type: Optional[pulumi.Input[_builtins.str]] = ...,
        likelihood: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeRegexArgs
            ]
        ] = ...,
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        stored_type: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeStoredTypeArgs
            ]
        ] = ...,
        surrogate_type: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSurrogateTypeArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infoType")
    def info_type(
        self,
    ) -> pulumi.Input[
        PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeArgs
    ]: ...
    @info_type.setter
    def info_type(
        self,
        value: pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dictionary(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryArgs
        ]
    ]: ...
    @dictionary.setter
    def dictionary(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="exclusionType")
    def exclusion_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @exclusion_type.setter
    def exclusion_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def likelihood(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @likelihood.setter
    def likelihood(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeRegexArgs]
    ]: ...
    @regex.setter
    def regex(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeRegexArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storedType")
    def stored_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeStoredTypeArgs
        ]
    ]: ...
    @stored_type.setter
    def stored_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeStoredTypeArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="surrogateType")
    def surrogate_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSurrogateTypeArgs
        ]
    ]: ...
    @surrogate_type.setter
    def surrogate_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSurrogateTypeArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryArgsDict(
    TypedDict
):
    cloud_storage_path: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgsDict
        ]
    ]
    word_list: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryWordListArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_path: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgs
            ]
        ] = ...,
        word_list: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryWordListArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgs
        ]
    ]: ...
    @cloud_storage_path.setter
    def cloud_storage_path(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryWordListArgs
        ]
    ]: ...
    @word_list.setter
    def word_list(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryWordListArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgsDict(
    TypedDict
):
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryCloudStoragePathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryWordListArgsDict(
    TypedDict
):
    words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryWordListArgs:
    def __init__(
        __self__, *, words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def words(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @words.setter
    def words(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeRegexArgsDict(TypedDict):
    pattern: pulumi.Input[_builtins.str]
    group_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeRegexArgs:
    def __init__(
        __self__,
        *,
        pattern: pulumi.Input[_builtins.str],
        group_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @group_indexes.setter
    def group_indexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeStoredTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeStoredTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSurrogateTypeArgsDict(
    TypedDict
): ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSurrogateTypeArgs:
    def __init__(__self__) -> None: ...

class PreventionJobTriggerInspectJobInspectConfigInfoTypeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobInspectConfigInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobInspectConfigLimitsArgsDict(TypedDict):
    max_findings_per_info_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeArgsDict
                ]
            ]
        ]
    ]
    max_findings_per_item: NotRequired[pulumi.Input[_builtins.int]]
    max_findings_per_request: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigLimitsArgs:
    def __init__(
        __self__,
        *,
        max_findings_per_info_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeArgs
                    ]
                ]
            ]
        ] = ...,
        max_findings_per_item: Optional[pulumi.Input[_builtins.int]] = ...,
        max_findings_per_request: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerInfoTypes")
    def max_findings_per_info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeArgs
                ]
            ]
        ]
    ]: ...
    @max_findings_per_info_types.setter
    def max_findings_per_info_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerItem")
    def max_findings_per_item(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_findings_per_item.setter
    def max_findings_per_item(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerRequest")
    def max_findings_per_request(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_findings_per_request.setter
    def max_findings_per_request(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeArgsDict(
    TypedDict
):
    info_type: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgsDict
        ]
    ]
    max_findings: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeArgs:
    def __init__(
        __self__,
        *,
        info_type: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgs
            ]
        ] = ...,
        max_findings: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infoType")
    def info_type(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgs
        ]
    ]: ...
    @info_type.setter
    def info_type(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxFindings")
    def max_findings(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_findings.setter
    def max_findings(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetArgsDict(TypedDict):
    rules: pulumi.Input[
        Sequence[
            pulumi.Input[PreventionJobTriggerInspectJobInspectConfigRuleSetRuleArgsDict]
        ]
    ]
    info_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[
            Sequence[
                pulumi.Input[PreventionJobTriggerInspectJobInspectConfigRuleSetRuleArgs]
            ]
        ],
        info_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[PreventionJobTriggerInspectJobInspectConfigRuleSetRuleArgs]
        ]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[PreventionJobTriggerInspectJobInspectConfigRuleSetRuleArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeArgs
                ]
            ]
        ]
    ]: ...
    @info_types.setter
    def info_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleArgsDict(TypedDict):
    exclusion_rule: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleArgsDict
        ]
    ]
    hotword_rule: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleArgs:
    def __init__(
        __self__,
        *,
        exclusion_rule: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleArgs
            ]
        ] = ...,
        hotword_rule: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exclusionRule")
    def exclusion_rule(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleArgs
        ]
    ]: ...
    @exclusion_rule.setter
    def exclusion_rule(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hotwordRule")
    def hotword_rule(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleArgs
        ]
    ]: ...
    @hotword_rule.setter
    def hotword_rule(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleArgsDict(
    TypedDict
):
    matching_type: pulumi.Input[_builtins.str]
    dictionary: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryArgsDict
        ]
    ]
    exclude_by_hotword: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgsDict
        ]
    ]
    exclude_info_types: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgsDict
        ]
    ]
    regex: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleRegexArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleArgs:
    def __init__(
        __self__,
        *,
        matching_type: pulumi.Input[_builtins.str],
        dictionary: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryArgs
            ]
        ] = ...,
        exclude_by_hotword: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgs
            ]
        ] = ...,
        exclude_info_types: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgs
            ]
        ] = ...,
        regex: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleRegexArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchingType")
    def matching_type(self) -> pulumi.Input[_builtins.str]: ...
    @matching_type.setter
    def matching_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def dictionary(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryArgs
        ]
    ]: ...
    @dictionary.setter
    def dictionary(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeByHotword")
    def exclude_by_hotword(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgs
        ]
    ]: ...
    @exclude_by_hotword.setter
    def exclude_by_hotword(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeInfoTypes")
    def exclude_info_types(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgs
        ]
    ]: ...
    @exclude_info_types.setter
    def exclude_info_types(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def regex(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleRegexArgs
        ]
    ]: ...
    @regex.setter
    def regex(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleRegexArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryArgsDict(
    TypedDict
):
    cloud_storage_path: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgsDict
        ]
    ]
    word_list: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_path: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgs
            ]
        ] = ...,
        word_list: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgs
        ]
    ]: ...
    @cloud_storage_path.setter
    def cloud_storage_path(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgs
        ]
    ]: ...
    @word_list.setter
    def word_list(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgsDict(
    TypedDict
):
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgsDict(
    TypedDict
):
    words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryWordListArgs:
    def __init__(
        __self__, *, words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def words(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @words.setter
    def words(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgsDict(
    TypedDict
):
    hotword_regex: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgsDict
        ]
    ]
    proximity: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordArgs:
    def __init__(
        __self__,
        *,
        hotword_regex: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgs
            ]
        ] = ...,
        proximity: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hotwordRegex")
    def hotword_regex(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgs
        ]
    ]: ...
    @hotword_regex.setter
    def hotword_regex(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def proximity(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgs
        ]
    ]: ...
    @proximity.setter
    def proximity(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgsDict(
    TypedDict
):
    group_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    pattern: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegexArgs:
    def __init__(
        __self__,
        *,
        group_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        pattern: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @group_indexes.setter
    def group_indexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgsDict(
    TypedDict
):
    window_after: NotRequired[pulumi.Input[_builtins.int]]
    window_before: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximityArgs:
    def __init__(
        __self__,
        *,
        window_after: Optional[pulumi.Input[_builtins.int]] = ...,
        window_before: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="windowAfter")
    def window_after(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @window_after.setter
    def window_after(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="windowBefore")
    def window_before(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @window_before.setter
    def window_before(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgsDict(
    TypedDict
):
    info_types: pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesArgs:
    def __init__(
        __self__,
        *,
        info_types: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgs
            ]
        ]
    ]: ...
    @info_types.setter
    def info_types(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgs
                ]
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    sensitivity_score: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgsDict
        ]
    ]
    version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        sensitivity_score: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgs
            ]
        ] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgs
        ]
    ]: ...
    @sensitivity_score.setter
    def sensitivity_score(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgsDict(
    TypedDict
):
    score: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScoreArgs:
    def __init__(__self__, *, score: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def score(self) -> pulumi.Input[_builtins.str]: ...
    @score.setter
    def score(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleRegexArgsDict(
    TypedDict
):
    pattern: pulumi.Input[_builtins.str]
    group_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleRegexArgs:
    def __init__(
        __self__,
        *,
        pattern: pulumi.Input[_builtins.str],
        group_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @group_indexes.setter
    def group_indexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleArgsDict(
    TypedDict
):
    hotword_regex: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgsDict
        ]
    ]
    likelihood_adjustment: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgsDict
        ]
    ]
    proximity: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleProximityArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleArgs:
    def __init__(
        __self__,
        *,
        hotword_regex: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs
            ]
        ] = ...,
        likelihood_adjustment: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs
            ]
        ] = ...,
        proximity: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleProximityArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hotwordRegex")
    def hotword_regex(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs
        ]
    ]: ...
    @hotword_regex.setter
    def hotword_regex(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="likelihoodAdjustment")
    def likelihood_adjustment(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs
        ]
    ]: ...
    @likelihood_adjustment.setter
    def likelihood_adjustment(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def proximity(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleProximityArgs
        ]
    ]: ...
    @proximity.setter
    def proximity(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleProximityArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgsDict(
    TypedDict
):
    group_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    pattern: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleHotwordRegexArgs:
    def __init__(
        __self__,
        *,
        group_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
        pattern: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @group_indexes.setter
    def group_indexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgsDict(
    TypedDict
):
    fixed_likelihood: NotRequired[pulumi.Input[_builtins.str]]
    relative_likelihood: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustmentArgs:
    def __init__(
        __self__,
        *,
        fixed_likelihood: Optional[pulumi.Input[_builtins.str]] = ...,
        relative_likelihood: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedLikelihood")
    def fixed_likelihood(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fixed_likelihood.setter
    def fixed_likelihood(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relativeLikelihood")
    def relative_likelihood(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @relative_likelihood.setter
    def relative_likelihood(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleProximityArgsDict(
    TypedDict
):
    window_after: NotRequired[pulumi.Input[_builtins.int]]
    window_before: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleProximityArgs:
    def __init__(
        __self__,
        *,
        window_after: Optional[pulumi.Input[_builtins.int]] = ...,
        window_before: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="windowAfter")
    def window_after(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @window_after.setter
    def window_after(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="windowBefore")
    def window_before(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @window_before.setter
    def window_before(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PreventionJobTriggerInspectJobStorageConfigArgsDict(TypedDict):
    big_query_options: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsArgsDict]
    ]
    cloud_storage_options: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsArgsDict
        ]
    ]
    datastore_options: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsArgsDict
        ]
    ]
    hybrid_options: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobStorageConfigHybridOptionsArgsDict]
    ]
    timespan_config: NotRequired[
        pulumi.Input[PreventionJobTriggerInspectJobStorageConfigTimespanConfigArgsDict]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigArgs:
    def __init__(
        __self__,
        *,
        big_query_options: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsArgs]
        ] = ...,
        cloud_storage_options: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsArgs
            ]
        ] = ...,
        datastore_options: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsArgs
            ]
        ] = ...,
        hybrid_options: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobStorageConfigHybridOptionsArgs]
        ] = ...,
        timespan_config: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobStorageConfigTimespanConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bigQueryOptions")
    def big_query_options(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsArgs]
    ]: ...
    @big_query_options.setter
    def big_query_options(
        self,
        value: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageOptions")
    def cloud_storage_options(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsArgs]
    ]: ...
    @cloud_storage_options.setter
    def cloud_storage_options(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="datastoreOptions")
    def datastore_options(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsArgs]
    ]: ...
    @datastore_options.setter
    def datastore_options(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hybridOptions")
    def hybrid_options(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobStorageConfigHybridOptionsArgs]
    ]: ...
    @hybrid_options.setter
    def hybrid_options(
        self,
        value: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobStorageConfigHybridOptionsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timespanConfig")
    def timespan_config(
        self,
    ) -> Optional[
        pulumi.Input[PreventionJobTriggerInspectJobStorageConfigTimespanConfigArgs]
    ]: ...
    @timespan_config.setter
    def timespan_config(
        self,
        value: Optional[
            pulumi.Input[PreventionJobTriggerInspectJobStorageConfigTimespanConfigArgs]
        ],
    ): ...

class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsArgsDict(TypedDict):
    table_reference: pulumi.Input[
        PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceArgsDict
    ]
    excluded_fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsExcludedFieldArgsDict
                ]
            ]
        ]
    ]
    identifying_fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIdentifyingFieldArgsDict
                ]
            ]
        ]
    ]
    included_fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIncludedFieldArgsDict
                ]
            ]
        ]
    ]
    rows_limit: NotRequired[pulumi.Input[_builtins.int]]
    rows_limit_percent: NotRequired[pulumi.Input[_builtins.int]]
    sample_method: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsArgs:
    def __init__(
        __self__,
        *,
        table_reference: pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceArgs
        ],
        excluded_fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsExcludedFieldArgs
                    ]
                ]
            ]
        ] = ...,
        identifying_fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIdentifyingFieldArgs
                    ]
                ]
            ]
        ] = ...,
        included_fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIncludedFieldArgs
                    ]
                ]
            ]
        ] = ...,
        rows_limit: Optional[pulumi.Input[_builtins.int]] = ...,
        rows_limit_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        sample_method: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tableReference")
    def table_reference(
        self,
    ) -> pulumi.Input[
        PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceArgs
    ]: ...
    @table_reference.setter
    def table_reference(
        self,
        value: pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludedFields")
    def excluded_fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsExcludedFieldArgs
                ]
            ]
        ]
    ]: ...
    @excluded_fields.setter
    def excluded_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsExcludedFieldArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="identifyingFields")
    def identifying_fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIdentifyingFieldArgs
                ]
            ]
        ]
    ]: ...
    @identifying_fields.setter
    def identifying_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIdentifyingFieldArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="includedFields")
    def included_fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIncludedFieldArgs
                ]
            ]
        ]
    ]: ...
    @included_fields.setter
    def included_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIncludedFieldArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rowsLimit")
    def rows_limit(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rows_limit.setter
    def rows_limit(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="rowsLimitPercent")
    def rows_limit_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @rows_limit_percent.setter
    def rows_limit_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleMethod")
    def sample_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sample_method.setter
    def sample_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsExcludedFieldArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsExcludedFieldArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIdentifyingFieldArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIdentifyingFieldArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIncludedFieldArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIncludedFieldArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceArgsDict(
    TypedDict
):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    table_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReferenceArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        table_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsArgsDict(TypedDict):
    file_set: pulumi.Input[
        PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetArgsDict
    ]
    bytes_limit_per_file: NotRequired[pulumi.Input[_builtins.int]]
    bytes_limit_per_file_percent: NotRequired[pulumi.Input[_builtins.int]]
    file_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    files_limit_percent: NotRequired[pulumi.Input[_builtins.int]]
    sample_method: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsArgs:
    def __init__(
        __self__,
        *,
        file_set: pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetArgs
        ],
        bytes_limit_per_file: Optional[pulumi.Input[_builtins.int]] = ...,
        bytes_limit_per_file_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        file_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        files_limit_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        sample_method: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSet")
    def file_set(
        self,
    ) -> pulumi.Input[
        PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetArgs
    ]: ...
    @file_set.setter
    def file_set(
        self,
        value: pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bytesLimitPerFile")
    def bytes_limit_per_file(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bytes_limit_per_file.setter
    def bytes_limit_per_file(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="bytesLimitPerFilePercent")
    def bytes_limit_per_file_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @bytes_limit_per_file_percent.setter
    def bytes_limit_per_file_percent(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fileTypes")
    def file_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @file_types.setter
    def file_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="filesLimitPercent")
    def files_limit_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @files_limit_percent.setter
    def files_limit_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="sampleMethod")
    def sample_method(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sample_method.setter
    def sample_method(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetArgsDict(
    TypedDict
):
    regex_file_set: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetArgsDict
        ]
    ]
    url: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetArgs:
    def __init__(
        __self__,
        *,
        regex_file_set: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetArgs
            ]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="regexFileSet")
    def regex_file_set(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetArgs
        ]
    ]: ...
    @regex_file_set.setter
    def regex_file_set(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetArgsDict(
    TypedDict
):
    bucket_name: pulumi.Input[_builtins.str]
    exclude_regexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_regexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSetArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        exclude_regexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_regexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="excludeRegexes")
    def exclude_regexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_regexes.setter
    def exclude_regexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_regexes.setter
    def include_regexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsArgsDict(TypedDict):
    kind: pulumi.Input[
        PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindArgsDict
    ]
    partition_id: pulumi.Input[
        PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdArgsDict
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsArgs:
    def __init__(
        __self__,
        *,
        kind: pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindArgs
        ],
        partition_id: pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kind(
        self,
    ) -> pulumi.Input[
        PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindArgs
    ]: ...
    @kind.setter
    def kind(
        self,
        value: pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="partitionId")
    def partition_id(
        self,
    ) -> pulumi.Input[
        PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdArgs
    ]: ...
    @partition_id.setter
    def partition_id(
        self,
        value: pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdArgs
        ],
    ): ...

class PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKindArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdArgsDict(
    TypedDict
):
    project_id: pulumi.Input[_builtins.str]
    namespace_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionIdArgs:
    def __init__(
        __self__,
        *,
        project_id: pulumi.Input[_builtins.str],
        namespace_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PreventionJobTriggerInspectJobStorageConfigHybridOptionsArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    required_finding_label_keys: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    table_options: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigHybridOptionsArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        required_finding_label_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        table_options: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsArgs
            ]
        ] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="requiredFindingLabelKeys")
    def required_finding_label_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @required_finding_label_keys.setter
    def required_finding_label_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tableOptions")
    def table_options(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsArgs
        ]
    ]: ...
    @table_options.setter
    def table_options(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsArgsDict(
    TypedDict
):
    identifying_fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsIdentifyingFieldArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsArgs:
    def __init__(
        __self__,
        *,
        identifying_fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsIdentifyingFieldArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identifyingFields")
    def identifying_fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsIdentifyingFieldArgs
                ]
            ]
        ]
    ]: ...
    @identifying_fields.setter
    def identifying_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsIdentifyingFieldArgs
                    ]
                ]
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsIdentifyingFieldArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsIdentifyingFieldArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerInspectJobStorageConfigTimespanConfigArgsDict(TypedDict):
    enable_auto_population_of_timespan_config: NotRequired[pulumi.Input[_builtins.bool]]
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    timestamp_field: NotRequired[
        pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigTimespanConfigArgs:
    def __init__(
        __self__,
        *,
        enable_auto_population_of_timespan_config: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        timestamp_field: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableAutoPopulationOfTimespanConfig")
    def enable_auto_population_of_timespan_config(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_auto_population_of_timespan_config.setter
    def enable_auto_population_of_timespan_config(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timestampField")
    def timestamp_field(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldArgs
        ]
    ]: ...
    @timestamp_field.setter
    def timestamp_field(
        self,
        value: Optional[
            pulumi.Input[
                PreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldArgs
            ]
        ],
    ): ...

class PreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampFieldArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionJobTriggerTriggerArgsDict(TypedDict):
    manual: NotRequired[pulumi.Input[PreventionJobTriggerTriggerManualArgsDict]]
    schedule: NotRequired[pulumi.Input[PreventionJobTriggerTriggerScheduleArgsDict]]
    ...

@pulumi.input_type
class PreventionJobTriggerTriggerArgs:
    def __init__(
        __self__,
        *,
        manual: Optional[pulumi.Input[PreventionJobTriggerTriggerManualArgs]] = ...,
        schedule: Optional[pulumi.Input[PreventionJobTriggerTriggerScheduleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def manual(
        self,
    ) -> Optional[pulumi.Input[PreventionJobTriggerTriggerManualArgs]]: ...
    @manual.setter
    def manual(
        self, value: Optional[pulumi.Input[PreventionJobTriggerTriggerManualArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def schedule(
        self,
    ) -> Optional[pulumi.Input[PreventionJobTriggerTriggerScheduleArgs]]: ...
    @schedule.setter
    def schedule(
        self, value: Optional[pulumi.Input[PreventionJobTriggerTriggerScheduleArgs]]
    ): ...

class PreventionJobTriggerTriggerManualArgsDict(TypedDict): ...

@pulumi.input_type
class PreventionJobTriggerTriggerManualArgs:
    def __init__(__self__) -> None: ...

class PreventionJobTriggerTriggerScheduleArgsDict(TypedDict):
    recurrence_period_duration: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PreventionJobTriggerTriggerScheduleArgs:
    def __init__(
        __self__,
        *,
        recurrence_period_duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recurrencePeriodDuration")
    def recurrence_period_duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recurrence_period_duration.setter
    def recurrence_period_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class PreventionStoredInfoTypeDictionaryArgsDict(TypedDict):
    cloud_storage_path: NotRequired[
        pulumi.Input[PreventionStoredInfoTypeDictionaryCloudStoragePathArgsDict]
    ]
    word_list: NotRequired[
        pulumi.Input[PreventionStoredInfoTypeDictionaryWordListArgsDict]
    ]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeDictionaryArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_path: Optional[
            pulumi.Input[PreventionStoredInfoTypeDictionaryCloudStoragePathArgs]
        ] = ...,
        word_list: Optional[
            pulumi.Input[PreventionStoredInfoTypeDictionaryWordListArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(
        self,
    ) -> Optional[
        pulumi.Input[PreventionStoredInfoTypeDictionaryCloudStoragePathArgs]
    ]: ...
    @cloud_storage_path.setter
    def cloud_storage_path(
        self,
        value: Optional[
            pulumi.Input[PreventionStoredInfoTypeDictionaryCloudStoragePathArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(
        self,
    ) -> Optional[pulumi.Input[PreventionStoredInfoTypeDictionaryWordListArgs]]: ...
    @word_list.setter
    def word_list(
        self,
        value: Optional[pulumi.Input[PreventionStoredInfoTypeDictionaryWordListArgs]],
    ): ...

class PreventionStoredInfoTypeDictionaryCloudStoragePathArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeDictionaryCloudStoragePathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class PreventionStoredInfoTypeDictionaryWordListArgsDict(TypedDict):
    words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeDictionaryWordListArgs:
    def __init__(
        __self__, *, words: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def words(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @words.setter
    def words(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class PreventionStoredInfoTypeLargeCustomDictionaryArgsDict(TypedDict):
    output_path: pulumi.Input[
        PreventionStoredInfoTypeLargeCustomDictionaryOutputPathArgsDict
    ]
    big_query_field: NotRequired[
        pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldArgsDict]
    ]
    cloud_storage_file_set: NotRequired[
        pulumi.Input[
            PreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetArgsDict
        ]
    ]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeLargeCustomDictionaryArgs:
    def __init__(
        __self__,
        *,
        output_path: pulumi.Input[
            PreventionStoredInfoTypeLargeCustomDictionaryOutputPathArgs
        ],
        big_query_field: Optional[
            pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldArgs]
        ] = ...,
        cloud_storage_file_set: Optional[
            pulumi.Input[
                PreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="outputPath")
    def output_path(
        self,
    ) -> pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryOutputPathArgs]: ...
    @output_path.setter
    def output_path(
        self,
        value: pulumi.Input[
            PreventionStoredInfoTypeLargeCustomDictionaryOutputPathArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bigQueryField")
    def big_query_field(
        self,
    ) -> Optional[
        pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldArgs]
    ]: ...
    @big_query_field.setter
    def big_query_field(
        self,
        value: Optional[
            pulumi.Input[PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageFileSet")
    def cloud_storage_file_set(
        self,
    ) -> Optional[
        pulumi.Input[
            PreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetArgs
        ]
    ]: ...
    @cloud_storage_file_set.setter
    def cloud_storage_file_set(
        self,
        value: Optional[
            pulumi.Input[
                PreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetArgs
            ]
        ],
    ): ...

class PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldArgsDict(TypedDict):
    field: pulumi.Input[
        PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldArgsDict
    ]
    table: pulumi.Input[
        PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableArgsDict
    ]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldArgs:
    def __init__(
        __self__,
        *,
        field: pulumi.Input[
            PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldArgs
        ],
        table: pulumi.Input[
            PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(
        self,
    ) -> pulumi.Input[
        PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldArgs
    ]: ...
    @field.setter
    def field(
        self,
        value: pulumi.Input[
            PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def table(
        self,
    ) -> pulumi.Input[
        PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableArgs
    ]: ...
    @table.setter
    def table(
        self,
        value: pulumi.Input[
            PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableArgs
        ],
    ): ...

class PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldFieldArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableArgsDict(
    TypedDict
):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    table_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTableArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        table_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[_builtins.str]: ...
    @table_id.setter
    def table_id(self, value: pulumi.Input[_builtins.str]): ...

class PreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetArgsDict(
    TypedDict
):
    url: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSetArgs:
    def __init__(__self__, *, url: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Input[_builtins.str]: ...
    @url.setter
    def url(self, value: pulumi.Input[_builtins.str]): ...

class PreventionStoredInfoTypeLargeCustomDictionaryOutputPathArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeLargeCustomDictionaryOutputPathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...

class PreventionStoredInfoTypeRegexArgsDict(TypedDict):
    pattern: pulumi.Input[_builtins.str]
    group_indexes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ...

@pulumi.input_type
class PreventionStoredInfoTypeRegexArgs:
    def __init__(
        __self__,
        *,
        pattern: pulumi.Input[_builtins.str],
        group_indexes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @group_indexes.setter
    def group_indexes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...
