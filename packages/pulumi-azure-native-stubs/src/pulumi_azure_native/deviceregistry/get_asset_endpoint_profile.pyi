

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAssetEndpointProfileResult', 'AwaitableGetAssetEndpointProfileResult', 'get_asset_endpoint_profile', 'get_asset_endpoint_profile_output']
@pulumi.output_type
class GetAssetEndpointProfileResult:
    
    def __init__(__self__, additional_configuration=..., authentication=..., azure_api_version=..., discovered_asset_endpoint_profile_ref=..., endpoint_profile_type=..., extended_location=..., id=..., location=..., name=..., provisioning_state=..., status=..., system_data=..., tags=..., target_address=..., type=..., uuid=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalConfiguration")
    def additional_configuration(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[outputs.AuthenticationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveredAssetEndpointProfileRef")
    def discovered_asset_endpoint_profile_ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointProfileType")
    def endpoint_profile_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> outputs.ExtendedLocationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> outputs.AssetEndpointProfileStatusResponse:
        
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
    @pulumi.getter(name="targetAddress")
    def target_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uuid(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAssetEndpointProfileResult(GetAssetEndpointProfileResult):
    def __await__(self): # -> Generator[Never, Any, GetAssetEndpointProfileResult]:
        ...
    


def get_asset_endpoint_profile(asset_endpoint_profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAssetEndpointProfileResult:
    
    ...

def get_asset_endpoint_profile_output(asset_endpoint_profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAssetEndpointProfileResult]:
    
    ...

