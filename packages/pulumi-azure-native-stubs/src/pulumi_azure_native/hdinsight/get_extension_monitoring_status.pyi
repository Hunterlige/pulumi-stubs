

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetExtensionMonitoringStatusResult', 'AwaitableGetExtensionMonitoringStatusResult', 'get_extension_monitoring_status', 'get_extension_monitoring_status_output']
@pulumi.output_type
class GetExtensionMonitoringStatusResult:
    
    def __init__(__self__, azure_api_version=..., cluster_monitoring_enabled=..., workspace_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterMonitoringEnabled")
    def cluster_monitoring_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetExtensionMonitoringStatusResult(GetExtensionMonitoringStatusResult):
    def __await__(self): # -> Generator[Never, Any, GetExtensionMonitoringStatusResult]:
        ...
    


def get_extension_monitoring_status(cluster_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetExtensionMonitoringStatusResult:
    
    ...

def get_extension_monitoring_status_output(cluster_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetExtensionMonitoringStatusResult]:
    
    ...

