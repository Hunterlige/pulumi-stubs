import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDbNodesResult",
    "AwaitableGetDbNodesResult",
    "get_db_nodes",
    "get_db_nodes_output",
]

@pulumi.output_type
class GetDbNodesResult:
    def __init__(
        __self__, cloud_vm_cluster_id=..., db_nodes=..., id=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudVmClusterId")
    def cloud_vm_cluster_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dbNodes")
    def db_nodes(self) -> Sequence[outputs.GetDbNodesDbNodeResult]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetDbNodesResult(GetDbNodesResult):
    def __await__(self): ...

def get_db_nodes(
    cloud_vm_cluster_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetDbNodesResult: ...
def get_db_nodes_output(
    cloud_vm_cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDbNodesResult]: ...
