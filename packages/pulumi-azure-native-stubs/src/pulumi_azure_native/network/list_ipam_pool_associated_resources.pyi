

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListIpamPoolAssociatedResourcesResult', 'AwaitableListIpamPoolAssociatedResourcesResult', 'list_ipam_pool_associated_resources', 'list_ipam_pool_associated_resources_output']
@pulumi.output_type
class ListIpamPoolAssociatedResourcesResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.PoolAssociationResponse]]:
        ...
    


class AwaitableListIpamPoolAssociatedResourcesResult(ListIpamPoolAssociatedResourcesResult):
    def __await__(self): # -> Generator[Never, Any, ListIpamPoolAssociatedResourcesResult]:
        ...
    


def list_ipam_pool_associated_resources(network_manager_name: Optional[_builtins.str] = ..., pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListIpamPoolAssociatedResourcesResult:
    
    ...

def list_ipam_pool_associated_resources_output(network_manager_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListIpamPoolAssociatedResourcesResult]:
    
    ...

