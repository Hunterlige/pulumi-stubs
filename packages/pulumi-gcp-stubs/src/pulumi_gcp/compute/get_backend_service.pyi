import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBackendServiceResult",
    "AwaitableGetBackendServiceResult",
    "get_backend_service",
    "get_backend_service_output",
]

@pulumi.output_type
class GetBackendServiceResult:
    def __init__(
        __self__,
        affinity_cookie_ttl_sec=...,
        backends=...,
        cdn_policies=...,
        circuit_breakers=...,
        compression_mode=...,
        connection_draining_timeout_sec=...,
        consistent_hash=...,
        creation_timestamp=...,
        custom_metrics=...,
        custom_request_headers=...,
        custom_response_headers=...,
        description=...,
        dynamic_forwardings=...,
        edge_security_policy=...,
        enable_cdn=...,
        external_managed_migration_state=...,
        external_managed_migration_testing_percentage=...,
        fingerprint=...,
        generated_id=...,
        health_checks=...,
        iaps=...,
        id=...,
        ip_address_selection_policy=...,
        load_balancing_scheme=...,
        locality_lb_policies=...,
        locality_lb_policy=...,
        log_configs=...,
        max_stream_durations=...,
        name=...,
        network_pass_through_lb_traffic_policies=...,
        outlier_detections=...,
        params=...,
        port_name=...,
        project=...,
        protocol=...,
        security_policy=...,
        security_settings=...,
        self_link=...,
        service_lb_policy=...,
        session_affinity=...,
        strong_session_affinity_cookies=...,
        timeout_sec=...,
        tls_settings=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="affinityCookieTtlSec")
    def affinity_cookie_ttl_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Sequence[outputs.GetBackendServiceBackendResult]: ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicies")
    def cdn_policies(self) -> Sequence[outputs.GetBackendServiceCdnPolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakers")
    def circuit_breakers(
        self,
    ) -> Sequence[outputs.GetBackendServiceCircuitBreakerResult]: ...
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeoutSec")
    def connection_draining_timeout_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="consistentHash")
    def consistent_hash(
        self,
    ) -> Sequence[outputs.GetBackendServiceConsistentHashResult]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customMetrics")
    def custom_metrics(
        self,
    ) -> Sequence[outputs.GetBackendServiceCustomMetricResult]: ...
    @_builtins.property
    @pulumi.getter(name="customRequestHeaders")
    def custom_request_headers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customResponseHeaders")
    def custom_response_headers(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dynamicForwardings")
    def dynamic_forwardings(
        self,
    ) -> Sequence[outputs.GetBackendServiceDynamicForwardingResult]: ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="externalManagedMigrationState")
    def external_managed_migration_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="externalManagedMigrationTestingPercentage")
    def external_managed_migration_testing_percentage(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="generatedId")
    def generated_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def iaps(self) -> Sequence[outputs.GetBackendServiceIapResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressSelectionPolicy")
    def ip_address_selection_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="localityLbPolicies")
    def locality_lb_policies(
        self,
    ) -> Sequence[outputs.GetBackendServiceLocalityLbPolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="localityLbPolicy")
    def locality_lb_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logConfigs")
    def log_configs(self) -> Sequence[outputs.GetBackendServiceLogConfigResult]: ...
    @_builtins.property
    @pulumi.getter(name="maxStreamDurations")
    def max_stream_durations(
        self,
    ) -> Sequence[outputs.GetBackendServiceMaxStreamDurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkPassThroughLbTrafficPolicies")
    def network_pass_through_lb_traffic_policies(
        self,
    ) -> Sequence[outputs.GetBackendServiceNetworkPassThroughLbTrafficPolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="outlierDetections")
    def outlier_detections(
        self,
    ) -> Sequence[outputs.GetBackendServiceOutlierDetectionResult]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Sequence[outputs.GetBackendServiceParamResult]: ...
    @_builtins.property
    @pulumi.getter(name="portName")
    def port_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(
        self,
    ) -> Sequence[outputs.GetBackendServiceSecuritySettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="serviceLbPolicy")
    def service_lb_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="strongSessionAffinityCookies")
    def strong_session_affinity_cookies(
        self,
    ) -> Sequence[outputs.GetBackendServiceStrongSessionAffinityCookyResult]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(self) -> Sequence[outputs.GetBackendServiceTlsSettingResult]: ...

class AwaitableGetBackendServiceResult(GetBackendServiceResult):
    def __await__(self): ...

def get_backend_service(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBackendServiceResult: ...
def get_backend_service_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBackendServiceResult]: ...
