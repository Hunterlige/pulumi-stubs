

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetNetworkInsightsAnalysisResult', 'AwaitableGetNetworkInsightsAnalysisResult', 'get_network_insights_analysis', 'get_network_insights_analysis_output']
@pulumi.output_type
class GetNetworkInsightsAnalysisResult:
    
    def __init__(__self__, alternate_path_hints=..., arn=..., explanations=..., filter_in_arns=..., filters=..., forward_path_components=..., id=..., network_insights_analysis_id=..., network_insights_path_id=..., path_found=..., region=..., return_path_components=..., start_date=..., status=..., status_message=..., tags=..., warning_message=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternatePathHints")
    def alternate_path_hints(self) -> Sequence[outputs.GetNetworkInsightsAnalysisAlternatePathHintResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def explanations(self) -> Sequence[outputs.GetNetworkInsightsAnalysisExplanationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterInArns")
    def filter_in_arns(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Optional[Sequence[outputs.GetNetworkInsightsAnalysisFilterResult]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardPathComponents")
    def forward_path_components(self) -> Sequence[outputs.GetNetworkInsightsAnalysisForwardPathComponentResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInsightsAnalysisId")
    def network_insights_analysis_id(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInsightsPathId")
    def network_insights_path_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathFound")
    def path_found(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPathComponents")
    def return_path_components(self) -> Sequence[outputs.GetNetworkInsightsAnalysisReturnPathComponentResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warningMessage")
    def warning_message(self) -> _builtins.str:
        
        ...
    


class AwaitableGetNetworkInsightsAnalysisResult(GetNetworkInsightsAnalysisResult):
    def __await__(self): # -> Generator[Never, Any, GetNetworkInsightsAnalysisResult]:
        ...
    


def get_network_insights_analysis(filters: Optional[Sequence[Union[GetNetworkInsightsAnalysisFilterArgs, GetNetworkInsightsAnalysisFilterArgsDict]]] = ..., network_insights_analysis_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., tags: Optional[Mapping[str, _builtins.str]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetNetworkInsightsAnalysisResult:
    
    ...

def get_network_insights_analysis_output(filters: Optional[pulumi.Input[Optional[Sequence[Union[GetNetworkInsightsAnalysisFilterArgs, GetNetworkInsightsAnalysisFilterArgsDict]]]]] = ..., network_insights_analysis_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetNetworkInsightsAnalysisResult]:
    
    ...

