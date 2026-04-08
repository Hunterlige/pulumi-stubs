import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDomainServiceResult",
    "AwaitableGetDomainServiceResult",
    "get_domain_service",
    "get_domain_service_output",
]

@pulumi.output_type
class GetDomainServiceResult:
    def __init__(
        __self__,
        azure_api_version=...,
        config_diagnostics=...,
        deployment_id=...,
        domain_configuration_type=...,
        domain_name=...,
        domain_security_settings=...,
        etag=...,
        filtered_sync=...,
        id=...,
        ldaps_settings=...,
        location=...,
        migration_properties=...,
        name=...,
        notification_settings=...,
        provisioning_state=...,
        replica_sets=...,
        resource_forest_settings=...,
        sku=...,
        sync_application_id=...,
        sync_owner=...,
        sync_scope=...,
        system_data=...,
        tags=...,
        tenant_id=...,
        type=...,
        version=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="configDiagnostics")
    def config_diagnostics(self) -> Optional[outputs.ConfigDiagnosticsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="domainConfigurationType")
    def domain_configuration_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainSecuritySettings")
    def domain_security_settings(
        self,
    ) -> Optional[outputs.DomainSecuritySettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filteredSync")
    def filtered_sync(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ldapsSettings")
    def ldaps_settings(self) -> Optional[outputs.LdapsSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="migrationProperties")
    def migration_properties(self) -> outputs.MigrationPropertiesResponse: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> Optional[outputs.NotificationSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="replicaSets")
    def replica_sets(self) -> Optional[Sequence[outputs.ReplicaSetResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceForestSettings")
    def resource_forest_settings(
        self,
    ) -> Optional[outputs.ResourceForestSettingsResponse]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncApplicationId")
    def sync_application_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncOwner")
    def sync_owner(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="syncScope")
    def sync_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.int: ...

class AwaitableGetDomainServiceResult(GetDomainServiceResult):
    def __await__(self): ...

def get_domain_service(
    domain_service_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDomainServiceResult: ...
def get_domain_service_output(
    domain_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDomainServiceResult]: ...
