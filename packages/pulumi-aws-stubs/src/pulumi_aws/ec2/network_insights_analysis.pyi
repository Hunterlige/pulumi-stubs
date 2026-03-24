

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['NetworkInsightsAnalysisArgs', 'NetworkInsightsAnalysis']
@pulumi.input_type
class NetworkInsightsAnalysisArgs:
    def __init__(__self__, *, network_insights_path_id: pulumi.Input[_builtins.str], filter_in_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., wait_for_completion: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInsightsPathId")
    def network_insights_path_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @network_insights_path_id.setter
    def network_insights_path_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterInArns")
    def filter_in_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @filter_in_arns.setter
    def filter_in_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForCompletion")
    def wait_for_completion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_completion.setter
    def wait_for_completion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _NetworkInsightsAnalysisState:
    def __init__(__self__, *, alternate_path_hints: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisAlternatePathHintArgs]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., explanations: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationArgs]]]] = ..., filter_in_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., forward_path_components: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentArgs]]]] = ..., network_insights_path_id: Optional[pulumi.Input[_builtins.str]] = ..., path_found: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., return_path_components: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentArgs]]]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_message: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., wait_for_completion: Optional[pulumi.Input[_builtins.bool]] = ..., warning_message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternatePathHints")
    def alternate_path_hints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisAlternatePathHintArgs]]]]:
        
        ...
    
    @alternate_path_hints.setter
    def alternate_path_hints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisAlternatePathHintArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def explanations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationArgs]]]]:
        
        ...
    
    @explanations.setter
    def explanations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisExplanationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterInArns")
    def filter_in_arns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @filter_in_arns.setter
    def filter_in_arns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardPathComponents")
    def forward_path_components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentArgs]]]]:
        
        ...
    
    @forward_path_components.setter
    def forward_path_components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisForwardPathComponentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInsightsPathId")
    def network_insights_path_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @network_insights_path_id.setter
    def network_insights_path_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathFound")
    def path_found(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @path_found.setter
    def path_found(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPathComponents")
    def return_path_components(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentArgs]]]]:
        
        ...
    
    @return_path_components.setter
    def return_path_components(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkInsightsAnalysisReturnPathComponentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status_message.setter
    def status_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForCompletion")
    def wait_for_completion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_completion.setter
    def wait_for_completion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warningMessage")
    def warning_message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @warning_message.setter
    def warning_message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class NetworkInsightsAnalysis(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., filter_in_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., network_insights_path_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., wait_for_completion: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: NetworkInsightsAnalysisArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., alternate_path_hints: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkInsightsAnalysisAlternatePathHintArgs, NetworkInsightsAnalysisAlternatePathHintArgsDict]]]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., explanations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkInsightsAnalysisExplanationArgs, NetworkInsightsAnalysisExplanationArgsDict]]]]] = ..., filter_in_arns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., forward_path_components: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkInsightsAnalysisForwardPathComponentArgs, NetworkInsightsAnalysisForwardPathComponentArgsDict]]]]] = ..., network_insights_path_id: Optional[pulumi.Input[_builtins.str]] = ..., path_found: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., return_path_components: Optional[pulumi.Input[Sequence[pulumi.Input[Union[NetworkInsightsAnalysisReturnPathComponentArgs, NetworkInsightsAnalysisReturnPathComponentArgsDict]]]]] = ..., start_date: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., status_message: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., wait_for_completion: Optional[pulumi.Input[_builtins.bool]] = ..., warning_message: Optional[pulumi.Input[_builtins.str]] = ...) -> NetworkInsightsAnalysis:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="alternatePathHints")
    def alternate_path_hints(self) -> pulumi.Output[Sequence[outputs.NetworkInsightsAnalysisAlternatePathHint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def explanations(self) -> pulumi.Output[Sequence[outputs.NetworkInsightsAnalysisExplanation]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterInArns")
    def filter_in_arns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardPathComponents")
    def forward_path_components(self) -> pulumi.Output[Sequence[outputs.NetworkInsightsAnalysisForwardPathComponent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkInsightsPathId")
    def network_insights_path_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pathFound")
    def path_found(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPathComponents")
    def return_path_components(self) -> pulumi.Output[Sequence[outputs.NetworkInsightsAnalysisReturnPathComponent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForCompletion")
    def wait_for_completion(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="warningMessage")
    def warning_message(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


