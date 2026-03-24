

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTargetGroupResult', 'AwaitableGetTargetGroupResult', 'get_target_group', 'get_target_group_output']
@pulumi.output_type
class GetTargetGroupResult:
    
    def __init__(__self__, arn=..., arn_suffix=..., connection_termination=..., deregistration_delay=..., health_check=..., id=..., lambda_multi_value_headers_enabled=..., load_balancer_arns=..., load_balancing_algorithm_type=..., load_balancing_anomaly_mitigation=..., load_balancing_cross_zone_enabled=..., name=..., port=..., preserve_client_ip=..., protocol=..., protocol_version=..., proxy_protocol_v2=..., region=..., slow_start=..., stickiness=..., tags=..., target_control_port=..., target_type=..., vpc_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="arnSuffix")
    def arn_suffix(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionTermination")
    def connection_termination(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deregistrationDelay")
    def deregistration_delay(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> outputs.GetTargetGroupHealthCheckResult:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaMultiValueHeadersEnabled")
    def lambda_multi_value_headers_enabled(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancerArns")
    def load_balancer_arns(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancingAlgorithmType")
    def load_balancing_algorithm_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancingAnomalyMitigation")
    def load_balancing_anomaly_mitigation(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loadBalancingCrossZoneEnabled")
    def load_balancing_cross_zone_enabled(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveClientIp")
    def preserve_client_ip(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="proxyProtocolV2")
    def proxy_protocol_v2(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="slowStart")
    def slow_start(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter
    def stickiness(self) -> outputs.GetTargetGroupStickinessResult:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetControlPort")
    def target_control_port(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        ...
    


class AwaitableGetTargetGroupResult(GetTargetGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetTargetGroupResult]:
        ...
    


def get_target_group(arn: Optional[_builtins.str] = ..., load_balancing_anomaly_mitigation: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTargetGroupResult:
    
    ...

def get_target_group_output(arn: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., load_balancing_anomaly_mitigation: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTargetGroupResult]:
    
    ...

