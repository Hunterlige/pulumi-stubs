

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStaticSiteCustomDomainResult', 'AwaitableGetStaticSiteCustomDomainResult', 'get_static_site_custom_domain', 'get_static_site_custom_domain_output']
@pulumi.output_type
class GetStaticSiteCustomDomainResult:
    
    def __init__(__self__, azure_api_version=..., created_on=..., domain_name=..., error_message=..., id=..., kind=..., name=..., status=..., type=..., validation_token=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> _builtins.str:
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
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationToken")
    def validation_token(self) -> _builtins.str:
        
        ...
    


class AwaitableGetStaticSiteCustomDomainResult(GetStaticSiteCustomDomainResult):
    def __await__(self): # -> Generator[Never, Any, GetStaticSiteCustomDomainResult]:
        ...
    


def get_static_site_custom_domain(domain_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStaticSiteCustomDomainResult:
    
    ...

def get_static_site_custom_domain_output(domain_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStaticSiteCustomDomainResult]:
    
    ...

