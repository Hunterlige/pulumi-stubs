

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOnlineDeploymentLogsResult', 'AwaitableGetOnlineDeploymentLogsResult', 'get_online_deployment_logs', 'get_online_deployment_logs_output']
@pulumi.output_type
class GetOnlineDeploymentLogsResult:
    def __init__(__self__, content=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetOnlineDeploymentLogsResult(GetOnlineDeploymentLogsResult):
    def __await__(self): # -> Generator[Never, Any, GetOnlineDeploymentLogsResult]:
        ...
    


def get_online_deployment_logs(container_type: Optional[Union[_builtins.str, ContainerType]] = ..., deployment_name: Optional[_builtins.str] = ..., endpoint_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., tail: Optional[_builtins.int] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOnlineDeploymentLogsResult:
    
    ...

def get_online_deployment_logs_output(container_type: Optional[pulumi.Input[Optional[Union[_builtins.str, ContainerType]]]] = ..., deployment_name: Optional[pulumi.Input[_builtins.str]] = ..., endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., tail: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOnlineDeploymentLogsResult]:
    
    ...

