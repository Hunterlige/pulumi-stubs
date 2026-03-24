

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkVirtualApplianceBootDiagnosticLogsResult', ..., 'get_network_virtual_appliance_boot_diagnostic_logs', ...]
@pulumi.output_type
class GetNetworkVirtualApplianceBootDiagnosticLogsResult:
    def __init__(__self__, instance_id=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[_builtins.int]:
        
        ...
    


class AwaitableGetNetworkVirtualApplianceBootDiagnosticLogsResult(GetNetworkVirtualApplianceBootDiagnosticLogsResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkVirtualApplianceBootDiagnosticLogsResult]:
        ...
    


def get_network_virtual_appliance_boot_diagnostic_logs(console_screenshot_storage_sas_url: Optional[_builtins.str] = ..., instance_id: Optional[_builtins.int] = ..., network_virtual_appliance_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., serial_console_storage_sas_url: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkVirtualApplianceBootDiagnosticLogsResult:
    
    ...

def get_network_virtual_appliance_boot_diagnostic_logs_output(console_screenshot_storage_sas_url: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., instance_id: Optional[pulumi.Input[Optional[_builtins.int]]] = ..., network_virtual_appliance_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., serial_console_storage_sas_url: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkVirtualApplianceBootDiagnosticLogsResult]:
    
    ...

