import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FleetComputeConfiguration",
    "FleetScalingConfiguration",
    ...,
    "FleetStatus",
    "FleetVpcConfig",
    "ProjectArtifacts",
    "ProjectBuildBatchConfig",
    "ProjectBuildBatchConfigRestrictions",
    "ProjectCache",
    "ProjectEnvironment",
    "ProjectEnvironmentDockerServer",
    "ProjectEnvironmentEnvironmentVariable",
    "ProjectEnvironmentFleet",
    "ProjectEnvironmentRegistryCredential",
    "ProjectFileSystemLocation",
    "ProjectLogsConfig",
    "ProjectLogsConfigCloudwatchLogs",
    "ProjectLogsConfigS3Logs",
    "ProjectSecondaryArtifact",
    "ProjectSecondarySource",
    "ProjectSecondarySourceAuth",
    "ProjectSecondarySourceBuildStatusConfig",
    "ProjectSecondarySourceGitSubmodulesConfig",
    "ProjectSecondarySourceVersion",
    "ProjectSource",
    "ProjectSourceAuth",
    "ProjectSourceBuildStatusConfig",
    "ProjectSourceGitSubmodulesConfig",
    "ProjectVpcConfig",
    "ReportGroupExportConfig",
    "ReportGroupExportConfigS3Destination",
    "WebhookFilterGroup",
    "WebhookFilterGroupFilter",
    "WebhookPullRequestBuildPolicy",
    "WebhookScopeConfiguration",
    "GetFleetComputeConfigurationResult",
    "GetFleetScalingConfigurationResult",
    ...,
    "GetFleetStatusResult",
    "GetFleetVpcConfigResult",
]

@pulumi.output_type
class FleetComputeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disk: Optional[_builtins.int] = ...,
        instance_type: Optional[_builtins.str] = ...,
        machine_type: Optional[_builtins.str] = ...,
        memory: Optional[_builtins.int] = ...,
        vcpu: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disk(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def vcpu(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FleetScalingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        desired_capacity: Optional[_builtins.int] = ...,
        max_capacity: Optional[_builtins.int] = ...,
        scaling_type: Optional[_builtins.str] = ...,
        target_tracking_scaling_configs: Optional[
            Sequence[outputs.FleetScalingConfigurationTargetTrackingScalingConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="scalingType")
    def scaling_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingScalingConfigs")
    def target_tracking_scaling_configs(
        self,
    ) -> Optional[
        Sequence[outputs.FleetScalingConfigurationTargetTrackingScalingConfig]
    ]: ...

@pulumi.output_type
class FleetScalingConfigurationTargetTrackingScalingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        metric_type: Optional[_builtins.str] = ...,
        target_value: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricType")
    def metric_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class FleetStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        context: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
        status_code: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FleetVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
        vpc_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

@pulumi.output_type
class ProjectArtifacts(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        artifact_identifier: Optional[_builtins.str] = ...,
        bucket_owner_access: Optional[_builtins.str] = ...,
        encryption_disabled: Optional[_builtins.bool] = ...,
        location: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        namespace_type: Optional[_builtins.str] = ...,
        override_artifact_name: Optional[_builtins.bool] = ...,
        packaging: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="artifactIdentifier")
    def artifact_identifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccess")
    def bucket_owner_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overrideArtifactName")
    def override_artifact_name(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def packaging(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectBuildBatchConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service_role: _builtins.str,
        combine_artifacts: Optional[_builtins.bool] = ...,
        restrictions: Optional[outputs.ProjectBuildBatchConfigRestrictions] = ...,
        timeout_in_mins: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="combineArtifacts")
    def combine_artifacts(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def restrictions(self) -> Optional[outputs.ProjectBuildBatchConfigRestrictions]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMins")
    def timeout_in_mins(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ProjectBuildBatchConfigRestrictions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compute_types_alloweds: Optional[Sequence[_builtins.str]] = ...,
        maximum_builds_allowed: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeTypesAlloweds")
    def compute_types_alloweds(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maximumBuildsAllowed")
    def maximum_builds_allowed(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ProjectCache(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cache_namespace: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        modes: Optional[Sequence[_builtins.str]] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheNamespace")
    def cache_namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def modes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectEnvironment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compute_type: _builtins.str,
        image: _builtins.str,
        type: _builtins.str,
        certificate: Optional[_builtins.str] = ...,
        docker_server: Optional[outputs.ProjectEnvironmentDockerServer] = ...,
        environment_variables: Optional[
            Sequence[outputs.ProjectEnvironmentEnvironmentVariable]
        ] = ...,
        fleet: Optional[outputs.ProjectEnvironmentFleet] = ...,
        image_pull_credentials_type: Optional[_builtins.str] = ...,
        privileged_mode: Optional[_builtins.bool] = ...,
        registry_credential: Optional[
            outputs.ProjectEnvironmentRegistryCredential
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dockerServer")
    def docker_server(self) -> Optional[outputs.ProjectEnvironmentDockerServer]: ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[Sequence[outputs.ProjectEnvironmentEnvironmentVariable]]: ...
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> Optional[outputs.ProjectEnvironmentFleet]: ...
    @_builtins.property
    @pulumi.getter(name="imagePullCredentialsType")
    def image_pull_credentials_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privilegedMode")
    def privileged_mode(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="registryCredential")
    def registry_credential(
        self,
    ) -> Optional[outputs.ProjectEnvironmentRegistryCredential]: ...

@pulumi.output_type
class ProjectEnvironmentDockerServer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compute_type: _builtins.str,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ProjectEnvironmentEnvironmentVariable(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        value: _builtins.str,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectEnvironmentFleet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, fleet_arn: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fleetArn")
    def fleet_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectEnvironmentRegistryCredential(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, credential: _builtins.str, credential_provider: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credential(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="credentialProvider")
    def credential_provider(self) -> _builtins.str: ...

@pulumi.output_type
class ProjectFileSystemLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        identifier: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
        mount_options: Optional[_builtins.str] = ...,
        mount_point: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectLogsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[outputs.ProjectLogsConfigCloudwatchLogs] = ...,
        s3_logs: Optional[outputs.ProjectLogsConfigS3Logs] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(self) -> Optional[outputs.ProjectLogsConfigCloudwatchLogs]: ...
    @_builtins.property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> Optional[outputs.ProjectLogsConfigS3Logs]: ...

@pulumi.output_type
class ProjectLogsConfigCloudwatchLogs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        group_name: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        stream_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectLogsConfigS3Logs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_owner_access: Optional[_builtins.str] = ...,
        encryption_disabled: Optional[_builtins.bool] = ...,
        location: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccess")
    def bucket_owner_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectSecondaryArtifact(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        artifact_identifier: _builtins.str,
        type: _builtins.str,
        bucket_owner_access: Optional[_builtins.str] = ...,
        encryption_disabled: Optional[_builtins.bool] = ...,
        location: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        namespace_type: Optional[_builtins.str] = ...,
        override_artifact_name: Optional[_builtins.bool] = ...,
        packaging: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactIdentifier")
    def artifact_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccess")
    def bucket_owner_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="overrideArtifactName")
    def override_artifact_name(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def packaging(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectSecondarySource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_identifier: _builtins.str,
        type: _builtins.str,
        auth: Optional[outputs.ProjectSecondarySourceAuth] = ...,
        build_status_config: Optional[
            outputs.ProjectSecondarySourceBuildStatusConfig
        ] = ...,
        buildspec: Optional[_builtins.str] = ...,
        git_clone_depth: Optional[_builtins.int] = ...,
        git_submodules_config: Optional[
            outputs.ProjectSecondarySourceGitSubmodulesConfig
        ] = ...,
        insecure_ssl: Optional[_builtins.bool] = ...,
        location: Optional[_builtins.str] = ...,
        report_build_status: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[outputs.ProjectSecondarySourceAuth]: ...
    @_builtins.property
    @pulumi.getter(name="buildStatusConfig")
    def build_status_config(
        self,
    ) -> Optional[outputs.ProjectSecondarySourceBuildStatusConfig]: ...
    @_builtins.property
    @pulumi.getter
    def buildspec(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gitCloneDepth")
    def git_clone_depth(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="gitSubmodulesConfig")
    def git_submodules_config(
        self,
    ) -> Optional[outputs.ProjectSecondarySourceGitSubmodulesConfig]: ...
    @_builtins.property
    @pulumi.getter(name="insecureSsl")
    def insecure_ssl(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reportBuildStatus")
    def report_build_status(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ProjectSecondarySourceAuth(dict):
    def __init__(__self__, *, resource: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ProjectSecondarySourceBuildStatusConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        context: Optional[_builtins.str] = ...,
        target_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetUrl")
    def target_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectSecondarySourceGitSubmodulesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, fetch_submodules: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fetchSubmodules")
    def fetch_submodules(self) -> _builtins.bool: ...

@pulumi.output_type
class ProjectSecondarySourceVersion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, source_identifier: _builtins.str, source_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> _builtins.str: ...

@pulumi.output_type
class ProjectSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        auth: Optional[outputs.ProjectSourceAuth] = ...,
        build_status_config: Optional[outputs.ProjectSourceBuildStatusConfig] = ...,
        buildspec: Optional[_builtins.str] = ...,
        git_clone_depth: Optional[_builtins.int] = ...,
        git_submodules_config: Optional[outputs.ProjectSourceGitSubmodulesConfig] = ...,
        insecure_ssl: Optional[_builtins.bool] = ...,
        location: Optional[_builtins.str] = ...,
        report_build_status: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[outputs.ProjectSourceAuth]: ...
    @_builtins.property
    @pulumi.getter(name="buildStatusConfig")
    def build_status_config(
        self,
    ) -> Optional[outputs.ProjectSourceBuildStatusConfig]: ...
    @_builtins.property
    @pulumi.getter
    def buildspec(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gitCloneDepth")
    def git_clone_depth(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="gitSubmodulesConfig")
    def git_submodules_config(
        self,
    ) -> Optional[outputs.ProjectSourceGitSubmodulesConfig]: ...
    @_builtins.property
    @pulumi.getter(name="insecureSsl")
    def insecure_ssl(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reportBuildStatus")
    def report_build_status(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ProjectSourceAuth(dict):
    def __init__(__self__, *, resource: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ProjectSourceBuildStatusConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        context: Optional[_builtins.str] = ...,
        target_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetUrl")
    def target_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectSourceGitSubmodulesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, fetch_submodules: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fetchSubmodules")
    def fetch_submodules(self) -> _builtins.bool: ...

@pulumi.output_type
class ProjectVpcConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
        vpc_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...

@pulumi.output_type
class ReportGroupExportConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        s3_destination: Optional[outputs.ReportGroupExportConfigS3Destination] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(
        self,
    ) -> Optional[outputs.ReportGroupExportConfigS3Destination]: ...

@pulumi.output_type
class ReportGroupExportConfigS3Destination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        encryption_key: _builtins.str,
        encryption_disabled: Optional[_builtins.bool] = ...,
        packaging: Optional[_builtins.str] = ...,
        path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def packaging(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WebhookFilterGroup(dict):
    def __init__(
        __self__, *, filters: Optional[Sequence[outputs.WebhookFilterGroupFilter]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.WebhookFilterGroupFilter]]: ...

@pulumi.output_type
class WebhookFilterGroupFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        pattern: _builtins.str,
        type: _builtins.str,
        exclude_matched_pattern: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="excludeMatchedPattern")
    def exclude_matched_pattern(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class WebhookPullRequestBuildPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        requires_comment_approval: _builtins.str,
        approver_roles: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiresCommentApproval")
    def requires_comment_approval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="approverRoles")
    def approver_roles(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class WebhookScopeConfiguration(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        scope: _builtins.str,
        domain: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetFleetComputeConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        disk: _builtins.int,
        instance_type: _builtins.str,
        machine_type: _builtins.str,
        memory: _builtins.int,
        vcpu: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disk(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def vcpu(self) -> _builtins.int: ...

@pulumi.output_type
class GetFleetScalingConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        desired_capacity: _builtins.int,
        max_capacity: _builtins.int,
        scaling_type: _builtins.str,
        target_tracking_scaling_configs: Sequence[
            outputs.GetFleetScalingConfigurationTargetTrackingScalingConfigResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="scalingType")
    def scaling_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingScalingConfigs")
    def target_tracking_scaling_configs(
        self,
    ) -> Sequence[
        outputs.GetFleetScalingConfigurationTargetTrackingScalingConfigResult
    ]: ...

@pulumi.output_type
class GetFleetScalingConfigurationTargetTrackingScalingConfigResult(dict):
    def __init__(
        __self__, *, metric_type: _builtins.str, target_value: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricType")
    def metric_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.float: ...

@pulumi.output_type
class GetFleetStatusResult(dict):
    def __init__(
        __self__,
        *,
        context: _builtins.str,
        message: _builtins.str,
        status_code: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.str: ...

@pulumi.output_type
class GetFleetVpcConfigResult(dict):
    def __init__(
        __self__,
        *,
        security_group_ids: Sequence[_builtins.str],
        subnets: Sequence[_builtins.str],
        vpc_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str: ...
