

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MetricsDestinationArgs', 'MetricsDestination']
@pulumi.input_type
class MetricsDestinationArgs:
    def __init__(__self__, *, app_monitor_name: pulumi.Input[_builtins.str], destination: pulumi.Input[_builtins.str], destination_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appMonitorName")
    def app_monitor_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app_monitor_name.setter
    def app_monitor_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_arn.setter
    def destination_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _MetricsDestinationState:
    def __init__(__self__, *, app_monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., destination_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appMonitorName")
    def app_monitor_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app_monitor_name.setter
    def app_monitor_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination_arn.setter
    def destination_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:rum/metricsDestination:MetricsDestination")
class MetricsDestination(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., app_monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., destination_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: MetricsDestinationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., app_monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., destination_arn: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> MetricsDestination:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appMonitorName")
    def app_monitor_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationArn")
    def destination_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


