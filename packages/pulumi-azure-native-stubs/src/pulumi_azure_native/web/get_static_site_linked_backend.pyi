

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetStaticSiteLinkedBackendResult', 'AwaitableGetStaticSiteLinkedBackendResult', 'get_static_site_linked_backend', 'get_static_site_linked_backend_output']
@pulumi.output_type
class GetStaticSiteLinkedBackendResult:
    
    def __init__(__self__, azure_api_version=..., backend_resource_id=..., created_on=..., id=..., kind=..., name=..., provisioning_state=..., region=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="backendResourceId")
    def backend_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> _builtins.str:
        
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetStaticSiteLinkedBackendResult(GetStaticSiteLinkedBackendResult):
    def __await__(self): # -> Generator[Never, Any, GetStaticSiteLinkedBackendResult]:
        ...
    


def get_static_site_linked_backend(linked_backend_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetStaticSiteLinkedBackendResult:
    
    ...

def get_static_site_linked_backend_output(linked_backend_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetStaticSiteLinkedBackendResult]:
    
    ...

