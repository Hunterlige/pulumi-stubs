

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ComputeEnvironmentComputeResourcesArgs', 'ComputeEnvironmentComputeResourcesArgsDict', ..., ..., ..., ..., 'ComputeEnvironmentEksConfigurationArgs', 'ComputeEnvironmentEksConfigurationArgsDict', 'ComputeEnvironmentUpdatePolicyArgs', 'ComputeEnvironmentUpdatePolicyArgsDict', 'JobDefinitionEksPropertiesArgs', 'JobDefinitionEksPropertiesArgsDict', 'JobDefinitionEksPropertiesPodPropertiesArgs', 'JobDefinitionEksPropertiesPodPropertiesArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'JobDefinitionEksPropertiesPodPropertiesVolumeArgs', ..., ..., ..., ..., ..., ..., ..., 'JobDefinitionRetryStrategyArgs', 'JobDefinitionRetryStrategyArgsDict', 'JobDefinitionRetryStrategyEvaluateOnExitArgs', 'JobDefinitionRetryStrategyEvaluateOnExitArgsDict', 'JobDefinitionTimeoutArgs', 'JobDefinitionTimeoutArgsDict', 'JobQueueComputeEnvironmentOrderArgs', 'JobQueueComputeEnvironmentOrderArgsDict', 'JobQueueJobStateTimeLimitActionArgs', 'JobQueueJobStateTimeLimitActionArgsDict', 'JobQueueTimeoutsArgs', 'JobQueueTimeoutsArgsDict', 'SchedulingPolicyFairSharePolicyArgs', 'SchedulingPolicyFairSharePolicyArgsDict', ..., ...]
class ComputeEnvironmentComputeResourcesArgsDict(TypedDict):
    max_vcpus: pulumi.Input[_builtins.int]
    subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    type: pulumi.Input[_builtins.str]
    allocation_strategy: NotRequired[pulumi.Input[_builtins.str]]
    bid_percentage: NotRequired[pulumi.Input[_builtins.int]]
    desired_vcpus: NotRequired[pulumi.Input[_builtins.int]]
    ec2_configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input[ComputeEnvironmentComputeResourcesEc2ConfigurationArgsDict]]]]
    ec2_key_pair: NotRequired[pulumi.Input[_builtins.str]]
    image_id: NotRequired[pulumi.Input[_builtins.str]]
    instance_role: NotRequired[pulumi.Input[_builtins.str]]
    instance_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    launch_template: NotRequired[pulumi.Input[ComputeEnvironmentComputeResourcesLaunchTemplateArgsDict]]
    min_vcpus: NotRequired[pulumi.Input[_builtins.int]]
    placement_group: NotRequired[pulumi.Input[_builtins.str]]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    spot_iam_fleet_role: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ComputeEnvironmentComputeResourcesArgs:
    def __init__(__self__, *, max_vcpus: pulumi.Input[_builtins.int], subnets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], type: pulumi.Input[_builtins.str], allocation_strategy: Optional[pulumi.Input[_builtins.str]] = ..., bid_percentage: Optional[pulumi.Input[_builtins.int]] = ..., desired_vcpus: Optional[pulumi.Input[_builtins.int]] = ..., ec2_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[ComputeEnvironmentComputeResourcesEc2ConfigurationArgs]]]] = ..., ec2_key_pair: Optional[pulumi.Input[_builtins.str]] = ..., image_id: Optional[pulumi.Input[_builtins.str]] = ..., instance_role: Optional[pulumi.Input[_builtins.str]] = ..., instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., launch_template: Optional[pulumi.Input[ComputeEnvironmentComputeResourcesLaunchTemplateArgs]] = ..., min_vcpus: Optional[pulumi.Input[_builtins.int]] = ..., placement_group: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., spot_iam_fleet_role: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxVcpus")
    def max_vcpus(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_vcpus.setter
    def max_vcpus(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @allocation_strategy.setter
    def allocation_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bidPercentage")
    def bid_percentage(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @bid_percentage.setter
    def bid_percentage(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredVcpus")
    def desired_vcpus(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @desired_vcpus.setter
    def desired_vcpus(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2Configurations")
    def ec2_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ComputeEnvironmentComputeResourcesEc2ConfigurationArgs]]]]:
        
        ...
    
    @ec2_configurations.setter
    def ec2_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ComputeEnvironmentComputeResourcesEc2ConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ec2KeyPair")
    def ec2_key_pair(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ec2_key_pair.setter
    def ec2_key_pair(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageId")
    def image_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_id.setter
    def image_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceRole")
    def instance_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_role.setter
    def instance_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @instance_types.setter
    def instance_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplate")
    def launch_template(self) -> Optional[pulumi.Input[ComputeEnvironmentComputeResourcesLaunchTemplateArgs]]:
        
        ...
    
    @launch_template.setter
    def launch_template(self, value: Optional[pulumi.Input[ComputeEnvironmentComputeResourcesLaunchTemplateArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minVcpus")
    def min_vcpus(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @min_vcpus.setter
    def min_vcpus(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroup")
    def placement_group(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_group.setter
    def placement_group(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spotIamFleetRole")
    def spot_iam_fleet_role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @spot_iam_fleet_role.setter
    def spot_iam_fleet_role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ComputeEnvironmentComputeResourcesEc2ConfigurationArgsDict(TypedDict):
    image_id_override: NotRequired[pulumi.Input[_builtins.str]]
    image_kubernetes_version: NotRequired[pulumi.Input[_builtins.str]]
    image_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ComputeEnvironmentComputeResourcesEc2ConfigurationArgs:
    def __init__(__self__, *, image_id_override: Optional[pulumi.Input[_builtins.str]] = ..., image_kubernetes_version: Optional[pulumi.Input[_builtins.str]] = ..., image_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageIdOverride")
    def image_id_override(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_id_override.setter
    def image_id_override(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageKubernetesVersion")
    def image_kubernetes_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_kubernetes_version.setter
    def image_kubernetes_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageType")
    def image_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_type.setter
    def image_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ComputeEnvironmentComputeResourcesLaunchTemplateArgsDict(TypedDict):
    launch_template_id: NotRequired[pulumi.Input[_builtins.str]]
    launch_template_name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ComputeEnvironmentComputeResourcesLaunchTemplateArgs:
    def __init__(__self__, *, launch_template_id: Optional[pulumi.Input[_builtins.str]] = ..., launch_template_name: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateId")
    def launch_template_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_template_id.setter
    def launch_template_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="launchTemplateName")
    def launch_template_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @launch_template_name.setter
    def launch_template_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ComputeEnvironmentEksConfigurationArgsDict(TypedDict):
    eks_cluster_arn: pulumi.Input[_builtins.str]
    kubernetes_namespace: pulumi.Input[_builtins.str]


@pulumi.input_type
class ComputeEnvironmentEksConfigurationArgs:
    def __init__(__self__, *, eks_cluster_arn: pulumi.Input[_builtins.str], kubernetes_namespace: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eksClusterArn")
    def eks_cluster_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @eks_cluster_arn.setter
    def eks_cluster_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesNamespace")
    def kubernetes_namespace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kubernetes_namespace.setter
    def kubernetes_namespace(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ComputeEnvironmentUpdatePolicyArgsDict(TypedDict):
    job_execution_timeout_minutes: NotRequired[pulumi.Input[_builtins.int]]
    terminate_jobs_on_update: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ComputeEnvironmentUpdatePolicyArgs:
    def __init__(__self__, *, job_execution_timeout_minutes: Optional[pulumi.Input[_builtins.int]] = ..., terminate_jobs_on_update: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobExecutionTimeoutMinutes")
    def job_execution_timeout_minutes(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @job_execution_timeout_minutes.setter
    def job_execution_timeout_minutes(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="terminateJobsOnUpdate")
    def terminate_jobs_on_update(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @terminate_jobs_on_update.setter
    def terminate_jobs_on_update(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesArgsDict(TypedDict):
    pod_properties: pulumi.Input[JobDefinitionEksPropertiesPodPropertiesArgsDict]


@pulumi.input_type
class JobDefinitionEksPropertiesArgs:
    def __init__(__self__, *, pod_properties: pulumi.Input[JobDefinitionEksPropertiesPodPropertiesArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="podProperties")
    def pod_properties(self) -> pulumi.Input[JobDefinitionEksPropertiesPodPropertiesArgs]:
        
        ...
    
    @pod_properties.setter
    def pod_properties(self, value: pulumi.Input[JobDefinitionEksPropertiesPodPropertiesArgs]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesArgsDict(TypedDict):
    containers: pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerArgsDict]]]
    dns_policy: NotRequired[pulumi.Input[_builtins.str]]
    host_network: NotRequired[pulumi.Input[_builtins.bool]]
    image_pull_secrets: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesImagePullSecretArgsDict]]]]
    init_containers: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerArgsDict]]]]
    metadata: NotRequired[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesMetadataArgsDict]]
    service_account_name: NotRequired[pulumi.Input[_builtins.str]]
    share_process_namespace: NotRequired[pulumi.Input[_builtins.bool]]
    volumes: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeArgsDict]]]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesArgs:
    def __init__(__self__, *, containers: pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerArgs]]], dns_policy: Optional[pulumi.Input[_builtins.str]] = ..., host_network: Optional[pulumi.Input[_builtins.bool]] = ..., image_pull_secrets: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesImagePullSecretArgs]]]] = ..., init_containers: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerArgs]]]] = ..., metadata: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesMetadataArgs]] = ..., service_account_name: Optional[pulumi.Input[_builtins.str]] = ..., share_process_namespace: Optional[pulumi.Input[_builtins.bool]] = ..., volumes: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def containers(self) -> pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerArgs]]]:
        
        ...
    
    @containers.setter
    def containers(self, value: pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsPolicy")
    def dns_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dns_policy.setter
    def dns_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostNetwork")
    def host_network(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @host_network.setter
    def host_network(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imagePullSecrets")
    def image_pull_secrets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesImagePullSecretArgs]]]]:
        
        ...
    
    @image_pull_secrets.setter
    def image_pull_secrets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesImagePullSecretArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="initContainers")
    def init_containers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerArgs]]]]:
        
        ...
    
    @init_containers.setter
    def init_containers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesMetadataArgs]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesMetadataArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account_name.setter
    def service_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareProcessNamespace")
    def share_process_namespace(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @share_process_namespace.setter
    def share_process_namespace(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeArgs]]]]:
        
        ...
    
    @volumes.setter
    def volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeArgs]]]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesContainerArgsDict(TypedDict):
    image: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    envs: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerEnvArgsDict]]]]
    image_pull_policy: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    resources: NotRequired[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerResourcesArgsDict]]
    security_context: NotRequired[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerSecurityContextArgsDict]]
    volume_mounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerVolumeMountArgsDict]]]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesContainerArgs:
    def __init__(__self__, *, image: pulumi.Input[_builtins.str], args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., envs: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerEnvArgs]]]] = ..., image_pull_policy: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerResourcesArgs]] = ..., security_context: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerSecurityContextArgs]] = ..., volume_mounts: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerVolumeMountArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @args.setter
    def args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @commands.setter
    def commands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerEnvArgs]]]]:
        
        ...
    
    @envs.setter
    def envs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerEnvArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imagePullPolicy")
    def image_pull_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_pull_policy.setter
    def image_pull_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerResourcesArgs]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityContext")
    def security_context(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerSecurityContextArgs]]:
        
        ...
    
    @security_context.setter
    def security_context(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerSecurityContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerVolumeMountArgs]]]]:
        
        ...
    
    @volume_mounts.setter
    def volume_mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesContainerVolumeMountArgs]]]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesContainerEnvArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesContainerEnvArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesContainerResourcesArgsDict(TypedDict):
    limits: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    requests: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesContainerResourcesArgs:
    def __init__(__self__, *, limits: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., requests: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @requests.setter
    def requests(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesContainerSecurityContextArgsDict(TypedDict):
    allow_privilege_escalation: NotRequired[pulumi.Input[_builtins.bool]]
    privileged: NotRequired[pulumi.Input[_builtins.bool]]
    read_only_root_file_system: NotRequired[pulumi.Input[_builtins.bool]]
    run_as_group: NotRequired[pulumi.Input[_builtins.int]]
    run_as_non_root: NotRequired[pulumi.Input[_builtins.bool]]
    run_as_user: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesContainerSecurityContextArgs:
    def __init__(__self__, *, allow_privilege_escalation: Optional[pulumi.Input[_builtins.bool]] = ..., privileged: Optional[pulumi.Input[_builtins.bool]] = ..., read_only_root_file_system: Optional[pulumi.Input[_builtins.bool]] = ..., run_as_group: Optional[pulumi.Input[_builtins.int]] = ..., run_as_non_root: Optional[pulumi.Input[_builtins.bool]] = ..., run_as_user: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPrivilegeEscalation")
    def allow_privilege_escalation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def privileged(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @privileged.setter
    def privileged(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnlyRootFileSystem")
    def read_only_root_file_system(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @read_only_root_file_system.setter
    def read_only_root_file_system(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsGroup")
    def run_as_group(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @run_as_group.setter
    def run_as_group(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsNonRoot")
    def run_as_non_root(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @run_as_non_root.setter
    def run_as_non_root(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @run_as_user.setter
    def run_as_user(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesContainerVolumeMountArgsDict(TypedDict):
    mount_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesContainerVolumeMountArgs:
    def __init__(__self__, *, mount_path: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], read_only: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @mount_path.setter
    def mount_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesImagePullSecretArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesImagePullSecretArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesInitContainerArgsDict(TypedDict):
    image: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    envs: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerEnvArgsDict]]]]
    image_pull_policy: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    resources: NotRequired[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerResourcesArgsDict]]
    security_context: NotRequired[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerSecurityContextArgsDict]]
    volume_mounts: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerVolumeMountArgsDict]]]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesInitContainerArgs:
    def __init__(__self__, *, image: pulumi.Input[_builtins.str], args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., envs: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerEnvArgs]]]] = ..., image_pull_policy: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerResourcesArgs]] = ..., security_context: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerSecurityContextArgs]] = ..., volume_mounts: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerVolumeMountArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @args.setter
    def args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @commands.setter
    def commands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerEnvArgs]]]]:
        
        ...
    
    @envs.setter
    def envs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerEnvArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imagePullPolicy")
    def image_pull_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_pull_policy.setter
    def image_pull_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerResourcesArgs]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerResourcesArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityContext")
    def security_context(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerSecurityContextArgs]]:
        
        ...
    
    @security_context.setter
    def security_context(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerSecurityContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerVolumeMountArgs]]]]:
        
        ...
    
    @volume_mounts.setter
    def volume_mounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesInitContainerVolumeMountArgs]]]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesInitContainerEnvArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesInitContainerEnvArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesInitContainerResourcesArgsDict(TypedDict):
    limits: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    requests: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesInitContainerResourcesArgs:
    def __init__(__self__, *, limits: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., requests: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @requests.setter
    def requests(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesInitContainerSecurityContextArgsDict(TypedDict):
    allow_privilege_escalation: NotRequired[pulumi.Input[_builtins.bool]]
    privileged: NotRequired[pulumi.Input[_builtins.bool]]
    read_only_root_file_system: NotRequired[pulumi.Input[_builtins.bool]]
    run_as_group: NotRequired[pulumi.Input[_builtins.int]]
    run_as_non_root: NotRequired[pulumi.Input[_builtins.bool]]
    run_as_user: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesInitContainerSecurityContextArgs:
    def __init__(__self__, *, allow_privilege_escalation: Optional[pulumi.Input[_builtins.bool]] = ..., privileged: Optional[pulumi.Input[_builtins.bool]] = ..., read_only_root_file_system: Optional[pulumi.Input[_builtins.bool]] = ..., run_as_group: Optional[pulumi.Input[_builtins.int]] = ..., run_as_non_root: Optional[pulumi.Input[_builtins.bool]] = ..., run_as_user: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPrivilegeEscalation")
    def allow_privilege_escalation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_privilege_escalation.setter
    def allow_privilege_escalation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def privileged(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @privileged.setter
    def privileged(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnlyRootFileSystem")
    def read_only_root_file_system(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @read_only_root_file_system.setter
    def read_only_root_file_system(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsGroup")
    def run_as_group(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @run_as_group.setter
    def run_as_group(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsNonRoot")
    def run_as_non_root(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @run_as_non_root.setter
    def run_as_non_root(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @run_as_user.setter
    def run_as_user(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesInitContainerVolumeMountArgsDict(TypedDict):
    mount_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesInitContainerVolumeMountArgs:
    def __init__(__self__, *, mount_path: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], read_only: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @mount_path.setter
    def mount_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesMetadataArgsDict(TypedDict):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesMetadataArgs:
    def __init__(__self__, *, labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesVolumeArgsDict(TypedDict):
    empty_dir: NotRequired[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeEmptyDirArgsDict]]
    host_path: NotRequired[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeHostPathArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    secret: NotRequired[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeSecretArgsDict]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesVolumeArgs:
    def __init__(__self__, *, empty_dir: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeEmptyDirArgs]] = ..., host_path: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeHostPathArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., secret: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeSecretArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeEmptyDirArgs]]:
        ...
    
    @empty_dir.setter
    def empty_dir(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeEmptyDirArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostPath")
    def host_path(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeHostPathArgs]]:
        ...
    
    @host_path.setter
    def host_path(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeHostPathArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeSecretArgs]]:
        ...
    
    @secret.setter
    def secret(self, value: Optional[pulumi.Input[JobDefinitionEksPropertiesPodPropertiesVolumeSecretArgs]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesVolumeEmptyDirArgsDict(TypedDict):
    size_limit: pulumi.Input[_builtins.str]
    medium: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesVolumeEmptyDirArgs:
    def __init__(__self__, *, size_limit: pulumi.Input[_builtins.str], medium: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @size_limit.setter
    def size_limit(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @medium.setter
    def medium(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesVolumeHostPathArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesVolumeHostPathArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobDefinitionEksPropertiesPodPropertiesVolumeSecretArgsDict(TypedDict):
    secret_name: pulumi.Input[_builtins.str]
    optional: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class JobDefinitionEksPropertiesPodPropertiesVolumeSecretArgs:
    def __init__(__self__, *, secret_name: pulumi.Input[_builtins.str], optional: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def optional(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @optional.setter
    def optional(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class JobDefinitionRetryStrategyArgsDict(TypedDict):
    attempts: NotRequired[pulumi.Input[_builtins.int]]
    evaluate_on_exits: NotRequired[pulumi.Input[Sequence[pulumi.Input[JobDefinitionRetryStrategyEvaluateOnExitArgsDict]]]]


@pulumi.input_type
class JobDefinitionRetryStrategyArgs:
    def __init__(__self__, *, attempts: Optional[pulumi.Input[_builtins.int]] = ..., evaluate_on_exits: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionRetryStrategyEvaluateOnExitArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def attempts(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @attempts.setter
    def attempts(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluateOnExits")
    def evaluate_on_exits(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionRetryStrategyEvaluateOnExitArgs]]]]:
        
        ...
    
    @evaluate_on_exits.setter
    def evaluate_on_exits(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobDefinitionRetryStrategyEvaluateOnExitArgs]]]]): # -> None:
        ...
    


class JobDefinitionRetryStrategyEvaluateOnExitArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    on_exit_code: NotRequired[pulumi.Input[_builtins.str]]
    on_reason: NotRequired[pulumi.Input[_builtins.str]]
    on_status_reason: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobDefinitionRetryStrategyEvaluateOnExitArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], on_exit_code: Optional[pulumi.Input[_builtins.str]] = ..., on_reason: Optional[pulumi.Input[_builtins.str]] = ..., on_status_reason: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onExitCode")
    def on_exit_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_exit_code.setter
    def on_exit_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onReason")
    def on_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_reason.setter
    def on_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onStatusReason")
    def on_status_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @on_status_reason.setter
    def on_status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class JobDefinitionTimeoutArgsDict(TypedDict):
    attempt_duration_seconds: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class JobDefinitionTimeoutArgs:
    def __init__(__self__, *, attempt_duration_seconds: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attemptDurationSeconds")
    def attempt_duration_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @attempt_duration_seconds.setter
    def attempt_duration_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class JobQueueComputeEnvironmentOrderArgsDict(TypedDict):
    compute_environment: pulumi.Input[_builtins.str]
    order: pulumi.Input[_builtins.int]


@pulumi.input_type
class JobQueueComputeEnvironmentOrderArgs:
    def __init__(__self__, *, compute_environment: pulumi.Input[_builtins.str], order: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeEnvironment")
    def compute_environment(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @compute_environment.setter
    def compute_environment(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @order.setter
    def order(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class JobQueueJobStateTimeLimitActionArgsDict(TypedDict):
    action: pulumi.Input[_builtins.str]
    max_time_seconds: pulumi.Input[_builtins.int]
    reason: pulumi.Input[_builtins.str]
    state: pulumi.Input[_builtins.str]


@pulumi.input_type
class JobQueueJobStateTimeLimitActionArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], max_time_seconds: pulumi.Input[_builtins.int], reason: pulumi.Input[_builtins.str], state: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxTimeSeconds")
    def max_time_seconds(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_time_seconds.setter
    def max_time_seconds(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reason(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @reason.setter
    def reason(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @state.setter
    def state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class JobQueueTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class JobQueueTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SchedulingPolicyFairSharePolicyArgsDict(TypedDict):
    compute_reservation: NotRequired[pulumi.Input[_builtins.int]]
    share_decay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    share_distributions: NotRequired[pulumi.Input[Sequence[pulumi.Input[SchedulingPolicyFairSharePolicyShareDistributionArgsDict]]]]


@pulumi.input_type
class SchedulingPolicyFairSharePolicyArgs:
    def __init__(__self__, *, compute_reservation: Optional[pulumi.Input[_builtins.int]] = ..., share_decay_seconds: Optional[pulumi.Input[_builtins.int]] = ..., share_distributions: Optional[pulumi.Input[Sequence[pulumi.Input[SchedulingPolicyFairSharePolicyShareDistributionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeReservation")
    def compute_reservation(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @compute_reservation.setter
    def compute_reservation(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareDecaySeconds")
    def share_decay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        ...
    
    @share_decay_seconds.setter
    def share_decay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareDistributions")
    def share_distributions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SchedulingPolicyFairSharePolicyShareDistributionArgs]]]]:
        
        ...
    
    @share_distributions.setter
    def share_distributions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SchedulingPolicyFairSharePolicyShareDistributionArgs]]]]): # -> None:
        ...
    


class SchedulingPolicyFairSharePolicyShareDistributionArgsDict(TypedDict):
    share_identifier: pulumi.Input[_builtins.str]
    weight_factor: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class SchedulingPolicyFairSharePolicyShareDistributionArgs:
    def __init__(__self__, *, share_identifier: pulumi.Input[_builtins.str], weight_factor: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareIdentifier")
    def share_identifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @share_identifier.setter
    def share_identifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weightFactor")
    def weight_factor(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @weight_factor.setter
    def weight_factor(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


