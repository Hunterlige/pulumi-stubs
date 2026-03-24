

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
    
    def __init__(__self__, azure_api_version=..., configured_role_types=..., culture=..., data_box_edge_device_status=..., data_residency=..., description=..., device_hcs_version=..., device_local_capacity=..., device_model=..., device_software_version=..., device_type=..., edge_profile=..., etag=..., friendly_name=..., id=..., identity=..., kind=..., kubernetes_workload_profile=..., location=..., model_description=..., name=..., node_count=..., resource_move_details=..., serial_number=..., sku=..., system_data=..., tags=..., time_zone=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configuredRoleTypes")
    def configured_role_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def culture(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataBoxEdgeDeviceStatus")
    def data_box_edge_device_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataResidency")
    def data_residency(self) -> Optional[outputs.DataResidencyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceHcsVersion")
    def device_hcs_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceLocalCapacity")
    def device_local_capacity(self) -> _builtins.float:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceModel")
    def device_model(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceSoftwareVersion")
    def device_software_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgeProfile")
    def edge_profile(self) -> outputs.EdgeProfileResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identity(self) -> Optional[outputs.ResourceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kubernetesWorkloadProfile")
    def kubernetes_workload_profile(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelDescription")
    def model_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceMoveDetails")
    def resource_move_details(self) -> outputs.ResourceMoveDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetDeviceResult(GetDeviceResult):
    def __await__(self): # -> Generator[Never, Any, GetDeviceResult]:
        ...
    


def get_device(device_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetDeviceResult:
    
    ...

def get_device_output(device_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetDeviceResult]:
    
    ...

