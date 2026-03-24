

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetOriginResult', 'AwaitableGetOriginResult', 'get_origin', 'get_origin_output']
@pulumi.output_type
class GetOriginResult:
    
    def __init__(__self__, azure_api_version=..., enabled=..., host_name=..., http_port=..., https_port=..., id=..., name=..., origin_host_header=..., priority=..., private_endpoint_status=..., private_link_alias=..., private_link_approval_message=..., private_link_location=..., private_link_resource_id=..., provisioning_state=..., resource_state=..., system_data=..., type=..., weight=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostName")
    def host_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> Optional[_builtins.int]:
        
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
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateEndpointStatus")
    def private_endpoint_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[_builtins.str]:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> Optional[_builtins.int]:
        
        ...
    


class AwaitableGetOriginResult(GetOriginResult):
    def __await__(self): # -> Generator[Never, Any, GetOriginResult]:
        ...
    


def get_origin(endpoint_name: Optional[_builtins.str] = ..., origin_name: Optional[_builtins.str] = ..., profile_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetOriginResult:
    
    ...

def get_origin_output(endpoint_name: Optional[pulumi.Input[_builtins.str]] = ..., origin_name: Optional[pulumi.Input[_builtins.str]] = ..., profile_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetOriginResult]:
    
    ...

