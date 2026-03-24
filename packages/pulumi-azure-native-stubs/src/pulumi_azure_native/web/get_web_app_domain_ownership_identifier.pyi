

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetWebAppDomainOwnershipIdentifierResult', 'AwaitableGetWebAppDomainOwnershipIdentifierResult', 'get_web_app_domain_ownership_identifier', 'get_web_app_domain_ownership_identifier_output']
@pulumi.output_type
class GetWebAppDomainOwnershipIdentifierResult:
    
    def __init__(__self__, azure_api_version=..., id=..., kind=..., name=..., type=..., value=...) -> None:
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
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetWebAppDomainOwnershipIdentifierResult(GetWebAppDomainOwnershipIdentifierResult):
    def __await__(self): # -> Generator[Never, Any, GetWebAppDomainOwnershipIdentifierResult]:
        ...
    


def get_web_app_domain_ownership_identifier(domain_ownership_identifier_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetWebAppDomainOwnershipIdentifierResult:
    
    ...

def get_web_app_domain_ownership_identifier_output(domain_ownership_identifier_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetWebAppDomainOwnershipIdentifierResult]:
    
    ...

