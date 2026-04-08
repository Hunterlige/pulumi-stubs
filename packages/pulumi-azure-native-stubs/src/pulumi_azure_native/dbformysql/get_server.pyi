import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetServerResult",
    "AwaitableGetServerResult",
    "get_server",
    "get_server_output",
]

@pulumi.output_type
class GetServerResult:
    def __init__(
        __self__,
        administrator_login=...,
        availability_zone=...,
        azure_api_version=...,
        backup=...,
        data_encryption=...,
        fully_qualified_domain_name=...,
        high_availability=...,
        id=...,
        identity=...,
        import_source_properties=...,
        location=...,
        maintenance_window=...,
        name=...,
        network=...,
        private_endpoint_connections=...,
        replica_capacity=...,
        replication_role=...,
        sku=...,
        source_server_resource_id=...,
        state=...,
        storage=...,
        system_data=...,
        tags=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def backup(self) -> Optional[outputs.BackupResponse]: ...
    @_builtins.property
    @pulumi.getter(name="dataEncryption")
    def data_encryption(self) -> Optional[outputs.DataEncryptionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="highAvailability")
    def high_availability(self) -> Optional[outputs.HighAvailabilityResponse]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.MySQLServerIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="importSourceProperties")
    def import_source_properties(
        self,
    ) -> Optional[outputs.ImportSourcePropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[outputs.MaintenanceWindowResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[outputs.NetworkResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="replicaCapacity")
    def replica_capacity(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.MySQLServerSkuResponse]: ...
    @_builtins.property
    @pulumi.getter(name="sourceServerResourceId")
    def source_server_resource_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def storage(self) -> Optional[outputs.StorageResponse]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

class AwaitableGetServerResult(GetServerResult):
    def __await__(self): ...

def get_server(
    resource_group_name: Optional[_builtins.str] = ...,
    server_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetServerResult: ...
def get_server_output(
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    server_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetServerResult]: ...
