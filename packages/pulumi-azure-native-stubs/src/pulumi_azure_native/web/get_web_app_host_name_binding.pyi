

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppHostNameBindingResult', 'AwaitableGetWebAppHostNameBindingResult', 'get_web_app_host_name_binding', 'get_web_app_host_name_binding_output']
@pulumi.output_type
class GetWebAppHostNameBindingResult:
    
    def __init__(__self__, azure_api_version=..., azure_resource_name=..., azure_resource_type=..., custom_host_name_dns_record_type=..., domain_id=..., host_name_type=..., id=..., kind=..., name=..., site_name=..., ssl_state=..., thumbprint=..., type=..., virtual_ip=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureResourceName")
    def azure_resource_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureResourceType")
    def azure_resource_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHostNameDnsRecordType")
    def custom_host_name_dns_record_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostNameType")
    def host_name_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslState")
    def ssl_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def thumbprint(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualIP")
    def virtual_ip(self) -> _builtins.str:
        
        ...
    


class AwaitableGetWebAppHostNameBindingResult(GetWebAppHostNameBindingResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppHostNameBindingResult]:
        ...
    


def get_web_app_host_name_binding(host_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppHostNameBindingResult:
    
    ...

def get_web_app_host_name_binding_output(host_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppHostNameBindingResult]:
    
    ...

