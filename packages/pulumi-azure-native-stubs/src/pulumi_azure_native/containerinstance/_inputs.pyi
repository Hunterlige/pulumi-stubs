import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApiEntityReferenceArgs",
    "ApiEntityReferenceArgsDict",
    "ApplicationGatewayBackendAddressPoolArgs",
    "ApplicationGatewayBackendAddressPoolArgsDict",
    "ApplicationGatewayArgs",
    "ApplicationGatewayArgsDict",
    "AzureFileVolumeArgs",
    "AzureFileVolumeArgsDict",
    "ConfidentialComputePropertiesArgs",
    "ConfidentialComputePropertiesArgsDict",
    "ConfigMapArgs",
    "ConfigMapArgsDict",
    "ContainerExecArgs",
    "ContainerExecArgsDict",
    "ContainerGroupDiagnosticsArgs",
    "ContainerGroupDiagnosticsArgsDict",
    "ContainerGroupIdentityArgs",
    "ContainerGroupIdentityArgsDict",
    "ContainerGroupProfileReferenceDefinitionArgs",
    "ContainerGroupProfileReferenceDefinitionArgsDict",
    "ContainerGroupProfileStubArgs",
    "ContainerGroupProfileStubArgsDict",
    "ContainerGroupSubnetIdArgs",
    "ContainerGroupSubnetIdArgsDict",
    "ContainerHttpGetArgs",
    "ContainerHttpGetArgsDict",
    "ContainerPortArgs",
    "ContainerPortArgsDict",
    "ContainerProbeArgs",
    "ContainerProbeArgsDict",
    "ContainerArgs",
    "ContainerArgsDict",
    "DeploymentExtensionSpecArgs",
    "DeploymentExtensionSpecArgsDict",
    "DnsConfigurationArgs",
    "DnsConfigurationArgsDict",
    "ElasticProfileContainerGroupNamingPolicyArgs",
    "ElasticProfileContainerGroupNamingPolicyArgsDict",
    "ElasticProfileGuidNamingPolicyArgs",
    "ElasticProfileGuidNamingPolicyArgsDict",
    "ElasticProfileArgs",
    "ElasticProfileArgsDict",
    "EncryptionPropertiesArgs",
    "EncryptionPropertiesArgsDict",
    "EnvironmentVariableArgs",
    "EnvironmentVariableArgsDict",
    "FileSharePropertiesArgs",
    "FileSharePropertiesArgsDict",
    "FileShareArgs",
    "FileShareArgsDict",
    "GitRepoVolumeArgs",
    "GitRepoVolumeArgsDict",
    "GpuResourceArgs",
    "GpuResourceArgsDict",
    "HttpHeaderArgs",
    "HttpHeaderArgsDict",
    "ImageRegistryCredentialArgs",
    "ImageRegistryCredentialArgsDict",
    "InitContainerDefinitionArgs",
    "InitContainerDefinitionArgsDict",
    "IpAddressArgs",
    "IpAddressArgsDict",
    "LoadBalancerBackendAddressPoolArgs",
    "LoadBalancerBackendAddressPoolArgsDict",
    "LoadBalancerArgs",
    "LoadBalancerArgsDict",
    "LogAnalyticsArgs",
    "LogAnalyticsArgsDict",
    "NGroupCGPropertyContainerPropertiesArgs",
    "NGroupCGPropertyContainerPropertiesArgsDict",
    "NGroupCGPropertyContainerArgs",
    "NGroupCGPropertyContainerArgsDict",
    "NGroupCGPropertyVolumeArgs",
    "NGroupCGPropertyVolumeArgsDict",
    "NGroupContainerGroupPropertiesArgs",
    "NGroupContainerGroupPropertiesArgsDict",
    "NGroupIdentityArgs",
    "NGroupIdentityArgsDict",
    "NetworkProfileArgs",
    "NetworkProfileArgsDict",
    "PlacementProfileArgs",
    "PlacementProfileArgsDict",
    "PortArgs",
    "PortArgsDict",
    "ResourceLimitsArgs",
    "ResourceLimitsArgsDict",
    "ResourceRequestsArgs",
    "ResourceRequestsArgsDict",
    "ResourceRequirementsArgs",
    "ResourceRequirementsArgsDict",
    "SecurityContextCapabilitiesDefinitionArgs",
    "SecurityContextCapabilitiesDefinitionArgsDict",
    "SecurityContextDefinitionArgs",
    "SecurityContextDefinitionArgsDict",
    "StandbyPoolProfileDefinitionArgs",
    "StandbyPoolProfileDefinitionArgsDict",
    "StorageProfileArgs",
    "StorageProfileArgsDict",
    "UpdateProfileRollingUpdateProfileArgs",
    "UpdateProfileRollingUpdateProfileArgsDict",
    "UpdateProfileArgs",
    "UpdateProfileArgsDict",
    "VolumeMountArgs",
    "VolumeMountArgsDict",
    "VolumeArgs",
    "VolumeArgsDict",
]

class ApiEntityReferenceArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApiEntityReferenceArgs:
    def __init__(
        __self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationGatewayBackendAddressPoolArgsDict(TypedDict):
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationGatewayBackendAddressPoolArgs:
    def __init__(
        __self__, *, resource: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ApplicationGatewayArgsDict(TypedDict):
    backend_address_pools: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ApplicationGatewayBackendAddressPoolArgsDict]]
        ]
    ]
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ApplicationGatewayArgs:
    def __init__(
        __self__,
        *,
        backend_address_pools: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayBackendAddressPoolArgs]]
            ]
        ] = ...,
        resource: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ApplicationGatewayBackendAddressPoolArgs]]]
    ]: ...
    @backend_address_pools.setter
    def backend_address_pools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ApplicationGatewayBackendAddressPoolArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AzureFileVolumeArgsDict(TypedDict):
    share_name: pulumi.Input[_builtins.str]
    storage_account_name: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]
    storage_account_key: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_key_reference: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AzureFileVolumeArgs:
    def __init__(
        __self__,
        *,
        share_name: pulumi.Input[_builtins.str],
        storage_account_name: pulumi.Input[_builtins.str],
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        storage_account_key: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_key_reference: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> pulumi.Input[_builtins.str]: ...
    @share_name.setter
    def share_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Input[_builtins.str]: ...
    @storage_account_name.setter
    def storage_account_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountKey")
    def storage_account_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_key.setter
    def storage_account_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountKeyReference")
    def storage_account_key_reference(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_key_reference.setter
    def storage_account_key_reference(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ConfidentialComputePropertiesArgsDict(TypedDict):
    cce_policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfidentialComputePropertiesArgs:
    def __init__(
        __self__, *, cce_policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ccePolicy")
    def cce_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cce_policy.setter
    def cce_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigMapArgsDict(TypedDict):
    key_value_pairs: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ConfigMapArgs:
    def __init__(
        __self__,
        *,
        key_value_pairs: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyValuePairs")
    def key_value_pairs(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @key_value_pairs.setter
    def key_value_pairs(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ContainerExecArgsDict(TypedDict):
    command: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ContainerExecArgs:
    def __init__(
        __self__,
        *,
        command: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def command(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @command.setter
    def command(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ContainerGroupDiagnosticsArgsDict(TypedDict):
    log_analytics: NotRequired[pulumi.Input[LogAnalyticsArgsDict]]

@pulumi.input_type
class ContainerGroupDiagnosticsArgs:
    def __init__(
        __self__, *, log_analytics: Optional[pulumi.Input[LogAnalyticsArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="logAnalytics")
    def log_analytics(self) -> Optional[pulumi.Input[LogAnalyticsArgs]]: ...
    @log_analytics.setter
    def log_analytics(self, value: Optional[pulumi.Input[LogAnalyticsArgs]]): ...

class ContainerGroupIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ContainerGroupIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[ResourceIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ContainerGroupProfileReferenceDefinitionArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    revision: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ContainerGroupProfileReferenceDefinitionArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ContainerGroupProfileStubArgsDict(TypedDict):
    container_group_properties: NotRequired[
        pulumi.Input[NGroupContainerGroupPropertiesArgsDict]
    ]
    network_profile: NotRequired[pulumi.Input[NetworkProfileArgsDict]]
    resource: NotRequired[pulumi.Input[ApiEntityReferenceArgsDict]]
    revision: NotRequired[pulumi.Input[_builtins.int]]
    storage_profile: NotRequired[pulumi.Input[StorageProfileArgsDict]]

@pulumi.input_type
class ContainerGroupProfileStubArgs:
    def __init__(
        __self__,
        *,
        container_group_properties: Optional[
            pulumi.Input[NGroupContainerGroupPropertiesArgs]
        ] = ...,
        network_profile: Optional[pulumi.Input[NetworkProfileArgs]] = ...,
        resource: Optional[pulumi.Input[ApiEntityReferenceArgs]] = ...,
        revision: Optional[pulumi.Input[_builtins.int]] = ...,
        storage_profile: Optional[pulumi.Input[StorageProfileArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerGroupProperties")
    def container_group_properties(
        self,
    ) -> Optional[pulumi.Input[NGroupContainerGroupPropertiesArgs]]: ...
    @container_group_properties.setter
    def container_group_properties(
        self, value: Optional[pulumi.Input[NGroupContainerGroupPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input[NetworkProfileArgs]]: ...
    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input[NetworkProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[ApiEntityReferenceArgs]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[ApiEntityReferenceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input[StorageProfileArgs]]: ...
    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input[StorageProfileArgs]]): ...

class ContainerGroupSubnetIdArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ContainerGroupSubnetIdArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ContainerHttpGetArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    http_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[HttpHeaderArgsDict]]]]
    path: NotRequired[pulumi.Input[_builtins.str]]
    scheme: NotRequired[pulumi.Input[Union[_builtins.str, Scheme]]]

@pulumi.input_type
class ContainerHttpGetArgs:
    def __init__(
        __self__,
        *,
        port: pulumi.Input[_builtins.int],
        http_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[HttpHeaderArgs]]]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        scheme: Optional[pulumi.Input[Union[_builtins.str, Scheme]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[HttpHeaderArgs]]]]: ...
    @http_headers.setter
    def http_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HttpHeaderArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scheme(self) -> Optional[pulumi.Input[Union[_builtins.str, Scheme]]]: ...
    @scheme.setter
    def scheme(self, value: Optional[pulumi.Input[Union[_builtins.str, Scheme]]]): ...

class ContainerPortArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    protocol: NotRequired[pulumi.Input[Union[_builtins.str, ContainerNetworkProtocol]]]

@pulumi.input_type
class ContainerPortArgs:
    def __init__(
        __self__,
        *,
        port: pulumi.Input[_builtins.int],
        protocol: Optional[
            pulumi.Input[Union[_builtins.str, ContainerNetworkProtocol]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ContainerNetworkProtocol]]]: ...
    @protocol.setter
    def protocol(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, ContainerNetworkProtocol]]],
    ): ...

class ContainerProbeArgsDict(TypedDict):
    exec_: NotRequired[pulumi.Input[ContainerExecArgsDict]]
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    http_get: NotRequired[pulumi.Input[ContainerHttpGetArgsDict]]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ContainerProbeArgs:
    def __init__(
        __self__,
        *,
        exec_: Optional[pulumi.Input[ContainerExecArgs]] = ...,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        http_get: Optional[pulumi.Input[ContainerHttpGetArgs]] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        success_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exec")
    def exec_(self) -> Optional[pulumi.Input[ContainerExecArgs]]: ...
    @exec_.setter
    def exec_(self, value: Optional[pulumi.Input[ContainerExecArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(self) -> Optional[pulumi.Input[ContainerHttpGetArgs]]: ...
    @http_get.setter
    def http_get(self, value: Optional[pulumi.Input[ContainerHttpGetArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ContainerArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    command: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    config_map: NotRequired[pulumi.Input[ConfigMapArgsDict]]
    environment_variables: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgsDict]]]
    ]
    image: NotRequired[pulumi.Input[_builtins.str]]
    liveness_probe: NotRequired[pulumi.Input[ContainerProbeArgsDict]]
    ports: NotRequired[pulumi.Input[Sequence[pulumi.Input[ContainerPortArgsDict]]]]
    readiness_probe: NotRequired[pulumi.Input[ContainerProbeArgsDict]]
    resources: NotRequired[pulumi.Input[ResourceRequirementsArgsDict]]
    security_context: NotRequired[pulumi.Input[SecurityContextDefinitionArgsDict]]
    volume_mounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VolumeMountArgsDict]]]
    ]

@pulumi.input_type
class ContainerArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        command: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        config_map: Optional[pulumi.Input[ConfigMapArgs]] = ...,
        environment_variables: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]
        ] = ...,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        liveness_probe: Optional[pulumi.Input[ContainerProbeArgs]] = ...,
        ports: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerPortArgs]]]] = ...,
        readiness_probe: Optional[pulumi.Input[ContainerProbeArgs]] = ...,
        resources: Optional[pulumi.Input[ResourceRequirementsArgs]] = ...,
        security_context: Optional[pulumi.Input[SecurityContextDefinitionArgs]] = ...,
        volume_mounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def command(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @command.setter
    def command(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="configMap")
    def config_map(self) -> Optional[pulumi.Input[ConfigMapArgs]]: ...
    @config_map.setter
    def config_map(self, value: Optional[pulumi.Input[ConfigMapArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(self) -> Optional[pulumi.Input[ContainerProbeArgs]]: ...
    @liveness_probe.setter
    def liveness_probe(self, value: Optional[pulumi.Input[ContainerProbeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerPortArgs]]]]: ...
    @ports.setter
    def ports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerPortArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(self) -> Optional[pulumi.Input[ContainerProbeArgs]]: ...
    @readiness_probe.setter
    def readiness_probe(self, value: Optional[pulumi.Input[ContainerProbeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[ResourceRequirementsArgs]]: ...
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[ResourceRequirementsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="securityContext")
    def security_context(
        self,
    ) -> Optional[pulumi.Input[SecurityContextDefinitionArgs]]: ...
    @security_context.setter
    def security_context(
        self, value: Optional[pulumi.Input[SecurityContextDefinitionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]: ...
    @volume_mounts.setter
    def volume_mounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]
    ): ...

class DeploymentExtensionSpecArgsDict(TypedDict):
    extension_type: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    protected_settings: NotRequired[Any]
    settings: NotRequired[Any]

@pulumi.input_type
class DeploymentExtensionSpecArgs:
    def __init__(
        __self__,
        *,
        extension_type: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        protected_settings: Optional[Any] = ...,
        settings: Optional[Any] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extensionType")
    def extension_type(self) -> pulumi.Input[_builtins.str]: ...
    @extension_type.setter
    def extension_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]: ...
    @protected_settings.setter
    def protected_settings(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[Any]: ...
    @settings.setter
    def settings(self, value: Optional[Any]): ...

class DnsConfigurationArgsDict(TypedDict):
    name_servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    options: NotRequired[pulumi.Input[_builtins.str]]
    search_domains: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DnsConfigurationArgs:
    def __init__(
        __self__,
        *,
        name_servers: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        options: Optional[pulumi.Input[_builtins.str]] = ...,
        search_domains: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @name_servers.setter
    def name_servers(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def options(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @options.setter
    def options(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="searchDomains")
    def search_domains(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @search_domains.setter
    def search_domains(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ElasticProfileContainerGroupNamingPolicyArgsDict(TypedDict):
    guid_naming_policy: NotRequired[
        pulumi.Input[ElasticProfileGuidNamingPolicyArgsDict]
    ]

@pulumi.input_type
class ElasticProfileContainerGroupNamingPolicyArgs:
    def __init__(
        __self__,
        *,
        guid_naming_policy: Optional[
            pulumi.Input[ElasticProfileGuidNamingPolicyArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="guidNamingPolicy")
    def guid_naming_policy(
        self,
    ) -> Optional[pulumi.Input[ElasticProfileGuidNamingPolicyArgs]]: ...
    @guid_naming_policy.setter
    def guid_naming_policy(
        self, value: Optional[pulumi.Input[ElasticProfileGuidNamingPolicyArgs]]
    ): ...

class ElasticProfileGuidNamingPolicyArgsDict(TypedDict):
    prefix: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ElasticProfileGuidNamingPolicyArgs:
    def __init__(
        __self__, *, prefix: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ElasticProfileArgsDict(TypedDict):
    container_group_naming_policy: NotRequired[
        pulumi.Input[ElasticProfileContainerGroupNamingPolicyArgsDict]
    ]
    desired_count: NotRequired[pulumi.Input[_builtins.int]]
    maintain_desired_count: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ElasticProfileArgs:
    def __init__(
        __self__,
        *,
        container_group_naming_policy: Optional[
            pulumi.Input[ElasticProfileContainerGroupNamingPolicyArgs]
        ] = ...,
        desired_count: Optional[pulumi.Input[_builtins.int]] = ...,
        maintain_desired_count: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerGroupNamingPolicy")
    def container_group_naming_policy(
        self,
    ) -> Optional[pulumi.Input[ElasticProfileContainerGroupNamingPolicyArgs]]: ...
    @container_group_naming_policy.setter
    def container_group_naming_policy(
        self,
        value: Optional[pulumi.Input[ElasticProfileContainerGroupNamingPolicyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="desiredCount")
    def desired_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @desired_count.setter
    def desired_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maintainDesiredCount")
    def maintain_desired_count(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @maintain_desired_count.setter
    def maintain_desired_count(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class EncryptionPropertiesArgsDict(TypedDict):
    key_name: pulumi.Input[_builtins.str]
    key_version: pulumi.Input[_builtins.str]
    vault_base_url: pulumi.Input[_builtins.str]
    identity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EncryptionPropertiesArgs:
    def __init__(
        __self__,
        *,
        key_name: pulumi.Input[_builtins.str],
        key_version: pulumi.Input[_builtins.str],
        vault_base_url: pulumi.Input[_builtins.str],
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]: ...
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> pulumi.Input[_builtins.str]: ...
    @key_version.setter
    def key_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="vaultBaseUrl")
    def vault_base_url(self) -> pulumi.Input[_builtins.str]: ...
    @vault_base_url.setter
    def vault_base_url(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EnvironmentVariableArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    secure_value: NotRequired[pulumi.Input[_builtins.str]]
    secure_value_reference: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EnvironmentVariableArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        secure_value: Optional[pulumi.Input[_builtins.str]] = ...,
        secure_value_reference: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="secureValue")
    def secure_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secure_value.setter
    def secure_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secureValueReference")
    def secure_value_reference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secure_value_reference.setter
    def secure_value_reference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FileSharePropertiesArgsDict(TypedDict):
    share_access_tier: NotRequired[pulumi.Input[AzureFileShareAccessTier]]
    share_access_type: NotRequired[pulumi.Input[AzureFileShareAccessType]]

@pulumi.input_type
class FileSharePropertiesArgs:
    def __init__(
        __self__,
        *,
        share_access_tier: Optional[pulumi.Input[AzureFileShareAccessTier]] = ...,
        share_access_type: Optional[pulumi.Input[AzureFileShareAccessType]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="shareAccessTier")
    def share_access_tier(self) -> Optional[pulumi.Input[AzureFileShareAccessTier]]: ...
    @share_access_tier.setter
    def share_access_tier(
        self, value: Optional[pulumi.Input[AzureFileShareAccessTier]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="shareAccessType")
    def share_access_type(self) -> Optional[pulumi.Input[AzureFileShareAccessType]]: ...
    @share_access_type.setter
    def share_access_type(
        self, value: Optional[pulumi.Input[AzureFileShareAccessType]]
    ): ...

class FileShareArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[FileSharePropertiesArgsDict]]
    resource_group_name: NotRequired[pulumi.Input[_builtins.str]]
    storage_account_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FileShareArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[FileSharePropertiesArgs]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[FileSharePropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[FileSharePropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GitRepoVolumeArgsDict(TypedDict):
    repository: pulumi.Input[_builtins.str]
    directory: NotRequired[pulumi.Input[_builtins.str]]
    revision: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GitRepoVolumeArgs:
    def __init__(
        __self__,
        *,
        repository: pulumi.Input[_builtins.str],
        directory: Optional[pulumi.Input[_builtins.str]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Input[_builtins.str]: ...
    @repository.setter
    def repository(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def directory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory.setter
    def directory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GpuResourceArgsDict(TypedDict):
    count: pulumi.Input[_builtins.int]
    sku: pulumi.Input[Union[_builtins.str, GpuSku]]

@pulumi.input_type
class GpuResourceArgs:
    def __init__(
        __self__,
        *,
        count: pulumi.Input[_builtins.int],
        sku: pulumi.Input[Union[_builtins.str, GpuSku]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.int]: ...
    @count.setter
    def count(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[Union[_builtins.str, GpuSku]]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[Union[_builtins.str, GpuSku]]): ...

class HttpHeaderArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class HttpHeaderArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ImageRegistryCredentialArgsDict(TypedDict):
    server: pulumi.Input[_builtins.str]
    identity: NotRequired[pulumi.Input[_builtins.str]]
    identity_url: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]
    password_reference: NotRequired[pulumi.Input[_builtins.str]]
    username: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ImageRegistryCredentialArgs:
    def __init__(
        __self__,
        *,
        server: pulumi.Input[_builtins.str],
        identity: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_url: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
        password_reference: Optional[pulumi.Input[_builtins.str]] = ...,
        username: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]: ...
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityUrl")
    def identity_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_url.setter
    def identity_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="passwordReference")
    def password_reference(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password_reference.setter
    def password_reference(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InitContainerDefinitionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    command: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    environment_variables: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgsDict]]]
    ]
    image: NotRequired[pulumi.Input[_builtins.str]]
    security_context: NotRequired[pulumi.Input[SecurityContextDefinitionArgsDict]]
    volume_mounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VolumeMountArgsDict]]]
    ]

@pulumi.input_type
class InitContainerDefinitionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        command: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        environment_variables: Optional[
            pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]
        ] = ...,
        image: Optional[pulumi.Input[_builtins.str]] = ...,
        security_context: Optional[pulumi.Input[SecurityContextDefinitionArgs]] = ...,
        volume_mounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def command(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @command.setter
    def command(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityContext")
    def security_context(
        self,
    ) -> Optional[pulumi.Input[SecurityContextDefinitionArgs]]: ...
    @security_context.setter
    def security_context(
        self, value: Optional[pulumi.Input[SecurityContextDefinitionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]: ...
    @volume_mounts.setter
    def volume_mounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]
    ): ...

class IpAddressArgsDict(TypedDict):
    ports: pulumi.Input[Sequence[pulumi.Input[PortArgsDict]]]
    type: pulumi.Input[Union[_builtins.str, ContainerGroupIpAddressType]]
    auto_generated_domain_name_label_scope: NotRequired[
        pulumi.Input[Union[_builtins.str, DnsNameLabelReusePolicy]]
    ]
    dns_name_label: NotRequired[pulumi.Input[_builtins.str]]
    ip: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IpAddressArgs:
    def __init__(
        __self__,
        *,
        ports: pulumi.Input[Sequence[pulumi.Input[PortArgs]]],
        type: pulumi.Input[Union[_builtins.str, ContainerGroupIpAddressType]],
        auto_generated_domain_name_label_scope: Optional[
            pulumi.Input[Union[_builtins.str, DnsNameLabelReusePolicy]]
        ] = ...,
        dns_name_label: Optional[pulumi.Input[_builtins.str]] = ...,
        ip: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> pulumi.Input[Sequence[pulumi.Input[PortArgs]]]: ...
    @ports.setter
    def ports(self, value: pulumi.Input[Sequence[pulumi.Input[PortArgs]]]): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> pulumi.Input[Union[_builtins.str, ContainerGroupIpAddressType]]: ...
    @type.setter
    def type(
        self, value: pulumi.Input[Union[_builtins.str, ContainerGroupIpAddressType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="autoGeneratedDomainNameLabelScope")
    def auto_generated_domain_name_label_scope(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, DnsNameLabelReusePolicy]]]: ...
    @auto_generated_domain_name_label_scope.setter
    def auto_generated_domain_name_label_scope(
        self,
        value: Optional[pulumi.Input[Union[_builtins.str, DnsNameLabelReusePolicy]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dnsNameLabel")
    def dns_name_label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dns_name_label.setter
    def dns_name_label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip.setter
    def ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LoadBalancerBackendAddressPoolArgsDict(TypedDict):
    resource: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LoadBalancerBackendAddressPoolArgs:
    def __init__(
        __self__, *, resource: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def resource(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource.setter
    def resource(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LoadBalancerArgsDict(TypedDict):
    backend_address_pools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[LoadBalancerBackendAddressPoolArgsDict]]]
    ]

@pulumi.input_type
class LoadBalancerArgs:
    def __init__(
        __self__,
        *,
        backend_address_pools: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancerBackendAddressPoolArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[LoadBalancerBackendAddressPoolArgs]]]
    ]: ...
    @backend_address_pools.setter
    def backend_address_pools(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[LoadBalancerBackendAddressPoolArgs]]]
        ],
    ): ...

class LogAnalyticsArgsDict(TypedDict):
    workspace_id: pulumi.Input[_builtins.str]
    workspace_key: pulumi.Input[_builtins.str]
    log_type: NotRequired[pulumi.Input[Union[_builtins.str, LogAnalyticsLogType]]]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    workspace_resource_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LogAnalyticsArgs:
    def __init__(
        __self__,
        *,
        workspace_id: pulumi.Input[_builtins.str],
        workspace_key: pulumi.Input[_builtins.str],
        log_type: Optional[
            pulumi.Input[Union[_builtins.str, LogAnalyticsLogType]]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        workspace_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workspaceKey")
    def workspace_key(self) -> pulumi.Input[_builtins.str]: ...
    @workspace_key.setter
    def workspace_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, LogAnalyticsLogType]]]: ...
    @log_type.setter
    def log_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, LogAnalyticsLogType]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workspace_resource_id.setter
    def workspace_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NGroupCGPropertyContainerPropertiesArgsDict(TypedDict):
    volume_mounts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[VolumeMountArgsDict]]]
    ]

@pulumi.input_type
class NGroupCGPropertyContainerPropertiesArgs:
    def __init__(
        __self__,
        *,
        volume_mounts: Optional[
            pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]: ...
    @volume_mounts.setter
    def volume_mounts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeMountArgs]]]]
    ): ...

class NGroupCGPropertyContainerArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[NGroupCGPropertyContainerPropertiesArgsDict]]

@pulumi.input_type
class NGroupCGPropertyContainerArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[
            pulumi.Input[NGroupCGPropertyContainerPropertiesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[NGroupCGPropertyContainerPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[NGroupCGPropertyContainerPropertiesArgs]]
    ): ...

class NGroupCGPropertyVolumeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    azure_file: NotRequired[pulumi.Input[AzureFileVolumeArgsDict]]

@pulumi.input_type
class NGroupCGPropertyVolumeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        azure_file: Optional[pulumi.Input[AzureFileVolumeArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="azureFile")
    def azure_file(self) -> Optional[pulumi.Input[AzureFileVolumeArgs]]: ...
    @azure_file.setter
    def azure_file(self, value: Optional[pulumi.Input[AzureFileVolumeArgs]]): ...

class NGroupContainerGroupPropertiesArgsDict(TypedDict):
    containers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NGroupCGPropertyContainerArgsDict]]]
    ]
    subnet_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ContainerGroupSubnetIdArgsDict]]]
    ]
    volumes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[NGroupCGPropertyVolumeArgsDict]]]
    ]

@pulumi.input_type
class NGroupContainerGroupPropertiesArgs:
    def __init__(
        __self__,
        *,
        containers: Optional[
            pulumi.Input[Sequence[pulumi.Input[NGroupCGPropertyContainerArgs]]]
        ] = ...,
        subnet_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerGroupSubnetIdArgs]]]
        ] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[NGroupCGPropertyVolumeArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[NGroupCGPropertyContainerArgs]]]
    ]: ...
    @containers.setter
    def containers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NGroupCGPropertyContainerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerGroupSubnetIdArgs]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ContainerGroupSubnetIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[NGroupCGPropertyVolumeArgs]]]]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[NGroupCGPropertyVolumeArgs]]]
        ],
    ): ...

class NGroupIdentityArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[ResourceIdentityType]]
    user_assigned_identities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class NGroupIdentityArgs:
    def __init__(
        __self__,
        *,
        type: Optional[pulumi.Input[ResourceIdentityType]] = ...,
        user_assigned_identities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[ResourceIdentityType]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[ResourceIdentityType]]): ...
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_assigned_identities.setter
    def user_assigned_identities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class NetworkProfileArgsDict(TypedDict):
    application_gateway: NotRequired[pulumi.Input[ApplicationGatewayArgsDict]]
    load_balancer: NotRequired[pulumi.Input[LoadBalancerArgsDict]]

@pulumi.input_type
class NetworkProfileArgs:
    def __init__(
        __self__,
        *,
        application_gateway: Optional[pulumi.Input[ApplicationGatewayArgs]] = ...,
        load_balancer: Optional[pulumi.Input[LoadBalancerArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationGateway")
    def application_gateway(self) -> Optional[pulumi.Input[ApplicationGatewayArgs]]: ...
    @application_gateway.setter
    def application_gateway(
        self, value: Optional[pulumi.Input[ApplicationGatewayArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> Optional[pulumi.Input[LoadBalancerArgs]]: ...
    @load_balancer.setter
    def load_balancer(self, value: Optional[pulumi.Input[LoadBalancerArgs]]): ...

class PlacementProfileArgsDict(TypedDict):
    fault_domain_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class PlacementProfileArgs:
    def __init__(
        __self__, *, fault_domain_count: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="faultDomainCount")
    def fault_domain_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @fault_domain_count.setter
    def fault_domain_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class PortArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    protocol: NotRequired[
        pulumi.Input[Union[_builtins.str, ContainerGroupNetworkProtocol]]
    ]

@pulumi.input_type
class PortArgs:
    def __init__(
        __self__,
        *,
        port: pulumi.Input[_builtins.int],
        protocol: Optional[
            pulumi.Input[Union[_builtins.str, ContainerGroupNetworkProtocol]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, ContainerGroupNetworkProtocol]]
    ]: ...
    @protocol.setter
    def protocol(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, ContainerGroupNetworkProtocol]]
        ],
    ): ...

class ResourceLimitsArgsDict(TypedDict):
    cpu: NotRequired[pulumi.Input[_builtins.float]]
    gpu: NotRequired[pulumi.Input[GpuResourceArgsDict]]
    memory_in_gb: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ResourceLimitsArgs:
    def __init__(
        __self__,
        *,
        cpu: Optional[pulumi.Input[_builtins.float]] = ...,
        gpu: Optional[pulumi.Input[GpuResourceArgs]] = ...,
        memory_in_gb: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def gpu(self) -> Optional[pulumi.Input[GpuResourceArgs]]: ...
    @gpu.setter
    def gpu(self, value: Optional[pulumi.Input[GpuResourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryInGB")
    def memory_in_gb(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @memory_in_gb.setter
    def memory_in_gb(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ResourceRequestsArgsDict(TypedDict):
    cpu: pulumi.Input[_builtins.float]
    memory_in_gb: pulumi.Input[_builtins.float]
    gpu: NotRequired[pulumi.Input[GpuResourceArgsDict]]

@pulumi.input_type
class ResourceRequestsArgs:
    def __init__(
        __self__,
        *,
        cpu: pulumi.Input[_builtins.float],
        memory_in_gb: pulumi.Input[_builtins.float],
        gpu: Optional[pulumi.Input[GpuResourceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[_builtins.float]: ...
    @cpu.setter
    def cpu(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="memoryInGB")
    def memory_in_gb(self) -> pulumi.Input[_builtins.float]: ...
    @memory_in_gb.setter
    def memory_in_gb(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def gpu(self) -> Optional[pulumi.Input[GpuResourceArgs]]: ...
    @gpu.setter
    def gpu(self, value: Optional[pulumi.Input[GpuResourceArgs]]): ...

class ResourceRequirementsArgsDict(TypedDict):
    requests: pulumi.Input[ResourceRequestsArgsDict]
    limits: NotRequired[pulumi.Input[ResourceLimitsArgsDict]]

@pulumi.input_type
class ResourceRequirementsArgs:
    def __init__(
        __self__,
        *,
        requests: pulumi.Input[ResourceRequestsArgs],
        limits: Optional[pulumi.Input[ResourceLimitsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> pulumi.Input[ResourceRequestsArgs]: ...
    @requests.setter
    def requests(self, value: pulumi.Input[ResourceRequestsArgs]): ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[ResourceLimitsArgs]]: ...
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[ResourceLimitsArgs]]): ...

class SecurityContextCapabilitiesDefinitionArgsDict(TypedDict):
    add: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    drop: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class SecurityContextCapabilitiesDefinitionArgs:
    def __init__(
        __self__,
        *,
        add: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        drop: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def add(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @add.setter
    def add(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def drop(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @drop.setter
    def drop(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class SecurityContextDefinitionArgsDict(TypedDict):
    allow_privilege_escalation: NotRequired[pulumi.Input[_builtins.bool]]
    capabilities: NotRequired[
        pulumi.Input[SecurityContextCapabilitiesDefinitionArgsDict]
    ]
    privileged: NotRequired[pulumi.Input[_builtins.bool]]
    run_as_group: NotRequired[pulumi.Input[_builtins.int]]
    run_as_user: NotRequired[pulumi.Input[_builtins.int]]
    seccomp_profile: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SecurityContextDefinitionArgs:
    def __init__(
        __self__,
        *,
        allow_privilege_escalation: Optional[pulumi.Input[_builtins.bool]] = ...,
        capabilities: Optional[
            pulumi.Input[SecurityContextCapabilitiesDefinitionArgs]
        ] = ...,
        privileged: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_as_group: Optional[pulumi.Input[_builtins.int]] = ...,
        run_as_user: Optional[pulumi.Input[_builtins.int]] = ...,
        seccomp_profile: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPrivilegeEscalation")
    def allow_privilege_escalation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_privilege_escalation.setter
    def allow_privilege_escalation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def capabilities(
        self,
    ) -> Optional[pulumi.Input[SecurityContextCapabilitiesDefinitionArgs]]: ...
    @capabilities.setter
    def capabilities(
        self, value: Optional[pulumi.Input[SecurityContextCapabilitiesDefinitionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def privileged(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @privileged.setter
    def privileged(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="runAsGroup")
    def run_as_group(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @run_as_group.setter
    def run_as_group(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @run_as_user.setter
    def run_as_user(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="seccompProfile")
    def seccomp_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @seccomp_profile.setter
    def seccomp_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StandbyPoolProfileDefinitionArgsDict(TypedDict):
    fail_container_group_create_on_reuse_failure: NotRequired[
        pulumi.Input[_builtins.bool]
    ]
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class StandbyPoolProfileDefinitionArgs:
    def __init__(
        __self__,
        *,
        fail_container_group_create_on_reuse_failure: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failContainerGroupCreateOnReuseFailure")
    def fail_container_group_create_on_reuse_failure(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_container_group_create_on_reuse_failure.setter
    def fail_container_group_create_on_reuse_failure(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class StorageProfileArgsDict(TypedDict):
    file_shares: NotRequired[pulumi.Input[Sequence[pulumi.Input[FileShareArgsDict]]]]

@pulumi.input_type
class StorageProfileArgs:
    def __init__(
        __self__,
        *,
        file_shares: Optional[
            pulumi.Input[Sequence[pulumi.Input[FileShareArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileShares")
    def file_shares(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FileShareArgs]]]]: ...
    @file_shares.setter
    def file_shares(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FileShareArgs]]]]
    ): ...

class UpdateProfileRollingUpdateProfileArgsDict(TypedDict):
    in_place_update: NotRequired[pulumi.Input[_builtins.bool]]
    max_batch_percent: NotRequired[pulumi.Input[_builtins.int]]
    max_unhealthy_percent: NotRequired[pulumi.Input[_builtins.int]]
    pause_time_between_batches: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class UpdateProfileRollingUpdateProfileArgs:
    def __init__(
        __self__,
        *,
        in_place_update: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_batch_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        max_unhealthy_percent: Optional[pulumi.Input[_builtins.int]] = ...,
        pause_time_between_batches: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inPlaceUpdate")
    def in_place_update(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @in_place_update.setter
    def in_place_update(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxBatchPercent")
    def max_batch_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_batch_percent.setter
    def max_batch_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxUnhealthyPercent")
    def max_unhealthy_percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_unhealthy_percent.setter
    def max_unhealthy_percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="pauseTimeBetweenBatches")
    def pause_time_between_batches(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pause_time_between_batches.setter
    def pause_time_between_batches(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class UpdateProfileArgsDict(TypedDict):
    rolling_update_profile: NotRequired[
        pulumi.Input[UpdateProfileRollingUpdateProfileArgsDict]
    ]
    update_mode: NotRequired[pulumi.Input[Union[_builtins.str, NGroupUpdateMode]]]

@pulumi.input_type
class UpdateProfileArgs:
    def __init__(
        __self__,
        *,
        rolling_update_profile: Optional[
            pulumi.Input[UpdateProfileRollingUpdateProfileArgs]
        ] = ...,
        update_mode: Optional[
            pulumi.Input[Union[_builtins.str, NGroupUpdateMode]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="rollingUpdateProfile")
    def rolling_update_profile(
        self,
    ) -> Optional[pulumi.Input[UpdateProfileRollingUpdateProfileArgs]]: ...
    @rolling_update_profile.setter
    def rolling_update_profile(
        self, value: Optional[pulumi.Input[UpdateProfileRollingUpdateProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateMode")
    def update_mode(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, NGroupUpdateMode]]]: ...
    @update_mode.setter
    def update_mode(
        self, value: Optional[pulumi.Input[Union[_builtins.str, NGroupUpdateMode]]]
    ): ...

class VolumeMountArgsDict(TypedDict):
    mount_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class VolumeMountArgs:
    def __init__(
        __self__,
        *,
        mount_path: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @mount_path.setter
    def mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class VolumeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    azure_file: NotRequired[pulumi.Input[AzureFileVolumeArgsDict]]
    empty_dir: NotRequired[Any]
    git_repo: NotRequired[pulumi.Input[GitRepoVolumeArgsDict]]
    secret: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    secret_reference: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class VolumeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        azure_file: Optional[pulumi.Input[AzureFileVolumeArgs]] = ...,
        empty_dir: Optional[Any] = ...,
        git_repo: Optional[pulumi.Input[GitRepoVolumeArgs]] = ...,
        secret: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        secret_reference: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="azureFile")
    def azure_file(self) -> Optional[pulumi.Input[AzureFileVolumeArgs]]: ...
    @azure_file.setter
    def azure_file(self, value: Optional[pulumi.Input[AzureFileVolumeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(self) -> Optional[Any]: ...
    @empty_dir.setter
    def empty_dir(self, value: Optional[Any]): ...
    @_builtins.property
    @pulumi.getter(name="gitRepo")
    def git_repo(self) -> Optional[pulumi.Input[GitRepoVolumeArgs]]: ...
    @git_repo.setter
    def git_repo(self, value: Optional[pulumi.Input[GitRepoVolumeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def secret(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @secret.setter
    def secret(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretReference")
    def secret_reference(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @secret_reference.setter
    def secret_reference(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
