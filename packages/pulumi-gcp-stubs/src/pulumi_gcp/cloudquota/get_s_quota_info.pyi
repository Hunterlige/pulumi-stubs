

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetSQuotaInfoResult', 'AwaitableGetSQuotaInfoResult', 'get_s_quota_info', 'get_s_quota_info_output']
@pulumi.output_type
class GetSQuotaInfoResult:
    
    def __init__(__self__, container_type=..., dimensions=..., dimensions_infos=..., id=..., is_concurrent=..., is_fixed=..., is_precise=..., metric=..., metric_display_name=..., metric_unit=..., name=..., parent=..., quota_display_name=..., quota_id=..., quota_increase_eligibilities=..., refresh_interval=..., service=..., service_request_quota_uri=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerType")
    def container_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dimensionsInfos")
    def dimensions_infos(self) -> Sequence[outputs.GetSQuotaInfoDimensionsInfoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isConcurrent")
    def is_concurrent(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isFixed")
    def is_fixed(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isPrecise")
    def is_precise(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricDisplayName")
    def metric_display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricUnit")
    def metric_unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaDisplayName")
    def quota_display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="quotaIncreaseEligibilities")
    def quota_increase_eligibilities(self) -> Sequence[outputs.GetSQuotaInfoQuotaIncreaseEligibilityResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="refreshInterval")
    def refresh_interval(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceRequestQuotaUri")
    def service_request_quota_uri(self) -> _builtins.str:
        
        ...
    


class AwaitableGetSQuotaInfoResult(GetSQuotaInfoResult):
    def __await__(self): # -> Generator[Never, Any, GetSQuotaInfoResult]:
        ...
    


def get_s_quota_info(parent: Optional[_builtins.str] = ..., quota_id: Optional[_builtins.str] = ..., service: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetSQuotaInfoResult:
    
    ...

def get_s_quota_info_output(parent: Optional[pulumi.Input[_builtins.str]] = ..., quota_id: Optional[pulumi.Input[_builtins.str]] = ..., service: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetSQuotaInfoResult]:
    
    ...

