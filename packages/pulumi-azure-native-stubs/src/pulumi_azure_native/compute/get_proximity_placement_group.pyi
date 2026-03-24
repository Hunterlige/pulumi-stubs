

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProximityPlacementGroupResult', 'AwaitableGetProximityPlacementGroupResult', 'get_proximity_placement_group', 'get_proximity_placement_group_output']
@pulumi.output_type
class GetProximityPlacementGroupResult:
    
    def __init__(__self__, availability_sets=..., azure_api_version=..., colocation_status=..., id=..., intent=..., location=..., name=..., proximity_placement_group_type=..., system_data=..., tags=..., type=..., virtual_machine_scale_sets=..., virtual_machines=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="availabilitySets")
    def availability_sets(self) -> Sequence[outputs.SubResourceWithColocationStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="colocationStatus")
    def colocation_status(self) -> Optional[outputs.InstanceViewStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.ProximityPlacementGroupPropertiesIntentResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="proximityPlacementGroupType")
    def proximity_placement_group_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachineScaleSets")
    def virtual_machine_scale_sets(self) -> Sequence[outputs.SubResourceWithColocationStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(self) -> Sequence[outputs.SubResourceWithColocationStatusResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetProximityPlacementGroupResult(GetProximityPlacementGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetProximityPlacementGroupResult]:
        ...
    


def get_proximity_placement_group(include_colocation_status: Optional[_builtins.str] = ..., proximity_placement_group_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProximityPlacementGroupResult:
    
    ...

def get_proximity_placement_group_output(include_colocation_status: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., proximity_placement_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProximityPlacementGroupResult]:
    
    ...

