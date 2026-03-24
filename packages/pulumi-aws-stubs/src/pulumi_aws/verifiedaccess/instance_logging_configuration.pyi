

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
__all__ = ['InstanceLoggingConfigurationArgs', 'InstanceLoggingConfiguration']
@pulumi.input_type
class InstanceLoggingConfigurationArgs:
    def __init__(__self__, *, access_logs: pulumi.Input[InstanceLoggingConfigurationAccessLogsArgs], verifiedaccess_instance_id: pulumi.Input[_builtins.str], region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> pulumi.Input[InstanceLoggingConfigurationAccessLogsArgs]:
        
        ...
    
    @access_logs.setter
    def access_logs(self, value: pulumi.Input[InstanceLoggingConfigurationAccessLogsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedaccessInstanceId")
    def verifiedaccess_instance_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @verifiedaccess_instance_id.setter
    def verifiedaccess_instance_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _InstanceLoggingConfigurationState:
    def __init__(__self__, *, access_logs: Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsArgs]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., verifiedaccess_instance_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsArgs]]:
        
        ...
    
    @access_logs.setter
    def access_logs(self, value: Optional[pulumi.Input[InstanceLoggingConfigurationAccessLogsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedaccessInstanceId")
    def verifiedaccess_instance_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @verifiedaccess_instance_id.setter
    def verifiedaccess_instance_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class InstanceLoggingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_logs: Optional[pulumi.Input[Union[InstanceLoggingConfigurationAccessLogsArgs, InstanceLoggingConfigurationAccessLogsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., verifiedaccess_instance_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: InstanceLoggingConfigurationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_logs: Optional[pulumi.Input[Union[InstanceLoggingConfigurationAccessLogsArgs, InstanceLoggingConfigurationAccessLogsArgsDict]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., verifiedaccess_instance_id: Optional[pulumi.Input[_builtins.str]] = ...) -> InstanceLoggingConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> pulumi.Output[outputs.InstanceLoggingConfigurationAccessLogs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedaccessInstanceId")
    def verifiedaccess_instance_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


