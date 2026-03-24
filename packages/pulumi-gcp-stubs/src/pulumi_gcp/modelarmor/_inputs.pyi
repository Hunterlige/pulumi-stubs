

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FloorsettingAiPlatformFloorSettingArgs', 'FloorsettingAiPlatformFloorSettingArgsDict', 'FloorsettingFilterConfigArgs', 'FloorsettingFilterConfigArgsDict', ..., ..., ..., ..., 'FloorsettingFilterConfigRaiSettingsArgs', 'FloorsettingFilterConfigRaiSettingsArgsDict', 'FloorsettingFilterConfigRaiSettingsRaiFilterArgs', ..., 'FloorsettingFilterConfigSdpSettingsArgs', 'FloorsettingFilterConfigSdpSettingsArgsDict', ..., ..., 'FloorsettingFilterConfigSdpSettingsBasicConfigArgs', ..., 'FloorsettingFloorSettingMetadataArgs', 'FloorsettingFloorSettingMetadataArgsDict', ..., ..., 'FloorsettingGoogleMcpServerFloorSettingArgs', 'FloorsettingGoogleMcpServerFloorSettingArgsDict', 'TemplateFilterConfigArgs', 'TemplateFilterConfigArgsDict', 'TemplateFilterConfigMaliciousUriFilterSettingsArgs', ..., ..., ..., 'TemplateFilterConfigRaiSettingsArgs', 'TemplateFilterConfigRaiSettingsArgsDict', 'TemplateFilterConfigRaiSettingsRaiFilterArgs', 'TemplateFilterConfigRaiSettingsRaiFilterArgsDict', 'TemplateFilterConfigSdpSettingsArgs', 'TemplateFilterConfigSdpSettingsArgsDict', 'TemplateFilterConfigSdpSettingsAdvancedConfigArgs', ..., 'TemplateFilterConfigSdpSettingsBasicConfigArgs', 'TemplateFilterConfigSdpSettingsBasicConfigArgsDict', 'TemplateTemplateMetadataArgs', 'TemplateTemplateMetadataArgsDict', 'TemplateTemplateMetadataMultiLanguageDetectionArgs', ...]
class FloorsettingAiPlatformFloorSettingArgsDict(TypedDict):
    enable_cloud_logging: NotRequired[pulumi.Input[_builtins.bool]]
    inspect_and_block: NotRequired[pulumi.Input[_builtins.bool]]
    inspect_only: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FloorsettingAiPlatformFloorSettingArgs:
    def __init__(__self__, *, enable_cloud_logging: Optional[pulumi.Input[_builtins.bool]] = ..., inspect_and_block: Optional[pulumi.Input[_builtins.bool]] = ..., inspect_only: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCloudLogging")
    def enable_cloud_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_cloud_logging.setter
    def enable_cloud_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectAndBlock")
    def inspect_and_block(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @inspect_and_block.setter
    def inspect_and_block(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectOnly")
    def inspect_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @inspect_only.setter
    def inspect_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class FloorsettingFilterConfigArgsDict(TypedDict):
    malicious_uri_filter_settings: NotRequired[pulumi.Input[FloorsettingFilterConfigMaliciousUriFilterSettingsArgsDict]]
    pi_and_jailbreak_filter_settings: NotRequired[pulumi.Input[FloorsettingFilterConfigPiAndJailbreakFilterSettingsArgsDict]]
    rai_settings: NotRequired[pulumi.Input[FloorsettingFilterConfigRaiSettingsArgsDict]]
    sdp_settings: NotRequired[pulumi.Input[FloorsettingFilterConfigSdpSettingsArgsDict]]


@pulumi.input_type
class FloorsettingFilterConfigArgs:
    def __init__(__self__, *, malicious_uri_filter_settings: Optional[pulumi.Input[FloorsettingFilterConfigMaliciousUriFilterSettingsArgs]] = ..., pi_and_jailbreak_filter_settings: Optional[pulumi.Input[FloorsettingFilterConfigPiAndJailbreakFilterSettingsArgs]] = ..., rai_settings: Optional[pulumi.Input[FloorsettingFilterConfigRaiSettingsArgs]] = ..., sdp_settings: Optional[pulumi.Input[FloorsettingFilterConfigSdpSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maliciousUriFilterSettings")
    def malicious_uri_filter_settings(self) -> Optional[pulumi.Input[FloorsettingFilterConfigMaliciousUriFilterSettingsArgs]]:
        
        ...
    
    @malicious_uri_filter_settings.setter
    def malicious_uri_filter_settings(self, value: Optional[pulumi.Input[FloorsettingFilterConfigMaliciousUriFilterSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="piAndJailbreakFilterSettings")
    def pi_and_jailbreak_filter_settings(self) -> Optional[pulumi.Input[FloorsettingFilterConfigPiAndJailbreakFilterSettingsArgs]]:
        
        ...
    
    @pi_and_jailbreak_filter_settings.setter
    def pi_and_jailbreak_filter_settings(self, value: Optional[pulumi.Input[FloorsettingFilterConfigPiAndJailbreakFilterSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="raiSettings")
    def rai_settings(self) -> Optional[pulumi.Input[FloorsettingFilterConfigRaiSettingsArgs]]:
        
        ...
    
    @rai_settings.setter
    def rai_settings(self, value: Optional[pulumi.Input[FloorsettingFilterConfigRaiSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sdpSettings")
    def sdp_settings(self) -> Optional[pulumi.Input[FloorsettingFilterConfigSdpSettingsArgs]]:
        
        ...
    
    @sdp_settings.setter
    def sdp_settings(self, value: Optional[pulumi.Input[FloorsettingFilterConfigSdpSettingsArgs]]): # -> None:
        ...
    


class FloorsettingFilterConfigMaliciousUriFilterSettingsArgsDict(TypedDict):
    filter_enforcement: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FloorsettingFilterConfigMaliciousUriFilterSettingsArgs:
    def __init__(__self__, *, filter_enforcement: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_enforcement.setter
    def filter_enforcement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FloorsettingFilterConfigPiAndJailbreakFilterSettingsArgsDict(TypedDict):
    confidence_level: NotRequired[pulumi.Input[_builtins.str]]
    filter_enforcement: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FloorsettingFilterConfigPiAndJailbreakFilterSettingsArgs:
    def __init__(__self__, *, confidence_level: Optional[pulumi.Input[_builtins.str]] = ..., filter_enforcement: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @confidence_level.setter
    def confidence_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_enforcement.setter
    def filter_enforcement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FloorsettingFilterConfigRaiSettingsArgsDict(TypedDict):
    rai_filters: pulumi.Input[Sequence[pulumi.Input[FloorsettingFilterConfigRaiSettingsRaiFilterArgsDict]]]


@pulumi.input_type
class FloorsettingFilterConfigRaiSettingsArgs:
    def __init__(__self__, *, rai_filters: pulumi.Input[Sequence[pulumi.Input[FloorsettingFilterConfigRaiSettingsRaiFilterArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="raiFilters")
    def rai_filters(self) -> pulumi.Input[Sequence[pulumi.Input[FloorsettingFilterConfigRaiSettingsRaiFilterArgs]]]:
        
        ...
    
    @rai_filters.setter
    def rai_filters(self, value: pulumi.Input[Sequence[pulumi.Input[FloorsettingFilterConfigRaiSettingsRaiFilterArgs]]]): # -> None:
        ...
    


class FloorsettingFilterConfigRaiSettingsRaiFilterArgsDict(TypedDict):
    filter_type: pulumi.Input[_builtins.str]
    confidence_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FloorsettingFilterConfigRaiSettingsRaiFilterArgs:
    def __init__(__self__, *, filter_type: pulumi.Input[_builtins.str], confidence_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter_type.setter
    def filter_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @confidence_level.setter
    def confidence_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FloorsettingFilterConfigSdpSettingsArgsDict(TypedDict):
    advanced_config: NotRequired[pulumi.Input[FloorsettingFilterConfigSdpSettingsAdvancedConfigArgsDict]]
    basic_config: NotRequired[pulumi.Input[FloorsettingFilterConfigSdpSettingsBasicConfigArgsDict]]


@pulumi.input_type
class FloorsettingFilterConfigSdpSettingsArgs:
    def __init__(__self__, *, advanced_config: Optional[pulumi.Input[FloorsettingFilterConfigSdpSettingsAdvancedConfigArgs]] = ..., basic_config: Optional[pulumi.Input[FloorsettingFilterConfigSdpSettingsBasicConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedConfig")
    def advanced_config(self) -> Optional[pulumi.Input[FloorsettingFilterConfigSdpSettingsAdvancedConfigArgs]]:
        
        ...
    
    @advanced_config.setter
    def advanced_config(self, value: Optional[pulumi.Input[FloorsettingFilterConfigSdpSettingsAdvancedConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicConfig")
    def basic_config(self) -> Optional[pulumi.Input[FloorsettingFilterConfigSdpSettingsBasicConfigArgs]]:
        
        ...
    
    @basic_config.setter
    def basic_config(self, value: Optional[pulumi.Input[FloorsettingFilterConfigSdpSettingsBasicConfigArgs]]): # -> None:
        ...
    


class FloorsettingFilterConfigSdpSettingsAdvancedConfigArgsDict(TypedDict):
    deidentify_template: NotRequired[pulumi.Input[_builtins.str]]
    inspect_template: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FloorsettingFilterConfigSdpSettingsAdvancedConfigArgs:
    def __init__(__self__, *, deidentify_template: Optional[pulumi.Input[_builtins.str]] = ..., inspect_template: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deidentify_template.setter
    def deidentify_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inspect_template.setter
    def inspect_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FloorsettingFilterConfigSdpSettingsBasicConfigArgsDict(TypedDict):
    filter_enforcement: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FloorsettingFilterConfigSdpSettingsBasicConfigArgs:
    def __init__(__self__, *, filter_enforcement: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_enforcement.setter
    def filter_enforcement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class FloorsettingFloorSettingMetadataArgsDict(TypedDict):
    multi_language_detection: NotRequired[pulumi.Input[FloorsettingFloorSettingMetadataMultiLanguageDetectionArgsDict]]


@pulumi.input_type
class FloorsettingFloorSettingMetadataArgs:
    def __init__(__self__, *, multi_language_detection: Optional[pulumi.Input[FloorsettingFloorSettingMetadataMultiLanguageDetectionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiLanguageDetection")
    def multi_language_detection(self) -> Optional[pulumi.Input[FloorsettingFloorSettingMetadataMultiLanguageDetectionArgs]]:
        
        ...
    
    @multi_language_detection.setter
    def multi_language_detection(self, value: Optional[pulumi.Input[FloorsettingFloorSettingMetadataMultiLanguageDetectionArgs]]): # -> None:
        ...
    


class FloorsettingFloorSettingMetadataMultiLanguageDetectionArgsDict(TypedDict):
    enable_multi_language_detection: pulumi.Input[_builtins.bool]


@pulumi.input_type
class FloorsettingFloorSettingMetadataMultiLanguageDetectionArgs:
    def __init__(__self__, *, enable_multi_language_detection: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiLanguageDetection")
    def enable_multi_language_detection(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_multi_language_detection.setter
    def enable_multi_language_detection(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class FloorsettingGoogleMcpServerFloorSettingArgsDict(TypedDict):
    enable_cloud_logging: NotRequired[pulumi.Input[_builtins.bool]]
    inspect_and_block: NotRequired[pulumi.Input[_builtins.bool]]
    inspect_only: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class FloorsettingGoogleMcpServerFloorSettingArgs:
    def __init__(__self__, *, enable_cloud_logging: Optional[pulumi.Input[_builtins.bool]] = ..., inspect_and_block: Optional[pulumi.Input[_builtins.bool]] = ..., inspect_only: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCloudLogging")
    def enable_cloud_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_cloud_logging.setter
    def enable_cloud_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectAndBlock")
    def inspect_and_block(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @inspect_and_block.setter
    def inspect_and_block(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectOnly")
    def inspect_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @inspect_only.setter
    def inspect_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class TemplateFilterConfigArgsDict(TypedDict):
    malicious_uri_filter_settings: NotRequired[pulumi.Input[TemplateFilterConfigMaliciousUriFilterSettingsArgsDict]]
    pi_and_jailbreak_filter_settings: NotRequired[pulumi.Input[TemplateFilterConfigPiAndJailbreakFilterSettingsArgsDict]]
    rai_settings: NotRequired[pulumi.Input[TemplateFilterConfigRaiSettingsArgsDict]]
    sdp_settings: NotRequired[pulumi.Input[TemplateFilterConfigSdpSettingsArgsDict]]


@pulumi.input_type
class TemplateFilterConfigArgs:
    def __init__(__self__, *, malicious_uri_filter_settings: Optional[pulumi.Input[TemplateFilterConfigMaliciousUriFilterSettingsArgs]] = ..., pi_and_jailbreak_filter_settings: Optional[pulumi.Input[TemplateFilterConfigPiAndJailbreakFilterSettingsArgs]] = ..., rai_settings: Optional[pulumi.Input[TemplateFilterConfigRaiSettingsArgs]] = ..., sdp_settings: Optional[pulumi.Input[TemplateFilterConfigSdpSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maliciousUriFilterSettings")
    def malicious_uri_filter_settings(self) -> Optional[pulumi.Input[TemplateFilterConfigMaliciousUriFilterSettingsArgs]]:
        
        ...
    
    @malicious_uri_filter_settings.setter
    def malicious_uri_filter_settings(self, value: Optional[pulumi.Input[TemplateFilterConfigMaliciousUriFilterSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="piAndJailbreakFilterSettings")
    def pi_and_jailbreak_filter_settings(self) -> Optional[pulumi.Input[TemplateFilterConfigPiAndJailbreakFilterSettingsArgs]]:
        
        ...
    
    @pi_and_jailbreak_filter_settings.setter
    def pi_and_jailbreak_filter_settings(self, value: Optional[pulumi.Input[TemplateFilterConfigPiAndJailbreakFilterSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="raiSettings")
    def rai_settings(self) -> Optional[pulumi.Input[TemplateFilterConfigRaiSettingsArgs]]:
        
        ...
    
    @rai_settings.setter
    def rai_settings(self, value: Optional[pulumi.Input[TemplateFilterConfigRaiSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sdpSettings")
    def sdp_settings(self) -> Optional[pulumi.Input[TemplateFilterConfigSdpSettingsArgs]]:
        
        ...
    
    @sdp_settings.setter
    def sdp_settings(self, value: Optional[pulumi.Input[TemplateFilterConfigSdpSettingsArgs]]): # -> None:
        ...
    


class TemplateFilterConfigMaliciousUriFilterSettingsArgsDict(TypedDict):
    filter_enforcement: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TemplateFilterConfigMaliciousUriFilterSettingsArgs:
    def __init__(__self__, *, filter_enforcement: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_enforcement.setter
    def filter_enforcement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TemplateFilterConfigPiAndJailbreakFilterSettingsArgsDict(TypedDict):
    confidence_level: NotRequired[pulumi.Input[_builtins.str]]
    filter_enforcement: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TemplateFilterConfigPiAndJailbreakFilterSettingsArgs:
    def __init__(__self__, *, confidence_level: Optional[pulumi.Input[_builtins.str]] = ..., filter_enforcement: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @confidence_level.setter
    def confidence_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_enforcement.setter
    def filter_enforcement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TemplateFilterConfigRaiSettingsArgsDict(TypedDict):
    rai_filters: pulumi.Input[Sequence[pulumi.Input[TemplateFilterConfigRaiSettingsRaiFilterArgsDict]]]


@pulumi.input_type
class TemplateFilterConfigRaiSettingsArgs:
    def __init__(__self__, *, rai_filters: pulumi.Input[Sequence[pulumi.Input[TemplateFilterConfigRaiSettingsRaiFilterArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="raiFilters")
    def rai_filters(self) -> pulumi.Input[Sequence[pulumi.Input[TemplateFilterConfigRaiSettingsRaiFilterArgs]]]:
        
        ...
    
    @rai_filters.setter
    def rai_filters(self, value: pulumi.Input[Sequence[pulumi.Input[TemplateFilterConfigRaiSettingsRaiFilterArgs]]]): # -> None:
        ...
    


class TemplateFilterConfigRaiSettingsRaiFilterArgsDict(TypedDict):
    filter_type: pulumi.Input[_builtins.str]
    confidence_level: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TemplateFilterConfigRaiSettingsRaiFilterArgs:
    def __init__(__self__, *, filter_type: pulumi.Input[_builtins.str], confidence_level: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @filter_type.setter
    def filter_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @confidence_level.setter
    def confidence_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TemplateFilterConfigSdpSettingsArgsDict(TypedDict):
    advanced_config: NotRequired[pulumi.Input[TemplateFilterConfigSdpSettingsAdvancedConfigArgsDict]]
    basic_config: NotRequired[pulumi.Input[TemplateFilterConfigSdpSettingsBasicConfigArgsDict]]


@pulumi.input_type
class TemplateFilterConfigSdpSettingsArgs:
    def __init__(__self__, *, advanced_config: Optional[pulumi.Input[TemplateFilterConfigSdpSettingsAdvancedConfigArgs]] = ..., basic_config: Optional[pulumi.Input[TemplateFilterConfigSdpSettingsBasicConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedConfig")
    def advanced_config(self) -> Optional[pulumi.Input[TemplateFilterConfigSdpSettingsAdvancedConfigArgs]]:
        
        ...
    
    @advanced_config.setter
    def advanced_config(self, value: Optional[pulumi.Input[TemplateFilterConfigSdpSettingsAdvancedConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicConfig")
    def basic_config(self) -> Optional[pulumi.Input[TemplateFilterConfigSdpSettingsBasicConfigArgs]]:
        
        ...
    
    @basic_config.setter
    def basic_config(self, value: Optional[pulumi.Input[TemplateFilterConfigSdpSettingsBasicConfigArgs]]): # -> None:
        ...
    


class TemplateFilterConfigSdpSettingsAdvancedConfigArgsDict(TypedDict):
    deidentify_template: NotRequired[pulumi.Input[_builtins.str]]
    inspect_template: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TemplateFilterConfigSdpSettingsAdvancedConfigArgs:
    def __init__(__self__, *, deidentify_template: Optional[pulumi.Input[_builtins.str]] = ..., inspect_template: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @deidentify_template.setter
    def deidentify_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @inspect_template.setter
    def inspect_template(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TemplateFilterConfigSdpSettingsBasicConfigArgsDict(TypedDict):
    filter_enforcement: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class TemplateFilterConfigSdpSettingsBasicConfigArgs:
    def __init__(__self__, *, filter_enforcement: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_enforcement.setter
    def filter_enforcement(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TemplateTemplateMetadataArgsDict(TypedDict):
    custom_llm_response_safety_error_code: NotRequired[pulumi.Input[_builtins.int]]
    custom_llm_response_safety_error_message: NotRequired[pulumi.Input[_builtins.str]]
    custom_prompt_safety_error_code: NotRequired[pulumi.Input[_builtins.int]]
    custom_prompt_safety_error_message: NotRequired[pulumi.Input[_builtins.str]]
    enforcement_type: NotRequired[pulumi.Input[_builtins.str]]
    ignore_partial_invocation_failures: NotRequired[pulumi.Input[_builtins.bool]]
    log_sanitize_operations: NotRequired[pulumi.Input[_builtins.bool]]
    log_template_operations: NotRequired[pulumi.Input[_builtins.bool]]
    multi_language_detection: NotRequired[pulumi.Input[TemplateTemplateMetadataMultiLanguageDetectionArgsDict]]


@pulumi.input_type
class TemplateTemplateMetadataArgs:
    def __init__(__self__, *, custom_llm_response_safety_error_code: Optional[pulumi.Input[_builtins.int]] = ..., custom_llm_response_safety_error_message: Optional[pulumi.Input[_builtins.str]] = ..., custom_prompt_safety_error_code: Optional[pulumi.Input[_builtins.int]] = ..., custom_prompt_safety_error_message: Optional[pulumi.Input[_builtins.str]] = ..., enforcement_type: Optional[pulumi.Input[_builtins.str]] = ..., ignore_partial_invocation_failures: Optional[pulumi.Input[_builtins.bool]] = ..., log_sanitize_operations: Optional[pulumi.Input[_builtins.bool]] = ..., log_template_operations: Optional[pulumi.Input[_builtins.bool]] = ..., multi_language_detection: Optional[pulumi.Input[TemplateTemplateMetadataMultiLanguageDetectionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLlmResponseSafetyErrorCode")
    def custom_llm_response_safety_error_code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @custom_llm_response_safety_error_code.setter
    def custom_llm_response_safety_error_code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customLlmResponseSafetyErrorMessage")
    def custom_llm_response_safety_error_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_llm_response_safety_error_message.setter
    def custom_llm_response_safety_error_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPromptSafetyErrorCode")
    def custom_prompt_safety_error_code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @custom_prompt_safety_error_code.setter
    def custom_prompt_safety_error_code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPromptSafetyErrorMessage")
    def custom_prompt_safety_error_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_prompt_safety_error_message.setter
    def custom_prompt_safety_error_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforcementType")
    def enforcement_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @enforcement_type.setter
    def enforcement_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignorePartialInvocationFailures")
    def ignore_partial_invocation_failures(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_partial_invocation_failures.setter
    def ignore_partial_invocation_failures(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logSanitizeOperations")
    def log_sanitize_operations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_sanitize_operations.setter
    def log_sanitize_operations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logTemplateOperations")
    def log_template_operations(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_template_operations.setter
    def log_template_operations(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiLanguageDetection")
    def multi_language_detection(self) -> Optional[pulumi.Input[TemplateTemplateMetadataMultiLanguageDetectionArgs]]:
        
        ...
    
    @multi_language_detection.setter
    def multi_language_detection(self, value: Optional[pulumi.Input[TemplateTemplateMetadataMultiLanguageDetectionArgs]]): # -> None:
        ...
    


class TemplateTemplateMetadataMultiLanguageDetectionArgsDict(TypedDict):
    enable_multi_language_detection: pulumi.Input[_builtins.bool]


@pulumi.input_type
class TemplateTemplateMetadataMultiLanguageDetectionArgs:
    def __init__(__self__, *, enable_multi_language_detection: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiLanguageDetection")
    def enable_multi_language_detection(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_multi_language_detection.setter
    def enable_multi_language_detection(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


