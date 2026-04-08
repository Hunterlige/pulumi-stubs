import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RedisEnterpriseArgs", "RedisEnterprise"]

@pulumi.input_type
class RedisEnterpriseArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[SkuArgs],
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption: Optional[pulumi.Input[ClusterPropertiesEncryptionArgs]] = ...,
        high_availability: Optional[
            pulumi.Input[Union[_builtins.str, HighAvailability]]
        ] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, TlsVersion]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[SkuArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[ClusterPropertiesEncryptionArgs]]: ...
    @encryption.setter
    def encryption(
        self, value: Optional[pulumi.Input[ClusterPropertiesEncryptionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="highAvailability")
    def high_availability(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, HighAvailability]]]: ...
    @high_availability.setter
    def high_availability(
        self, value: Optional[pulumi.Input[Union[_builtins.str, HighAvailability]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]]: ...
    @minimum_tls_version.setter
    def minimum_tls_version(
        self, value: Optional[pulumi.Input[Union[_builtins.str, TlsVersion]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @zones.setter
    def zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:redisenterprise:RedisEnterprise")
class RedisEnterprise(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption: Optional[
            pulumi.Input[
                Union[
                    ClusterPropertiesEncryptionArgs, ClusterPropertiesEncryptionArgsDict
                ]
            ]
        ] = ...,
        high_availability: Optional[
            pulumi.Input[Union[_builtins.str, HighAvailability]]
        ] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, TlsVersion]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RedisEnterpriseArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> RedisEnterprise: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> pulumi.Output[Optional[outputs.ClusterPropertiesResponseEncryption]]: ...
    @_builtins.property
    @pulumi.getter(name="highAvailability")
    def high_availability(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redundancyMode")
    def redundancy_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
