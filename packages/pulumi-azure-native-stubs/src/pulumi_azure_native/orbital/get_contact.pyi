

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetContactResult', 'AwaitableGetContactResult', 'get_contact', 'get_contact_output']
@pulumi.output_type
class GetContactResult:
    
    def __init__(__self__, antenna_configuration=..., azure_api_version=..., contact_profile=..., end_azimuth_degrees=..., end_elevation_degrees=..., error_message=..., ground_station_name=..., id=..., maximum_elevation_degrees=..., name=..., reservation_end_time=..., reservation_start_time=..., rx_end_time=..., rx_start_time=..., start_azimuth_degrees=..., start_elevation_degrees=..., status=..., system_data=..., tx_end_time=..., tx_start_time=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="antennaConfiguration")
    def antenna_configuration(self) -> outputs.ContactsPropertiesResponseAntennaConfiguration:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactProfile")
    def contact_profile(self) -> outputs.ContactsPropertiesResponseContactProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAzimuthDegrees")
    def end_azimuth_degrees(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endElevationDegrees")
    def end_elevation_degrees(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groundStationName")
    def ground_station_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumElevationDegrees")
    def maximum_elevation_degrees(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationEndTime")
    def reservation_end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reservationStartTime")
    def reservation_start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rxEndTime")
    def rx_end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rxStartTime")
    def rx_start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAzimuthDegrees")
    def start_azimuth_degrees(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startElevationDegrees")
    def start_elevation_degrees(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="txEndTime")
    def tx_end_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="txStartTime")
    def tx_start_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetContactResult(GetContactResult):
    def __await__(self): # -> Generator[Never, Any, GetContactResult]:
        ...
    


def get_contact(contact_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., spacecraft_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetContactResult:
    
    ...

def get_contact_output(contact_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., spacecraft_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetContactResult]:
    
    ...

