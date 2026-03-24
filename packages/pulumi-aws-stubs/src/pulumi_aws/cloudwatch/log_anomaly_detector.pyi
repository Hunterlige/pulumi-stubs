

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['LogAnomalyDetectorArgs', 'LogAnomalyDetector']
@pulumi.input_type
class LogAnomalyDetectorArgs:
    def __init__(__self__, *, enabled: pulumi.Input[_builtins.bool], log_group_arn_lists: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], anomaly_visibility_time: Optional[pulumi.Input[_builtins.int]] = ..., detector_name: Optional[pulumi.Input[_builtins.str]] = ..., evaluation_frequency: Optional[pulumi.Input[_builtins.str]] = ..., filter_pattern: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]:
        ...
    
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArnLists")
    def log_group_arn_lists(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @log_group_arn_lists.setter
    def log_group_arn_lists(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="anomalyVisibilityTime")
    def anomaly_visibility_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @anomaly_visibility_time.setter
    def anomaly_visibility_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectorName")
    def detector_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @detector_name.setter
    def detector_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @evaluation_frequency.setter
    def evaluation_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_pattern.setter
    def filter_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    


@pulumi.input_type
class _LogAnomalyDetectorState:
    def __init__(__self__, *, anomaly_visibility_time: Optional[pulumi.Input[_builtins.int]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., detector_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., evaluation_frequency: Optional[pulumi.Input[_builtins.str]] = ..., filter_pattern: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., log_group_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anomalyVisibilityTime")
    def anomaly_visibility_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @anomaly_visibility_time.setter
    def anomaly_visibility_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectorName")
    def detector_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @detector_name.setter
    def detector_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @evaluation_frequency.setter
    def evaluation_frequency(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @filter_pattern.setter
    def filter_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArnLists")
    def log_group_arn_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @log_group_arn_lists.setter
    def log_group_arn_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token(...)
class LogAnomalyDetector(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., anomaly_visibility_time: Optional[pulumi.Input[_builtins.int]] = ..., detector_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., evaluation_frequency: Optional[pulumi.Input[_builtins.str]] = ..., filter_pattern: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., log_group_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: LogAnomalyDetectorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., anomaly_visibility_time: Optional[pulumi.Input[_builtins.int]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., detector_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., evaluation_frequency: Optional[pulumi.Input[_builtins.str]] = ..., filter_pattern: Optional[pulumi.Input[_builtins.str]] = ..., kms_key_id: Optional[pulumi.Input[_builtins.str]] = ..., log_group_arn_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> LogAnomalyDetector:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anomalyVisibilityTime")
    def anomaly_visibility_time(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectorName")
    def detector_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logGroupArnLists")
    def log_group_arn_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        ...
    


