import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RedisArgs", "Redis"]

@pulumi.input_type
class RedisArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[SkuArgs],
        disable_access_key_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_non_ssl_port: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, TlsVersion]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        redis_configuration: Optional[
            pulumi.Input[RedisCommonPropertiesRedisConfigurationArgs]
        ] = ...,
        redis_version: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas_per_master: Optional[pulumi.Input[_builtins.int]] = ...,
        replicas_per_primary: Optional[pulumi.Input[_builtins.int]] = ...,
        shard_count: Optional[pulumi.Input[_builtins.int]] = ...,
        static_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tenant_settings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_channel: Optional[
            pulumi.Input[Union[_builtins.str, UpdateChannel]]
        ] = ...,
        zonal_allocation_policy: Optional[
            pulumi.Input[Union[_builtins.str, ZonalAllocationPolicy]]
        ] = ...,
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
    @pulumi.getter(name="disableAccessKeyAuthentication")
    def disable_access_key_authentication(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_access_key_authentication.setter
    def disable_access_key_authentication(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableNonSslPort")
    def enable_non_ssl_port(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_non_ssl_port.setter
    def enable_non_ssl_port(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redisConfiguration")
    def redis_configuration(
        self,
    ) -> Optional[pulumi.Input[RedisCommonPropertiesRedisConfigurationArgs]]: ...
    @redis_configuration.setter
    def redis_configuration(
        self, value: Optional[pulumi.Input[RedisCommonPropertiesRedisConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redis_version.setter
    def redis_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicasPerMaster")
    def replicas_per_master(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replicas_per_master.setter
    def replicas_per_master(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="replicasPerPrimary")
    def replicas_per_primary(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @replicas_per_primary.setter
    def replicas_per_primary(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @shard_count.setter
    def shard_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="staticIP")
    def static_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @static_ip.setter
    def static_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnet_id.setter
    def subnet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="tenantSettings")
    def tenant_settings(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tenant_settings.setter
    def tenant_settings(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateChannel")
    def update_channel(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, UpdateChannel]]]: ...
    @update_channel.setter
    def update_channel(
        self, value: Optional[pulumi.Input[Union[_builtins.str, UpdateChannel]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="zonalAllocationPolicy")
    def zonal_allocation_policy(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ZonalAllocationPolicy]]]: ...
    @zonal_allocation_policy.setter
    def zonal_allocation_policy(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ZonalAllocationPolicy]]]
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

@pulumi.type_token("azure-native:redis:Redis")
class Redis(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        disable_access_key_authentication: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_non_ssl_port: Optional[pulumi.Input[_builtins.bool]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, TlsVersion]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        redis_configuration: Optional[
            pulumi.Input[
                Union[
                    RedisCommonPropertiesRedisConfigurationArgs,
                    RedisCommonPropertiesRedisConfigurationArgsDict,
                ]
            ]
        ] = ...,
        redis_version: Optional[pulumi.Input[_builtins.str]] = ...,
        replicas_per_master: Optional[pulumi.Input[_builtins.int]] = ...,
        replicas_per_primary: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        shard_count: Optional[pulumi.Input[_builtins.int]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        static_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        subnet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tenant_settings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        update_channel: Optional[
            pulumi.Input[Union[_builtins.str, UpdateChannel]]
        ] = ...,
        zonal_allocation_policy: Optional[
            pulumi.Input[Union[_builtins.str, ZonalAllocationPolicy]]
        ] = ...,
        zones: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RedisArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Redis: ...
    @_builtins.property
    @pulumi.getter(name="accessKeys")
    def access_keys(self) -> pulumi.Output[outputs.RedisAccessKeysResponse]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableAccessKeyAuthentication")
    def disable_access_key_authentication(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enableNonSslPort")
    def enable_non_ssl_port(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
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
    def instances(
        self,
    ) -> pulumi.Output[Sequence[outputs.RedisInstanceDetailsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedServers")
    def linked_servers(
        self,
    ) -> pulumi.Output[Sequence[outputs.RedisLinkedServerResponse]]: ...
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
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="redisConfiguration")
    def redis_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RedisCommonPropertiesRedisConfigurationResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="replicasPerMaster")
    def replicas_per_master(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="replicasPerPrimary")
    def replicas_per_primary(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sslPort")
    def ssl_port(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="staticIP")
    def static_ip(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tenantSettings")
    def tenant_settings(
        self,
    ) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateChannel")
    def update_channel(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="zonalAllocationPolicy")
    def zonal_allocation_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
