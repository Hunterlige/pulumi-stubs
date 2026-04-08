import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["NamespaceArgs", "Namespace"]

@pulumi.input_type
class NamespaceArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        alternate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption: Optional[pulumi.Input[EncryptionArgs]] = ...,
        identity: Optional[pulumi.Input[IdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, TlsVersion]]
        ] = ...,
        namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        premium_messaging_partitions: Optional[pulumi.Input[_builtins.int]] = ...,
        private_endpoint_connections: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        sku: Optional[pulumi.Input[SBSkuArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alternate_name.setter
    def alternate_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionArgs]]: ...
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): ...
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
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="premiumMessagingPartitions")
    def premium_messaging_partitions(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @premium_messaging_partitions.setter
    def premium_messaging_partitions(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]
    ]: ...
    @private_endpoint_connections.setter
    def private_endpoint_connections(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[PrivateEndpointConnectionArgs]]]
        ],
    ): ...
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
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[SBSkuArgs]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[SBSkuArgs]]): ...
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
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @zone_redundant.setter
    def zone_redundant(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("azure-native:servicebus:Namespace")
class Namespace(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        alternate_name: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption: Optional[
            pulumi.Input[Union[EncryptionArgs, EncryptionArgsDict]]
        ] = ...,
        identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        minimum_tls_version: Optional[
            pulumi.Input[Union[_builtins.str, TlsVersion]]
        ] = ...,
        namespace_name: Optional[pulumi.Input[_builtins.str]] = ...,
        premium_messaging_partitions: Optional[pulumi.Input[_builtins.int]] = ...,
        private_endpoint_connections: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            PrivateEndpointConnectionArgs,
                            PrivateEndpointConnectionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SBSkuArgs, SBSkuArgsDict]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: NamespaceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Namespace: ...
    @_builtins.property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional[outputs.EncryptionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metricId")
    def metric_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="premiumMessagingPartitions")
    def premium_messaging_partitions(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.PrivateEndpointConnectionResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceBusEndpoint")
    def service_bus_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[outputs.SBSkuResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
