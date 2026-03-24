import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectivityTestDestination",
    "ConnectivityTestSource",
    "ConnectivityTestSourceAppEngineVersion",
    "ConnectivityTestSourceCloudFunction",
    "ConnectivityTestSourceCloudRunRevision",
    "GetConnectivityTestRunReachabilityDetailResult",
    ...,
    ...,
    ...,
    "GetConnectivityTestsConnectivityTestResult",
    ...,
    "GetConnectivityTestsConnectivityTestSourceResult",
    ...,
    ...,
    ...,
]

@pulumi.output_type
class ConnectivityTestDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_sql_instance: Optional[_builtins.str] = ...,
        forwarding_rule: Optional[_builtins.str] = ...,
        fqdn: Optional[_builtins.str] = ...,
        gke_master_cluster: Optional[_builtins.str] = ...,
        instance: Optional[_builtins.str] = ...,
        ip_address: Optional[_builtins.str] = ...,
        network: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        project_id: Optional[_builtins.str] = ...,
        redis_cluster: Optional[_builtins.str] = ...,
        redis_instance: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gkeMasterCluster")
    def gke_master_cluster(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redisCluster")
    def redis_cluster(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="redisInstance")
    def redis_instance(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectivityTestSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        app_engine_version: Optional[
            outputs.ConnectivityTestSourceAppEngineVersion
        ] = ...,
        cloud_function: Optional[outputs.ConnectivityTestSourceCloudFunction] = ...,
        cloud_run_revision: Optional[
            outputs.ConnectivityTestSourceCloudRunRevision
        ] = ...,
        cloud_sql_instance: Optional[_builtins.str] = ...,
        gke_master_cluster: Optional[_builtins.str] = ...,
        instance: Optional[_builtins.str] = ...,
        ip_address: Optional[_builtins.str] = ...,
        network: Optional[_builtins.str] = ...,
        network_type: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
        project_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appEngineVersion")
    def app_engine_version(
        self,
    ) -> Optional[outputs.ConnectivityTestSourceAppEngineVersion]: ...
    @_builtins.property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(
        self,
    ) -> Optional[outputs.ConnectivityTestSourceCloudFunction]: ...
    @_builtins.property
    @pulumi.getter(name="cloudRunRevision")
    def cloud_run_revision(
        self,
    ) -> Optional[outputs.ConnectivityTestSourceCloudRunRevision]: ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="gkeMasterCluster")
    def gke_master_cluster(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectivityTestSourceAppEngineVersion(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectivityTestSourceCloudFunction(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConnectivityTestSourceCloudRunRevision(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetConnectivityTestRunReachabilityDetailResult(dict):
    def __init__(
        __self__,
        *,
        result: _builtins.str,
        traces: Sequence[outputs.GetConnectivityTestRunReachabilityDetailTraceResult],
        verify_time: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def result(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def traces(
        self,
    ) -> Sequence[outputs.GetConnectivityTestRunReachabilityDetailTraceResult]: ...
    @_builtins.property
    @pulumi.getter(name="verifyTime")
    def verify_time(self) -> _builtins.str: ...

@pulumi.output_type
class GetConnectivityTestRunReachabilityDetailTraceResult(dict):
    def __init__(
        __self__,
        *,
        endpoint_infos: Sequence[
            outputs.GetConnectivityTestRunReachabilityDetailTraceEndpointInfoResult
        ],
        forward_trace_id: _builtins.int,
        steps: Sequence[
            outputs.GetConnectivityTestRunReachabilityDetailTraceStepResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointInfos")
    def endpoint_infos(
        self,
    ) -> Sequence[
        outputs.GetConnectivityTestRunReachabilityDetailTraceEndpointInfoResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="forwardTraceId")
    def forward_trace_id(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def steps(
        self,
    ) -> Sequence[outputs.GetConnectivityTestRunReachabilityDetailTraceStepResult]: ...

@pulumi.output_type
class GetConnectivityTestRunReachabilityDetailTraceEndpointInfoResult(dict):
    def __init__(
        __self__,
        *,
        destination_ip: _builtins.str,
        destination_network_uri: _builtins.str,
        destination_port: _builtins.int,
        protocol: _builtins.str,
        source_agent_uri: _builtins.str,
        source_ip: _builtins.str,
        source_network_uri: _builtins.str,
        source_port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationIp")
    def destination_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationNetworkUri")
    def destination_network_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceAgentUri")
    def source_agent_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceNetworkUri")
    def source_network_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourcePort")
    def source_port(self) -> _builtins.int: ...

@pulumi.output_type
class GetConnectivityTestRunReachabilityDetailTraceStepResult(dict):
    def __init__(
        __self__,
        *,
        causes_drop: _builtins.bool,
        description: _builtins.str,
        project_id: _builtins.str,
        state: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="causesDrop")
    def causes_drop(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str: ...

@pulumi.output_type
class GetConnectivityTestsConnectivityTestResult(dict):
    def __init__(
        __self__,
        *,
        bypass_firewall_checks: _builtins.bool,
        description: _builtins.str,
        destinations: Sequence[
            outputs.GetConnectivityTestsConnectivityTestDestinationResult
        ],
        effective_labels: Mapping[str, _builtins.str],
        labels: Mapping[str, _builtins.str],
        name: _builtins.str,
        project: _builtins.str,
        protocol: _builtins.str,
        pulumi_labels: Mapping[str, _builtins.str],
        related_projects: Sequence[_builtins.str],
        round_trip: _builtins.bool,
        sources: Sequence[outputs.GetConnectivityTestsConnectivityTestSourceResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bypassFirewallChecks")
    def bypass_firewall_checks(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Sequence[outputs.GetConnectivityTestsConnectivityTestDestinationResult]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relatedProjects")
    def related_projects(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roundTrip")
    def round_trip(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def sources(
        self,
    ) -> Sequence[outputs.GetConnectivityTestsConnectivityTestSourceResult]: ...

@pulumi.output_type
class GetConnectivityTestsConnectivityTestDestinationResult(dict):
    def __init__(
        __self__,
        *,
        cloud_sql_instance: _builtins.str,
        forwarding_rule: _builtins.str,
        fqdn: _builtins.str,
        gke_master_cluster: _builtins.str,
        instance: _builtins.str,
        ip_address: _builtins.str,
        network: _builtins.str,
        port: _builtins.int,
        project_id: _builtins.str,
        redis_cluster: _builtins.str,
        redis_instance: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gkeMasterCluster")
    def gke_master_cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="redisCluster")
    def redis_cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="redisInstance")
    def redis_instance(self) -> _builtins.str: ...

@pulumi.output_type
class GetConnectivityTestsConnectivityTestSourceResult(dict):
    def __init__(
        __self__,
        *,
        app_engine_versions: Sequence[
            outputs.GetConnectivityTestsConnectivityTestSourceAppEngineVersionResult
        ],
        cloud_functions: Sequence[
            outputs.GetConnectivityTestsConnectivityTestSourceCloudFunctionResult
        ],
        cloud_run_revisions: Sequence[
            outputs.GetConnectivityTestsConnectivityTestSourceCloudRunRevisionResult
        ],
        cloud_sql_instance: _builtins.str,
        gke_master_cluster: _builtins.str,
        instance: _builtins.str,
        ip_address: _builtins.str,
        network: _builtins.str,
        network_type: _builtins.str,
        port: _builtins.int,
        project_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appEngineVersions")
    def app_engine_versions(
        self,
    ) -> Sequence[
        outputs.GetConnectivityTestsConnectivityTestSourceAppEngineVersionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="cloudFunctions")
    def cloud_functions(
        self,
    ) -> Sequence[
        outputs.GetConnectivityTestsConnectivityTestSourceCloudFunctionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="cloudRunRevisions")
    def cloud_run_revisions(
        self,
    ) -> Sequence[
        outputs.GetConnectivityTestsConnectivityTestSourceCloudRunRevisionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="gkeMasterCluster")
    def gke_master_cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetConnectivityTestsConnectivityTestSourceAppEngineVersionResult(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetConnectivityTestsConnectivityTestSourceCloudFunctionResult(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetConnectivityTestsConnectivityTestSourceCloudRunRevisionResult(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
