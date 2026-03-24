

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAksAssessmentOperationResult', 'AwaitableGetAksAssessmentOperationResult', 'get_aks_assessment_operation', 'get_aks_assessment_operation_output']
@pulumi.output_type
class GetAksAssessmentOperationResult:
    
    def __init__(__self__, azure_api_version=..., details=..., e_tag=..., id=..., name=..., provisioning_state=..., scope=..., settings=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> outputs.AKSAssessmentDetailsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> _builtins.str:
        
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
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[outputs.AssessmentScopeParametersResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> outputs.AKSAssessmentSettingsResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAksAssessmentOperationResult(GetAksAssessmentOperationResult):
    def __await__(self): # -> Generator[Never, Any, GetAksAssessmentOperationResult]:
        ...
    


def get_aks_assessment_operation(assessment_name: Optional[_builtins.str] = ..., project_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAksAssessmentOperationResult:
    
    ...

def get_aks_assessment_operation_output(assessment_name: Optional[pulumi.Input[_builtins.str]] = ..., project_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAksAssessmentOperationResult]:
    
    ...

