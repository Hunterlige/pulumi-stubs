import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetConfigurationStoreResult",
    "AwaitableGetConfigurationStoreResult",
    "get_configuration_store",
    "get_configuration_store_output",
]

@pulumi.output_type
class GetConfigurationStoreResult:
    def __init__(
        __self__,
        azure_api_version=...,
        creation_date=...,
        data_plane_proxy=...,
        disable_local_auth=...,
        enable_purge_protection=...,
        encryption=...,
        endpoint=...,
        id=...,
        identity=...,
        location=...,
        name=...,
        private_endpoint_connections=...,
        provisioning_state=...,
        public_network_access=...,
        sku=...,
        soft_delete_retention_in_days=...,
        system_data=...,
        tags=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataPlaneProxy")
    def data_plane_proxy(
        self,
    ) -> Optional[outputs.DataPlaneProxyPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePurgeProtection")
    def enable_purge_protection(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def encryption(self) -> Optional[outputs.EncryptionPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ResourceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionReferenceResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> outputs.SkuResponse: ...
    @_builtins.property
    @pulumi.getter(name="softDeleteRetentionInDays")
    def soft_delete_retention_in_days(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetConfigurationStoreResult(GetConfigurationStoreResult):
    def __await__(self): ...

def get_configuration_store(
    config_store_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetConfigurationStoreResult: ...
def get_configuration_store_output(
    config_store_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetConfigurationStoreResult]: ...
