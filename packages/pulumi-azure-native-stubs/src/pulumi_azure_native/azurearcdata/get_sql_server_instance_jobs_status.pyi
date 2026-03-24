

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSqlServerInstanceJobsStatusResult', 'AwaitableGetSqlServerInstanceJobsStatusResult', 'get_sql_server_instance_jobs_status', 'get_sql_server_instance_jobs_status_output']
@pulumi.output_type
class GetSqlServerInstanceJobsStatusResult:
    
    def __init__(__self__, jobs_status=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobsStatus")
    def jobs_status(self) -> Optional[Sequence[outputs.SqlServerInstanceJobStatusResponse]]:
        
        ...
    


class AwaitableGetSqlServerInstanceJobsStatusResult(GetSqlServerInstanceJobsStatusResult):
    def __await__(self): # -> Generator[Never, Any, GetSqlServerInstanceJobsStatusResult]:
        ...
    


def get_sql_server_instance_jobs_status(feature_name: Optional[_builtins.str] = ..., job_type: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., sql_server_instance_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSqlServerInstanceJobsStatusResult:
    
    ...

def get_sql_server_instance_jobs_status_output(feature_name: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., job_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., sql_server_instance_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSqlServerInstanceJobsStatusResult]:
    
    ...

