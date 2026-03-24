

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetHealthCheckResult', 'AwaitableGetHealthCheckResult', 'get_health_check', 'get_health_check_output']
@pulumi.output_type
class GetHealthCheckResult:
    
    def __init__(__self__, check_interval_sec=..., creation_timestamp=..., description=..., grpc_health_checks=..., grpc_tls_health_checks=..., healthy_threshold=..., http2_health_checks=..., http_health_checks=..., https_health_checks=..., id=..., log_configs=..., name=..., project=..., self_link=..., source_regions=..., ssl_health_checks=..., tcp_health_checks=..., timeout_sec=..., type=..., unhealthy_threshold=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkIntervalSec")
    def check_interval_sec(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcHealthChecks")
    def grpc_health_checks(self) -> Sequence[outputs.GetHealthCheckGrpcHealthCheckResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="grpcTlsHealthChecks")
    def grpc_tls_health_checks(self) -> Sequence[outputs.GetHealthCheckGrpcTlsHealthCheckResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="http2HealthChecks")
    def http2_health_checks(self) -> Sequence[outputs.GetHealthCheckHttp2HealthCheckResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpHealthChecks")
    def http_health_checks(self) -> Sequence[outputs.GetHealthCheckHttpHealthCheckResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsHealthChecks")
    def https_health_checks(self) -> Sequence[outputs.GetHealthCheckHttpsHealthCheckResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logConfigs")
    def log_configs(self) -> Sequence[outputs.GetHealthCheckLogConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRegions")
    def source_regions(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslHealthChecks")
    def ssl_health_checks(self) -> Sequence[outputs.GetHealthCheckSslHealthCheckResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tcpHealthChecks")
    def tcp_health_checks(self) -> Sequence[outputs.GetHealthCheckTcpHealthCheckResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSec")
    def timeout_sec(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> _builtins.int:
        ...
    


class AwaitableGetHealthCheckResult(GetHealthCheckResult):
    def __await__(self): # -> Generator[Never, Any, GetHealthCheckResult]:
        ...
    


def get_health_check(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetHealthCheckResult:
    
    ...

def get_health_check_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetHealthCheckResult]:
    
    ...

