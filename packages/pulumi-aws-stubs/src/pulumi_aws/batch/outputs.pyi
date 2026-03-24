import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ComputeEnvironmentComputeResources",
    "ComputeEnvironmentComputeResourcesEc2Configuration",
    "ComputeEnvironmentComputeResourcesLaunchTemplate",
    "ComputeEnvironmentEksConfiguration",
    "ComputeEnvironmentUpdatePolicy",
    "JobDefinitionEksProperties",
    "JobDefinitionEksPropertiesPodProperties",
    "JobDefinitionEksPropertiesPodPropertiesContainer",
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
    "JobDefinitionEksPropertiesPodPropertiesMetadata",
    "JobDefinitionEksPropertiesPodPropertiesVolume",
    ...,
    ...,
    ...,
    "JobDefinitionRetryStrategy",
    "JobDefinitionRetryStrategyEvaluateOnExit",
    "JobDefinitionTimeout",
    "JobQueueComputeEnvironmentOrder",
    "JobQueueJobStateTimeLimitAction",
    "JobQueueTimeouts",
    "SchedulingPolicyFairSharePolicy",
    "SchedulingPolicyFairSharePolicyShareDistribution",
    "GetComputeEnvironmentUpdatePolicyResult",
    "GetJobDefinitionEksPropertyResult",
    "GetJobDefinitionEksPropertyPodPropertyResult",
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
    "GetJobDefinitionEksPropertyPodPropertyVolumeResult",
    ...,
    ...,
    ...,
    "GetJobDefinitionNodePropertyResult",
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
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "GetJobDefinitionRetryStrategyResult",
    "GetJobDefinitionRetryStrategyEvaluateOnExitResult",
    "GetJobDefinitionTimeoutResult",
    "GetJobQueueComputeEnvironmentOrderResult",
    "GetJobQueueJobStateTimeLimitActionResult",
    "GetSchedulingPolicyFairSharePolicyResult",
    ...,
]

@pulumi.output_type
class ComputeEnvironmentComputeResources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_vcpus: _builtins.int,
        subnets: Sequence[_builtins.str],
        type: _builtins.str,
        allocation_strategy: Optional[_builtins.str] = ...,
        bid_percentage: Optional[_builtins.int] = ...,
        desired_vcpus: Optional[_builtins.int] = ...,
        ec2_configurations: Optional[
            Sequence[outputs.ComputeEnvironmentComputeResourcesEc2Configuration]
        ] = ...,
        ec2_key_pair: Optional[_builtins.str] = ...,
        image_id: Optional[_builtins.str] = ...,
        instance_role: Optional[_builtins.str] = ...,
        instance_types: Optional[Sequence[_builtins.str]] = ...,
        launch_template: Optional[
            outputs.ComputeEnvironmentComputeResourcesLaunchTemplate
        ] = ...,
        min_vcpus: Optional[_builtins.int] = ...,
        placement_group: Optional[_builtins.str] = ...,
        security_group_ids: Optional[Sequence[_builtins.str]] = ...,
        spot_iam_fleet_role: Optional[_builtins.str] = ...,
        tags: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxVcpus")
    def max_vcpus(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bidPercentage")
    def bid_percentage(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="desiredVcpus")
    def desired_vcpus(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="ec2Configurations")
    def ec2_configurations(
        self,
    ) -> Optional[
        Sequence[outputs.ComputeEnvironmentComputeResourcesEc2Configuration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ec2KeyPair")
    def ec2_key_pair(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceRole")
    def instance_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(
        self,
    ) -> Optional[outputs.ComputeEnvironmentComputeResourcesLaunchTemplate]: ...
    @_builtins.property
    @pulumi.getter(name="minVcpus")
    def min_vcpus(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="spotIamFleetRole")
    def spot_iam_fleet_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ComputeEnvironmentComputeResourcesEc2Configuration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image_id_override: Optional[_builtins.str] = ...,
        image_kubernetes_version: Optional[_builtins.str] = ...,
        image_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageIdOverride")
    def image_id_override(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageKubernetesVersion")
    def image_kubernetes_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ComputeEnvironmentComputeResourcesLaunchTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        launch_template_id: Optional[_builtins.str] = ...,
        launch_template_name: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ComputeEnvironmentEksConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, eks_cluster_arn: _builtins.str, kubernetes_namespace: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eksClusterArn")
    def eks_cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kubernetesNamespace")
    def kubernetes_namespace(self) -> _builtins.str: ...

@pulumi.output_type
class ComputeEnvironmentUpdatePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        job_execution_timeout_minutes: Optional[_builtins.int] = ...,
        terminate_jobs_on_update: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobExecutionTimeoutMinutes")
    def job_execution_timeout_minutes(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="terminateJobsOnUpdate")
    def terminate_jobs_on_update(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class JobDefinitionEksProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, pod_properties: outputs.JobDefinitionEksPropertiesPodProperties
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podProperties")
    def pod_properties(self) -> outputs.JobDefinitionEksPropertiesPodProperties: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        containers: Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesContainer],
        dns_policy: Optional[_builtins.str] = ...,
        host_network: Optional[_builtins.bool] = ...,
        image_pull_secrets: Optional[
            Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesImagePullSecret]
        ] = ...,
        init_containers: Optional[
            Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesInitContainer]
        ] = ...,
        metadata: Optional[
            outputs.JobDefinitionEksPropertiesPodPropertiesMetadata
        ] = ...,
        service_account_name: Optional[_builtins.str] = ...,
        share_process_namespace: Optional[_builtins.bool] = ...,
        volumes: Optional[
            Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesVolume]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesContainer]: ...
    @_builtins.property
    @pulumi.getter(name="dnsPolicy")
    def dns_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="hostNetwork")
    def host_network(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="imagePullSecrets")
    def image_pull_secrets(
        self,
    ) -> Optional[
        Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesImagePullSecret]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(
        self,
    ) -> Optional[
        Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesInitContainer]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[outputs.JobDefinitionEksPropertiesPodPropertiesMetadata]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareProcessNamespace")
    def share_process_namespace(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesVolume]]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesContainer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        commands: Optional[Sequence[_builtins.str]] = ...,
        envs: Optional[
            Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesContainerEnv]
        ] = ...,
        image_pull_policy: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        resources: Optional[
            outputs.JobDefinitionEksPropertiesPodPropertiesContainerResources
        ] = ...,
        security_context: Optional[
            outputs.JobDefinitionEksPropertiesPodPropertiesContainerSecurityContext
        ] = ...,
        volume_mounts: Optional[
            Sequence[
                outputs.JobDefinitionEksPropertiesPodPropertiesContainerVolumeMount
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[
        Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesContainerEnv]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="imagePullPolicy")
    def image_pull_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[
        outputs.JobDefinitionEksPropertiesPodPropertiesContainerResources
    ]: ...
    @_builtins.property
    @pulumi.getter(name="securityContext")
    def security_context(
        self,
    ) -> Optional[
        outputs.JobDefinitionEksPropertiesPodPropertiesContainerSecurityContext
    ]: ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[
        Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesContainerVolumeMount]
    ]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesContainerEnv(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesContainerResources(dict):
    def __init__(
        __self__,
        *,
        limits: Optional[Mapping[str, _builtins.str]] = ...,
        requests: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesContainerSecurityContext(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_privilege_escalation: Optional[_builtins.bool] = ...,
        privileged: Optional[_builtins.bool] = ...,
        read_only_root_file_system: Optional[_builtins.bool] = ...,
        run_as_group: Optional[_builtins.int] = ...,
        run_as_non_root: Optional[_builtins.bool] = ...,
        run_as_user: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPrivilegeEscalation")
    def allow_privilege_escalation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def privileged(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="readOnlyRootFileSystem")
    def read_only_root_file_system(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runAsGroup")
    def run_as_group(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="runAsNonRoot")
    def run_as_non_root(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesContainerVolumeMount(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mount_path: _builtins.str,
        name: _builtins.str,
        read_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesImagePullSecret(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesInitContainer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        commands: Optional[Sequence[_builtins.str]] = ...,
        envs: Optional[
            Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesInitContainerEnv]
        ] = ...,
        image_pull_policy: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        resources: Optional[
            outputs.JobDefinitionEksPropertiesPodPropertiesInitContainerResources
        ] = ...,
        security_context: Optional[
            outputs.JobDefinitionEksPropertiesPodPropertiesInitContainerSecurityContext
        ] = ...,
        volume_mounts: Optional[
            Sequence[
                outputs.JobDefinitionEksPropertiesPodPropertiesInitContainerVolumeMount
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[
        Sequence[outputs.JobDefinitionEksPropertiesPodPropertiesInitContainerEnv]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="imagePullPolicy")
    def image_pull_policy(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[
        outputs.JobDefinitionEksPropertiesPodPropertiesInitContainerResources
    ]: ...
    @_builtins.property
    @pulumi.getter(name="securityContext")
    def security_context(
        self,
    ) -> Optional[
        outputs.JobDefinitionEksPropertiesPodPropertiesInitContainerSecurityContext
    ]: ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[
        Sequence[
            outputs.JobDefinitionEksPropertiesPodPropertiesInitContainerVolumeMount
        ]
    ]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesInitContainerEnv(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesInitContainerResources(dict):
    def __init__(
        __self__,
        *,
        limits: Optional[Mapping[str, _builtins.str]] = ...,
        requests: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesInitContainerSecurityContext(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_privilege_escalation: Optional[_builtins.bool] = ...,
        privileged: Optional[_builtins.bool] = ...,
        read_only_root_file_system: Optional[_builtins.bool] = ...,
        run_as_group: Optional[_builtins.int] = ...,
        run_as_non_root: Optional[_builtins.bool] = ...,
        run_as_user: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPrivilegeEscalation")
    def allow_privilege_escalation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def privileged(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="readOnlyRootFileSystem")
    def read_only_root_file_system(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runAsGroup")
    def run_as_group(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="runAsNonRoot")
    def run_as_non_root(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesInitContainerVolumeMount(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mount_path: _builtins.str,
        name: _builtins.str,
        read_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesMetadata(dict):
    def __init__(
        __self__, *, labels: Optional[Mapping[str, _builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesVolume(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        empty_dir: Optional[
            outputs.JobDefinitionEksPropertiesPodPropertiesVolumeEmptyDir
        ] = ...,
        host_path: Optional[
            outputs.JobDefinitionEksPropertiesPodPropertiesVolumeHostPath
        ] = ...,
        name: Optional[_builtins.str] = ...,
        secret: Optional[
            outputs.JobDefinitionEksPropertiesPodPropertiesVolumeSecret
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(
        self,
    ) -> Optional[outputs.JobDefinitionEksPropertiesPodPropertiesVolumeEmptyDir]: ...
    @_builtins.property
    @pulumi.getter(name="hostPath")
    def host_path(
        self,
    ) -> Optional[outputs.JobDefinitionEksPropertiesPodPropertiesVolumeHostPath]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def secret(
        self,
    ) -> Optional[outputs.JobDefinitionEksPropertiesPodPropertiesVolumeSecret]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesVolumeEmptyDir(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, size_limit: _builtins.str, medium: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesVolumeHostPath(dict):
    def __init__(__self__, *, path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...

@pulumi.output_type
class JobDefinitionEksPropertiesPodPropertiesVolumeSecret(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_name: _builtins.str,
        optional: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def optional(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class JobDefinitionRetryStrategy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attempts: Optional[_builtins.int] = ...,
        evaluate_on_exits: Optional[
            Sequence[outputs.JobDefinitionRetryStrategyEvaluateOnExit]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attempts(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="evaluateOnExits")
    def evaluate_on_exits(
        self,
    ) -> Optional[Sequence[outputs.JobDefinitionRetryStrategyEvaluateOnExit]]: ...

@pulumi.output_type
class JobDefinitionRetryStrategyEvaluateOnExit(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        on_exit_code: Optional[_builtins.str] = ...,
        on_reason: Optional[_builtins.str] = ...,
        on_status_reason: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onExitCode")
    def on_exit_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="onReason")
    def on_reason(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="onStatusReason")
    def on_status_reason(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class JobDefinitionTimeout(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, attempt_duration_seconds: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attemptDurationSeconds")
    def attempt_duration_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class JobQueueComputeEnvironmentOrder(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, compute_environment: _builtins.str, order: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeEnvironment")
    def compute_environment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.int: ...

@pulumi.output_type
class JobQueueJobStateTimeLimitAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        max_time_seconds: _builtins.int,
        reason: _builtins.str,
        state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxTimeSeconds")
    def max_time_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class JobQueueTimeouts(dict):
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
class SchedulingPolicyFairSharePolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        compute_reservation: Optional[_builtins.int] = ...,
        share_decay_seconds: Optional[_builtins.int] = ...,
        share_distributions: Optional[
            Sequence[outputs.SchedulingPolicyFairSharePolicyShareDistribution]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeReservation")
    def compute_reservation(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="shareDecaySeconds")
    def share_decay_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="shareDistributions")
    def share_distributions(
        self,
    ) -> Optional[
        Sequence[outputs.SchedulingPolicyFairSharePolicyShareDistribution]
    ]: ...

@pulumi.output_type
class SchedulingPolicyFairSharePolicyShareDistribution(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        share_identifier: _builtins.str,
        weight_factor: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shareIdentifier")
    def share_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weightFactor")
    def weight_factor(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class GetComputeEnvironmentUpdatePolicyResult(dict):
    def __init__(
        __self__,
        *,
        job_execution_timeout_minutes: _builtins.int,
        terminate_jobs_on_update: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobExecutionTimeoutMinutes")
    def job_execution_timeout_minutes(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="terminateJobsOnUpdate")
    def terminate_jobs_on_update(self) -> _builtins.bool: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyResult(dict):
    def __init__(
        __self__,
        *,
        pod_properties: Sequence[outputs.GetJobDefinitionEksPropertyPodPropertyResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="podProperties")
    def pod_properties(
        self,
    ) -> Sequence[outputs.GetJobDefinitionEksPropertyPodPropertyResult]: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyResult(dict):
    def __init__(
        __self__,
        *,
        containers: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyContainerResult
        ],
        dns_policy: _builtins.str,
        host_network: _builtins.bool,
        image_pull_secrets: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyImagePullSecretResult
        ],
        init_containers: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerResult
        ],
        metadatas: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyMetadataResult
        ],
        service_account_name: _builtins.str,
        share_process_namespace: _builtins.bool,
        volumes: Sequence[outputs.GetJobDefinitionEksPropertyPodPropertyVolumeResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Sequence[outputs.GetJobDefinitionEksPropertyPodPropertyContainerResult]: ...
    @_builtins.property
    @pulumi.getter(name="dnsPolicy")
    def dns_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostNetwork")
    def host_network(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="imagePullSecrets")
    def image_pull_secrets(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyImagePullSecretResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def metadatas(
        self,
    ) -> Sequence[outputs.GetJobDefinitionEksPropertyPodPropertyMetadataResult]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="shareProcessNamespace")
    def share_process_namespace(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Sequence[outputs.GetJobDefinitionEksPropertyPodPropertyVolumeResult]: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyContainerResult(dict):
    def __init__(
        __self__,
        *,
        args: Sequence[_builtins.str],
        commands: Sequence[_builtins.str],
        envs: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyContainerEnvResult
        ],
        image: _builtins.str,
        image_pull_policy: _builtins.str,
        name: _builtins.str,
        resources: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyContainerResourceResult
        ],
        security_contexts: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyContainerSecurityContextResult
        ],
        volume_mounts: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyContainerVolumeMountResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Sequence[outputs.GetJobDefinitionEksPropertyPodPropertyContainerEnvResult]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagePullPolicy")
    def image_pull_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyContainerResourceResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="securityContexts")
    def security_contexts(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyContainerSecurityContextResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyContainerVolumeMountResult
    ]: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyContainerEnvResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyContainerResourceResult(dict):
    def __init__(
        __self__,
        *,
        limits: Mapping[str, _builtins.str],
        requests: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyContainerSecurityContextResult(dict):
    def __init__(
        __self__,
        *,
        allow_privilege_escalation: _builtins.bool,
        privileged: _builtins.bool,
        read_only_root_file_system: _builtins.bool,
        run_as_group: _builtins.int,
        run_as_non_root: _builtins.bool,
        run_as_user: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPrivilegeEscalation")
    def allow_privilege_escalation(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def privileged(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="readOnlyRootFileSystem")
    def read_only_root_file_system(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="runAsGroup")
    def run_as_group(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="runAsNonRoot")
    def run_as_non_root(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> _builtins.int: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyContainerVolumeMountResult(dict):
    def __init__(
        __self__,
        *,
        mount_path: _builtins.str,
        name: _builtins.str,
        read_only: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyImagePullSecretResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyInitContainerResult(dict):
    def __init__(
        __self__,
        *,
        args: Sequence[_builtins.str],
        commands: Sequence[_builtins.str],
        envs: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerEnvResult
        ],
        image: _builtins.str,
        image_pull_policy: _builtins.str,
        name: _builtins.str,
        resources: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerResourceResult
        ],
        security_contexts: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerSecurityContextResult
        ],
        volume_mounts: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerVolumeMountResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerEnvResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imagePullPolicy")
    def image_pull_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerResourceResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="securityContexts")
    def security_contexts(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerSecurityContextResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyInitContainerVolumeMountResult
    ]: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyInitContainerEnvResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyInitContainerResourceResult(dict):
    def __init__(
        __self__,
        *,
        limits: Mapping[str, _builtins.str],
        requests: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyInitContainerSecurityContextResult(dict):
    def __init__(
        __self__,
        *,
        allow_privilege_escalation: _builtins.bool,
        privileged: _builtins.bool,
        read_only_root_file_system: _builtins.bool,
        run_as_group: _builtins.int,
        run_as_non_root: _builtins.bool,
        run_as_user: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPrivilegeEscalation")
    def allow_privilege_escalation(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def privileged(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="readOnlyRootFileSystem")
    def read_only_root_file_system(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="runAsGroup")
    def run_as_group(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="runAsNonRoot")
    def run_as_non_root(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> _builtins.int: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyInitContainerVolumeMountResult(dict):
    def __init__(
        __self__,
        *,
        mount_path: _builtins.str,
        name: _builtins.str,
        read_only: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyMetadataResult(dict):
    def __init__(__self__, *, labels: Mapping[str, _builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyVolumeResult(dict):
    def __init__(
        __self__,
        *,
        empty_dirs: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyVolumeEmptyDirResult
        ],
        host_paths: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyVolumeHostPathResult
        ],
        name: _builtins.str,
        secrets: Sequence[
            outputs.GetJobDefinitionEksPropertyPodPropertyVolumeSecretResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emptyDirs")
    def empty_dirs(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyVolumeEmptyDirResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="hostPaths")
    def host_paths(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionEksPropertyPodPropertyVolumeHostPathResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def secrets(
        self,
    ) -> Sequence[outputs.GetJobDefinitionEksPropertyPodPropertyVolumeSecretResult]: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyVolumeEmptyDirResult(dict):
    def __init__(
        __self__, *, medium: _builtins.str, size_limit: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyVolumeHostPathResult(dict):
    def __init__(__self__, *, path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionEksPropertyPodPropertyVolumeSecretResult(dict):
    def __init__(
        __self__, *, optional: _builtins.bool, secret_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def optional(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyResult(dict):
    def __init__(
        __self__,
        *,
        main_node: _builtins.int,
        node_range_properties: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyResult
        ],
        num_nodes: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mainNode")
    def main_node(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="nodeRangeProperties")
    def node_range_properties(
        self,
    ) -> Sequence[outputs.GetJobDefinitionNodePropertyNodeRangePropertyResult]: ...
    @_builtins.property
    @pulumi.getter(name="numNodes")
    def num_nodes(self) -> _builtins.int: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyResult(dict):
    def __init__(
        __self__,
        *,
        containers: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerResult
        ],
        target_nodes: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="targetNodes")
    def target_nodes(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerResult(dict):
    def __init__(
        __self__,
        *,
        commands: Sequence[_builtins.str],
        environments: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerEnvironmentResult
        ],
        ephemeral_storages: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerEphemeralStorageResult
        ],
        execution_role_arn: _builtins.str,
        fargate_platform_configurations: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerFargatePlatformConfigurationResult
        ],
        image: _builtins.str,
        instance_type: _builtins.str,
        job_role_arn: _builtins.str,
        linux_parameters: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLinuxParameterResult
        ],
        log_configurations: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLogConfigurationResult
        ],
        mount_points: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerMountPointResult
        ],
        network_configurations: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerNetworkConfigurationResult
        ],
        privileged: _builtins.bool,
        readonly_root_filesystem: _builtins.bool,
        resource_requirements: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerResourceRequirementResult
        ],
        runtime_platforms: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerRuntimePlatformResult
        ],
        secrets: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerSecretResult
        ],
        ulimits: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerUlimitResult
        ],
        user: _builtins.str,
        volumes: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def environments(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerEnvironmentResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorages")
    def ephemeral_storages(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerEphemeralStorageResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fargatePlatformConfigurations")
    def fargate_platform_configurations(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerFargatePlatformConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="jobRoleArn")
    def job_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linuxParameters")
    def linux_parameters(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLinuxParameterResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="logConfigurations")
    def log_configurations(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLogConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mountPoints")
    def mount_points(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerMountPointResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigurations")
    def network_configurations(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerNetworkConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def privileged(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="readonlyRootFilesystem")
    def readonly_root_filesystem(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="resourceRequirements")
    def resource_requirements(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerResourceRequirementResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="runtimePlatforms")
    def runtime_platforms(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerRuntimePlatformResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def secrets(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerSecretResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def ulimits(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerUlimitResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def user(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeResult
    ]: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerEnvironmentResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerEphemeralStorageResult(
    dict
):
    def __init__(__self__, *, size_in_gib: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeInGib")
    def size_in_gib(self) -> _builtins.int: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerFargatePlatformConfigurationResult(
    dict
):
    def __init__(__self__, *, platform_version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerLinuxParameterResult(dict):
    def __init__(
        __self__,
        *,
        devices: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLinuxParameterDeviceResult
        ],
        init_process_enabled: _builtins.bool,
        max_swap: _builtins.int,
        shared_memory_size: _builtins.int,
        swappiness: _builtins.int,
        tmpfs: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLinuxParameterTmpfResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def devices(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLinuxParameterDeviceResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="initProcessEnabled")
    def init_process_enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="maxSwap")
    def max_swap(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sharedMemorySize")
    def shared_memory_size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def swappiness(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def tmpfs(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLinuxParameterTmpfResult
    ]: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerLinuxParameterDeviceResult(
    dict
):
    def __init__(
        __self__,
        *,
        container_path: _builtins.str,
        host_path: _builtins.str,
        permissions: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPath")
    def container_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="hostPath")
    def host_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerLinuxParameterTmpfResult(
    dict
):
    def __init__(
        __self__,
        *,
        container_path: _builtins.str,
        mount_options: Sequence[_builtins.str],
        size: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPath")
    def container_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerLogConfigurationResult(
    dict
):
    def __init__(
        __self__,
        *,
        log_driver: _builtins.str,
        options: Mapping[str, _builtins.str],
        secret_options: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLogConfigurationSecretOptionResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logDriver")
    def log_driver(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretOptions")
    def secret_options(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerLogConfigurationSecretOptionResult
    ]: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerLogConfigurationSecretOptionResult(
    dict
):
    def __init__(
        __self__, *, name: _builtins.str, value_from: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="valueFrom")
    def value_from(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerMountPointResult(dict):
    def __init__(
        __self__,
        *,
        container_path: _builtins.str,
        read_only: _builtins.bool,
        source_volume: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPath")
    def container_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="sourceVolume")
    def source_volume(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerNetworkConfigurationResult(
    dict
):
    def __init__(__self__, *, assign_public_ip: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assignPublicIp")
    def assign_public_ip(self) -> _builtins.bool: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerResourceRequirementResult(
    dict
):
    def __init__(__self__, *, type: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerRuntimePlatformResult(dict):
    def __init__(
        __self__,
        *,
        cpu_architecture: _builtins.str,
        operating_system_family: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuArchitecture")
    def cpu_architecture(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="operatingSystemFamily")
    def operating_system_family(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerSecretResult(dict):
    def __init__(
        __self__, *, name: _builtins.str, value_from: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="valueFrom")
    def value_from(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerUlimitResult(dict):
    def __init__(
        __self__,
        *,
        hard_limit: _builtins.int,
        name: _builtins.str,
        soft_limit: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="hardLimit")
    def hard_limit(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="softLimit")
    def soft_limit(self) -> _builtins.int: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeResult(dict):
    def __init__(
        __self__,
        *,
        efs_volume_configurations: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeEfsVolumeConfigurationResult
        ],
        hosts: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeHostResult
        ],
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="efsVolumeConfigurations")
    def efs_volume_configurations(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeEfsVolumeConfigurationResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def hosts(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeHostResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeEfsVolumeConfigurationResult(
    dict
):
    def __init__(
        __self__,
        *,
        authorization_configs: Sequence[
            outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeEfsVolumeConfigurationAuthorizationConfigResult
        ],
        file_system_id: _builtins.str,
        root_directory: _builtins.str,
        transit_encryption: _builtins.str,
        transit_encryption_port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="authorizationConfigs")
    def authorization_configs(
        self,
    ) -> Sequence[
        outputs.GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeEfsVolumeConfigurationAuthorizationConfigResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitEncryption")
    def transit_encryption(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="transitEncryptionPort")
    def transit_encryption_port(self) -> _builtins.int: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeEfsVolumeConfigurationAuthorizationConfigResult(
    dict
):
    def __init__(
        __self__, *, access_point_id: _builtins.str, iam: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessPointId")
    def access_point_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def iam(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionNodePropertyNodeRangePropertyContainerVolumeHostResult(dict):
    def __init__(__self__, *, source_path: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourcePath")
    def source_path(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionRetryStrategyResult(dict):
    def __init__(
        __self__,
        *,
        attempts: _builtins.int,
        evaluate_on_exits: Sequence[
            outputs.GetJobDefinitionRetryStrategyEvaluateOnExitResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attempts(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="evaluateOnExits")
    def evaluate_on_exits(
        self,
    ) -> Sequence[outputs.GetJobDefinitionRetryStrategyEvaluateOnExitResult]: ...

@pulumi.output_type
class GetJobDefinitionRetryStrategyEvaluateOnExitResult(dict):
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        on_exit_code: _builtins.str,
        on_reason: _builtins.str,
        on_status_reason: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onExitCode")
    def on_exit_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onReason")
    def on_reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onStatusReason")
    def on_status_reason(self) -> _builtins.str: ...

@pulumi.output_type
class GetJobDefinitionTimeoutResult(dict):
    def __init__(__self__, *, attempt_duration_seconds: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attemptDurationSeconds")
    def attempt_duration_seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetJobQueueComputeEnvironmentOrderResult(dict):
    def __init__(
        __self__, *, compute_environment: _builtins.str, order: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeEnvironment")
    def compute_environment(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> _builtins.int: ...

@pulumi.output_type
class GetJobQueueJobStateTimeLimitActionResult(dict):
    def __init__(
        __self__,
        *,
        action: _builtins.str,
        max_time_seconds: _builtins.int,
        reason: _builtins.str,
        state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxTimeSeconds")
    def max_time_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetSchedulingPolicyFairSharePolicyResult(dict):
    def __init__(
        __self__,
        *,
        compute_reservation: _builtins.int,
        share_decay_seconds: _builtins.int,
        share_distributions: Sequence[
            outputs.GetSchedulingPolicyFairSharePolicyShareDistributionResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="computeReservation")
    def compute_reservation(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="shareDecaySeconds")
    def share_decay_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="shareDistributions")
    def share_distributions(
        self,
    ) -> Sequence[
        outputs.GetSchedulingPolicyFairSharePolicyShareDistributionResult
    ]: ...

@pulumi.output_type
class GetSchedulingPolicyFairSharePolicyShareDistributionResult(dict):
    def __init__(
        __self__, *, share_identifier: _builtins.str, weight_factor: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shareIdentifier")
    def share_identifier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weightFactor")
    def weight_factor(self) -> _builtins.float: ...
