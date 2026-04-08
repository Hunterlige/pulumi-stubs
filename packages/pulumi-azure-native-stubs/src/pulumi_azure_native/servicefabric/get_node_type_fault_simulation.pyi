import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNodeTypeFaultSimulationResult",
    "AwaitableGetNodeTypeFaultSimulationResult",
    "get_node_type_fault_simulation",
    "get_node_type_fault_simulation_output",
]

@pulumi.output_type
class GetNodeTypeFaultSimulationResult:
    def __init__(
        __self__,
        details=...,
        end_time=...,
        simulation_id=...,
        start_time=...,
        status=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[outputs.FaultSimulationDetailsResponse]: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="simulationId")
    def simulation_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

class AwaitableGetNodeTypeFaultSimulationResult(GetNodeTypeFaultSimulationResult):
    def __await__(self): ...

def get_node_type_fault_simulation(
    cluster_name: Optional[_builtins.str] = ...,
    node_type_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    simulation_id: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNodeTypeFaultSimulationResult: ...
def get_node_type_fault_simulation_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    node_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    simulation_id: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNodeTypeFaultSimulationResult]: ...
