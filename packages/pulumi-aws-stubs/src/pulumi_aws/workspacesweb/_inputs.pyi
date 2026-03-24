import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "IpAccessSettingsIpRuleArgs",
    "IpAccessSettingsIpRuleArgsDict",
    "PortalTimeoutsArgs",
    "PortalTimeoutsArgsDict",
    "SessionLoggerEventFilterArgs",
    "SessionLoggerEventFilterArgsDict",
    "SessionLoggerEventFilterAllArgs",
    "SessionLoggerEventFilterAllArgsDict",
    "SessionLoggerLogConfigurationArgs",
    "SessionLoggerLogConfigurationArgsDict",
    "SessionLoggerLogConfigurationS3Args",
    "SessionLoggerLogConfigurationS3ArgsDict",
    "TrustStoreCertificateArgs",
    "TrustStoreCertificateArgsDict",
    "UserSettingsCookieSynchronizationConfigurationArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "UserSettingsToolbarConfigurationArgs",
    "UserSettingsToolbarConfigurationArgsDict",
]

class DataProtectionSettingsInlineRedactionConfigurationArgsDict(TypedDict):
    inline_redaction_patterns: pulumi.Input[
        Sequence[
            pulumi.Input[
                DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternArgsDict
            ]
        ]
    ]
    global_confidence_level: NotRequired[pulumi.Input[_builtins.int]]
    global_enforced_urls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    global_exempt_urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DataProtectionSettingsInlineRedactionConfigurationArgs:
    def __init__(
        __self__,
        *,
        inline_redaction_patterns: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternArgs
                ]
            ]
        ],
        global_confidence_level: Optional[pulumi.Input[_builtins.int]] = ...,
        global_enforced_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        global_exempt_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inlineRedactionPatterns")
    def inline_redaction_patterns(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternArgs
            ]
        ]
    ]: ...
    @inline_redaction_patterns.setter
    def inline_redaction_patterns(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalConfidenceLevel")
    def global_confidence_level(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @global_confidence_level.setter
    def global_confidence_level(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="globalEnforcedUrls")
    def global_enforced_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @global_enforced_urls.setter
    def global_enforced_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalExemptUrls")
    def global_exempt_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @global_exempt_urls.setter
    def global_exempt_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternArgsDict(
    TypedDict
):
    built_in_pattern_id: NotRequired[pulumi.Input[_builtins.str]]
    confidence_level: NotRequired[pulumi.Input[_builtins.int]]
    custom_pattern: NotRequired[
        pulumi.Input[
            DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternCustomPatternArgsDict
        ]
    ]
    enforced_urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    exempt_urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    redaction_place_holders: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternRedactionPlaceHolderArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternArgs:
    def __init__(
        __self__,
        *,
        built_in_pattern_id: Optional[pulumi.Input[_builtins.str]] = ...,
        confidence_level: Optional[pulumi.Input[_builtins.int]] = ...,
        custom_pattern: Optional[
            pulumi.Input[
                DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternCustomPatternArgs
            ]
        ] = ...,
        enforced_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        exempt_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        redaction_place_holders: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternRedactionPlaceHolderArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="builtInPatternId")
    def built_in_pattern_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @built_in_pattern_id.setter
    def built_in_pattern_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="confidenceLevel")
    def confidence_level(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @confidence_level.setter
    def confidence_level(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="customPattern")
    def custom_pattern(
        self,
    ) -> Optional[
        pulumi.Input[
            DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternCustomPatternArgs
        ]
    ]: ...
    @custom_pattern.setter
    def custom_pattern(
        self,
        value: Optional[
            pulumi.Input[
                DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternCustomPatternArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enforcedUrls")
    def enforced_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enforced_urls.setter
    def enforced_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exemptUrls")
    def exempt_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exempt_urls.setter
    def exempt_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redactionPlaceHolders")
    def redaction_place_holders(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternRedactionPlaceHolderArgs
                ]
            ]
        ]
    ]: ...
    @redaction_place_holders.setter
    def redaction_place_holders(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternRedactionPlaceHolderArgs
                    ]
                ]
            ]
        ],
    ): ...

class DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternCustomPatternArgsDict(
    TypedDict
):
    pattern_name: pulumi.Input[_builtins.str]
    pattern_regex: pulumi.Input[_builtins.str]
    keyword_regex: NotRequired[pulumi.Input[_builtins.str]]
    pattern_description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternCustomPatternArgs:
    def __init__(
        __self__,
        *,
        pattern_name: pulumi.Input[_builtins.str],
        pattern_regex: pulumi.Input[_builtins.str],
        keyword_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        pattern_description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="patternName")
    def pattern_name(self) -> pulumi.Input[_builtins.str]: ...
    @pattern_name.setter
    def pattern_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="patternRegex")
    def pattern_regex(self) -> pulumi.Input[_builtins.str]: ...
    @pattern_regex.setter
    def pattern_regex(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keywordRegex")
    def keyword_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @keyword_regex.setter
    def keyword_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="patternDescription")
    def pattern_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pattern_description.setter
    def pattern_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternRedactionPlaceHolderArgsDict(
    TypedDict
):
    redaction_place_holder_type: pulumi.Input[_builtins.str]
    redaction_place_holder_text: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataProtectionSettingsInlineRedactionConfigurationInlineRedactionPatternRedactionPlaceHolderArgs:
    def __init__(
        __self__,
        *,
        redaction_place_holder_type: pulumi.Input[_builtins.str],
        redaction_place_holder_text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="redactionPlaceHolderType")
    def redaction_place_holder_type(self) -> pulumi.Input[_builtins.str]: ...
    @redaction_place_holder_type.setter
    def redaction_place_holder_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="redactionPlaceHolderText")
    def redaction_place_holder_text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redaction_place_holder_text.setter
    def redaction_place_holder_text(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class IpAccessSettingsIpRuleArgsDict(TypedDict):
    ip_range: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class IpAccessSettingsIpRuleArgs:
    def __init__(
        __self__,
        *,
        ip_range: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> pulumi.Input[_builtins.str]: ...
    @ip_range.setter
    def ip_range(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PortalTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class PortalTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SessionLoggerEventFilterArgsDict(TypedDict):
    all: NotRequired[pulumi.Input[SessionLoggerEventFilterAllArgsDict]]
    includes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class SessionLoggerEventFilterArgs:
    def __init__(
        __self__,
        *,
        all: Optional[pulumi.Input[SessionLoggerEventFilterAllArgs]] = ...,
        includes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[pulumi.Input[SessionLoggerEventFilterAllArgs]]: ...
    @all.setter
    def all(self, value: Optional[pulumi.Input[SessionLoggerEventFilterAllArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @includes.setter
    def includes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SessionLoggerEventFilterAllArgsDict(TypedDict): ...

@pulumi.input_type
class SessionLoggerEventFilterAllArgs:
    def __init__(__self__) -> None: ...

class SessionLoggerLogConfigurationArgsDict(TypedDict):
    s3: NotRequired[pulumi.Input[SessionLoggerLogConfigurationS3ArgsDict]]
    ...

@pulumi.input_type
class SessionLoggerLogConfigurationArgs:
    def __init__(
        __self__,
        *,
        s3: Optional[pulumi.Input[SessionLoggerLogConfigurationS3Args]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[SessionLoggerLogConfigurationS3Args]]: ...
    @s3.setter
    def s3(
        self, value: Optional[pulumi.Input[SessionLoggerLogConfigurationS3Args]]
    ): ...

class SessionLoggerLogConfigurationS3ArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    folder_structure: pulumi.Input[_builtins.str]
    log_file_format: pulumi.Input[_builtins.str]
    bucket_owner: NotRequired[pulumi.Input[_builtins.str]]
    key_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class SessionLoggerLogConfigurationS3Args:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        folder_structure: pulumi.Input[_builtins.str],
        log_file_format: pulumi.Input[_builtins.str],
        bucket_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="folderStructure")
    def folder_structure(self) -> pulumi.Input[_builtins.str]: ...
    @folder_structure.setter
    def folder_structure(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logFileFormat")
    def log_file_format(self) -> pulumi.Input[_builtins.str]: ...
    @log_file_format.setter
    def log_file_format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketOwner")
    def bucket_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_owner.setter
    def bucket_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_prefix.setter
    def key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TrustStoreCertificateArgsDict(TypedDict):
    body: pulumi.Input[_builtins.str]
    issuer: NotRequired[pulumi.Input[_builtins.str]]
    not_valid_after: NotRequired[pulumi.Input[_builtins.str]]
    not_valid_before: NotRequired[pulumi.Input[_builtins.str]]
    subject: NotRequired[pulumi.Input[_builtins.str]]
    thumbprint: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class TrustStoreCertificateArgs:
    def __init__(
        __self__,
        *,
        body: pulumi.Input[_builtins.str],
        issuer: Optional[pulumi.Input[_builtins.str]] = ...,
        not_valid_after: Optional[pulumi.Input[_builtins.str]] = ...,
        not_valid_before: Optional[pulumi.Input[_builtins.str]] = ...,
        subject: Optional[pulumi.Input[_builtins.str]] = ...,
        thumbprint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def body(self) -> pulumi.Input[_builtins.str]: ...
    @body.setter
    def body(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notValidAfter")
    def not_valid_after(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_valid_after.setter
    def not_valid_after(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notValidBefore")
    def not_valid_before(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @not_valid_before.setter
    def not_valid_before(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject.setter
    def subject(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserSettingsCookieSynchronizationConfigurationArgsDict(TypedDict):
    allowlists: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    UserSettingsCookieSynchronizationConfigurationAllowlistArgsDict
                ]
            ]
        ]
    ]
    blocklists: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    UserSettingsCookieSynchronizationConfigurationBlocklistArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class UserSettingsCookieSynchronizationConfigurationArgs:
    def __init__(
        __self__,
        *,
        allowlists: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        UserSettingsCookieSynchronizationConfigurationAllowlistArgs
                    ]
                ]
            ]
        ] = ...,
        blocklists: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        UserSettingsCookieSynchronizationConfigurationBlocklistArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def allowlists(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    UserSettingsCookieSynchronizationConfigurationAllowlistArgs
                ]
            ]
        ]
    ]: ...
    @allowlists.setter
    def allowlists(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        UserSettingsCookieSynchronizationConfigurationAllowlistArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def blocklists(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    UserSettingsCookieSynchronizationConfigurationBlocklistArgs
                ]
            ]
        ]
    ]: ...
    @blocklists.setter
    def blocklists(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        UserSettingsCookieSynchronizationConfigurationBlocklistArgs
                    ]
                ]
            ]
        ],
    ): ...

class UserSettingsCookieSynchronizationConfigurationAllowlistArgsDict(TypedDict):
    domain: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class UserSettingsCookieSynchronizationConfigurationAllowlistArgs:
    def __init__(
        __self__,
        *,
        domain: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserSettingsCookieSynchronizationConfigurationBlocklistArgsDict(TypedDict):
    domain: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class UserSettingsCookieSynchronizationConfigurationBlocklistArgs:
    def __init__(
        __self__,
        *,
        domain: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class UserSettingsToolbarConfigurationArgsDict(TypedDict):
    hidden_toolbar_items: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    max_display_resolution: NotRequired[pulumi.Input[_builtins.str]]
    toolbar_type: NotRequired[pulumi.Input[_builtins.str]]
    visual_mode: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class UserSettingsToolbarConfigurationArgs:
    def __init__(
        __self__,
        *,
        hidden_toolbar_items: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        max_display_resolution: Optional[pulumi.Input[_builtins.str]] = ...,
        toolbar_type: Optional[pulumi.Input[_builtins.str]] = ...,
        visual_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hiddenToolbarItems")
    def hidden_toolbar_items(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @hidden_toolbar_items.setter
    def hidden_toolbar_items(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxDisplayResolution")
    def max_display_resolution(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_display_resolution.setter
    def max_display_resolution(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="toolbarType")
    def toolbar_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @toolbar_type.setter
    def toolbar_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="visualMode")
    def visual_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visual_mode.setter
    def visual_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
