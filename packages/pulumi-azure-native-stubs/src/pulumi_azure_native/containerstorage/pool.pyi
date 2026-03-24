

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PoolArgs', 'Pool']
@pulumi.input_type
class PoolArgs:
    def __init__(__self__, *, pool_type: pulumi.Input[PoolTypeArgs], resource_group_name: pulumi.Input[_builtins.str], assignments: Optional[pulumi.Input[Sequence[pulumi.Input[AssignmentArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., reclaim_policy: Optional[pulumi.Input[Union[_builtins.str, ReclaimPolicy]]] = ..., resources: Optional[pulumi.Input[ResourcesArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Zone]]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolType")
    def pool_type(self) -> pulumi.Input[PoolTypeArgs]:
        
        ...
    
    @pool_type.setter
    def pool_type(self, value: pulumi.Input[PoolTypeArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def assignments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssignmentArgs]]]]:
        
        ...
    
    @assignments.setter
    def assignments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AssignmentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reclaimPolicy")
    def reclaim_policy(self) -> Optional[pulumi.Input[Union[_builtins.str, ReclaimPolicy]]]:
        
        ...
    
    @reclaim_policy.setter
    def reclaim_policy(self, value: Optional[pulumi.Input[Union[_builtins.str, ReclaimPolicy]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[ResourcesArgs]]:
        
        ...
    
    @resources.setter
    def resources(self, value: Optional[pulumi.Input[ResourcesArgs]]): # -> None:
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
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Zone]]]]]:
        
        ...
    
    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Zone]]]]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:containerstorage:Pool")
class Pool(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., assignments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AssignmentArgs, AssignmentArgsDict]]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_type: Optional[pulumi.Input[Union[PoolTypeArgs, PoolTypeArgsDict]]] = ..., reclaim_policy: Optional[pulumi.Input[Union[_builtins.str, ReclaimPolicy]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resources: Optional[pulumi.Input[Union[ResourcesArgs, ResourcesArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., zones: Optional[pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Zone]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PoolArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Pool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def assignments(self) -> pulumi.Output[Optional[Sequence[outputs.AssignmentResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="poolType")
    def pool_type(self) -> pulumi.Output[outputs.PoolTypeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reclaimPolicy")
    def reclaim_policy(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional[outputs.ResourcesResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.ResourceOperationalStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    


