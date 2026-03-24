

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSupportPlanTypeResult', 'AwaitableGetSupportPlanTypeResult', 'get_support_plan_type', 'get_support_plan_type_output']
@pulumi.output_type
class GetSupportPlanTypeResult:
    
    def __init__(__self__, azure_api_version=..., id=..., name=..., provisioning_state=..., type=...) -> None:
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSupportPlanTypeResult(GetSupportPlanTypeResult):
    def __await__(self): # -> Generator[Never, Any, GetSupportPlanTypeResult]:
        ...
    


def get_support_plan_type(plan_type_name: Optional[_builtins.str] = ..., provider_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSupportPlanTypeResult:
    
    ...

def get_support_plan_type_output(plan_type_name: Optional[pulumi.Input[_builtins.str]] = ..., provider_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSupportPlanTypeResult]:
    
    ...

