

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetTopicResult', 'AwaitableGetTopicResult', 'get_topic', 'get_topic_output']
@pulumi.output_type
class GetTopicResult:
    
    def __init__(__self__, effective_labels=..., id=..., ingestion_data_source_settings=..., kms_key_name=..., labels=..., message_retention_duration=..., message_storage_policies=..., message_transforms=..., name=..., project=..., pulumi_labels=..., schema_settings=..., tags=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ingestionDataSourceSettings")
    def ingestion_data_source_settings(self) -> Sequence[outputs.GetTopicIngestionDataSourceSettingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRetentionDuration")
    def message_retention_duration(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageStoragePolicies")
    def message_storage_policies(self) -> Sequence[outputs.GetTopicMessageStoragePolicyResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageTransforms")
    def message_transforms(self) -> Sequence[outputs.GetTopicMessageTransformResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaSettings")
    def schema_settings(self) -> Sequence[outputs.GetTopicSchemaSettingResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        ...
    


class AwaitableGetTopicResult(GetTopicResult):
    def __await__(self): # -> Generator[Never, Any, GetTopicResult]:
        ...
    


def get_topic(name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetTopicResult:
    
    ...

def get_topic_output(name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetTopicResult]:
    
    ...

