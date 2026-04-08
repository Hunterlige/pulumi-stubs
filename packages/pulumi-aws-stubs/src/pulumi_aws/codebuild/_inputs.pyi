import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FleetComputeConfigurationArgs",
    "FleetComputeConfigurationArgsDict",
    "FleetScalingConfigurationArgs",
    "FleetScalingConfigurationArgsDict",
    ...,
    ...,
    "FleetStatusArgs",
    "FleetStatusArgsDict",
    "FleetVpcConfigArgs",
    "FleetVpcConfigArgsDict",
    "ProjectArtifactsArgs",
    "ProjectArtifactsArgsDict",
    "ProjectBuildBatchConfigArgs",
    "ProjectBuildBatchConfigArgsDict",
    "ProjectBuildBatchConfigRestrictionsArgs",
    "ProjectBuildBatchConfigRestrictionsArgsDict",
    "ProjectCacheArgs",
    "ProjectCacheArgsDict",
    "ProjectEnvironmentArgs",
    "ProjectEnvironmentArgsDict",
    "ProjectEnvironmentDockerServerArgs",
    "ProjectEnvironmentDockerServerArgsDict",
    "ProjectEnvironmentEnvironmentVariableArgs",
    "ProjectEnvironmentEnvironmentVariableArgsDict",
    "ProjectEnvironmentFleetArgs",
    "ProjectEnvironmentFleetArgsDict",
    "ProjectEnvironmentRegistryCredentialArgs",
    "ProjectEnvironmentRegistryCredentialArgsDict",
    "ProjectFileSystemLocationArgs",
    "ProjectFileSystemLocationArgsDict",
    "ProjectLogsConfigArgs",
    "ProjectLogsConfigArgsDict",
    "ProjectLogsConfigCloudwatchLogsArgs",
    "ProjectLogsConfigCloudwatchLogsArgsDict",
    "ProjectLogsConfigS3LogsArgs",
    "ProjectLogsConfigS3LogsArgsDict",
    "ProjectSecondaryArtifactArgs",
    "ProjectSecondaryArtifactArgsDict",
    "ProjectSecondarySourceArgs",
    "ProjectSecondarySourceArgsDict",
    "ProjectSecondarySourceAuthArgs",
    "ProjectSecondarySourceAuthArgsDict",
    "ProjectSecondarySourceBuildStatusConfigArgs",
    "ProjectSecondarySourceBuildStatusConfigArgsDict",
    "ProjectSecondarySourceGitSubmodulesConfigArgs",
    "ProjectSecondarySourceGitSubmodulesConfigArgsDict",
    "ProjectSecondarySourceVersionArgs",
    "ProjectSecondarySourceVersionArgsDict",
    "ProjectSourceArgs",
    "ProjectSourceArgsDict",
    "ProjectSourceAuthArgs",
    "ProjectSourceAuthArgsDict",
    "ProjectSourceBuildStatusConfigArgs",
    "ProjectSourceBuildStatusConfigArgsDict",
    "ProjectSourceGitSubmodulesConfigArgs",
    "ProjectSourceGitSubmodulesConfigArgsDict",
    "ProjectVpcConfigArgs",
    "ProjectVpcConfigArgsDict",
    "ReportGroupExportConfigArgs",
    "ReportGroupExportConfigArgsDict",
    "ReportGroupExportConfigS3DestinationArgs",
    "ReportGroupExportConfigS3DestinationArgsDict",
    "WebhookFilterGroupArgs",
    "WebhookFilterGroupArgsDict",
    "WebhookFilterGroupFilterArgs",
    "WebhookFilterGroupFilterArgsDict",
    "WebhookPullRequestBuildPolicyArgs",
    "WebhookPullRequestBuildPolicyArgsDict",
    "WebhookScopeConfigurationArgs",
    "WebhookScopeConfigurationArgsDict",
]

class FleetComputeConfigurationArgsDict(TypedDict):
    disk: NotRequired[pulumi.Input[_builtins.int]]
    instance_type: NotRequired[pulumi.Input[_builtins.str]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    memory: NotRequired[pulumi.Input[_builtins.int]]
    vcpu: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FleetComputeConfigurationArgs:
    def __init__(
        __self__,
        *,
        disk: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_type: Optional[pulumi.Input[_builtins.str]] = ...,
        machine_type: Optional[pulumi.Input[_builtins.str]] = ...,
        memory: Optional[pulumi.Input[_builtins.int]] = ...,
        vcpu: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disk(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @disk.setter
    def disk(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def vcpu(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @vcpu.setter
    def vcpu(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class FleetScalingConfigurationArgsDict(TypedDict):
    desired_capacity: NotRequired[pulumi.Input[_builtins.int]]
    max_capacity: NotRequired[pulumi.Input[_builtins.int]]
    scaling_type: NotRequired[pulumi.Input[_builtins.str]]
    target_tracking_scaling_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    FleetScalingConfigurationTargetTrackingScalingConfigArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class FleetScalingConfigurationArgs:
    def __init__(
        __self__,
        *,
        desired_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        max_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        scaling_type: Optional[pulumi.Input[_builtins.str]] = ...,
        target_tracking_scaling_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FleetScalingConfigurationTargetTrackingScalingConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @desired_capacity.setter
    def desired_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingType")
    def scaling_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scaling_type.setter
    def scaling_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingScalingConfigs")
    def target_tracking_scaling_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[FleetScalingConfigurationTargetTrackingScalingConfigArgs]
            ]
        ]
    ]: ...
    @target_tracking_scaling_configs.setter
    def target_tracking_scaling_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        FleetScalingConfigurationTargetTrackingScalingConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class FleetScalingConfigurationTargetTrackingScalingConfigArgsDict(TypedDict):
    metric_type: NotRequired[pulumi.Input[_builtins.str]]
    target_value: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class FleetScalingConfigurationTargetTrackingScalingConfigArgs:
    def __init__(
        __self__,
        *,
        metric_type: Optional[pulumi.Input[_builtins.str]] = ...,
        target_value: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricType")
    def metric_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @metric_type.setter
    def metric_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @target_value.setter
    def target_value(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class FleetStatusArgsDict(TypedDict):
    context: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    status_code: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FleetStatusArgs:
    def __init__(
        __self__,
        *,
        context: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        status_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FleetVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class FleetVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...

class ProjectArtifactsArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    artifact_identifier: NotRequired[pulumi.Input[_builtins.str]]
    bucket_owner_access: NotRequired[pulumi.Input[_builtins.str]]
    encryption_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    namespace_type: NotRequired[pulumi.Input[_builtins.str]]
    override_artifact_name: NotRequired[pulumi.Input[_builtins.bool]]
    packaging: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectArtifactsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        artifact_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_owner_access: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace_type: Optional[pulumi.Input[_builtins.str]] = ...,
        override_artifact_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        packaging: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="artifactIdentifier")
    def artifact_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @artifact_identifier.setter
    def artifact_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccess")
    def bucket_owner_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_owner_access.setter
    def bucket_owner_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encryption_disabled.setter
    def encryption_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace_type.setter
    def namespace_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overrideArtifactName")
    def override_artifact_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @override_artifact_name.setter
    def override_artifact_name(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def packaging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @packaging.setter
    def packaging(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectBuildBatchConfigArgsDict(TypedDict):
    service_role: pulumi.Input[_builtins.str]
    combine_artifacts: NotRequired[pulumi.Input[_builtins.bool]]
    restrictions: NotRequired[pulumi.Input[ProjectBuildBatchConfigRestrictionsArgsDict]]
    timeout_in_mins: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ProjectBuildBatchConfigArgs:
    def __init__(
        __self__,
        *,
        service_role: pulumi.Input[_builtins.str],
        combine_artifacts: Optional[pulumi.Input[_builtins.bool]] = ...,
        restrictions: Optional[
            pulumi.Input[ProjectBuildBatchConfigRestrictionsArgs]
        ] = ...,
        timeout_in_mins: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Input[_builtins.str]: ...
    @service_role.setter
    def service_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="combineArtifacts")
    def combine_artifacts(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @combine_artifacts.setter
    def combine_artifacts(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def restrictions(
        self,
    ) -> Optional[pulumi.Input[ProjectBuildBatchConfigRestrictionsArgs]]: ...
    @restrictions.setter
    def restrictions(
        self, value: Optional[pulumi.Input[ProjectBuildBatchConfigRestrictionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutInMins")
    def timeout_in_mins(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_in_mins.setter
    def timeout_in_mins(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ProjectBuildBatchConfigRestrictionsArgsDict(TypedDict):
    compute_types_alloweds: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    maximum_builds_allowed: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ProjectBuildBatchConfigRestrictionsArgs:
    def __init__(
        __self__,
        *,
        compute_types_alloweds: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        maximum_builds_allowed: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeTypesAlloweds")
    def compute_types_alloweds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @compute_types_alloweds.setter
    def compute_types_alloweds(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maximumBuildsAllowed")
    def maximum_builds_allowed(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_builds_allowed.setter
    def maximum_builds_allowed(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ProjectCacheArgsDict(TypedDict):
    cache_namespace: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    modes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectCacheArgs:
    def __init__(
        __self__,
        *,
        cache_namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        modes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cacheNamespace")
    def cache_namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cache_namespace.setter
    def cache_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def modes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @modes.setter
    def modes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectEnvironmentArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    image: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    certificate: NotRequired[pulumi.Input[_builtins.str]]
    docker_server: NotRequired[pulumi.Input[ProjectEnvironmentDockerServerArgsDict]]
    environment_variables: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ProjectEnvironmentEnvironmentVariableArgsDict]]
        ]
    ]
    fleet: NotRequired[pulumi.Input[ProjectEnvironmentFleetArgsDict]]
    image_pull_credentials_type: NotRequired[pulumi.Input[_builtins.str]]
    privileged_mode: NotRequired[pulumi.Input[_builtins.bool]]
    registry_credential: NotRequired[
        pulumi.Input[ProjectEnvironmentRegistryCredentialArgsDict]
    ]

@pulumi.input_type
class ProjectEnvironmentArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        image: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        docker_server: Optional[pulumi.Input[ProjectEnvironmentDockerServerArgs]] = ...,
        environment_variables: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ProjectEnvironmentEnvironmentVariableArgs]]
            ]
        ] = ...,
        fleet: Optional[pulumi.Input[ProjectEnvironmentFleetArgs]] = ...,
        image_pull_credentials_type: Optional[pulumi.Input[_builtins.str]] = ...,
        privileged_mode: Optional[pulumi.Input[_builtins.bool]] = ...,
        registry_credential: Optional[
            pulumi.Input[ProjectEnvironmentRegistryCredentialArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]: ...
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dockerServer")
    def docker_server(
        self,
    ) -> Optional[pulumi.Input[ProjectEnvironmentDockerServerArgs]]: ...
    @docker_server.setter
    def docker_server(
        self, value: Optional[pulumi.Input[ProjectEnvironmentDockerServerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ProjectEnvironmentEnvironmentVariableArgs]]]
    ]: ...
    @environment_variables.setter
    def environment_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ProjectEnvironmentEnvironmentVariableArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def fleet(self) -> Optional[pulumi.Input[ProjectEnvironmentFleetArgs]]: ...
    @fleet.setter
    def fleet(self, value: Optional[pulumi.Input[ProjectEnvironmentFleetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="imagePullCredentialsType")
    def image_pull_credentials_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_pull_credentials_type.setter
    def image_pull_credentials_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privilegedMode")
    def privileged_mode(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @privileged_mode.setter
    def privileged_mode(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="registryCredential")
    def registry_credential(
        self,
    ) -> Optional[pulumi.Input[ProjectEnvironmentRegistryCredentialArgs]]: ...
    @registry_credential.setter
    def registry_credential(
        self, value: Optional[pulumi.Input[ProjectEnvironmentRegistryCredentialArgs]]
    ): ...

class ProjectEnvironmentDockerServerArgsDict(TypedDict):
    compute_type: pulumi.Input[_builtins.str]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ProjectEnvironmentDockerServerArgs:
    def __init__(
        __self__,
        *,
        compute_type: pulumi.Input[_builtins.str],
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[_builtins.str]: ...
    @compute_type.setter
    def compute_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ProjectEnvironmentEnvironmentVariableArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectEnvironmentEnvironmentVariableArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectEnvironmentFleetArgsDict(TypedDict):
    fleet_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectEnvironmentFleetArgs:
    def __init__(
        __self__, *, fleet_arn: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fleetArn")
    def fleet_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fleet_arn.setter
    def fleet_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectEnvironmentRegistryCredentialArgsDict(TypedDict):
    credential: pulumi.Input[_builtins.str]
    credential_provider: pulumi.Input[_builtins.str]

@pulumi.input_type
class ProjectEnvironmentRegistryCredentialArgs:
    def __init__(
        __self__,
        *,
        credential: pulumi.Input[_builtins.str],
        credential_provider: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def credential(self) -> pulumi.Input[_builtins.str]: ...
    @credential.setter
    def credential(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="credentialProvider")
    def credential_provider(self) -> pulumi.Input[_builtins.str]: ...
    @credential_provider.setter
    def credential_provider(self, value: pulumi.Input[_builtins.str]): ...

class ProjectFileSystemLocationArgsDict(TypedDict):
    identifier: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    mount_options: NotRequired[pulumi.Input[_builtins.str]]
    mount_point: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectFileSystemLocationArgs:
    def __init__(
        __self__,
        *,
        identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        mount_options: Optional[pulumi.Input[_builtins.str]] = ...,
        mount_point: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identifier.setter
    def identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mount_options.setter
    def mount_options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mount_point.setter
    def mount_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectLogsConfigArgsDict(TypedDict):
    cloudwatch_logs: NotRequired[pulumi.Input[ProjectLogsConfigCloudwatchLogsArgsDict]]
    s3_logs: NotRequired[pulumi.Input[ProjectLogsConfigS3LogsArgsDict]]

@pulumi.input_type
class ProjectLogsConfigArgs:
    def __init__(
        __self__,
        *,
        cloudwatch_logs: Optional[
            pulumi.Input[ProjectLogsConfigCloudwatchLogsArgs]
        ] = ...,
        s3_logs: Optional[pulumi.Input[ProjectLogsConfigS3LogsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudwatchLogs")
    def cloudwatch_logs(
        self,
    ) -> Optional[pulumi.Input[ProjectLogsConfigCloudwatchLogsArgs]]: ...
    @cloudwatch_logs.setter
    def cloudwatch_logs(
        self, value: Optional[pulumi.Input[ProjectLogsConfigCloudwatchLogsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> Optional[pulumi.Input[ProjectLogsConfigS3LogsArgs]]: ...
    @s3_logs.setter
    def s3_logs(self, value: Optional[pulumi.Input[ProjectLogsConfigS3LogsArgs]]): ...

class ProjectLogsConfigCloudwatchLogsArgsDict(TypedDict):
    group_name: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    stream_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectLogsConfigCloudwatchLogsArgs:
    def __init__(
        __self__,
        *,
        group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        stream_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groupName")
    def group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @group_name.setter
    def group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="streamName")
    def stream_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @stream_name.setter
    def stream_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectLogsConfigS3LogsArgsDict(TypedDict):
    bucket_owner_access: NotRequired[pulumi.Input[_builtins.str]]
    encryption_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectLogsConfigS3LogsArgs:
    def __init__(
        __self__,
        *,
        bucket_owner_access: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccess")
    def bucket_owner_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_owner_access.setter
    def bucket_owner_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encryption_disabled.setter
    def encryption_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectSecondaryArtifactArgsDict(TypedDict):
    artifact_identifier: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    bucket_owner_access: NotRequired[pulumi.Input[_builtins.str]]
    encryption_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    namespace_type: NotRequired[pulumi.Input[_builtins.str]]
    override_artifact_name: NotRequired[pulumi.Input[_builtins.bool]]
    packaging: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectSecondaryArtifactArgs:
    def __init__(
        __self__,
        *,
        artifact_identifier: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        bucket_owner_access: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace_type: Optional[pulumi.Input[_builtins.str]] = ...,
        override_artifact_name: Optional[pulumi.Input[_builtins.bool]] = ...,
        packaging: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="artifactIdentifier")
    def artifact_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @artifact_identifier.setter
    def artifact_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bucketOwnerAccess")
    def bucket_owner_access(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_owner_access.setter
    def bucket_owner_access(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encryption_disabled.setter
    def encryption_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace_type.setter
    def namespace_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overrideArtifactName")
    def override_artifact_name(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @override_artifact_name.setter
    def override_artifact_name(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def packaging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @packaging.setter
    def packaging(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectSecondarySourceArgsDict(TypedDict):
    source_identifier: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    auth: NotRequired[pulumi.Input[ProjectSecondarySourceAuthArgsDict]]
    build_status_config: NotRequired[
        pulumi.Input[ProjectSecondarySourceBuildStatusConfigArgsDict]
    ]
    buildspec: NotRequired[pulumi.Input[_builtins.str]]
    git_clone_depth: NotRequired[pulumi.Input[_builtins.int]]
    git_submodules_config: NotRequired[
        pulumi.Input[ProjectSecondarySourceGitSubmodulesConfigArgsDict]
    ]
    insecure_ssl: NotRequired[pulumi.Input[_builtins.bool]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    report_build_status: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ProjectSecondarySourceArgs:
    def __init__(
        __self__,
        *,
        source_identifier: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        auth: Optional[pulumi.Input[ProjectSecondarySourceAuthArgs]] = ...,
        build_status_config: Optional[
            pulumi.Input[ProjectSecondarySourceBuildStatusConfigArgs]
        ] = ...,
        buildspec: Optional[pulumi.Input[_builtins.str]] = ...,
        git_clone_depth: Optional[pulumi.Input[_builtins.int]] = ...,
        git_submodules_config: Optional[
            pulumi.Input[ProjectSecondarySourceGitSubmodulesConfigArgs]
        ] = ...,
        insecure_ssl: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        report_build_status: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @source_identifier.setter
    def source_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[ProjectSecondarySourceAuthArgs]]: ...
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[ProjectSecondarySourceAuthArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="buildStatusConfig")
    def build_status_config(
        self,
    ) -> Optional[pulumi.Input[ProjectSecondarySourceBuildStatusConfigArgs]]: ...
    @build_status_config.setter
    def build_status_config(
        self, value: Optional[pulumi.Input[ProjectSecondarySourceBuildStatusConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def buildspec(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @buildspec.setter
    def buildspec(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitCloneDepth")
    def git_clone_depth(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @git_clone_depth.setter
    def git_clone_depth(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="gitSubmodulesConfig")
    def git_submodules_config(
        self,
    ) -> Optional[pulumi.Input[ProjectSecondarySourceGitSubmodulesConfigArgs]]: ...
    @git_submodules_config.setter
    def git_submodules_config(
        self,
        value: Optional[pulumi.Input[ProjectSecondarySourceGitSubmodulesConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="insecureSsl")
    def insecure_ssl(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @insecure_ssl.setter
    def insecure_ssl(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reportBuildStatus")
    def report_build_status(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @report_build_status.setter
    def report_build_status(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ProjectSecondarySourceAuthArgsDict(TypedDict):
    resource: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ProjectSecondarySourceAuthArgs:
    def __init__(
        __self__,
        *,
        resource: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[_builtins.str]: ...
    @resource.setter
    def resource(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ProjectSecondarySourceBuildStatusConfigArgsDict(TypedDict):
    context: NotRequired[pulumi.Input[_builtins.str]]
    target_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectSecondarySourceBuildStatusConfigArgs:
    def __init__(
        __self__,
        *,
        context: Optional[pulumi.Input[_builtins.str]] = ...,
        target_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetUrl")
    def target_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_url.setter
    def target_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectSecondarySourceGitSubmodulesConfigArgsDict(TypedDict):
    fetch_submodules: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ProjectSecondarySourceGitSubmodulesConfigArgs:
    def __init__(
        __self__, *, fetch_submodules: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fetchSubmodules")
    def fetch_submodules(self) -> pulumi.Input[_builtins.bool]: ...
    @fetch_submodules.setter
    def fetch_submodules(self, value: pulumi.Input[_builtins.bool]): ...

class ProjectSecondarySourceVersionArgsDict(TypedDict):
    source_identifier: pulumi.Input[_builtins.str]
    source_version: pulumi.Input[_builtins.str]

@pulumi.input_type
class ProjectSecondarySourceVersionArgs:
    def __init__(
        __self__,
        *,
        source_identifier: pulumi.Input[_builtins.str],
        source_version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceIdentifier")
    def source_identifier(self) -> pulumi.Input[_builtins.str]: ...
    @source_identifier.setter
    def source_identifier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceVersion")
    def source_version(self) -> pulumi.Input[_builtins.str]: ...
    @source_version.setter
    def source_version(self, value: pulumi.Input[_builtins.str]): ...

class ProjectSourceArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    auth: NotRequired[pulumi.Input[ProjectSourceAuthArgsDict]]
    build_status_config: NotRequired[
        pulumi.Input[ProjectSourceBuildStatusConfigArgsDict]
    ]
    buildspec: NotRequired[pulumi.Input[_builtins.str]]
    git_clone_depth: NotRequired[pulumi.Input[_builtins.int]]
    git_submodules_config: NotRequired[
        pulumi.Input[ProjectSourceGitSubmodulesConfigArgsDict]
    ]
    insecure_ssl: NotRequired[pulumi.Input[_builtins.bool]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    report_build_status: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ProjectSourceArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        auth: Optional[pulumi.Input[ProjectSourceAuthArgs]] = ...,
        build_status_config: Optional[
            pulumi.Input[ProjectSourceBuildStatusConfigArgs]
        ] = ...,
        buildspec: Optional[pulumi.Input[_builtins.str]] = ...,
        git_clone_depth: Optional[pulumi.Input[_builtins.int]] = ...,
        git_submodules_config: Optional[
            pulumi.Input[ProjectSourceGitSubmodulesConfigArgs]
        ] = ...,
        insecure_ssl: Optional[pulumi.Input[_builtins.bool]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        report_build_status: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[ProjectSourceAuthArgs]]: ...
    @auth.setter
    def auth(self, value: Optional[pulumi.Input[ProjectSourceAuthArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="buildStatusConfig")
    def build_status_config(
        self,
    ) -> Optional[pulumi.Input[ProjectSourceBuildStatusConfigArgs]]: ...
    @build_status_config.setter
    def build_status_config(
        self, value: Optional[pulumi.Input[ProjectSourceBuildStatusConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def buildspec(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @buildspec.setter
    def buildspec(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gitCloneDepth")
    def git_clone_depth(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @git_clone_depth.setter
    def git_clone_depth(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="gitSubmodulesConfig")
    def git_submodules_config(
        self,
    ) -> Optional[pulumi.Input[ProjectSourceGitSubmodulesConfigArgs]]: ...
    @git_submodules_config.setter
    def git_submodules_config(
        self, value: Optional[pulumi.Input[ProjectSourceGitSubmodulesConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="insecureSsl")
    def insecure_ssl(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @insecure_ssl.setter
    def insecure_ssl(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reportBuildStatus")
    def report_build_status(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @report_build_status.setter
    def report_build_status(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ProjectSourceAuthArgsDict(TypedDict):
    resource: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ProjectSourceAuthArgs:
    def __init__(
        __self__,
        *,
        resource: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> pulumi.Input[_builtins.str]: ...
    @resource.setter
    def resource(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ProjectSourceBuildStatusConfigArgsDict(TypedDict):
    context: NotRequired[pulumi.Input[_builtins.str]]
    target_url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ProjectSourceBuildStatusConfigArgs:
    def __init__(
        __self__,
        *,
        context: Optional[pulumi.Input[_builtins.str]] = ...,
        target_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context.setter
    def context(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetUrl")
    def target_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_url.setter
    def target_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProjectSourceGitSubmodulesConfigArgsDict(TypedDict):
    fetch_submodules: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ProjectSourceGitSubmodulesConfigArgs:
    def __init__(
        __self__, *, fetch_submodules: pulumi.Input[_builtins.bool]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fetchSubmodules")
    def fetch_submodules(self) -> pulumi.Input[_builtins.bool]: ...
    @fetch_submodules.setter
    def fetch_submodules(self, value: pulumi.Input[_builtins.bool]): ...

class ProjectVpcConfigArgsDict(TypedDict):
    security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ProjectVpcConfigArgs:
    def __init__(
        __self__,
        *,
        security_group_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...

class ReportGroupExportConfigArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    s3_destination: NotRequired[
        pulumi.Input[ReportGroupExportConfigS3DestinationArgsDict]
    ]

@pulumi.input_type
class ReportGroupExportConfigArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        s3_destination: Optional[
            pulumi.Input[ReportGroupExportConfigS3DestinationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(
        self,
    ) -> Optional[pulumi.Input[ReportGroupExportConfigS3DestinationArgs]]: ...
    @s3_destination.setter
    def s3_destination(
        self, value: Optional[pulumi.Input[ReportGroupExportConfigS3DestinationArgs]]
    ): ...

class ReportGroupExportConfigS3DestinationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    encryption_key: pulumi.Input[_builtins.str]
    encryption_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    packaging: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReportGroupExportConfigS3DestinationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        encryption_key: pulumi.Input[_builtins.str],
        encryption_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        packaging: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> pulumi.Input[_builtins.str]: ...
    @encryption_key.setter
    def encryption_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionDisabled")
    def encryption_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @encryption_disabled.setter
    def encryption_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def packaging(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @packaging.setter
    def packaging(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebhookFilterGroupArgsDict(TypedDict):
    filters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupFilterArgsDict]]]
    ]

@pulumi.input_type
class WebhookFilterGroupArgs:
    def __init__(
        __self__,
        *,
        filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupFilterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupFilterArgs]]]
    ]: ...
    @filters.setter
    def filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WebhookFilterGroupFilterArgs]]]
        ],
    ): ...

class WebhookFilterGroupFilterArgsDict(TypedDict):
    pattern: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    exclude_matched_pattern: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WebhookFilterGroupFilterArgs:
    def __init__(
        __self__,
        *,
        pattern: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        exclude_matched_pattern: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[_builtins.str]: ...
    @pattern.setter
    def pattern(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="excludeMatchedPattern")
    def exclude_matched_pattern(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @exclude_matched_pattern.setter
    def exclude_matched_pattern(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class WebhookPullRequestBuildPolicyArgsDict(TypedDict):
    requires_comment_approval: pulumi.Input[_builtins.str]
    approver_roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WebhookPullRequestBuildPolicyArgs:
    def __init__(
        __self__,
        *,
        requires_comment_approval: pulumi.Input[_builtins.str],
        approver_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiresCommentApproval")
    def requires_comment_approval(self) -> pulumi.Input[_builtins.str]: ...
    @requires_comment_approval.setter
    def requires_comment_approval(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="approverRoles")
    def approver_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @approver_roles.setter
    def approver_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WebhookScopeConfigurationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    scope: pulumi.Input[_builtins.str]
    domain: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WebhookScopeConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        scope: pulumi.Input[_builtins.str],
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
