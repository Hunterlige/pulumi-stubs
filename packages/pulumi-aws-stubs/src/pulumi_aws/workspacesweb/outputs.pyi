import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataProtectionSettingsInlineRedactionConfiguration",
    ...,
    ...,
    ...,
    "IpAccessSettingsIpRule",
    "PortalTimeouts",
    "SessionLoggerEventFilter",
    "SessionLoggerEventFilterAll",
    "SessionLoggerLogConfiguration",
    "SessionLoggerLogConfigurationS3",
    "TrustStoreCertificate",
    "UserSettingsCookieSynchronizationConfiguration",
    ...,
    ...,
    "UserSettingsToolbarConfiguration",
]

@pulumi.output_type
class DataProtectionSettingsInlineRedactionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        inline_redaction_patterns: Sequence[
            outputs.DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPattern
        ],
        global_confidence_level: Optional[_builtins.int] = ...,
        global_enforced_urls: Optional[Sequence[_builtins.str]] = ...,
        global_exempt_urls: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlineRedactionPatterns")
    def inline_redaction_patterns(
        self,
    ) -> Sequence[
        outputs.DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPattern
    ]: ...
    @_builtins.property
    @pulumi.getter(name="globalConfidenceLevel")
    def global_confidence_level(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="globalEnforcedUrls")
    def global_enforced_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="globalExemptUrls")
    def global_exempt_urls(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPattern(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        built_in_pattern_id: Optional[_builtins.str] = ...,
        confidence_level: Optional[_builtins.int] = ...,
        custom_pattern: Optional[
            outputs.DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternCustomPattern
        ] = ...,
        enforced_urls: Optional[Sequence[_builtins.str]] = ...,
        exempt_urls: Optional[Sequence[_builtins.str]] = ...,
        redaction_place_holders: Optional[
            Sequence[
                outputs.DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternRedactionPlaceHolder
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="builtInPatternId")
    def built_in_pattern_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="customPattern")
    def custom_pattern(
        self,
    ) -> Optional[
        outputs.DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternCustomPattern
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enforcedUrls")
    def enforced_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="exemptUrls")
    def exempt_urls(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="redactionPlaceHolders")
    def redaction_place_holders(
        self,
    ) -> Optional[
        Sequence[
            outputs.DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternRedactionPlaceHolder
        ]
    ]: ...

@pulumi.output_type
class DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternCustomPattern(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pattern_name: _builtins.str,
        pattern_regex: _builtins.str,
        keyword_regex: Optional[_builtins.str] = ...,
        pattern_description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="patternName")
    def pattern_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="patternRegex")
    def pattern_regex(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keywordRegex")
    def keyword_regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="patternDescription")
    def pattern_description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternRedactionPlaceHolder(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        redaction_place_holder_type: _builtins.str,
        redaction_place_holder_text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="redactionPlaceHolderType")
    def redaction_place_holder_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="redactionPlaceHolderText")
    def redaction_place_holder_text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IpAccessSettingsIpRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, ip_range: _builtins.str, description: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class PortalTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SessionLoggerEventFilter(dict):
    def __init__(
        __self__,
        *,
        all: Optional[outputs.SessionLoggerEventFilterAll] = ...,
        includes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.SessionLoggerEventFilterAll]: ...
    @_builtins.property
    @pulumi.getter
    def includes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class SessionLoggerEventFilterAll(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class SessionLoggerLogConfiguration(dict):
    def __init__(
        __self__, *, s3: Optional[outputs.SessionLoggerLogConfigurationS3] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[outputs.SessionLoggerLogConfigurationS3]: ...

@pulumi.output_type
class SessionLoggerLogConfigurationS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        folder_structure: _builtins.str,
        log_file_format: _builtins.str,
        bucket_owner: Optional[_builtins.str] = ...,
        key_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="folderStructure")
    def folder_structure(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logFileFormat")
    def log_file_format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwner")
    def bucket_owner(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TrustStoreCertificate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        body: _builtins.str,
        issuer: Optional[_builtins.str] = ...,
        not_valid_after: Optional[_builtins.str] = ...,
        not_valid_before: Optional[_builtins.str] = ...,
        subject: Optional[_builtins.str] = ...,
        thumbprint: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notValidAfter")
    def not_valid_after(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notValidBefore")
    def not_valid_before(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserSettingsCookieSynchronizationConfiguration(dict):
    def __init__(
        __self__,
        *,
        allowlists: Optional[
            Sequence[outputs.UserSettingsCookieSynchronizationConfigurationAllowlist]
        ] = ...,
        blocklists: Optional[
            Sequence[outputs.UserSettingsCookieSynchronizationConfigurationBlocklist]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def allowlists(
        self,
    ) -> Optional[
        Sequence[outputs.UserSettingsCookieSynchronizationConfigurationAllowlist]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def blocklists(
        self,
    ) -> Optional[
        Sequence[outputs.UserSettingsCookieSynchronizationConfigurationBlocklist]
    ]: ...

@pulumi.output_type
class UserSettingsCookieSynchronizationConfigurationAllowlist(dict):
    def __init__(
        __self__,
        *,
        domain: _builtins.str,
        name: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserSettingsCookieSynchronizationConfigurationBlocklist(dict):
    def __init__(
        __self__,
        *,
        domain: _builtins.str,
        name: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class UserSettingsToolbarConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        hidden_toolbar_items: Optional[Sequence[_builtins.str]] = ...,
        max_display_resolution: Optional[_builtins.str] = ...,
        toolbar_type: Optional[_builtins.str] = ...,
        visual_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hiddenToolbarItems")
    def hidden_toolbar_items(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxDisplayResolution")
    def max_display_resolution(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="toolbarType")
    def toolbar_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="visualMode")
    def visual_mode(self) -> Optional[_builtins.str]: ...
