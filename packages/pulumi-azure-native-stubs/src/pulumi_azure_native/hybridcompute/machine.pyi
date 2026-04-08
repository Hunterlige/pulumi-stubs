import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["MachineArgs", "Machine"]

@pulumi.input_type
class MachineArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        agent_upgrade: Optional[pulumi.Input[AgentUpgradeArgs]] = ...,
        client_public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        expand: Optional[pulumi.Input[_builtins.str]] = ...,
        extensions: Optional[
            pulumi.Input[Sequence[pulumi.Input[MachineExtensionInstanceViewArgs]]]
        ] = ...,
        identity: Optional[pulumi.Input[IdentityArgs]] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, ArcKindEnum]]] = ...,
        license_profile: Optional[
            pulumi.Input[LicenseProfileMachineInstanceViewArgs]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        location_data: Optional[pulumi.Input[LocationDataArgs]] = ...,
        machine_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mssql_discovered: Optional[pulumi.Input[_builtins.str]] = ...,
        os_profile: Optional[pulumi.Input[OSProfileArgs]] = ...,
        os_type: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_scope_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        service_statuses: Optional[pulumi.Input[ServiceStatusesArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vm_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentUpgrade")
    def agent_upgrade(self) -> Optional[pulumi.Input[AgentUpgradeArgs]]: ...
    @agent_upgrade.setter
    def agent_upgrade(self, value: Optional[pulumi.Input[AgentUpgradeArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="clientPublicKey")
    def client_public_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_public_key.setter
    def client_public_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def expand(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expand.setter
    def expand(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[MachineExtensionInstanceViewArgs]]]
    ]: ...
    @extensions.setter
    def extensions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[MachineExtensionInstanceViewArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[IdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[IdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[_builtins.str, ArcKindEnum]]]: ...
    @kind.setter
    def kind(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ArcKindEnum]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="licenseProfile")
    def license_profile(
        self,
    ) -> Optional[pulumi.Input[LicenseProfileMachineInstanceViewArgs]]: ...
    @license_profile.setter
    def license_profile(
        self, value: Optional[pulumi.Input[LicenseProfileMachineInstanceViewArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="locationData")
    def location_data(self) -> Optional[pulumi.Input[LocationDataArgs]]: ...
    @location_data.setter
    def location_data(self, value: Optional[pulumi.Input[LocationDataArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="machineName")
    def machine_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @machine_name.setter
    def machine_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mssqlDiscovered")
    def mssql_discovered(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mssql_discovered.setter
    def mssql_discovered(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input[OSProfileArgs]]: ...
    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input[OSProfileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parentClusterResourceId")
    def parent_cluster_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parent_cluster_resource_id.setter
    def parent_cluster_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_link_scope_resource_id.setter
    def private_link_scope_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceStatuses")
    def service_statuses(self) -> Optional[pulumi.Input[ServiceStatusesArgs]]: ...
    @service_statuses.setter
    def service_statuses(self, value: Optional[pulumi.Input[ServiceStatusesArgs]]): ...
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
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vm_id.setter
    def vm_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("azure-native:hybridcompute:Machine")
class Machine(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_upgrade: Optional[
            pulumi.Input[Union[AgentUpgradeArgs, AgentUpgradeArgsDict]]
        ] = ...,
        client_public_key: Optional[pulumi.Input[_builtins.str]] = ...,
        expand: Optional[pulumi.Input[_builtins.str]] = ...,
        extensions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            MachineExtensionInstanceViewArgs,
                            MachineExtensionInstanceViewArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        identity: Optional[pulumi.Input[Union[IdentityArgs, IdentityArgsDict]]] = ...,
        kind: Optional[pulumi.Input[Union[_builtins.str, ArcKindEnum]]] = ...,
        license_profile: Optional[
            pulumi.Input[
                Union[
                    LicenseProfileMachineInstanceViewArgs,
                    LicenseProfileMachineInstanceViewArgsDict,
                ]
            ]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        location_data: Optional[
            pulumi.Input[Union[LocationDataArgs, LocationDataArgsDict]]
        ] = ...,
        machine_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mssql_discovered: Optional[pulumi.Input[_builtins.str]] = ...,
        os_profile: Optional[
            pulumi.Input[Union[OSProfileArgs, OSProfileArgsDict]]
        ] = ...,
        os_type: Optional[pulumi.Input[_builtins.str]] = ...,
        parent_cluster_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        private_link_scope_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_statuses: Optional[
            pulumi.Input[Union[ServiceStatusesArgs, ServiceStatusesArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vm_id: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: MachineArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Machine: ...
    @_builtins.property
    @pulumi.getter(name="adFqdn")
    def ad_fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="agentConfiguration")
    def agent_configuration(
        self,
    ) -> pulumi.Output[outputs.AgentConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="agentUpgrade")
    def agent_upgrade(
        self,
    ) -> pulumi.Output[Optional[outputs.AgentUpgradeResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clientPublicKey")
    def client_public_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="cloudMetadata")
    def cloud_metadata(
        self,
    ) -> pulumi.Output[Optional[outputs.CloudMetadataResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="detectedProperties")
    def detected_properties(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dnsFqdn")
    def dns_fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> pulumi.Output[Sequence[outputs.ErrorDetailResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def extensions(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.MachineExtensionInstanceViewResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional[outputs.IdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="lastStatusChange")
    def last_status_change(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="licenseProfile")
    def license_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.LicenseProfileMachineInstanceViewResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="locationData")
    def location_data(
        self,
    ) -> pulumi.Output[Optional[outputs.LocationDataResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="machineFqdn")
    def machine_fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="mssqlDiscovered")
    def mssql_discovered(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[outputs.NetworkProfileResponse]: ...
    @_builtins.property
    @pulumi.getter(name="osEdition")
    def os_edition(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osName")
    def os_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> pulumi.Output[Optional[outputs.OSProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="osSku")
    def os_sku(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parentClusterResourceId")
    def parent_cluster_resource_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> pulumi.Output[Sequence[outputs.MachineExtensionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceStatuses")
    def service_statuses(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceStatusesResponse]]: ...
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
    @pulumi.getter(name="vmId")
    def vm_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vmUuid")
    def vm_uuid(self) -> pulumi.Output[_builtins.str]: ...
