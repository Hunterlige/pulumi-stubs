

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NodePoolArgs', 'NodePool']
@pulumi.input_type
class NodePoolArgs:
    def __init__(__self__, *, cluster: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], node_count: pulumi.Input[_builtins.int], node_location: pulumi.Input[_builtins.str], labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., local_disk_encryption: Optional[pulumi.Input[NodePoolLocalDiskEncryptionArgs]] = ..., machine_filter: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[NodePoolNodeConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLocation")
    def node_location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @node_location.setter
    def node_location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="localDiskEncryption")
    def local_disk_encryption(self) -> Optional[pulumi.Input[NodePoolLocalDiskEncryptionArgs]]:
        
        ...
    
    @local_disk_encryption.setter
    def local_disk_encryption(self, value: Optional[pulumi.Input[NodePoolLocalDiskEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineFilter")
    def machine_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_filter.setter
    def machine_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[NodePoolNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[NodePoolNodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _NodePoolState:
    def __init__(__self__, *, cluster: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., local_disk_encryption: Optional[pulumi.Input[NodePoolLocalDiskEncryptionArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., machine_filter: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[NodePoolNodeConfigArgs]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., node_location: Optional[pulumi.Input[_builtins.str]] = ..., node_version: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="localDiskEncryption")
    def local_disk_encryption(self) -> Optional[pulumi.Input[NodePoolLocalDiskEncryptionArgs]]:
        
        ...
    
    @local_disk_encryption.setter
    def local_disk_encryption(self, value: Optional[pulumi.Input[NodePoolLocalDiskEncryptionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineFilter")
    def machine_filter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_filter.setter
    def machine_filter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> Optional[pulumi.Input[NodePoolNodeConfigArgs]]:
        
        ...
    
    @node_config.setter
    def node_config(self, value: Optional[pulumi.Input[NodePoolNodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLocation")
    def node_location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_location.setter
    def node_location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeVersion")
    def node_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_version.setter
    def node_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:edgecontainer/nodePool:NodePool")
class NodePool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., local_disk_encryption: Optional[pulumi.Input[Union[NodePoolLocalDiskEncryptionArgs, NodePoolLocalDiskEncryptionArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., machine_filter: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[Union[NodePoolNodeConfigArgs, NodePoolNodeConfigArgsDict]]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., node_location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NodePoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., cluster: Optional[pulumi.Input[_builtins.str]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., local_disk_encryption: Optional[pulumi.Input[Union[NodePoolLocalDiskEncryptionArgs, NodePoolLocalDiskEncryptionArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., machine_filter: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., node_config: Optional[pulumi.Input[Union[NodePoolNodeConfigArgs, NodePoolNodeConfigArgsDict]]] = ..., node_count: Optional[pulumi.Input[_builtins.int]] = ..., node_location: Optional[pulumi.Input[_builtins.str]] = ..., node_version: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> NodePool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="localDiskEncryption")
    def local_disk_encryption(self) -> pulumi.Output[Optional[outputs.NodePoolLocalDiskEncryption]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineFilter")
    def machine_filter(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeConfig")
    def node_config(self) -> pulumi.Output[outputs.NodePoolNodeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeLocation")
    def node_location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeVersion")
    def node_version(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


