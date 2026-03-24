import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "V2QueuedResourceTpu",
    "V2QueuedResourceTpuNodeSpec",
    "V2QueuedResourceTpuNodeSpecNode",
    "V2QueuedResourceTpuNodeSpecNodeNetworkConfig",
    "V2VmAcceleratorConfig",
    "V2VmDataDisk",
    "V2VmNetworkConfig",
    "V2VmNetworkEndpoint",
    "V2VmNetworkEndpointAccessConfig",
    "V2VmSchedulingConfig",
    "V2VmServiceAccount",
    "V2VmShieldedInstanceConfig",
    "V2VmSymptom",
]

@pulumi.output_type
class V2QueuedResourceTpu(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        node_specs: Optional[Sequence[outputs.V2QueuedResourceTpuNodeSpec]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nodeSpecs")
    def node_specs(self) -> Optional[Sequence[outputs.V2QueuedResourceTpuNodeSpec]]: ...

@pulumi.output_type
class V2QueuedResourceTpuNodeSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        node: outputs.V2QueuedResourceTpuNodeSpecNode,
        parent: _builtins.str,
        node_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def node(self) -> outputs.V2QueuedResourceTpuNodeSpecNode: ...
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2QueuedResourceTpuNodeSpecNode(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        runtime_version: _builtins.str,
        accelerator_type: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        network_config: Optional[
            outputs.V2QueuedResourceTpuNodeSpecNodeNetworkConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="acceleratorType")
    def accelerator_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfig")
    def network_config(
        self,
    ) -> Optional[outputs.V2QueuedResourceTpuNodeSpecNodeNetworkConfig]: ...

@pulumi.output_type
class V2QueuedResourceTpuNodeSpecNodeNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        can_ip_forward: Optional[_builtins.bool] = ...,
        enable_external_ips: Optional[_builtins.bool] = ...,
        network: Optional[_builtins.str] = ...,
        queue_count: Optional[_builtins.int] = ...,
        subnetwork: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableExternalIps")
    def enable_external_ips(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queueCount")
    def queue_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2VmAcceleratorConfig(dict):
    def __init__(__self__, *, topology: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topology(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class V2VmDataDisk(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, source_disk: _builtins.str, mode: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceDisk")
    def source_disk(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2VmNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        can_ip_forward: Optional[_builtins.bool] = ...,
        enable_external_ips: Optional[_builtins.bool] = ...,
        network: Optional[_builtins.str] = ...,
        queue_count: Optional[_builtins.int] = ...,
        subnetwork: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="canIpForward")
    def can_ip_forward(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableExternalIps")
    def enable_external_ips(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queueCount")
    def queue_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2VmNetworkEndpoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_configs: Optional[
            Sequence[outputs.V2VmNetworkEndpointAccessConfig]
        ] = ...,
        ip_address: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfigs")
    def access_configs(
        self,
    ) -> Optional[Sequence[outputs.V2VmNetworkEndpointAccessConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class V2VmNetworkEndpointAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, external_ip: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalIp")
    def external_ip(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class V2VmSchedulingConfig(dict):
    def __init__(
        __self__,
        *,
        preemptible: Optional[_builtins.bool] = ...,
        reserved: Optional[_builtins.bool] = ...,
        spot: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def preemptible(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def reserved(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def spot(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class V2VmServiceAccount(dict):
    def __init__(
        __self__,
        *,
        email: Optional[_builtins.str] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class V2VmShieldedInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enable_secure_boot: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> _builtins.bool: ...

@pulumi.output_type
class V2VmSymptom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        create_time: Optional[_builtins.str] = ...,
        details: Optional[_builtins.str] = ...,
        symptom_type: Optional[_builtins.str] = ...,
        worker_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="symptomType")
    def symptom_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workerId")
    def worker_id(self) -> Optional[_builtins.str]: ...
