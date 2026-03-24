import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkstationConfigArgs", "WorkstationConfig"]

@pulumi.input_type
class WorkstationConfigArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        workstation_cluster_id: pulumi.Input[_builtins.str],
        workstation_config_id: pulumi.Input[_builtins.str],
        allowed_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigAllowedPortArgs]]]
        ] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        container: Optional[pulumi.Input[WorkstationConfigContainerArgs]] = ...,
        disable_tcp_connections: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_audit_agent: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key: Optional[
            pulumi.Input[WorkstationConfigEncryptionKeyArgs]
        ] = ...,
        ephemeral_directories: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkstationConfigEphemeralDirectoryArgs]]
            ]
        ] = ...,
        host: Optional[pulumi.Input[WorkstationConfigHostArgs]] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        max_usable_workstations: Optional[pulumi.Input[_builtins.int]] = ...,
        persistent_directories: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkstationConfigPersistentDirectoryArgs]]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        readiness_checks: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigReadinessCheckArgs]]]
        ] = ...,
        replica_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        running_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workstationClusterId")
    def workstation_cluster_id(self) -> pulumi.Input[_builtins.str]: ...
    @workstation_cluster_id.setter
    def workstation_cluster_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workstationConfigId")
    def workstation_config_id(self) -> pulumi.Input[_builtins.str]: ...
    @workstation_config_id.setter
    def workstation_config_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowedPorts")
    def allowed_ports(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkstationConfigAllowedPortArgs]]]
    ]: ...
    @allowed_ports.setter
    def allowed_ports(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigAllowedPortArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[pulumi.Input[WorkstationConfigContainerArgs]]: ...
    @container.setter
    def container(
        self, value: Optional[pulumi.Input[WorkstationConfigContainerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableTcpConnections")
    def disable_tcp_connections(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_tcp_connections.setter
    def disable_tcp_connections(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAuditAgent")
    def enable_audit_agent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_audit_agent.setter
    def enable_audit_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(
        self,
    ) -> Optional[pulumi.Input[WorkstationConfigEncryptionKeyArgs]]: ...
    @encryption_key.setter
    def encryption_key(
        self, value: Optional[pulumi.Input[WorkstationConfigEncryptionKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralDirectories")
    def ephemeral_directories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkstationConfigEphemeralDirectoryArgs]]]
    ]: ...
    @ephemeral_directories.setter
    def ephemeral_directories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkstationConfigEphemeralDirectoryArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[WorkstationConfigHostArgs]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[WorkstationConfigHostArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxUsableWorkstations")
    def max_usable_workstations(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_usable_workstations.setter
    def max_usable_workstations(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="persistentDirectories")
    def persistent_directories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkstationConfigPersistentDirectoryArgs]]]
    ]: ...
    @persistent_directories.setter
    def persistent_directories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkstationConfigPersistentDirectoryArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="readinessChecks")
    def readiness_checks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkstationConfigReadinessCheckArgs]]]
    ]: ...
    @readiness_checks.setter
    def readiness_checks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigReadinessCheckArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @replica_zones.setter
    def replica_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runningTimeout")
    def running_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @running_timeout.setter
    def running_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _WorkstationConfigState:
    def __init__(
        __self__,
        *,
        allowed_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigAllowedPortArgs]]]
        ] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigConditionArgs]]]
        ] = ...,
        container: Optional[pulumi.Input[WorkstationConfigContainerArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        degraded: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_tcp_connections: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_audit_agent: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key: Optional[
            pulumi.Input[WorkstationConfigEncryptionKeyArgs]
        ] = ...,
        ephemeral_directories: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkstationConfigEphemeralDirectoryArgs]]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        host: Optional[pulumi.Input[WorkstationConfigHostArgs]] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_usable_workstations: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        persistent_directories: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkstationConfigPersistentDirectoryArgs]]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        readiness_checks: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigReadinessCheckArgs]]]
        ] = ...,
        replica_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        running_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        workstation_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workstation_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowedPorts")
    def allowed_ports(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkstationConfigAllowedPortArgs]]]
    ]: ...
    @allowed_ports.setter
    def allowed_ports(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigAllowedPortArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkstationConfigConditionArgs]]]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[pulumi.Input[WorkstationConfigContainerArgs]]: ...
    @container.setter
    def container(
        self, value: Optional[pulumi.Input[WorkstationConfigContainerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def degraded(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @degraded.setter
    def degraded(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="disableTcpConnections")
    def disable_tcp_connections(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_tcp_connections.setter
    def disable_tcp_connections(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_annotations.setter
    def effective_annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAuditAgent")
    def enable_audit_agent(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_audit_agent.setter
    def enable_audit_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(
        self,
    ) -> Optional[pulumi.Input[WorkstationConfigEncryptionKeyArgs]]: ...
    @encryption_key.setter
    def encryption_key(
        self, value: Optional[pulumi.Input[WorkstationConfigEncryptionKeyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralDirectories")
    def ephemeral_directories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkstationConfigEphemeralDirectoryArgs]]]
    ]: ...
    @ephemeral_directories.setter
    def ephemeral_directories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkstationConfigEphemeralDirectoryArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[WorkstationConfigHostArgs]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[WorkstationConfigHostArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxUsableWorkstations")
    def max_usable_workstations(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_usable_workstations.setter
    def max_usable_workstations(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="persistentDirectories")
    def persistent_directories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkstationConfigPersistentDirectoryArgs]]]
    ]: ...
    @persistent_directories.setter
    def persistent_directories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkstationConfigPersistentDirectoryArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readinessChecks")
    def readiness_checks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkstationConfigReadinessCheckArgs]]]
    ]: ...
    @readiness_checks.setter
    def readiness_checks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkstationConfigReadinessCheckArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @replica_zones.setter
    def replica_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runningTimeout")
    def running_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @running_timeout.setter
    def running_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workstationClusterId")
    def workstation_cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workstation_cluster_id.setter
    def workstation_cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workstationConfigId")
    def workstation_config_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workstation_config_id.setter
    def workstation_config_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class WorkstationConfig(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        allowed_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkstationConfigAllowedPortArgs,
                            WorkstationConfigAllowedPortArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        container: Optional[
            pulumi.Input[
                Union[
                    WorkstationConfigContainerArgs, WorkstationConfigContainerArgsDict
                ]
            ]
        ] = ...,
        disable_tcp_connections: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_audit_agent: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key: Optional[
            pulumi.Input[
                Union[
                    WorkstationConfigEncryptionKeyArgs,
                    WorkstationConfigEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        ephemeral_directories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkstationConfigEphemeralDirectoryArgs,
                            WorkstationConfigEphemeralDirectoryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        host: Optional[
            pulumi.Input[
                Union[WorkstationConfigHostArgs, WorkstationConfigHostArgsDict]
            ]
        ] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_usable_workstations: Optional[pulumi.Input[_builtins.int]] = ...,
        persistent_directories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkstationConfigPersistentDirectoryArgs,
                            WorkstationConfigPersistentDirectoryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        readiness_checks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkstationConfigReadinessCheckArgs,
                            WorkstationConfigReadinessCheckArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        replica_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        running_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        workstation_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workstation_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkstationConfigArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        allowed_ports: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkstationConfigAllowedPortArgs,
                            WorkstationConfigAllowedPortArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkstationConfigConditionArgs,
                            WorkstationConfigConditionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        container: Optional[
            pulumi.Input[
                Union[
                    WorkstationConfigContainerArgs, WorkstationConfigContainerArgsDict
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        degraded: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_tcp_connections: Optional[pulumi.Input[_builtins.bool]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_audit_agent: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption_key: Optional[
            pulumi.Input[
                Union[
                    WorkstationConfigEncryptionKeyArgs,
                    WorkstationConfigEncryptionKeyArgsDict,
                ]
            ]
        ] = ...,
        ephemeral_directories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkstationConfigEphemeralDirectoryArgs,
                            WorkstationConfigEphemeralDirectoryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        host: Optional[
            pulumi.Input[
                Union[WorkstationConfigHostArgs, WorkstationConfigHostArgsDict]
            ]
        ] = ...,
        idle_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        max_usable_workstations: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        persistent_directories: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkstationConfigPersistentDirectoryArgs,
                            WorkstationConfigPersistentDirectoryArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        readiness_checks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkstationConfigReadinessCheckArgs,
                            WorkstationConfigReadinessCheckArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        replica_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        running_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        workstation_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        workstation_config_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> WorkstationConfig: ...
    @_builtins.property
    @pulumi.getter(name="allowedPorts")
    def allowed_ports(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkstationConfigAllowedPort]]: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkstationConfigCondition]]: ...
    @_builtins.property
    @pulumi.getter
    def container(self) -> pulumi.Output[outputs.WorkstationConfigContainer]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def degraded(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableTcpConnections")
    def disable_tcp_connections(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableAuditAgent")
    def enable_audit_agent(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkstationConfigEncryptionKey]]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralDirectories")
    def ephemeral_directories(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkstationConfigEphemeralDirectory]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Output[outputs.WorkstationConfigHost]: ...
    @_builtins.property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxUsableWorkstations")
    def max_usable_workstations(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="persistentDirectories")
    def persistent_directories(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkstationConfigPersistentDirectory]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="readinessChecks")
    def readiness_checks(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.WorkstationConfigReadinessCheck]]]: ...
    @_builtins.property
    @pulumi.getter(name="replicaZones")
    def replica_zones(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="runningTimeout")
    def running_timeout(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workstationClusterId")
    def workstation_cluster_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workstationConfigId")
    def workstation_config_id(self) -> pulumi.Output[_builtins.str]: ...
