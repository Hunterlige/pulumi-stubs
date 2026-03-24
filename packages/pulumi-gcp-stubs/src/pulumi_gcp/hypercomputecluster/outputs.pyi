import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClusterComputeResource",
    "ClusterComputeResourceConfig",
    "ClusterComputeResourceConfigNewFlexStartInstances",
    "ClusterComputeResourceConfigNewOnDemandInstances",
    "ClusterComputeResourceConfigNewReservedInstances",
    "ClusterComputeResourceConfigNewSpotInstances",
    "ClusterNetworkResource",
    "ClusterNetworkResourceConfig",
    "ClusterNetworkResourceConfigExistingNetwork",
    "ClusterNetworkResourceConfigNewNetwork",
    "ClusterNetworkResourceNetwork",
    "ClusterOrchestrator",
    "ClusterOrchestratorSlurm",
    "ClusterOrchestratorSlurmLoginNodes",
    "ClusterOrchestratorSlurmLoginNodesBootDisk",
    "ClusterOrchestratorSlurmLoginNodesInstance",
    "ClusterOrchestratorSlurmLoginNodesStorageConfig",
    "ClusterOrchestratorSlurmNodeSet",
    "ClusterOrchestratorSlurmNodeSetComputeInstance",
    ...,
    "ClusterOrchestratorSlurmNodeSetStorageConfig",
    "ClusterOrchestratorSlurmPartition",
    "ClusterStorageResource",
    "ClusterStorageResourceBucket",
    "ClusterStorageResourceConfig",
    "ClusterStorageResourceConfigExistingBucket",
    "ClusterStorageResourceConfigExistingFilestore",
    "ClusterStorageResourceConfigExistingLustre",
    "ClusterStorageResourceConfigNewBucket",
    "ClusterStorageResourceConfigNewBucketAutoclass",
    ...,
    "ClusterStorageResourceConfigNewFilestore",
    "ClusterStorageResourceConfigNewFilestoreFileShare",
    "ClusterStorageResourceConfigNewLustre",
    "ClusterStorageResourceFilestore",
    "ClusterStorageResourceLustre",
]

@pulumi.output_type
class ClusterComputeResource(dict):
    def __init__(
        __self__, *, config: outputs.ClusterComputeResourceConfig, id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> outputs.ClusterComputeResourceConfig: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterComputeResourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        new_flex_start_instances: Optional[
            outputs.ClusterComputeResourceConfigNewFlexStartInstances
        ] = ...,
        new_on_demand_instances: Optional[
            outputs.ClusterComputeResourceConfigNewOnDemandInstances
        ] = ...,
        new_reserved_instances: Optional[
            outputs.ClusterComputeResourceConfigNewReservedInstances
        ] = ...,
        new_spot_instances: Optional[
            outputs.ClusterComputeResourceConfigNewSpotInstances
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newFlexStartInstances")
    def new_flex_start_instances(
        self,
    ) -> Optional[outputs.ClusterComputeResourceConfigNewFlexStartInstances]: ...
    @_builtins.property
    @pulumi.getter(name="newOnDemandInstances")
    def new_on_demand_instances(
        self,
    ) -> Optional[outputs.ClusterComputeResourceConfigNewOnDemandInstances]: ...
    @_builtins.property
    @pulumi.getter(name="newReservedInstances")
    def new_reserved_instances(
        self,
    ) -> Optional[outputs.ClusterComputeResourceConfigNewReservedInstances]: ...
    @_builtins.property
    @pulumi.getter(name="newSpotInstances")
    def new_spot_instances(
        self,
    ) -> Optional[outputs.ClusterComputeResourceConfigNewSpotInstances]: ...

@pulumi.output_type
class ClusterComputeResourceConfigNewFlexStartInstances(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        machine_type: _builtins.str,
        max_duration: _builtins.str,
        zone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maxDuration")
    def max_duration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterComputeResourceConfigNewOnDemandInstances(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, machine_type: _builtins.str, zone: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterComputeResourceConfigNewReservedInstances(dict):
    def __init__(__self__, *, reservation: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def reservation(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterComputeResourceConfigNewSpotInstances(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        machine_type: _builtins.str,
        zone: _builtins.str,
        termination_action: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="terminationAction")
    def termination_action(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNetworkResource(dict):
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        config: Optional[outputs.ClusterNetworkResourceConfig] = ...,
        networks: Optional[Sequence[outputs.ClusterNetworkResourceNetwork]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> Optional[outputs.ClusterNetworkResourceConfig]: ...
    @_builtins.property
    @pulumi.getter
    def networks(self) -> Optional[Sequence[outputs.ClusterNetworkResourceNetwork]]: ...

@pulumi.output_type
class ClusterNetworkResourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        existing_network: Optional[
            outputs.ClusterNetworkResourceConfigExistingNetwork
        ] = ...,
        new_network: Optional[outputs.ClusterNetworkResourceConfigNewNetwork] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="existingNetwork")
    def existing_network(
        self,
    ) -> Optional[outputs.ClusterNetworkResourceConfigExistingNetwork]: ...
    @_builtins.property
    @pulumi.getter(name="newNetwork")
    def new_network(
        self,
    ) -> Optional[outputs.ClusterNetworkResourceConfigNewNetwork]: ...

@pulumi.output_type
class ClusterNetworkResourceConfigExistingNetwork(dict):
    def __init__(
        __self__, *, network: _builtins.str, subnetwork: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterNetworkResourceConfigNewNetwork(dict):
    def __init__(
        __self__, *, network: _builtins.str, description: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterNetworkResourceNetwork(dict):
    def __init__(
        __self__,
        *,
        network: Optional[_builtins.str] = ...,
        subnetwork: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterOrchestrator(dict):
    def __init__(
        __self__, *, slurm: Optional[outputs.ClusterOrchestratorSlurm] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def slurm(self) -> Optional[outputs.ClusterOrchestratorSlurm]: ...

@pulumi.output_type
class ClusterOrchestratorSlurm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        login_nodes: outputs.ClusterOrchestratorSlurmLoginNodes,
        node_sets: Sequence[outputs.ClusterOrchestratorSlurmNodeSet],
        partitions: Sequence[outputs.ClusterOrchestratorSlurmPartition],
        default_partition: Optional[_builtins.str] = ...,
        epilog_bash_scripts: Optional[Sequence[_builtins.str]] = ...,
        prolog_bash_scripts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="loginNodes")
    def login_nodes(self) -> outputs.ClusterOrchestratorSlurmLoginNodes: ...
    @_builtins.property
    @pulumi.getter(name="nodeSets")
    def node_sets(self) -> Sequence[outputs.ClusterOrchestratorSlurmNodeSet]: ...
    @_builtins.property
    @pulumi.getter
    def partitions(self) -> Sequence[outputs.ClusterOrchestratorSlurmPartition]: ...
    @_builtins.property
    @pulumi.getter(name="defaultPartition")
    def default_partition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="epilogBashScripts")
    def epilog_bash_scripts(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="prologBashScripts")
    def prolog_bash_scripts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClusterOrchestratorSlurmLoginNodes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        count: _builtins.str,
        machine_type: _builtins.str,
        zone: _builtins.str,
        boot_disk: Optional[outputs.ClusterOrchestratorSlurmLoginNodesBootDisk] = ...,
        enable_os_login: Optional[_builtins.bool] = ...,
        enable_public_ips: Optional[_builtins.bool] = ...,
        instances: Optional[
            Sequence[outputs.ClusterOrchestratorSlurmLoginNodesInstance]
        ] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        startup_script: Optional[_builtins.str] = ...,
        storage_configs: Optional[
            Sequence[outputs.ClusterOrchestratorSlurmLoginNodesStorageConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(
        self,
    ) -> Optional[outputs.ClusterOrchestratorSlurmLoginNodesBootDisk]: ...
    @_builtins.property
    @pulumi.getter(name="enableOsLogin")
    def enable_os_login(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePublicIps")
    def enable_public_ips(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[Sequence[outputs.ClusterOrchestratorSlurmLoginNodesInstance]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startupScript")
    def startup_script(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageConfigs")
    def storage_configs(
        self,
    ) -> Optional[
        Sequence[outputs.ClusterOrchestratorSlurmLoginNodesStorageConfig]
    ]: ...

@pulumi.output_type
class ClusterOrchestratorSlurmLoginNodesBootDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, size_gb: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterOrchestratorSlurmLoginNodesInstance(dict):
    def __init__(__self__, *, instance: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterOrchestratorSlurmLoginNodesStorageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, id: _builtins.str, local_mount: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localMount")
    def local_mount(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterOrchestratorSlurmNodeSet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        id: _builtins.str,
        compute_id: Optional[_builtins.str] = ...,
        compute_instance: Optional[
            outputs.ClusterOrchestratorSlurmNodeSetComputeInstance
        ] = ...,
        max_dynamic_node_count: Optional[_builtins.str] = ...,
        static_node_count: Optional[_builtins.str] = ...,
        storage_configs: Optional[
            Sequence[outputs.ClusterOrchestratorSlurmNodeSetStorageConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="computeInstance")
    def compute_instance(
        self,
    ) -> Optional[outputs.ClusterOrchestratorSlurmNodeSetComputeInstance]: ...
    @_builtins.property
    @pulumi.getter(name="maxDynamicNodeCount")
    def max_dynamic_node_count(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="staticNodeCount")
    def static_node_count(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageConfigs")
    def storage_configs(
        self,
    ) -> Optional[Sequence[outputs.ClusterOrchestratorSlurmNodeSetStorageConfig]]: ...

@pulumi.output_type
class ClusterOrchestratorSlurmNodeSetComputeInstance(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        boot_disk: Optional[
            outputs.ClusterOrchestratorSlurmNodeSetComputeInstanceBootDisk
        ] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        startup_script: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bootDisk")
    def boot_disk(
        self,
    ) -> Optional[outputs.ClusterOrchestratorSlurmNodeSetComputeInstanceBootDisk]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="startupScript")
    def startup_script(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterOrchestratorSlurmNodeSetComputeInstanceBootDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, size_gb: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterOrchestratorSlurmNodeSetStorageConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, id: _builtins.str, local_mount: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localMount")
    def local_mount(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterOrchestratorSlurmPartition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, id: _builtins.str, node_set_ids: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeSetIds")
    def node_set_ids(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClusterStorageResource(dict):
    def __init__(
        __self__,
        *,
        config: outputs.ClusterStorageResourceConfig,
        id: _builtins.str,
        buckets: Optional[Sequence[outputs.ClusterStorageResourceBucket]] = ...,
        filestores: Optional[Sequence[outputs.ClusterStorageResourceFilestore]] = ...,
        lustres: Optional[Sequence[outputs.ClusterStorageResourceLustre]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def config(self) -> outputs.ClusterStorageResourceConfig: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> Optional[Sequence[outputs.ClusterStorageResourceBucket]]: ...
    @_builtins.property
    @pulumi.getter
    def filestores(
        self,
    ) -> Optional[Sequence[outputs.ClusterStorageResourceFilestore]]: ...
    @_builtins.property
    @pulumi.getter
    def lustres(self) -> Optional[Sequence[outputs.ClusterStorageResourceLustre]]: ...

@pulumi.output_type
class ClusterStorageResourceBucket(dict):
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterStorageResourceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        existing_bucket: Optional[
            outputs.ClusterStorageResourceConfigExistingBucket
        ] = ...,
        existing_filestore: Optional[
            outputs.ClusterStorageResourceConfigExistingFilestore
        ] = ...,
        existing_lustre: Optional[
            outputs.ClusterStorageResourceConfigExistingLustre
        ] = ...,
        new_bucket: Optional[outputs.ClusterStorageResourceConfigNewBucket] = ...,
        new_filestore: Optional[outputs.ClusterStorageResourceConfigNewFilestore] = ...,
        new_lustre: Optional[outputs.ClusterStorageResourceConfigNewLustre] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="existingBucket")
    def existing_bucket(
        self,
    ) -> Optional[outputs.ClusterStorageResourceConfigExistingBucket]: ...
    @_builtins.property
    @pulumi.getter(name="existingFilestore")
    def existing_filestore(
        self,
    ) -> Optional[outputs.ClusterStorageResourceConfigExistingFilestore]: ...
    @_builtins.property
    @pulumi.getter(name="existingLustre")
    def existing_lustre(
        self,
    ) -> Optional[outputs.ClusterStorageResourceConfigExistingLustre]: ...
    @_builtins.property
    @pulumi.getter(name="newBucket")
    def new_bucket(self) -> Optional[outputs.ClusterStorageResourceConfigNewBucket]: ...
    @_builtins.property
    @pulumi.getter(name="newFilestore")
    def new_filestore(
        self,
    ) -> Optional[outputs.ClusterStorageResourceConfigNewFilestore]: ...
    @_builtins.property
    @pulumi.getter(name="newLustre")
    def new_lustre(self) -> Optional[outputs.ClusterStorageResourceConfigNewLustre]: ...

@pulumi.output_type
class ClusterStorageResourceConfigExistingBucket(dict):
    def __init__(__self__, *, bucket: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterStorageResourceConfigExistingFilestore(dict):
    def __init__(__self__, *, filestore: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filestore(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterStorageResourceConfigExistingLustre(dict):
    def __init__(__self__, *, lustre: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def lustre(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterStorageResourceConfigNewBucket(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        autoclass: Optional[
            outputs.ClusterStorageResourceConfigNewBucketAutoclass
        ] = ...,
        hierarchical_namespace: Optional[
            outputs.ClusterStorageResourceConfigNewBucketHierarchicalNamespace
        ] = ...,
        storage_class: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def autoclass(
        self,
    ) -> Optional[outputs.ClusterStorageResourceConfigNewBucketAutoclass]: ...
    @_builtins.property
    @pulumi.getter(name="hierarchicalNamespace")
    def hierarchical_namespace(
        self,
    ) -> Optional[
        outputs.ClusterStorageResourceConfigNewBucketHierarchicalNamespace
    ]: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterStorageResourceConfigNewBucketAutoclass(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...

@pulumi.output_type
class ClusterStorageResourceConfigNewBucketHierarchicalNamespace(dict):
    def __init__(__self__, *, enabled: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ClusterStorageResourceConfigNewFilestore(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_shares: Sequence[
            outputs.ClusterStorageResourceConfigNewFilestoreFileShare
        ],
        filestore: _builtins.str,
        tier: _builtins.str,
        description: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileShares")
    def file_shares(
        self,
    ) -> Sequence[outputs.ClusterStorageResourceConfigNewFilestoreFileShare]: ...
    @_builtins.property
    @pulumi.getter
    def filestore(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tier(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterStorageResourceConfigNewFilestoreFileShare(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, capacity_gb: _builtins.str, file_share: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityGb")
    def capacity_gb(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fileShare")
    def file_share(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterStorageResourceConfigNewLustre(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        capacity_gb: _builtins.str,
        filesystem: _builtins.str,
        lustre: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityGb")
    def capacity_gb(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filesystem(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def lustre(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterStorageResourceFilestore(dict):
    def __init__(__self__, *, filestore: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filestore(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterStorageResourceLustre(dict):
    def __init__(__self__, *, lustre: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def lustre(self) -> Optional[_builtins.str]: ...
