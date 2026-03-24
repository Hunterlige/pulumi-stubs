

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
__all__ = ['PolicyArgs', 'Policy']
@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *, exclude_resource_tags: pulumi.Input[_builtins.bool], security_service_policy_data: pulumi.Input[PolicySecurityServicePolicyDataArgs], delete_all_policy_resources: Optional[pulumi.Input[_builtins.bool]] = ..., delete_unused_fm_managed_resources: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exclude_map: Optional[pulumi.Input[PolicyExcludeMapArgs]] = ..., include_map: Optional[pulumi.Input[PolicyIncludeMapArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remediation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., resource_set_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_tag_logical_operator: Optional[pulumi.Input[_builtins.str]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_type_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeResourceTags")
    def exclude_resource_tags(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @exclude_resource_tags.setter
    def exclude_resource_tags(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityServicePolicyData")
    def security_service_policy_data(self) -> pulumi.Input[PolicySecurityServicePolicyDataArgs]:
        
        ...
    
    @security_service_policy_data.setter
    def security_service_policy_data(self, value: pulumi.Input[PolicySecurityServicePolicyDataArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAllPolicyResources")
    def delete_all_policy_resources(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_all_policy_resources.setter
    def delete_all_policy_resources(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteUnusedFmManagedResources")
    def delete_unused_fm_managed_resources(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_unused_fm_managed_resources.setter
    def delete_unused_fm_managed_resources(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeMap")
    def exclude_map(self) -> Optional[pulumi.Input[PolicyExcludeMapArgs]]:
        
        ...
    
    @exclude_map.setter
    def exclude_map(self, value: Optional[pulumi.Input[PolicyExcludeMapArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeMap")
    def include_map(self) -> Optional[pulumi.Input[PolicyIncludeMapArgs]]:
        
        ...
    
    @include_map.setter
    def include_map(self, value: Optional[pulumi.Input[PolicyIncludeMapArgs]]): # -> None:
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
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remediationEnabled")
    def remediation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @remediation_enabled.setter
    def remediation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSetIds")
    def resource_set_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @resource_set_ids.setter
    def resource_set_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagLogicalOperator")
    def resource_tag_logical_operator(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_tag_logical_operator.setter
    def resource_tag_logical_operator(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_tags.setter
    def resource_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypeLists")
    def resource_type_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_type_lists.setter
    def resource_type_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _PolicyState:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ..., delete_all_policy_resources: Optional[pulumi.Input[_builtins.bool]] = ..., delete_unused_fm_managed_resources: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exclude_map: Optional[pulumi.Input[PolicyExcludeMapArgs]] = ..., exclude_resource_tags: Optional[pulumi.Input[_builtins.bool]] = ..., include_map: Optional[pulumi.Input[PolicyIncludeMapArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_update_token: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remediation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., resource_set_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_tag_logical_operator: Optional[pulumi.Input[_builtins.str]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_type_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_service_policy_data: Optional[pulumi.Input[PolicySecurityServicePolicyDataArgs]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAllPolicyResources")
    def delete_all_policy_resources(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_all_policy_resources.setter
    def delete_all_policy_resources(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteUnusedFmManagedResources")
    def delete_unused_fm_managed_resources(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_unused_fm_managed_resources.setter
    def delete_unused_fm_managed_resources(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeMap")
    def exclude_map(self) -> Optional[pulumi.Input[PolicyExcludeMapArgs]]:
        
        ...
    
    @exclude_map.setter
    def exclude_map(self, value: Optional[pulumi.Input[PolicyExcludeMapArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeResourceTags")
    def exclude_resource_tags(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @exclude_resource_tags.setter
    def exclude_resource_tags(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeMap")
    def include_map(self) -> Optional[pulumi.Input[PolicyIncludeMapArgs]]:
        
        ...
    
    @include_map.setter
    def include_map(self, value: Optional[pulumi.Input[PolicyIncludeMapArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyUpdateToken")
    def policy_update_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @policy_update_token.setter
    def policy_update_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remediationEnabled")
    def remediation_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @remediation_enabled.setter
    def remediation_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSetIds")
    def resource_set_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @resource_set_ids.setter
    def resource_set_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagLogicalOperator")
    def resource_tag_logical_operator(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_tag_logical_operator.setter
    def resource_tag_logical_operator(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_tags.setter
    def resource_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypeLists")
    def resource_type_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @resource_type_lists.setter
    def resource_type_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityServicePolicyData")
    def security_service_policy_data(self) -> Optional[pulumi.Input[PolicySecurityServicePolicyDataArgs]]:
        
        ...
    
    @security_service_policy_data.setter
    def security_service_policy_data(self, value: Optional[pulumi.Input[PolicySecurityServicePolicyDataArgs]]): # -> None:
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
    


@pulumi.type_token("aws:fms/policy:Policy")
class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., delete_all_policy_resources: Optional[pulumi.Input[_builtins.bool]] = ..., delete_unused_fm_managed_resources: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exclude_map: Optional[pulumi.Input[Union[PolicyExcludeMapArgs, PolicyExcludeMapArgsDict]]] = ..., exclude_resource_tags: Optional[pulumi.Input[_builtins.bool]] = ..., include_map: Optional[pulumi.Input[Union[PolicyIncludeMapArgs, PolicyIncludeMapArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remediation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., resource_set_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_tag_logical_operator: Optional[pulumi.Input[_builtins.str]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_type_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_service_policy_data: Optional[pulumi.Input[Union[PolicySecurityServicePolicyDataArgs, PolicySecurityServicePolicyDataArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PolicyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., delete_all_policy_resources: Optional[pulumi.Input[_builtins.bool]] = ..., delete_unused_fm_managed_resources: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., exclude_map: Optional[pulumi.Input[Union[PolicyExcludeMapArgs, PolicyExcludeMapArgsDict]]] = ..., exclude_resource_tags: Optional[pulumi.Input[_builtins.bool]] = ..., include_map: Optional[pulumi.Input[Union[PolicyIncludeMapArgs, PolicyIncludeMapArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., policy_update_token: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., remediation_enabled: Optional[pulumi.Input[_builtins.bool]] = ..., resource_set_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., resource_tag_logical_operator: Optional[pulumi.Input[_builtins.str]] = ..., resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., resource_type_lists: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., security_service_policy_data: Optional[pulumi.Input[Union[PolicySecurityServicePolicyDataArgs, PolicySecurityServicePolicyDataArgsDict]]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> Policy:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteAllPolicyResources")
    def delete_all_policy_resources(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteUnusedFmManagedResources")
    def delete_unused_fm_managed_resources(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeMap")
    def exclude_map(self) -> pulumi.Output[Optional[outputs.PolicyExcludeMap]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeResourceTags")
    def exclude_resource_tags(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeMap")
    def include_map(self) -> pulumi.Output[Optional[outputs.PolicyIncludeMap]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyUpdateToken")
    def policy_update_token(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remediationEnabled")
    def remediation_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceSetIds")
    def resource_set_ids(self) -> pulumi.Output[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTagLogicalOperator")
    def resource_tag_logical_operator(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypeLists")
    def resource_type_lists(self) -> pulumi.Output[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityServicePolicyData")
    def security_service_policy_data(self) -> pulumi.Output[outputs.PolicySecurityServicePolicyData]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


