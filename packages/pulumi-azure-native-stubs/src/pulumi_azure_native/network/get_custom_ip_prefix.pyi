

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCustomIPPrefixResult', 'AwaitableGetCustomIPPrefixResult', 'get_custom_ip_prefix', 'get_custom_ip_prefix_output']
@pulumi.output_type
class GetCustomIPPrefixResult:
    
    def __init__(__self__, asn=..., authorization_message=..., azure_api_version=..., child_custom_ip_prefixes=..., cidr=..., commissioned_state=..., custom_ip_prefix_parent=..., etag=..., express_route_advertise=..., extended_location=..., failed_reason=..., geo=..., id=..., location=..., name=..., no_internet_advertise=..., prefix_type=..., provisioning_state=..., public_ip_prefixes=..., resource_guid=..., signed_message=..., tags=..., type=..., zones=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationMessage")
    def authorization_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childCustomIpPrefixes")
    def child_custom_ip_prefixes(self) -> Sequence[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commissionedState")
    def commissioned_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customIpPrefixParent")
    def custom_ip_prefix_parent(self) -> Optional[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressRouteAdvertise")
    def express_route_advertise(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[outputs.ExtendedLocationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failedReason")
    def failed_reason(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def geo(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noInternetAdvertise")
    def no_internet_advertise(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixType")
    def prefix_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicIpPrefixes")
    def public_ip_prefixes(self) -> Sequence[outputs.SubResourceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signedMessage")
    def signed_message(self) -> Optional[_builtins.str]:
        
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
    def zones(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


class AwaitableGetCustomIPPrefixResult(GetCustomIPPrefixResult):
    def __await__(self): # -> Generator[Never, Any, GetCustomIPPrefixResult]:
        ...
    


def get_custom_ip_prefix(custom_ip_prefix_name: Optional[_builtins.str] = ..., expand: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCustomIPPrefixResult:
    
    ...

def get_custom_ip_prefix_output(custom_ip_prefix_name: Optional[pulumi.Input[_builtins.str]] = ..., expand: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCustomIPPrefixResult]:
    
    ...

