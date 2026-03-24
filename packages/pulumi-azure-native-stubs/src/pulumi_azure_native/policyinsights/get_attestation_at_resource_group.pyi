

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetAttestationAtResourceGroupResult', 'AwaitableGetAttestationAtResourceGroupResult', 'get_attestation_at_resource_group', 'get_attestation_at_resource_group_output']
@pulumi.output_type
class GetAttestationAtResourceGroupResult:
    
    def __init__(__self__, assessment_date=..., azure_api_version=..., comments=..., compliance_state=..., evidence=..., expires_on=..., id=..., last_compliance_state_change_at=..., metadata=..., name=..., owner=..., policy_assignment_id=..., policy_definition_reference_id=..., provisioning_state=..., system_data=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assessmentDate")
    def assessment_date(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comments(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceState")
    def compliance_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def evidence(self) -> Optional[Sequence[outputs.AttestationEvidenceResponse]]:
        
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
    @pulumi.getter(name="lastComplianceStateChangeAt")
    def last_compliance_state_change_at(self) -> _builtins.str:
        
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
    @pulumi.getter
    def owner(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetAttestationAtResourceGroupResult(GetAttestationAtResourceGroupResult):
    def __await__(self): # -> Generator[Never, Any, GetAttestationAtResourceGroupResult]:
        ...
    


def get_attestation_at_resource_group(attestation_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetAttestationAtResourceGroupResult:
    
    ...

def get_attestation_at_resource_group_output(attestation_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetAttestationAtResourceGroupResult]:
    
    ...

