

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListEdgeSiteL2ConnectionsResult', 'AwaitableListEdgeSiteL2ConnectionsResult', 'list_edge_site_l2_connections', 'list_edge_site_l2_connections_output']
@pulumi.output_type
class ListEdgeSiteL2ConnectionsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.ResourceIdListResultResponseValue]]:
        
        ...
    


class AwaitableListEdgeSiteL2ConnectionsResult(ListEdgeSiteL2ConnectionsResult):
    def __await__(self): # -> Generator[Never, Any, ListEdgeSiteL2ConnectionsResult]:
        ...
    


def list_edge_site_l2_connections(edge_site_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListEdgeSiteL2ConnectionsResult:
    
    ...

def list_edge_site_l2_connections_output(edge_site_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListEdgeSiteL2ConnectionsResult]:
    
    ...

