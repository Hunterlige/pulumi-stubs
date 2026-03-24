

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
__all__ = ['AnalysisArgs', 'Analysis']
@pulumi.input_type
class AnalysisArgs:
    def __init__(__self__, *, analysis_id: pulumi.Input[_builtins.str], aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[AnalysisParametersArgs]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[AnalysisPermissionArgs]]]] = ..., recovery_window_in_days: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_entity: Optional[pulumi.Input[AnalysisSourceEntityArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., theme_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisId")
    def analysis_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @analysis_id.setter
    def analysis_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[AnalysisParametersArgs]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[AnalysisParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AnalysisPermissionArgs]]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AnalysisPermissionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryWindowInDays")
    def recovery_window_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @recovery_window_in_days.setter
    def recovery_window_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEntity")
    def source_entity(self) -> Optional[pulumi.Input[AnalysisSourceEntityArgs]]:
        
        ...
    
    @source_entity.setter
    def source_entity(self, value: Optional[pulumi.Input[AnalysisSourceEntityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="themeArn")
    def theme_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @theme_arn.setter
    def theme_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AnalysisState:
    def __init__(__self__, *, analysis_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., last_published_time: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_time: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[AnalysisParametersArgs]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[AnalysisPermissionArgs]]]] = ..., recovery_window_in_days: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_entity: Optional[pulumi.Input[AnalysisSourceEntityArgs]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., theme_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisId")
    def analysis_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @analysis_id.setter
    def analysis_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPublishedTime")
    def last_published_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @last_published_time.setter
    def last_published_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_updated_time.setter
    def last_updated_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[AnalysisParametersArgs]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[AnalysisParametersArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AnalysisPermissionArgs]]]]:
        
        ...
    
    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AnalysisPermissionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryWindowInDays")
    def recovery_window_in_days(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @recovery_window_in_days.setter
    def recovery_window_in_days(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEntity")
    def source_entity(self) -> Optional[pulumi.Input[AnalysisSourceEntityArgs]]:
        
        ...
    
    @source_entity.setter
    def source_entity(self, value: Optional[pulumi.Input[AnalysisSourceEntityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="themeArn")
    def theme_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @theme_arn.setter
    def theme_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:quicksight/analysis:Analysis")
class Analysis(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., analysis_id: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Union[AnalysisParametersArgs, AnalysisParametersArgsDict]]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AnalysisPermissionArgs, AnalysisPermissionArgsDict]]]]] = ..., recovery_window_in_days: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_entity: Optional[pulumi.Input[Union[AnalysisSourceEntityArgs, AnalysisSourceEntityArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., theme_arn: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AnalysisArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., analysis_id: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., last_published_time: Optional[pulumi.Input[_builtins.str]] = ..., last_updated_time: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., parameters: Optional[pulumi.Input[Union[AnalysisParametersArgs, AnalysisParametersArgsDict]]] = ..., permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AnalysisPermissionArgs, AnalysisPermissionArgsDict]]]]] = ..., recovery_window_in_days: Optional[pulumi.Input[_builtins.int]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., source_entity: Optional[pulumi.Input[Union[AnalysisSourceEntityArgs, AnalysisSourceEntityArgsDict]]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., theme_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> Analysis:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="analysisId")
    def analysis_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastPublishedTime")
    def last_published_time(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[outputs.AnalysisParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence[outputs.AnalysisPermission]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recoveryWindowInDays")
    def recovery_window_in_days(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEntity")
    def source_entity(self) -> pulumi.Output[Optional[outputs.AnalysisSourceEntity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="themeArn")
    def theme_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


