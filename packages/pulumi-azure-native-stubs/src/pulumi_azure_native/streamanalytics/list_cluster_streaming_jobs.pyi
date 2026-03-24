

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListClusterStreamingJobsResult', 'AwaitableListClusterStreamingJobsResult', 'list_cluster_streaming_jobs', 'list_cluster_streaming_jobs_output']
@pulumi.output_type
class ListClusterStreamingJobsResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Sequence[outputs.ClusterJobResponse]:
        
        ...
    


class AwaitableListClusterStreamingJobsResult(ListClusterStreamingJobsResult):
    def __await__(self): # -> Generator[Never, Any, ListClusterStreamingJobsResult]:
        ...
    


def list_cluster_streaming_jobs(cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListClusterStreamingJobsResult:
    
    ...

def list_cluster_streaming_jobs_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListClusterStreamingJobsResult]:
    
    ...

