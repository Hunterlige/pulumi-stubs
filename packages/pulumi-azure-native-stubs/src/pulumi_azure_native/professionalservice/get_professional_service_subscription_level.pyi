

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetProfessionalServiceSubscriptionLevelResult', ..., 'get_professional_service_subscription_level', 'get_professional_service_subscription_level_output']
@pulumi.output_type
class GetProfessionalServiceSubscriptionLevelResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., properties=..., tags=..., type=...) -> None:
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
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> outputs.ProfessionalServiceResourceResponseProperties:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetProfessionalServiceSubscriptionLevelResult(GetProfessionalServiceSubscriptionLevelResult):
    def __await__(self): # -> Generator[Never, Any, GetProfessionalServiceSubscriptionLevelResult]:
        ...
    


def get_professional_service_subscription_level(resource_group_name: Optional[_builtins.str] = ..., resource_name: Optional[_builtins.str] = ..., subscription_id: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetProfessionalServiceSubscriptionLevelResult:
    
    ...

def get_professional_service_subscription_level_output(resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_name: Optional[pulumi.Input[_builtins.str]] = ..., subscription_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetProfessionalServiceSubscriptionLevelResult]:
    
    ...

