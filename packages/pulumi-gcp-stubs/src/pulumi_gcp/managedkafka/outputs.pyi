import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AclAclEntry",
    "ClusterBrokerCapacityConfig",
    "ClusterCapacityConfig",
    "ClusterGcpConfig",
    "ClusterGcpConfigAccessConfig",
    "ClusterGcpConfigAccessConfigNetworkConfig",
    "ClusterRebalanceConfig",
    "ClusterTlsConfig",
    "ClusterTlsConfigTrustConfig",
    "ClusterTlsConfigTrustConfigCasConfig",
    "ConnectClusterCapacityConfig",
    "ConnectClusterGcpConfig",
    "ConnectClusterGcpConfigAccessConfig",
    "ConnectClusterGcpConfigAccessConfigNetworkConfig",
    "ConnectorTaskRestartPolicy",
]

@pulumi.output_type
class AclAclEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        operation: _builtins.str,
        principal: _builtins.str,
        host: Optional[_builtins.str] = ...,
        permission_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="permissionType")
    def permission_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterBrokerCapacityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, disk_size_gib: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGib")
    def disk_size_gib(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterCapacityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, memory_bytes: _builtins.str, vcpu_count: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryBytes")
    def memory_bytes(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterGcpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_config: outputs.ClusterGcpConfigAccessConfig,
        kms_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> outputs.ClusterGcpConfigAccessConfig: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterGcpConfigAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network_configs: Sequence[outputs.ClusterGcpConfigAccessConfigNetworkConfig],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(
        self,
    ) -> Sequence[outputs.ClusterGcpConfigAccessConfigNetworkConfig]: ...

@pulumi.output_type
class ClusterGcpConfigAccessConfigNetworkConfig(dict):
    def __init__(__self__, *, subnet: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> _builtins.str: ...

@pulumi.output_type
class ClusterRebalanceConfig(dict):
    def __init__(__self__, *, mode: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClusterTlsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ssl_principal_mapping_rules: Optional[_builtins.str] = ...,
        trust_config: Optional[outputs.ClusterTlsConfigTrustConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sslPrincipalMappingRules")
    def ssl_principal_mapping_rules(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trustConfig")
    def trust_config(self) -> Optional[outputs.ClusterTlsConfigTrustConfig]: ...

@pulumi.output_type
class ClusterTlsConfigTrustConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cas_configs: Optional[
            Sequence[outputs.ClusterTlsConfigTrustConfigCasConfig]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="casConfigs")
    def cas_configs(
        self,
    ) -> Optional[Sequence[outputs.ClusterTlsConfigTrustConfigCasConfig]]: ...

@pulumi.output_type
class ClusterTlsConfigTrustConfigCasConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, ca_pool: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caPool")
    def ca_pool(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectClusterCapacityConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, memory_bytes: _builtins.str, vcpu_count: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryBytes")
    def memory_bytes(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> _builtins.str: ...

@pulumi.output_type
class ConnectClusterGcpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, access_config: outputs.ConnectClusterGcpConfigAccessConfig
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> outputs.ConnectClusterGcpConfigAccessConfig: ...

@pulumi.output_type
class ConnectClusterGcpConfigAccessConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        network_configs: Sequence[
            outputs.ConnectClusterGcpConfigAccessConfigNetworkConfig
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(
        self,
    ) -> Sequence[outputs.ConnectClusterGcpConfigAccessConfigNetworkConfig]: ...

@pulumi.output_type
class ConnectClusterGcpConfigAccessConfigNetworkConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        primary_subnet: _builtins.str,
        additional_subnets: Optional[Sequence[_builtins.str]] = ...,
        dns_domain_names: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primarySubnet")
    def primary_subnet(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="additionalSubnets")
    @_utilities.deprecated(...)
    def additional_subnets(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dnsDomainNames")
    def dns_domain_names(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConnectorTaskRestartPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_backoff: Optional[_builtins.str] = ...,
        minimum_backoff: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumBackoff")
    def maximum_backoff(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minimumBackoff")
    def minimum_backoff(self) -> Optional[_builtins.str]: ...
