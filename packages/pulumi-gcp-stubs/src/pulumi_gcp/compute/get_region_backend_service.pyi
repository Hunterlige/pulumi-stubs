import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRegionBackendServiceResult",
    "AwaitableGetRegionBackendServiceResult",
    "get_region_backend_service",
    "get_region_backend_service_output",
]

@pulumi.output_type
class GetRegionBackendServiceResult:
    def __init__(
        __self__,
        affinity_cookie_ttl_sec=...,
        backends=...,
        cdn_policies=...,
        circuit_breakers=...,
        connection_draining_timeout_sec=...,
        connection_tracking_policies=...,
        consistent_hashes=...,
        creation_timestamp=...,
        custom_metrics=...,
        description=...,
        dynamic_forwardings=...,
        enable_cdn=...,
        failover_policies=...,
        fingerprint=...,
        generated_id=...,
        ha_policies=...,
        health_checks=...,
        iaps=...,
        id=...,
        ip_address_selection_policy=...,
        load_balancing_scheme=...,
        locality_lb_policy=...,
        log_configs=...,
        name=...,
        network=...,
        network_pass_through_lb_traffic_policies=...,
        outlier_detections=...,
        params=...,
        port_name=...,
        project=...,
        protocol=...,
        region=...,
        security_policy=...,
        self_link=...,
        session_affinity=...,
        strong_session_affinity_cookies=...,
        subsettings=...,
        timeout_sec=...,
        tls_settings=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="affinityCookieTtlSec")
    def affinity_cookie_ttl_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def backends(self) -> Sequence[outputs.GetRegionBackendServiceBackendResult]: ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicies")
    def cdn_policies(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceCdnPolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakers")
    def circuit_breakers(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceCircuitBreakerResult]: ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeoutSec")
    def connection_draining_timeout_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="connectionTrackingPolicies")
    def connection_tracking_policies(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceConnectionTrackingPolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="consistentHashes")
    def consistent_hashes(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceConsistentHashResult]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customMetrics")
    def custom_metrics(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceCustomMetricResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dynamicForwardings")
    def dynamic_forwardings(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceDynamicForwardingResult]: ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="failoverPolicies")
    def failover_policies(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceFailoverPolicyResult]: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="generatedId")
    def generated_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="haPolicies")
    def ha_policies(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceHaPolicyResult]: ...
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def iaps(self) -> Sequence[outputs.GetRegionBackendServiceIapResult]: ...
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
    @pulumi.getter(name="localityLbPolicy")
    def locality_lb_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logConfigs")
    def log_configs(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceLogConfigResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkPassThroughLbTrafficPolicies")
    def network_pass_through_lb_traffic_policies(
        self,
    ) -> Sequence[
        outputs.GetRegionBackendServiceNetworkPassThroughLbTrafficPolicyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outlierDetections")
    def outlier_detections(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceOutlierDetectionResult]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Sequence[outputs.GetRegionBackendServiceParamResult]: ...
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
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="strongSessionAffinityCookies")
    def strong_session_affinity_cookies(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceStrongSessionAffinityCookyResult]: ...
    @_builtins.property
    @pulumi.getter
    def subsettings(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceSubsettingResult]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(
        self,
    ) -> Sequence[outputs.GetRegionBackendServiceTlsSettingResult]: ...

class AwaitableGetRegionBackendServiceResult(GetRegionBackendServiceResult):
    def __await__(self): ...

def get_region_backend_service(
    name: Optional[_builtins.str] = ...,
    project: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRegionBackendServiceResult: ...
def get_region_backend_service_output(
    name: Optional[pulumi.Input[_builtins.str]] = ...,
    project: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRegionBackendServiceResult]: ...
