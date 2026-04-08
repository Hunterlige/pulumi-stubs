import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DomainServiceArgs", "DomainService"]

@pulumi.input_type
class DomainServiceArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        config_diagnostics: Optional[pulumi.Input[ConfigDiagnosticsArgs]] = ...,
        domain_configuration_type: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_security_settings: Optional[
            pulumi.Input[DomainSecuritySettingsArgs]
        ] = ...,
        domain_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        filtered_sync: Optional[pulumi.Input[Union[_builtins.str, FilteredSync]]] = ...,
        ldaps_settings: Optional[pulumi.Input[LdapsSettingsArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_settings: Optional[pulumi.Input[NotificationSettingsArgs]] = ...,
        replica_sets: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReplicaSetArgs]]]
        ] = ...,
        resource_forest_settings: Optional[
            pulumi.Input[ResourceForestSettingsArgs]
        ] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_scope: Optional[pulumi.Input[Union[_builtins.str, SyncScope]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="configDiagnostics")
    def config_diagnostics(self) -> Optional[pulumi.Input[ConfigDiagnosticsArgs]]: ...
    @config_diagnostics.setter
    def config_diagnostics(
        self, value: Optional[pulumi.Input[ConfigDiagnosticsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainConfigurationType")
    def domain_configuration_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_configuration_type.setter
    def domain_configuration_type(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainSecuritySettings")
    def domain_security_settings(
        self,
    ) -> Optional[pulumi.Input[DomainSecuritySettingsArgs]]: ...
    @domain_security_settings.setter
    def domain_security_settings(
        self, value: Optional[pulumi.Input[DomainSecuritySettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="domainServiceName")
    def domain_service_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_service_name.setter
    def domain_service_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filteredSync")
    def filtered_sync(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, FilteredSync]]]: ...
    @filtered_sync.setter
    def filtered_sync(
        self, value: Optional[pulumi.Input[Union[_builtins.str, FilteredSync]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ldapsSettings")
    def ldaps_settings(self) -> Optional[pulumi.Input[LdapsSettingsArgs]]: ...
    @ldaps_settings.setter
    def ldaps_settings(self, value: Optional[pulumi.Input[LdapsSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> Optional[pulumi.Input[NotificationSettingsArgs]]: ...
    @notification_settings.setter
    def notification_settings(
        self, value: Optional[pulumi.Input[NotificationSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaSets")
    def replica_sets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReplicaSetArgs]]]]: ...
    @replica_sets.setter
    def replica_sets(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ReplicaSetArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceForestSettings")
    def resource_forest_settings(
        self,
    ) -> Optional[pulumi.Input[ResourceForestSettingsArgs]]: ...
    @resource_forest_settings.setter
    def resource_forest_settings(
        self, value: Optional[pulumi.Input[ResourceForestSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sku.setter
    def sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="syncScope")
    def sync_scope(self) -> Optional[pulumi.Input[Union[_builtins.str, SyncScope]]]: ...
    @sync_scope.setter
    def sync_scope(
        self, value: Optional[pulumi.Input[Union[_builtins.str, SyncScope]]]
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

@pulumi.type_token("azure-native:aad:DomainService")
class DomainService(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        config_diagnostics: Optional[
            pulumi.Input[Union[ConfigDiagnosticsArgs, ConfigDiagnosticsArgsDict]]
        ] = ...,
        domain_configuration_type: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_security_settings: Optional[
            pulumi.Input[
                Union[DomainSecuritySettingsArgs, DomainSecuritySettingsArgsDict]
            ]
        ] = ...,
        domain_service_name: Optional[pulumi.Input[_builtins.str]] = ...,
        filtered_sync: Optional[pulumi.Input[Union[_builtins.str, FilteredSync]]] = ...,
        ldaps_settings: Optional[
            pulumi.Input[Union[LdapsSettingsArgs, LdapsSettingsArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        notification_settings: Optional[
            pulumi.Input[Union[NotificationSettingsArgs, NotificationSettingsArgsDict]]
        ] = ...,
        replica_sets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[ReplicaSetArgs, ReplicaSetArgsDict]]]
            ]
        ] = ...,
        resource_forest_settings: Optional[
            pulumi.Input[
                Union[ResourceForestSettingsArgs, ResourceForestSettingsArgsDict]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_scope: Optional[pulumi.Input[Union[_builtins.str, SyncScope]]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DomainServiceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DomainService: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configDiagnostics")
    def config_diagnostics(
        self,
    ) -> pulumi.Output[Optional[outputs.ConfigDiagnosticsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainConfigurationType")
    def domain_configuration_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="domainSecuritySettings")
    def domain_security_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.DomainSecuritySettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="filteredSync")
    def filtered_sync(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ldapsSettings")
    def ldaps_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.LdapsSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="migrationProperties")
    def migration_properties(
        self,
    ) -> pulumi.Output[outputs.MigrationPropertiesResponse]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.NotificationSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaSets")
    def replica_sets(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ReplicaSetResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceForestSettings")
    def resource_forest_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.ResourceForestSettingsResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="syncApplicationId")
    def sync_application_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncOwner")
    def sync_owner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="syncScope")
    def sync_scope(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.int]: ...
