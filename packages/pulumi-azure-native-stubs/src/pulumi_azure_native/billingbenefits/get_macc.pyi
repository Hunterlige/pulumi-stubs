

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetMaccResult', 'AwaitableGetMaccResult', 'get_macc', 'get_macc_output']
@pulumi.output_type
class GetMaccResult:
    
    def __init__(__self__, allow_contributors=..., automatic_shortfall=..., automatic_shortfall_suppress_reason=..., azure_api_version=..., billing_account_resource_id=..., commitment=..., display_name=..., end_at=..., entity_type=..., etag=..., id=..., identity=..., kind=..., location=..., managed_by=..., milestones=..., name=..., plan=..., primary_billing_account_resource_id=..., primary_resource_id=..., product_code=..., provisioning_state=..., resource_id=..., shortfall=..., sku=..., start_at=..., status=..., system_data=..., system_id=..., tags=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowContributors")
    def allow_contributors(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticShortfall")
    def automatic_shortfall(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automaticShortfallSuppressReason")
    def automatic_shortfall_suppress_reason(self) -> Optional[outputs.AutomaticShortfallSuppressReasonResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingAccountResourceId")
    def billing_account_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commitment(self) -> Optional[outputs.CommitmentResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endAt")
    def end_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> _builtins.str:
        
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
    def identity(self) -> Optional[outputs.ManagedServiceIdentityResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def milestones(self) -> Optional[Sequence[outputs.MaccMilestoneResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[outputs.PlanResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryBillingAccountResourceId")
    def primary_billing_account_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryResourceId")
    def primary_resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shortfall(self) -> Optional[outputs.ShortfallResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sku(self) -> Optional[outputs.SkuResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startAt")
    def start_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemId")
    def system_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetMaccResult(GetMaccResult):
    def __await__(self): # -> Generator[Never, Any, GetMaccResult]:
        ...
    


def get_macc(macc_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetMaccResult:
    
    ...

def get_macc_output(macc_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetMaccResult]:
    
    ...

