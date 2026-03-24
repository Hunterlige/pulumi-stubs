import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FloorsettingAiPlatformFloorSetting",
    "FloorsettingFilterConfig",
    "FloorsettingFilterConfigMaliciousUriFilterSettings",
    ...,
    "FloorsettingFilterConfigRaiSettings",
    "FloorsettingFilterConfigRaiSettingsRaiFilter",
    "FloorsettingFilterConfigSdpSettings",
    "FloorsettingFilterConfigSdpSettingsAdvancedConfig",
    "FloorsettingFilterConfigSdpSettingsBasicConfig",
    "FloorsettingFloorSettingMetadata",
    ...,
    "FloorsettingGoogleMcpServerFloorSetting",
    "TemplateFilterConfig",
    "TemplateFilterConfigMaliciousUriFilterSettings",
    "TemplateFilterConfigPiAndJailbreakFilterSettings",
    "TemplateFilterConfigRaiSettings",
    "TemplateFilterConfigRaiSettingsRaiFilter",
    "TemplateFilterConfigSdpSettings",
    "TemplateFilterConfigSdpSettingsAdvancedConfig",
    "TemplateFilterConfigSdpSettingsBasicConfig",
    "TemplateTemplateMetadata",
    "TemplateTemplateMetadataMultiLanguageDetection",
]

@pulumi.output_type
class FloorsettingAiPlatformFloorSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_cloud_logging: Optional[_builtins.bool] = ...,
        inspect_and_block: Optional[_builtins.bool] = ...,
        inspect_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableCloudLogging")
    def enable_cloud_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inspectAndBlock")
    def inspect_and_block(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inspectOnly")
    def inspect_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class FloorsettingFilterConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        malicious_uri_filter_settings: Optional[
            outputs.FloorsettingFilterConfigMaliciousUriFilterSettings
        ] = ...,
        pi_and_jailbreak_filter_settings: Optional[
            outputs.FloorsettingFilterConfigPiAndJailbreakFilterSettings
        ] = ...,
        rai_settings: Optional[outputs.FloorsettingFilterConfigRaiSettings] = ...,
        sdp_settings: Optional[outputs.FloorsettingFilterConfigSdpSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maliciousUriFilterSettings")
    def malicious_uri_filter_settings(
        self,
    ) -> Optional[outputs.FloorsettingFilterConfigMaliciousUriFilterSettings]: ...
    @_builtins.property
    @pulumi.getter(name="piAndJailbreakFilterSettings")
    def pi_and_jailbreak_filter_settings(
        self,
    ) -> Optional[outputs.FloorsettingFilterConfigPiAndJailbreakFilterSettings]: ...
    @_builtins.property
    @pulumi.getter(name="raiSettings")
    def rai_settings(self) -> Optional[outputs.FloorsettingFilterConfigRaiSettings]: ...
    @_builtins.property
    @pulumi.getter(name="sdpSettings")
    def sdp_settings(self) -> Optional[outputs.FloorsettingFilterConfigSdpSettings]: ...

@pulumi.output_type
class FloorsettingFilterConfigMaliciousUriFilterSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter_enforcement: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FloorsettingFilterConfigPiAndJailbreakFilterSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        confidence_level: Optional[_builtins.str] = ...,
        filter_enforcement: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FloorsettingFilterConfigRaiSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rai_filters: Sequence[outputs.FloorsettingFilterConfigRaiSettingsRaiFilter],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="raiFilters")
    def rai_filters(
        self,
    ) -> Sequence[outputs.FloorsettingFilterConfigRaiSettingsRaiFilter]: ...

@pulumi.output_type
class FloorsettingFilterConfigRaiSettingsRaiFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filter_type: _builtins.str,
        confidence_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FloorsettingFilterConfigSdpSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advanced_config: Optional[
            outputs.FloorsettingFilterConfigSdpSettingsAdvancedConfig
        ] = ...,
        basic_config: Optional[
            outputs.FloorsettingFilterConfigSdpSettingsBasicConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedConfig")
    def advanced_config(
        self,
    ) -> Optional[outputs.FloorsettingFilterConfigSdpSettingsAdvancedConfig]: ...
    @_builtins.property
    @pulumi.getter(name="basicConfig")
    def basic_config(
        self,
    ) -> Optional[outputs.FloorsettingFilterConfigSdpSettingsBasicConfig]: ...

@pulumi.output_type
class FloorsettingFilterConfigSdpSettingsAdvancedConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deidentify_template: Optional[_builtins.str] = ...,
        inspect_template: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FloorsettingFilterConfigSdpSettingsBasicConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter_enforcement: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FloorsettingFloorSettingMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        multi_language_detection: Optional[
            outputs.FloorsettingFloorSettingMetadataMultiLanguageDetection
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="multiLanguageDetection")
    def multi_language_detection(
        self,
    ) -> Optional[outputs.FloorsettingFloorSettingMetadataMultiLanguageDetection]: ...

@pulumi.output_type
class FloorsettingFloorSettingMetadataMultiLanguageDetection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enable_multi_language_detection: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMultiLanguageDetection")
    def enable_multi_language_detection(self) -> _builtins.bool: ...

@pulumi.output_type
class FloorsettingGoogleMcpServerFloorSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_cloud_logging: Optional[_builtins.bool] = ...,
        inspect_and_block: Optional[_builtins.bool] = ...,
        inspect_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableCloudLogging")
    def enable_cloud_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inspectAndBlock")
    def inspect_and_block(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="inspectOnly")
    def inspect_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class TemplateFilterConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        malicious_uri_filter_settings: Optional[
            outputs.TemplateFilterConfigMaliciousUriFilterSettings
        ] = ...,
        pi_and_jailbreak_filter_settings: Optional[
            outputs.TemplateFilterConfigPiAndJailbreakFilterSettings
        ] = ...,
        rai_settings: Optional[outputs.TemplateFilterConfigRaiSettings] = ...,
        sdp_settings: Optional[outputs.TemplateFilterConfigSdpSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maliciousUriFilterSettings")
    def malicious_uri_filter_settings(
        self,
    ) -> Optional[outputs.TemplateFilterConfigMaliciousUriFilterSettings]: ...
    @_builtins.property
    @pulumi.getter(name="piAndJailbreakFilterSettings")
    def pi_and_jailbreak_filter_settings(
        self,
    ) -> Optional[outputs.TemplateFilterConfigPiAndJailbreakFilterSettings]: ...
    @_builtins.property
    @pulumi.getter(name="raiSettings")
    def rai_settings(self) -> Optional[outputs.TemplateFilterConfigRaiSettings]: ...
    @_builtins.property
    @pulumi.getter(name="sdpSettings")
    def sdp_settings(self) -> Optional[outputs.TemplateFilterConfigSdpSettings]: ...

@pulumi.output_type
class TemplateFilterConfigMaliciousUriFilterSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter_enforcement: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TemplateFilterConfigPiAndJailbreakFilterSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        confidence_level: Optional[_builtins.str] = ...,
        filter_enforcement: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TemplateFilterConfigRaiSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rai_filters: Sequence[outputs.TemplateFilterConfigRaiSettingsRaiFilter],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="raiFilters")
    def rai_filters(
        self,
    ) -> Sequence[outputs.TemplateFilterConfigRaiSettingsRaiFilter]: ...

@pulumi.output_type
class TemplateFilterConfigRaiSettingsRaiFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        filter_type: _builtins.str,
        confidence_level: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TemplateFilterConfigSdpSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advanced_config: Optional[
            outputs.TemplateFilterConfigSdpSettingsAdvancedConfig
        ] = ...,
        basic_config: Optional[
            outputs.TemplateFilterConfigSdpSettingsBasicConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedConfig")
    def advanced_config(
        self,
    ) -> Optional[outputs.TemplateFilterConfigSdpSettingsAdvancedConfig]: ...
    @_builtins.property
    @pulumi.getter(name="basicConfig")
    def basic_config(
        self,
    ) -> Optional[outputs.TemplateFilterConfigSdpSettingsBasicConfig]: ...

@pulumi.output_type
class TemplateFilterConfigSdpSettingsAdvancedConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        deidentify_template: Optional[_builtins.str] = ...,
        inspect_template: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TemplateFilterConfigSdpSettingsBasicConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter_enforcement: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="filterEnforcement")
    def filter_enforcement(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TemplateTemplateMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        custom_llm_response_safety_error_code: Optional[_builtins.int] = ...,
        custom_llm_response_safety_error_message: Optional[_builtins.str] = ...,
        custom_prompt_safety_error_code: Optional[_builtins.int] = ...,
        custom_prompt_safety_error_message: Optional[_builtins.str] = ...,
        enforcement_type: Optional[_builtins.str] = ...,
        ignore_partial_invocation_failures: Optional[_builtins.bool] = ...,
        log_sanitize_operations: Optional[_builtins.bool] = ...,
        log_template_operations: Optional[_builtins.bool] = ...,
        multi_language_detection: Optional[
            outputs.TemplateTemplateMetadataMultiLanguageDetection
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customLlmResponseSafetyErrorCode")
    def custom_llm_response_safety_error_code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="customLlmResponseSafetyErrorMessage")
    def custom_llm_response_safety_error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customPromptSafetyErrorCode")
    def custom_prompt_safety_error_code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="customPromptSafetyErrorMessage")
    def custom_prompt_safety_error_message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enforcementType")
    def enforcement_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ignorePartialInvocationFailures")
    def ignore_partial_invocation_failures(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logSanitizeOperations")
    def log_sanitize_operations(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="logTemplateOperations")
    def log_template_operations(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="multiLanguageDetection")
    def multi_language_detection(
        self,
    ) -> Optional[outputs.TemplateTemplateMetadataMultiLanguageDetection]: ...

@pulumi.output_type
class TemplateTemplateMetadataMultiLanguageDetection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enable_multi_language_detection: _builtins.bool
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableMultiLanguageDetection")
    def enable_multi_language_detection(self) -> _builtins.bool: ...
