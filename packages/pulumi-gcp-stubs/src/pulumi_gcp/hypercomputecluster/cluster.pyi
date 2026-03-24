

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ClusterArgs', 'Cluster']
@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *, cluster_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], compute_resources: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterComputeResourceArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., network_resources: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceArgs]]]] = ..., orchestrator: Optional[pulumi.Input[ClusterOrchestratorArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., storage_resources: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeResources")
    def compute_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterComputeResourceArgs]]]]:
        
        ...
    
    @compute_resources.setter
    def compute_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterComputeResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkResources")
    def network_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceArgs]]]]:
        
        ...
    
    @network_resources.setter
    def network_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def orchestrator(self) -> Optional[pulumi.Input[ClusterOrchestratorArgs]]:
        
        ...
    
    @orchestrator.setter
    def orchestrator(self, value: Optional[pulumi.Input[ClusterOrchestratorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageResources")
    def storage_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceArgs]]]]:
        
        ...
    
    @storage_resources.setter
    def storage_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *, cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., compute_resources: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterComputeResourceArgs]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_resources: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceArgs]]]] = ..., orchestrator: Optional[pulumi.Input[ClusterOrchestratorArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., storage_resources: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceArgs]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeResources")
    def compute_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterComputeResourceArgs]]]]:
        
        ...
    
    @compute_resources.setter
    def compute_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterComputeResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkResources")
    def network_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceArgs]]]]:
        
        ...
    
    @network_resources.setter
    def network_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterNetworkResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def orchestrator(self) -> Optional[pulumi.Input[ClusterOrchestratorArgs]]:
        
        ...
    
    @orchestrator.setter
    def orchestrator(self, value: Optional[pulumi.Input[ClusterOrchestratorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageResources")
    def storage_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceArgs]]]]:
        
        ...
    
    @storage_resources.setter
    def storage_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ClusterStorageResourceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:hypercomputecluster/cluster:Cluster")
class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., compute_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterComputeResourceArgs, ClusterComputeResourceArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., network_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterNetworkResourceArgs, ClusterNetworkResourceArgsDict]]]]] = ..., orchestrator: Optional[pulumi.Input[Union[ClusterOrchestratorArgs, ClusterOrchestratorArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., storage_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterStorageResourceArgs, ClusterStorageResourceArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ClusterArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cluster_id: Optional[pulumi.Input[_builtins.str]] = ..., compute_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterComputeResourceArgs, ClusterComputeResourceArgsDict]]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterNetworkResourceArgs, ClusterNetworkResourceArgsDict]]]]] = ..., orchestrator: Optional[pulumi.Input[Union[ClusterOrchestratorArgs, ClusterOrchestratorArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., reconciling: Optional[pulumi.Input[_builtins.bool]] = ..., storage_resources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ClusterStorageResourceArgs, ClusterStorageResourceArgsDict]]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Cluster:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeResources")
    def compute_resources(self) -> pulumi.Output[Optional[Sequence[outputs.ClusterComputeResource]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkResources")
    def network_resources(self) -> pulumi.Output[Optional[Sequence[outputs.ClusterNetworkResource]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def orchestrator(self) -> pulumi.Output[Optional[outputs.ClusterOrchestrator]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageResources")
    def storage_resources(self) -> pulumi.Output[Optional[Sequence[outputs.ClusterStorageResource]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


