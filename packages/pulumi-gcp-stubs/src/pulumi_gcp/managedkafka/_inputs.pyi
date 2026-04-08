import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AclAclEntryArgs",
    "AclAclEntryArgsDict",
    "ClusterBrokerCapacityConfigArgs",
    "ClusterBrokerCapacityConfigArgsDict",
    "ClusterCapacityConfigArgs",
    "ClusterCapacityConfigArgsDict",
    "ClusterGcpConfigArgs",
    "ClusterGcpConfigArgsDict",
    "ClusterGcpConfigAccessConfigArgs",
    "ClusterGcpConfigAccessConfigArgsDict",
    "ClusterGcpConfigAccessConfigNetworkConfigArgs",
    "ClusterGcpConfigAccessConfigNetworkConfigArgsDict",
    "ClusterRebalanceConfigArgs",
    "ClusterRebalanceConfigArgsDict",
    "ClusterTlsConfigArgs",
    "ClusterTlsConfigArgsDict",
    "ClusterTlsConfigTrustConfigArgs",
    "ClusterTlsConfigTrustConfigArgsDict",
    "ClusterTlsConfigTrustConfigCasConfigArgs",
    "ClusterTlsConfigTrustConfigCasConfigArgsDict",
    "ConnectClusterCapacityConfigArgs",
    "ConnectClusterCapacityConfigArgsDict",
    "ConnectClusterGcpConfigArgs",
    "ConnectClusterGcpConfigArgsDict",
    "ConnectClusterGcpConfigAccessConfigArgs",
    "ConnectClusterGcpConfigAccessConfigArgsDict",
    ...,
    ...,
    "ConnectorTaskRestartPolicyArgs",
    "ConnectorTaskRestartPolicyArgsDict",
]

class AclAclEntryArgsDict(TypedDict):
    operation: pulumi.Input[_builtins.str]
    principal: pulumi.Input[_builtins.str]
    host: NotRequired[pulumi.Input[_builtins.str]]
    permission_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AclAclEntryArgs:
    def __init__(
        __self__,
        *,
        operation: pulumi.Input[_builtins.str],
        principal: pulumi.Input[_builtins.str],
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        permission_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> pulumi.Input[_builtins.str]: ...
    @operation.setter
    def operation(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="permissionType")
    def permission_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission_type.setter
    def permission_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterBrokerCapacityConfigArgsDict(TypedDict):
    disk_size_gib: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterBrokerCapacityConfigArgs:
    def __init__(
        __self__, *, disk_size_gib: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="diskSizeGib")
    def disk_size_gib(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disk_size_gib.setter
    def disk_size_gib(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterCapacityConfigArgsDict(TypedDict):
    memory_bytes: pulumi.Input[_builtins.str]
    vcpu_count: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterCapacityConfigArgs:
    def __init__(
        __self__,
        *,
        memory_bytes: pulumi.Input[_builtins.str],
        vcpu_count: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryBytes")
    def memory_bytes(self) -> pulumi.Input[_builtins.str]: ...
    @memory_bytes.setter
    def memory_bytes(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> pulumi.Input[_builtins.str]: ...
    @vcpu_count.setter
    def vcpu_count(self, value: pulumi.Input[_builtins.str]): ...

class ClusterGcpConfigArgsDict(TypedDict):
    access_config: pulumi.Input[ClusterGcpConfigAccessConfigArgsDict]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterGcpConfigArgs:
    def __init__(
        __self__,
        *,
        access_config: pulumi.Input[ClusterGcpConfigAccessConfigArgs],
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> pulumi.Input[ClusterGcpConfigAccessConfigArgs]: ...
    @access_config.setter
    def access_config(self, value: pulumi.Input[ClusterGcpConfigAccessConfigArgs]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterGcpConfigAccessConfigArgsDict(TypedDict):
    network_configs: pulumi.Input[
        Sequence[pulumi.Input[ClusterGcpConfigAccessConfigNetworkConfigArgsDict]]
    ]

@pulumi.input_type
class ClusterGcpConfigAccessConfigArgs:
    def __init__(
        __self__,
        *,
        network_configs: pulumi.Input[
            Sequence[pulumi.Input[ClusterGcpConfigAccessConfigNetworkConfigArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ClusterGcpConfigAccessConfigNetworkConfigArgs]]
    ]: ...
    @network_configs.setter
    def network_configs(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ClusterGcpConfigAccessConfigNetworkConfigArgs]]
        ],
    ): ...

class ClusterGcpConfigAccessConfigNetworkConfigArgsDict(TypedDict):
    subnet: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterGcpConfigAccessConfigNetworkConfigArgs:
    def __init__(__self__, *, subnet: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Input[_builtins.str]: ...
    @subnet.setter
    def subnet(self, value: pulumi.Input[_builtins.str]): ...

class ClusterRebalanceConfigArgsDict(TypedDict):
    mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ClusterRebalanceConfigArgs:
    def __init__(
        __self__, *, mode: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClusterTlsConfigArgsDict(TypedDict):
    ssl_principal_mapping_rules: NotRequired[pulumi.Input[_builtins.str]]
    trust_config: NotRequired[pulumi.Input[ClusterTlsConfigTrustConfigArgsDict]]

@pulumi.input_type
class ClusterTlsConfigArgs:
    def __init__(
        __self__,
        *,
        ssl_principal_mapping_rules: Optional[pulumi.Input[_builtins.str]] = ...,
        trust_config: Optional[pulumi.Input[ClusterTlsConfigTrustConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sslPrincipalMappingRules")
    def ssl_principal_mapping_rules(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ssl_principal_mapping_rules.setter
    def ssl_principal_mapping_rules(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="trustConfig")
    def trust_config(
        self,
    ) -> Optional[pulumi.Input[ClusterTlsConfigTrustConfigArgs]]: ...
    @trust_config.setter
    def trust_config(
        self, value: Optional[pulumi.Input[ClusterTlsConfigTrustConfigArgs]]
    ): ...

class ClusterTlsConfigTrustConfigArgsDict(TypedDict):
    cas_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ClusterTlsConfigTrustConfigCasConfigArgsDict]]
        ]
    ]

@pulumi.input_type
class ClusterTlsConfigTrustConfigArgs:
    def __init__(
        __self__,
        *,
        cas_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterTlsConfigTrustConfigCasConfigArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="casConfigs")
    def cas_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ClusterTlsConfigTrustConfigCasConfigArgs]]]
    ]: ...
    @cas_configs.setter
    def cas_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ClusterTlsConfigTrustConfigCasConfigArgs]]
            ]
        ],
    ): ...

class ClusterTlsConfigTrustConfigCasConfigArgsDict(TypedDict):
    ca_pool: pulumi.Input[_builtins.str]

@pulumi.input_type
class ClusterTlsConfigTrustConfigCasConfigArgs:
    def __init__(__self__, *, ca_pool: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caPool")
    def ca_pool(self) -> pulumi.Input[_builtins.str]: ...
    @ca_pool.setter
    def ca_pool(self, value: pulumi.Input[_builtins.str]): ...

class ConnectClusterCapacityConfigArgsDict(TypedDict):
    memory_bytes: pulumi.Input[_builtins.str]
    vcpu_count: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConnectClusterCapacityConfigArgs:
    def __init__(
        __self__,
        *,
        memory_bytes: pulumi.Input[_builtins.str],
        vcpu_count: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryBytes")
    def memory_bytes(self) -> pulumi.Input[_builtins.str]: ...
    @memory_bytes.setter
    def memory_bytes(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vcpuCount")
    def vcpu_count(self) -> pulumi.Input[_builtins.str]: ...
    @vcpu_count.setter
    def vcpu_count(self, value: pulumi.Input[_builtins.str]): ...

class ConnectClusterGcpConfigArgsDict(TypedDict):
    access_config: pulumi.Input[ConnectClusterGcpConfigAccessConfigArgsDict]

@pulumi.input_type
class ConnectClusterGcpConfigArgs:
    def __init__(
        __self__,
        *,
        access_config: pulumi.Input[ConnectClusterGcpConfigAccessConfigArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessConfig")
    def access_config(
        self,
    ) -> pulumi.Input[ConnectClusterGcpConfigAccessConfigArgs]: ...
    @access_config.setter
    def access_config(
        self, value: pulumi.Input[ConnectClusterGcpConfigAccessConfigArgs]
    ): ...

class ConnectClusterGcpConfigAccessConfigArgsDict(TypedDict):
    network_configs: pulumi.Input[
        Sequence[pulumi.Input[ConnectClusterGcpConfigAccessConfigNetworkConfigArgsDict]]
    ]

@pulumi.input_type
class ConnectClusterGcpConfigAccessConfigArgs:
    def __init__(
        __self__,
        *,
        network_configs: pulumi.Input[
            Sequence[pulumi.Input[ConnectClusterGcpConfigAccessConfigNetworkConfigArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="networkConfigs")
    def network_configs(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ConnectClusterGcpConfigAccessConfigNetworkConfigArgs]]
    ]: ...
    @network_configs.setter
    def network_configs(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ConnectClusterGcpConfigAccessConfigNetworkConfigArgs]]
        ],
    ): ...

class ConnectClusterGcpConfigAccessConfigNetworkConfigArgsDict(TypedDict):
    primary_subnet: pulumi.Input[_builtins.str]
    additional_subnets: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    dns_domain_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ConnectClusterGcpConfigAccessConfigNetworkConfigArgs:
    def __init__(
        __self__,
        *,
        primary_subnet: pulumi.Input[_builtins.str],
        additional_subnets: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        dns_domain_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="primarySubnet")
    def primary_subnet(self) -> pulumi.Input[_builtins.str]: ...
    @primary_subnet.setter
    def primary_subnet(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalSubnets")
    @_utilities.deprecated(...)
    def additional_subnets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_subnets.setter
    def additional_subnets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsDomainNames")
    def dns_domain_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @dns_domain_names.setter
    def dns_domain_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ConnectorTaskRestartPolicyArgsDict(TypedDict):
    maximum_backoff: NotRequired[pulumi.Input[_builtins.str]]
    minimum_backoff: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectorTaskRestartPolicyArgs:
    def __init__(
        __self__,
        *,
        maximum_backoff: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_backoff: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumBackoff")
    def maximum_backoff(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @maximum_backoff.setter
    def maximum_backoff(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumBackoff")
    def minimum_backoff(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @minimum_backoff.setter
    def minimum_backoff(self, value: Optional[pulumi.Input[_builtins.str]]): ...
