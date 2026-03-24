import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["BackendServiceArgs", "BackendService"]

@pulumi.input_type
class BackendServiceArgs:
    def __init__(
        __self__,
        *,
        affinity_cookie_ttl_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        backends: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceBackendArgs]]]
        ] = ...,
        cdn_policy: Optional[pulumi.Input[BackendServiceCdnPolicyArgs]] = ...,
        circuit_breakers: Optional[
            pulumi.Input[BackendServiceCircuitBreakersArgs]
        ] = ...,
        compression_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_draining_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        consistent_hash: Optional[pulumi.Input[BackendServiceConsistentHashArgs]] = ...,
        custom_metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceCustomMetricArgs]]]
        ] = ...,
        custom_request_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_response_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_forwarding: Optional[
            pulumi.Input[BackendServiceDynamicForwardingArgs]
        ] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        external_managed_migration_state: Optional[pulumi.Input[_builtins.str]] = ...,
        external_managed_migration_testing_percentage: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        health_checks: Optional[pulumi.Input[_builtins.str]] = ...,
        iap: Optional[pulumi.Input[BackendServiceIapArgs]] = ...,
        ip_address_selection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        locality_lb_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceLocalityLbPolicyArgs]]]
        ] = ...,
        locality_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[pulumi.Input[BackendServiceLogConfigArgs]] = ...,
        max_stream_duration: Optional[
            pulumi.Input[BackendServiceMaxStreamDurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_pass_through_lb_traffic_policy: Optional[
            pulumi.Input[BackendServiceNetworkPassThroughLbTrafficPolicyArgs]
        ] = ...,
        outlier_detection: Optional[
            pulumi.Input[BackendServiceOutlierDetectionArgs]
        ] = ...,
        params: Optional[pulumi.Input[BackendServiceParamsArgs]] = ...,
        port_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        security_settings: Optional[
            pulumi.Input[BackendServiceSecuritySettingsArgs]
        ] = ...,
        service_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_session_affinity_cookie: Optional[
            pulumi.Input[BackendServiceStrongSessionAffinityCookieArgs]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_settings: Optional[pulumi.Input[BackendServiceTlsSettingsArgs]] = ...,
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
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BackendServiceBackendArgs]]]]: ...
    @backends.setter
    def backends(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceBackendArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(self) -> Optional[pulumi.Input[BackendServiceCdnPolicyArgs]]: ...
    @cdn_policy.setter
    def cdn_policy(
        self, value: Optional[pulumi.Input[BackendServiceCdnPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakers")
    def circuit_breakers(
        self,
    ) -> Optional[pulumi.Input[BackendServiceCircuitBreakersArgs]]: ...
    @circuit_breakers.setter
    def circuit_breakers(
        self, value: Optional[pulumi.Input[BackendServiceCircuitBreakersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression_mode.setter
    def compression_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="consistentHash")
    def consistent_hash(
        self,
    ) -> Optional[pulumi.Input[BackendServiceConsistentHashArgs]]: ...
    @consistent_hash.setter
    def consistent_hash(
        self, value: Optional[pulumi.Input[BackendServiceConsistentHashArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customMetrics")
    def custom_metrics(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BackendServiceCustomMetricArgs]]]
    ]: ...
    @custom_metrics.setter
    def custom_metrics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceCustomMetricArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customRequestHeaders")
    def custom_request_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_request_headers.setter
    def custom_request_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customResponseHeaders")
    def custom_response_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_response_headers.setter
    def custom_response_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    ) -> Optional[pulumi.Input[BackendServiceDynamicForwardingArgs]]: ...
    @dynamic_forwarding.setter
    def dynamic_forwarding(
        self, value: Optional[pulumi.Input[BackendServiceDynamicForwardingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_security_policy.setter
    def edge_security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cdn.setter
    def enable_cdn(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="externalManagedMigrationState")
    def external_managed_migration_state(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_managed_migration_state.setter
    def external_managed_migration_state(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="externalManagedMigrationTestingPercentage")
    def external_managed_migration_testing_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @external_managed_migration_testing_percentage.setter
    def external_managed_migration_testing_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_checks.setter
    def health_checks(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iap(self) -> Optional[pulumi.Input[BackendServiceIapArgs]]: ...
    @iap.setter
    def iap(self, value: Optional[pulumi.Input[BackendServiceIapArgs]]): ...
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
    @pulumi.getter(name="localityLbPolicies")
    def locality_lb_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BackendServiceLocalityLbPolicyArgs]]]
    ]: ...
    @locality_lb_policies.setter
    def locality_lb_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceLocalityLbPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localityLbPolicy")
    def locality_lb_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locality_lb_policy.setter
    def locality_lb_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[BackendServiceLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[BackendServiceLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxStreamDuration")
    def max_stream_duration(
        self,
    ) -> Optional[pulumi.Input[BackendServiceMaxStreamDurationArgs]]: ...
    @max_stream_duration.setter
    def max_stream_duration(
        self, value: Optional[pulumi.Input[BackendServiceMaxStreamDurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkPassThroughLbTrafficPolicy")
    def network_pass_through_lb_traffic_policy(
        self,
    ) -> Optional[
        pulumi.Input[BackendServiceNetworkPassThroughLbTrafficPolicyArgs]
    ]: ...
    @network_pass_through_lb_traffic_policy.setter
    def network_pass_through_lb_traffic_policy(
        self,
        value: Optional[
            pulumi.Input[BackendServiceNetworkPassThroughLbTrafficPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outlierDetection")
    def outlier_detection(
        self,
    ) -> Optional[pulumi.Input[BackendServiceOutlierDetectionArgs]]: ...
    @outlier_detection.setter
    def outlier_detection(
        self, value: Optional[pulumi.Input[BackendServiceOutlierDetectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[BackendServiceParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[BackendServiceParamsArgs]]): ...
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
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(
        self,
    ) -> Optional[pulumi.Input[BackendServiceSecuritySettingsArgs]]: ...
    @security_settings.setter
    def security_settings(
        self, value: Optional[pulumi.Input[BackendServiceSecuritySettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceLbPolicy")
    def service_lb_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_lb_policy.setter
    def service_lb_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_affinity.setter
    def session_affinity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strongSessionAffinityCookie")
    def strong_session_affinity_cookie(
        self,
    ) -> Optional[pulumi.Input[BackendServiceStrongSessionAffinityCookieArgs]]: ...
    @strong_session_affinity_cookie.setter
    def strong_session_affinity_cookie(
        self,
        value: Optional[pulumi.Input[BackendServiceStrongSessionAffinityCookieArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(self) -> Optional[pulumi.Input[BackendServiceTlsSettingsArgs]]: ...
    @tls_settings.setter
    def tls_settings(
        self, value: Optional[pulumi.Input[BackendServiceTlsSettingsArgs]]
    ): ...

@pulumi.input_type
class _BackendServiceState:
    def __init__(
        __self__,
        *,
        affinity_cookie_ttl_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        backends: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceBackendArgs]]]
        ] = ...,
        cdn_policy: Optional[pulumi.Input[BackendServiceCdnPolicyArgs]] = ...,
        circuit_breakers: Optional[
            pulumi.Input[BackendServiceCircuitBreakersArgs]
        ] = ...,
        compression_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_draining_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        consistent_hash: Optional[pulumi.Input[BackendServiceConsistentHashArgs]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_metrics: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceCustomMetricArgs]]]
        ] = ...,
        custom_request_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_response_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_forwarding: Optional[
            pulumi.Input[BackendServiceDynamicForwardingArgs]
        ] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        external_managed_migration_state: Optional[pulumi.Input[_builtins.str]] = ...,
        external_managed_migration_testing_percentage: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        generated_id: Optional[pulumi.Input[_builtins.int]] = ...,
        health_checks: Optional[pulumi.Input[_builtins.str]] = ...,
        iap: Optional[pulumi.Input[BackendServiceIapArgs]] = ...,
        ip_address_selection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        locality_lb_policies: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceLocalityLbPolicyArgs]]]
        ] = ...,
        locality_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[pulumi.Input[BackendServiceLogConfigArgs]] = ...,
        max_stream_duration: Optional[
            pulumi.Input[BackendServiceMaxStreamDurationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_pass_through_lb_traffic_policy: Optional[
            pulumi.Input[BackendServiceNetworkPassThroughLbTrafficPolicyArgs]
        ] = ...,
        outlier_detection: Optional[
            pulumi.Input[BackendServiceOutlierDetectionArgs]
        ] = ...,
        params: Optional[pulumi.Input[BackendServiceParamsArgs]] = ...,
        port_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        security_settings: Optional[
            pulumi.Input[BackendServiceSecuritySettingsArgs]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        service_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_session_affinity_cookie: Optional[
            pulumi.Input[BackendServiceStrongSessionAffinityCookieArgs]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_settings: Optional[pulumi.Input[BackendServiceTlsSettingsArgs]] = ...,
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
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BackendServiceBackendArgs]]]]: ...
    @backends.setter
    def backends(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceBackendArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(self) -> Optional[pulumi.Input[BackendServiceCdnPolicyArgs]]: ...
    @cdn_policy.setter
    def cdn_policy(
        self, value: Optional[pulumi.Input[BackendServiceCdnPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakers")
    def circuit_breakers(
        self,
    ) -> Optional[pulumi.Input[BackendServiceCircuitBreakersArgs]]: ...
    @circuit_breakers.setter
    def circuit_breakers(
        self, value: Optional[pulumi.Input[BackendServiceCircuitBreakersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression_mode.setter
    def compression_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="consistentHash")
    def consistent_hash(
        self,
    ) -> Optional[pulumi.Input[BackendServiceConsistentHashArgs]]: ...
    @consistent_hash.setter
    def consistent_hash(
        self, value: Optional[pulumi.Input[BackendServiceConsistentHashArgs]]
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
        pulumi.Input[Sequence[pulumi.Input[BackendServiceCustomMetricArgs]]]
    ]: ...
    @custom_metrics.setter
    def custom_metrics(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceCustomMetricArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customRequestHeaders")
    def custom_request_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_request_headers.setter
    def custom_request_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customResponseHeaders")
    def custom_response_headers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_response_headers.setter
    def custom_response_headers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    ) -> Optional[pulumi.Input[BackendServiceDynamicForwardingArgs]]: ...
    @dynamic_forwarding.setter
    def dynamic_forwarding(
        self, value: Optional[pulumi.Input[BackendServiceDynamicForwardingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @edge_security_policy.setter
    def edge_security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cdn.setter
    def enable_cdn(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="externalManagedMigrationState")
    def external_managed_migration_state(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @external_managed_migration_state.setter
    def external_managed_migration_state(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="externalManagedMigrationTestingPercentage")
    def external_managed_migration_testing_percentage(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @external_managed_migration_testing_percentage.setter
    def external_managed_migration_testing_percentage(
        self, value: Optional[pulumi.Input[_builtins.float]]
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
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @health_checks.setter
    def health_checks(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def iap(self) -> Optional[pulumi.Input[BackendServiceIapArgs]]: ...
    @iap.setter
    def iap(self, value: Optional[pulumi.Input[BackendServiceIapArgs]]): ...
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
    @pulumi.getter(name="localityLbPolicies")
    def locality_lb_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[BackendServiceLocalityLbPolicyArgs]]]
    ]: ...
    @locality_lb_policies.setter
    def locality_lb_policies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BackendServiceLocalityLbPolicyArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="localityLbPolicy")
    def locality_lb_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locality_lb_policy.setter
    def locality_lb_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[BackendServiceLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[BackendServiceLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxStreamDuration")
    def max_stream_duration(
        self,
    ) -> Optional[pulumi.Input[BackendServiceMaxStreamDurationArgs]]: ...
    @max_stream_duration.setter
    def max_stream_duration(
        self, value: Optional[pulumi.Input[BackendServiceMaxStreamDurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkPassThroughLbTrafficPolicy")
    def network_pass_through_lb_traffic_policy(
        self,
    ) -> Optional[
        pulumi.Input[BackendServiceNetworkPassThroughLbTrafficPolicyArgs]
    ]: ...
    @network_pass_through_lb_traffic_policy.setter
    def network_pass_through_lb_traffic_policy(
        self,
        value: Optional[
            pulumi.Input[BackendServiceNetworkPassThroughLbTrafficPolicyArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="outlierDetection")
    def outlier_detection(
        self,
    ) -> Optional[pulumi.Input[BackendServiceOutlierDetectionArgs]]: ...
    @outlier_detection.setter
    def outlier_detection(
        self, value: Optional[pulumi.Input[BackendServiceOutlierDetectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[BackendServiceParamsArgs]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[BackendServiceParamsArgs]]): ...
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
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(
        self,
    ) -> Optional[pulumi.Input[BackendServiceSecuritySettingsArgs]]: ...
    @security_settings.setter
    def security_settings(
        self, value: Optional[pulumi.Input[BackendServiceSecuritySettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceLbPolicy")
    def service_lb_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_lb_policy.setter
    def service_lb_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @session_affinity.setter
    def session_affinity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="strongSessionAffinityCookie")
    def strong_session_affinity_cookie(
        self,
    ) -> Optional[pulumi.Input[BackendServiceStrongSessionAffinityCookieArgs]]: ...
    @strong_session_affinity_cookie.setter
    def strong_session_affinity_cookie(
        self,
        value: Optional[pulumi.Input[BackendServiceStrongSessionAffinityCookieArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(self) -> Optional[pulumi.Input[BackendServiceTlsSettingsArgs]]: ...
    @tls_settings.setter
    def tls_settings(
        self, value: Optional[pulumi.Input[BackendServiceTlsSettingsArgs]]
    ): ...

@pulumi.type_token("gcp:compute/backendService:BackendService")
class BackendService(pulumi.CustomResource):
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
                        Union[BackendServiceBackendArgs, BackendServiceBackendArgsDict]
                    ]
                ]
            ]
        ] = ...,
        cdn_policy: Optional[
            pulumi.Input[
                Union[BackendServiceCdnPolicyArgs, BackendServiceCdnPolicyArgsDict]
            ]
        ] = ...,
        circuit_breakers: Optional[
            pulumi.Input[
                Union[
                    BackendServiceCircuitBreakersArgs,
                    BackendServiceCircuitBreakersArgsDict,
                ]
            ]
        ] = ...,
        compression_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_draining_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        consistent_hash: Optional[
            pulumi.Input[
                Union[
                    BackendServiceConsistentHashArgs,
                    BackendServiceConsistentHashArgsDict,
                ]
            ]
        ] = ...,
        custom_metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BackendServiceCustomMetricArgs,
                            BackendServiceCustomMetricArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        custom_request_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_response_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_forwarding: Optional[
            pulumi.Input[
                Union[
                    BackendServiceDynamicForwardingArgs,
                    BackendServiceDynamicForwardingArgsDict,
                ]
            ]
        ] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        external_managed_migration_state: Optional[pulumi.Input[_builtins.str]] = ...,
        external_managed_migration_testing_percentage: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        health_checks: Optional[pulumi.Input[_builtins.str]] = ...,
        iap: Optional[
            pulumi.Input[Union[BackendServiceIapArgs, BackendServiceIapArgsDict]]
        ] = ...,
        ip_address_selection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        locality_lb_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BackendServiceLocalityLbPolicyArgs,
                            BackendServiceLocalityLbPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        locality_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[BackendServiceLogConfigArgs, BackendServiceLogConfigArgsDict]
            ]
        ] = ...,
        max_stream_duration: Optional[
            pulumi.Input[
                Union[
                    BackendServiceMaxStreamDurationArgs,
                    BackendServiceMaxStreamDurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_pass_through_lb_traffic_policy: Optional[
            pulumi.Input[
                Union[
                    BackendServiceNetworkPassThroughLbTrafficPolicyArgs,
                    BackendServiceNetworkPassThroughLbTrafficPolicyArgsDict,
                ]
            ]
        ] = ...,
        outlier_detection: Optional[
            pulumi.Input[
                Union[
                    BackendServiceOutlierDetectionArgs,
                    BackendServiceOutlierDetectionArgsDict,
                ]
            ]
        ] = ...,
        params: Optional[
            pulumi.Input[Union[BackendServiceParamsArgs, BackendServiceParamsArgsDict]]
        ] = ...,
        port_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        security_settings: Optional[
            pulumi.Input[
                Union[
                    BackendServiceSecuritySettingsArgs,
                    BackendServiceSecuritySettingsArgsDict,
                ]
            ]
        ] = ...,
        service_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_session_affinity_cookie: Optional[
            pulumi.Input[
                Union[
                    BackendServiceStrongSessionAffinityCookieArgs,
                    BackendServiceStrongSessionAffinityCookieArgsDict,
                ]
            ]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_settings: Optional[
            pulumi.Input[
                Union[BackendServiceTlsSettingsArgs, BackendServiceTlsSettingsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[BackendServiceArgs] = ...,
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
                        Union[BackendServiceBackendArgs, BackendServiceBackendArgsDict]
                    ]
                ]
            ]
        ] = ...,
        cdn_policy: Optional[
            pulumi.Input[
                Union[BackendServiceCdnPolicyArgs, BackendServiceCdnPolicyArgsDict]
            ]
        ] = ...,
        circuit_breakers: Optional[
            pulumi.Input[
                Union[
                    BackendServiceCircuitBreakersArgs,
                    BackendServiceCircuitBreakersArgsDict,
                ]
            ]
        ] = ...,
        compression_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_draining_timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        consistent_hash: Optional[
            pulumi.Input[
                Union[
                    BackendServiceConsistentHashArgs,
                    BackendServiceConsistentHashArgsDict,
                ]
            ]
        ] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_metrics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BackendServiceCustomMetricArgs,
                            BackendServiceCustomMetricArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        custom_request_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_response_headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        dynamic_forwarding: Optional[
            pulumi.Input[
                Union[
                    BackendServiceDynamicForwardingArgs,
                    BackendServiceDynamicForwardingArgsDict,
                ]
            ]
        ] = ...,
        edge_security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_cdn: Optional[pulumi.Input[_builtins.bool]] = ...,
        external_managed_migration_state: Optional[pulumi.Input[_builtins.str]] = ...,
        external_managed_migration_testing_percentage: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        generated_id: Optional[pulumi.Input[_builtins.int]] = ...,
        health_checks: Optional[pulumi.Input[_builtins.str]] = ...,
        iap: Optional[
            pulumi.Input[Union[BackendServiceIapArgs, BackendServiceIapArgsDict]]
        ] = ...,
        ip_address_selection_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        load_balancing_scheme: Optional[pulumi.Input[_builtins.str]] = ...,
        locality_lb_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            BackendServiceLocalityLbPolicyArgs,
                            BackendServiceLocalityLbPolicyArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        locality_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[BackendServiceLogConfigArgs, BackendServiceLogConfigArgsDict]
            ]
        ] = ...,
        max_stream_duration: Optional[
            pulumi.Input[
                Union[
                    BackendServiceMaxStreamDurationArgs,
                    BackendServiceMaxStreamDurationArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_pass_through_lb_traffic_policy: Optional[
            pulumi.Input[
                Union[
                    BackendServiceNetworkPassThroughLbTrafficPolicyArgs,
                    BackendServiceNetworkPassThroughLbTrafficPolicyArgsDict,
                ]
            ]
        ] = ...,
        outlier_detection: Optional[
            pulumi.Input[
                Union[
                    BackendServiceOutlierDetectionArgs,
                    BackendServiceOutlierDetectionArgsDict,
                ]
            ]
        ] = ...,
        params: Optional[
            pulumi.Input[Union[BackendServiceParamsArgs, BackendServiceParamsArgsDict]]
        ] = ...,
        port_name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
        security_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        security_settings: Optional[
            pulumi.Input[
                Union[
                    BackendServiceSecuritySettingsArgs,
                    BackendServiceSecuritySettingsArgsDict,
                ]
            ]
        ] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        service_lb_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.str]] = ...,
        strong_session_affinity_cookie: Optional[
            pulumi.Input[
                Union[
                    BackendServiceStrongSessionAffinityCookieArgs,
                    BackendServiceStrongSessionAffinityCookieArgsDict,
                ]
            ]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        tls_settings: Optional[
            pulumi.Input[
                Union[BackendServiceTlsSettingsArgs, BackendServiceTlsSettingsArgsDict]
            ]
        ] = ...,
    ) -> BackendService: ...
    @_builtins.property
    @pulumi.getter(name="affinityCookieTtlSec")
    def affinity_cookie_ttl_sec(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def backends(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BackendServiceBackend]]]: ...
    @_builtins.property
    @pulumi.getter(name="cdnPolicy")
    def cdn_policy(self) -> pulumi.Output[outputs.BackendServiceCdnPolicy]: ...
    @_builtins.property
    @pulumi.getter(name="circuitBreakers")
    def circuit_breakers(
        self,
    ) -> pulumi.Output[Optional[outputs.BackendServiceCircuitBreakers]]: ...
    @_builtins.property
    @pulumi.getter(name="compressionMode")
    def compression_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="connectionDrainingTimeoutSec")
    def connection_draining_timeout_sec(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="consistentHash")
    def consistent_hash(
        self,
    ) -> pulumi.Output[Optional[outputs.BackendServiceConsistentHash]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customMetrics")
    def custom_metrics(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BackendServiceCustomMetric]]]: ...
    @_builtins.property
    @pulumi.getter(name="customRequestHeaders")
    def custom_request_headers(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="customResponseHeaders")
    def custom_response_headers(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="dynamicForwarding")
    def dynamic_forwarding(
        self,
    ) -> pulumi.Output[Optional[outputs.BackendServiceDynamicForwarding]]: ...
    @_builtins.property
    @pulumi.getter(name="edgeSecurityPolicy")
    def edge_security_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableCdn")
    def enable_cdn(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="externalManagedMigrationState")
    def external_managed_migration_state(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="externalManagedMigrationTestingPercentage")
    def external_managed_migration_testing_percentage(
        self,
    ) -> pulumi.Output[Optional[_builtins.float]]: ...
    @_builtins.property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="generatedId")
    def generated_id(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="healthChecks")
    def health_checks(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def iap(self) -> pulumi.Output[outputs.BackendServiceIap]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddressSelectionPolicy")
    def ip_address_selection_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="loadBalancingScheme")
    def load_balancing_scheme(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="localityLbPolicies")
    def locality_lb_policies(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.BackendServiceLocalityLbPolicy]]]: ...
    @_builtins.property
    @pulumi.getter(name="localityLbPolicy")
    def locality_lb_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[outputs.BackendServiceLogConfig]: ...
    @_builtins.property
    @pulumi.getter(name="maxStreamDuration")
    def max_stream_duration(
        self,
    ) -> pulumi.Output[Optional[outputs.BackendServiceMaxStreamDuration]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkPassThroughLbTrafficPolicy")
    def network_pass_through_lb_traffic_policy(
        self,
    ) -> pulumi.Output[
        Optional[outputs.BackendServiceNetworkPassThroughLbTrafficPolicy]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outlierDetection")
    def outlier_detection(
        self,
    ) -> pulumi.Output[Optional[outputs.BackendServiceOutlierDetection]]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> pulumi.Output[Optional[outputs.BackendServiceParams]]: ...
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
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.BackendServiceSecuritySettings]]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceLbPolicy")
    def service_lb_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="strongSessionAffinityCookie")
    def strong_session_affinity_cookie(
        self,
    ) -> pulumi.Output[Optional[outputs.BackendServiceStrongSessionAffinityCookie]]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tlsSettings")
    def tls_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.BackendServiceTlsSettings]]: ...
