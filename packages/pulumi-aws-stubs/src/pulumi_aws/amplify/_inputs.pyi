import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppAutoBranchCreationConfigArgs",
    "AppAutoBranchCreationConfigArgsDict",
    "AppCacheConfigArgs",
    "AppCacheConfigArgsDict",
    "AppCustomRuleArgs",
    "AppCustomRuleArgsDict",
    "AppJobConfigArgs",
    "AppJobConfigArgsDict",
    "AppProductionBranchArgs",
    "AppProductionBranchArgsDict",
    "DomainAssociationCertificateSettingsArgs",
    "DomainAssociationCertificateSettingsArgsDict",
    "DomainAssociationSubDomainArgs",
    "DomainAssociationSubDomainArgsDict",
]

class AppAutoBranchCreationConfigArgsDict(TypedDict):
    basic_auth_credentials: NotRequired[pulumi.Input[_builtins.str]]
    build_spec: NotRequired[pulumi.Input[_builtins.str]]
    enable_auto_build: NotRequired[pulumi.Input[_builtins.bool]]
    enable_basic_auth: NotRequired[pulumi.Input[_builtins.bool]]
    enable_performance_mode: NotRequired[pulumi.Input[_builtins.bool]]
    enable_pull_request_preview: NotRequired[pulumi.Input[_builtins.bool]]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    framework: NotRequired[pulumi.Input[_builtins.str]]
    pull_request_environment_name: NotRequired[pulumi.Input[_builtins.str]]
    stage: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AppAutoBranchCreationConfigArgs:
    def __init__(
        __self__,
        *,
        basic_auth_credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        build_spec: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_auto_build: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_basic_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_performance_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_pull_request_preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        framework: Optional[pulumi.Input[_builtins.str]] = ...,
        pull_request_environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        stage: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @basic_auth_credentials.setter
    def basic_auth_credentials(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_spec.setter
    def build_spec(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAutoBuild")
    def enable_auto_build(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_auto_build.setter
    def enable_auto_build(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_basic_auth.setter
    def enable_basic_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enablePerformanceMode")
    def enable_performance_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_performance_mode.setter
    def enable_performance_mode(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enablePullRequestPreview")
    def enable_pull_request_preview(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_pull_request_preview.setter
    def enable_pull_request_preview(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def framework(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @framework.setter
    def framework(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pullRequestEnvironmentName")
    def pull_request_environment_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pull_request_environment_name.setter
    def pull_request_environment_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stage.setter
    def stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppCacheConfigArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class AppCacheConfigArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class AppCustomRuleArgsDict(TypedDict):
    source: pulumi.Input[_builtins.str]
    target: pulumi.Input[_builtins.str]
    condition: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AppCustomRuleArgs:
    def __init__(
        __self__,
        *,
        source: pulumi.Input[_builtins.str],
        target: pulumi.Input[_builtins.str],
        condition: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppJobConfigArgsDict(TypedDict):
    build_compute_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AppJobConfigArgs:
    def __init__(
        __self__, *, build_compute_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="buildComputeType")
    def build_compute_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build_compute_type.setter
    def build_compute_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppProductionBranchArgsDict(TypedDict):
    branch_name: NotRequired[pulumi.Input[_builtins.str]]
    last_deploy_time: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    thumbnail_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AppProductionBranchArgs:
    def __init__(
        __self__,
        *,
        branch_name: Optional[pulumi.Input[_builtins.str]] = ...,
        last_deploy_time: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        thumbnail_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch_name.setter
    def branch_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastDeployTime")
    def last_deploy_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_deploy_time.setter
    def last_deploy_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="thumbnailUrl")
    def thumbnail_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @thumbnail_url.setter
    def thumbnail_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainAssociationCertificateSettingsArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    certificate_verification_dns_record: NotRequired[pulumi.Input[_builtins.str]]
    custom_certificate_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainAssociationCertificateSettingsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        certificate_verification_dns_record: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        custom_certificate_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateVerificationDnsRecord")
    def certificate_verification_dns_record(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_verification_dns_record.setter
    def certificate_verification_dns_record(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customCertificateArn")
    def custom_certificate_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_certificate_arn.setter
    def custom_certificate_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainAssociationSubDomainArgsDict(TypedDict):
    branch_name: pulumi.Input[_builtins.str]
    prefix: pulumi.Input[_builtins.str]
    dns_record: NotRequired[pulumi.Input[_builtins.str]]
    verified: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DomainAssociationSubDomainArgs:
    def __init__(
        __self__,
        *,
        branch_name: pulumi.Input[_builtins.str],
        prefix: pulumi.Input[_builtins.str],
        dns_record: Optional[pulumi.Input[_builtins.str]] = ...,
        verified: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> pulumi.Input[_builtins.str]: ...
    @branch_name.setter
    def branch_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]: ...
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dnsRecord")
    def dns_record(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_record.setter
    def dns_record(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def verified(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @verified.setter
    def verified(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
