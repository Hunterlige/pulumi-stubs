

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOriginGroupResult', 'AwaitableGetOriginGroupResult', 'get_origin_group', 'get_origin_group_output']
@pulumi.output_type
class GetOriginGroupResult:
    
    def __init__(__self__, azure_api_version=..., health_probe_settings=..., id=..., name=..., origins=..., provisioning_state=..., resource_state=..., response_based_origin_error_detection_settings=..., system_data=..., traffic_restoration_time_to_healed_or_new_endpoints_in_minutes=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional[outputs.HealthProbeParametersResponse]:
        
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
    def origins(self) -> Optional[Sequence[outputs.ResourceReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseBasedOriginErrorDetectionSettings")
    def response_based_origin_error_detection_settings(self) -> Optional[outputs.ResponseBasedOriginErrorDetectionParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name=...)
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetOriginGroupResult(GetOriginGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetOriginGroupResult]:
        ...
    


def get_origin_group(endpoint_name: Optional[_builtins.str] = ..., origin_group_name: Optional[_builtins.str] = ..., profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOriginGroupResult:
    
    ...

def get_origin_group_output(endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., origin_group_name: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOriginGroupResult]:
    
    ...

