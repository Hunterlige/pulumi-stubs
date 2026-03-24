

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetResourcesResult', 'AwaitableGetResourcesResult', 'get_resources', 'get_resources_output']
@pulumi.output_type
class GetResourcesResult:
    
    def __init__(__self__, exclude_compliant_resources=..., id=..., include_compliance_details=..., region=..., resource_arn_lists=..., resource_tag_mapping_lists=..., resource_type_filters=..., tag_filters=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeCompliantResources")
    def exclude_compliant_resources(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeComplianceDetails")
    def include_compliance_details(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArnLists")
    def resource_arn_lists(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagMappingLists")
    def resource_tag_mapping_lists(self) -> Sequence[outputs.GetResourcesResourceTagMappingListResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypeFilters")
    def resource_type_filters(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagFilters")
    def tag_filters(self) -> Optional[Sequence[outputs.GetResourcesTagFilterResult]]:
        ...
    


class AwaitableGetResourcesResult(GetResourcesResult):
    def __await__(self): # -> Generator[Never, Any, GetResourcesResult]:
        ...
    


def get_resources(exclude_compliant_resources: Optional[_builtins.bool] = ..., include_compliance_details: Optional[_builtins.bool] = ..., region: Optional[_builtins.str] = ..., resource_arn_lists: Optional[Sequence[_builtins.str]] = ..., resource_type_filters: Optional[Sequence[_builtins.str]] = ..., tag_filters: Optional[Sequence[Union[GetResourcesTagFilterArgs, GetResourcesTagFilterArgsDict]]] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetResourcesResult:
    
    ...

def get_resources_output(exclude_compliant_resources: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., include_compliance_details: Optional[pulumi.Input[Optional[_builtins.bool]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., resource_arn_lists: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., resource_type_filters: Optional[pulumi.Input[Optional[Sequence[_builtins.str]]]] = ..., tag_filters: Optional[pulumi.Input[Optional[Sequence[Union[GetResourcesTagFilterArgs, GetResourcesTagFilterArgsDict]]]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetResourcesResult]:
    
    ...

