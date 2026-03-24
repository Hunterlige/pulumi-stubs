

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['QueueArgs', 'Queue']
@pulumi.input_type
class QueueArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], app_engine_routing_override: Optional[pulumi.Input[QueueAppEngineRoutingOverrideArgs]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., http_target: Optional[pulumi.Input[QueueHttpTargetArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rate_limits: Optional[pulumi.Input[QueueRateLimitsArgs]] = ..., retry_config: Optional[pulumi.Input[QueueRetryConfigArgs]] = ..., stackdriver_logging_config: Optional[pulumi.Input[QueueStackdriverLoggingConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appEngineRoutingOverride")
    def app_engine_routing_override(self) -> Optional[pulumi.Input[QueueAppEngineRoutingOverrideArgs]]:
        
        ...
    
    @app_engine_routing_override.setter
    def app_engine_routing_override(self, value: Optional[pulumi.Input[QueueAppEngineRoutingOverrideArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> Optional[pulumi.Input[QueueHttpTargetArgs]]:
        
        ...
    
    @http_target.setter
    def http_target(self, value: Optional[pulumi.Input[QueueHttpTargetArgs]]): # -> None:
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
    @pulumi.getter(name="rateLimits")
    def rate_limits(self) -> Optional[pulumi.Input[QueueRateLimitsArgs]]:
        
        ...
    
    @rate_limits.setter
    def rate_limits(self, value: Optional[pulumi.Input[QueueRateLimitsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> Optional[pulumi.Input[QueueRetryConfigArgs]]:
        
        ...
    
    @retry_config.setter
    def retry_config(self, value: Optional[pulumi.Input[QueueRetryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackdriverLoggingConfig")
    def stackdriver_logging_config(self) -> Optional[pulumi.Input[QueueStackdriverLoggingConfigArgs]]:
        
        ...
    
    @stackdriver_logging_config.setter
    def stackdriver_logging_config(self, value: Optional[pulumi.Input[QueueStackdriverLoggingConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _QueueState:
    def __init__(__self__, *, app_engine_routing_override: Optional[pulumi.Input[QueueAppEngineRoutingOverrideArgs]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., http_target: Optional[pulumi.Input[QueueHttpTargetArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rate_limits: Optional[pulumi.Input[QueueRateLimitsArgs]] = ..., retry_config: Optional[pulumi.Input[QueueRetryConfigArgs]] = ..., stackdriver_logging_config: Optional[pulumi.Input[QueueStackdriverLoggingConfigArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appEngineRoutingOverride")
    def app_engine_routing_override(self) -> Optional[pulumi.Input[QueueAppEngineRoutingOverrideArgs]]:
        
        ...
    
    @app_engine_routing_override.setter
    def app_engine_routing_override(self, value: Optional[pulumi.Input[QueueAppEngineRoutingOverrideArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> Optional[pulumi.Input[QueueHttpTargetArgs]]:
        
        ...
    
    @http_target.setter
    def http_target(self, value: Optional[pulumi.Input[QueueHttpTargetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="rateLimits")
    def rate_limits(self) -> Optional[pulumi.Input[QueueRateLimitsArgs]]:
        
        ...
    
    @rate_limits.setter
    def rate_limits(self, value: Optional[pulumi.Input[QueueRateLimitsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> Optional[pulumi.Input[QueueRetryConfigArgs]]:
        
        ...
    
    @retry_config.setter
    def retry_config(self, value: Optional[pulumi.Input[QueueRetryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackdriverLoggingConfig")
    def stackdriver_logging_config(self) -> Optional[pulumi.Input[QueueStackdriverLoggingConfigArgs]]:
        
        ...
    
    @stackdriver_logging_config.setter
    def stackdriver_logging_config(self, value: Optional[pulumi.Input[QueueStackdriverLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:cloudtasks/queue:Queue")
class Queue(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., app_engine_routing_override: Optional[pulumi.Input[Union[QueueAppEngineRoutingOverrideArgs, QueueAppEngineRoutingOverrideArgsDict]]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., http_target: Optional[pulumi.Input[Union[QueueHttpTargetArgs, QueueHttpTargetArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rate_limits: Optional[pulumi.Input[Union[QueueRateLimitsArgs, QueueRateLimitsArgsDict]]] = ..., retry_config: Optional[pulumi.Input[Union[QueueRetryConfigArgs, QueueRetryConfigArgsDict]]] = ..., stackdriver_logging_config: Optional[pulumi.Input[Union[QueueStackdriverLoggingConfigArgs, QueueStackdriverLoggingConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: QueueArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app_engine_routing_override: Optional[pulumi.Input[Union[QueueAppEngineRoutingOverrideArgs, QueueAppEngineRoutingOverrideArgsDict]]] = ..., desired_state: Optional[pulumi.Input[_builtins.str]] = ..., http_target: Optional[pulumi.Input[Union[QueueHttpTargetArgs, QueueHttpTargetArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., rate_limits: Optional[pulumi.Input[Union[QueueRateLimitsArgs, QueueRateLimitsArgsDict]]] = ..., retry_config: Optional[pulumi.Input[Union[QueueRetryConfigArgs, QueueRetryConfigArgsDict]]] = ..., stackdriver_logging_config: Optional[pulumi.Input[Union[QueueStackdriverLoggingConfigArgs, QueueStackdriverLoggingConfigArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> Queue:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appEngineRoutingOverride")
    def app_engine_routing_override(self) -> pulumi.Output[Optional[outputs.QueueAppEngineRoutingOverride]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpTarget")
    def http_target(self) -> pulumi.Output[Optional[outputs.QueueHttpTarget]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="rateLimits")
    def rate_limits(self) -> pulumi.Output[outputs.QueueRateLimits]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryConfig")
    def retry_config(self) -> pulumi.Output[outputs.QueueRetryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stackdriverLoggingConfig")
    def stackdriver_logging_config(self) -> pulumi.Output[Optional[outputs.QueueStackdriverLoggingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


