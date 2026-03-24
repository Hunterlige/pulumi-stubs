import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ClusterArgs", "Cluster"]

@pulumi.input_type
class ClusterArgs:
    def __init__(
        __self__,
        *,
        release_label: pulumi.Input[_builtins.str],
        service_role: pulumi.Input[_builtins.str],
        additional_info: Optional[pulumi.Input[_builtins.str]] = ...,
        applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        auto_termination_policy: Optional[
            pulumi.Input[ClusterAutoTerminationPolicyArgs]
        ] = ...,
        autoscaling_role: Optional[pulumi.Input[_builtins.str]] = ...,
        bootstrap_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterBootstrapActionArgs]]]
        ] = ...,
        configurations: Optional[pulumi.Input[_builtins.str]] = ...,
        configurations_json: Optional[pulumi.Input[_builtins.str]] = ...,
        core_instance_fleet: Optional[pulumi.Input[ClusterCoreInstanceFleetArgs]] = ...,
        core_instance_group: Optional[pulumi.Input[ClusterCoreInstanceGroupArgs]] = ...,
        custom_ami_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_root_volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
        ec2_attributes: Optional[pulumi.Input[ClusterEc2AttributesArgs]] = ...,
        keep_job_flow_alive_when_no_steps: Optional[pulumi.Input[_builtins.bool]] = ...,
        kerberos_attributes: Optional[
            pulumi.Input[ClusterKerberosAttributesArgs]
        ] = ...,
        list_steps_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        log_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        master_instance_fleet: Optional[
            pulumi.Input[ClusterMasterInstanceFleetArgs]
        ] = ...,
        master_instance_group: Optional[
            pulumi.Input[ClusterMasterInstanceGroupArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_group_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterPlacementGroupConfigArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scale_down_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        security_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        step_concurrency_level: Optional[pulumi.Input[_builtins.int]] = ...,
        steps: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStepArgs]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        termination_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        unhealthy_node_replacement: Optional[pulumi.Input[_builtins.bool]] = ...,
        visible_to_all_users: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> pulumi.Input[_builtins.str]: ...
    @release_label.setter
    def release_label(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Input[_builtins.str]: ...
    @service_role.setter
    def service_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_info.setter
    def additional_info(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def applications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @applications.setter
    def applications(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoTerminationPolicy")
    def auto_termination_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterAutoTerminationPolicyArgs]]: ...
    @auto_termination_policy.setter
    def auto_termination_policy(
        self, value: Optional[pulumi.Input[ClusterAutoTerminationPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingRole")
    def autoscaling_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autoscaling_role.setter
    def autoscaling_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bootstrapActions")
    def bootstrap_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterBootstrapActionArgs]]]]: ...
    @bootstrap_actions.setter
    def bootstrap_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterBootstrapActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationsJson")
    def configurations_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configurations_json.setter
    def configurations_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coreInstanceFleet")
    def core_instance_fleet(
        self,
    ) -> Optional[pulumi.Input[ClusterCoreInstanceFleetArgs]]: ...
    @core_instance_fleet.setter
    def core_instance_fleet(
        self, value: Optional[pulumi.Input[ClusterCoreInstanceFleetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="coreInstanceGroup")
    def core_instance_group(
        self,
    ) -> Optional[pulumi.Input[ClusterCoreInstanceGroupArgs]]: ...
    @core_instance_group.setter
    def core_instance_group(
        self, value: Optional[pulumi.Input[ClusterCoreInstanceGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customAmiId")
    def custom_ami_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_ami_id.setter
    def custom_ami_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebsRootVolumeSize")
    def ebs_root_volume_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ebs_root_volume_size.setter
    def ebs_root_volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ec2Attributes")
    def ec2_attributes(self) -> Optional[pulumi.Input[ClusterEc2AttributesArgs]]: ...
    @ec2_attributes.setter
    def ec2_attributes(
        self, value: Optional[pulumi.Input[ClusterEc2AttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keepJobFlowAliveWhenNoSteps")
    def keep_job_flow_alive_when_no_steps(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @keep_job_flow_alive_when_no_steps.setter
    def keep_job_flow_alive_when_no_steps(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kerberosAttributes")
    def kerberos_attributes(
        self,
    ) -> Optional[pulumi.Input[ClusterKerberosAttributesArgs]]: ...
    @kerberos_attributes.setter
    def kerberos_attributes(
        self, value: Optional[pulumi.Input[ClusterKerberosAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="listStepsStates")
    def list_steps_states(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @list_steps_states.setter
    def list_steps_states(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logEncryptionKmsKeyId")
    def log_encryption_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_encryption_kms_key_id.setter
    def log_encryption_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logUri")
    def log_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_uri.setter
    def log_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterInstanceFleet")
    def master_instance_fleet(
        self,
    ) -> Optional[pulumi.Input[ClusterMasterInstanceFleetArgs]]: ...
    @master_instance_fleet.setter
    def master_instance_fleet(
        self, value: Optional[pulumi.Input[ClusterMasterInstanceFleetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterInstanceGroup")
    def master_instance_group(
        self,
    ) -> Optional[pulumi.Input[ClusterMasterInstanceGroupArgs]]: ...
    @master_instance_group.setter
    def master_instance_group(
        self, value: Optional[pulumi.Input[ClusterMasterInstanceGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osReleaseLabel")
    def os_release_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_release_label.setter
    def os_release_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="placementGroupConfigs")
    def placement_group_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterPlacementGroupConfigArgs]]]
    ]: ...
    @placement_group_configs.setter
    def placement_group_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterPlacementGroupConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scaleDownBehavior")
    def scale_down_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scale_down_behavior.setter
    def scale_down_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_configuration.setter
    def security_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stepConcurrencyLevel")
    def step_concurrency_level(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @step_concurrency_level.setter
    def step_concurrency_level(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStepArgs]]]]: ...
    @steps.setter
    def steps(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStepArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @termination_protection.setter
    def termination_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="unhealthyNodeReplacement")
    def unhealthy_node_replacement(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unhealthy_node_replacement.setter
    def unhealthy_node_replacement(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="visibleToAllUsers")
    def visible_to_all_users(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @visible_to_all_users.setter
    def visible_to_all_users(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.input_type
class _ClusterState:
    def __init__(
        __self__,
        *,
        additional_info: Optional[pulumi.Input[_builtins.str]] = ...,
        applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_termination_policy: Optional[
            pulumi.Input[ClusterAutoTerminationPolicyArgs]
        ] = ...,
        autoscaling_role: Optional[pulumi.Input[_builtins.str]] = ...,
        bootstrap_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterBootstrapActionArgs]]]
        ] = ...,
        cluster_state: Optional[pulumi.Input[_builtins.str]] = ...,
        configurations: Optional[pulumi.Input[_builtins.str]] = ...,
        configurations_json: Optional[pulumi.Input[_builtins.str]] = ...,
        core_instance_fleet: Optional[pulumi.Input[ClusterCoreInstanceFleetArgs]] = ...,
        core_instance_group: Optional[pulumi.Input[ClusterCoreInstanceGroupArgs]] = ...,
        custom_ami_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_root_volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
        ec2_attributes: Optional[pulumi.Input[ClusterEc2AttributesArgs]] = ...,
        keep_job_flow_alive_when_no_steps: Optional[pulumi.Input[_builtins.bool]] = ...,
        kerberos_attributes: Optional[
            pulumi.Input[ClusterKerberosAttributesArgs]
        ] = ...,
        list_steps_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        log_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        master_instance_fleet: Optional[
            pulumi.Input[ClusterMasterInstanceFleetArgs]
        ] = ...,
        master_instance_group: Optional[
            pulumi.Input[ClusterMasterInstanceGroupArgs]
        ] = ...,
        master_public_dns: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_group_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterPlacementGroupConfigArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        scale_down_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        security_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        step_concurrency_level: Optional[pulumi.Input[_builtins.int]] = ...,
        steps: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStepArgs]]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        termination_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        unhealthy_node_replacement: Optional[pulumi.Input[_builtins.bool]] = ...,
        visible_to_all_users: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_info.setter
    def additional_info(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def applications(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @applications.setter
    def applications(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="autoTerminationPolicy")
    def auto_termination_policy(
        self,
    ) -> Optional[pulumi.Input[ClusterAutoTerminationPolicyArgs]]: ...
    @auto_termination_policy.setter
    def auto_termination_policy(
        self, value: Optional[pulumi.Input[ClusterAutoTerminationPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoscalingRole")
    def autoscaling_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @autoscaling_role.setter
    def autoscaling_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bootstrapActions")
    def bootstrap_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterBootstrapActionArgs]]]]: ...
    @bootstrap_actions.setter
    def bootstrap_actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterBootstrapActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterState")
    def cluster_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_state.setter
    def cluster_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationsJson")
    def configurations_json(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configurations_json.setter
    def configurations_json(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="coreInstanceFleet")
    def core_instance_fleet(
        self,
    ) -> Optional[pulumi.Input[ClusterCoreInstanceFleetArgs]]: ...
    @core_instance_fleet.setter
    def core_instance_fleet(
        self, value: Optional[pulumi.Input[ClusterCoreInstanceFleetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="coreInstanceGroup")
    def core_instance_group(
        self,
    ) -> Optional[pulumi.Input[ClusterCoreInstanceGroupArgs]]: ...
    @core_instance_group.setter
    def core_instance_group(
        self, value: Optional[pulumi.Input[ClusterCoreInstanceGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customAmiId")
    def custom_ami_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_ami_id.setter
    def custom_ami_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ebsRootVolumeSize")
    def ebs_root_volume_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @ebs_root_volume_size.setter
    def ebs_root_volume_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="ec2Attributes")
    def ec2_attributes(self) -> Optional[pulumi.Input[ClusterEc2AttributesArgs]]: ...
    @ec2_attributes.setter
    def ec2_attributes(
        self, value: Optional[pulumi.Input[ClusterEc2AttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="keepJobFlowAliveWhenNoSteps")
    def keep_job_flow_alive_when_no_steps(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @keep_job_flow_alive_when_no_steps.setter
    def keep_job_flow_alive_when_no_steps(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kerberosAttributes")
    def kerberos_attributes(
        self,
    ) -> Optional[pulumi.Input[ClusterKerberosAttributesArgs]]: ...
    @kerberos_attributes.setter
    def kerberos_attributes(
        self, value: Optional[pulumi.Input[ClusterKerberosAttributesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="listStepsStates")
    def list_steps_states(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @list_steps_states.setter
    def list_steps_states(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logEncryptionKmsKeyId")
    def log_encryption_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_encryption_kms_key_id.setter
    def log_encryption_kms_key_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logUri")
    def log_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @log_uri.setter
    def log_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="masterInstanceFleet")
    def master_instance_fleet(
        self,
    ) -> Optional[pulumi.Input[ClusterMasterInstanceFleetArgs]]: ...
    @master_instance_fleet.setter
    def master_instance_fleet(
        self, value: Optional[pulumi.Input[ClusterMasterInstanceFleetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterInstanceGroup")
    def master_instance_group(
        self,
    ) -> Optional[pulumi.Input[ClusterMasterInstanceGroupArgs]]: ...
    @master_instance_group.setter
    def master_instance_group(
        self, value: Optional[pulumi.Input[ClusterMasterInstanceGroupArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="masterPublicDns")
    def master_public_dns(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @master_public_dns.setter
    def master_public_dns(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osReleaseLabel")
    def os_release_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_release_label.setter
    def os_release_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="placementGroupConfigs")
    def placement_group_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterPlacementGroupConfigArgs]]]
    ]: ...
    @placement_group_configs.setter
    def placement_group_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterPlacementGroupConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_label.setter
    def release_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scaleDownBehavior")
    def scale_down_behavior(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scale_down_behavior.setter
    def scale_down_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_configuration.setter
    def security_configuration(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_role.setter
    def service_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stepConcurrencyLevel")
    def step_concurrency_level(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @step_concurrency_level.setter
    def step_concurrency_level(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStepArgs]]]]: ...
    @steps.setter
    def steps(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStepArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @termination_protection.setter
    def termination_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="unhealthyNodeReplacement")
    def unhealthy_node_replacement(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unhealthy_node_replacement.setter
    def unhealthy_node_replacement(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="visibleToAllUsers")
    def visible_to_all_users(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @visible_to_all_users.setter
    def visible_to_all_users(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("aws:emr/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_info: Optional[pulumi.Input[_builtins.str]] = ...,
        applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        auto_termination_policy: Optional[
            pulumi.Input[
                Union[
                    ClusterAutoTerminationPolicyArgs,
                    ClusterAutoTerminationPolicyArgsDict,
                ]
            ]
        ] = ...,
        autoscaling_role: Optional[pulumi.Input[_builtins.str]] = ...,
        bootstrap_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterBootstrapActionArgs, ClusterBootstrapActionArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        configurations: Optional[pulumi.Input[_builtins.str]] = ...,
        configurations_json: Optional[pulumi.Input[_builtins.str]] = ...,
        core_instance_fleet: Optional[
            pulumi.Input[
                Union[ClusterCoreInstanceFleetArgs, ClusterCoreInstanceFleetArgsDict]
            ]
        ] = ...,
        core_instance_group: Optional[
            pulumi.Input[
                Union[ClusterCoreInstanceGroupArgs, ClusterCoreInstanceGroupArgsDict]
            ]
        ] = ...,
        custom_ami_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_root_volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
        ec2_attributes: Optional[
            pulumi.Input[Union[ClusterEc2AttributesArgs, ClusterEc2AttributesArgsDict]]
        ] = ...,
        keep_job_flow_alive_when_no_steps: Optional[pulumi.Input[_builtins.bool]] = ...,
        kerberos_attributes: Optional[
            pulumi.Input[
                Union[ClusterKerberosAttributesArgs, ClusterKerberosAttributesArgsDict]
            ]
        ] = ...,
        list_steps_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        log_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        master_instance_fleet: Optional[
            pulumi.Input[
                Union[
                    ClusterMasterInstanceFleetArgs, ClusterMasterInstanceFleetArgsDict
                ]
            ]
        ] = ...,
        master_instance_group: Optional[
            pulumi.Input[
                Union[
                    ClusterMasterInstanceGroupArgs, ClusterMasterInstanceGroupArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_group_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterPlacementGroupConfigArgs,
                            ClusterPlacementGroupConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        scale_down_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        security_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        step_concurrency_level: Optional[pulumi.Input[_builtins.int]] = ...,
        steps: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ClusterStepArgs, ClusterStepArgsDict]]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        termination_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        unhealthy_node_replacement: Optional[pulumi.Input[_builtins.bool]] = ...,
        visible_to_all_users: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ClusterArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_info: Optional[pulumi.Input[_builtins.str]] = ...,
        applications: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        auto_termination_policy: Optional[
            pulumi.Input[
                Union[
                    ClusterAutoTerminationPolicyArgs,
                    ClusterAutoTerminationPolicyArgsDict,
                ]
            ]
        ] = ...,
        autoscaling_role: Optional[pulumi.Input[_builtins.str]] = ...,
        bootstrap_actions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterBootstrapActionArgs, ClusterBootstrapActionArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        cluster_state: Optional[pulumi.Input[_builtins.str]] = ...,
        configurations: Optional[pulumi.Input[_builtins.str]] = ...,
        configurations_json: Optional[pulumi.Input[_builtins.str]] = ...,
        core_instance_fleet: Optional[
            pulumi.Input[
                Union[ClusterCoreInstanceFleetArgs, ClusterCoreInstanceFleetArgsDict]
            ]
        ] = ...,
        core_instance_group: Optional[
            pulumi.Input[
                Union[ClusterCoreInstanceGroupArgs, ClusterCoreInstanceGroupArgsDict]
            ]
        ] = ...,
        custom_ami_id: Optional[pulumi.Input[_builtins.str]] = ...,
        ebs_root_volume_size: Optional[pulumi.Input[_builtins.int]] = ...,
        ec2_attributes: Optional[
            pulumi.Input[Union[ClusterEc2AttributesArgs, ClusterEc2AttributesArgsDict]]
        ] = ...,
        keep_job_flow_alive_when_no_steps: Optional[pulumi.Input[_builtins.bool]] = ...,
        kerberos_attributes: Optional[
            pulumi.Input[
                Union[ClusterKerberosAttributesArgs, ClusterKerberosAttributesArgsDict]
            ]
        ] = ...,
        list_steps_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        log_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...,
        log_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        master_instance_fleet: Optional[
            pulumi.Input[
                Union[
                    ClusterMasterInstanceFleetArgs, ClusterMasterInstanceFleetArgsDict
                ]
            ]
        ] = ...,
        master_instance_group: Optional[
            pulumi.Input[
                Union[
                    ClusterMasterInstanceGroupArgs, ClusterMasterInstanceGroupArgsDict
                ]
            ]
        ] = ...,
        master_public_dns: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        os_release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_group_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ClusterPlacementGroupConfigArgs,
                            ClusterPlacementGroupConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        release_label: Optional[pulumi.Input[_builtins.str]] = ...,
        scale_down_behavior: Optional[pulumi.Input[_builtins.str]] = ...,
        security_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        service_role: Optional[pulumi.Input[_builtins.str]] = ...,
        step_concurrency_level: Optional[pulumi.Input[_builtins.int]] = ...,
        steps: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ClusterStepArgs, ClusterStepArgsDict]]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        termination_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        unhealthy_node_replacement: Optional[pulumi.Input[_builtins.bool]] = ...,
        visible_to_all_users: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> Cluster: ...
    @_builtins.property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def applications(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="autoTerminationPolicy")
    def auto_termination_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterAutoTerminationPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="autoscalingRole")
    def autoscaling_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="bootstrapActions")
    def bootstrap_actions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ClusterBootstrapAction]]]: ...
    @_builtins.property
    @pulumi.getter(name="clusterState")
    def cluster_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def configurations(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="configurationsJson")
    def configurations_json(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="coreInstanceFleet")
    def core_instance_fleet(
        self,
    ) -> pulumi.Output[outputs.ClusterCoreInstanceFleet]: ...
    @_builtins.property
    @pulumi.getter(name="coreInstanceGroup")
    def core_instance_group(
        self,
    ) -> pulumi.Output[outputs.ClusterCoreInstanceGroup]: ...
    @_builtins.property
    @pulumi.getter(name="customAmiId")
    def custom_ami_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ebsRootVolumeSize")
    def ebs_root_volume_size(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="ec2Attributes")
    def ec2_attributes(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterEc2Attributes]]: ...
    @_builtins.property
    @pulumi.getter(name="keepJobFlowAliveWhenNoSteps")
    def keep_job_flow_alive_when_no_steps(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kerberosAttributes")
    def kerberos_attributes(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterKerberosAttributes]]: ...
    @_builtins.property
    @pulumi.getter(name="listStepsStates")
    def list_steps_states(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="logEncryptionKmsKeyId")
    def log_encryption_kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logUri")
    def log_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="masterInstanceFleet")
    def master_instance_fleet(
        self,
    ) -> pulumi.Output[outputs.ClusterMasterInstanceFleet]: ...
    @_builtins.property
    @pulumi.getter(name="masterInstanceGroup")
    def master_instance_group(
        self,
    ) -> pulumi.Output[outputs.ClusterMasterInstanceGroup]: ...
    @_builtins.property
    @pulumi.getter(name="masterPublicDns")
    def master_public_dns(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osReleaseLabel")
    def os_release_label(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="placementGroupConfigs")
    def placement_group_configs(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ClusterPlacementGroupConfig]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="releaseLabel")
    def release_label(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scaleDownBehavior")
    def scale_down_behavior(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityConfiguration")
    def security_configuration(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stepConcurrencyLevel")
    def step_concurrency_level(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def steps(self) -> pulumi.Output[Sequence[outputs.ClusterStep]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="terminationProtection")
    def termination_protection(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyNodeReplacement")
    def unhealthy_node_replacement(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="visibleToAllUsers")
    def visible_to_all_users(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
