

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
__all__ = ['AccessLevelConditionArgs', 'AccessLevelCondition']
@pulumi.input_type
class AccessLevelConditionArgs:
    def __init__(__self__, *, access_level: pulumi.Input[_builtins.str], device_policy: Optional[pulumi.Input[AccessLevelConditionDevicePolicyArgs]] = ..., ip_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate: Optional[pulumi.Input[_builtins.bool]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., required_access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_network_sources: Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelConditionVpcNetworkSourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @access_level.setter
    def access_level(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="devicePolicy")
    def device_policy(self) -> Optional[pulumi.Input[AccessLevelConditionDevicePolicyArgs]]:
        
        ...
    
    @device_policy.setter
    def device_policy(self, value: Optional[pulumi.Input[AccessLevelConditionDevicePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSubnetworks")
    def ip_subnetworks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_subnetworks.setter
    def ip_subnetworks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def negate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate.setter
    def negate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredAccessLevels")
    def required_access_levels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @required_access_levels.setter
    def required_access_levels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelConditionVpcNetworkSourceArgs]]]]:
        
        ...
    
    @vpc_network_sources.setter
    def vpc_network_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelConditionVpcNetworkSourceArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _AccessLevelConditionState:
    def __init__(__self__, *, access_level: Optional[pulumi.Input[_builtins.str]] = ..., access_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., device_policy: Optional[pulumi.Input[AccessLevelConditionDevicePolicyArgs]] = ..., ip_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate: Optional[pulumi.Input[_builtins.bool]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., required_access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_network_sources: Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelConditionVpcNetworkSourceArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_level.setter
    def access_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_policy_id.setter
    def access_policy_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="devicePolicy")
    def device_policy(self) -> Optional[pulumi.Input[AccessLevelConditionDevicePolicyArgs]]:
        
        ...
    
    @device_policy.setter
    def device_policy(self, value: Optional[pulumi.Input[AccessLevelConditionDevicePolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSubnetworks")
    def ip_subnetworks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @ip_subnetworks.setter
    def ip_subnetworks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def negate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate.setter
    def negate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredAccessLevels")
    def required_access_levels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @required_access_levels.setter
    def required_access_levels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelConditionVpcNetworkSourceArgs]]]]:
        
        ...
    
    @vpc_network_sources.setter
    def vpc_network_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessLevelConditionVpcNetworkSourceArgs]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AccessLevelCondition(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_level: Optional[pulumi.Input[_builtins.str]] = ..., device_policy: Optional[pulumi.Input[Union[AccessLevelConditionDevicePolicyArgs, AccessLevelConditionDevicePolicyArgsDict]]] = ..., ip_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate: Optional[pulumi.Input[_builtins.bool]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., required_access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_network_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AccessLevelConditionVpcNetworkSourceArgs, AccessLevelConditionVpcNetworkSourceArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccessLevelConditionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_level: Optional[pulumi.Input[_builtins.str]] = ..., access_policy_id: Optional[pulumi.Input[_builtins.str]] = ..., device_policy: Optional[pulumi.Input[Union[AccessLevelConditionDevicePolicyArgs, AccessLevelConditionDevicePolicyArgsDict]]] = ..., ip_subnetworks: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., members: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., negate: Optional[pulumi.Input[_builtins.bool]] = ..., regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., required_access_levels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vpc_network_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AccessLevelConditionVpcNetworkSourceArgs, AccessLevelConditionVpcNetworkSourceArgsDict]]]]] = ...) -> AccessLevelCondition:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessPolicyId")
    def access_policy_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="devicePolicy")
    def device_policy(self) -> pulumi.Output[Optional[outputs.AccessLevelConditionDevicePolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSubnetworks")
    def ip_subnetworks(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def negate(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredAccessLevels")
    def required_access_levels(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcNetworkSources")
    def vpc_network_sources(self) -> pulumi.Output[Optional[Sequence[outputs.AccessLevelConditionVpcNetworkSource]]]:
        
        ...
    


