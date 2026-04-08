import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ManagedEnvironmentArgs", "ManagedEnvironment"]

@pulumi.input_type
class ManagedEnvironmentArgs:
    def __init__(
        __self__,
        *,
        resource_group_name: pulumi.Input[_builtins.str],
        app_insights_configuration: Optional[
            pulumi.Input[AppInsightsConfigurationArgs]
        ] = ...,
        app_logs_configuration: Optional[pulumi.Input[AppLogsConfigurationArgs]] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_domain_configuration: Optional[
            pulumi.Input[CustomDomainConfigurationArgs]
        ] = ...,
        dapr_ai_connection_string: Optional[pulumi.Input[_builtins.str]] = ...,
        dapr_ai_instrumentation_key: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_encryption_configuration: Optional[
            pulumi.Input[DiskEncryptionConfigurationArgs]
        ] = ...,
        environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[pulumi.Input[ManagedServiceIdentityArgs]] = ...,
        infrastructure_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_configuration: Optional[pulumi.Input[IngressConfigurationArgs]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        open_telemetry_configuration: Optional[
            pulumi.Input[OpenTelemetryConfigurationArgs]
        ] = ...,
        peer_authentication: Optional[
            pulumi.Input[ManagedEnvironmentPeerAuthenticationArgs]
        ] = ...,
        peer_traffic_configuration: Optional[
            pulumi.Input[ManagedEnvironmentPeerTrafficConfigurationArgs]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vnet_configuration: Optional[pulumi.Input[VnetConfigurationArgs]] = ...,
        workload_profiles: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadProfileArgs]]]
        ] = ...,
        zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appInsightsConfiguration")
    def app_insights_configuration(
        self,
    ) -> Optional[pulumi.Input[AppInsightsConfigurationArgs]]: ...
    @app_insights_configuration.setter
    def app_insights_configuration(
        self, value: Optional[pulumi.Input[AppInsightsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appLogsConfiguration")
    def app_logs_configuration(
        self,
    ) -> Optional[pulumi.Input[AppLogsConfigurationArgs]]: ...
    @app_logs_configuration.setter
    def app_logs_configuration(
        self, value: Optional[pulumi.Input[AppLogsConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @availability_zones.setter
    def availability_zones(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(
        self,
    ) -> Optional[pulumi.Input[CustomDomainConfigurationArgs]]: ...
    @custom_domain_configuration.setter
    def custom_domain_configuration(
        self, value: Optional[pulumi.Input[CustomDomainConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dapr_ai_connection_string.setter
    def dapr_ai_connection_string(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="daprAIInstrumentationKey")
    def dapr_ai_instrumentation_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dapr_ai_instrumentation_key.setter
    def dapr_ai_instrumentation_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionConfiguration")
    def disk_encryption_configuration(
        self,
    ) -> Optional[pulumi.Input[DiskEncryptionConfigurationArgs]]: ...
    @disk_encryption_configuration.setter
    def disk_encryption_configuration(
        self, value: Optional[pulumi.Input[DiskEncryptionConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input[ManagedServiceIdentityArgs]]: ...
    @identity.setter
    def identity(self, value: Optional[pulumi.Input[ManagedServiceIdentityArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="infrastructureResourceGroup")
    def infrastructure_resource_group(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @infrastructure_resource_group.setter
    def infrastructure_resource_group(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingressConfiguration")
    def ingress_configuration(
        self,
    ) -> Optional[pulumi.Input[IngressConfigurationArgs]]: ...
    @ingress_configuration.setter
    def ingress_configuration(
        self, value: Optional[pulumi.Input[IngressConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kind.setter
    def kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openTelemetryConfiguration")
    def open_telemetry_configuration(
        self,
    ) -> Optional[pulumi.Input[OpenTelemetryConfigurationArgs]]: ...
    @open_telemetry_configuration.setter
    def open_telemetry_configuration(
        self, value: Optional[pulumi.Input[OpenTelemetryConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peerAuthentication")
    def peer_authentication(
        self,
    ) -> Optional[pulumi.Input[ManagedEnvironmentPeerAuthenticationArgs]]: ...
    @peer_authentication.setter
    def peer_authentication(
        self, value: Optional[pulumi.Input[ManagedEnvironmentPeerAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="peerTrafficConfiguration")
    def peer_traffic_configuration(
        self,
    ) -> Optional[pulumi.Input[ManagedEnvironmentPeerTrafficConfigurationArgs]]: ...
    @peer_traffic_configuration.setter
    def peer_traffic_configuration(
        self,
        value: Optional[pulumi.Input[ManagedEnvironmentPeerTrafficConfigurationArgs]],
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
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vnetConfiguration")
    def vnet_configuration(self) -> Optional[pulumi.Input[VnetConfigurationArgs]]: ...
    @vnet_configuration.setter
    def vnet_configuration(
        self, value: Optional[pulumi.Input[VnetConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadProfiles")
    def workload_profiles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadProfileArgs]]]]: ...
    @workload_profiles.setter
    def workload_profiles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadProfileArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @zone_redundant.setter
    def zone_redundant(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

@pulumi.type_token("azure-native:app:ManagedEnvironment")
class ManagedEnvironment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_insights_configuration: Optional[
            pulumi.Input[
                Union[AppInsightsConfigurationArgs, AppInsightsConfigurationArgsDict]
            ]
        ] = ...,
        app_logs_configuration: Optional[
            pulumi.Input[Union[AppLogsConfigurationArgs, AppLogsConfigurationArgsDict]]
        ] = ...,
        availability_zones: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_domain_configuration: Optional[
            pulumi.Input[
                Union[CustomDomainConfigurationArgs, CustomDomainConfigurationArgsDict]
            ]
        ] = ...,
        dapr_ai_connection_string: Optional[pulumi.Input[_builtins.str]] = ...,
        dapr_ai_instrumentation_key: Optional[pulumi.Input[_builtins.str]] = ...,
        disk_encryption_configuration: Optional[
            pulumi.Input[
                Union[
                    DiskEncryptionConfigurationArgs, DiskEncryptionConfigurationArgsDict
                ]
            ]
        ] = ...,
        environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        identity: Optional[
            pulumi.Input[
                Union[ManagedServiceIdentityArgs, ManagedServiceIdentityArgsDict]
            ]
        ] = ...,
        infrastructure_resource_group: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_configuration: Optional[
            pulumi.Input[Union[IngressConfigurationArgs, IngressConfigurationArgsDict]]
        ] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        open_telemetry_configuration: Optional[
            pulumi.Input[
                Union[
                    OpenTelemetryConfigurationArgs, OpenTelemetryConfigurationArgsDict
                ]
            ]
        ] = ...,
        peer_authentication: Optional[
            pulumi.Input[
                Union[
                    ManagedEnvironmentPeerAuthenticationArgs,
                    ManagedEnvironmentPeerAuthenticationArgsDict,
                ]
            ]
        ] = ...,
        peer_traffic_configuration: Optional[
            pulumi.Input[
                Union[
                    ManagedEnvironmentPeerTrafficConfigurationArgs,
                    ManagedEnvironmentPeerTrafficConfigurationArgsDict,
                ]
            ]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vnet_configuration: Optional[
            pulumi.Input[Union[VnetConfigurationArgs, VnetConfigurationArgsDict]]
        ] = ...,
        workload_profiles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[WorkloadProfileArgs, WorkloadProfileArgsDict]]
                ]
            ]
        ] = ...,
        zone_redundant: Optional[pulumi.Input[_builtins.bool]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ManagedEnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> ManagedEnvironment: ...
    @_builtins.property
    @pulumi.getter(name="appInsightsConfiguration")
    def app_insights_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.AppInsightsConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="appLogsConfiguration")
    def app_logs_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.AppLogsConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.CustomDomainConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="daprAIInstrumentationKey")
    def dapr_ai_instrumentation_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="daprConfiguration")
    def dapr_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.DaprConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionConfiguration")
    def disk_encryption_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.DiskEncryptionConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="eventStreamEndpoint")
    def event_stream_endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identity(
        self,
    ) -> pulumi.Output[Optional[outputs.ManagedServiceIdentityResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureResourceGroup")
    def infrastructure_resource_group(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ingressConfiguration")
    def ingress_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.IngressConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="kedaConfiguration")
    def keda_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.KedaConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="openTelemetryConfiguration")
    def open_telemetry_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.OpenTelemetryConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="peerAuthentication")
    def peer_authentication(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ManagedEnvironmentResponsePeerAuthentication]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="peerTrafficConfiguration")
    def peer_traffic_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.ManagedEnvironmentResponsePeerTrafficConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> pulumi.Output[Sequence[outputs.PrivateEndpointConnectionResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkDefaultDomain")
    def private_link_default_domain(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter(name="vnetConfiguration")
    def vnet_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.VnetConfigurationResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="workloadProfiles")
    def workload_profiles(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.WorkloadProfileResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
