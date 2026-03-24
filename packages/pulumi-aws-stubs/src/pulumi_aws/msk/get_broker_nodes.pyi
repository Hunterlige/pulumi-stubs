import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetBrokerNodesResult",
    "AwaitableGetBrokerNodesResult",
    "get_broker_nodes",
    "get_broker_nodes_output",
]

@pulumi.output_type
class GetBrokerNodesResult:
    def __init__(
        __self__, cluster_arn=..., id=..., node_info_lists=..., region=...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="nodeInfoLists")
    def node_info_lists(self) -> Sequence[outputs.GetBrokerNodesNodeInfoListResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetBrokerNodesResult(GetBrokerNodesResult):
    def __await__(self): ...

def get_broker_nodes(
    cluster_arn: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetBrokerNodesResult: ...
def get_broker_nodes_output(
    cluster_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetBrokerNodesResult]: ...
