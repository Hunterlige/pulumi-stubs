

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAFDOriginGroupResult', 'AwaitableGetAFDOriginGroupResult', 'get_afd_origin_group', 'get_afd_origin_group_output']
@pulumi.output_type
class GetAFDOriginGroupResult:
    
    def __init__(__self__, authentication=..., azure_api_version=..., deployment_status=..., health_probe_settings=..., id=..., load_balancing_settings=..., name=..., profile_name=..., provisioning_state=..., session_affinity_state=..., system_data=..., traffic_restoration_time_to_healed_or_new_endpoints_in_minutes=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[outputs.OriginAuthenticationPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> _builtins.str:
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
    @pulumi.getter(name="loadBalancingSettings")
    def load_balancing_settings(self) -> Optional[outputs.LoadBalancingSettingsParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAffinityState")
    def session_affinity_state(self) -> Optional[_builtins.str]:
        
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
    


class AwaitableGetAFDOriginGroupResult(GetAFDOriginGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetAFDOriginGroupResult]:
        ...
    


def get_afd_origin_group(origin_group_name: Optional[_builtins.str] = ..., profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAFDOriginGroupResult:
    
    ...

def get_afd_origin_group_output(origin_group_name: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAFDOriginGroupResult]:
    
    ...

