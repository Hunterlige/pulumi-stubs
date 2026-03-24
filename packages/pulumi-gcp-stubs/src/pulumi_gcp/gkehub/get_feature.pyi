

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFeatureResult', 'AwaitableGetFeatureResult', 'get_feature', 'get_feature_output']
@pulumi.output_type
class GetFeatureResult:
    
    def __init__(__self__, create_time=..., delete_time=..., effective_labels=..., fleet_default_member_configs=..., id=..., labels=..., location=..., name=..., project=..., pulumi_labels=..., resource_states=..., specs=..., states=..., update_time=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fleetDefaultMemberConfigs")
    def fleet_default_member_configs(self) -> Sequence[outputs.GetFeatureFleetDefaultMemberConfigResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
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
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceStates")
    def resource_states(self) -> Sequence[outputs.GetFeatureResourceStateResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def specs(self) -> Sequence[outputs.GetFeatureSpecResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def states(self) -> Sequence[outputs.GetFeatureStateResult]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        ...
    


class AwaitableGetFeatureResult(GetFeatureResult):
    def __await__(self): # -> Generator[Never, Any, GetFeatureResult]:
        ...
    


def get_feature(location: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., project: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFeatureResult:
    
    ...

def get_feature_output(location: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFeatureResult]:
    
    ...

