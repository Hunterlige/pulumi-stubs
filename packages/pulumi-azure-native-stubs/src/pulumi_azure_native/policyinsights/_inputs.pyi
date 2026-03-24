

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AttestationEvidenceArgs', 'AttestationEvidenceArgsDict', 'RemediationFiltersArgs', 'RemediationFiltersArgsDict', 'RemediationPropertiesFailureThresholdArgs', 'RemediationPropertiesFailureThresholdArgsDict']
class AttestationEvidenceArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    source_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AttestationEvidenceArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., source_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_uri.setter
    def source_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RemediationFiltersArgsDict(TypedDict):
    
    locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    resource_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class RemediationFiltersArgs:
    def __init__(__self__, *, locations: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIds")
    def resource_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_ids.setter
    def resource_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class RemediationPropertiesFailureThresholdArgsDict(TypedDict):
    
    percentage: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class RemediationPropertiesFailureThresholdArgs:
    def __init__(__self__, *, percentage: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


