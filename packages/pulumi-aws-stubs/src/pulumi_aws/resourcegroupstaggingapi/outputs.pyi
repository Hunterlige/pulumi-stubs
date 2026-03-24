

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRequiredTagsRequiredTagResult', 'GetResourcesResourceTagMappingListResult', ..., 'GetResourcesTagFilterResult']
@pulumi.output_type
class GetRequiredTagsRequiredTagResult(dict):
    def __init__(__self__, *, cloud_formation_resource_types: Sequence[_builtins.str], reporting_tag_keys: Sequence[_builtins.str], resource_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudFormationResourceTypes")
    def cloud_formation_resource_types(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="reportingTagKeys")
    def reporting_tag_keys(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetResourcesResourceTagMappingListResult(dict):
    def __init__(__self__, *, compliance_details: Sequence[outputs.GetResourcesResourceTagMappingListComplianceDetailResult], resource_arn: _builtins.str, tags: Mapping[str, _builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceDetails")
    def compliance_details(self) -> Sequence[outputs.GetResourcesResourceTagMappingListComplianceDetailResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    


@pulumi.output_type
class GetResourcesResourceTagMappingListComplianceDetailResult(dict):
    def __init__(__self__, *, compliance_status: _builtins.bool, keys_with_noncompliant_values: Sequence[_builtins.str], non_compliant_keys: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceStatus")
    def compliance_status(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keysWithNoncompliantValues")
    def keys_with_noncompliant_values(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonCompliantKeys")
    def non_compliant_keys(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class GetResourcesTagFilterResult(dict):
    def __init__(__self__, *, key: _builtins.str, values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


