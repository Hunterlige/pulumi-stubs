import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterAuthorizationArgs",
    "ClusterAuthorizationArgsDict",
    "ClusterAuthorizationAdminUsersArgs",
    "ClusterAuthorizationAdminUsersArgsDict",
    "ClusterControlPlaneArgs",
    "ClusterControlPlaneArgsDict",
    "ClusterControlPlaneEncryptionArgs",
    "ClusterControlPlaneEncryptionArgsDict",
    "ClusterControlPlaneEncryptionKmsStatusArgs",
    "ClusterControlPlaneEncryptionKmsStatusArgsDict",
    "ClusterControlPlaneLocalArgs",
    "ClusterControlPlaneLocalArgsDict",
    "ClusterControlPlaneRemoteArgs",
    "ClusterControlPlaneRemoteArgsDict",
    "ClusterFleetArgs",
    "ClusterFleetArgsDict",
    "ClusterMaintenanceEventArgs",
    "ClusterMaintenanceEventArgsDict",
    "ClusterMaintenancePolicyArgs",
    "ClusterMaintenancePolicyArgsDict",
    "ClusterMaintenancePolicyMaintenanceExclusionArgs",
    ...,
    ...,
    ...,
    "ClusterMaintenancePolicyWindowArgs",
    "ClusterMaintenancePolicyWindowArgsDict",
    "ClusterMaintenancePolicyWindowRecurringWindowArgs",
    ...,
    ...,
    ...,
    "ClusterNetworkingArgs",
    "ClusterNetworkingArgsDict",
    "ClusterSystemAddonsConfigArgs",
    "ClusterSystemAddonsConfigArgsDict",
    "ClusterSystemAddonsConfigIngressArgs",
    "ClusterSystemAddonsConfigIngressArgsDict",
    "NodePoolLocalDiskEncryptionArgs",
    "NodePoolLocalDiskEncryptionArgsDict",
    "NodePoolNodeConfigArgs",
    "NodePoolNodeConfigArgsDict",
    "VpnConnectionDetailArgs",
    "VpnConnectionDetailArgsDict",
    "VpnConnectionDetailCloudRouterArgs",
    "VpnConnectionDetailCloudRouterArgsDict",
    "VpnConnectionDetailCloudVpnArgs",
    "VpnConnectionDetailCloudVpnArgsDict",
    "VpnConnectionVpcProjectArgs",
    "VpnConnectionVpcProjectArgsDict",
]

class ClusterAuthorizationArgsDict(TypedDict):
    admin_users: pulumi.Input[ClusterAuthorizationAdminUsersArgsDict]
    ...

@pulumi.input_type
class ClusterAuthorizationArgs:
    def __init__(
        __self__, *, admin_users: pulumi.Input[ClusterAuthorizationAdminUsersArgs]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adminUsers")
    def admin_users(self) -> pulumi.Input[ClusterAuthorizationAdminUsersArgs]: ...
    @admin_users.setter
    def admin_users(self, value: pulumi.Input[ClusterAuthorizationAdminUsersArgs]): ...

class ClusterAuthorizationAdminUsersArgsDict(TypedDict):
    username: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ClusterAuthorizationAdminUsersArgs:
    def __init__(__self__, *, username: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class ClusterControlPlaneArgsDict(TypedDict):
    local: NotRequired[pulumi.Input[ClusterControlPlaneLocalArgsDict]]
    remote: NotRequired[pulumi.Input[ClusterControlPlaneRemoteArgsDict]]
    ...

@pulumi.input_type
class ClusterControlPlaneArgs:
    def __init__(
        __self__,
        *,
        local: Optional[pulumi.Input[ClusterControlPlaneLocalArgs]] = ...,
        remote: Optional[pulumi.Input[ClusterControlPlaneRemoteArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def local(self) -> Optional[pulumi.Input[ClusterControlPlaneLocalArgs]]: ...
    @local.setter
    def local(self, value: Optional[pulumi.Input[ClusterControlPlaneLocalArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def remote(self) -> Optional[pulumi.Input[ClusterControlPlaneRemoteArgs]]: ...
    @remote.setter
    def remote(self, value: Optional[pulumi.Input[ClusterControlPlaneRemoteArgs]]): ...

class ClusterControlPlaneEncryptionArgsDict(TypedDict):
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_active_version: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_state: NotRequired[pulumi.Input[_builtins.str]]
    kms_statuses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterControlPlaneEncryptionKmsStatusArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class ClusterControlPlaneEncryptionArgs:
    def __init__(
        __self__,
        *,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_active_version: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_state: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterControlPlaneEncryptionKmsStatusArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyActiveVersion")
    def kms_key_active_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_active_version.setter
    def kms_key_active_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyState")
    def kms_key_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_state.setter
    def kms_key_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsStatuses")
    def kms_statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterControlPlaneEncryptionKmsStatusArgs]]]
    ]: ...
    @kms_statuses.setter
    def kms_statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterControlPlaneEncryptionKmsStatusArgs]]
            ]
        ],
    ): ...

class ClusterControlPlaneEncryptionKmsStatusArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterControlPlaneEncryptionKmsStatusArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterControlPlaneLocalArgsDict(TypedDict):
    machine_filter: NotRequired[pulumi.Input[_builtins.str]]
    node_count: NotRequired[pulumi.Input[_builtins.int]]
    node_location: NotRequired[pulumi.Input[_builtins.str]]
    shared_deployment_policy: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterControlPlaneLocalArgs:
    def __init__(
        __self__,
        *,
        machine_filter: Optional[pulumi.Input[_builtins.str]] = ...,
        node_count: Optional[pulumi.Input[_builtins.int]] = ...,
        node_location: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_deployment_policy: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineFilter")
    def machine_filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_filter.setter
    def machine_filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeLocation")
    def node_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_location.setter
    def node_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedDeploymentPolicy")
    def shared_deployment_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @shared_deployment_policy.setter
    def shared_deployment_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ClusterControlPlaneRemoteArgsDict(TypedDict):
    node_location: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterControlPlaneRemoteArgs:
    def __init__(
        __self__, *, node_location: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeLocation")
    def node_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @node_location.setter
    def node_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterFleetArgsDict(TypedDict):
    project: pulumi.Input[_builtins.str]
    membership: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterFleetArgs:
    def __init__(
        __self__,
        *,
        project: pulumi.Input[_builtins.str],
        membership: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Input[_builtins.str]: ...
    @project.setter
    def project(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def membership(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @membership.setter
    def membership(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMaintenanceEventArgsDict(TypedDict):
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    operation: NotRequired[pulumi.Input[_builtins.str]]
    schedule: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    target_version: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    uuid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterMaintenanceEventArgs:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        operation: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        target_version: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        uuid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operation.setter
    def operation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetVersion")
    def target_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_version.setter
    def target_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMaintenancePolicyArgsDict(TypedDict):
    window: pulumi.Input[ClusterMaintenancePolicyWindowArgsDict]
    maintenance_exclusions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class ClusterMaintenancePolicyArgs:
    def __init__(
        __self__,
        *,
        window: pulumi.Input[ClusterMaintenancePolicyWindowArgs],
        maintenance_exclusions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def window(self) -> pulumi.Input[ClusterMaintenancePolicyWindowArgs]: ...
    @window.setter
    def window(self, value: pulumi.Input[ClusterMaintenancePolicyWindowArgs]): ...
    @_builtins.property
    @pulumi.getter(name="maintenanceExclusions")
    def maintenance_exclusions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionArgs]]
        ]
    ]: ...
    @maintenance_exclusions.setter
    def maintenance_exclusions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionArgs]]
            ]
        ],
    ): ...

class ClusterMaintenancePolicyMaintenanceExclusionArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    window: NotRequired[
        pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionWindowArgsDict]
    ]
    ...

@pulumi.input_type
class ClusterMaintenancePolicyMaintenanceExclusionArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        window: Optional[
            pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionWindowArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def window(
        self,
    ) -> Optional[
        pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionWindowArgs]
    ]: ...
    @window.setter
    def window(
        self,
        value: Optional[
            pulumi.Input[ClusterMaintenancePolicyMaintenanceExclusionWindowArgs]
        ],
    ): ...

class ClusterMaintenancePolicyMaintenanceExclusionWindowArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterMaintenancePolicyMaintenanceExclusionWindowArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterMaintenancePolicyWindowArgsDict(TypedDict):
    recurring_window: pulumi.Input[
        ClusterMaintenancePolicyWindowRecurringWindowArgsDict
    ]
    ...

@pulumi.input_type
class ClusterMaintenancePolicyWindowArgs:
    def __init__(
        __self__,
        *,
        recurring_window: pulumi.Input[
            ClusterMaintenancePolicyWindowRecurringWindowArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recurringWindow")
    def recurring_window(
        self,
    ) -> pulumi.Input[ClusterMaintenancePolicyWindowRecurringWindowArgs]: ...
    @recurring_window.setter
    def recurring_window(
        self, value: pulumi.Input[ClusterMaintenancePolicyWindowRecurringWindowArgs]
    ): ...

class ClusterMaintenancePolicyWindowRecurringWindowArgsDict(TypedDict):
    recurrence: NotRequired[pulumi.Input[_builtins.str]]
    window: NotRequired[
        pulumi.Input[ClusterMaintenancePolicyWindowRecurringWindowWindowArgsDict]
    ]
    ...

@pulumi.input_type
class ClusterMaintenancePolicyWindowRecurringWindowArgs:
    def __init__(
        __self__,
        *,
        recurrence: Optional[pulumi.Input[_builtins.str]] = ...,
        window: Optional[
            pulumi.Input[ClusterMaintenancePolicyWindowRecurringWindowWindowArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def window(
        self,
    ) -> Optional[
        pulumi.Input[ClusterMaintenancePolicyWindowRecurringWindowWindowArgs]
    ]: ...
    @window.setter
    def window(
        self,
        value: Optional[
            pulumi.Input[ClusterMaintenancePolicyWindowRecurringWindowWindowArgs]
        ],
    ): ...

class ClusterMaintenancePolicyWindowRecurringWindowWindowArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterMaintenancePolicyWindowRecurringWindowWindowArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNetworkingArgsDict(TypedDict):
    cluster_ipv4_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    services_ipv4_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    cluster_ipv6_cidr_blocks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    network_type: NotRequired[pulumi.Input[_builtins.str]]
    services_ipv6_cidr_blocks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class ClusterNetworkingArgs:
    def __init__(
        __self__,
        *,
        cluster_ipv4_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        services_ipv4_cidr_blocks: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        cluster_ipv6_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        services_ipv6_cidr_blocks: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterIpv4CidrBlocks")
    def cluster_ipv4_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @cluster_ipv4_cidr_blocks.setter
    def cluster_ipv4_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="servicesIpv4CidrBlocks")
    def services_ipv4_cidr_blocks(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @services_ipv4_cidr_blocks.setter
    def services_ipv4_cidr_blocks(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clusterIpv6CidrBlocks")
    def cluster_ipv6_cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cluster_ipv6_cidr_blocks.setter
    def cluster_ipv6_cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="servicesIpv6CidrBlocks")
    def services_ipv6_cidr_blocks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @services_ipv6_cidr_blocks.setter
    def services_ipv6_cidr_blocks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterSystemAddonsConfigArgsDict(TypedDict):
    ingress: NotRequired[pulumi.Input[ClusterSystemAddonsConfigIngressArgsDict]]
    ...

@pulumi.input_type
class ClusterSystemAddonsConfigArgs:
    def __init__(
        __self__,
        *,
        ingress: Optional[pulumi.Input[ClusterSystemAddonsConfigIngressArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ingress(
        self,
    ) -> Optional[pulumi.Input[ClusterSystemAddonsConfigIngressArgs]]: ...
    @ingress.setter
    def ingress(
        self, value: Optional[pulumi.Input[ClusterSystemAddonsConfigIngressArgs]]
    ): ...

class ClusterSystemAddonsConfigIngressArgsDict(TypedDict):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ipv4_vip: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClusterSystemAddonsConfigIngressArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ipv4_vip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ipv4Vip")
    def ipv4_vip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipv4_vip.setter
    def ipv4_vip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolLocalDiskEncryptionArgsDict(TypedDict):
    kms_key: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_active_version: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class NodePoolLocalDiskEncryptionArgs:
    def __init__(
        __self__,
        *,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_active_version: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyActiveVersion")
    def kms_key_active_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_active_version.setter
    def kms_key_active_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyState")
    def kms_key_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_state.setter
    def kms_key_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NodePoolNodeConfigArgsDict(TypedDict):
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class NodePoolNodeConfigArgs:
    def __init__(
        __self__,
        *,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class VpnConnectionDetailArgsDict(TypedDict):
    cloud_routers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VpnConnectionDetailCloudRouterArgsDict]]]
    ]
    cloud_vpns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VpnConnectionDetailCloudVpnArgsDict]]]
    ]
    error: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class VpnConnectionDetailArgs:
    def __init__(
        __self__,
        *,
        cloud_routers: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpnConnectionDetailCloudRouterArgs]]]
        ] = ...,
        cloud_vpns: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpnConnectionDetailCloudVpnArgs]]]
        ] = ...,
        error: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudRouters")
    def cloud_routers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VpnConnectionDetailCloudRouterArgs]]]
    ]: ...
    @cloud_routers.setter
    def cloud_routers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpnConnectionDetailCloudRouterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudVpns")
    def cloud_vpns(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[VpnConnectionDetailCloudVpnArgs]]]
    ]: ...
    @cloud_vpns.setter
    def cloud_vpns(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[VpnConnectionDetailCloudVpnArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @error.setter
    def error(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VpnConnectionDetailCloudRouterArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class VpnConnectionDetailCloudRouterArgs:
    def __init__(
        __self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VpnConnectionDetailCloudVpnArgsDict(TypedDict):
    gateway: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class VpnConnectionDetailCloudVpnArgs:
    def __init__(
        __self__, *, gateway: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class VpnConnectionVpcProjectArgsDict(TypedDict):
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class VpnConnectionVpcProjectArgs:
    def __init__(
        __self__, *, project_id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
