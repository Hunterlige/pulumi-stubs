

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetDeviceResult', 'AwaitableGetDeviceResult', 'get_device', 'get_device_output']
@pulumi.output_type
class GetDeviceResult:
    
    def __init__(__self__, arn=..., aws_locations=..., description=..., device_id=..., global_network_id=..., id=..., locations=..., model=..., serial_number=..., site_id=..., tags=..., type=..., vendor=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsLocations")
    def aws_locations(self) -> Sequence[outputs.GetDeviceAwsLocationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Sequence[outputs.GetDeviceLocationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteId")
    def site_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vendor(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDeviceResult(GetDeviceResult):
    def __await__(self): # -> Generator[Never, Any, GetDeviceResult]:
        ...
    


def get_device(device_id: Optional[_builtins.str] = ..., global_network_id: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDeviceResult:
    
    ...

def get_device_output(device_id: Optional[pulumi.Input[_builtins.str]] = ..., global_network_id: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDeviceResult]:
    
    ...

