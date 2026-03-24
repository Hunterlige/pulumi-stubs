

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LoadBalancerAccessLogsArgs', 'LoadBalancerAccessLogsArgsDict', 'LoadBalancerHealthCheckArgs', 'LoadBalancerHealthCheckArgsDict', 'LoadBalancerListenerArgs', 'LoadBalancerListenerArgsDict', 'LoadBalancerPolicyPolicyAttributeArgs', 'LoadBalancerPolicyPolicyAttributeArgsDict', 'SslNegotiationPolicyAttributeArgs', 'SslNegotiationPolicyAttributeArgsDict']
class LoadBalancerAccessLogsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    bucket_prefix: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    interval: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class LoadBalancerAccessLogsArgs:
    def __init__(__self__, *, bucket: pulumi.Input[_builtins.str], bucket_prefix: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., interval: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class LoadBalancerHealthCheckArgsDict(TypedDict):
    healthy_threshold: pulumi.Input[_builtins.int]
    interval: pulumi.Input[_builtins.int]
    target: pulumi.Input[_builtins.str]
    timeout: pulumi.Input[_builtins.int]
    unhealthy_threshold: pulumi.Input[_builtins.int]


@pulumi.input_type
class LoadBalancerHealthCheckArgs:
    def __init__(__self__, *, healthy_threshold: pulumi.Input[_builtins.int], interval: pulumi.Input[_builtins.int], target: pulumi.Input[_builtins.str], timeout: pulumi.Input[_builtins.int], unhealthy_threshold: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthyThreshold")
    def healthy_threshold(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @healthy_threshold.setter
    def healthy_threshold(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @timeout.setter
    def timeout(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unhealthyThreshold")
    def unhealthy_threshold(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class LoadBalancerListenerArgsDict(TypedDict):
    instance_port: pulumi.Input[_builtins.int]
    instance_protocol: pulumi.Input[_builtins.str]
    lb_port: pulumi.Input[_builtins.int]
    lb_protocol: pulumi.Input[_builtins.str]
    ssl_certificate_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LoadBalancerListenerArgs:
    def __init__(__self__, *, instance_port: pulumi.Input[_builtins.int], instance_protocol: pulumi.Input[_builtins.str], lb_port: pulumi.Input[_builtins.int], lb_protocol: pulumi.Input[_builtins.str], ssl_certificate_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePort")
    def instance_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @instance_port.setter
    def instance_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceProtocol")
    def instance_protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_protocol.setter
    def instance_protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @lb_port.setter
    def lb_port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lbProtocol")
    def lb_protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lb_protocol.setter
    def lb_protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertificateId")
    def ssl_certificate_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssl_certificate_id.setter
    def ssl_certificate_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class LoadBalancerPolicyPolicyAttributeArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class LoadBalancerPolicyPolicyAttributeArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
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
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SslNegotiationPolicyAttributeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class SslNegotiationPolicyAttributeArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


