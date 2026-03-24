

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListMonitorMonitoredResourcesResult', 'AwaitableListMonitorMonitoredResourcesResult', 'list_monitor_monitored_resources', 'list_monitor_monitored_resources_output']
@pulumi.output_type
class ListMonitorMonitoredResourcesResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.MonitoredResourceResponse]]:
        
        ...
    


class AwaitableListMonitorMonitoredResourcesResult(ListMonitorMonitoredResourcesResult):
    def __await__(self): # -> Generator[Never, Any, ListMonitorMonitoredResourcesResult]:
        ...
    


def list_monitor_monitored_resources(monitor_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListMonitorMonitoredResourcesResult:
    
    ...

def list_monitor_monitored_resources_output(monitor_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListMonitorMonitoredResourcesResult]:
    
    ...

