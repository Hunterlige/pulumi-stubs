

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
__all__ = ['WorkloadNetworkSegmentArgs', 'WorkloadNetworkSegment']
@pulumi.input_type
class WorkloadNetworkSegmentArgs:
    def __init__(__self__, *, private_cloud_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], connected_gateway: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., revision: Optional[pulumi.Input[_builtins.float]] = ..., segment_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet: Optional[pulumi.Input[WorkloadNetworkSegmentSubnetArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedGateway")
    def connected_gateway(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connected_gateway.setter
    def connected_gateway(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentId")
    def segment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @segment_id.setter
    def segment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input[WorkloadNetworkSegmentSubnetArgs]]:
        
        ...
    
    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input[WorkloadNetworkSegmentSubnetArgs]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:avs:WorkloadNetworkSegment")
class WorkloadNetworkSegment(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., connected_gateway: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., private_cloud_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., revision: Optional[pulumi.Input[_builtins.float]] = ..., segment_id: Optional[pulumi.Input[_builtins.str]] = ..., subnet: Optional[pulumi.Input[Union[WorkloadNetworkSegmentSubnetArgs, WorkloadNetworkSegmentSubnetArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: WorkloadNetworkSegmentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> WorkloadNetworkSegment:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedGateway")
    def connected_gateway(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portVif")
    def port_vif(self) -> pulumi.Output[Sequence[outputs.WorkloadNetworkSegmentPortVifResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional[outputs.WorkloadNetworkSegmentSubnetResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


