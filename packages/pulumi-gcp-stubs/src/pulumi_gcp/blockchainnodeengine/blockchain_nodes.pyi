

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
__all__ = ['BlockchainNodesArgs', 'BlockchainNodes']
@pulumi.input_type
class BlockchainNodesArgs:
    def __init__(__self__, *, blockchain_node_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], blockchain_type: Optional[pulumi.Input[_builtins.str]] = ..., ethereum_details: Optional[pulumi.Input[BlockchainNodesEthereumDetailsArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockchainNodeId")
    def blockchain_node_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @blockchain_node_id.setter
    def blockchain_node_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockchainType")
    def blockchain_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blockchain_type.setter
    def blockchain_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ethereumDetails")
    def ethereum_details(self) -> Optional[pulumi.Input[BlockchainNodesEthereumDetailsArgs]]:
        
        ...
    
    @ethereum_details.setter
    def ethereum_details(self, value: Optional[pulumi.Input[BlockchainNodesEthereumDetailsArgs]]): # -> None:
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BlockchainNodesState:
    def __init__(__self__, *, blockchain_node_id: Optional[pulumi.Input[_builtins.str]] = ..., blockchain_type: Optional[pulumi.Input[_builtins.str]] = ..., connection_infos: Optional[pulumi.Input[Sequence[pulumi.Input[BlockchainNodesConnectionInfoArgs]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ethereum_details: Optional[pulumi.Input[BlockchainNodesEthereumDetailsArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockchainNodeId")
    def blockchain_node_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blockchain_node_id.setter
    def blockchain_node_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockchainType")
    def blockchain_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @blockchain_type.setter
    def blockchain_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfos")
    def connection_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BlockchainNodesConnectionInfoArgs]]]]:
        
        ...
    
    @connection_infos.setter
    def connection_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BlockchainNodesConnectionInfoArgs]]]]): # -> None:
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
    @pulumi.getter(name="ethereumDetails")
    def ethereum_details(self) -> Optional[pulumi.Input[BlockchainNodesEthereumDetailsArgs]]:
        
        ...
    
    @ethereum_details.setter
    def ethereum_details(self, value: Optional[pulumi.Input[BlockchainNodesEthereumDetailsArgs]]): # -> None:
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
    


@pulumi.type_token(...)
class BlockchainNodes(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., blockchain_node_id: Optional[pulumi.Input[_builtins.str]] = ..., blockchain_type: Optional[pulumi.Input[_builtins.str]] = ..., ethereum_details: Optional[pulumi.Input[Union[BlockchainNodesEthereumDetailsArgs, BlockchainNodesEthereumDetailsArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BlockchainNodesArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., blockchain_node_id: Optional[pulumi.Input[_builtins.str]] = ..., blockchain_type: Optional[pulumi.Input[_builtins.str]] = ..., connection_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BlockchainNodesConnectionInfoArgs, BlockchainNodesConnectionInfoArgsDict]]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., ethereum_details: Optional[pulumi.Input[Union[BlockchainNodesEthereumDetailsArgs, BlockchainNodesEthereumDetailsArgsDict]]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> BlockchainNodes:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockchainNodeId")
    def blockchain_node_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockchainType")
    def blockchain_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionInfos")
    def connection_infos(self) -> pulumi.Output[Sequence[outputs.BlockchainNodesConnectionInfo]]:
        
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
    @pulumi.getter(name="ethereumDetails")
    def ethereum_details(self) -> pulumi.Output[Optional[outputs.BlockchainNodesEthereumDetails]]:
        
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
    


