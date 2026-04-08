import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ListNodeTypeFaultSimulationResult",
    "AwaitableListNodeTypeFaultSimulationResult",
    "list_node_type_fault_simulation",
    "list_node_type_fault_simulation_output",
]

@pulumi.output_type
class ListNodeTypeFaultSimulationResult:
    def __init__(__self__, next_link=..., value=...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.FaultSimulationResponse]: ...

class AwaitableListNodeTypeFaultSimulationResult(ListNodeTypeFaultSimulationResult):
    def __await__(self): ...

def list_node_type_fault_simulation(
    cluster_name: Optional[_builtins.str] = ...,
    node_type_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableListNodeTypeFaultSimulationResult: ...
def list_node_type_fault_simulation_output(
    cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
    node_type_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[ListNodeTypeFaultSimulationResult]: ...
