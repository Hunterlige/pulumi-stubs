

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CapacityReservationArgs', 'CapacityReservation']
@pulumi.input_type
class CapacityReservationArgs:
    def __init__(__self__, *, availability_zone: pulumi.Input[_builtins.str], instance_count: pulumi.Input[_builtins.int], instance_platform: pulumi.Input[Union[_builtins.str, InstancePlatform]], instance_type: pulumi.Input[Union[_builtins.str, InstanceType]], ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., end_date_type: Optional[pulumi.Input[_builtins.str]] = ..., ephemeral_storage: Optional[pulumi.Input[_builtins.bool]] = ..., instance_match_criteria: Optional[pulumi.Input[_builtins.str]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., placement_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePlatform")
    def instance_platform(self) -> pulumi.Input[Union[_builtins.str, InstancePlatform]]:
        
        ...
    
    @instance_platform.setter
    def instance_platform(self, value: pulumi.Input[Union[_builtins.str, InstancePlatform]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[Union[_builtins.str, InstanceType]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[Union[_builtins.str, InstanceType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDateType")
    def end_date_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_date_type.setter
    def end_date_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ephemeral_storage.setter
    def ephemeral_storage(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMatchCriteria")
    def instance_match_criteria(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_match_criteria.setter
    def instance_match_criteria(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroupArn")
    def placement_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_group_arn.setter
    def placement_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tenancy(self) -> Optional[pulumi.Input[Union[_builtins.str, Tenancy]]]:
        
        ...
    
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]]): # -> None:
        ...
    


@pulumi.input_type
class _CapacityReservationState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., end_date_type: Optional[pulumi.Input[_builtins.str]] = ..., ephemeral_storage: Optional[pulumi.Input[_builtins.bool]] = ..., instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_match_criteria: Optional[pulumi.Input[_builtins.str]] = ..., instance_platform: Optional[pulumi.Input[Union[_builtins.str, InstancePlatform]]] = ..., instance_type: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., placement_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ebs_optimized.setter
    def ebs_optimized(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDateType")
    def end_date_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_date_type.setter
    def end_date_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ephemeral_storage.setter
    def ephemeral_storage(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @instance_count.setter
    def instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMatchCriteria")
    def instance_match_criteria(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instance_match_criteria.setter
    def instance_match_criteria(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePlatform")
    def instance_platform(self) -> Optional[pulumi.Input[Union[_builtins.str, InstancePlatform]]]:
        
        ...
    
    @instance_platform.setter
    def instance_platform(self, value: Optional[pulumi.Input[Union[_builtins.str, InstancePlatform]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[Union[_builtins.str, InstanceType]]]:
        
        ...
    
    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @outpost_arn.setter
    def outpost_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @owner_id.setter
    def owner_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroupArn")
    def placement_group_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @placement_group_arn.setter
    def placement_group_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def tenancy(self) -> Optional[pulumi.Input[Union[_builtins.str, Tenancy]]]:
        
        ...
    
    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]]): # -> None:
        ...
    


@pulumi.type_token("aws:ec2/capacityReservation:CapacityReservation")
class CapacityReservation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., end_date_type: Optional[pulumi.Input[_builtins.str]] = ..., ephemeral_storage: Optional[pulumi.Input[_builtins.bool]] = ..., instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_match_criteria: Optional[pulumi.Input[_builtins.str]] = ..., instance_platform: Optional[pulumi.Input[Union[_builtins.str, InstancePlatform]]] = ..., instance_type: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., placement_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CapacityReservationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., availability_zone: Optional[pulumi.Input[_builtins.str]] = ..., ebs_optimized: Optional[pulumi.Input[_builtins.bool]] = ..., end_date: Optional[pulumi.Input[_builtins.str]] = ..., end_date_type: Optional[pulumi.Input[_builtins.str]] = ..., ephemeral_storage: Optional[pulumi.Input[_builtins.bool]] = ..., instance_count: Optional[pulumi.Input[_builtins.int]] = ..., instance_match_criteria: Optional[pulumi.Input[_builtins.str]] = ..., instance_platform: Optional[pulumi.Input[Union[_builtins.str, InstancePlatform]]] = ..., instance_type: Optional[pulumi.Input[Union[_builtins.str, InstanceType]]] = ..., outpost_arn: Optional[pulumi.Input[_builtins.str]] = ..., owner_id: Optional[pulumi.Input[_builtins.str]] = ..., placement_group_arn: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tenancy: Optional[pulumi.Input[Union[_builtins.str, Tenancy]]] = ...) -> CapacityReservation:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ebsOptimized")
    def ebs_optimized(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endDateType")
    def end_date_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceCount")
    def instance_count(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceMatchCriteria")
    def instance_match_criteria(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instancePlatform")
    def instance_platform(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="placementGroupArn")
    def placement_group_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def tenancy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


