import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppAutoBranchCreationConfig",
    "AppCacheConfig",
    "AppCustomRule",
    "AppJobConfig",
    "AppProductionBranch",
    "DomainAssociationCertificateSettings",
    "DomainAssociationSubDomain",
]

@pulumi.output_type
class AppAutoBranchCreationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        basic_auth_credentials: Optional[_builtins.str] = ...,
        build_spec: Optional[_builtins.str] = ...,
        enable_auto_build: Optional[_builtins.bool] = ...,
        enable_basic_auth: Optional[_builtins.bool] = ...,
        enable_performance_mode: Optional[_builtins.bool] = ...,
        enable_pull_request_preview: Optional[_builtins.bool] = ...,
        environment_variables: Optional[Mapping[str, _builtins.str]] = ...,
        framework: Optional[_builtins.str] = ...,
        pull_request_environment_name: Optional[_builtins.str] = ...,
        stage: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAutoBuild")
    def enable_auto_build(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePerformanceMode")
    def enable_performance_mode(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePullRequestPreview")
    def enable_pull_request_preview(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def framework(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def stage(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppCacheConfig(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class AppCustomRule(dict):
    def __init__(
        __self__,
        *,
        source: _builtins.str,
        target: _builtins.str,
        condition: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppJobConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, build_compute_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="buildComputeType")
    def build_compute_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppProductionBranch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        branch_name: Optional[_builtins.str] = ...,
        last_deploy_time: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        thumbnail_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lastDeployTime")
    def last_deploy_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="thumbnailUrl")
    def thumbnail_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainAssociationCertificateSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        certificate_verification_dns_record: Optional[_builtins.str] = ...,
        custom_certificate_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateVerificationDnsRecord")
    def certificate_verification_dns_record(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customCertificateArn")
    def custom_certificate_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainAssociationSubDomain(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        branch_name: _builtins.str,
        prefix: _builtins.str,
        dns_record: Optional[_builtins.str] = ...,
        verified: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dnsRecord")
    def dns_record(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def verified(self) -> Optional[_builtins.bool]: ...
