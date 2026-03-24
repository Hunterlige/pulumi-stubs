import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegionHealthCheckArgs", "RegionHealthCheck"]

@pulumi.input_type
class RegionHealthCheckArgs:
    def __init__(
        __self__,
        *,
        check_interval_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        grpc_health_check: Optional[
            pulumi.Input[RegionHealthCheckGrpcHealthCheckArgs]
        ] = ...,
        grpc_tls_health_check: Optional[
            pulumi.Input[RegionHealthCheckGrpcTlsHealthCheckArgs]
        ] = ...,
        healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        http2_health_check: Optional[
            pulumi.Input[RegionHealthCheckHttp2HealthCheckArgs]
        ] = ...,
        http_health_check: Optional[
            pulumi.Input[RegionHealthCheckHttpHealthCheckArgs]
        ] = ...,
        https_health_check: Optional[
            pulumi.Input[RegionHealthCheckHttpsHealthCheckArgs]
        ] = ...,
        log_config: Optional[pulumi.Input[RegionHealthCheckLogConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_health_check: Optional[
            pulumi.Input[RegionHealthCheckSslHealthCheckArgs]
        ] = ...,
        tcp_health_check: Optional[
            pulumi.Input[RegionHealthCheckTcpHealthCheckArgs]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @check_interval_sec.setter
    def check_interval_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckGrpcHealthCheckArgs]]: ...
    @grpc_health_check.setter
    def grpc_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckGrpcHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grpcTlsHealthCheck")
    def grpc_tls_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckGrpcTlsHealthCheckArgs]]: ...
    @grpc_tls_health_check.setter
    def grpc_tls_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckGrpcTlsHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @healthy_threshold.setter
    def healthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckHttp2HealthCheckArgs]]: ...
    @http2_health_check.setter
    def http2_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckHttp2HealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckHttpHealthCheckArgs]]: ...
    @http_health_check.setter
    def http_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckHttpHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckHttpsHealthCheckArgs]]: ...
    @https_health_check.setter
    def https_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckHttpsHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[RegionHealthCheckLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[RegionHealthCheckLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckSslHealthCheckArgs]]: ...
    @ssl_health_check.setter
    def ssl_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckSslHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckTcpHealthCheckArgs]]: ...
    @tcp_health_check.setter
    def tcp_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckTcpHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.input_type
class _RegionHealthCheckState:
    def __init__(
        __self__,
        *,
        check_interval_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        grpc_health_check: Optional[
            pulumi.Input[RegionHealthCheckGrpcHealthCheckArgs]
        ] = ...,
        grpc_tls_health_check: Optional[
            pulumi.Input[RegionHealthCheckGrpcTlsHealthCheckArgs]
        ] = ...,
        health_check_id: Optional[pulumi.Input[_builtins.int]] = ...,
        healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        http2_health_check: Optional[
            pulumi.Input[RegionHealthCheckHttp2HealthCheckArgs]
        ] = ...,
        http_health_check: Optional[
            pulumi.Input[RegionHealthCheckHttpHealthCheckArgs]
        ] = ...,
        https_health_check: Optional[
            pulumi.Input[RegionHealthCheckHttpsHealthCheckArgs]
        ] = ...,
        log_config: Optional[pulumi.Input[RegionHealthCheckLogConfigArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_health_check: Optional[
            pulumi.Input[RegionHealthCheckSslHealthCheckArgs]
        ] = ...,
        tcp_health_check: Optional[
            pulumi.Input[RegionHealthCheckTcpHealthCheckArgs]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @check_interval_sec.setter
    def check_interval_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckGrpcHealthCheckArgs]]: ...
    @grpc_health_check.setter
    def grpc_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckGrpcHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="grpcTlsHealthCheck")
    def grpc_tls_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckGrpcTlsHealthCheckArgs]]: ...
    @grpc_tls_health_check.setter
    def grpc_tls_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckGrpcTlsHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @health_check_id.setter
    def health_check_id(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @healthy_threshold.setter
    def healthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckHttp2HealthCheckArgs]]: ...
    @http2_health_check.setter
    def http2_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckHttp2HealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckHttpHealthCheckArgs]]: ...
    @http_health_check.setter
    def http_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckHttpHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckHttpsHealthCheckArgs]]: ...
    @https_health_check.setter
    def https_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckHttpsHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[RegionHealthCheckLogConfigArgs]]: ...
    @log_config.setter
    def log_config(
        self, value: Optional[pulumi.Input[RegionHealthCheckLogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckSslHealthCheckArgs]]: ...
    @ssl_health_check.setter
    def ssl_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckSslHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(
        self,
    ) -> Optional[pulumi.Input[RegionHealthCheckTcpHealthCheckArgs]]: ...
    @tcp_health_check.setter
    def tcp_health_check(
        self, value: Optional[pulumi.Input[RegionHealthCheckTcpHealthCheckArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...

@pulumi.type_token("gcp:compute/regionHealthCheck:RegionHealthCheck")
class RegionHealthCheck(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        check_interval_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        grpc_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckGrpcHealthCheckArgs,
                    RegionHealthCheckGrpcHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        grpc_tls_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckGrpcTlsHealthCheckArgs,
                    RegionHealthCheckGrpcTlsHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        http2_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckHttp2HealthCheckArgs,
                    RegionHealthCheckHttp2HealthCheckArgsDict,
                ]
            ]
        ] = ...,
        http_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckHttpHealthCheckArgs,
                    RegionHealthCheckHttpHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        https_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckHttpsHealthCheckArgs,
                    RegionHealthCheckHttpsHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckLogConfigArgs, RegionHealthCheckLogConfigArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckSslHealthCheckArgs,
                    RegionHealthCheckSslHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        tcp_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckTcpHealthCheckArgs,
                    RegionHealthCheckTcpHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[RegionHealthCheckArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        check_interval_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        grpc_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckGrpcHealthCheckArgs,
                    RegionHealthCheckGrpcHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        grpc_tls_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckGrpcTlsHealthCheckArgs,
                    RegionHealthCheckGrpcTlsHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        health_check_id: Optional[pulumi.Input[_builtins.int]] = ...,
        healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        http2_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckHttp2HealthCheckArgs,
                    RegionHealthCheckHttp2HealthCheckArgsDict,
                ]
            ]
        ] = ...,
        http_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckHttpHealthCheckArgs,
                    RegionHealthCheckHttpHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        https_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckHttpsHealthCheckArgs,
                    RegionHealthCheckHttpsHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        log_config: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckLogConfigArgs, RegionHealthCheckLogConfigArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        ssl_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckSslHealthCheckArgs,
                    RegionHealthCheckSslHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        tcp_health_check: Optional[
            pulumi.Input[
                Union[
                    RegionHealthCheckTcpHealthCheckArgs,
                    RegionHealthCheckTcpHealthCheckArgsDict,
                ]
            ]
        ] = ...,
        timeout_sec: Optional[pulumi.Input[_builtins.int]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> RegionHealthCheck: ...
    @_builtins.property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionHealthCheckGrpcHealthCheck]]: ...
    @_builtins.property
    @pulumi.getter(name="grpcTlsHealthCheck")
    def grpc_tls_health_check(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionHealthCheckGrpcTlsHealthCheck]]: ...
    @_builtins.property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionHealthCheckHttp2HealthCheck]]: ...
    @_builtins.property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionHealthCheckHttpHealthCheck]]: ...
    @_builtins.property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionHealthCheckHttpsHealthCheck]]: ...
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[outputs.RegionHealthCheckLogConfig]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionHealthCheckSslHealthCheck]]: ...
    @_builtins.property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(
        self,
    ) -> pulumi.Output[Optional[outputs.RegionHealthCheckTcpHealthCheck]]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> pulumi.Output[Optional[_builtins.int]]: ...
