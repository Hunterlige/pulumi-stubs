import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PoolArgs", "Pool"]

@pulumi.input_type
class PoolArgs:
    def __init__(
        __self__,
        *,
        account_name: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        application_licenses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        application_packages: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationPackageReferenceArgs]]]
        ] = ...,
        certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[CertificateReferenceArgs]]]
        ] = ...,
        deployment_configuration: Optional[
            pulumi.Input[DeploymentConfigurationArgs]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[BatchPoolIdentityArgs]] = ...,
        inter_node_communication: Optional[
            pulumi.Input[InterNodeCommunicationState]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Sequence[pulumi.Input[MetadataItemArgs]]]
        ] = ...,
        mount_configuration: Optional[
            pulumi.Input[Sequence[pulumi.Input[MountConfigurationArgs]]]
        ] = ...,
        network_configuration: Optional[pulumi.Input[NetworkConfigurationArgs]] = ...,
        pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        scale_settings: Optional[pulumi.Input[ScaleSettingsArgs]] = ...,
        start_task: Optional[pulumi.Input[StartTaskArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_node_communication_mode: Optional[
            pulumi.Input[NodeCommunicationMode]
        ] = ...,
        task_scheduling_policy: Optional[pulumi.Input[TaskSchedulingPolicyArgs]] = ...,
        task_slots_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        upgrade_policy: Optional[pulumi.Input[UpgradePolicyArgs]] = ...,
        user_accounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[UserAccountArgs]]]
        ] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]: ...
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="applicationLicenses")
    def application_licenses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @application_licenses.setter
    def application_licenses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="applicationPackages")
    def application_packages(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationPackageReferenceArgs]]]
    ]: ...
    @application_packages.setter
    def application_packages(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ApplicationPackageReferenceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[CertificateReferenceArgs]]]]: ...
    @certificates.setter
    def certificates(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[CertificateReferenceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(
        self,
    ) -> Optional[pulumi.Input[DeploymentConfigurationArgs]]: ...
    @deployment_configuration.setter
    def deployment_configuration(
        self, value: Optional[pulumi.Input[DeploymentConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[BatchPoolIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[BatchPoolIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="interNodeCommunication")
    def inter_node_communication(
        self,
    ) -> Optional[pulumi.Input[InterNodeCommunicationState]]: ...
    @inter_node_communication.setter
    def inter_node_communication(
        self, value: Optional[pulumi.Input[InterNodeCommunicationState]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MetadataItemArgs]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[MetadataItemArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="mountConfiguration")
    def mount_configuration(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[MountConfigurationArgs]]]]: ...
    @mount_configuration.setter
    def mount_configuration(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[MountConfigurationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[pulumi.Input[NetworkConfigurationArgs]]: ...
    @network_configuration.setter
    def network_configuration(
        self, value: Optional[pulumi.Input[NetworkConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_tags.setter
    def resource_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="scaleSettings")
    def scale_settings(self) -> Optional[pulumi.Input[ScaleSettingsArgs]]: ...
    @scale_settings.setter
    def scale_settings(self, value: Optional[pulumi.Input[ScaleSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="startTask")
    def start_task(self) -> Optional[pulumi.Input[StartTaskArgs]]: ...
    @start_task.setter
    def start_task(self, value: Optional[pulumi.Input[StartTaskArgs]]): ...
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
    @pulumi.getter(name="targetNodeCommunicationMode")
    def target_node_communication_mode(
        self,
    ) -> Optional[pulumi.Input[NodeCommunicationMode]]: ...
    @target_node_communication_mode.setter
    def target_node_communication_mode(
        self, value: Optional[pulumi.Input[NodeCommunicationMode]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="taskSchedulingPolicy")
    def task_scheduling_policy(
        self,
    ) -> Optional[pulumi.Input[TaskSchedulingPolicyArgs]]: ...
    @task_scheduling_policy.setter
    def task_scheduling_policy(
        self, value: Optional[pulumi.Input[TaskSchedulingPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="taskSlotsPerNode")
    def task_slots_per_node(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @task_slots_per_node.setter
    def task_slots_per_node(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(self) -> Optional[pulumi.Input[UpgradePolicyArgs]]: ...
    @upgrade_policy.setter
    def upgrade_policy(self, value: Optional[pulumi.Input[UpgradePolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="userAccounts")
    def user_accounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[UserAccountArgs]]]]: ...
    @user_accounts.setter
    def user_accounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[UserAccountArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_size.setter
    def vm_size(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:batch:Pool")
class Pool(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        application_licenses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        application_packages: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ApplicationPackageReferenceArgs,
                            ApplicationPackageReferenceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        certificates: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[CertificateReferenceArgs, CertificateReferenceArgsDict]
                    ]
                ]
            ]
        ] = ...,
        deployment_configuration: Optional[
            pulumi.Input[
                Union[DeploymentConfigurationArgs, DeploymentConfigurationArgsDict]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[Union[BatchPoolIdentityArgs, BatchPoolIdentityArgsDict]]
        ] = ...,
        inter_node_communication: Optional[
            pulumi.Input[InterNodeCommunicationState]
        ] = ...,
        metadata: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[MetadataItemArgs, MetadataItemArgsDict]]]
            ]
        ] = ...,
        mount_configuration: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[MountConfigurationArgs, MountConfigurationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        network_configuration: Optional[
            pulumi.Input[Union[NetworkConfigurationArgs, NetworkConfigurationArgsDict]]
        ] = ...,
        pool_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        scale_settings: Optional[
            pulumi.Input[Union[ScaleSettingsArgs, ScaleSettingsArgsDict]]
        ] = ...,
        start_task: Optional[
            pulumi.Input[Union[StartTaskArgs, StartTaskArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_node_communication_mode: Optional[
            pulumi.Input[NodeCommunicationMode]
        ] = ...,
        task_scheduling_policy: Optional[
            pulumi.Input[Union[TaskSchedulingPolicyArgs, TaskSchedulingPolicyArgsDict]]
        ] = ...,
        task_slots_per_node: Optional[pulumi.Input[_builtins.int]] = ...,
        upgrade_policy: Optional[
            pulumi.Input[Union[UpgradePolicyArgs, UpgradePolicyArgsDict]]
        ] = ...,
        user_accounts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[UserAccountArgs, UserAccountArgsDict]]]
            ]
        ] = ...,
        vm_size: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PoolArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Pool: ...
    @_builtins.property
    @pulumi.getter(name="allocationState")
    def allocation_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="allocationStateTransitionTime")
    def allocation_state_transition_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="applicationLicenses")
    def application_licenses(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="applicationPackages")
    def application_packages(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.ApplicationPackageReferenceResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="autoScaleRun")
    def auto_scale_run(self) -> pulumi.Output[outputs.AutoScaleRunResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.CertificateReferenceResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="currentDedicatedNodes")
    def current_dedicated_nodes(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="currentLowPriorityNodes")
    def current_low_priority_nodes(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="currentNodeCommunicationMode")
    def current_node_communication_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentConfiguration")
    def deployment_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.DeploymentConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.BatchPoolIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="interNodeCommunication")
    def inter_node_communication(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.MetadataItemResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="mountConfiguration")
    def mount_configuration(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.MountConfigurationResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.NetworkConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningStateTransitionTime")
    def provisioning_state_transition_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resizeOperationStatus")
    def resize_operation_status(
        self,
    ) -> pulumi.Output[outputs.ResizeOperationStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="scaleSettings")
    def scale_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.ScaleSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="startTask")
    def start_task(self) -> pulumi.Output[Optional[outputs.StartTaskResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="targetNodeCommunicationMode")
    def target_node_communication_mode(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="taskSchedulingPolicy")
    def task_scheduling_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.TaskSchedulingPolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="taskSlotsPerNode")
    def task_slots_per_node(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="upgradePolicy")
    def upgrade_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.UpgradePolicyResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="userAccounts")
    def user_accounts(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.UserAccountResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> pulumi.Output[Optional[_builtins.str]]: ...
