

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPatchBaselineResult', 'AwaitableGetPatchBaselineResult', 'get_patch_baseline', 'get_patch_baseline_output']
@pulumi.output_type
class GetPatchBaselineResult:
    
    def __init__(__self__, approval_rules=..., approved_patches=..., approved_patches_compliance_level=..., approved_patches_enable_non_security=..., available_security_updates_compliance_status=..., default_baseline=..., description=..., global_filters=..., id=..., json=..., name=..., name_prefix=..., operating_system=..., owner=..., region=..., rejected_patches=..., rejected_patches_action=..., sources=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvalRules")
    def approval_rules(self) -> Sequence[outputs.GetPatchBaselineApprovalRuleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvedPatches")
    def approved_patches(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvedPatchesComplianceLevel")
    def approved_patches_compliance_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="approvedPatchesEnableNonSecurity")
    def approved_patches_enable_non_security(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="availableSecurityUpdatesComplianceStatus")
    def available_security_updates_compliance_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBaseline")
    def default_baseline(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalFilters")
    def global_filters(self) -> Sequence[outputs.GetPatchBaselineGlobalFilterResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def owner(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rejectedPatches")
    def rejected_patches(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rejectedPatchesAction")
    def rejected_patches_action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Sequence[outputs.GetPatchBaselineSourceResult]:
        
        ...
    


class AwaitableGetPatchBaselineResult(GetPatchBaselineResult):
    def __await__(self): # -> Generator[Never, Any, GetPatchBaselineResult]:
        ...
    


def get_patch_baseline(default_baseline: Optional[_builtins.bool] = ..., name_prefix: Optional[_builtins.str] = ..., operating_system: Optional[_builtins.str] = ..., owner: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPatchBaselineResult:
    
    ...

def get_patch_baseline_output(default_baseline: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., name_prefix: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., operating_system: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., owner: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPatchBaselineResult]:
    
    ...

