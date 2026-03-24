

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetQuicksightAnalysisResult', 'AwaitableGetQuicksightAnalysisResult', 'get_quicksight_analysis', 'get_quicksight_analysis_output']
@pulumi.output_type
class GetQuicksightAnalysisResult:
    
    def __init__(__self__, analysis_id=..., arn=..., aws_account_id=..., created_time=..., id=..., last_published_time=..., last_updated_time=..., name=..., permissions=..., region=..., status=..., tags=..., theme_arn=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisId")
    def analysis_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPublishedTime")
    def last_published_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[outputs.GetQuicksightAnalysisPermissionResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="themeArn")
    def theme_arn(self) -> _builtins.str:
        ...
    


class AwaitableGetQuicksightAnalysisResult(GetQuicksightAnalysisResult):
    def __await__(self): # -> Generator[Never, Any, GetQuicksightAnalysisResult]:
        ...
    


def get_quicksight_analysis(analysis_id: Optional[_builtins.str] = ..., aws_account_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetQuicksightAnalysisResult:
    
    ...

def get_quicksight_analysis_output(analysis_id: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetQuicksightAnalysisResult]:
    
    ...

