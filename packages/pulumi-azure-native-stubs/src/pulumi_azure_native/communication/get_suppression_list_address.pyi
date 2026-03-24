

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSuppressionListAddressResult', 'AwaitableGetSuppressionListAddressResult', 'get_suppression_list_address', 'get_suppression_list_address_output']
@pulumi.output_type
class GetSuppressionListAddressResult:
    
    def __init__(__self__, azure_api_version=..., data_location=..., email=..., first_name=..., id=..., last_modified=..., last_name=..., name=..., notes=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def notes(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSuppressionListAddressResult(GetSuppressionListAddressResult):
    def __await__(self): # -> Generator[Never, Any, GetSuppressionListAddressResult]:
        ...
    


def get_suppression_list_address(address_id: Optional[_builtins.str] = ..., domain_name: Optional[_builtins.str] = ..., email_service_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., suppression_list_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSuppressionListAddressResult:
    
    ...

def get_suppression_list_address_output(address_id: Optional[pulumi.Input[_builtins.str]] = ..., domain_name: Optional[pulumi.Input[_builtins.str]] = ..., email_service_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., suppression_list_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSuppressionListAddressResult]:
    
    ...

