import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["InstanceGroupManagerArgs", "InstanceGroupManager"]

@pulumi.input_type
class InstanceGroupManagerArgs:
    def __init__(
        __self__,
        *,
        base_instance_name: pulumi.Input[_builtins.str],
        versions: pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerVersionArgs]]],
        all_instances_config: Optional[
            pulumi.Input[InstanceGroupManagerAllInstancesConfigArgs]
        ] = ...,
        auto_healing_policies: Optional[
            pulumi.Input[InstanceGroupManagerAutoHealingPoliciesArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_lifecycle_policy: Optional[
            pulumi.Input[InstanceGroupManagerInstanceLifecyclePolicyArgs]
        ] = ...,
        list_managed_instances_results: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        named_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerNamedPortArgs]]]
        ] = ...,
        params: Optional[pulumi.Input[InstanceGroupManagerParamsArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_policies: Optional[
            pulumi.Input[InstanceGroupManagerResourcePoliciesArgs]
        ] = ...,
        standby_policy: Optional[
            pulumi.Input[InstanceGroupManagerStandbyPolicyArgs]
        ] = ...,
        stateful_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulDiskArgs]]]
        ] = ...,
        stateful_external_ips: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGroupManagerStatefulExternalIpArgs]]
            ]
        ] = ...,
        stateful_internal_ips: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGroupManagerStatefulInternalIpArgs]]
            ]
        ] = ...,
        target_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_size: Optional[pulumi.Input[_builtins.int]] = ...,
        target_stopped_size: Optional[pulumi.Input[_builtins.int]] = ...,
        target_suspended_size: Optional[pulumi.Input[_builtins.int]] = ...,
        update_policy: Optional[
            pulumi.Input[InstanceGroupManagerUpdatePolicyArgs]
        ] = ...,
        wait_for_instances: Optional[pulumi.Input[_builtins.bool]] = ...,
        wait_for_instances_status: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseInstanceName")
    def base_instance_name(self) -> pulumi.Input[_builtins.str]: ...
    @base_instance_name.setter
    def base_instance_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def versions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerVersionArgs]]]: ...
    @versions.setter
    def versions(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerVersionArgs]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allInstancesConfig")
    def all_instances_config(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerAllInstancesConfigArgs]]: ...
    @all_instances_config.setter
    def all_instances_config(
        self, value: Optional[pulumi.Input[InstanceGroupManagerAllInstancesConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoHealingPolicies")
    def auto_healing_policies(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerAutoHealingPoliciesArgs]]: ...
    @auto_healing_policies.setter
    def auto_healing_policies(
        self, value: Optional[pulumi.Input[InstanceGroupManagerAutoHealingPoliciesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceLifecyclePolicy")
    def instance_lifecycle_policy(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerInstanceLifecyclePolicyArgs]]: ...
    @instance_lifecycle_policy.setter
    def instance_lifecycle_policy(
        self,
        value: Optional[pulumi.Input[InstanceGroupManagerInstanceLifecyclePolicyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="listManagedInstancesResults")
    def list_managed_instances_results(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @list_managed_instances_results.setter
    def list_managed_instances_results(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namedPorts")
    def named_ports(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerNamedPortArgs]]]
    ]: ...
    @named_ports.setter
    def named_ports(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerNamedPortArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[InstanceGroupManagerParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[InstanceGroupManagerParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerResourcePoliciesArgs]]: ...
    @resource_policies.setter
    def resource_policies(
        self, value: Optional[pulumi.Input[InstanceGroupManagerResourcePoliciesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="standbyPolicy")
    def standby_policy(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerStandbyPolicyArgs]]: ...
    @standby_policy.setter
    def standby_policy(
        self, value: Optional[pulumi.Input[InstanceGroupManagerStandbyPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulDisks")
    def stateful_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulDiskArgs]]]
    ]: ...
    @stateful_disks.setter
    def stateful_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulDiskArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulExternalIps")
    def stateful_external_ips(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulExternalIpArgs]]]
    ]: ...
    @stateful_external_ips.setter
    def stateful_external_ips(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGroupManagerStatefulExternalIpArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulInternalIps")
    def stateful_internal_ips(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulInternalIpArgs]]]
    ]: ...
    @stateful_internal_ips.setter
    def stateful_internal_ips(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGroupManagerStatefulInternalIpArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetPools")
    def target_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_pools.setter
    def target_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_size.setter
    def target_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetStoppedSize")
    def target_stopped_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_stopped_size.setter
    def target_stopped_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetSuspendedSize")
    def target_suspended_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_suspended_size.setter
    def target_suspended_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="updatePolicy")
    def update_policy(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerUpdatePolicyArgs]]: ...
    @update_policy.setter
    def update_policy(
        self, value: Optional[pulumi.Input[InstanceGroupManagerUpdatePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitForInstances")
    def wait_for_instances(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_instances.setter
    def wait_for_instances(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="waitForInstancesStatus")
    def wait_for_instances_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_for_instances_status.setter
    def wait_for_instances_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _InstanceGroupManagerState:
    def __init__(
        __self__,
        *,
        all_instances_config: Optional[
            pulumi.Input[InstanceGroupManagerAllInstancesConfigArgs]
        ] = ...,
        auto_healing_policies: Optional[
            pulumi.Input[InstanceGroupManagerAutoHealingPoliciesArgs]
        ] = ...,
        base_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_group: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_group_manager_id: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_lifecycle_policy: Optional[
            pulumi.Input[InstanceGroupManagerInstanceLifecyclePolicyArgs]
        ] = ...,
        list_managed_instances_results: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        named_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerNamedPortArgs]]]
        ] = ...,
        operation: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[pulumi.Input[InstanceGroupManagerParamsArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_policies: Optional[
            pulumi.Input[InstanceGroupManagerResourcePoliciesArgs]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        standby_policy: Optional[
            pulumi.Input[InstanceGroupManagerStandbyPolicyArgs]
        ] = ...,
        stateful_disks: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulDiskArgs]]]
        ] = ...,
        stateful_external_ips: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGroupManagerStatefulExternalIpArgs]]
            ]
        ] = ...,
        stateful_internal_ips: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGroupManagerStatefulInternalIpArgs]]
            ]
        ] = ...,
        statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatusArgs]]]
        ] = ...,
        target_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_size: Optional[pulumi.Input[_builtins.int]] = ...,
        target_stopped_size: Optional[pulumi.Input[_builtins.int]] = ...,
        target_suspended_size: Optional[pulumi.Input[_builtins.int]] = ...,
        update_policy: Optional[
            pulumi.Input[InstanceGroupManagerUpdatePolicyArgs]
        ] = ...,
        versions: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerVersionArgs]]]
        ] = ...,
        wait_for_instances: Optional[pulumi.Input[_builtins.bool]] = ...,
        wait_for_instances_status: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allInstancesConfig")
    def all_instances_config(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerAllInstancesConfigArgs]]: ...
    @all_instances_config.setter
    def all_instances_config(
        self, value: Optional[pulumi.Input[InstanceGroupManagerAllInstancesConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoHealingPolicies")
    def auto_healing_policies(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerAutoHealingPoliciesArgs]]: ...
    @auto_healing_policies.setter
    def auto_healing_policies(
        self, value: Optional[pulumi.Input[InstanceGroupManagerAutoHealingPoliciesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="baseInstanceName")
    def base_instance_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_instance_name.setter
    def base_instance_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceGroup")
    def instance_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_group.setter
    def instance_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerId")
    def instance_group_manager_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @instance_group_manager_id.setter
    def instance_group_manager_id(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="instanceLifecyclePolicy")
    def instance_lifecycle_policy(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerInstanceLifecyclePolicyArgs]]: ...
    @instance_lifecycle_policy.setter
    def instance_lifecycle_policy(
        self,
        value: Optional[pulumi.Input[InstanceGroupManagerInstanceLifecyclePolicyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="listManagedInstancesResults")
    def list_managed_instances_results(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @list_managed_instances_results.setter
    def list_managed_instances_results(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namedPorts")
    def named_ports(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerNamedPortArgs]]]
    ]: ...
    @named_ports.setter
    def named_ports(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerNamedPortArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation.setter
    def operation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[InstanceGroupManagerParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[InstanceGroupManagerParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerResourcePoliciesArgs]]: ...
    @resource_policies.setter
    def resource_policies(
        self, value: Optional[pulumi.Input[InstanceGroupManagerResourcePoliciesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="standbyPolicy")
    def standby_policy(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerStandbyPolicyArgs]]: ...
    @standby_policy.setter
    def standby_policy(
        self, value: Optional[pulumi.Input[InstanceGroupManagerStandbyPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulDisks")
    def stateful_disks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulDiskArgs]]]
    ]: ...
    @stateful_disks.setter
    def stateful_disks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulDiskArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulExternalIps")
    def stateful_external_ips(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulExternalIpArgs]]]
    ]: ...
    @stateful_external_ips.setter
    def stateful_external_ips(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGroupManagerStatefulExternalIpArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="statefulInternalIps")
    def stateful_internal_ips(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatefulInternalIpArgs]]]
    ]: ...
    @stateful_internal_ips.setter
    def stateful_internal_ips(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InstanceGroupManagerStatefulInternalIpArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatusArgs]]]
    ]: ...
    @statuses.setter
    def statuses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerStatusArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetPools")
    def target_pools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @target_pools.setter
    def target_pools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_size.setter
    def target_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetStoppedSize")
    def target_stopped_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_stopped_size.setter
    def target_stopped_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetSuspendedSize")
    def target_suspended_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_suspended_size.setter
    def target_suspended_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="updatePolicy")
    def update_policy(
        self,
    ) -> Optional[pulumi.Input[InstanceGroupManagerUpdatePolicyArgs]]: ...
    @update_policy.setter
    def update_policy(
        self, value: Optional[pulumi.Input[InstanceGroupManagerUpdatePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def versions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerVersionArgs]]]
    ]: ...
    @versions.setter
    def versions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceGroupManagerVersionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitForInstances")
    def wait_for_instances(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @wait_for_instances.setter
    def wait_for_instances(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="waitForInstancesStatus")
    def wait_for_instances_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @wait_for_instances_status.setter
    def wait_for_instances_status(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class InstanceGroupManager(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        all_instances_config: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerAllInstancesConfigArgs,
                    InstanceGroupManagerAllInstancesConfigArgsDict,
                ]
            ]
        ] = ...,
        auto_healing_policies: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerAutoHealingPoliciesArgs,
                    InstanceGroupManagerAutoHealingPoliciesArgsDict,
                ]
            ]
        ] = ...,
        base_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_lifecycle_policy: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerInstanceLifecyclePolicyArgs,
                    InstanceGroupManagerInstanceLifecyclePolicyArgsDict,
                ]
            ]
        ] = ...,
        list_managed_instances_results: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        named_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerNamedPortArgs,
                            InstanceGroupManagerNamedPortArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        params: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerParamsArgs, InstanceGroupManagerParamsArgsDict
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_policies: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerResourcePoliciesArgs,
                    InstanceGroupManagerResourcePoliciesArgsDict,
                ]
            ]
        ] = ...,
        standby_policy: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerStandbyPolicyArgs,
                    InstanceGroupManagerStandbyPolicyArgsDict,
                ]
            ]
        ] = ...,
        stateful_disks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerStatefulDiskArgs,
                            InstanceGroupManagerStatefulDiskArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        stateful_external_ips: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerStatefulExternalIpArgs,
                            InstanceGroupManagerStatefulExternalIpArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        stateful_internal_ips: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerStatefulInternalIpArgs,
                            InstanceGroupManagerStatefulInternalIpArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        target_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_size: Optional[pulumi.Input[_builtins.int]] = ...,
        target_stopped_size: Optional[pulumi.Input[_builtins.int]] = ...,
        target_suspended_size: Optional[pulumi.Input[_builtins.int]] = ...,
        update_policy: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerUpdatePolicyArgs,
                    InstanceGroupManagerUpdatePolicyArgsDict,
                ]
            ]
        ] = ...,
        versions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerVersionArgs,
                            InstanceGroupManagerVersionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        wait_for_instances: Optional[pulumi.Input[_builtins.bool]] = ...,
        wait_for_instances_status: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: InstanceGroupManagerArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        all_instances_config: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerAllInstancesConfigArgs,
                    InstanceGroupManagerAllInstancesConfigArgsDict,
                ]
            ]
        ] = ...,
        auto_healing_policies: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerAutoHealingPoliciesArgs,
                    InstanceGroupManagerAutoHealingPoliciesArgsDict,
                ]
            ]
        ] = ...,
        base_instance_name: Optional[pulumi.Input[_builtins.str]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_group: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_group_manager_id: Optional[pulumi.Input[_builtins.int]] = ...,
        instance_lifecycle_policy: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerInstanceLifecyclePolicyArgs,
                    InstanceGroupManagerInstanceLifecyclePolicyArgsDict,
                ]
            ]
        ] = ...,
        list_managed_instances_results: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        named_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerNamedPortArgs,
                            InstanceGroupManagerNamedPortArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        operation: Optional[pulumi.Input[_builtins.str]] = ...,
        params: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerParamsArgs, InstanceGroupManagerParamsArgsDict
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_policies: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerResourcePoliciesArgs,
                    InstanceGroupManagerResourcePoliciesArgsDict,
                ]
            ]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        standby_policy: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerStandbyPolicyArgs,
                    InstanceGroupManagerStandbyPolicyArgsDict,
                ]
            ]
        ] = ...,
        stateful_disks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerStatefulDiskArgs,
                            InstanceGroupManagerStatefulDiskArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        stateful_external_ips: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerStatefulExternalIpArgs,
                            InstanceGroupManagerStatefulExternalIpArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        stateful_internal_ips: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerStatefulInternalIpArgs,
                            InstanceGroupManagerStatefulInternalIpArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerStatusArgs,
                            InstanceGroupManagerStatusArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        target_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        target_size: Optional[pulumi.Input[_builtins.int]] = ...,
        target_stopped_size: Optional[pulumi.Input[_builtins.int]] = ...,
        target_suspended_size: Optional[pulumi.Input[_builtins.int]] = ...,
        update_policy: Optional[
            pulumi.Input[
                Union[
                    InstanceGroupManagerUpdatePolicyArgs,
                    InstanceGroupManagerUpdatePolicyArgsDict,
                ]
            ]
        ] = ...,
        versions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            InstanceGroupManagerVersionArgs,
                            InstanceGroupManagerVersionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        wait_for_instances: Optional[pulumi.Input[_builtins.bool]] = ...,
        wait_for_instances_status: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> InstanceGroupManager: ...
    @_builtins.property
    @pulumi.getter(name="allInstancesConfig")
    def all_instances_config(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceGroupManagerAllInstancesConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="autoHealingPolicies")
    def auto_healing_policies(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceGroupManagerAutoHealingPolicies]]: ...
    @_builtins.property
    @pulumi.getter(name="baseInstanceName")
    def base_instance_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroup")
    def instance_group(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="instanceGroupManagerId")
    def instance_group_manager_id(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="instanceLifecyclePolicy")
    def instance_lifecycle_policy(
        self,
    ) -> pulumi.Output[outputs.InstanceGroupManagerInstanceLifecyclePolicy]: ...
    @_builtins.property
    @pulumi.getter(name="listManagedInstancesResults")
    def list_managed_instances_results(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namedPorts")
    def named_ports(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.InstanceGroupManagerNamedPort]]]: ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.InstanceGroupManagerParams]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourcePolicies")
    def resource_policies(
        self,
    ) -> pulumi.Output[Optional[outputs.InstanceGroupManagerResourcePolicies]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="standbyPolicy")
    def standby_policy(
        self,
    ) -> pulumi.Output[outputs.InstanceGroupManagerStandbyPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="statefulDisks")
    def stateful_disks(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.InstanceGroupManagerStatefulDisk]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="statefulExternalIps")
    def stateful_external_ips(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.InstanceGroupManagerStatefulExternalIp]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="statefulInternalIps")
    def stateful_internal_ips(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.InstanceGroupManagerStatefulInternalIp]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceGroupManagerStatus]]: ...
    @_builtins.property
    @pulumi.getter(name="targetPools")
    def target_pools(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="targetSize")
    def target_size(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="targetStoppedSize")
    def target_stopped_size(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="targetSuspendedSize")
    def target_suspended_size(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="updatePolicy")
    def update_policy(
        self,
    ) -> pulumi.Output[outputs.InstanceGroupManagerUpdatePolicy]: ...
    @_builtins.property
    @pulumi.getter
    def versions(
        self,
    ) -> pulumi.Output[Sequence[outputs.InstanceGroupManagerVersion]]: ...
    @_builtins.property
    @pulumi.getter(name="waitForInstances")
    def wait_for_instances(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="waitForInstancesStatus")
    def wait_for_instances_status(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[_builtins.str]: ...
