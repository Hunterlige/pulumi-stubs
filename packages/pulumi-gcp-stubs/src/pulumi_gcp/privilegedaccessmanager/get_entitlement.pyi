

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetEntitlementResult', 'AwaitableGetEntitlementResult', 'get_entitlement', 'get_entitlement_output']
@pulumi.output_type
class GetEntitlementResult:
    
    def __init__(__self__, additional_notification_targets=..., approval_workflows=..., create_time=..., eligible_users=..., entitlement_id=..., etag=..., id=..., location=..., max_request_duration=..., name=..., parent=..., privileged_accesses=..., requester_justification_configs=..., state=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalNotificationTargets")
    def additional_notification_targets(self) -> Sequence[outputs.GetEntitlementAdditionalNotificationTargetResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalWorkflows")
    def approval_workflows(self) -> Sequence[outputs.GetEntitlementApprovalWorkflowResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eligibleUsers")
    def eligible_users(self) -> Sequence[outputs.GetEntitlementEligibleUserResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entitlementId")
    def entitlement_id(self) -> Optional[_builtins.str]:
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
    def location(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRequestDuration")
    def max_request_duration(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privilegedAccesses")
    def privileged_accesses(self) -> Sequence[outputs.GetEntitlementPrivilegedAccessResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requesterJustificationConfigs")
    def requester_justification_configs(self) -> Sequence[outputs.GetEntitlementRequesterJustificationConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetEntitlementResult(GetEntitlementResult):
    def __await__(self): # -> Generator[Never, Any, GetEntitlementResult]:
        ...
    


def get_entitlement(entitlement_id: Optional[_builtins.str] = ..., location: Optional[_builtins.str] = ..., parent: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetEntitlementResult:
    
    ...

def get_entitlement_output(entitlement_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., location: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., parent: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetEntitlementResult]:
    
    ...

