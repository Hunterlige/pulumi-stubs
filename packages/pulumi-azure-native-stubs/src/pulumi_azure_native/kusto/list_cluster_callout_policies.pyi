

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListClusterCalloutPoliciesResult', 'AwaitableListClusterCalloutPoliciesResult', 'list_cluster_callout_policies', 'list_cluster_callout_policies_output']
@pulumi.output_type
class ListClusterCalloutPoliciesResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.CalloutPolicyResponse]]:
        
        ...
    


class AwaitableListClusterCalloutPoliciesResult(ListClusterCalloutPoliciesResult):
    def __await__(self): # -> Generator[Never, Any, ListClusterCalloutPoliciesResult]:
        ...
    


def list_cluster_callout_policies(cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListClusterCalloutPoliciesResult:
    
    ...

def list_cluster_callout_policies_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListClusterCalloutPoliciesResult]:
    
    ...

