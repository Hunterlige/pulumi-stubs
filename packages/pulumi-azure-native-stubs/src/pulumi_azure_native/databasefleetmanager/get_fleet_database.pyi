

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFleetDatabaseResult', 'AwaitableGetFleetDatabaseResult', 'get_fleet_database', 'get_fleet_database_output']
@pulumi.output_type
class GetFleetDatabaseResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
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
    @pulumi.getter
    def properties(self) -> outputs.FleetDatabasePropertiesResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetFleetDatabaseResult(GetFleetDatabaseResult):
    def __await__(self): # -> Generator[Never, Any, GetFleetDatabaseResult]:
        ...
    


def get_fleet_database(database_name: Optional[_builtins.str] = ..., fleet_name: Optional[_builtins.str] = ..., fleetspace_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFleetDatabaseResult:
    
    ...

def get_fleet_database_output(database_name: Optional[pulumi.Input[_builtins.str]] = ..., fleet_name: Optional[pulumi.Input[_builtins.str]] = ..., fleetspace_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFleetDatabaseResult]:
    
    ...

