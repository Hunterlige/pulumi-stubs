import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegionBackendServiceArgs", "RegionBackendService"]

@pulumi.input_type
class RegionBackendServiceArgs:
    def __init__(
        __self__,
        *,
        affinity_cookie_ttl_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        backends: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceBackendArgs]]]
        ] = ...,
        cdn_policy: Optional[pulumi.Input[RegionBackendServiceCdnPolicyArgs]] = ...,
        circuit_breakers: Optional[
            pulumi.Input[RegionBackendServiceCircuitBreakersArgs]
        ] = ...,
        connection_draining_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        connection_tracking_policy: Optional[
            pulumi.Input[RegionBackendServiceConnectionTrackingPolicyArgs]
        ] = ...,
        consistent_hash: Optional[
            pulumi.Input[RegionBackendServiceConsistentHashArgs]
        ] = ...,
        custom_metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceCustomMetricArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_forwarding: Optional[
            pulumi.Input[RegionBackendServiceDynamicForwardingArgs]
        ] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        failover_policy: Optional[
            pulumi.Input[RegionBackendServiceFailoverPolicyArgs]
        ] = ...,
        ha_policy: Optional[pulumi.Input[RegionBackendServiceHaPolicyArgs]] = ...,
        health_checks: Optional[pulumi.Input[_builtins.str]] = ...,
        iap: Optional[pulumi.Input[RegionBackendServiceIapArgs]] = ...,
        ip_address_selection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        locality_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[pulumi.Input[RegionBackendServiceLogConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_pass_through_lb_traffic_policy: Optional[
            pulumi.Input[RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgs]
        ] = ...,
        outlier_detection: Optional[
            pulumi.Input[RegionBackendServiceOutlierDetectionArgs]
        ] = ...,
        params: Optional[pulumi.Input[RegionBackendServiceParamsArgs]] = ...,
        port_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_session_affinity_cookie: Optional[
            pulumi.Input[RegionBackendServiceStrongSessionAffinityCookieArgs]
        ] = ...,
        subsetting: Optional[pulumi.Input[RegionBackendServiceSubsettingArgs]] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_settings: Optional[pulumi.Input[RegionBackendServiceTlsSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="affinityCookieTtlSec")
    def affinity_cookie_ttl_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @affinity_cookie_ttl_sec.setter
    def affinity_cookie_ttl_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def backends(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceBackendArgs]]]
    ]: ...
    @backends.setter
    def backends(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceBackendArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceCdnPolicyArgs]]: ...
    @cdn_policy.setter
    def cdn_policy(
        self, value: Optional[pulumi.Input[RegionBackendServiceCdnPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakers")
    def circuit_breakers(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceCircuitBreakersArgs]]: ...
    @circuit_breakers.setter
    def circuit_breakers(
        self, value: Optional[pulumi.Input[RegionBackendServiceCircuitBreakersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeoutSec")
    def connection_draining_timeout_sec(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_draining_timeout_sec.setter
    def connection_draining_timeout_sec(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionTrackingPolicy")
    def connection_tracking_policy(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceConnectionTrackingPolicyArgs]]: ...
    @connection_tracking_policy.setter
    def connection_tracking_policy(
        self,
        value: Optional[pulumi.Input[RegionBackendServiceConnectionTrackingPolicyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="consistentHash")
    def consistent_hash(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceConsistentHashArgs]]: ...
    @consistent_hash.setter
    def consistent_hash(
        self, value: Optional[pulumi.Input[RegionBackendServiceConsistentHashArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customMetrics")
    def custom_metrics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceCustomMetricArgs]]]
    ]: ...
    @custom_metrics.setter
    def custom_metrics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceCustomMetricArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dynamicForwarding")
    def dynamic_forwarding(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceDynamicForwardingArgs]]: ...
    @dynamic_forwarding.setter
    def dynamic_forwarding(
        self, value: Optional[pulumi.Input[RegionBackendServiceDynamicForwardingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cdn.setter
    def enable_cdn(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="failoverPolicy")
    def failover_policy(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceFailoverPolicyArgs]]: ...
    @failover_policy.setter
    def failover_policy(
        self, value: Optional[pulumi.Input[RegionBackendServiceFailoverPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="haPolicy")
    def ha_policy(self) -> Optional[pulumi.Input[RegionBackendServiceHaPolicyArgs]]: ...
    @ha_policy.setter
    def ha_policy(
        self, value: Optional[pulumi.Input[RegionBackendServiceHaPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_checks.setter
    def health_checks(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iap(self) -> Optional[pulumi.Input[RegionBackendServiceIapArgs]]: ...
    @iap.setter
    def iap(self, value: Optional[pulumi.Input[RegionBackendServiceIapArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressSelectionPolicy")
    def ip_address_selection_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_selection_policy.setter
    def ip_address_selection_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_scheme.setter
    def load_balancing_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localityLbPolicy")
    def locality_lb_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locality_lb_policy.setter
    def locality_lb_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[RegionBackendServiceLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkPassThroughLbTrafficPolicy")
    def network_pass_through_lb_traffic_policy(
        self,
    ) -> Optional[
        pulumi.Input[RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgs]
    ]: ...
    @network_pass_through_lb_traffic_policy.setter
    def network_pass_through_lb_traffic_policy(
        self,
        value: Optional[
            pulumi.Input[RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outlierDetection")
    def outlier_detection(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceOutlierDetectionArgs]]: ...
    @outlier_detection.setter
    def outlier_detection(
        self, value: Optional[pulumi.Input[RegionBackendServiceOutlierDetectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[RegionBackendServiceParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[RegionBackendServiceParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="portName")
    def port_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port_name.setter
    def port_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_affinity.setter
    def session_affinity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strongSessionAffinityCookie")
    def strong_session_affinity_cookie(
        self,
    ) -> Optional[
        pulumi.Input[RegionBackendServiceStrongSessionAffinityCookieArgs]
    ]: ...
    @strong_session_affinity_cookie.setter
    def strong_session_affinity_cookie(
        self,
        value: Optional[
            pulumi.Input[RegionBackendServiceStrongSessionAffinityCookieArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subsetting(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceSubsettingArgs]]: ...
    @subsetting.setter
    def subsetting(
        self, value: Optional[pulumi.Input[RegionBackendServiceSubsettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceTlsSettingsArgs]]: ...
    @tls_settings.setter
    def tls_settings(
        self, value: Optional[pulumi.Input[RegionBackendServiceTlsSettingsArgs]]
    ): ...

@pulumi.input_type
class _RegionBackendServiceState:
    def __init__(
        __self__,
        *,
        affinity_cookie_ttl_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        backends: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceBackendArgs]]]
        ] = ...,
        cdn_policy: Optional[pulumi.Input[RegionBackendServiceCdnPolicyArgs]] = ...,
        circuit_breakers: Optional[
            pulumi.Input[RegionBackendServiceCircuitBreakersArgs]
        ] = ...,
        connection_draining_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        connection_tracking_policy: Optional[
            pulumi.Input[RegionBackendServiceConnectionTrackingPolicyArgs]
        ] = ...,
        consistent_hash: Optional[
            pulumi.Input[RegionBackendServiceConsistentHashArgs]
        ] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceCustomMetricArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_forwarding: Optional[
            pulumi.Input[RegionBackendServiceDynamicForwardingArgs]
        ] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        failover_policy: Optional[
            pulumi.Input[RegionBackendServiceFailoverPolicyArgs]
        ] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        generated_id: Optional[pulumi.Input[_builtins.int]] = ...,
        ha_policy: Optional[pulumi.Input[RegionBackendServiceHaPolicyArgs]] = ...,
        health_checks: Optional[pulumi.Input[_builtins.str]] = ...,
        iap: Optional[pulumi.Input[RegionBackendServiceIapArgs]] = ...,
        ip_address_selection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        locality_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[pulumi.Input[RegionBackendServiceLogConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_pass_through_lb_traffic_policy: Optional[
            pulumi.Input[RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgs]
        ] = ...,
        outlier_detection: Optional[
            pulumi.Input[RegionBackendServiceOutlierDetectionArgs]
        ] = ...,
        params: Optional[pulumi.Input[RegionBackendServiceParamsArgs]] = ...,
        port_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_session_affinity_cookie: Optional[
            pulumi.Input[RegionBackendServiceStrongSessionAffinityCookieArgs]
        ] = ...,
        subsetting: Optional[pulumi.Input[RegionBackendServiceSubsettingArgs]] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_settings: Optional[pulumi.Input[RegionBackendServiceTlsSettingsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="affinityCookieTtlSec")
    def affinity_cookie_ttl_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @affinity_cookie_ttl_sec.setter
    def affinity_cookie_ttl_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def backends(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceBackendArgs]]]
    ]: ...
    @backends.setter
    def backends(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceBackendArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceCdnPolicyArgs]]: ...
    @cdn_policy.setter
    def cdn_policy(
        self, value: Optional[pulumi.Input[RegionBackendServiceCdnPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakers")
    def circuit_breakers(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceCircuitBreakersArgs]]: ...
    @circuit_breakers.setter
    def circuit_breakers(
        self, value: Optional[pulumi.Input[RegionBackendServiceCircuitBreakersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeoutSec")
    def connection_draining_timeout_sec(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @connection_draining_timeout_sec.setter
    def connection_draining_timeout_sec(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="connectionTrackingPolicy")
    def connection_tracking_policy(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceConnectionTrackingPolicyArgs]]: ...
    @connection_tracking_policy.setter
    def connection_tracking_policy(
        self,
        value: Optional[pulumi.Input[RegionBackendServiceConnectionTrackingPolicyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="consistentHash")
    def consistent_hash(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceConsistentHashArgs]]: ...
    @consistent_hash.setter
    def consistent_hash(
        self, value: Optional[pulumi.Input[RegionBackendServiceConsistentHashArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customMetrics")
    def custom_metrics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceCustomMetricArgs]]]
    ]: ...
    @custom_metrics.setter
    def custom_metrics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegionBackendServiceCustomMetricArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dynamicForwarding")
    def dynamic_forwarding(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceDynamicForwardingArgs]]: ...
    @dynamic_forwarding.setter
    def dynamic_forwarding(
        self, value: Optional[pulumi.Input[RegionBackendServiceDynamicForwardingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cdn.setter
    def enable_cdn(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="failoverPolicy")
    def failover_policy(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceFailoverPolicyArgs]]: ...
    @failover_policy.setter
    def failover_policy(
        self, value: Optional[pulumi.Input[RegionBackendServiceFailoverPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="generatedId")
    def generated_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generated_id.setter
    def generated_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="haPolicy")
    def ha_policy(self) -> Optional[pulumi.Input[RegionBackendServiceHaPolicyArgs]]: ...
    @ha_policy.setter
    def ha_policy(
        self, value: Optional[pulumi.Input[RegionBackendServiceHaPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_checks.setter
    def health_checks(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iap(self) -> Optional[pulumi.Input[RegionBackendServiceIapArgs]]: ...
    @iap.setter
    def iap(self, value: Optional[pulumi.Input[RegionBackendServiceIapArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddressSelectionPolicy")
    def ip_address_selection_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address_selection_policy.setter
    def ip_address_selection_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @load_balancing_scheme.setter
    def load_balancing_scheme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localityLbPolicy")
    def locality_lb_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locality_lb_policy.setter
    def locality_lb_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[RegionBackendServiceLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkPassThroughLbTrafficPolicy")
    def network_pass_through_lb_traffic_policy(
        self,
    ) -> Optional[
        pulumi.Input[RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgs]
    ]: ...
    @network_pass_through_lb_traffic_policy.setter
    def network_pass_through_lb_traffic_policy(
        self,
        value: Optional[
            pulumi.Input[RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outlierDetection")
    def outlier_detection(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceOutlierDetectionArgs]]: ...
    @outlier_detection.setter
    def outlier_detection(
        self, value: Optional[pulumi.Input[RegionBackendServiceOutlierDetectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[RegionBackendServiceParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[RegionBackendServiceParamsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="portName")
    def port_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @port_name.setter
    def port_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_affinity.setter
    def session_affinity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strongSessionAffinityCookie")
    def strong_session_affinity_cookie(
        self,
    ) -> Optional[
        pulumi.Input[RegionBackendServiceStrongSessionAffinityCookieArgs]
    ]: ...
    @strong_session_affinity_cookie.setter
    def strong_session_affinity_cookie(
        self,
        value: Optional[
            pulumi.Input[RegionBackendServiceStrongSessionAffinityCookieArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def subsetting(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceSubsettingArgs]]: ...
    @subsetting.setter
    def subsetting(
        self, value: Optional[pulumi.Input[RegionBackendServiceSubsettingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(
        self,
    ) -> Optional[pulumi.Input[RegionBackendServiceTlsSettingsArgs]]: ...
    @tls_settings.setter
    def tls_settings(
        self, value: Optional[pulumi.Input[RegionBackendServiceTlsSettingsArgs]]
    ): ...

@pulumi.type_token(...)
class RegionBackendService(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        affinity_cookie_ttl_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        backends: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RegionBackendServiceBackendArgs,
                            RegionBackendServiceBackendArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        cdn_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceCdnPolicyArgs,
                    RegionBackendServiceCdnPolicyArgsDict,
                ]
            ]
        ] = ...,
        circuit_breakers: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceCircuitBreakersArgs,
                    RegionBackendServiceCircuitBreakersArgsDict,
                ]
            ]
        ] = ...,
        connection_draining_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        connection_tracking_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceConnectionTrackingPolicyArgs,
                    RegionBackendServiceConnectionTrackingPolicyArgsDict,
                ]
            ]
        ] = ...,
        consistent_hash: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceConsistentHashArgs,
                    RegionBackendServiceConsistentHashArgsDict,
                ]
            ]
        ] = ...,
        custom_metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RegionBackendServiceCustomMetricArgs,
                            RegionBackendServiceCustomMetricArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_forwarding: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceDynamicForwardingArgs,
                    RegionBackendServiceDynamicForwardingArgsDict,
                ]
            ]
        ] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        failover_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceFailoverPolicyArgs,
                    RegionBackendServiceFailoverPolicyArgsDict,
                ]
            ]
        ] = ...,
        ha_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceHaPolicyArgs,
                    RegionBackendServiceHaPolicyArgsDict,
                ]
            ]
        ] = ...,
        health_checks: Optional[pulumi.Input[_builtins.str]] = ...,
        iap: Optional[
            pulumi.Input[
                Union[RegionBackendServiceIapArgs, RegionBackendServiceIapArgsDict]
            ]
        ] = ...,
        ip_address_selection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        locality_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceLogConfigArgs,
                    RegionBackendServiceLogConfigArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_pass_through_lb_traffic_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgs,
                    RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgsDict,
                ]
            ]
        ] = ...,
        outlier_detection: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceOutlierDetectionArgs,
                    RegionBackendServiceOutlierDetectionArgsDict,
                ]
            ]
        ] = ...,
        params: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceParamsArgs, RegionBackendServiceParamsArgsDict
                ]
            ]
        ] = ...,
        port_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_session_affinity_cookie: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceStrongSessionAffinityCookieArgs,
                    RegionBackendServiceStrongSessionAffinityCookieArgsDict,
                ]
            ]
        ] = ...,
        subsetting: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceSubsettingArgs,
                    RegionBackendServiceSubsettingArgsDict,
                ]
            ]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_settings: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceTlsSettingsArgs,
                    RegionBackendServiceTlsSettingsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[RegionBackendServiceArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        affinity_cookie_ttl_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        backends: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RegionBackendServiceBackendArgs,
                            RegionBackendServiceBackendArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        cdn_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceCdnPolicyArgs,
                    RegionBackendServiceCdnPolicyArgsDict,
                ]
            ]
        ] = ...,
        circuit_breakers: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceCircuitBreakersArgs,
                    RegionBackendServiceCircuitBreakersArgsDict,
                ]
            ]
        ] = ...,
        connection_draining_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        connection_tracking_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceConnectionTrackingPolicyArgs,
                    RegionBackendServiceConnectionTrackingPolicyArgsDict,
                ]
            ]
        ] = ...,
        consistent_hash: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceConsistentHashArgs,
                    RegionBackendServiceConsistentHashArgsDict,
                ]
            ]
        ] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RegionBackendServiceCustomMetricArgs,
                            RegionBackendServiceCustomMetricArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_forwarding: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceDynamicForwardingArgs,
                    RegionBackendServiceDynamicForwardingArgsDict,
                ]
            ]
        ] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        failover_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceFailoverPolicyArgs,
                    RegionBackendServiceFailoverPolicyArgsDict,
                ]
            ]
        ] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        generated_id: Optional[pulumi.Input[_builtins.int]] = ...,
        ha_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceHaPolicyArgs,
                    RegionBackendServiceHaPolicyArgsDict,
                ]
            ]
        ] = ...,
        health_checks: Optional[pulumi.Input[_builtins.str]] = ...,
        iap: Optional[
            pulumi.Input[
                Union[RegionBackendServiceIapArgs, RegionBackendServiceIapArgsDict]
            ]
        ] = ...,
        ip_address_selection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        locality_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceLogConfigArgs,
                    RegionBackendServiceLogConfigArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_pass_through_lb_traffic_policy: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgs,
                    RegionBackendServiceNetworkPassThroughLbTrafficPolicyArgsDict,
                ]
            ]
        ] = ...,
        outlier_detection: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceOutlierDetectionArgs,
                    RegionBackendServiceOutlierDetectionArgsDict,
                ]
            ]
        ] = ...,
        params: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceParamsArgs, RegionBackendServiceParamsArgsDict
                ]
            ]
        ] = ...,
        port_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_session_affinity_cookie: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceStrongSessionAffinityCookieArgs,
                    RegionBackendServiceStrongSessionAffinityCookieArgsDict,
                ]
            ]
        ] = ...,
        subsetting: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceSubsettingArgs,
                    RegionBackendServiceSubsettingArgsDict,
                ]
            ]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_settings: Optional[
            pulumi.Input[
                Union[
                    RegionBackendServiceTlsSettingsArgs,
                    RegionBackendServiceTlsSettingsArgsDict,
                ]
            ]
        ] = ...,
    ) -> RegionBackendService: ...
    @_builtins.property
    @pulumi.getter(name="affinityCookieTtlSec")
    def affinity_cookie_ttl_sec(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def backends(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RegionBackendServiceBackend]]]: ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(self) -> pulumi.Output[outputs.RegionBackendServiceCdnPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakers")
    def circuit_breakers(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionBackendServiceCircuitBreakers]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeoutSec")
    def connection_draining_timeout_sec(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionTrackingPolicy")
    def connection_tracking_policy(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RegionBackendServiceConnectionTrackingPolicy]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="consistentHash")
    def consistent_hash(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionBackendServiceConsistentHash]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customMetrics")
    def custom_metrics(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.RegionBackendServiceCustomMetric]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dynamicForwarding")
    def dynamic_forwarding(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionBackendServiceDynamicForwarding]]: ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="failoverPolicy")
    def failover_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionBackendServiceFailoverPolicy]]: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="generatedId")
    def generated_id(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="haPolicy")
    def ha_policy(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionBackendServiceHaPolicy]]: ...
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def iap(self) -> pulumi.Output[outputs.RegionBackendServiceIap]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressSelectionPolicy")
    def ip_address_selection_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="localityLbPolicy")
    def locality_lb_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[outputs.RegionBackendServiceLogConfig]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkPassThroughLbTrafficPolicy")
    def network_pass_through_lb_traffic_policy(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RegionBackendServiceNetworkPassThroughLbTrafficPolicy]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outlierDetection")
    def outlier_detection(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionBackendServiceOutlierDetection]]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.RegionBackendServiceParams]]: ...
    @_builtins.property
    @pulumi.getter(name="portName")
    def port_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="strongSessionAffinityCookie")
    def strong_session_affinity_cookie(
        self,
    ) -> pulumi.Output[
        Optional[outputs.RegionBackendServiceStrongSessionAffinityCookie]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def subsetting(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionBackendServiceSubsetting]]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionBackendServiceTlsSettings]]: ...
