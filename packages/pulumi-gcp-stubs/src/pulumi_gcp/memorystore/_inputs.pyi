import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "InstanceAutomatedBackupConfigArgs",
    "InstanceAutomatedBackupConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "InstanceCrossInstanceReplicationConfigArgs",
    "InstanceCrossInstanceReplicationConfigArgsDict",
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
    "InstanceDesiredAutoCreatedEndpointArgs",
    "InstanceDesiredAutoCreatedEndpointArgsDict",
    "InstanceDesiredPscAutoConnectionArgs",
    "InstanceDesiredPscAutoConnectionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "InstanceDiscoveryEndpointArgs",
    "InstanceDiscoveryEndpointArgsDict",
    "InstanceEndpointArgs",
    "InstanceEndpointArgsDict",
    "InstanceEndpointConnectionArgs",
    "InstanceEndpointConnectionArgsDict",
    "InstanceEndpointConnectionPscAutoConnectionArgs",
    ...,
    "InstanceGcsSourceArgs",
    "InstanceGcsSourceArgsDict",
    "InstanceMaintenancePolicyArgs",
    "InstanceMaintenancePolicyArgsDict",
    ...,
    ...,
    ...,
    ...,
    "InstanceMaintenanceScheduleArgs",
    "InstanceMaintenanceScheduleArgsDict",
    "InstanceManagedBackupSourceArgs",
    "InstanceManagedBackupSourceArgsDict",
    "InstanceManagedServerCaArgs",
    "InstanceManagedServerCaArgsDict",
    "InstanceManagedServerCaCaCertArgs",
    "InstanceManagedServerCaCaCertArgsDict",
    "InstanceNodeConfigArgs",
    "InstanceNodeConfigArgsDict",
    "InstancePersistenceConfigArgs",
    "InstancePersistenceConfigArgsDict",
    "InstancePersistenceConfigAofConfigArgs",
    "InstancePersistenceConfigAofConfigArgsDict",
    "InstancePersistenceConfigRdbConfigArgs",
    "InstancePersistenceConfigRdbConfigArgsDict",
    "InstancePscAttachmentDetailArgs",
    "InstancePscAttachmentDetailArgsDict",
    "InstancePscAutoConnectionArgs",
    "InstancePscAutoConnectionArgsDict",
    "InstanceStateInfoArgs",
    "InstanceStateInfoArgsDict",
    "InstanceStateInfoUpdateInfoArgs",
    "InstanceStateInfoUpdateInfoArgsDict",
    "InstanceZoneDistributionConfigArgs",
    "InstanceZoneDistributionConfigArgsDict",
]

class InstanceAutomatedBackupConfigArgsDict(TypedDict):
    fixed_frequency_schedule: pulumi.Input[
        InstanceAutomatedBackupConfigFixedFrequencyScheduleArgsDict
    ]
    retention: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceAutomatedBackupConfigArgs:
    def __init__(
        __self__,
        *,
        fixed_frequency_schedule: pulumi.Input[
            InstanceAutomatedBackupConfigFixedFrequencyScheduleArgs
        ],
        retention: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fixedFrequencySchedule")
    def fixed_frequency_schedule(
        self,
    ) -> pulumi.Input[InstanceAutomatedBackupConfigFixedFrequencyScheduleArgs]: ...
    @fixed_frequency_schedule.setter
    def fixed_frequency_schedule(
        self,
        value: pulumi.Input[InstanceAutomatedBackupConfigFixedFrequencyScheduleArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def retention(self) -> pulumi.Input[_builtins.str]: ...
    @retention.setter
    def retention(self, value: pulumi.Input[_builtins.str]): ...

class InstanceAutomatedBackupConfigFixedFrequencyScheduleArgsDict(TypedDict):
    start_time: pulumi.Input[
        InstanceAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgsDict
    ]
    ...

@pulumi.input_type
class InstanceAutomatedBackupConfigFixedFrequencyScheduleArgs:
    def __init__(
        __self__,
        *,
        start_time: pulumi.Input[
            InstanceAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> pulumi.Input[
        InstanceAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgs
    ]: ...
    @start_time.setter
    def start_time(
        self,
        value: pulumi.Input[
            InstanceAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgs
        ],
    ): ...

class InstanceAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgsDict(TypedDict):
    hours: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class InstanceAutomatedBackupConfigFixedFrequencyScheduleStartTimeArgs:
    def __init__(__self__, *, hours: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> pulumi.Input[_builtins.int]: ...
    @hours.setter
    def hours(self, value: pulumi.Input[_builtins.int]): ...

class InstanceCrossInstanceReplicationConfigArgsDict(TypedDict):
    instance_role: NotRequired[pulumi.Input[_builtins.str]]
    memberships: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InstanceCrossInstanceReplicationConfigMembershipArgsDict]
            ]
        ]
    ]
    primary_instance: NotRequired[
        pulumi.Input[InstanceCrossInstanceReplicationConfigPrimaryInstanceArgsDict]
    ]
    secondary_instances: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceCrossInstanceReplicationConfigSecondaryInstanceArgsDict
                ]
            ]
        ]
    ]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceCrossInstanceReplicationConfigArgs:
    def __init__(
        __self__,
        *,
        instance_role: Optional[pulumi.Input[_builtins.str]] = ...,
        memberships: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InstanceCrossInstanceReplicationConfigMembershipArgs]
                ]
            ]
        ] = ...,
        primary_instance: Optional[
            pulumi.Input[InstanceCrossInstanceReplicationConfigPrimaryInstanceArgs]
        ] = ...,
        secondary_instances: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceCrossInstanceReplicationConfigSecondaryInstanceArgs
                    ]
                ]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceRole")
    def instance_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_role.setter
    def instance_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def memberships(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceCrossInstanceReplicationConfigMembershipArgs]]
        ]
    ]: ...
    @memberships.setter
    def memberships(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InstanceCrossInstanceReplicationConfigMembershipArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="primaryInstance")
    def primary_instance(
        self,
    ) -> Optional[
        pulumi.Input[InstanceCrossInstanceReplicationConfigPrimaryInstanceArgs]
    ]: ...
    @primary_instance.setter
    def primary_instance(
        self,
        value: Optional[
            pulumi.Input[InstanceCrossInstanceReplicationConfigPrimaryInstanceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryInstances")
    def secondary_instances(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceCrossInstanceReplicationConfigSecondaryInstanceArgs
                ]
            ]
        ]
    ]: ...
    @secondary_instances.setter
    def secondary_instances(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceCrossInstanceReplicationConfigSecondaryInstanceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceCrossInstanceReplicationConfigMembershipArgsDict(TypedDict):
    primary_instances: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceCrossInstanceReplicationConfigMembershipPrimaryInstanceArgsDict
                ]
            ]
        ]
    ]
    secondary_instances: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceCrossInstanceReplicationConfigMembershipSecondaryInstanceArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class InstanceCrossInstanceReplicationConfigMembershipArgs:
    def __init__(
        __self__,
        *,
        primary_instances: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceCrossInstanceReplicationConfigMembershipPrimaryInstanceArgs
                    ]
                ]
            ]
        ] = ...,
        secondary_instances: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceCrossInstanceReplicationConfigMembershipSecondaryInstanceArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primaryInstances")
    def primary_instances(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceCrossInstanceReplicationConfigMembershipPrimaryInstanceArgs
                ]
            ]
        ]
    ]: ...
    @primary_instances.setter
    def primary_instances(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceCrossInstanceReplicationConfigMembershipPrimaryInstanceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secondaryInstances")
    def secondary_instances(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceCrossInstanceReplicationConfigMembershipSecondaryInstanceArgs
                ]
            ]
        ]
    ]: ...
    @secondary_instances.setter
    def secondary_instances(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceCrossInstanceReplicationConfigMembershipSecondaryInstanceArgs
                    ]
                ]
            ]
        ],
    ): ...

class InstanceCrossInstanceReplicationConfigMembershipPrimaryInstanceArgsDict(
    TypedDict
):
    instance: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceCrossInstanceReplicationConfigMembershipPrimaryInstanceArgs:
    def __init__(
        __self__,
        *,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceCrossInstanceReplicationConfigMembershipSecondaryInstanceArgsDict(
    TypedDict
):
    instance: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceCrossInstanceReplicationConfigMembershipSecondaryInstanceArgs:
    def __init__(
        __self__,
        *,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceCrossInstanceReplicationConfigPrimaryInstanceArgsDict(TypedDict):
    instance: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceCrossInstanceReplicationConfigPrimaryInstanceArgs:
    def __init__(
        __self__,
        *,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceCrossInstanceReplicationConfigSecondaryInstanceArgsDict(TypedDict):
    instance: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceCrossInstanceReplicationConfigSecondaryInstanceArgs:
    def __init__(
        __self__,
        *,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceDesiredAutoCreatedEndpointArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceDesiredAutoCreatedEndpointArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class InstanceDesiredPscAutoConnectionArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceDesiredPscAutoConnectionArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgsDict(TypedDict):
    connections: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointArgs:
    def __init__(
        __self__,
        *,
        connections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connections(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionArgs
                ]
            ]
        ]
    ]: ...
    @connections.setter
    def connections(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionArgs
                    ]
                ]
            ]
        ],
    ): ...

class InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionArgsDict(
    TypedDict
):
    psc_connection: NotRequired[
        pulumi.Input[
            InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionPscConnectionArgsDict
        ]
    ]
    ...

@pulumi.input_type
class InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        psc_connection: Optional[
            pulumi.Input[
                InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionPscConnectionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pscConnection")
    def psc_connection(
        self,
    ) -> Optional[
        pulumi.Input[
            InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionPscConnectionArgs
        ]
    ]: ...
    @psc_connection.setter
    def psc_connection(
        self,
        value: Optional[
            pulumi.Input[
                InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionPscConnectionArgs
            ]
        ],
    ): ...

class InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionPscConnectionArgsDict(
    TypedDict
):
    forwarding_rule: pulumi.Input[_builtins.str]
    ip_address: pulumi.Input[_builtins.str]
    network: pulumi.Input[_builtins.str]
    psc_connection_id: pulumi.Input[_builtins.str]
    service_attachment: pulumi.Input[_builtins.str]
    connection_type: NotRequired[pulumi.Input[_builtins.str]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    psc_connection_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceDesiredUserCreatedEndpointsDesiredUserCreatedEndpointConnectionPscConnectionArgs:
    def __init__(
        __self__,
        *,
        forwarding_rule: pulumi.Input[_builtins.str],
        ip_address: pulumi.Input[_builtins.str],
        network: pulumi.Input[_builtins.str],
        psc_connection_id: pulumi.Input[_builtins.str],
        service_attachment: pulumi.Input[_builtins.str],
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_connection_status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> pulumi.Input[_builtins.str]: ...
    @forwarding_rule.setter
    def forwarding_rule(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Input[_builtins.str]: ...
    @ip_address.setter
    def ip_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> pulumi.Input[_builtins.str]: ...
    @psc_connection_id.setter
    def psc_connection_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> pulumi.Input[_builtins.str]: ...
    @service_attachment.setter
    def service_attachment(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_connection_status.setter
    def psc_connection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceDiscoveryEndpointArgsDict(TypedDict):
    address: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceDiscoveryEndpointArgs:
    def __init__(
        __self__,
        *,
        address: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceEndpointArgsDict(TypedDict):
    connections: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InstanceEndpointConnectionArgsDict]]]
    ]
    ...

@pulumi.input_type
class InstanceEndpointArgs:
    def __init__(
        __self__,
        *,
        connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceEndpointConnectionArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceEndpointConnectionArgs]]]
    ]: ...
    @connections.setter
    def connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceEndpointConnectionArgs]]]
        ],
    ): ...

class InstanceEndpointConnectionArgsDict(TypedDict):
    psc_auto_connection: NotRequired[
        pulumi.Input[InstanceEndpointConnectionPscAutoConnectionArgsDict]
    ]
    ...

@pulumi.input_type
class InstanceEndpointConnectionArgs:
    def __init__(
        __self__,
        *,
        psc_auto_connection: Optional[
            pulumi.Input[InstanceEndpointConnectionPscAutoConnectionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pscAutoConnection")
    def psc_auto_connection(
        self,
    ) -> Optional[pulumi.Input[InstanceEndpointConnectionPscAutoConnectionArgs]]: ...
    @psc_auto_connection.setter
    def psc_auto_connection(
        self,
        value: Optional[pulumi.Input[InstanceEndpointConnectionPscAutoConnectionArgs]],
    ): ...

class InstanceEndpointConnectionPscAutoConnectionArgsDict(TypedDict):
    connection_type: NotRequired[pulumi.Input[_builtins.str]]
    forwarding_rule: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    psc_connection_id: NotRequired[pulumi.Input[_builtins.str]]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceEndpointConnectionPscAutoConnectionArgs:
    def __init__(
        __self__,
        *,
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        forwarding_rule: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @forwarding_rule.setter
    def forwarding_rule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_connection_id.setter
    def psc_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceGcsSourceArgsDict(TypedDict):
    uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class InstanceGcsSourceArgs:
    def __init__(
        __self__, *, uris: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uris(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @uris.setter
    def uris(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class InstanceMaintenancePolicyArgsDict(TypedDict):
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    weekly_maintenance_windows: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class InstanceMaintenancePolicyArgs:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        weekly_maintenance_windows: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklyMaintenanceWindows")
    def weekly_maintenance_windows(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs]]
        ]
    ]: ...
    @weekly_maintenance_windows.setter
    def weekly_maintenance_windows(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs]
                ]
            ]
        ],
    ): ...

class InstanceMaintenancePolicyWeeklyMaintenanceWindowArgsDict(TypedDict):
    day: pulumi.Input[_builtins.str]
    start_time: pulumi.Input[
        InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgsDict
    ]
    duration: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowArgs:
    def __init__(
        __self__,
        *,
        day: pulumi.Input[_builtins.str],
        start_time: pulumi.Input[
            InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs
        ],
        duration: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> pulumi.Input[_builtins.str]: ...
    @day.setter
    def day(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(
        self,
    ) -> pulumi.Input[
        InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs
    ]: ...
    @start_time.setter
    def start_time(
        self,
        value: pulumi.Input[
            InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @duration.setter
    def duration(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgsDict(TypedDict):
    hours: NotRequired[pulumi.Input[_builtins.int]]
    minutes: NotRequired[pulumi.Input[_builtins.int]]
    nanos: NotRequired[pulumi.Input[_builtins.int]]
    seconds: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceMaintenancePolicyWeeklyMaintenanceWindowStartTimeArgs:
    def __init__(
        __self__,
        *,
        hours: Optional[pulumi.Input[_builtins.int]] = ...,
        minutes: Optional[pulumi.Input[_builtins.int]] = ...,
        nanos: Optional[pulumi.Input[_builtins.int]] = ...,
        seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @seconds.setter
    def seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceMaintenanceScheduleArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    schedule_deadline_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceMaintenanceScheduleArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_deadline_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleDeadlineTime")
    def schedule_deadline_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_deadline_time.setter
    def schedule_deadline_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceManagedBackupSourceArgsDict(TypedDict):
    backup: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class InstanceManagedBackupSourceArgs:
    def __init__(__self__, *, backup: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> pulumi.Input[_builtins.str]: ...
    @backup.setter
    def backup(self, value: pulumi.Input[_builtins.str]): ...

class InstanceManagedServerCaArgsDict(TypedDict):
    ca_certs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InstanceManagedServerCaCaCertArgsDict]]]
    ]
    ...

@pulumi.input_type
class InstanceManagedServerCaArgs:
    def __init__(
        __self__,
        *,
        ca_certs: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceManagedServerCaCaCertArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceManagedServerCaCaCertArgs]]]
    ]: ...
    @ca_certs.setter
    def ca_certs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceManagedServerCaCaCertArgs]]]
        ],
    ): ...

class InstanceManagedServerCaCaCertArgsDict(TypedDict):
    certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class InstanceManagedServerCaCaCertArgs:
    def __init__(
        __self__,
        *,
        certificates: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificates(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @certificates.setter
    def certificates(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class InstanceNodeConfigArgsDict(TypedDict):
    size_gb: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class InstanceNodeConfigArgs:
    def __init__(
        __self__, *, size_gb: Optional[pulumi.Input[_builtins.float]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @size_gb.setter
    def size_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class InstancePersistenceConfigArgsDict(TypedDict):
    aof_config: NotRequired[pulumi.Input[InstancePersistenceConfigAofConfigArgsDict]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    rdb_config: NotRequired[pulumi.Input[InstancePersistenceConfigRdbConfigArgsDict]]
    ...

@pulumi.input_type
class InstancePersistenceConfigArgs:
    def __init__(
        __self__,
        *,
        aof_config: Optional[
            pulumi.Input[InstancePersistenceConfigAofConfigArgs]
        ] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        rdb_config: Optional[
            pulumi.Input[InstancePersistenceConfigRdbConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="aofConfig")
    def aof_config(
        self,
    ) -> Optional[pulumi.Input[InstancePersistenceConfigAofConfigArgs]]: ...
    @aof_config.setter
    def aof_config(
        self, value: Optional[pulumi.Input[InstancePersistenceConfigAofConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rdbConfig")
    def rdb_config(
        self,
    ) -> Optional[pulumi.Input[InstancePersistenceConfigRdbConfigArgs]]: ...
    @rdb_config.setter
    def rdb_config(
        self, value: Optional[pulumi.Input[InstancePersistenceConfigRdbConfigArgs]]
    ): ...

class InstancePersistenceConfigAofConfigArgsDict(TypedDict):
    append_fsync: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstancePersistenceConfigAofConfigArgs:
    def __init__(
        __self__, *, append_fsync: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appendFsync")
    def append_fsync(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @append_fsync.setter
    def append_fsync(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstancePersistenceConfigRdbConfigArgsDict(TypedDict):
    rdb_snapshot_period: NotRequired[pulumi.Input[_builtins.str]]
    rdb_snapshot_start_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstancePersistenceConfigRdbConfigArgs:
    def __init__(
        __self__,
        *,
        rdb_snapshot_period: Optional[pulumi.Input[_builtins.str]] = ...,
        rdb_snapshot_start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotPeriod")
    def rdb_snapshot_period(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdb_snapshot_period.setter
    def rdb_snapshot_period(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rdbSnapshotStartTime")
    def rdb_snapshot_start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rdb_snapshot_start_time.setter
    def rdb_snapshot_start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstancePscAttachmentDetailArgsDict(TypedDict):
    connection_type: NotRequired[pulumi.Input[_builtins.str]]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstancePscAttachmentDetailArgs:
    def __init__(
        __self__,
        *,
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstancePscAutoConnectionArgsDict(TypedDict):
    connection_type: NotRequired[pulumi.Input[_builtins.str]]
    forwarding_rule: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    psc_connection_id: NotRequired[pulumi.Input[_builtins.str]]
    psc_connection_status: NotRequired[pulumi.Input[_builtins.str]]
    service_attachment: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstancePscAutoConnectionArgs:
    def __init__(
        __self__,
        *,
        connection_type: Optional[pulumi.Input[_builtins.str]] = ...,
        forwarding_rule: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_connection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        psc_connection_status: Optional[pulumi.Input[_builtins.str]] = ...,
        service_attachment: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionType")
    def connection_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_type.setter
    def connection_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @forwarding_rule.setter
    def forwarding_rule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionId")
    def psc_connection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_connection_id.setter
    def psc_connection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pscConnectionStatus")
    def psc_connection_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @psc_connection_status.setter
    def psc_connection_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAttachment")
    def service_attachment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_attachment.setter
    def service_attachment(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InstanceStateInfoArgsDict(TypedDict):
    update_infos: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InstanceStateInfoUpdateInfoArgsDict]]]
    ]
    ...

@pulumi.input_type
class InstanceStateInfoArgs:
    def __init__(
        __self__,
        *,
        update_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceStateInfoUpdateInfoArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="updateInfos")
    def update_infos(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InstanceStateInfoUpdateInfoArgs]]]
    ]: ...
    @update_infos.setter
    def update_infos(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InstanceStateInfoUpdateInfoArgs]]]
        ],
    ): ...

class InstanceStateInfoUpdateInfoArgsDict(TypedDict):
    target_engine_version: NotRequired[pulumi.Input[_builtins.str]]
    target_node_type: NotRequired[pulumi.Input[_builtins.str]]
    target_replica_count: NotRequired[pulumi.Input[_builtins.int]]
    target_shard_count: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class InstanceStateInfoUpdateInfoArgs:
    def __init__(
        __self__,
        *,
        target_engine_version: Optional[pulumi.Input[_builtins.str]] = ...,
        target_node_type: Optional[pulumi.Input[_builtins.str]] = ...,
        target_replica_count: Optional[pulumi.Input[_builtins.int]] = ...,
        target_shard_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetEngineVersion")
    def target_engine_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_engine_version.setter
    def target_engine_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetNodeType")
    def target_node_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_node_type.setter
    def target_node_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetReplicaCount")
    def target_replica_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_replica_count.setter
    def target_replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="targetShardCount")
    def target_shard_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @target_shard_count.setter
    def target_shard_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class InstanceZoneDistributionConfigArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class InstanceZoneDistributionConfigArgs:
    def __init__(
        __self__,
        *,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        zone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
