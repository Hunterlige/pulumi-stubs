import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetSingleServerResult",
    "AwaitableGetSingleServerResult",
    "get_single_server",
    "get_single_server_output",
]

@pulumi.output_type
class GetSingleServerResult:
    def __init__(
        __self__,
        administrator_login=...,
        azure_api_version=...,
        byok_enforcement=...,
        earliest_restore_date=...,
        fully_qualified_domain_name=...,
        id=...,
        identity=...,
        infrastructure_encryption=...,
        location=...,
        master_server_id=...,
        minimal_tls_version=...,
        name=...,
        private_endpoint_connections=...,
        public_network_access=...,
        replica_capacity=...,
        replication_role=...,
        sku=...,
        ssl_enforcement=...,
        storage_profile=...,
        tags=...,
        type=...,
        user_visible_state=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="byokEnforcement")
    def byok_enforcement(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="earliestRestoreDate")
    def earliest_restore_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ResourceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="masterServerId")
    def master_server_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minimalTlsVersion")
    def minimal_tls_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.ServerPrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCapacity")
    def replica_capacity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SingleServerSkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[outputs.StorageProfileResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userVisibleState")
    def user_visible_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetSingleServerResult(GetSingleServerResult):
    def __await__(self): ...

def get_single_server(
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetSingleServerResult: ...
def get_single_server_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetSingleServerResult]: ...
