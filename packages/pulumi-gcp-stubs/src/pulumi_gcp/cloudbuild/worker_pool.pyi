

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
__all__ = ['WorkerPoolArgs', 'WorkerPool']
@pulumi.input_type
class WorkerPoolArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[WorkerPoolNetworkConfigArgs]] = ..., private_service_connect: Optional[pulumi.Input[WorkerPoolPrivateServiceConnectArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., worker_config: Optional[pulumi.Input[WorkerPoolWorkerConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[WorkerPoolNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[WorkerPoolNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateServiceConnect")
    def private_service_connect(self) -> Optional[pulumi.Input[WorkerPoolPrivateServiceConnectArgs]]:
        
        ...
    
    @private_service_connect.setter
    def private_service_connect(self, value: Optional[pulumi.Input[WorkerPoolPrivateServiceConnectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[pulumi.Input[WorkerPoolWorkerConfigArgs]]:
        
        ...
    
    @worker_config.setter
    def worker_config(self, value: Optional[pulumi.Input[WorkerPoolWorkerConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkerPoolState:
    def __init__(__self__, *, annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[WorkerPoolNetworkConfigArgs]] = ..., private_service_connect: Optional[pulumi.Input[WorkerPoolPrivateServiceConnectArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., worker_config: Optional[pulumi.Input[WorkerPoolWorkerConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_annotations.setter
    def effective_annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[WorkerPoolNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[WorkerPoolNetworkConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateServiceConnect")
    def private_service_connect(self) -> Optional[pulumi.Input[WorkerPoolPrivateServiceConnectArgs]]:
        
        ...
    
    @private_service_connect.setter
    def private_service_connect(self, value: Optional[pulumi.Input[WorkerPoolPrivateServiceConnectArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> Optional[pulumi.Input[WorkerPoolWorkerConfigArgs]]:
        
        ...
    
    @worker_config.setter
    def worker_config(self, value: Optional[pulumi.Input[WorkerPoolWorkerConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:cloudbuild/workerPool:WorkerPool")
class WorkerPool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[WorkerPoolNetworkConfigArgs, WorkerPoolNetworkConfigArgsDict]]] = ..., private_service_connect: Optional[pulumi.Input[Union[WorkerPoolPrivateServiceConnectArgs, WorkerPoolPrivateServiceConnectArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., worker_config: Optional[pulumi.Input[Union[WorkerPoolWorkerConfigArgs, WorkerPoolWorkerConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkerPoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., delete_time: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., effective_annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[Union[WorkerPoolNetworkConfigArgs, WorkerPoolNetworkConfigArgsDict]]] = ..., private_service_connect: Optional[pulumi.Input[Union[WorkerPoolPrivateServiceConnectArgs, WorkerPoolPrivateServiceConnectArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., uid: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ..., worker_config: Optional[pulumi.Input[Union[WorkerPoolWorkerConfigArgs, WorkerPoolWorkerConfigArgsDict]]] = ...) -> WorkerPool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
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
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> pulumi.Output[Optional[outputs.WorkerPoolNetworkConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateServiceConnect")
    def private_service_connect(self) -> pulumi.Output[Optional[outputs.WorkerPoolPrivateServiceConnect]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerConfig")
    def worker_config(self) -> pulumi.Output[outputs.WorkerPoolWorkerConfig]:
        
        ...
    


