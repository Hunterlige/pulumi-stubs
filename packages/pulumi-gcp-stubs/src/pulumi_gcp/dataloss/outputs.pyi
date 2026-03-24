

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PreventionDeidentifyTemplateDeidentifyConfig', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionDiscoveryConfigAction', 'PreventionDiscoveryConfigActionExportData', ..., ..., 'PreventionDiscoveryConfigActionPubSubNotification', ..., ..., ..., 'PreventionDiscoveryConfigActionPublishToChronicle', ..., 'PreventionDiscoveryConfigActionPublishToScc', 'PreventionDiscoveryConfigActionTagResources', ..., ..., ..., 'PreventionDiscoveryConfigError', 'PreventionDiscoveryConfigErrorDetails', 'PreventionDiscoveryConfigOrgConfig', 'PreventionDiscoveryConfigOrgConfigLocation', ..., ..., 'PreventionDiscoveryConfigTarget', 'PreventionDiscoveryConfigTargetBigQueryTarget', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionDiscoveryConfigTargetCloudSqlTarget', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionDiscoveryConfigTargetCloudStorageTarget', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionDiscoveryConfigTargetOtherCloudTarget', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionDiscoveryConfigTargetSecretsTarget', 'PreventionInspectTemplateInspectConfig', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionInspectTemplateInspectConfigInfoType', ..., 'PreventionInspectTemplateInspectConfigLimits', ..., ..., ..., 'PreventionInspectTemplateInspectConfigRuleSet', ..., ..., 'PreventionInspectTemplateInspectConfigRuleSetRule', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionJobTriggerInspectJob', 'PreventionJobTriggerInspectJobAction', 'PreventionJobTriggerInspectJobActionDeidentify', ..., ..., ..., ..., 'PreventionJobTriggerInspectJobActionPubSub', ..., ..., ..., ..., 'PreventionJobTriggerInspectJobActionSaveFindings', ..., ..., ..., 'PreventionJobTriggerInspectJobInspectConfig', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionJobTriggerInspectJobInspectConfigLimits', ..., ..., ..., 'PreventionJobTriggerInspectJobInspectConfigRuleSet', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionJobTriggerInspectJobStorageConfig', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'PreventionJobTriggerTrigger', 'PreventionJobTriggerTriggerManual', 'PreventionJobTriggerTriggerSchedule', 'PreventionStoredInfoTypeDictionary', 'PreventionStoredInfoTypeDictionaryCloudStoragePath', 'PreventionStoredInfoTypeDictionaryWordList', 'PreventionStoredInfoTypeLargeCustomDictionary', ..., ..., ..., ..., ..., 'PreventionStoredInfoTypeRegex']
@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, image_transformations: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformations] = ..., info_type_transformations: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformations] = ..., record_transformations: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformations] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageTransformations")
    def image_transformations(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformations]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypeTransformations")
    def info_type_transformations(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformations]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordTransformations")
    def record_transformations(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformations]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformations(dict):
    def __init__(__self__, *, transforms: Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransform]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transforms(self) -> Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransform]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransform(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_info_types: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllInfoTypes] = ..., all_text: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllText] = ..., redaction_color: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformRedactionColor] = ..., selected_info_types: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypes] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allInfoTypes")
    def all_info_types(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllInfoTypes]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allText")
    def all_text(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllText]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactionColor")
    def redaction_color(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformRedactionColor]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedInfoTypes")
    def selected_info_types(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypes]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllInfoTypes(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformAllText(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformRedactionColor(dict):
    def __init__(__self__, *, blue: Optional[_builtins.float] = ..., green: Optional[_builtins.float] = ..., red: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def blue(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def green(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def red(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, info_types: Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoType]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(self) -> Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoType]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigImageTransformationsTransformSelectedInfoTypesInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformations(dict):
    def __init__(__self__, *, transformations: Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transformations(self) -> Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformation]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, primitive_transformation: outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformation, info_types: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primitiveTransformation")
    def primitive_transformation(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoType]]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucketing_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfig] = ..., character_mask_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfig] = ..., crypto_deterministic_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfig] = ..., crypto_hash_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfig] = ..., crypto_replace_ffx_fpe_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfig] = ..., date_shift_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfig] = ..., fixed_size_bucketing_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfig] = ..., redact_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfig] = ..., replace_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfig] = ..., replace_dictionary_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfig] = ..., replace_with_info_type_config: Optional[_builtins.bool] = ..., time_part_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketingConfig")
    def bucketing_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="characterMaskConfig")
    def character_mask_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoDeterministicConfig")
    def crypto_deterministic_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoHashConfig")
    def crypto_hash_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoReplaceFfxFpeConfig")
    def crypto_replace_ffx_fpe_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateShiftConfig")
    def date_shift_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedSizeBucketingConfig")
    def fixed_size_bucketing_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactConfig")
    def redact_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceConfig")
    def replace_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceDictionaryConfig")
    def replace_dictionary_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceWithInfoTypeConfig")
    def replace_with_info_type_config(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePartConfig")
    def time_part_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfig]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfig(dict):
    def __init__(__self__, *, buckets: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucket]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucket]]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucket(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, replacement_value: outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValue, max: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMax] = ..., min: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMin] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementValue")
    def replacement_value(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValue:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMax]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMin]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMax(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMin(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, characters_to_ignores: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnore]] = ..., masking_character: Optional[_builtins.str] = ..., number_to_mask: Optional[_builtins.int] = ..., reverse_order: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="charactersToIgnores")
    def characters_to_ignores(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnore]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maskingCharacter")
    def masking_character(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberToMask")
    def number_to_mask(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseOrder")
    def reverse_order(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnore(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, characters_to_skip: Optional[_builtins.str] = ..., common_characters_to_ignore: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="charactersToSkip")
    def characters_to_skip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonCharactersToIgnore")
    def common_characters_to_ignore(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, context: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContext] = ..., crypto_key: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKey] = ..., surrogate_info_type: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoType] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContext]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoType]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContext(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., sensitivity_score: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKey] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKey]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, common_alphabet: Optional[_builtins.str] = ..., context: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContext] = ..., crypto_key: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKey] = ..., custom_alphabet: Optional[_builtins.str] = ..., radix: Optional[_builtins.int] = ..., surrogate_info_type: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoType] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonAlphabet")
    def common_alphabet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContext]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customAlphabet")
    def custom_alphabet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def radix(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoType]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContext(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., sensitivity_score: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lower_bound_days: _builtins.int, upper_bound_days: _builtins.int, context: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContext] = ..., crypto_key: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKey] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowerBoundDays")
    def lower_bound_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upperBoundDays")
    def upper_bound_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContext]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKey]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContext(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_size: _builtins.float, lower_bound: outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBound, upper_bound: outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBound) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketSize")
    def bucket_size(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowerBound")
    def lower_bound(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBound:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upperBound")
    def upper_bound(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBound:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBound(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBound(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, new_value: outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValue) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newValue")
    def new_value(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValue:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.int] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, word_list: outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordList) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordList:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordList(dict):
    def __init__(__self__, *, words: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def words(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, part_to_extract: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partToExtract")
    def part_to_extract(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformations(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_transformations: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformation]] = ..., record_suppressions: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppression]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldTransformations")
    def field_transformations(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordSuppressions")
    def record_suppressions(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppression]]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fields: Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationField], condition: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationCondition] = ..., info_type_transformations: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformations] = ..., primitive_transformation: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationField]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypeTransformations")
    def info_type_transformations(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformations]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primitiveTransformation")
    def primitive_transformation(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformation]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationCondition(dict):
    def __init__(__self__, *, expressions: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expressions(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressions]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditions] = ..., logical_operator: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalOperator")
    def logical_operator(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditions(dict):
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsCondition]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsCondition]]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsCondition(dict):
    def __init__(__self__, *, field: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionField, operator: _builtins.str, value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionField:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValue]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationConditionExpressionsConditionsConditionValueTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformations(dict):
    def __init__(__self__, *, transformations: Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transformations(self) -> Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformation]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, primitive_transformation: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformation, info_types: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primitiveTransformation")
    def primitive_transformation(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformation:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoType]]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucketing_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfig] = ..., character_mask_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfig] = ..., crypto_deterministic_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfig] = ..., crypto_hash_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfig] = ..., crypto_replace_ffx_fpe_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfig] = ..., date_shift_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfig] = ..., fixed_size_bucketing_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfig] = ..., redact_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfig] = ..., replace_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfig] = ..., replace_dictionary_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfig] = ..., replace_with_info_type_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceWithInfoTypeConfig] = ..., time_part_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketingConfig")
    def bucketing_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="characterMaskConfig")
    def character_mask_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoDeterministicConfig")
    def crypto_deterministic_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoHashConfig")
    def crypto_hash_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoReplaceFfxFpeConfig")
    def crypto_replace_ffx_fpe_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateShiftConfig")
    def date_shift_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedSizeBucketingConfig")
    def fixed_size_bucketing_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactConfig")
    def redact_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceConfig")
    def replace_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceDictionaryConfig")
    def replace_dictionary_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceWithInfoTypeConfig")
    def replace_with_info_type_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceWithInfoTypeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePartConfig")
    def time_part_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfig]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfig(dict):
    def __init__(__self__, *, buckets: Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucket]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucket]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucket(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, replacement_value: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValue, max: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMax] = ..., min: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMin] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementValue")
    def replacement_value(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValue:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMax]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMin]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMax(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMin(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, characters_to_ignores: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnore]] = ..., masking_character: Optional[_builtins.str] = ..., number_to_mask: Optional[_builtins.int] = ..., reverse_order: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="charactersToIgnores")
    def characters_to_ignores(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnore]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maskingCharacter")
    def masking_character(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberToMask")
    def number_to_mask(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseOrder")
    def reverse_order(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnore(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, characters_to_skip: Optional[_builtins.str] = ..., common_characters_to_ignore: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="charactersToSkip")
    def characters_to_skip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonCharactersToIgnore")
    def common_characters_to_ignore(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKey, surrogate_info_type: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoType, context: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContext] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKey:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoType:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContext]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigContext(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKey) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKey:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKey, common_alphabet: Optional[_builtins.str] = ..., context: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContext] = ..., custom_alphabet: Optional[_builtins.str] = ..., radix: Optional[_builtins.int] = ..., surrogate_info_type: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoType] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKey:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonAlphabet")
    def common_alphabet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContext]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customAlphabet")
    def custom_alphabet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def radix(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoType]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContext(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lower_bound_days: _builtins.int, upper_bound_days: _builtins.int, context: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContext] = ..., crypto_key: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKey] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowerBoundDays")
    def lower_bound_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upperBoundDays")
    def upper_bound_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContext]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKey]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigContext(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_size: _builtins.float, lower_bound: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBound, upper_bound: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBound) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketSize")
    def bucket_size(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowerBound")
    def lower_bound(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBound:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upperBound")
    def upper_bound(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBound:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBound(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBound(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationRedactConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, new_value: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValue) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newValue")
    def new_value(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValue:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceConfigNewValueTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, word_list: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordList) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordList:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceDictionaryConfigWordList(dict):
    def __init__(__self__, *, words: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def words(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationReplaceWithInfoTypeConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationInfoTypeTransformationsTransformationPrimitiveTransformationTimePartConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, part_to_extract: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partToExtract")
    def part_to_extract(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucketing_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfig] = ..., character_mask_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfig] = ..., crypto_deterministic_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfig] = ..., crypto_hash_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfig] = ..., crypto_replace_ffx_fpe_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfig] = ..., date_shift_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfig] = ..., fixed_size_bucketing_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfig] = ..., redact_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationRedactConfig] = ..., replace_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfig] = ..., replace_dictionary_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfig] = ..., time_part_config: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationTimePartConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketingConfig")
    def bucketing_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="characterMaskConfig")
    def character_mask_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoDeterministicConfig")
    def crypto_deterministic_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoHashConfig")
    def crypto_hash_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoReplaceFfxFpeConfig")
    def crypto_replace_ffx_fpe_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateShiftConfig")
    def date_shift_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedSizeBucketingConfig")
    def fixed_size_bucketing_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactConfig")
    def redact_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationRedactConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceConfig")
    def replace_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceDictionaryConfig")
    def replace_dictionary_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePartConfig")
    def time_part_config(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationTimePartConfig]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfig(dict):
    def __init__(__self__, *, buckets: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucket]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucket]]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucket(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, replacement_value: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValue, max: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMax] = ..., min: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMin] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="replacementValue")
    def replacement_value(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValue:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def max(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMax]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def min(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMin]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMax(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMaxTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMin(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketMinTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationBucketingConfigBucketReplacementValueTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, characters_to_ignores: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnore]] = ..., masking_character: Optional[_builtins.str] = ..., number_to_mask: Optional[_builtins.int] = ..., reverse_order: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="charactersToIgnores")
    def characters_to_ignores(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnore]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maskingCharacter")
    def masking_character(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberToMask")
    def number_to_mask(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reverseOrder")
    def reverse_order(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCharacterMaskConfigCharactersToIgnore(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, characters_to_skip: Optional[_builtins.str] = ..., common_characters_to_ignore: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="charactersToSkip")
    def characters_to_skip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonCharactersToIgnore")
    def common_characters_to_ignore(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, context: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigContext] = ..., crypto_key: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKey] = ..., surrogate_info_type: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoType] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigContext]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoType]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigContext(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., sensitivity_score: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoDeterministicConfigSurrogateInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKey] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKey]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoHashConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, common_alphabet: Optional[_builtins.str] = ..., context: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContext] = ..., crypto_key: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKey] = ..., custom_alphabet: Optional[_builtins.str] = ..., radix: Optional[_builtins.int] = ..., surrogate_info_type: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoType] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commonAlphabet")
    def common_alphabet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContext]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKey]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customAlphabet")
    def custom_alphabet(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def radix(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="surrogateInfoType")
    def surrogate_info_type(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoType]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigContext(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., sensitivity_score: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationCryptoReplaceFfxFpeConfigSurrogateInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lower_bound_days: _builtins.int, upper_bound_days: _builtins.int, context: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigContext] = ..., crypto_key: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKey] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowerBoundDays")
    def lower_bound_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upperBoundDays")
    def upper_bound_days(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigContext]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKey")
    def crypto_key(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKey]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigContext(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_wrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrapped] = ..., transient: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransient] = ..., unwrapped: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrapped] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsWrapped")
    def kms_wrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrapped]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def transient(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransient]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unwrapped(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrapped]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyKmsWrapped(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, crypto_key_name: _builtins.str, wrapped_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wrappedKey")
    def wrapped_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyTransient(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationDateShiftConfigCryptoKeyUnwrapped(dict):
    def __init__(__self__, *, key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_size: _builtins.float, lower_bound: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBound, upper_bound: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBound) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketSize")
    def bucket_size(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowerBound")
    def lower_bound(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBound:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="upperBound")
    def upper_bound(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBound:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBound(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigLowerBoundTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBound(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationFixedSizeBucketingConfigUpperBoundTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationRedactConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, new_value: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValue) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newValue")
    def new_value(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValue:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceConfigNewValueTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, word_list: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigWordList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigWordList]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationReplaceDictionaryConfigWordList(dict):
    def __init__(__self__, *, words: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def words(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsFieldTransformationPrimitiveTransformationTimePartConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, part_to_extract: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partToExtract")
    def part_to_extract(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppression(dict):
    def __init__(__self__, *, condition: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionCondition] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionCondition]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionCondition(dict):
    def __init__(__self__, *, expressions: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expressions(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressions]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditions] = ..., logical_operator: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalOperator")
    def logical_operator(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditions(dict):
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsCondition]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsCondition]]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsCondition(dict):
    def __init__(__self__, *, field: outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionField, operator: _builtins.str, value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionField:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValue]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionField(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boolean_value: Optional[_builtins.bool] = ..., date_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueDateValue] = ..., day_of_week_value: Optional[_builtins.str] = ..., float_value: Optional[_builtins.float] = ..., integer_value: Optional[_builtins.str] = ..., string_value: Optional[_builtins.str] = ..., time_value: Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueTimeValue] = ..., timestamp_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="booleanValue")
    def boolean_value(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateValue")
    def date_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueDateValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dayOfWeekValue")
    def day_of_week_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="floatValue")
    def float_value(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="integerValue")
    def integer_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeValue")
    def time_value(self) -> Optional[outputs.PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueTimeValue]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueDateValue(dict):
    def __init__(__self__, *, day: Optional[_builtins.int] = ..., month: Optional[_builtins.int] = ..., year: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDeidentifyTemplateDeidentifyConfigRecordTransformationsRecordSuppressionConditionExpressionsConditionsConditionValueTimeValue(dict):
    def __init__(__self__, *, hours: Optional[_builtins.int] = ..., minutes: Optional[_builtins.int] = ..., nanos: Optional[_builtins.int] = ..., seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, export_data: Optional[outputs.PreventionDiscoveryConfigActionExportData] = ..., pub_sub_notification: Optional[outputs.PreventionDiscoveryConfigActionPubSubNotification] = ..., publish_to_chronicle: Optional[outputs.PreventionDiscoveryConfigActionPublishToChronicle] = ..., publish_to_dataplex_catalog: Optional[outputs.PreventionDiscoveryConfigActionPublishToDataplexCatalog] = ..., publish_to_scc: Optional[outputs.PreventionDiscoveryConfigActionPublishToScc] = ..., tag_resources: Optional[outputs.PreventionDiscoveryConfigActionTagResources] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exportData")
    def export_data(self) -> Optional[outputs.PreventionDiscoveryConfigActionExportData]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubSubNotification")
    def pub_sub_notification(self) -> Optional[outputs.PreventionDiscoveryConfigActionPubSubNotification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishToChronicle")
    def publish_to_chronicle(self) -> Optional[outputs.PreventionDiscoveryConfigActionPublishToChronicle]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishToDataplexCatalog")
    def publish_to_dataplex_catalog(self) -> Optional[outputs.PreventionDiscoveryConfigActionPublishToDataplexCatalog]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishToScc")
    def publish_to_scc(self) -> Optional[outputs.PreventionDiscoveryConfigActionPublishToScc]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagResources")
    def tag_resources(self) -> Optional[outputs.PreventionDiscoveryConfigActionTagResources]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionExportData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, profile_table: Optional[outputs.PreventionDiscoveryConfigActionExportDataProfileTable] = ..., sample_findings_table: Optional[outputs.PreventionDiscoveryConfigActionExportDataSampleFindingsTable] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileTable")
    def profile_table(self) -> Optional[outputs.PreventionDiscoveryConfigActionExportDataProfileTable]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleFindingsTable")
    def sample_findings_table(self) -> Optional[outputs.PreventionDiscoveryConfigActionExportDataSampleFindingsTable]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionExportDataProfileTable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataset_id: Optional[_builtins.str] = ..., project_id: Optional[_builtins.str] = ..., table_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionExportDataSampleFindingsTable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataset_id: Optional[_builtins.str] = ..., project_id: Optional[_builtins.str] = ..., table_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionPubSubNotification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, detail_of_message: Optional[_builtins.str] = ..., event: Optional[_builtins.str] = ..., pubsub_condition: Optional[outputs.PreventionDiscoveryConfigActionPubSubNotificationPubsubCondition] = ..., topic: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailOfMessage")
    def detail_of_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubCondition")
    def pubsub_condition(self) -> Optional[outputs.PreventionDiscoveryConfigActionPubSubNotificationPubsubCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionPubSubNotificationPubsubCondition(dict):
    def __init__(__self__, *, expressions: Optional[outputs.PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expressions(self) -> Optional[outputs.PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressions]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conditions: Optional[Sequence[outputs.PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsCondition]] = ..., logical_operator: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsCondition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logicalOperator")
    def logical_operator(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionPubSubNotificationPubsubConditionExpressionsCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, minimum_risk_score: Optional[_builtins.str] = ..., minimum_sensitivity_score: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumRiskScore")
    def minimum_risk_score(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minimumSensitivityScore")
    def minimum_sensitivity_score(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionPublishToChronicle(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionPublishToDataplexCatalog(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionPublishToScc(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionTagResources(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lower_data_risk_to_low: Optional[_builtins.bool] = ..., profile_generations_to_tags: Optional[Sequence[_builtins.str]] = ..., tag_conditions: Optional[Sequence[outputs.PreventionDiscoveryConfigActionTagResourcesTagCondition]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowerDataRiskToLow")
    def lower_data_risk_to_low(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileGenerationsToTags")
    def profile_generations_to_tags(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagConditions")
    def tag_conditions(self) -> Optional[Sequence[outputs.PreventionDiscoveryConfigActionTagResourcesTagCondition]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionTagResourcesTagCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, sensitivity_score: Optional[outputs.PreventionDiscoveryConfigActionTagResourcesTagConditionSensitivityScore] = ..., tag: Optional[outputs.PreventionDiscoveryConfigActionTagResourcesTagConditionTag] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionDiscoveryConfigActionTagResourcesTagConditionSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[outputs.PreventionDiscoveryConfigActionTagResourcesTagConditionTag]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionTagResourcesTagConditionSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigActionTagResourcesTagConditionTag(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, namespaced_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedValue")
    def namespaced_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigError(dict):
    def __init__(__self__, *, details: Optional[outputs.PreventionDiscoveryConfigErrorDetails] = ..., timestamp: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[outputs.PreventionDiscoveryConfigErrorDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timestamp(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigErrorDetails(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[Sequence[Mapping[str, _builtins.str]]] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigOrgConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location: Optional[outputs.PreventionDiscoveryConfigOrgConfigLocation] = ..., project_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[outputs.PreventionDiscoveryConfigOrgConfigLocation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigOrgConfigLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, folder_id: Optional[_builtins.str] = ..., organization_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigOtherCloudStartingLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_location: Optional[outputs.PreventionDiscoveryConfigOtherCloudStartingLocationAwsLocation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsLocation")
    def aws_location(self) -> Optional[outputs.PreventionDiscoveryConfigOtherCloudStartingLocationAwsLocation]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigOtherCloudStartingLocationAwsLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_id: Optional[_builtins.str] = ..., all_asset_inventory_assets: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allAssetInventoryAssets")
    def all_asset_inventory_assets(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, big_query_target: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTarget] = ..., cloud_sql_target: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTarget] = ..., cloud_storage_target: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTarget] = ..., other_cloud_target: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTarget] = ..., secrets_target: Optional[outputs.PreventionDiscoveryConfigTargetSecretsTarget] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigQueryTarget")
    def big_query_target(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTarget]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSqlTarget")
    def cloud_sql_target(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTarget]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageTarget")
    def cloud_storage_target(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTarget]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="otherCloudTarget")
    def other_cloud_target(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTarget]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretsTarget")
    def secrets_target(self) -> Optional[outputs.PreventionDiscoveryConfigTargetSecretsTarget]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTarget(dict):
    def __init__(__self__, *, cadence: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetCadence] = ..., conditions: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetConditions] = ..., disabled: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetDisabled] = ..., filter: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilter] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetCadence]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetDisabled]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilter]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetCadence(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, inspect_template_modified_cadence: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetCadenceInspectTemplateModifiedCadence] = ..., schema_modified_cadence: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetCadenceSchemaModifiedCadence] = ..., table_modified_cadence: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetCadenceTableModifiedCadence] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplateModifiedCadence")
    def inspect_template_modified_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetCadenceInspectTemplateModifiedCadence]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaModifiedCadence")
    def schema_modified_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetCadenceSchemaModifiedCadence]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableModifiedCadence")
    def table_modified_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetCadenceTableModifiedCadence]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetCadenceInspectTemplateModifiedCadence(dict):
    def __init__(__self__, *, frequency: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetCadenceSchemaModifiedCadence(dict):
    def __init__(__self__, *, frequency: Optional[_builtins.str] = ..., types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetCadenceTableModifiedCadence(dict):
    def __init__(__self__, *, frequency: Optional[_builtins.str] = ..., types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetConditions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_after: Optional[_builtins.str] = ..., or_conditions: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetConditionsOrConditions] = ..., type_collection: Optional[_builtins.str] = ..., types: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetConditionsTypes] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAfter")
    def created_after(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orConditions")
    def or_conditions(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetConditionsOrConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="typeCollection")
    def type_collection(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetConditionsTypes]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetConditionsOrConditions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, min_age: Optional[_builtins.str] = ..., min_row_count: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minAge")
    def min_age(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minRowCount")
    def min_row_count(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetConditionsTypes(dict):
    def __init__(__self__, *, types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetDisabled(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, other_tables: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterOtherTables] = ..., table_reference: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterTableReference] = ..., tables: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterTables] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="otherTables")
    def other_tables(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterOtherTables]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableReference")
    def table_reference(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterTableReference]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tables(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterTables]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterOtherTables(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterTableReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataset_id: _builtins.str, table_id: _builtins.str, project_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterTables(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, include_regexes: Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexes] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(self) -> Optional[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexes]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexes(dict):
    def __init__(__self__, *, patterns: Optional[Sequence[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesPattern]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def patterns(self) -> Optional[Sequence[outputs.PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesPattern]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetBigQueryTargetFilterTablesIncludeRegexesPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataset_id_regex: Optional[_builtins.str] = ..., project_id_regex: Optional[_builtins.str] = ..., table_id_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetIdRegex")
    def dataset_id_regex(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectIdRegex")
    def project_id_regex(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableIdRegex")
    def table_id_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filter: outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilter, conditions: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetConditions] = ..., disabled: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetDisabled] = ..., generation_cadence: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadence] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilter:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetDisabled]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generationCadence")
    def generation_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadence]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetConditions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_engines: Optional[Sequence[_builtins.str]] = ..., types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseEngines")
    def database_engines(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetDisabled(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, collection: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollection] = ..., database_resource_reference: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterDatabaseResourceReference] = ..., others: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterOthers] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollection]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseResourceReference")
    def database_resource_reference(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterDatabaseResourceReference]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def others(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterOthers]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, include_regexes: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexes] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexes]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexes(dict):
    def __init__(__self__, *, patterns: Optional[Sequence[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesPattern]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def patterns(self) -> Optional[Sequence[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesPattern]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterCollectionIncludeRegexesPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database_regex: Optional[_builtins.str] = ..., database_resource_name_regex: Optional[_builtins.str] = ..., instance_regex: Optional[_builtins.str] = ..., project_id_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseRegex")
    def database_regex(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseResourceNameRegex")
    def database_resource_name_regex(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRegex")
    def instance_regex(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectIdRegex")
    def project_id_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterDatabaseResourceReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, database: _builtins.str, database_resource: _builtins.str, instance: _builtins.str, project_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseResource")
    def database_resource(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetFilterOthers(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadence(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, inspect_template_modified_cadence: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceInspectTemplateModifiedCadence] = ..., refresh_frequency: Optional[_builtins.str] = ..., schema_modified_cadence: Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceSchemaModifiedCadence] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplateModifiedCadence")
    def inspect_template_modified_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceInspectTemplateModifiedCadence]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshFrequency")
    def refresh_frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaModifiedCadence")
    def schema_modified_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceSchemaModifiedCadence]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceInspectTemplateModifiedCadence(dict):
    def __init__(__self__, *, frequency: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudSqlTargetGenerationCadenceSchemaModifiedCadence(dict):
    def __init__(__self__, *, frequency: Optional[_builtins.str] = ..., types: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filter: outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilter, conditions: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetConditions] = ..., disabled: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetDisabled] = ..., generation_cadence: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadence] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilter:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetDisabled]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generationCadence")
    def generation_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadence]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetConditions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_conditions: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetConditionsCloudStorageConditions] = ..., created_after: Optional[_builtins.str] = ..., min_age: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageConditions")
    def cloud_storage_conditions(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetConditionsCloudStorageConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAfter")
    def created_after(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minAge")
    def min_age(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetConditionsCloudStorageConditions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, included_bucket_attributes: Optional[Sequence[_builtins.str]] = ..., included_object_attributes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedBucketAttributes")
    def included_bucket_attributes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedObjectAttributes")
    def included_object_attributes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetDisabled(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_resource_reference: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCloudStorageResourceReference] = ..., collection: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollection] = ..., others: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterOthers] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageResourceReference")
    def cloud_storage_resource_reference(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCloudStorageResourceReference]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollection]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def others(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterOthers]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCloudStorageResourceReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: Optional[_builtins.str] = ..., project_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, include_regexes: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexes] = ..., include_tags: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTags] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexes]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeTags")
    def include_tags(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTags]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexes(dict):
    def __init__(__self__, *, patterns: Optional[Sequence[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPattern]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def patterns(self) -> Optional[Sequence[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPattern]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_regex: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternCloudStorageRegex] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageRegex")
    def cloud_storage_regex(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternCloudStorageRegex]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeRegexesPatternCloudStorageRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name_regex: Optional[_builtins.str] = ..., project_id_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketNameRegex")
    def bucket_name_regex(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectIdRegex")
    def project_id_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTags(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tag_filters: Optional[Sequence[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsTagFilter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagFilters")
    def tag_filters(self) -> Optional[Sequence[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsTagFilter]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterCollectionIncludeTagsTagFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, namespaced_tag_key: Optional[_builtins.str] = ..., namespaced_tag_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedTagKey")
    def namespaced_tag_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespacedTagValue")
    def namespaced_tag_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetFilterOthers(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadence(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, inspect_template_modified_cadence: Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceInspectTemplateModifiedCadence] = ..., refresh_frequency: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplateModifiedCadence")
    def inspect_template_modified_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceInspectTemplateModifiedCadence]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshFrequency")
    def refresh_frequency(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetCloudStorageTargetGenerationCadenceInspectTemplateModifiedCadence(dict):
    def __init__(__self__, *, frequency: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTarget(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, filter: outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilter, conditions: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetConditions] = ..., data_source_type: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetDataSourceType] = ..., disabled: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetDisabled] = ..., generation_cadence: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadence] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilter:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceType")
    def data_source_type(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetDataSourceType]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetDisabled]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generationCadence")
    def generation_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadence]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetConditions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, amazon_s3_bucket_conditions: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetConditionsAmazonS3BucketConditions] = ..., min_age: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonS3BucketConditions")
    def amazon_s3_bucket_conditions(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetConditionsAmazonS3BucketConditions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minAge")
    def min_age(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetConditionsAmazonS3BucketConditions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_types: Optional[Sequence[_builtins.str]] = ..., object_storage_classes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketTypes")
    def bucket_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectStorageClasses")
    def object_storage_classes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetDataSourceType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetDisabled(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, collection: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollection] = ..., others: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterOthers] = ..., single_resource: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResource] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollection]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def others(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterOthers]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleResource")
    def single_resource(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResource]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, include_regexes: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexes] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexes]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexes(dict):
    def __init__(__self__, *, patterns: Optional[Sequence[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPattern]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def patterns(self) -> Optional[Sequence[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPattern]]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, amazon_s3_bucket_regex: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegex] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonS3BucketRegex")
    def amazon_s3_bucket_regex(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegex]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_account_regex: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexAwsAccountRegex] = ..., bucket_name_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountRegex")
    def aws_account_regex(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexAwsAccountRegex]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketNameRegex")
    def bucket_name_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterCollectionIncludeRegexesPatternAmazonS3BucketRegexAwsAccountRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_id_regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountIdRegex")
    def account_id_regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterOthers(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, amazon_s3_bucket: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3Bucket] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonS3Bucket")
    def amazon_s3_bucket(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3Bucket]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3Bucket(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_account: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketAwsAccount] = ..., bucket_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccount")
    def aws_account(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketAwsAccount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetFilterSingleResourceAmazonS3BucketAwsAccount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, account_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadence(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, inspect_template_modified_cadence: Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceInspectTemplateModifiedCadence] = ..., refresh_frequency: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplateModifiedCadence")
    def inspect_template_modified_cadence(self) -> Optional[outputs.PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceInspectTemplateModifiedCadence]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshFrequency")
    def refresh_frequency(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetOtherCloudTargetGenerationCadenceInspectTemplateModifiedCadence(dict):
    def __init__(__self__, *, frequency: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionDiscoveryConfigTargetSecretsTarget(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content_options: Optional[Sequence[_builtins.str]] = ..., custom_info_types: Optional[Sequence[outputs.PreventionInspectTemplateInspectConfigCustomInfoType]] = ..., exclude_info_types: Optional[_builtins.bool] = ..., include_quote: Optional[_builtins.bool] = ..., info_types: Optional[Sequence[outputs.PreventionInspectTemplateInspectConfigInfoType]] = ..., limits: Optional[outputs.PreventionInspectTemplateInspectConfigLimits] = ..., min_likelihood: Optional[_builtins.str] = ..., rule_sets: Optional[Sequence[outputs.PreventionInspectTemplateInspectConfigRuleSet]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentOptions")
    def content_options(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customInfoTypes")
    def custom_info_types(self) -> Optional[Sequence[outputs.PreventionInspectTemplateInspectConfigCustomInfoType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeInfoTypes")
    def exclude_info_types(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeQuote")
    def include_quote(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(self) -> Optional[Sequence[outputs.PreventionInspectTemplateInspectConfigInfoType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigLimits]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minLikelihood")
    def min_likelihood(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> Optional[Sequence[outputs.PreventionInspectTemplateInspectConfigRuleSet]]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, info_type: outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeInfoType, dictionary: Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeDictionary] = ..., exclusion_type: Optional[_builtins.str] = ..., likelihood: Optional[_builtins.str] = ..., regex: Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeRegex] = ..., sensitivity_score: Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeSensitivityScore] = ..., stored_type: Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeStoredType] = ..., surrogate_type: Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeSurrogateType] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoType")
    def info_type(self) -> outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeInfoType:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dictionary(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeDictionary]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exclusionType")
    def exclusion_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def likelihood(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeRegex]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storedType")
    def stored_type(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeStoredType]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="surrogateType")
    def surrogate_type(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeSurrogateType]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeDictionary(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_path: Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryCloudStoragePath] = ..., word_list: Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryWordList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryCloudStoragePath]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryWordList]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryCloudStoragePath(dict):
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeDictionaryWordList(dict):
    def __init__(__self__, *, words: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def words(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pattern: _builtins.str, group_indexes: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeStoredType(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigCustomInfoTypeSurrogateType(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionInspectTemplateInspectConfigInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigLimits(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_findings_per_item: _builtins.int, max_findings_per_request: _builtins.int, max_findings_per_info_types: Optional[Sequence[outputs.PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerItem")
    def max_findings_per_item(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerRequest")
    def max_findings_per_request(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerInfoTypes")
    def max_findings_per_info_types(self) -> Optional[Sequence[outputs.PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoType]]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_findings: _builtins.int, info_type: Optional[outputs.PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoType] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFindings")
    def max_findings(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoType")
    def info_type(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoType]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, info_types: Sequence[outputs.PreventionInspectTemplateInspectConfigRuleSetInfoType], rules: Sequence[outputs.PreventionInspectTemplateInspectConfigRuleSetRule]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(self) -> Sequence[outputs.PreventionInspectTemplateInspectConfigRuleSetInfoType]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.PreventionInspectTemplateInspectConfigRuleSetRule]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, exclusion_rule: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRule] = ..., hotword_rule: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRule] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exclusionRule")
    def exclusion_rule(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotwordRule")
    def hotword_rule(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRule]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, matching_type: _builtins.str, dictionary: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionary] = ..., exclude_by_hotword: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotword] = ..., exclude_info_types: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypes] = ..., regex: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegex] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingType")
    def matching_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dictionary(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionary]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeByHotword")
    def exclude_by_hotword(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotword]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeInfoTypes")
    def exclude_info_types(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypes]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegex]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionary(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_path: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePath] = ..., word_list: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePath]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordList]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePath(dict):
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleDictionaryWordList(dict):
    def __init__(__self__, *, words: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def words(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotword(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hotword_regex: outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegex, proximity: outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximity) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotwordRegex")
    def hotword_regex(self) -> outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegex:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def proximity(self) -> outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximity:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pattern: _builtins.str, group_indexes: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, window_after: Optional[_builtins.int] = ..., window_before: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowAfter")
    def window_after(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowBefore")
    def window_before(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, info_types: Sequence[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoType]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(self) -> Sequence[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoType]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleExclusionRuleRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pattern: _builtins.str, group_indexes: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hotword_regex: outputs.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegex, likelihood_adjustment: outputs.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustment, proximity: outputs.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximity) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotwordRegex")
    def hotword_regex(self) -> outputs.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegex:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="likelihoodAdjustment")
    def likelihood_adjustment(self) -> outputs.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustment:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def proximity(self) -> outputs.PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximity:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleHotwordRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pattern: _builtins.str, group_indexes: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fixed_likelihood: Optional[_builtins.str] = ..., relative_likelihood: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedLikelihood")
    def fixed_likelihood(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativeLikelihood")
    def relative_likelihood(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionInspectTemplateInspectConfigRuleSetRuleHotwordRuleProximity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, window_after: Optional[_builtins.int] = ..., window_before: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowAfter")
    def window_after(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowBefore")
    def window_before(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJob(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, storage_config: outputs.PreventionJobTriggerInspectJobStorageConfig, actions: Optional[Sequence[outputs.PreventionJobTriggerInspectJobAction]] = ..., inspect_config: Optional[outputs.PreventionJobTriggerInspectJobInspectConfig] = ..., inspect_template_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageConfig")
    def storage_config(self) -> outputs.PreventionJobTriggerInspectJobStorageConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectConfig")
    def inspect_config(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplateName")
    def inspect_template_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deidentify: Optional[outputs.PreventionJobTriggerInspectJobActionDeidentify] = ..., job_notification_emails: Optional[outputs.PreventionJobTriggerInspectJobActionJobNotificationEmails] = ..., pub_sub: Optional[outputs.PreventionJobTriggerInspectJobActionPubSub] = ..., publish_findings_to_cloud_data_catalog: Optional[outputs.PreventionJobTriggerInspectJobActionPublishFindingsToCloudDataCatalog] = ..., publish_findings_to_dataplex_catalog: Optional[outputs.PreventionJobTriggerInspectJobActionPublishFindingsToDataplexCatalog] = ..., publish_summary_to_cscc: Optional[outputs.PreventionJobTriggerInspectJobActionPublishSummaryToCscc] = ..., publish_to_stackdriver: Optional[outputs.PreventionJobTriggerInspectJobActionPublishToStackdriver] = ..., save_findings: Optional[outputs.PreventionJobTriggerInspectJobActionSaveFindings] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deidentify(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionDeidentify]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobNotificationEmails")
    def job_notification_emails(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionJobNotificationEmails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubSub")
    def pub_sub(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionPubSub]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishFindingsToCloudDataCatalog")
    @_utilities.deprecated(...)
    def publish_findings_to_cloud_data_catalog(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionPublishFindingsToCloudDataCatalog]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishFindingsToDataplexCatalog")
    def publish_findings_to_dataplex_catalog(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionPublishFindingsToDataplexCatalog]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishSummaryToCscc")
    def publish_summary_to_cscc(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionPublishSummaryToCscc]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publishToStackdriver")
    def publish_to_stackdriver(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionPublishToStackdriver]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="saveFindings")
    def save_findings(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionSaveFindings]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionDeidentify(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_output: _builtins.str, file_types_to_transforms: Optional[Sequence[_builtins.str]] = ..., transformation_config: Optional[outputs.PreventionJobTriggerInspectJobActionDeidentifyTransformationConfig] = ..., transformation_details_storage_config: Optional[outputs.PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageOutput")
    def cloud_storage_output(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileTypesToTransforms")
    def file_types_to_transforms(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transformationConfig")
    def transformation_config(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionDeidentifyTransformationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transformationDetailsStorageConfig")
    def transformation_details_storage_config(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfig]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionDeidentifyTransformationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deidentify_template: Optional[_builtins.str] = ..., image_redact_template: Optional[_builtins.str] = ..., structured_deidentify_template: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageRedactTemplate")
    def image_redact_template(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="structuredDeidentifyTemplate")
    def structured_deidentify_template(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfig(dict):
    def __init__(__self__, *, table: outputs.PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigTable) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> outputs.PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigTable:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionDeidentifyTransformationDetailsStorageConfigTable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataset_id: _builtins.str, project_id: _builtins.str, table_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionJobNotificationEmails(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionPubSub(dict):
    def __init__(__self__, *, topic: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionPublishFindingsToCloudDataCatalog(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionPublishFindingsToDataplexCatalog(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionPublishSummaryToCscc(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionPublishToStackdriver(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionSaveFindings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, output_config: outputs.PreventionJobTriggerInspectJobActionSaveFindingsOutputConfig) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> outputs.PreventionJobTriggerInspectJobActionSaveFindingsOutputConfig:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionSaveFindingsOutputConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, output_schema: Optional[_builtins.str] = ..., storage_path: Optional[outputs.PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigStoragePath] = ..., table: Optional[outputs.PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigTable] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputSchema")
    def output_schema(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storagePath")
    def storage_path(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigStoragePath]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[outputs.PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigTable]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigStoragePath(dict):
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobActionSaveFindingsOutputConfigTable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataset_id: _builtins.str, project_id: _builtins.str, table_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_info_types: Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoType]] = ..., exclude_info_types: Optional[_builtins.bool] = ..., include_quote: Optional[_builtins.bool] = ..., info_types: Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigInfoType]] = ..., limits: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigLimits] = ..., min_likelihood: Optional[_builtins.str] = ..., rule_sets: Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSet]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customInfoTypes")
    def custom_info_types(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeInfoTypes")
    def exclude_info_types(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeQuote")
    def include_quote(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigInfoType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigLimits]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minLikelihood")
    def min_likelihood(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSet]]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, info_type: outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoType, dictionary: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionary] = ..., exclusion_type: Optional[_builtins.str] = ..., likelihood: Optional[_builtins.str] = ..., regex: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeRegex] = ..., sensitivity_score: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSensitivityScore] = ..., stored_type: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeStoredType] = ..., surrogate_type: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSurrogateType] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoType")
    def info_type(self) -> outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoType:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dictionary(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionary]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exclusionType")
    def exclusion_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def likelihood(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeRegex]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storedType")
    def stored_type(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeStoredType]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="surrogateType")
    def surrogate_type(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSurrogateType]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionary(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_path: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryCloudStoragePath] = ..., word_list: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryWordList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryCloudStoragePath]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryWordList]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryCloudStoragePath(dict):
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeDictionaryWordList(dict):
    def __init__(__self__, *, words: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def words(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pattern: _builtins.str, group_indexes: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeStoredType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, create_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigCustomInfoTypeSurrogateType(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigLimits(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_findings_per_info_types: Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoType]] = ..., max_findings_per_item: Optional[_builtins.int] = ..., max_findings_per_request: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerInfoTypes")
    def max_findings_per_info_types(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerItem")
    def max_findings_per_item(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFindingsPerRequest")
    def max_findings_per_request(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, info_type: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoType] = ..., max_findings: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoType")
    def info_type(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoType]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxFindings")
    def max_findings(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigLimitsMaxFindingsPerInfoTypeInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, rules: Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRule], info_types: Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetInfoType]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetInfoType]]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, exclusion_rule: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRule] = ..., hotword_rule: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRule] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exclusionRule")
    def exclusion_rule(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRule]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotwordRule")
    def hotword_rule(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRule]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, matching_type: _builtins.str, dictionary: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionary] = ..., exclude_by_hotword: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotword] = ..., exclude_info_types: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypes] = ..., regex: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleRegex] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchingType")
    def matching_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dictionary(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionary]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeByHotword")
    def exclude_by_hotword(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotword]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeInfoTypes")
    def exclude_info_types(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypes]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleRegex]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionary(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_path: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePath] = ..., word_list: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryWordList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePath]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryWordList]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryCloudStoragePath(dict):
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleDictionaryWordList(dict):
    def __init__(__self__, *, words: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def words(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotword(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hotword_regex: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegex] = ..., proximity: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximity] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotwordRegex")
    def hotword_regex(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegex]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def proximity(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximity]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordHotwordRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_indexes: Optional[Sequence[_builtins.int]] = ..., pattern: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeByHotwordProximity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, window_after: Optional[_builtins.int] = ..., window_before: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowAfter")
    def window_after(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowBefore")
    def window_before(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, info_types: Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoType]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="infoTypes")
    def info_types(self) -> Sequence[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoType]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoType(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, sensitivity_score: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScore] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityScore")
    def sensitivity_score(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleExcludeInfoTypesInfoTypeSensitivityScore(dict):
    def __init__(__self__, *, score: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def score(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleExclusionRuleRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pattern: _builtins.str, group_indexes: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, hotword_regex: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleHotwordRegex] = ..., likelihood_adjustment: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustment] = ..., proximity: Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleProximity] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hotwordRegex")
    def hotword_regex(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleHotwordRegex]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="likelihoodAdjustment")
    def likelihood_adjustment(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def proximity(self) -> Optional[outputs.PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleProximity]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleHotwordRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, group_indexes: Optional[Sequence[_builtins.int]] = ..., pattern: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleLikelihoodAdjustment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fixed_likelihood: Optional[_builtins.str] = ..., relative_likelihood: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fixedLikelihood")
    def fixed_likelihood(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relativeLikelihood")
    def relative_likelihood(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobInspectConfigRuleSetRuleHotwordRuleProximity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, window_after: Optional[_builtins.int] = ..., window_before: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowAfter")
    def window_after(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="windowBefore")
    def window_before(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, big_query_options: Optional[outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptions] = ..., cloud_storage_options: Optional[outputs.PreventionJobTriggerInspectJobStorageConfigCloudStorageOptions] = ..., datastore_options: Optional[outputs.PreventionJobTriggerInspectJobStorageConfigDatastoreOptions] = ..., hybrid_options: Optional[outputs.PreventionJobTriggerInspectJobStorageConfigHybridOptions] = ..., timespan_config: Optional[outputs.PreventionJobTriggerInspectJobStorageConfigTimespanConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigQueryOptions")
    def big_query_options(self) -> Optional[outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageOptions")
    def cloud_storage_options(self) -> Optional[outputs.PreventionJobTriggerInspectJobStorageConfigCloudStorageOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastoreOptions")
    def datastore_options(self) -> Optional[outputs.PreventionJobTriggerInspectJobStorageConfigDatastoreOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hybridOptions")
    def hybrid_options(self) -> Optional[outputs.PreventionJobTriggerInspectJobStorageConfigHybridOptions]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timespanConfig")
    def timespan_config(self) -> Optional[outputs.PreventionJobTriggerInspectJobStorageConfigTimespanConfig]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, table_reference: outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference, excluded_fields: Optional[Sequence[outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsExcludedField]] = ..., identifying_fields: Optional[Sequence[outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIdentifyingField]] = ..., included_fields: Optional[Sequence[outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIncludedField]] = ..., rows_limit: Optional[_builtins.int] = ..., rows_limit_percent: Optional[_builtins.int] = ..., sample_method: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableReference")
    def table_reference(self) -> outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedFields")
    def excluded_fields(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsExcludedField]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identifyingFields")
    def identifying_fields(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIdentifyingField]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedFields")
    def included_fields(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIncludedField]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowsLimit")
    def rows_limit(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rowsLimitPercent")
    def rows_limit_percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleMethod")
    def sample_method(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsExcludedField(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIdentifyingField(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsIncludedField(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigBigQueryOptionsTableReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataset_id: _builtins.str, project_id: _builtins.str, table_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigCloudStorageOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_set: outputs.PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet, bytes_limit_per_file: Optional[_builtins.int] = ..., bytes_limit_per_file_percent: Optional[_builtins.int] = ..., file_types: Optional[Sequence[_builtins.str]] = ..., files_limit_percent: Optional[_builtins.int] = ..., sample_method: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSet")
    def file_set(self) -> outputs.PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesLimitPerFile")
    def bytes_limit_per_file(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesLimitPerFilePercent")
    def bytes_limit_per_file_percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileTypes")
    def file_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filesLimitPercent")
    def files_limit_percent(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleMethod")
    def sample_method(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regex_file_set: Optional[outputs.PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexFileSet")
    def regex_file_set(self) -> Optional[outputs.PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigCloudStorageOptionsFileSetRegexFileSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, exclude_regexes: Optional[Sequence[_builtins.str]] = ..., include_regexes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeRegexes")
    def exclude_regexes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeRegexes")
    def include_regexes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigDatastoreOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kind: outputs.PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind, partition_id: outputs.PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> outputs.PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partitionId")
    def partition_id(self) -> outputs.PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsKind(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigDatastoreOptionsPartitionId(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, project_id: _builtins.str, namespace_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigHybridOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., labels: Optional[Mapping[str, _builtins.str]] = ..., required_finding_label_keys: Optional[Sequence[_builtins.str]] = ..., table_options: Optional[outputs.PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptions] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredFindingLabelKeys")
    def required_finding_label_keys(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableOptions")
    def table_options(self) -> Optional[outputs.PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptions]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identifying_fields: Optional[Sequence[outputs.PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsIdentifyingField]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identifyingFields")
    def identifying_fields(self) -> Optional[Sequence[outputs.PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsIdentifyingField]]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigHybridOptionsTableOptionsIdentifyingField(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigTimespanConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_auto_population_of_timespan_config: Optional[_builtins.bool] = ..., end_time: Optional[_builtins.str] = ..., start_time: Optional[_builtins.str] = ..., timestamp_field: Optional[outputs.PreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoPopulationOfTimespanConfig")
    def enable_auto_population_of_timespan_config(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timestampField")
    def timestamp_field(self) -> Optional[outputs.PreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerInspectJobStorageConfigTimespanConfigTimestampField(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerTrigger(dict):
    def __init__(__self__, *, manual: Optional[outputs.PreventionJobTriggerTriggerManual] = ..., schedule: Optional[outputs.PreventionJobTriggerTriggerSchedule] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def manual(self) -> Optional[outputs.PreventionJobTriggerTriggerManual]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[outputs.PreventionJobTriggerTriggerSchedule]:
        
        ...
    


@pulumi.output_type
class PreventionJobTriggerTriggerManual(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class PreventionJobTriggerTriggerSchedule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, recurrence_period_duration: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recurrencePeriodDuration")
    def recurrence_period_duration(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeDictionary(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_storage_path: Optional[outputs.PreventionStoredInfoTypeDictionaryCloudStoragePath] = ..., word_list: Optional[outputs.PreventionStoredInfoTypeDictionaryWordList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStoragePath")
    def cloud_storage_path(self) -> Optional[outputs.PreventionStoredInfoTypeDictionaryCloudStoragePath]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="wordList")
    def word_list(self) -> Optional[outputs.PreventionStoredInfoTypeDictionaryWordList]:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeDictionaryCloudStoragePath(dict):
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeDictionaryWordList(dict):
    def __init__(__self__, *, words: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def words(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeLargeCustomDictionary(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, output_path: outputs.PreventionStoredInfoTypeLargeCustomDictionaryOutputPath, big_query_field: Optional[outputs.PreventionStoredInfoTypeLargeCustomDictionaryBigQueryField] = ..., cloud_storage_file_set: Optional[outputs.PreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputPath")
    def output_path(self) -> outputs.PreventionStoredInfoTypeLargeCustomDictionaryOutputPath:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigQueryField")
    def big_query_field(self) -> Optional[outputs.PreventionStoredInfoTypeLargeCustomDictionaryBigQueryField]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudStorageFileSet")
    def cloud_storage_file_set(self) -> Optional[outputs.PreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet]:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeLargeCustomDictionaryBigQueryField(dict):
    def __init__(__self__, *, field: outputs.PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField, table: outputs.PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> outputs.PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def table(self) -> outputs.PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldField(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeLargeCustomDictionaryBigQueryFieldTable(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dataset_id: _builtins.str, project_id: _builtins.str, table_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tableId")
    def table_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeLargeCustomDictionaryCloudStorageFileSet(dict):
    def __init__(__self__, *, url: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeLargeCustomDictionaryOutputPath(dict):
    def __init__(__self__, *, path: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PreventionStoredInfoTypeRegex(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, pattern: _builtins.str, group_indexes: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupIndexes")
    def group_indexes(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


