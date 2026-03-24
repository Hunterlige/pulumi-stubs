

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['FleetArgs', 'Fleet']
@pulumi.input_type
class FleetArgs:
    def __init__(__self__, *, compute_capacity: pulumi.Input[FleetComputeCapacityArgs], instance_type: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ..., disconnect_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_join_info: Optional[pulumi.Input[FleetDomainJoinInfoArgs]] = ..., enable_default_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., fleet_type: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., idle_disconnect_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., max_sessions_per_instance: Optional[pulumi.Input[_builtins.int]] = ..., max_user_duration_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stream_view: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[FleetVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCapacity")
    def compute_capacity(self) -> pulumi.Input[FleetComputeCapacityArgs]:
        
        ...
    
    @compute_capacity.setter
    def compute_capacity(self, value: pulumi.Input[FleetComputeCapacityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disconnectTimeoutInSeconds")
    def disconnect_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disconnect_timeout_in_seconds.setter
    def disconnect_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainJoinInfo")
    def domain_join_info(self) -> Optional[pulumi.Input[FleetDomainJoinInfoArgs]]:
        
        ...
    
    @domain_join_info.setter
    def domain_join_info(self, value: Optional[pulumi.Input[FleetDomainJoinInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_default_internet_access.setter
    def enable_default_internet_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fleet_type.setter
    def fleet_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleDisconnectTimeoutInSeconds")
    def idle_disconnect_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_disconnect_timeout_in_seconds.setter
    def idle_disconnect_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_arn.setter
    def image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSessionsPerInstance")
    def max_sessions_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_sessions_per_instance.setter
    def max_sessions_per_instance(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUserDurationInSeconds")
    def max_user_duration_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_user_duration_in_seconds.setter
    def max_user_duration_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamView")
    def stream_view(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stream_view.setter
    def stream_view(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[FleetVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[FleetVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _FleetState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., compute_capacity: Optional[pulumi.Input[FleetComputeCapacityArgs]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disconnect_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_join_info: Optional[pulumi.Input[FleetDomainJoinInfoArgs]] = ..., enable_default_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., fleet_type: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., idle_disconnect_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., max_sessions_per_instance: Optional[pulumi.Input[_builtins.int]] = ..., max_user_duration_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., stream_view: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[FleetVpcConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCapacity")
    def compute_capacity(self) -> Optional[pulumi.Input[FleetComputeCapacityArgs]]:
        
        ...
    
    @compute_capacity.setter
    def compute_capacity(self, value: Optional[pulumi.Input[FleetComputeCapacityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disconnectTimeoutInSeconds")
    def disconnect_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @disconnect_timeout_in_seconds.setter
    def disconnect_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainJoinInfo")
    def domain_join_info(self) -> Optional[pulumi.Input[FleetDomainJoinInfoArgs]]:
        
        ...
    
    @domain_join_info.setter
    def domain_join_info(self, value: Optional[pulumi.Input[FleetDomainJoinInfoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_default_internet_access.setter
    def enable_default_internet_access(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fleet_type.setter
    def fleet_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleDisconnectTimeoutInSeconds")
    def idle_disconnect_timeout_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_disconnect_timeout_in_seconds.setter
    def idle_disconnect_timeout_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_arn.setter
    def image_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSessionsPerInstance")
    def max_sessions_per_instance(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_sessions_per_instance.setter
    def max_sessions_per_instance(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUserDurationInSeconds")
    def max_user_duration_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_user_duration_in_seconds.setter
    def max_user_duration_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamView")
    def stream_view(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @stream_view.setter
    def stream_view(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input[FleetVpcConfigArgs]]:
        
        ...
    
    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input[FleetVpcConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:appstream/fleet:Fleet")
class Fleet(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., compute_capacity: Optional[pulumi.Input[Union[FleetComputeCapacityArgs, FleetComputeCapacityArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disconnect_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_join_info: Optional[pulumi.Input[Union[FleetDomainJoinInfoArgs, FleetDomainJoinInfoArgsDict]]] = ..., enable_default_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., fleet_type: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., idle_disconnect_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., max_sessions_per_instance: Optional[pulumi.Input[_builtins.int]] = ..., max_user_duration_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., stream_view: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[Union[FleetVpcConfigArgs, FleetVpcConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: FleetArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., compute_capacity: Optional[pulumi.Input[Union[FleetComputeCapacityArgs, FleetComputeCapacityArgsDict]]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., disconnect_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., domain_join_info: Optional[pulumi.Input[Union[FleetDomainJoinInfoArgs, FleetDomainJoinInfoArgsDict]]] = ..., enable_default_internet_access: Optional[pulumi.Input[_builtins.bool]] = ..., fleet_type: Optional[pulumi.Input[_builtins.str]] = ..., iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., idle_disconnect_timeout_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., image_arn: Optional[pulumi.Input[_builtins.str]] = ..., image_name: Optional[pulumi.Input[_builtins.str]] = ..., instance_type: Optional[pulumi.Input[_builtins.str]] = ..., max_sessions_per_instance: Optional[pulumi.Input[_builtins.int]] = ..., max_user_duration_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ..., stream_view: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., vpc_config: Optional[pulumi.Input[Union[FleetVpcConfigArgs, FleetVpcConfigArgsDict]]] = ...) -> Fleet:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCapacity")
    def compute_capacity(self) -> pulumi.Output[outputs.FleetComputeCapacity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disconnectTimeoutInSeconds")
    def disconnect_timeout_in_seconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainJoinInfo")
    def domain_join_info(self) -> pulumi.Output[outputs.FleetDomainJoinInfo]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultInternetAccess")
    def enable_default_internet_access(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetType")
    def fleet_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleDisconnectTimeoutInSeconds")
    def idle_disconnect_timeout_in_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxSessionsPerInstance")
    def max_sessions_per_instance(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxUserDurationInSeconds")
    def max_user_duration_in_seconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamView")
    def stream_view(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[outputs.FleetVpcConfig]:
        
        ...
    


