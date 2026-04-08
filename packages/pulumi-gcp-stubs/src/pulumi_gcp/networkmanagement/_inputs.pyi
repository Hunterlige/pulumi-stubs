import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConnectivityTestDestinationArgs",
    "ConnectivityTestDestinationArgsDict",
    "ConnectivityTestSourceArgs",
    "ConnectivityTestSourceArgsDict",
    "ConnectivityTestSourceAppEngineVersionArgs",
    "ConnectivityTestSourceAppEngineVersionArgsDict",
    "ConnectivityTestSourceCloudFunctionArgs",
    "ConnectivityTestSourceCloudFunctionArgsDict",
    "ConnectivityTestSourceCloudRunRevisionArgs",
    "ConnectivityTestSourceCloudRunRevisionArgsDict",
]

class ConnectivityTestDestinationArgsDict(TypedDict):
    cloud_sql_instance: NotRequired[pulumi.Input[_builtins.str]]
    forwarding_rule: NotRequired[pulumi.Input[_builtins.str]]
    fqdn: NotRequired[pulumi.Input[_builtins.str]]
    gke_master_cluster: NotRequired[pulumi.Input[_builtins.str]]
    instance: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    redis_cluster: NotRequired[pulumi.Input[_builtins.str]]
    redis_instance: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectivityTestDestinationArgs:
    def __init__(
        __self__,
        *,
        cloud_sql_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        forwarding_rule: Optional[pulumi.Input[_builtins.str]] = ...,
        fqdn: Optional[pulumi.Input[_builtins.str]] = ...,
        gke_master_cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        redis_cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        redis_instance: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_sql_instance.setter
    def cloud_sql_instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forwardingRule")
    def forwarding_rule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @forwarding_rule.setter
    def forwarding_rule(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gkeMasterCluster")
    def gke_master_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gke_master_cluster.setter
    def gke_master_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redisCluster")
    def redis_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redis_cluster.setter
    def redis_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="redisInstance")
    def redis_instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @redis_instance.setter
    def redis_instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectivityTestSourceArgsDict(TypedDict):
    app_engine_version: NotRequired[
        pulumi.Input[ConnectivityTestSourceAppEngineVersionArgsDict]
    ]
    cloud_function: NotRequired[
        pulumi.Input[ConnectivityTestSourceCloudFunctionArgsDict]
    ]
    cloud_run_revision: NotRequired[
        pulumi.Input[ConnectivityTestSourceCloudRunRevisionArgsDict]
    ]
    cloud_sql_instance: NotRequired[pulumi.Input[_builtins.str]]
    gke_master_cluster: NotRequired[pulumi.Input[_builtins.str]]
    instance: NotRequired[pulumi.Input[_builtins.str]]
    ip_address: NotRequired[pulumi.Input[_builtins.str]]
    network: NotRequired[pulumi.Input[_builtins.str]]
    network_type: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectivityTestSourceArgs:
    def __init__(
        __self__,
        *,
        app_engine_version: Optional[
            pulumi.Input[ConnectivityTestSourceAppEngineVersionArgs]
        ] = ...,
        cloud_function: Optional[
            pulumi.Input[ConnectivityTestSourceCloudFunctionArgs]
        ] = ...,
        cloud_run_revision: Optional[
            pulumi.Input[ConnectivityTestSourceCloudRunRevisionArgs]
        ] = ...,
        cloud_sql_instance: Optional[pulumi.Input[_builtins.str]] = ...,
        gke_master_cluster: Optional[pulumi.Input[_builtins.str]] = ...,
        instance: Optional[pulumi.Input[_builtins.str]] = ...,
        ip_address: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        network_type: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appEngineVersion")
    def app_engine_version(
        self,
    ) -> Optional[pulumi.Input[ConnectivityTestSourceAppEngineVersionArgs]]: ...
    @app_engine_version.setter
    def app_engine_version(
        self, value: Optional[pulumi.Input[ConnectivityTestSourceAppEngineVersionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudFunction")
    def cloud_function(
        self,
    ) -> Optional[pulumi.Input[ConnectivityTestSourceCloudFunctionArgs]]: ...
    @cloud_function.setter
    def cloud_function(
        self, value: Optional[pulumi.Input[ConnectivityTestSourceCloudFunctionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudRunRevision")
    def cloud_run_revision(
        self,
    ) -> Optional[pulumi.Input[ConnectivityTestSourceCloudRunRevisionArgs]]: ...
    @cloud_run_revision.setter
    def cloud_run_revision(
        self, value: Optional[pulumi.Input[ConnectivityTestSourceCloudRunRevisionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cloud_sql_instance.setter
    def cloud_sql_instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gkeMasterCluster")
    def gke_master_cluster(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gke_master_cluster.setter
    def gke_master_cluster(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def instance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance.setter
    def instance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_type.setter
    def network_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectivityTestSourceAppEngineVersionArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectivityTestSourceAppEngineVersionArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectivityTestSourceCloudFunctionArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectivityTestSourceCloudFunctionArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectivityTestSourceCloudRunRevisionArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectivityTestSourceCloudRunRevisionArgs:
    def __init__(
        __self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
