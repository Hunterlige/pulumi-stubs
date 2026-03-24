

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., ..., ...]
@pulumi.output_type
class GetIspCacheNodesOperationCacheNodeMccIssueDetailsHistoryResult:
    
    def __init__(__self__, id=..., location=..., name=..., properties=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter
    def properties(self) -> outputs.MccCacheNodeIssueHistoryPropertiesResponse:
        
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
    


class AwaitableGetIspCacheNodesOperationCacheNodeMccIssueDetailsHistoryResult(GetIspCacheNodesOperationCacheNodeMccIssueDetailsHistoryResult):
    def __await__(self): # -> Generator[Never, Any, GetIspCacheNodesOperationCacheNodeMccIssueDetailsHistoryResult]:
        ...
    


def get_isp_cache_nodes_operation_cache_node_mcc_issue_details_history(cache_node_resource_name: Optional[_builtins.str] = ..., customer_resource_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetIspCacheNodesOperationCacheNodeMccIssueDetailsHistoryResult:
    
    ...

def get_isp_cache_nodes_operation_cache_node_mcc_issue_details_history_output(cache_node_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., customer_resource_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetIspCacheNodesOperationCacheNodeMccIssueDetailsHistoryResult]:
    
    ...

