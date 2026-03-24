

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['HealthCheckArgs', 'HealthCheck']
@pulumi.input_type
class HealthCheckArgs:
    def __init__(__self__, *, check_interval_sec: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., grpc_health_check: Optional[pulumi.Input[HealthCheckGrpcHealthCheckArgs]] = ..., grpc_tls_health_check: Optional[pulumi.Input[HealthCheckGrpcTlsHealthCheckArgs]] = ..., healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ..., http2_health_check: Optional[pulumi.Input[HealthCheckHttp2HealthCheckArgs]] = ..., http_health_check: Optional[pulumi.Input[HealthCheckHttpHealthCheckArgs]] = ..., https_health_check: Optional[pulumi.Input[HealthCheckHttpsHealthCheckArgs]] = ..., log_config: Optional[pulumi.Input[HealthCheckLogConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., source_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ssl_health_check: Optional[pulumi.Input[HealthCheckSslHealthCheckArgs]] = ..., tcp_health_check: Optional[pulumi.Input[HealthCheckTcpHealthCheckArgs]] = ..., timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @check_interval_sec.setter
    def check_interval_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(self) -> Optional[pulumi.Input[HealthCheckGrpcHealthCheckArgs]]:
        
        ...
    
    @grpc_health_check.setter
    def grpc_health_check(self, value: Optional[pulumi.Input[HealthCheckGrpcHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcTlsHealthCheck")
    def grpc_tls_health_check(self) -> Optional[pulumi.Input[HealthCheckGrpcTlsHealthCheckArgs]]:
        
        ...
    
    @grpc_tls_health_check.setter
    def grpc_tls_health_check(self, value: Optional[pulumi.Input[HealthCheckGrpcTlsHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @healthy_threshold.setter
    def healthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(self) -> Optional[pulumi.Input[HealthCheckHttp2HealthCheckArgs]]:
        
        ...
    
    @http2_health_check.setter
    def http2_health_check(self, value: Optional[pulumi.Input[HealthCheckHttp2HealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(self) -> Optional[pulumi.Input[HealthCheckHttpHealthCheckArgs]]:
        
        ...
    
    @http_health_check.setter
    def http_health_check(self, value: Optional[pulumi.Input[HealthCheckHttpHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(self) -> Optional[pulumi.Input[HealthCheckHttpsHealthCheckArgs]]:
        
        ...
    
    @https_health_check.setter
    def https_health_check(self, value: Optional[pulumi.Input[HealthCheckHttpsHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[HealthCheckLogConfigArgs]]:
        
        ...
    
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[HealthCheckLogConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRegions")
    def source_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_regions.setter
    def source_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(self) -> Optional[pulumi.Input[HealthCheckSslHealthCheckArgs]]:
        
        ...
    
    @ssl_health_check.setter
    def ssl_health_check(self, value: Optional[pulumi.Input[HealthCheckSslHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(self) -> Optional[pulumi.Input[HealthCheckTcpHealthCheckArgs]]:
        
        ...
    
    @tcp_health_check.setter
    def tcp_health_check(self, value: Optional[pulumi.Input[HealthCheckTcpHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.input_type
class _HealthCheckState:
    def __init__(__self__, *, check_interval_sec: Optional[pulumi.Input[_builtins.int]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., grpc_health_check: Optional[pulumi.Input[HealthCheckGrpcHealthCheckArgs]] = ..., grpc_tls_health_check: Optional[pulumi.Input[HealthCheckGrpcTlsHealthCheckArgs]] = ..., healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ..., http2_health_check: Optional[pulumi.Input[HealthCheckHttp2HealthCheckArgs]] = ..., http_health_check: Optional[pulumi.Input[HealthCheckHttpHealthCheckArgs]] = ..., https_health_check: Optional[pulumi.Input[HealthCheckHttpsHealthCheckArgs]] = ..., log_config: Optional[pulumi.Input[HealthCheckLogConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., source_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ssl_health_check: Optional[pulumi.Input[HealthCheckSslHealthCheckArgs]] = ..., tcp_health_check: Optional[pulumi.Input[HealthCheckTcpHealthCheckArgs]] = ..., timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @check_interval_sec.setter
    def check_interval_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @creation_timestamp.setter
    def creation_timestamp(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(self) -> Optional[pulumi.Input[HealthCheckGrpcHealthCheckArgs]]:
        
        ...
    
    @grpc_health_check.setter
    def grpc_health_check(self, value: Optional[pulumi.Input[HealthCheckGrpcHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcTlsHealthCheck")
    def grpc_tls_health_check(self) -> Optional[pulumi.Input[HealthCheckGrpcTlsHealthCheckArgs]]:
        
        ...
    
    @grpc_tls_health_check.setter
    def grpc_tls_health_check(self, value: Optional[pulumi.Input[HealthCheckGrpcTlsHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @healthy_threshold.setter
    def healthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(self) -> Optional[pulumi.Input[HealthCheckHttp2HealthCheckArgs]]:
        
        ...
    
    @http2_health_check.setter
    def http2_health_check(self, value: Optional[pulumi.Input[HealthCheckHttp2HealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(self) -> Optional[pulumi.Input[HealthCheckHttpHealthCheckArgs]]:
        
        ...
    
    @http_health_check.setter
    def http_health_check(self, value: Optional[pulumi.Input[HealthCheckHttpHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(self) -> Optional[pulumi.Input[HealthCheckHttpsHealthCheckArgs]]:
        
        ...
    
    @https_health_check.setter
    def https_health_check(self, value: Optional[pulumi.Input[HealthCheckHttpsHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> Optional[pulumi.Input[HealthCheckLogConfigArgs]]:
        
        ...
    
    @log_config.setter
    def log_config(self, value: Optional[pulumi.Input[HealthCheckLogConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRegions")
    def source_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @source_regions.setter
    def source_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(self) -> Optional[pulumi.Input[HealthCheckSslHealthCheckArgs]]:
        
        ...
    
    @ssl_health_check.setter
    def ssl_health_check(self, value: Optional[pulumi.Input[HealthCheckSslHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(self) -> Optional[pulumi.Input[HealthCheckTcpHealthCheckArgs]]:
        
        ...
    
    @tcp_health_check.setter
    def tcp_health_check(self, value: Optional[pulumi.Input[HealthCheckTcpHealthCheckArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @timeout_sec.setter
    def timeout_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("gcp:compute/healthCheck:HealthCheck")
class HealthCheck(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., check_interval_sec: Optional[pulumi.Input[_builtins.int]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., grpc_health_check: Optional[pulumi.Input[Union[HealthCheckGrpcHealthCheckArgs, HealthCheckGrpcHealthCheckArgsDict]]] = ..., grpc_tls_health_check: Optional[pulumi.Input[Union[HealthCheckGrpcTlsHealthCheckArgs, HealthCheckGrpcTlsHealthCheckArgsDict]]] = ..., healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ..., http2_health_check: Optional[pulumi.Input[Union[HealthCheckHttp2HealthCheckArgs, HealthCheckHttp2HealthCheckArgsDict]]] = ..., http_health_check: Optional[pulumi.Input[Union[HealthCheckHttpHealthCheckArgs, HealthCheckHttpHealthCheckArgsDict]]] = ..., https_health_check: Optional[pulumi.Input[Union[HealthCheckHttpsHealthCheckArgs, HealthCheckHttpsHealthCheckArgsDict]]] = ..., log_config: Optional[pulumi.Input[Union[HealthCheckLogConfigArgs, HealthCheckLogConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., source_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ssl_health_check: Optional[pulumi.Input[Union[HealthCheckSslHealthCheckArgs, HealthCheckSslHealthCheckArgsDict]]] = ..., tcp_health_check: Optional[pulumi.Input[Union[HealthCheckTcpHealthCheckArgs, HealthCheckTcpHealthCheckArgsDict]]] = ..., timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[HealthCheckArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., check_interval_sec: Optional[pulumi.Input[_builtins.int]] = ..., creation_timestamp: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., grpc_health_check: Optional[pulumi.Input[Union[HealthCheckGrpcHealthCheckArgs, HealthCheckGrpcHealthCheckArgsDict]]] = ..., grpc_tls_health_check: Optional[pulumi.Input[Union[HealthCheckGrpcTlsHealthCheckArgs, HealthCheckGrpcTlsHealthCheckArgsDict]]] = ..., healthy_threshold: Optional[pulumi.Input[_builtins.int]] = ..., http2_health_check: Optional[pulumi.Input[Union[HealthCheckHttp2HealthCheckArgs, HealthCheckHttp2HealthCheckArgsDict]]] = ..., http_health_check: Optional[pulumi.Input[Union[HealthCheckHttpHealthCheckArgs, HealthCheckHttpHealthCheckArgsDict]]] = ..., https_health_check: Optional[pulumi.Input[Union[HealthCheckHttpsHealthCheckArgs, HealthCheckHttpsHealthCheckArgsDict]]] = ..., log_config: Optional[pulumi.Input[Union[HealthCheckLogConfigArgs, HealthCheckLogConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., self_link: Optional[pulumi.Input[_builtins.str]] = ..., source_regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., ssl_health_check: Optional[pulumi.Input[Union[HealthCheckSslHealthCheckArgs, HealthCheckSslHealthCheckArgsDict]]] = ..., tcp_health_check: Optional[pulumi.Input[Union[HealthCheckTcpHealthCheckArgs, HealthCheckTcpHealthCheckArgsDict]]] = ..., timeout_sec: Optional[pulumi.Input[_builtins.int]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., unhealthy_threshold: Optional[pulumi.Input[_builtins.int]] = ...) -> HealthCheck:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcHealthCheck")
    def grpc_health_check(self) -> pulumi.Output[Optional[outputs.HealthCheckGrpcHealthCheck]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcTlsHealthCheck")
    def grpc_tls_health_check(self) -> pulumi.Output[Optional[outputs.HealthCheckGrpcTlsHealthCheck]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="http2HealthCheck")
    def http2_health_check(self) -> pulumi.Output[Optional[outputs.HealthCheckHttp2HealthCheck]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHealthCheck")
    def http_health_check(self) -> pulumi.Output[Optional[outputs.HealthCheckHttpHealthCheck]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsHealthCheck")
    def https_health_check(self) -> pulumi.Output[Optional[outputs.HealthCheckHttpsHealthCheck]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfig")
    def log_config(self) -> pulumi.Output[outputs.HealthCheckLogConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRegions")
    def source_regions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslHealthCheck")
    def ssl_health_check(self) -> pulumi.Output[Optional[outputs.HealthCheckSslHealthCheck]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpHealthCheck")
    def tcp_health_check(self) -> pulumi.Output[Optional[outputs.HealthCheckTcpHealthCheck]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    


