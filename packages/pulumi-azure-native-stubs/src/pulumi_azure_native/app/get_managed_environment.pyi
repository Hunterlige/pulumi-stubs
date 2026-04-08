import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetManagedEnvironmentResult",
    "AwaitableGetManagedEnvironmentResult",
    "get_managed_environment",
    "get_managed_environment_output",
]

@pulumi.output_type
class GetManagedEnvironmentResult:
    def __init__(
        __self__,
        app_insights_configuration=...,
        app_logs_configuration=...,
        availability_zones=...,
        azure_api_version=...,
        custom_domain_configuration=...,
        dapr_ai_connection_string=...,
        dapr_ai_instrumentation_key=...,
        dapr_configuration=...,
        default_domain=...,
        deployment_errors=...,
        disk_encryption_configuration=...,
        event_stream_endpoint=...,
        id=...,
        identity=...,
        infrastructure_resource_group=...,
        ingress_configuration=...,
        keda_configuration=...,
        kind=...,
        location=...,
        name=...,
        open_telemetry_configuration=...,
        peer_authentication=...,
        peer_traffic_configuration=...,
        private_endpoint_connections=...,
        private_link_default_domain=...,
        provisioning_state=...,
        public_network_access=...,
        static_ip=...,
        system_data=...,
        tags=...,
        type=...,
        vnet_configuration=...,
        workload_profiles=...,
        zone_redundant=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appInsightsConfiguration")
    def app_insights_configuration(
        self,
    ) -> Optional[outputs.AppInsightsConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="appLogsConfiguration")
    def app_logs_configuration(
        self,
    ) -> Optional[outputs.AppLogsConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customDomainConfiguration")
    def custom_domain_configuration(
        self,
    ) -> Optional[outputs.CustomDomainConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="daprAIConnectionString")
    def dapr_ai_connection_string(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="daprAIInstrumentationKey")
    def dapr_ai_instrumentation_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="daprConfiguration")
    def dapr_configuration(self) -> Optional[outputs.DaprConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deploymentErrors")
    def deployment_errors(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="diskEncryptionConfiguration")
    def disk_encryption_configuration(
        self,
    ) -> Optional[outputs.DiskEncryptionConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="eventStreamEndpoint")
    def event_stream_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]: ...
    @_builtins.property
    @pulumi.getter(name="infrastructureResourceGroup")
    def infrastructure_resource_group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ingressConfiguration")
    def ingress_configuration(
        self,
    ) -> Optional[outputs.IngressConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="kedaConfiguration")
    def keda_configuration(self) -> Optional[outputs.KedaConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="openTelemetryConfiguration")
    def open_telemetry_configuration(
        self,
    ) -> Optional[outputs.OpenTelemetryConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="peerAuthentication")
    def peer_authentication(
        self,
    ) -> Optional[outputs.ManagedEnvironmentResponsePeerAuthentication]: ...
    @_builtins.property
    @pulumi.getter(name="peerTrafficConfiguration")
    def peer_traffic_configuration(
        self,
    ) -> Optional[outputs.ManagedEnvironmentResponsePeerTrafficConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(
        self,
    ) -> Sequence[outputs.PrivateEndpointConnectionResponse]: ...
    @_builtins.property
    @pulumi.getter(name="privateLinkDefaultDomain")
    def private_link_default_domain(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="staticIp")
    def static_ip(self) -> _builtins.str: ...
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
    @pulumi.getter(name="vnetConfiguration")
    def vnet_configuration(self) -> Optional[outputs.VnetConfigurationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="workloadProfiles")
    def workload_profiles(
        self,
    ) -> Optional[Sequence[outputs.WorkloadProfileResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[_builtins.bool]: ...

class AwaitableGetManagedEnvironmentResult(GetManagedEnvironmentResult):
    def __await__(self): ...

def get_managed_environment(
    environment_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetManagedEnvironmentResult: ...
def get_managed_environment_output(
    environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetManagedEnvironmentResult]: ...
