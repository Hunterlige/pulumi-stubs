

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPacketCaptureResult', 'AwaitableGetPacketCaptureResult', 'get_packet_capture', 'get_packet_capture_output']
@pulumi.output_type
class GetPacketCaptureResult:
    
    def __init__(__self__, azure_api_version=..., bytes_to_capture_per_packet=..., capture_settings=..., continuous_capture=..., etag=..., filters=..., id=..., name=..., provisioning_state=..., scope=..., storage_location=..., target=..., target_type=..., time_limit_in_seconds=..., total_bytes_per_session=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bytesToCapturePerPacket")
    def bytes_to_capture_per_packet(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="captureSettings")
    def capture_settings(self) -> Optional[outputs.PacketCaptureSettingsResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continuousCapture")
    def continuous_capture(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.PacketCaptureFilterResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.PacketCaptureMachineScopeResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> outputs.PacketCaptureStorageLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeLimitInSeconds")
    def time_limit_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="totalBytesPerSession")
    def total_bytes_per_session(self) -> Optional[_builtins.float]:
        
        ...
    


class AwaitableGetPacketCaptureResult(GetPacketCaptureResult):
    def __await__(self): # -> Generator[Never, Any, GetPacketCaptureResult]:
        ...
    


def get_packet_capture(network_watcher_name: Optional[_builtins.str] = ..., packet_capture_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPacketCaptureResult:
    
    ...

def get_packet_capture_output(network_watcher_name: Optional[pulumi.Input[_builtins.str]] = ..., packet_capture_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPacketCaptureResult]:
    
    ...

