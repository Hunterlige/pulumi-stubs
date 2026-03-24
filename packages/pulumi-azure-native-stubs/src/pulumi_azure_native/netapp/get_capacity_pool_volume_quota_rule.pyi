

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetCapacityPoolVolumeQuotaRuleResult', 'AwaitableGetCapacityPoolVolumeQuotaRuleResult', 'get_capacity_pool_volume_quota_rule', 'get_capacity_pool_volume_quota_rule_output']
@pulumi.output_type
class GetCapacityPoolVolumeQuotaRuleResult:
    
    def __init__(__self__, azure_api_version=..., id=..., location=..., name=..., provisioning_state=..., quota_size_in_ki_bs=..., quota_target=..., quota_type=..., system_data=..., tags=..., type=...) -> None:
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
    def location(self) -> _builtins.str:
        
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
    @pulumi.getter(name="quotaSizeInKiBs")
    def quota_size_in_ki_bs(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaTarget")
    def quota_target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaType")
    def quota_type(self) -> Optional[_builtins.str]:
        
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
    


class AwaitableGetCapacityPoolVolumeQuotaRuleResult(GetCapacityPoolVolumeQuotaRuleResult):
    def __await__(self): # -> Generator[Never, Any, GetCapacityPoolVolumeQuotaRuleResult]:
        ...
    


def get_capacity_pool_volume_quota_rule(account_name: Optional[_builtins.str] = ..., pool_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., volume_name: Optional[_builtins.str] = ..., volume_quota_rule_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetCapacityPoolVolumeQuotaRuleResult:
    
    ...

def get_capacity_pool_volume_quota_rule_output(account_name: Optional[pulumi.Input[_builtins.str]] = ..., pool_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_name: Optional[pulumi.Input[_builtins.str]] = ..., volume_quota_rule_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetCapacityPoolVolumeQuotaRuleResult]:
    
    ...

