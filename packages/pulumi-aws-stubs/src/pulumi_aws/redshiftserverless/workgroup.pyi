

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkgroupArgs', 'Workgroup']
@pulumi.input_type
class WorkgroupArgs:
    def __init__(__self__, *, namespace_name: pulumi.Input[_builtins.str], workgroup_name: pulumi.Input[_builtins.str], base_capacity: Optional[pulumi.Input[_builtins.int]] = ..., config_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupConfigParameterArgs]]]] = ..., enhanced_vpc_routing: Optional[pulumi.Input[_builtins.bool]] = ..., max_capacity: Optional[pulumi.Input[_builtins.int]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., price_performance_target: Optional[pulumi.Input[WorkgroupPricePerformanceTargetArgs]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., track_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @workgroup_name.setter
    def workgroup_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseCapacity")
    def base_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @base_capacity.setter
    def base_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configParameters")
    def config_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupConfigParameterArgs]]]]:
        
        ...
    
    @config_parameters.setter
    def config_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupConfigParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricePerformanceTarget")
    def price_performance_target(self) -> Optional[pulumi.Input[WorkgroupPricePerformanceTargetArgs]]:
        
        ...
    
    @price_performance_target.setter
    def price_performance_target(self, value: Optional[pulumi.Input[WorkgroupPricePerformanceTargetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackName")
    def track_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @track_name.setter
    def track_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _WorkgroupState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., base_capacity: Optional[pulumi.Input[_builtins.int]] = ..., config_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupConfigParameterArgs]]]] = ..., endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointArgs]]]] = ..., enhanced_vpc_routing: Optional[pulumi.Input[_builtins.bool]] = ..., max_capacity: Optional[pulumi.Input[_builtins.int]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., price_performance_target: Optional[pulumi.Input[WorkgroupPricePerformanceTargetArgs]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., track_name: Optional[pulumi.Input[_builtins.str]] = ..., workgroup_id: Optional[pulumi.Input[_builtins.str]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseCapacity")
    def base_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @base_capacity.setter
    def base_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="configParameters")
    def config_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupConfigParameterArgs]]]]:
        
        ...
    
    @config_parameters.setter
    def config_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupConfigParameterArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointArgs]]]]:
        
        ...
    
    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkgroupEndpointArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enhanced_vpc_routing.setter
    def enhanced_vpc_routing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_capacity.setter
    def max_capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricePerformanceTarget")
    def price_performance_target(self) -> Optional[pulumi.Input[WorkgroupPricePerformanceTargetArgs]]:
        
        ...
    
    @price_performance_target.setter
    def price_performance_target(self, value: Optional[pulumi.Input[WorkgroupPricePerformanceTargetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @publicly_accessible.setter
    def publicly_accessible(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="trackName")
    def track_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @track_name.setter
    def track_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupId")
    def workgroup_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workgroup_id.setter
    def workgroup_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @workgroup_name.setter
    def workgroup_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:redshiftserverless/workgroup:Workgroup")
class Workgroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., base_capacity: Optional[pulumi.Input[_builtins.int]] = ..., config_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkgroupConfigParameterArgs, WorkgroupConfigParameterArgsDict]]]]] = ..., enhanced_vpc_routing: Optional[pulumi.Input[_builtins.bool]] = ..., max_capacity: Optional[pulumi.Input[_builtins.int]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., price_performance_target: Optional[pulumi.Input[Union[WorkgroupPricePerformanceTargetArgs, WorkgroupPricePerformanceTargetArgsDict]]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., track_name: Optional[pulumi.Input[_builtins.str]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkgroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., base_capacity: Optional[pulumi.Input[_builtins.int]] = ..., config_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkgroupConfigParameterArgs, WorkgroupConfigParameterArgsDict]]]]] = ..., endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[WorkgroupEndpointArgs, WorkgroupEndpointArgsDict]]]]] = ..., enhanced_vpc_routing: Optional[pulumi.Input[_builtins.bool]] = ..., max_capacity: Optional[pulumi.Input[_builtins.int]] = ..., namespace_name: Optional[pulumi.Input[_builtins.str]] = ..., port: Optional[pulumi.Input[_builtins.int]] = ..., price_performance_target: Optional[pulumi.Input[Union[WorkgroupPricePerformanceTargetArgs, WorkgroupPricePerformanceTargetArgsDict]]] = ..., publicly_accessible: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., track_name: Optional[pulumi.Input[_builtins.str]] = ..., workgroup_id: Optional[pulumi.Input[_builtins.str]] = ..., workgroup_name: Optional[pulumi.Input[_builtins.str]] = ...) -> Workgroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baseCapacity")
    def base_capacity(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configParameters")
    def config_parameters(self) -> pulumi.Output[Sequence[outputs.WorkgroupConfigParameter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Sequence[outputs.WorkgroupEndpoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enhancedVpcRouting")
    def enhanced_vpc_routing(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCapacity")
    def max_capacity(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pricePerformanceTarget")
    def price_performance_target(self) -> pulumi.Output[outputs.WorkgroupPricePerformanceTarget]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
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
    @pulumi.getter(name="trackName")
    def track_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupId")
    def workgroup_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workgroupName")
    def workgroup_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


