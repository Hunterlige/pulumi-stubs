

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['V2QueuedResourceTpuArgs', 'V2QueuedResourceTpuArgsDict', 'V2QueuedResourceTpuNodeSpecArgs', 'V2QueuedResourceTpuNodeSpecArgsDict', 'V2QueuedResourceTpuNodeSpecNodeArgs', 'V2QueuedResourceTpuNodeSpecNodeArgsDict', 'V2QueuedResourceTpuNodeSpecNodeNetworkConfigArgs', ..., 'V2VmAcceleratorConfigArgs', 'V2VmAcceleratorConfigArgsDict', 'V2VmDataDiskArgs', 'V2VmDataDiskArgsDict', 'V2VmNetworkConfigArgs', 'V2VmNetworkConfigArgsDict', 'V2VmNetworkEndpointArgs', 'V2VmNetworkEndpointArgsDict', 'V2VmNetworkEndpointAccessConfigArgs', 'V2VmNetworkEndpointAccessConfigArgsDict', 'V2VmSchedulingConfigArgs', 'V2VmSchedulingConfigArgsDict', 'V2VmServiceAccountArgs', 'V2VmServiceAccountArgsDict', 'V2VmShieldedInstanceConfigArgs', 'V2VmShieldedInstanceConfigArgsDict', 'V2VmSymptomArgs', 'V2VmSymptomArgsDict']
class V2QueuedResourceTpuArgsDict(TypedDict):
    node_specs: NotRequired[pulumi.Input[Sequence[pulumi.Input[V2QueuedResourceTpuNodeSpecArgsDict]]]]


@pulumi.input_type
class V2QueuedResourceTpuArgs:
    def __init__(__self__, *, node_specs: Optional[pulumi.Input[Sequence[pulumi.Input[V2QueuedResourceTpuNodeSpecArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeSpecs")
    def node_specs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2QueuedResourceTpuNodeSpecArgs]]]]:
        
        ...
    
    @node_specs.setter
    def node_specs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2QueuedResourceTpuNodeSpecArgs]]]]): # -> None:
        ...
    


class V2QueuedResourceTpuNodeSpecArgsDict(TypedDict):
    node: pulumi.Input[V2QueuedResourceTpuNodeSpecNodeArgsDict]
    parent: pulumi.Input[_builtins.str]
    node_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class V2QueuedResourceTpuNodeSpecArgs:
    def __init__(__self__, *, node: pulumi.Input[V2QueuedResourceTpuNodeSpecNodeArgs], parent: pulumi.Input[_builtins.str], node_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def node(self) -> pulumi.Input[V2QueuedResourceTpuNodeSpecNodeArgs]:
        
        ...
    
    @node.setter
    def node(self, value: pulumi.Input[V2QueuedResourceTpuNodeSpecNodeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @parent.setter
    def parent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @node_id.setter
    def node_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class V2QueuedResourceTpuNodeSpecNodeArgsDict(TypedDict):
    runtime_version: pulumi.Input[_builtins.str]
    accelerator_type: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    network_config: NotRequired[pulumi.Input[V2QueuedResourceTpuNodeSpecNodeNetworkConfigArgsDict]]


@pulumi.input_type
class V2QueuedResourceTpuNodeSpecNodeArgs:
    def __init__(__self__, *, runtime_version: pulumi.Input[_builtins.str], accelerator_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., network_config: Optional[pulumi.Input[V2QueuedResourceTpuNodeSpecNodeNetworkConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @runtime_version.setter
    def runtime_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accelerator_type.setter
    def accelerator_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(self) -> Optional[pulumi.Input[V2QueuedResourceTpuNodeSpecNodeNetworkConfigArgs]]:
        
        ...
    
    @network_config.setter
    def network_config(self, value: Optional[pulumi.Input[V2QueuedResourceTpuNodeSpecNodeNetworkConfigArgs]]): # -> None:
        ...
    


class V2QueuedResourceTpuNodeSpecNodeNetworkConfigArgsDict(TypedDict):
    can_ip_forward: NotRequired[pulumi.Input[_builtins.bool]]
    enable_external_ips: NotRequired[pulumi.Input[_builtins.bool]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    queue_count: NotRequired[pulumi.Input[_builtins.int]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class V2QueuedResourceTpuNodeSpecNodeNetworkConfigArgs:
    def __init__(__self__, *, can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ..., enable_external_ips: Optional[pulumi.Input[_builtins.bool]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., queue_count: Optional[pulumi.Input[_builtins.int]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @can_ip_forward.setter
    def can_ip_forward(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExternalIps")
    def enable_external_ips(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_external_ips.setter
    def enable_external_ips(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueCount")
    def queue_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @queue_count.setter
    def queue_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class V2VmAcceleratorConfigArgsDict(TypedDict):
    topology: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class V2VmAcceleratorConfigArgs:
    def __init__(__self__, *, topology: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topology(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @topology.setter
    def topology(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class V2VmDataDiskArgsDict(TypedDict):
    source_disk: pulumi.Input[_builtins.str]
    mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class V2VmDataDiskArgs:
    def __init__(__self__, *, source_disk: pulumi.Input[_builtins.str], mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @source_disk.setter
    def source_disk(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class V2VmNetworkConfigArgsDict(TypedDict):
    can_ip_forward: NotRequired[pulumi.Input[_builtins.bool]]
    enable_external_ips: NotRequired[pulumi.Input[_builtins.bool]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    queue_count: NotRequired[pulumi.Input[_builtins.int]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class V2VmNetworkConfigArgs:
    def __init__(__self__, *, can_ip_forward: Optional[pulumi.Input[_builtins.bool]] = ..., enable_external_ips: Optional[pulumi.Input[_builtins.bool]] = ..., network: Optional[pulumi.Input[_builtins.str]] = ..., queue_count: Optional[pulumi.Input[_builtins.int]] = ..., subnetwork: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @can_ip_forward.setter
    def can_ip_forward(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableExternalIps")
    def enable_external_ips(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_external_ips.setter
    def enable_external_ips(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queueCount")
    def queue_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @queue_count.setter
    def queue_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class V2VmNetworkEndpointArgsDict(TypedDict):
    access_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkEndpointAccessConfigArgsDict]]]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class V2VmNetworkEndpointArgs:
    def __init__(__self__, *, access_configs: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkEndpointAccessConfigArgs]]]] = ..., ip_address: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkEndpointAccessConfigArgs]]]]:
        
        ...
    
    @access_configs.setter
    def access_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[V2VmNetworkEndpointAccessConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class V2VmNetworkEndpointAccessConfigArgsDict(TypedDict):
    external_ip: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class V2VmNetworkEndpointAccessConfigArgs:
    def __init__(__self__, *, external_ip: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @external_ip.setter
    def external_ip(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class V2VmSchedulingConfigArgsDict(TypedDict):
    preemptible: NotRequired[pulumi.Input[_builtins.bool]]
    reserved: NotRequired[pulumi.Input[_builtins.bool]]
    spot: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class V2VmSchedulingConfigArgs:
    def __init__(__self__, *, preemptible: Optional[pulumi.Input[_builtins.bool]] = ..., reserved: Optional[pulumi.Input[_builtins.bool]] = ..., spot: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @preemptible.setter
    def preemptible(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def reserved(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @reserved.setter
    def reserved(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @spot.setter
    def spot(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class V2VmServiceAccountArgsDict(TypedDict):
    email: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class V2VmServiceAccountArgs:
    def __init__(__self__, *, email: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email.setter
    def email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class V2VmShieldedInstanceConfigArgsDict(TypedDict):
    enable_secure_boot: pulumi.Input[_builtins.bool]


@pulumi.input_type
class V2VmShieldedInstanceConfigArgs:
    def __init__(__self__, *, enable_secure_boot: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class V2VmSymptomArgsDict(TypedDict):
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    details: NotRequired[pulumi.Input[_builtins.str]]
    symptom_type: NotRequired[pulumi.Input[_builtins.str]]
    worker_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class V2VmSymptomArgs:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., details: Optional[pulumi.Input[_builtins.str]] = ..., symptom_type: Optional[pulumi.Input[_builtins.str]] = ..., worker_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def details(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="symptomType")
    def symptom_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @symptom_type.setter
    def symptom_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workerId")
    def worker_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @worker_id.setter
    def worker_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


