

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetReportPlanResult', 'AwaitableGetReportPlanResult', 'get_report_plan', 'get_report_plan_output']
@pulumi.output_type
class GetReportPlanResult:
    
    def __init__(__self__, arn=..., creation_time=..., deployment_status=..., description=..., id=..., name=..., region=..., report_delivery_channels=..., report_settings=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
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
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportDeliveryChannels")
    def report_delivery_channels(self) -> Sequence[outputs.GetReportPlanReportDeliveryChannelResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportSettings")
    def report_settings(self) -> Sequence[outputs.GetReportPlanReportSettingResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


class AwaitableGetReportPlanResult(GetReportPlanResult):
    def __await__(self): # -> Generator[Never, Any, GetReportPlanResult]:
        ...
    


def get_report_plan(name: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetReportPlanResult:
    
    ...

def get_report_plan_output(name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetReportPlanResult]:
    
    ...

