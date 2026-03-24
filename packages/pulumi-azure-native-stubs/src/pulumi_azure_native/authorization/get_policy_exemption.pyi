

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPolicyExemptionResult', 'AwaitableGetPolicyExemptionResult', 'get_policy_exemption', 'get_policy_exemption_output']
@pulumi.output_type
class GetPolicyExemptionResult:
    
    def __init__(__self__, assignment_scope_validation=..., azure_api_version=..., description=..., display_name=..., exemption_category=..., expires_on=..., id=..., metadata=..., name=..., policy_assignment_id=..., policy_definition_reference_ids=..., resource_selectors=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assignmentScopeValidation")
    def assignment_scope_validation(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptionCategory")
    def exemption_category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceIds")
    def policy_definition_reference_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSelectors")
    def resource_selectors(self) -> Optional[Sequence[outputs.ResourceSelectorResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetPolicyExemptionResult(GetPolicyExemptionResult):
    def __await__(self): # -> Generator[Never, Any, GetPolicyExemptionResult]:
        ...
    


def get_policy_exemption(policy_exemption_name: Optional[_builtins.str] = ..., scope: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPolicyExemptionResult:
    
    ...

def get_policy_exemption_output(policy_exemption_name: Optional[pulumi.Input[_builtins.str]] = ..., scope: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPolicyExemptionResult]:
    
    ...

