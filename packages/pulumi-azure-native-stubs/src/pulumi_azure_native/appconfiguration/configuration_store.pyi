import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ConfigurationStoreArgs", "ConfigurationStore"]

@pulumi.input_type
class ConfigurationStoreArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[SkuArgs],
        config_store_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[CreateMode]] = ...,
        data_plane_proxy: Optional[pulumi.Input[DataPlaneProxyPropertiesArgs]] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_purge_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption: Optional[pulumi.Input[EncryptionPropertiesArgs]] = ...,
        identity: Optional[pulumi.Input[ResourceIdentityArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        soft_delete_retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
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
    @pulumi.getter(name="configStoreName")
    def config_store_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @config_store_name.setter
    def config_store_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[CreateMode]]: ...
    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[CreateMode]]): ...
    @_builtins.property
    @pulumi.getter(name="dataPlaneProxy")
    def data_plane_proxy(
        self,
    ) -> Optional[pulumi.Input[DataPlaneProxyPropertiesArgs]]: ...
    @data_plane_proxy.setter
    def data_plane_proxy(
        self, value: Optional[pulumi.Input[DataPlaneProxyPropertiesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enablePurgeProtection")
    def enable_purge_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_purge_protection.setter
    def enable_purge_protection(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[EncryptionPropertiesArgs]]: ...
    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[EncryptionPropertiesArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ResourceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ResourceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="softDeleteRetentionInDays")
    def soft_delete_retention_in_days(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @soft_delete_retention_in_days.setter
    def soft_delete_retention_in_days(
        self, value: Optional[pulumi.Input[_builtins.int]]
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

@pulumi.type_token("azure-native:appconfiguration:ConfigurationStore")
class ConfigurationStore(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        config_store_name: Optional[pulumi.Input[_builtins.str]] = ...,
        create_mode: Optional[pulumi.Input[CreateMode]] = ...,
        data_plane_proxy: Optional[
            pulumi.Input[
                Union[DataPlaneProxyPropertiesArgs, DataPlaneProxyPropertiesArgsDict]
            ]
        ] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_purge_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        encryption: Optional[
            pulumi.Input[Union[EncryptionPropertiesArgs, EncryptionPropertiesArgsDict]]
        ] = ...,
        identity: Optional[
            pulumi.Input[Union[ResourceIdentityArgs, ResourceIdentityArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        soft_delete_retention_in_days: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ConfigurationStoreArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ConfigurationStore: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataPlaneProxy")
    def data_plane_proxy(
        self,
    ) -> pulumi.Output[Optional[outputs.DataPlaneProxyPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="enablePurgeProtection")
    def enable_purge_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(
        self,
    ) -> pulumi.Output[Optional[outputs.EncryptionPropertiesResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.ResourceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[
        Sequence[outputs.PrivateEndpointConnectionReferenceResponse]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionInDays")
    def soft_delete_retention_in_days(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
