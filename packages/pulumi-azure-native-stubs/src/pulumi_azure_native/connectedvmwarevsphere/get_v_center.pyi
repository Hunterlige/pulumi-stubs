

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetVCenterResult', 'AwaitableGetVCenterResult', 'get_v_center', 'get_v_center_output']
@pulumi.output_type
class GetVCenterResult:
    
    def __init__(__self__, azure_api_version=..., connection_status=..., credentials=..., custom_resource_name=..., extended_location=..., fqdn=..., id=..., instance_uuid=..., kind=..., location=..., name=..., port=..., provisioning_state=..., statuses=..., system_data=..., tags=..., type=..., uuid=..., version=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[outputs.VICredentialResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fqdn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceUuid")
    def instance_uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> Sequence[outputs.ResourceStatusResponse]:
        
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
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


class AwaitableGetVCenterResult(GetVCenterResult):
    def __await__(self): # -> Generator[Never, Any, GetVCenterResult]:
        ...
    


def get_v_center(resource_group_name: Optional[_builtins.str] = ..., vcenter_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetVCenterResult:
    
    ...

def get_v_center_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., vcenter_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetVCenterResult]:
    
    ...

