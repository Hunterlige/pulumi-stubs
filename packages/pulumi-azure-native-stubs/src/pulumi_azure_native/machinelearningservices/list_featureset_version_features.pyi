

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListFeaturesetVersionFeaturesResult', 'AwaitableListFeaturesetVersionFeaturesResult', 'list_featureset_version_features', 'list_featureset_version_features_output']
@pulumi.output_type
class ListFeaturesetVersionFeaturesResult:
    
    def __init__(__self__, next_link=..., value=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Sequence[outputs.FeatureResponse]]:
        
        ...
    


class AwaitableListFeaturesetVersionFeaturesResult(ListFeaturesetVersionFeaturesResult):
    def __await__(self): # -> Generator[Never, Any, ListFeaturesetVersionFeaturesResult]:
        ...
    


def list_featureset_version_features(name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., skip: Optional[_builtins.str] = ..., tags: Optional[_builtins.str] = ..., version: Optional[_builtins.str] = ..., workspace_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListFeaturesetVersionFeaturesResult:
    
    ...

def list_featureset_version_features_output(name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., skip: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., tags: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., workspace_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListFeaturesetVersionFeaturesResult]:
    
    ...

