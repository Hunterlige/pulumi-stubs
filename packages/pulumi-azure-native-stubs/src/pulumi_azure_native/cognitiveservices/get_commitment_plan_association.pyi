

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCommitmentPlanAssociationResult', 'AwaitableGetCommitmentPlanAssociationResult', 'get_commitment_plan_association', 'get_commitment_plan_association_output']
@pulumi.output_type
class GetCommitmentPlanAssociationResult:
    
    def __init__(__self__, account_id=..., azure_api_version=..., etag=..., id=..., name=..., system_data=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetCommitmentPlanAssociationResult(GetCommitmentPlanAssociationResult):
    def __await__(self): # -> Generator[Never, Any, GetCommitmentPlanAssociationResult]:
        ...
    


def get_commitment_plan_association(commitment_plan_association_name: Optional[_builtins.str] = ..., commitment_plan_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCommitmentPlanAssociationResult:
    
    ...

def get_commitment_plan_association_output(commitment_plan_association_name: Optional[pulumi.Input[_builtins.str]] = ..., commitment_plan_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCommitmentPlanAssociationResult]:
    
    ...

