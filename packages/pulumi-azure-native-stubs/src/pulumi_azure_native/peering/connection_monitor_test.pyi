

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConnectionMonitorTestArgs', 'ConnectionMonitorTest']
@pulumi.input_type
class ConnectionMonitorTestArgs:
    def __init__(__self__, *, peering_service_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], connection_monitor_test_name: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., destination_port: Optional[pulumi.Input[_builtins.int]] = ..., source_agent: Optional[pulumi.Input[_builtins.str]] = ..., test_frequency_in_sec: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="peeringServiceName")
    def peering_service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @peering_service_name.setter
    def peering_service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionMonitorTestName")
    def connection_monitor_test_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_monitor_test_name.setter
    def connection_monitor_test_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAgent")
    def source_agent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_agent.setter
    def source_agent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFrequencyInSec")
    def test_frequency_in_sec(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @test_frequency_in_sec.setter
    def test_frequency_in_sec(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:peering:ConnectionMonitorTest")
class ConnectionMonitorTest(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connection_monitor_test_name: Optional[pulumi.Input[_builtins.str]] = ..., destination: Optional[pulumi.Input[_builtins.str]] = ..., destination_port: Optional[pulumi.Input[_builtins.int]] = ..., peering_service_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., source_agent: Optional[pulumi.Input[_builtins.str]] = ..., test_frequency_in_sec: Optional[pulumi.Input[_builtins.int]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConnectionMonitorTestArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> ConnectionMonitorTest:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTestSuccessful")
    def is_test_successful(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceAgent")
    def source_agent(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="testFrequencyInSec")
    def test_frequency_in_sec(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


