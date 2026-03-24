import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AiLogicConfigGenerativeLanguageConfigArgs",
    "AiLogicConfigGenerativeLanguageConfigArgsDict",
    "AiLogicConfigTelemetryConfigArgs",
    "AiLogicConfigTelemetryConfigArgsDict",
    "AppHostingBackendCodebaseArgs",
    "AppHostingBackendCodebaseArgsDict",
    "AppHostingBackendManagedResourceArgs",
    "AppHostingBackendManagedResourceArgsDict",
    "AppHostingBackendManagedResourceRunServiceArgs",
    "AppHostingBackendManagedResourceRunServiceArgsDict",
    "AppHostingBuildErrorArgs",
    "AppHostingBuildErrorArgsDict",
    "AppHostingBuildSourceArgs",
    "AppHostingBuildSourceArgsDict",
    "AppHostingBuildSourceCodebaseArgs",
    "AppHostingBuildSourceCodebaseArgsDict",
    "AppHostingBuildSourceCodebaseAuthorArgs",
    "AppHostingBuildSourceCodebaseAuthorArgsDict",
    "AppHostingBuildSourceContainerArgs",
    "AppHostingBuildSourceContainerArgsDict",
    "AppHostingDomainCustomDomainStatusArgs",
    "AppHostingDomainCustomDomainStatusArgsDict",
    "AppHostingDomainCustomDomainStatusIssueArgs",
    "AppHostingDomainCustomDomainStatusIssueArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AppHostingDomainServeArgs",
    "AppHostingDomainServeArgsDict",
    "AppHostingDomainServeRedirectArgs",
    "AppHostingDomainServeRedirectArgsDict",
    "AppHostingTrafficCurrentArgs",
    "AppHostingTrafficCurrentArgsDict",
    "AppHostingTrafficCurrentSplitArgs",
    "AppHostingTrafficCurrentSplitArgsDict",
    "AppHostingTrafficRolloutPolicyArgs",
    "AppHostingTrafficRolloutPolicyArgsDict",
    "AppHostingTrafficTargetArgs",
    "AppHostingTrafficTargetArgsDict",
    "AppHostingTrafficTargetSplitArgs",
    "AppHostingTrafficTargetSplitArgsDict",
    "ExtensionsInstanceConfigArgs",
    "ExtensionsInstanceConfigArgsDict",
    "ExtensionsInstanceErrorStatusArgs",
    "ExtensionsInstanceErrorStatusArgsDict",
    "ExtensionsInstanceRuntimeDataArgs",
    "ExtensionsInstanceRuntimeDataArgsDict",
    "ExtensionsInstanceRuntimeDataFatalErrorArgs",
    "ExtensionsInstanceRuntimeDataFatalErrorArgsDict",
    "ExtensionsInstanceRuntimeDataProcessingStateArgs",
    ...,
    "HostingCustomDomainCertArgs",
    "HostingCustomDomainCertArgsDict",
    "HostingCustomDomainCertVerificationArgs",
    "HostingCustomDomainCertVerificationArgsDict",
    "HostingCustomDomainCertVerificationDnsArgs",
    "HostingCustomDomainCertVerificationDnsArgsDict",
    "HostingCustomDomainCertVerificationDnsDesiredArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "HostingCustomDomainCertVerificationHttpArgs",
    "HostingCustomDomainCertVerificationHttpArgsDict",
    "HostingCustomDomainIssueArgs",
    "HostingCustomDomainIssueArgsDict",
    "HostingCustomDomainRequiredDnsUpdateArgs",
    "HostingCustomDomainRequiredDnsUpdateArgsDict",
    "HostingCustomDomainRequiredDnsUpdateDesiredArgs",
    ...,
    ...,
    ...,
    "HostingCustomDomainRequiredDnsUpdateDiscoveredArgs",
    ...,
    ...,
    ...,
    "HostingVersionConfigArgs",
    "HostingVersionConfigArgsDict",
    "HostingVersionConfigHeaderArgs",
    "HostingVersionConfigHeaderArgsDict",
    "HostingVersionConfigRedirectArgs",
    "HostingVersionConfigRedirectArgsDict",
    "HostingVersionConfigRewriteArgs",
    "HostingVersionConfigRewriteArgsDict",
    "HostingVersionConfigRewriteRunArgs",
    "HostingVersionConfigRewriteRunArgsDict",
]

class AiLogicConfigGenerativeLanguageConfigArgsDict(TypedDict):
    api_key: NotRequired[pulumi.Input[_builtins.str]]
    api_key_wo: NotRequired[pulumi.Input[_builtins.str]]
    api_key_wo_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AiLogicConfigGenerativeLanguageConfigArgs:
    def __init__(
        __self__,
        *,
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_wo: Optional[pulumi.Input[_builtins.str]] = ...,
        api_key_wo_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="apiKeyWo")
    def api_key_wo(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_wo.setter
    def api_key_wo(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="apiKeyWoVersion")
    def api_key_wo_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_wo_version.setter
    def api_key_wo_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AiLogicConfigTelemetryConfigArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]
    sampling_rate: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AiLogicConfigTelemetryConfigArgs:
    def __init__(
        __self__,
        *,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        sampling_rate: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @sampling_rate.setter
    def sampling_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppHostingBackendCodebaseArgsDict(TypedDict):
    repository: pulumi.Input[_builtins.str]
    root_directory: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingBackendCodebaseArgs:
    def __init__(
        __self__,
        *,
        repository: pulumi.Input[_builtins.str],
        root_directory: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Input[_builtins.str]: ...
    @repository.setter
    def repository(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_directory.setter
    def root_directory(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingBackendManagedResourceArgsDict(TypedDict):
    run_services: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppHostingBackendManagedResourceRunServiceArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class AppHostingBackendManagedResourceArgs:
    def __init__(
        __self__,
        *,
        run_services: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppHostingBackendManagedResourceRunServiceArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="runServices")
    def run_services(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppHostingBackendManagedResourceRunServiceArgs]]
        ]
    ]: ...
    @run_services.setter
    def run_services(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppHostingBackendManagedResourceRunServiceArgs]]
            ]
        ],
    ): ...

class AppHostingBackendManagedResourceRunServiceArgsDict(TypedDict):
    service: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingBackendManagedResourceRunServiceArgs:
    def __init__(
        __self__, *, service: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingBuildErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingBuildErrorArgs:
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

class AppHostingBuildSourceArgsDict(TypedDict):
    codebase: NotRequired[pulumi.Input[AppHostingBuildSourceCodebaseArgsDict]]
    container: NotRequired[pulumi.Input[AppHostingBuildSourceContainerArgsDict]]
    ...

@pulumi.input_type
class AppHostingBuildSourceArgs:
    def __init__(
        __self__,
        *,
        codebase: Optional[pulumi.Input[AppHostingBuildSourceCodebaseArgs]] = ...,
        container: Optional[pulumi.Input[AppHostingBuildSourceContainerArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def codebase(self) -> Optional[pulumi.Input[AppHostingBuildSourceCodebaseArgs]]: ...
    @codebase.setter
    def codebase(
        self, value: Optional[pulumi.Input[AppHostingBuildSourceCodebaseArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def container(
        self,
    ) -> Optional[pulumi.Input[AppHostingBuildSourceContainerArgs]]: ...
    @container.setter
    def container(
        self, value: Optional[pulumi.Input[AppHostingBuildSourceContainerArgs]]
    ): ...

class AppHostingBuildSourceCodebaseArgsDict(TypedDict):
    authors: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppHostingBuildSourceCodebaseAuthorArgsDict]]
        ]
    ]
    branch: NotRequired[pulumi.Input[_builtins.str]]
    commit: NotRequired[pulumi.Input[_builtins.str]]
    commit_message: NotRequired[pulumi.Input[_builtins.str]]
    commit_time: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    hash: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingBuildSourceCodebaseArgs:
    def __init__(
        __self__,
        *,
        authors: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppHostingBuildSourceCodebaseAuthorArgs]]
            ]
        ] = ...,
        branch: Optional[pulumi.Input[_builtins.str]] = ...,
        commit: Optional[pulumi.Input[_builtins.str]] = ...,
        commit_message: Optional[pulumi.Input[_builtins.str]] = ...,
        commit_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        hash: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def authors(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppHostingBuildSourceCodebaseAuthorArgs]]]
    ]: ...
    @authors.setter
    def authors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppHostingBuildSourceCodebaseAuthorArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch.setter
    def branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def commit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commit.setter
    def commit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commitMessage")
    def commit_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commit_message.setter
    def commit_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commitTime")
    def commit_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commit_time.setter
    def commit_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def hash(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hash.setter
    def hash(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingBuildSourceCodebaseAuthorArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    email: NotRequired[pulumi.Input[_builtins.str]]
    image_uri: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingBuildSourceCodebaseAuthorArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        email: Optional[pulumi.Input[_builtins.str]] = ...,
        image_uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingBuildSourceContainerArgsDict(TypedDict):
    image: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AppHostingBuildSourceContainerArgs:
    def __init__(__self__, *, image: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]: ...
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): ...

class AppHostingDomainCustomDomainStatusArgsDict(TypedDict):
    cert_state: NotRequired[pulumi.Input[_builtins.str]]
    host_state: NotRequired[pulumi.Input[_builtins.str]]
    issues: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppHostingDomainCustomDomainStatusIssueArgsDict]]
        ]
    ]
    ownership_state: NotRequired[pulumi.Input[_builtins.str]]
    required_dns_updates: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppHostingDomainCustomDomainStatusArgs:
    def __init__(
        __self__,
        *,
        cert_state: Optional[pulumi.Input[_builtins.str]] = ...,
        host_state: Optional[pulumi.Input[_builtins.str]] = ...,
        issues: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppHostingDomainCustomDomainStatusIssueArgs]]
            ]
        ] = ...,
        ownership_state: Optional[pulumi.Input[_builtins.str]] = ...,
        required_dns_updates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certState")
    def cert_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert_state.setter
    def cert_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostState")
    def host_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_state.setter
    def host_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def issues(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppHostingDomainCustomDomainStatusIssueArgs]]
        ]
    ]: ...
    @issues.setter
    def issues(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppHostingDomainCustomDomainStatusIssueArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ownershipState")
    def ownership_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ownership_state.setter
    def ownership_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredDnsUpdates")
    def required_dns_updates(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppHostingDomainCustomDomainStatusRequiredDnsUpdateArgs]
            ]
        ]
    ]: ...
    @required_dns_updates.setter
    def required_dns_updates(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppHostingDomainCustomDomainStatusIssueArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingDomainCustomDomainStatusIssueArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingDomainCustomDomainStatusRequiredDnsUpdateArgsDict(TypedDict):
    check_time: NotRequired[pulumi.Input[_builtins.str]]
    desireds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredArgsDict
                ]
            ]
        ]
    ]
    discovereds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredArgsDict
                ]
            ]
        ]
    ]
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateArgs:
    def __init__(
        __self__,
        *,
        check_time: Optional[pulumi.Input[_builtins.str]] = ...,
        desireds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredArgs
                    ]
                ]
            ]
        ] = ...,
        discovereds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredArgs
                    ]
                ]
            ]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkTime")
    def check_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @check_time.setter
    def check_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def desireds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredArgs
                ]
            ]
        ]
    ]: ...
    @desireds.setter
    def desireds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def discovereds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredArgs
                ]
            ]
        ]
    ]: ...
    @discovereds.setter
    def discovereds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredArgsDict(TypedDict):
    check_errors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredCheckErrorArgsDict
                ]
            ]
        ]
    ]
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    records: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredRecordArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredArgs:
    def __init__(
        __self__,
        *,
        check_errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredCheckErrorArgs
                    ]
                ]
            ]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredRecordArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkErrors")
    def check_errors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredCheckErrorArgs
                ]
            ]
        ]
    ]: ...
    @check_errors.setter
    def check_errors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredCheckErrorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def records(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredRecordArgs
                ]
            ]
        ]
    ]: ...
    @records.setter
    def records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredRecordArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredCheckErrorArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredCheckErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredRecordArgsDict(
    TypedDict
):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    rdata: NotRequired[pulumi.Input[_builtins.str]]
    relevant_states: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    required_action: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredRecordArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rdata: Optional[pulumi.Input[_builtins.str]] = ...,
        relevant_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        required_action: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdata.setter
    def rdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relevantStates")
    def relevant_states(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @relevant_states.setter
    def relevant_states(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @required_action.setter
    def required_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredArgsDict(TypedDict):
    check_errors: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredCheckErrorArgsDict
                ]
            ]
        ]
    ]
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    records: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredRecordArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredArgs:
    def __init__(
        __self__,
        *,
        check_errors: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredCheckErrorArgs
                    ]
                ]
            ]
        ] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredRecordArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkErrors")
    def check_errors(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredCheckErrorArgs
                ]
            ]
        ]
    ]: ...
    @check_errors.setter
    def check_errors(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredCheckErrorArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def records(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredRecordArgs
                ]
            ]
        ]
    ]: ...
    @records.setter
    def records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredRecordArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredCheckErrorArgsDict(
    TypedDict
):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredCheckErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredRecordArgsDict(
    TypedDict
):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    rdata: NotRequired[pulumi.Input[_builtins.str]]
    relevant_states: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    required_action: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredRecordArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rdata: Optional[pulumi.Input[_builtins.str]] = ...,
        relevant_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        required_action: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdata.setter
    def rdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relevantStates")
    def relevant_states(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @relevant_states.setter
    def relevant_states(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @required_action.setter
    def required_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingDomainServeArgsDict(TypedDict):
    redirect: NotRequired[pulumi.Input[AppHostingDomainServeRedirectArgsDict]]
    ...

@pulumi.input_type
class AppHostingDomainServeArgs:
    def __init__(
        __self__,
        *,
        redirect: Optional[pulumi.Input[AppHostingDomainServeRedirectArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> Optional[pulumi.Input[AppHostingDomainServeRedirectArgs]]: ...
    @redirect.setter
    def redirect(
        self, value: Optional[pulumi.Input[AppHostingDomainServeRedirectArgs]]
    ): ...

class AppHostingDomainServeRedirectArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingDomainServeRedirectArgs:
    def __init__(
        __self__,
        *,
        uri: pulumi.Input[_builtins.str],
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]: ...
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingTrafficCurrentArgsDict(TypedDict):
    splits: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficCurrentSplitArgsDict]]]
    ]
    ...

@pulumi.input_type
class AppHostingTrafficCurrentArgs:
    def __init__(
        __self__,
        *,
        splits: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficCurrentSplitArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def splits(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficCurrentSplitArgs]]]
    ]: ...
    @splits.setter
    def splits(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficCurrentSplitArgs]]]
        ],
    ): ...

class AppHostingTrafficCurrentSplitArgsDict(TypedDict):
    build: NotRequired[pulumi.Input[_builtins.str]]
    percent: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AppHostingTrafficCurrentSplitArgs:
    def __init__(
        __self__,
        *,
        build: Optional[pulumi.Input[_builtins.str]] = ...,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build.setter
    def build(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AppHostingTrafficRolloutPolicyArgsDict(TypedDict):
    codebase_branch: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    disabled_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppHostingTrafficRolloutPolicyArgs:
    def __init__(
        __self__,
        *,
        codebase_branch: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        disabled_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="codebaseBranch")
    def codebase_branch(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @codebase_branch.setter
    def codebase_branch(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="disabledTime")
    def disabled_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disabled_time.setter
    def disabled_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppHostingTrafficTargetArgsDict(TypedDict):
    splits: pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficTargetSplitArgsDict]]]
    ...

@pulumi.input_type
class AppHostingTrafficTargetArgs:
    def __init__(
        __self__,
        *,
        splits: pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficTargetSplitArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def splits(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficTargetSplitArgs]]]: ...
    @splits.setter
    def splits(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[AppHostingTrafficTargetSplitArgs]]],
    ): ...

class AppHostingTrafficTargetSplitArgsDict(TypedDict):
    build: pulumi.Input[_builtins.str]
    percent: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class AppHostingTrafficTargetSplitArgs:
    def __init__(
        __self__,
        *,
        build: pulumi.Input[_builtins.str],
        percent: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def build(self) -> pulumi.Input[_builtins.str]: ...
    @build.setter
    def build(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> pulumi.Input[_builtins.int]: ...
    @percent.setter
    def percent(self, value: pulumi.Input[_builtins.int]): ...

class ExtensionsInstanceConfigArgsDict(TypedDict):
    extension_ref: pulumi.Input[_builtins.str]
    params: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    allowed_event_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    eventarc_channel: NotRequired[pulumi.Input[_builtins.str]]
    extension_version: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    populated_postinstall_content: NotRequired[pulumi.Input[_builtins.str]]
    system_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ExtensionsInstanceConfigArgs:
    def __init__(
        __self__,
        *,
        extension_ref: pulumi.Input[_builtins.str],
        params: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        allowed_event_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        eventarc_channel: Optional[pulumi.Input[_builtins.str]] = ...,
        extension_version: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        populated_postinstall_content: Optional[pulumi.Input[_builtins.str]] = ...,
        system_params: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extensionRef")
    def extension_ref(self) -> pulumi.Input[_builtins.str]: ...
    @extension_ref.setter
    def extension_ref(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @params.setter
    def params(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowedEventTypes")
    def allowed_event_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_event_types.setter
    def allowed_event_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eventarcChannel")
    def eventarc_channel(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eventarc_channel.setter
    def eventarc_channel(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="extensionVersion")
    def extension_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extension_version.setter
    def extension_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="populatedPostinstallContent")
    def populated_postinstall_content(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @populated_postinstall_content.setter
    def populated_postinstall_content(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="systemParams")
    def system_params(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @system_params.setter
    def system_params(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ExtensionsInstanceErrorStatusArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]
    ]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ExtensionsInstanceErrorStatusArgs:
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

class ExtensionsInstanceRuntimeDataArgsDict(TypedDict):
    fatal_error: NotRequired[
        pulumi.Input[ExtensionsInstanceRuntimeDataFatalErrorArgsDict]
    ]
    processing_state: NotRequired[
        pulumi.Input[ExtensionsInstanceRuntimeDataProcessingStateArgsDict]
    ]
    state_update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ExtensionsInstanceRuntimeDataArgs:
    def __init__(
        __self__,
        *,
        fatal_error: Optional[
            pulumi.Input[ExtensionsInstanceRuntimeDataFatalErrorArgs]
        ] = ...,
        processing_state: Optional[
            pulumi.Input[ExtensionsInstanceRuntimeDataProcessingStateArgs]
        ] = ...,
        state_update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fatalError")
    def fatal_error(
        self,
    ) -> Optional[pulumi.Input[ExtensionsInstanceRuntimeDataFatalErrorArgs]]: ...
    @fatal_error.setter
    def fatal_error(
        self, value: Optional[pulumi.Input[ExtensionsInstanceRuntimeDataFatalErrorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="processingState")
    def processing_state(
        self,
    ) -> Optional[pulumi.Input[ExtensionsInstanceRuntimeDataProcessingStateArgs]]: ...
    @processing_state.setter
    def processing_state(
        self,
        value: Optional[pulumi.Input[ExtensionsInstanceRuntimeDataProcessingStateArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stateUpdateTime")
    def state_update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_update_time.setter
    def state_update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExtensionsInstanceRuntimeDataFatalErrorArgsDict(TypedDict):
    error_message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ExtensionsInstanceRuntimeDataFatalErrorArgs:
    def __init__(
        __self__, *, error_message: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error_message.setter
    def error_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExtensionsInstanceRuntimeDataProcessingStateArgsDict(TypedDict):
    detail_message: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ExtensionsInstanceRuntimeDataProcessingStateArgs:
    def __init__(
        __self__,
        *,
        detail_message: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="detailMessage")
    def detail_message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @detail_message.setter
    def detail_message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostingCustomDomainCertArgsDict(TypedDict):
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    verification: NotRequired[pulumi.Input[HostingCustomDomainCertVerificationArgsDict]]
    ...

@pulumi.input_type
class HostingCustomDomainCertArgs:
    def __init__(
        __self__,
        *,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        verification: Optional[
            pulumi.Input[HostingCustomDomainCertVerificationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def verification(
        self,
    ) -> Optional[pulumi.Input[HostingCustomDomainCertVerificationArgs]]: ...
    @verification.setter
    def verification(
        self, value: Optional[pulumi.Input[HostingCustomDomainCertVerificationArgs]]
    ): ...

class HostingCustomDomainCertVerificationArgsDict(TypedDict):
    dns: NotRequired[pulumi.Input[HostingCustomDomainCertVerificationDnsArgsDict]]
    http: NotRequired[pulumi.Input[HostingCustomDomainCertVerificationHttpArgsDict]]
    ...

@pulumi.input_type
class HostingCustomDomainCertVerificationArgs:
    def __init__(
        __self__,
        *,
        dns: Optional[pulumi.Input[HostingCustomDomainCertVerificationDnsArgs]] = ...,
        http: Optional[pulumi.Input[HostingCustomDomainCertVerificationHttpArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dns(
        self,
    ) -> Optional[pulumi.Input[HostingCustomDomainCertVerificationDnsArgs]]: ...
    @dns.setter
    def dns(
        self, value: Optional[pulumi.Input[HostingCustomDomainCertVerificationDnsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def http(
        self,
    ) -> Optional[pulumi.Input[HostingCustomDomainCertVerificationHttpArgs]]: ...
    @http.setter
    def http(
        self, value: Optional[pulumi.Input[HostingCustomDomainCertVerificationHttpArgs]]
    ): ...

class HostingCustomDomainCertVerificationDnsArgsDict(TypedDict):
    check_time: NotRequired[pulumi.Input[_builtins.str]]
    desireds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[HostingCustomDomainCertVerificationDnsDesiredArgsDict]
            ]
        ]
    ]
    discovereds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[HostingCustomDomainCertVerificationDnsDiscoveredArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class HostingCustomDomainCertVerificationDnsArgs:
    def __init__(
        __self__,
        *,
        check_time: Optional[pulumi.Input[_builtins.str]] = ...,
        desireds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[HostingCustomDomainCertVerificationDnsDesiredArgs]
                ]
            ]
        ] = ...,
        discovereds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[HostingCustomDomainCertVerificationDnsDiscoveredArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkTime")
    def check_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @check_time.setter
    def check_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def desireds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[HostingCustomDomainCertVerificationDnsDesiredArgs]]
        ]
    ]: ...
    @desireds.setter
    def desireds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[HostingCustomDomainCertVerificationDnsDesiredArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def discovereds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[HostingCustomDomainCertVerificationDnsDiscoveredArgs]]
        ]
    ]: ...
    @discovereds.setter
    def discovereds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[HostingCustomDomainCertVerificationDnsDiscoveredArgs]
                ]
            ]
        ],
    ): ...

class HostingCustomDomainCertVerificationDnsDesiredArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    records: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    HostingCustomDomainCertVerificationDnsDesiredRecordArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class HostingCustomDomainCertVerificationDnsDesiredArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        HostingCustomDomainCertVerificationDnsDesiredRecordArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def records(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[HostingCustomDomainCertVerificationDnsDesiredRecordArgs]
            ]
        ]
    ]: ...
    @records.setter
    def records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        HostingCustomDomainCertVerificationDnsDesiredRecordArgs
                    ]
                ]
            ]
        ],
    ): ...

class HostingCustomDomainCertVerificationDnsDesiredRecordArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    rdata: NotRequired[pulumi.Input[_builtins.str]]
    required_action: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostingCustomDomainCertVerificationDnsDesiredRecordArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rdata: Optional[pulumi.Input[_builtins.str]] = ...,
        required_action: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdata.setter
    def rdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @required_action.setter
    def required_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostingCustomDomainCertVerificationDnsDiscoveredArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    records: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    HostingCustomDomainCertVerificationDnsDiscoveredRecordArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class HostingCustomDomainCertVerificationDnsDiscoveredArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        HostingCustomDomainCertVerificationDnsDiscoveredRecordArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def records(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[HostingCustomDomainCertVerificationDnsDiscoveredRecordArgs]
            ]
        ]
    ]: ...
    @records.setter
    def records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        HostingCustomDomainCertVerificationDnsDiscoveredRecordArgs
                    ]
                ]
            ]
        ],
    ): ...

class HostingCustomDomainCertVerificationDnsDiscoveredRecordArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    rdata: NotRequired[pulumi.Input[_builtins.str]]
    required_action: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostingCustomDomainCertVerificationDnsDiscoveredRecordArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rdata: Optional[pulumi.Input[_builtins.str]] = ...,
        required_action: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdata.setter
    def rdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @required_action.setter
    def required_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostingCustomDomainCertVerificationHttpArgsDict(TypedDict):
    desired: NotRequired[pulumi.Input[_builtins.str]]
    discovered: NotRequired[pulumi.Input[_builtins.str]]
    last_check_time: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostingCustomDomainCertVerificationHttpArgs:
    def __init__(
        __self__,
        *,
        desired: Optional[pulumi.Input[_builtins.str]] = ...,
        discovered: Optional[pulumi.Input[_builtins.str]] = ...,
        last_check_time: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def desired(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired.setter
    def desired(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def discovered(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovered.setter
    def discovered(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastCheckTime")
    def last_check_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_check_time.setter
    def last_check_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostingCustomDomainIssueArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostingCustomDomainIssueArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        details: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostingCustomDomainRequiredDnsUpdateArgsDict(TypedDict):
    check_time: NotRequired[pulumi.Input[_builtins.str]]
    desireds: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[HostingCustomDomainRequiredDnsUpdateDesiredArgsDict]]
        ]
    ]
    discovereds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[HostingCustomDomainRequiredDnsUpdateDiscoveredArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class HostingCustomDomainRequiredDnsUpdateArgs:
    def __init__(
        __self__,
        *,
        check_time: Optional[pulumi.Input[_builtins.str]] = ...,
        desireds: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[HostingCustomDomainRequiredDnsUpdateDesiredArgs]]
            ]
        ] = ...,
        discovereds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[HostingCustomDomainRequiredDnsUpdateDiscoveredArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkTime")
    def check_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @check_time.setter
    def check_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def desireds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[HostingCustomDomainRequiredDnsUpdateDesiredArgs]]
        ]
    ]: ...
    @desireds.setter
    def desireds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[HostingCustomDomainRequiredDnsUpdateDesiredArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def discovereds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[HostingCustomDomainRequiredDnsUpdateDiscoveredArgs]]
        ]
    ]: ...
    @discovereds.setter
    def discovereds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[HostingCustomDomainRequiredDnsUpdateDiscoveredArgs]
                ]
            ]
        ],
    ): ...

class HostingCustomDomainRequiredDnsUpdateDesiredArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    records: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[HostingCustomDomainRequiredDnsUpdateDesiredRecordArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class HostingCustomDomainRequiredDnsUpdateDesiredArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[HostingCustomDomainRequiredDnsUpdateDesiredRecordArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def records(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[HostingCustomDomainRequiredDnsUpdateDesiredRecordArgs]
            ]
        ]
    ]: ...
    @records.setter
    def records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[HostingCustomDomainRequiredDnsUpdateDesiredRecordArgs]
                ]
            ]
        ],
    ): ...

class HostingCustomDomainRequiredDnsUpdateDesiredRecordArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    rdata: NotRequired[pulumi.Input[_builtins.str]]
    required_action: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostingCustomDomainRequiredDnsUpdateDesiredRecordArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rdata: Optional[pulumi.Input[_builtins.str]] = ...,
        required_action: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdata.setter
    def rdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @required_action.setter
    def required_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostingCustomDomainRequiredDnsUpdateDiscoveredArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    records: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    HostingCustomDomainRequiredDnsUpdateDiscoveredRecordArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class HostingCustomDomainRequiredDnsUpdateDiscoveredArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        HostingCustomDomainRequiredDnsUpdateDiscoveredRecordArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def records(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[HostingCustomDomainRequiredDnsUpdateDiscoveredRecordArgs]
            ]
        ]
    ]: ...
    @records.setter
    def records(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        HostingCustomDomainRequiredDnsUpdateDiscoveredRecordArgs
                    ]
                ]
            ]
        ],
    ): ...

class HostingCustomDomainRequiredDnsUpdateDiscoveredRecordArgsDict(TypedDict):
    domain_name: NotRequired[pulumi.Input[_builtins.str]]
    rdata: NotRequired[pulumi.Input[_builtins.str]]
    required_action: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostingCustomDomainRequiredDnsUpdateDiscoveredRecordArgs:
    def __init__(
        __self__,
        *,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        rdata: Optional[pulumi.Input[_builtins.str]] = ...,
        required_action: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdata.setter
    def rdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @required_action.setter
    def required_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostingVersionConfigArgsDict(TypedDict):
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigHeaderArgsDict]]]
    ]
    redirects: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigRedirectArgsDict]]]
    ]
    rewrites: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigRewriteArgsDict]]]
    ]
    ...

@pulumi.input_type
class HostingVersionConfigArgs:
    def __init__(
        __self__,
        *,
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigHeaderArgs]]]
        ] = ...,
        redirects: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigRedirectArgs]]]
        ] = ...,
        rewrites: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigRewriteArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigHeaderArgs]]]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigHeaderArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def redirects(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigRedirectArgs]]]
    ]: ...
    @redirects.setter
    def redirects(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigRedirectArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def rewrites(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigRewriteArgs]]]
    ]: ...
    @rewrites.setter
    def rewrites(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[HostingVersionConfigRewriteArgs]]]
        ],
    ): ...

class HostingVersionConfigHeaderArgsDict(TypedDict):
    headers: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    glob: NotRequired[pulumi.Input[_builtins.str]]
    regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostingVersionConfigHeaderArgs:
    def __init__(
        __self__,
        *,
        headers: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]],
        glob: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headers(self) -> pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]: ...
    @headers.setter
    def headers(
        self, value: pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def glob(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @glob.setter
    def glob(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostingVersionConfigRedirectArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    status_code: pulumi.Input[_builtins.int]
    glob: NotRequired[pulumi.Input[_builtins.str]]
    regex: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostingVersionConfigRedirectArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        status_code: pulumi.Input[_builtins.int],
        glob: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> pulumi.Input[_builtins.int]: ...
    @status_code.setter
    def status_code(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def glob(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @glob.setter
    def glob(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class HostingVersionConfigRewriteArgsDict(TypedDict):
    function: NotRequired[pulumi.Input[_builtins.str]]
    glob: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    regex: NotRequired[pulumi.Input[_builtins.str]]
    run: NotRequired[pulumi.Input[HostingVersionConfigRewriteRunArgsDict]]
    ...

@pulumi.input_type
class HostingVersionConfigRewriteArgs:
    def __init__(
        __self__,
        *,
        function: Optional[pulumi.Input[_builtins.str]] = ...,
        glob: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        regex: Optional[pulumi.Input[_builtins.str]] = ...,
        run: Optional[pulumi.Input[HostingVersionConfigRewriteRunArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function.setter
    def function(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def glob(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @glob.setter
    def glob(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @regex.setter
    def regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def run(self) -> Optional[pulumi.Input[HostingVersionConfigRewriteRunArgs]]: ...
    @run.setter
    def run(
        self, value: Optional[pulumi.Input[HostingVersionConfigRewriteRunArgs]]
    ): ...

class HostingVersionConfigRewriteRunArgsDict(TypedDict):
    service_id: pulumi.Input[_builtins.str]
    region: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class HostingVersionConfigRewriteRunArgs:
    def __init__(
        __self__,
        *,
        service_id: pulumi.Input[_builtins.str],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Input[_builtins.str]: ...
    @service_id.setter
    def service_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
