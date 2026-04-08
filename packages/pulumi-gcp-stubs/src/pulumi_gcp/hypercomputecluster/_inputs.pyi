import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterComputeResourceArgs",
    "ClusterComputeResourceArgsDict",
    "ClusterComputeResourceConfigArgs",
    "ClusterComputeResourceConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ClusterComputeResourceConfigNewSpotInstancesArgs",
    ...,
    "ClusterNetworkResourceArgs",
    "ClusterNetworkResourceArgsDict",
    "ClusterNetworkResourceConfigArgs",
    "ClusterNetworkResourceConfigArgsDict",
    "ClusterNetworkResourceConfigExistingNetworkArgs",
    ...,
    "ClusterNetworkResourceConfigNewNetworkArgs",
    "ClusterNetworkResourceConfigNewNetworkArgsDict",
    "ClusterNetworkResourceNetworkArgs",
    "ClusterNetworkResourceNetworkArgsDict",
    "ClusterOrchestratorArgs",
    "ClusterOrchestratorArgsDict",
    "ClusterOrchestratorSlurmArgs",
    "ClusterOrchestratorSlurmArgsDict",
    "ClusterOrchestratorSlurmLoginNodesArgs",
    "ClusterOrchestratorSlurmLoginNodesArgsDict",
    "ClusterOrchestratorSlurmLoginNodesBootDiskArgs",
    "ClusterOrchestratorSlurmLoginNodesBootDiskArgsDict",
    "ClusterOrchestratorSlurmLoginNodesInstanceArgs",
    "ClusterOrchestratorSlurmLoginNodesInstanceArgsDict",
    ...,
    ...,
    "ClusterOrchestratorSlurmNodeSetArgs",
    "ClusterOrchestratorSlurmNodeSetArgsDict",
    "ClusterOrchestratorSlurmNodeSetComputeInstanceArgs",
    ...,
    ...,
    ...,
    "ClusterOrchestratorSlurmNodeSetStorageConfigArgs",
    ...,
    "ClusterOrchestratorSlurmPartitionArgs",
    "ClusterOrchestratorSlurmPartitionArgsDict",
    "ClusterStorageResourceArgs",
    "ClusterStorageResourceArgsDict",
    "ClusterStorageResourceBucketArgs",
    "ClusterStorageResourceBucketArgsDict",
    "ClusterStorageResourceConfigArgs",
    "ClusterStorageResourceConfigArgsDict",
    "ClusterStorageResourceConfigExistingBucketArgs",
    "ClusterStorageResourceConfigExistingBucketArgsDict",
    "ClusterStorageResourceConfigExistingFilestoreArgs",
    ...,
    "ClusterStorageResourceConfigExistingLustreArgs",
    "ClusterStorageResourceConfigExistingLustreArgsDict",
    "ClusterStorageResourceConfigNewBucketArgs",
    "ClusterStorageResourceConfigNewBucketArgsDict",
    "ClusterStorageResourceConfigNewBucketAutoclassArgs",
    ...,
    ...,
    ...,
    "ClusterStorageResourceConfigNewFilestoreArgs",
    "ClusterStorageResourceConfigNewFilestoreArgsDict",
    ...,
    ...,
    "ClusterStorageResourceConfigNewLustreArgs",
    "ClusterStorageResourceConfigNewLustreArgsDict",
    "ClusterStorageResourceFilestoreArgs",
    "ClusterStorageResourceFilestoreArgsDict",
    "ClusterStorageResourceLustreArgs",
    "ClusterStorageResourceLustreArgsDict",
]

class ClusterComputeResourceArgsDict(TypedDict):
    config: pulumi.Input[ClusterComputeResourceConfigArgsDict]
    id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterComputeResourceArgs:
    def __init__(
        __self__,
        *,
        config: pulumi.Input[ClusterComputeResourceConfigArgs],
        id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Input[ClusterComputeResourceConfigArgs]: ...
    @config.setter
    def config(self, value: pulumi.Input[ClusterComputeResourceConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...

class ClusterComputeResourceConfigArgsDict(TypedDict):
    new_flex_start_instances: NotRequired[
        pulumi.Input[ClusterComputeResourceConfigNewFlexStartInstancesArgsDict]
    ]
    new_on_demand_instances: NotRequired[
        pulumi.Input[ClusterComputeResourceConfigNewOnDemandInstancesArgsDict]
    ]
    new_reserved_instances: NotRequired[
        pulumi.Input[ClusterComputeResourceConfigNewReservedInstancesArgsDict]
    ]
    new_spot_instances: NotRequired[
        pulumi.Input[ClusterComputeResourceConfigNewSpotInstancesArgsDict]
    ]

@pulumi.input_type
class ClusterComputeResourceConfigArgs:
    def __init__(
        __self__,
        *,
        new_flex_start_instances: Optional[
            pulumi.Input[ClusterComputeResourceConfigNewFlexStartInstancesArgs]
        ] = ...,
        new_on_demand_instances: Optional[
            pulumi.Input[ClusterComputeResourceConfigNewOnDemandInstancesArgs]
        ] = ...,
        new_reserved_instances: Optional[
            pulumi.Input[ClusterComputeResourceConfigNewReservedInstancesArgs]
        ] = ...,
        new_spot_instances: Optional[
            pulumi.Input[ClusterComputeResourceConfigNewSpotInstancesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newFlexStartInstances")
    def new_flex_start_instances(
        self,
    ) -> Optional[
        pulumi.Input[ClusterComputeResourceConfigNewFlexStartInstancesArgs]
    ]: ...
    @new_flex_start_instances.setter
    def new_flex_start_instances(
        self,
        value: Optional[
            pulumi.Input[ClusterComputeResourceConfigNewFlexStartInstancesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="newOnDemandInstances")
    def new_on_demand_instances(
        self,
    ) -> Optional[
        pulumi.Input[ClusterComputeResourceConfigNewOnDemandInstancesArgs]
    ]: ...
    @new_on_demand_instances.setter
    def new_on_demand_instances(
        self,
        value: Optional[
            pulumi.Input[ClusterComputeResourceConfigNewOnDemandInstancesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="newReservedInstances")
    def new_reserved_instances(
        self,
    ) -> Optional[
        pulumi.Input[ClusterComputeResourceConfigNewReservedInstancesArgs]
    ]: ...
    @new_reserved_instances.setter
    def new_reserved_instances(
        self,
        value: Optional[
            pulumi.Input[ClusterComputeResourceConfigNewReservedInstancesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="newSpotInstances")
    def new_spot_instances(
        self,
    ) -> Optional[pulumi.Input[ClusterComputeResourceConfigNewSpotInstancesArgs]]: ...
    @new_spot_instances.setter
    def new_spot_instances(
        self,
        value: Optional[pulumi.Input[ClusterComputeResourceConfigNewSpotInstancesArgs]],
    ): ...

class ClusterComputeResourceConfigNewFlexStartInstancesArgsDict(TypedDict):
    machine_type: pulumi.Input[_builtins.str]
    max_duration: pulumi.Input[_builtins.str]
    zone: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterComputeResourceConfigNewFlexStartInstancesArgs:
    def __init__(
        __self__,
        *,
        machine_type: pulumi.Input[_builtins.str],
        max_duration: pulumi.Input[_builtins.str],
        zone: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Input[_builtins.str]: ...
    @machine_type.setter
    def machine_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="maxDuration")
    def max_duration(self) -> pulumi.Input[_builtins.str]: ...
    @max_duration.setter
    def max_duration(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Input[_builtins.str]: ...
    @zone.setter
    def zone(self, value: pulumi.Input[_builtins.str]): ...

class ClusterComputeResourceConfigNewOnDemandInstancesArgsDict(TypedDict):
    machine_type: pulumi.Input[_builtins.str]
    zone: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterComputeResourceConfigNewOnDemandInstancesArgs:
    def __init__(
        __self__,
        *,
        machine_type: pulumi.Input[_builtins.str],
        zone: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Input[_builtins.str]: ...
    @machine_type.setter
    def machine_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Input[_builtins.str]: ...
    @zone.setter
    def zone(self, value: pulumi.Input[_builtins.str]): ...

class ClusterComputeResourceConfigNewReservedInstancesArgsDict(TypedDict):
    reservation: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterComputeResourceConfigNewReservedInstancesArgs:
    def __init__(
        __self__, *, reservation: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def reservation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reservation.setter
    def reservation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterComputeResourceConfigNewSpotInstancesArgsDict(TypedDict):
    machine_type: pulumi.Input[_builtins.str]
    zone: pulumi.Input[_builtins.str]
    termination_action: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterComputeResourceConfigNewSpotInstancesArgs:
    def __init__(
        __self__,
        *,
        machine_type: pulumi.Input[_builtins.str],
        zone: pulumi.Input[_builtins.str],
        termination_action: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Input[_builtins.str]: ...
    @machine_type.setter
    def machine_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Input[_builtins.str]: ...
    @zone.setter
    def zone(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="terminationAction")
    def termination_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @termination_action.setter
    def termination_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNetworkResourceArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    config: NotRequired[pulumi.Input[ClusterNetworkResourceConfigArgsDict]]
    networks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceNetworkArgsDict]]]
    ]

@pulumi.input_type
class ClusterNetworkResourceArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        config: Optional[pulumi.Input[ClusterNetworkResourceConfigArgs]] = ...,
        networks: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceNetworkArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[ClusterNetworkResourceConfigArgs]]: ...
    @config.setter
    def config(
        self, value: Optional[pulumi.Input[ClusterNetworkResourceConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def networks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceNetworkArgs]]]
    ]: ...
    @networks.setter
    def networks(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceNetworkArgs]]]
        ],
    ): ...

class ClusterNetworkResourceConfigArgsDict(TypedDict):
    existing_network: NotRequired[
        pulumi.Input[ClusterNetworkResourceConfigExistingNetworkArgsDict]
    ]
    new_network: NotRequired[
        pulumi.Input[ClusterNetworkResourceConfigNewNetworkArgsDict]
    ]

@pulumi.input_type
class ClusterNetworkResourceConfigArgs:
    def __init__(
        __self__,
        *,
        existing_network: Optional[
            pulumi.Input[ClusterNetworkResourceConfigExistingNetworkArgs]
        ] = ...,
        new_network: Optional[
            pulumi.Input[ClusterNetworkResourceConfigNewNetworkArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="existingNetwork")
    def existing_network(
        self,
    ) -> Optional[pulumi.Input[ClusterNetworkResourceConfigExistingNetworkArgs]]: ...
    @existing_network.setter
    def existing_network(
        self,
        value: Optional[pulumi.Input[ClusterNetworkResourceConfigExistingNetworkArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="newNetwork")
    def new_network(
        self,
    ) -> Optional[pulumi.Input[ClusterNetworkResourceConfigNewNetworkArgs]]: ...
    @new_network.setter
    def new_network(
        self, value: Optional[pulumi.Input[ClusterNetworkResourceConfigNewNetworkArgs]]
    ): ...

class ClusterNetworkResourceConfigExistingNetworkArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    subnetwork: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterNetworkResourceConfigExistingNetworkArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        subnetwork: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> pulumi.Input[_builtins.str]: ...
    @subnetwork.setter
    def subnetwork(self, value: pulumi.Input[_builtins.str]): ...

class ClusterNetworkResourceConfigNewNetworkArgsDict(TypedDict):
    network: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNetworkResourceConfigNewNetworkArgs:
    def __init__(
        __self__,
        *,
        network: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Input[_builtins.str]: ...
    @network.setter
    def network(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterNetworkResourceNetworkArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterNetworkResourceNetworkArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterOrchestratorArgsDict(TypedDict):
    slurm: NotRequired[pulumi.Input[ClusterOrchestratorSlurmArgsDict]]

@pulumi.input_type
class ClusterOrchestratorArgs:
    def __init__(
        __self__, *, slurm: Optional[pulumi.Input[ClusterOrchestratorSlurmArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def slurm(self) -> Optional[pulumi.Input[ClusterOrchestratorSlurmArgs]]: ...
    @slurm.setter
    def slurm(self, value: Optional[pulumi.Input[ClusterOrchestratorSlurmArgs]]): ...

class ClusterOrchestratorSlurmArgsDict(TypedDict):
    login_nodes: pulumi.Input[ClusterOrchestratorSlurmLoginNodesArgsDict]
    node_sets: pulumi.Input[
        Sequence[pulumi.Input[ClusterOrchestratorSlurmNodeSetArgsDict]]
    ]
    partitions: pulumi.Input[
        Sequence[pulumi.Input[ClusterOrchestratorSlurmPartitionArgsDict]]
    ]
    default_partition: NotRequired[pulumi.Input[_builtins.str]]
    epilog_bash_scripts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    prolog_bash_scripts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ClusterOrchestratorSlurmArgs:
    def __init__(
        __self__,
        *,
        login_nodes: pulumi.Input[ClusterOrchestratorSlurmLoginNodesArgs],
        node_sets: pulumi.Input[
            Sequence[pulumi.Input[ClusterOrchestratorSlurmNodeSetArgs]]
        ],
        partitions: pulumi.Input[
            Sequence[pulumi.Input[ClusterOrchestratorSlurmPartitionArgs]]
        ],
        default_partition: Optional[pulumi.Input[_builtins.str]] = ...,
        epilog_bash_scripts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        prolog_bash_scripts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginNodes")
    def login_nodes(self) -> pulumi.Input[ClusterOrchestratorSlurmLoginNodesArgs]: ...
    @login_nodes.setter
    def login_nodes(
        self, value: pulumi.Input[ClusterOrchestratorSlurmLoginNodesArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeSets")
    def node_sets(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ClusterOrchestratorSlurmNodeSetArgs]]]: ...
    @node_sets.setter
    def node_sets(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ClusterOrchestratorSlurmNodeSetArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def partitions(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ClusterOrchestratorSlurmPartitionArgs]]
    ]: ...
    @partitions.setter
    def partitions(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ClusterOrchestratorSlurmPartitionArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultPartition")
    def default_partition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_partition.setter
    def default_partition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="epilogBashScripts")
    def epilog_bash_scripts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @epilog_bash_scripts.setter
    def epilog_bash_scripts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="prologBashScripts")
    def prolog_bash_scripts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @prolog_bash_scripts.setter
    def prolog_bash_scripts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClusterOrchestratorSlurmLoginNodesArgsDict(TypedDict):
    count: pulumi.Input[_builtins.str]
    machine_type: pulumi.Input[_builtins.str]
    zone: pulumi.Input[_builtins.str]
    boot_disk: NotRequired[
        pulumi.Input[ClusterOrchestratorSlurmLoginNodesBootDiskArgsDict]
    ]
    enable_os_login: NotRequired[pulumi.Input[_builtins.bool]]
    enable_public_ips: NotRequired[pulumi.Input[_builtins.bool]]
    instances: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterOrchestratorSlurmLoginNodesInstanceArgsDict]]
        ]
    ]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    startup_script: NotRequired[pulumi.Input[_builtins.str]]
    storage_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClusterOrchestratorSlurmLoginNodesStorageConfigArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class ClusterOrchestratorSlurmLoginNodesArgs:
    def __init__(
        __self__,
        *,
        count: pulumi.Input[_builtins.str],
        machine_type: pulumi.Input[_builtins.str],
        zone: pulumi.Input[_builtins.str],
        boot_disk: Optional[
            pulumi.Input[ClusterOrchestratorSlurmLoginNodesBootDiskArgs]
        ] = ...,
        enable_os_login: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_public_ips: Optional[pulumi.Input[_builtins.bool]] = ...,
        instances: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterOrchestratorSlurmLoginNodesInstanceArgs]]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterOrchestratorSlurmLoginNodesStorageConfigArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.str]: ...
    @count.setter
    def count(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> pulumi.Input[_builtins.str]: ...
    @machine_type.setter
    def machine_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Input[_builtins.str]: ...
    @zone.setter
    def zone(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(
        self,
    ) -> Optional[pulumi.Input[ClusterOrchestratorSlurmLoginNodesBootDiskArgs]]: ...
    @boot_disk.setter
    def boot_disk(
        self,
        value: Optional[pulumi.Input[ClusterOrchestratorSlurmLoginNodesBootDiskArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableOsLogin")
    def enable_os_login(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_os_login.setter
    def enable_os_login(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enablePublicIps")
    def enable_public_ips(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_public_ips.setter
    def enable_public_ips(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterOrchestratorSlurmLoginNodesInstanceArgs]]
        ]
    ]: ...
    @instances.setter
    def instances(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterOrchestratorSlurmLoginNodesInstanceArgs]]
            ]
        ],
    ): ...
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
    @pulumi.getter(name="startupScript")
    def startup_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @startup_script.setter
    def startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageConfigs")
    def storage_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterOrchestratorSlurmLoginNodesStorageConfigArgs]]
        ]
    ]: ...
    @storage_configs.setter
    def storage_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClusterOrchestratorSlurmLoginNodesStorageConfigArgs]
                ]
            ]
        ],
    ): ...

class ClusterOrchestratorSlurmLoginNodesBootDiskArgsDict(TypedDict):
    size_gb: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterOrchestratorSlurmLoginNodesBootDiskArgs:
    def __init__(
        __self__,
        *,
        size_gb: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> pulumi.Input[_builtins.str]: ...
    @size_gb.setter
    def size_gb(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ClusterOrchestratorSlurmLoginNodesInstanceArgsDict(TypedDict):
    instance: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterOrchestratorSlurmLoginNodesInstanceArgs:
    def __init__(
        __self__, *, instance: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterOrchestratorSlurmLoginNodesStorageConfigArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    local_mount: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterOrchestratorSlurmLoginNodesStorageConfigArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        local_mount: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localMount")
    def local_mount(self) -> pulumi.Input[_builtins.str]: ...
    @local_mount.setter
    def local_mount(self, value: pulumi.Input[_builtins.str]): ...

class ClusterOrchestratorSlurmNodeSetArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    compute_id: NotRequired[pulumi.Input[_builtins.str]]
    compute_instance: NotRequired[
        pulumi.Input[ClusterOrchestratorSlurmNodeSetComputeInstanceArgsDict]
    ]
    max_dynamic_node_count: NotRequired[pulumi.Input[_builtins.str]]
    static_node_count: NotRequired[pulumi.Input[_builtins.str]]
    storage_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterOrchestratorSlurmNodeSetStorageConfigArgsDict]]
        ]
    ]

@pulumi.input_type
class ClusterOrchestratorSlurmNodeSetArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        compute_id: Optional[pulumi.Input[_builtins.str]] = ...,
        compute_instance: Optional[
            pulumi.Input[ClusterOrchestratorSlurmNodeSetComputeInstanceArgs]
        ] = ...,
        max_dynamic_node_count: Optional[pulumi.Input[_builtins.str]] = ...,
        static_node_count: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterOrchestratorSlurmNodeSetStorageConfigArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compute_id.setter
    def compute_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="computeInstance")
    def compute_instance(
        self,
    ) -> Optional[pulumi.Input[ClusterOrchestratorSlurmNodeSetComputeInstanceArgs]]: ...
    @compute_instance.setter
    def compute_instance(
        self,
        value: Optional[
            pulumi.Input[ClusterOrchestratorSlurmNodeSetComputeInstanceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxDynamicNodeCount")
    def max_dynamic_node_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_dynamic_node_count.setter
    def max_dynamic_node_count(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="staticNodeCount")
    def static_node_count(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @static_node_count.setter
    def static_node_count(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageConfigs")
    def storage_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterOrchestratorSlurmNodeSetStorageConfigArgs]]
        ]
    ]: ...
    @storage_configs.setter
    def storage_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterOrchestratorSlurmNodeSetStorageConfigArgs]]
            ]
        ],
    ): ...

class ClusterOrchestratorSlurmNodeSetComputeInstanceArgsDict(TypedDict):
    boot_disk: NotRequired[
        pulumi.Input[ClusterOrchestratorSlurmNodeSetComputeInstanceBootDiskArgsDict]
    ]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    startup_script: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterOrchestratorSlurmNodeSetComputeInstanceArgs:
    def __init__(
        __self__,
        *,
        boot_disk: Optional[
            pulumi.Input[ClusterOrchestratorSlurmNodeSetComputeInstanceBootDiskArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        startup_script: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(
        self,
    ) -> Optional[
        pulumi.Input[ClusterOrchestratorSlurmNodeSetComputeInstanceBootDiskArgs]
    ]: ...
    @boot_disk.setter
    def boot_disk(
        self,
        value: Optional[
            pulumi.Input[ClusterOrchestratorSlurmNodeSetComputeInstanceBootDiskArgs]
        ],
    ): ...
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
    @pulumi.getter(name="startupScript")
    def startup_script(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @startup_script.setter
    def startup_script(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterOrchestratorSlurmNodeSetComputeInstanceBootDiskArgsDict(TypedDict):
    size_gb: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterOrchestratorSlurmNodeSetComputeInstanceBootDiskArgs:
    def __init__(
        __self__,
        *,
        size_gb: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> pulumi.Input[_builtins.str]: ...
    @size_gb.setter
    def size_gb(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class ClusterOrchestratorSlurmNodeSetStorageConfigArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    local_mount: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterOrchestratorSlurmNodeSetStorageConfigArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        local_mount: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localMount")
    def local_mount(self) -> pulumi.Input[_builtins.str]: ...
    @local_mount.setter
    def local_mount(self, value: pulumi.Input[_builtins.str]): ...

class ClusterOrchestratorSlurmPartitionArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    node_set_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ClusterOrchestratorSlurmPartitionArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        node_set_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="nodeSetIds")
    def node_set_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @node_set_ids.setter
    def node_set_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class ClusterStorageResourceArgsDict(TypedDict):
    config: pulumi.Input[ClusterStorageResourceConfigArgsDict]
    id: pulumi.Input[_builtins.str]
    buckets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceBucketArgsDict]]]
    ]
    filestores: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceFilestoreArgsDict]]]
    ]
    lustres: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceLustreArgsDict]]]
    ]

@pulumi.input_type
class ClusterStorageResourceArgs:
    def __init__(
        __self__,
        *,
        config: pulumi.Input[ClusterStorageResourceConfigArgs],
        id: pulumi.Input[_builtins.str],
        buckets: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceBucketArgs]]]
        ] = ...,
        filestores: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceFilestoreArgs]]]
        ] = ...,
        lustres: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceLustreArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> pulumi.Input[ClusterStorageResourceConfigArgs]: ...
    @config.setter
    def config(self, value: pulumi.Input[ClusterStorageResourceConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def buckets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceBucketArgs]]]
    ]: ...
    @buckets.setter
    def buckets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceBucketArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filestores(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceFilestoreArgs]]]
    ]: ...
    @filestores.setter
    def filestores(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceFilestoreArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def lustres(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceLustreArgs]]]
    ]: ...
    @lustres.setter
    def lustres(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceLustreArgs]]]
        ],
    ): ...

class ClusterStorageResourceBucketArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterStorageResourceBucketArgs:
    def __init__(
        __self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterStorageResourceConfigArgsDict(TypedDict):
    existing_bucket: NotRequired[
        pulumi.Input[ClusterStorageResourceConfigExistingBucketArgsDict]
    ]
    existing_filestore: NotRequired[
        pulumi.Input[ClusterStorageResourceConfigExistingFilestoreArgsDict]
    ]
    existing_lustre: NotRequired[
        pulumi.Input[ClusterStorageResourceConfigExistingLustreArgsDict]
    ]
    new_bucket: NotRequired[pulumi.Input[ClusterStorageResourceConfigNewBucketArgsDict]]
    new_filestore: NotRequired[
        pulumi.Input[ClusterStorageResourceConfigNewFilestoreArgsDict]
    ]
    new_lustre: NotRequired[pulumi.Input[ClusterStorageResourceConfigNewLustreArgsDict]]

@pulumi.input_type
class ClusterStorageResourceConfigArgs:
    def __init__(
        __self__,
        *,
        existing_bucket: Optional[
            pulumi.Input[ClusterStorageResourceConfigExistingBucketArgs]
        ] = ...,
        existing_filestore: Optional[
            pulumi.Input[ClusterStorageResourceConfigExistingFilestoreArgs]
        ] = ...,
        existing_lustre: Optional[
            pulumi.Input[ClusterStorageResourceConfigExistingLustreArgs]
        ] = ...,
        new_bucket: Optional[
            pulumi.Input[ClusterStorageResourceConfigNewBucketArgs]
        ] = ...,
        new_filestore: Optional[
            pulumi.Input[ClusterStorageResourceConfigNewFilestoreArgs]
        ] = ...,
        new_lustre: Optional[
            pulumi.Input[ClusterStorageResourceConfigNewLustreArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="existingBucket")
    def existing_bucket(
        self,
    ) -> Optional[pulumi.Input[ClusterStorageResourceConfigExistingBucketArgs]]: ...
    @existing_bucket.setter
    def existing_bucket(
        self,
        value: Optional[pulumi.Input[ClusterStorageResourceConfigExistingBucketArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="existingFilestore")
    def existing_filestore(
        self,
    ) -> Optional[pulumi.Input[ClusterStorageResourceConfigExistingFilestoreArgs]]: ...
    @existing_filestore.setter
    def existing_filestore(
        self,
        value: Optional[
            pulumi.Input[ClusterStorageResourceConfigExistingFilestoreArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="existingLustre")
    def existing_lustre(
        self,
    ) -> Optional[pulumi.Input[ClusterStorageResourceConfigExistingLustreArgs]]: ...
    @existing_lustre.setter
    def existing_lustre(
        self,
        value: Optional[pulumi.Input[ClusterStorageResourceConfigExistingLustreArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="newBucket")
    def new_bucket(
        self,
    ) -> Optional[pulumi.Input[ClusterStorageResourceConfigNewBucketArgs]]: ...
    @new_bucket.setter
    def new_bucket(
        self, value: Optional[pulumi.Input[ClusterStorageResourceConfigNewBucketArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="newFilestore")
    def new_filestore(
        self,
    ) -> Optional[pulumi.Input[ClusterStorageResourceConfigNewFilestoreArgs]]: ...
    @new_filestore.setter
    def new_filestore(
        self,
        value: Optional[pulumi.Input[ClusterStorageResourceConfigNewFilestoreArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="newLustre")
    def new_lustre(
        self,
    ) -> Optional[pulumi.Input[ClusterStorageResourceConfigNewLustreArgs]]: ...
    @new_lustre.setter
    def new_lustre(
        self, value: Optional[pulumi.Input[ClusterStorageResourceConfigNewLustreArgs]]
    ): ...

class ClusterStorageResourceConfigExistingBucketArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterStorageResourceConfigExistingBucketArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...

class ClusterStorageResourceConfigExistingFilestoreArgsDict(TypedDict):
    filestore: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterStorageResourceConfigExistingFilestoreArgs:
    def __init__(__self__, *, filestore: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filestore(self) -> pulumi.Input[_builtins.str]: ...
    @filestore.setter
    def filestore(self, value: pulumi.Input[_builtins.str]): ...

class ClusterStorageResourceConfigExistingLustreArgsDict(TypedDict):
    lustre: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterStorageResourceConfigExistingLustreArgs:
    def __init__(__self__, *, lustre: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def lustre(self) -> pulumi.Input[_builtins.str]: ...
    @lustre.setter
    def lustre(self, value: pulumi.Input[_builtins.str]): ...

class ClusterStorageResourceConfigNewBucketArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    autoclass: NotRequired[
        pulumi.Input[ClusterStorageResourceConfigNewBucketAutoclassArgsDict]
    ]
    hierarchical_namespace: NotRequired[
        pulumi.Input[ClusterStorageResourceConfigNewBucketHierarchicalNamespaceArgsDict]
    ]
    storage_class: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterStorageResourceConfigNewBucketArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        autoclass: Optional[
            pulumi.Input[ClusterStorageResourceConfigNewBucketAutoclassArgs]
        ] = ...,
        hierarchical_namespace: Optional[
            pulumi.Input[ClusterStorageResourceConfigNewBucketHierarchicalNamespaceArgs]
        ] = ...,
        storage_class: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def autoclass(
        self,
    ) -> Optional[pulumi.Input[ClusterStorageResourceConfigNewBucketAutoclassArgs]]: ...
    @autoclass.setter
    def autoclass(
        self,
        value: Optional[
            pulumi.Input[ClusterStorageResourceConfigNewBucketAutoclassArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="hierarchicalNamespace")
    def hierarchical_namespace(
        self,
    ) -> Optional[
        pulumi.Input[ClusterStorageResourceConfigNewBucketHierarchicalNamespaceArgs]
    ]: ...
    @hierarchical_namespace.setter
    def hierarchical_namespace(
        self,
        value: Optional[
            pulumi.Input[ClusterStorageResourceConfigNewBucketHierarchicalNamespaceArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterStorageResourceConfigNewBucketAutoclassArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ClusterStorageResourceConfigNewBucketAutoclassArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...

class ClusterStorageResourceConfigNewBucketHierarchicalNamespaceArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ClusterStorageResourceConfigNewBucketHierarchicalNamespaceArgs:
    def __init__(
        __self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ClusterStorageResourceConfigNewFilestoreArgsDict(TypedDict):
    file_shares: pulumi.Input[
        Sequence[
            pulumi.Input[ClusterStorageResourceConfigNewFilestoreFileShareArgsDict]
        ]
    ]
    filestore: pulumi.Input[_builtins.str]
    tier: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterStorageResourceConfigNewFilestoreArgs:
    def __init__(
        __self__,
        *,
        file_shares: pulumi.Input[
            Sequence[
                pulumi.Input[ClusterStorageResourceConfigNewFilestoreFileShareArgs]
            ]
        ],
        filestore: pulumi.Input[_builtins.str],
        tier: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileShares")
    def file_shares(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ClusterStorageResourceConfigNewFilestoreFileShareArgs]]
    ]: ...
    @file_shares.setter
    def file_shares(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[ClusterStorageResourceConfigNewFilestoreFileShareArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filestore(self) -> pulumi.Input[_builtins.str]: ...
    @filestore.setter
    def filestore(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> pulumi.Input[_builtins.str]: ...
    @tier.setter
    def tier(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterStorageResourceConfigNewFilestoreFileShareArgsDict(TypedDict):
    capacity_gb: pulumi.Input[_builtins.str]
    file_share: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterStorageResourceConfigNewFilestoreFileShareArgs:
    def __init__(
        __self__,
        *,
        capacity_gb: pulumi.Input[_builtins.str],
        file_share: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityGb")
    def capacity_gb(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_gb.setter
    def capacity_gb(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> pulumi.Input[_builtins.str]: ...
    @file_share.setter
    def file_share(self, value: pulumi.Input[_builtins.str]): ...

class ClusterStorageResourceConfigNewLustreArgsDict(TypedDict):
    capacity_gb: pulumi.Input[_builtins.str]
    filesystem: pulumi.Input[_builtins.str]
    lustre: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterStorageResourceConfigNewLustreArgs:
    def __init__(
        __self__,
        *,
        capacity_gb: pulumi.Input[_builtins.str],
        filesystem: pulumi.Input[_builtins.str],
        lustre: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityGb")
    def capacity_gb(self) -> pulumi.Input[_builtins.str]: ...
    @capacity_gb.setter
    def capacity_gb(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filesystem(self) -> pulumi.Input[_builtins.str]: ...
    @filesystem.setter
    def filesystem(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def lustre(self) -> pulumi.Input[_builtins.str]: ...
    @lustre.setter
    def lustre(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterStorageResourceFilestoreArgsDict(TypedDict):
    filestore: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterStorageResourceFilestoreArgs:
    def __init__(
        __self__, *, filestore: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filestore(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filestore.setter
    def filestore(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterStorageResourceLustreArgsDict(TypedDict):
    lustre: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterStorageResourceLustreArgs:
    def __init__(
        __self__, *, lustre: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def lustre(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lustre.setter
    def lustre(self, value: Optional[pulumi.Input[_builtins.str]]): ...
