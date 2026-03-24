

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GroupAdditionalGroupKey', 'GroupGroupKey', 'GroupMembershipMemberKey', 'GroupMembershipPreferredMemberKey', 'GroupMembershipRole', 'GroupMembershipRoleExpiryDetail', 'PolicyPolicyQuery', 'PolicySetting', 'GetGroupLookupGroupKeyResult', 'GetGroupMembershipsMembershipResult', 'GetGroupMembershipsMembershipMemberKeyResult', ..., 'GetGroupMembershipsMembershipRoleResult', ..., 'GetGroupTransitiveMembershipsMembershipResult', ..., 'GetGroupTransitiveMembershipsMembershipRoleResult', 'GetGroupsGroupResult', 'GetGroupsGroupAdditionalGroupKeyResult', 'GetGroupsGroupGroupKeyResult', 'GetPoliciesPolicyResult', 'GetPoliciesPolicyPolicyQueryResult', 'GetPolicyPolicyQueryResult']
@pulumi.output_type
class GroupAdditionalGroupKey(dict):
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupGroupKey(dict):
    def __init__(__self__, *, id: _builtins.str, namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupMembershipMemberKey(dict):
    def __init__(__self__, *, id: _builtins.str, namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupMembershipPreferredMemberKey(dict):
    def __init__(__self__, *, id: _builtins.str, namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GroupMembershipRole(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, expiry_detail: Optional[outputs.GroupMembershipRoleExpiryDetail] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDetail")
    def expiry_detail(self) -> Optional[outputs.GroupMembershipRoleExpiryDetail]:
        
        ...
    


@pulumi.output_type
class GroupMembershipRoleExpiryDetail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expire_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class PolicyPolicyQuery(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, org_unit: _builtins.str, group: Optional[_builtins.str] = ..., query: Optional[_builtins.str] = ..., sort_order: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgUnit")
    def org_unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class PolicySetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, value_json: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueJson")
    def value_json(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupLookupGroupKeyResult(dict):
    def __init__(__self__, *, id: _builtins.str, namespace: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetGroupMembershipsMembershipResult(dict):
    def __init__(__self__, *, create_ignore_already_exists: _builtins.bool, create_time: _builtins.str, group: _builtins.str, member_keys: Sequence[outputs.GetGroupMembershipsMembershipMemberKeyResult], name: _builtins.str, preferred_member_keys: Sequence[outputs.GetGroupMembershipsMembershipPreferredMemberKeyResult], roles: Sequence[outputs.GetGroupMembershipsMembershipRoleResult], type: _builtins.str, update_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createIgnoreAlreadyExists")
    def create_ignore_already_exists(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memberKeys")
    def member_keys(self) -> Sequence[outputs.GetGroupMembershipsMembershipMemberKeyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMemberKeys")
    def preferred_member_keys(self) -> Sequence[outputs.GetGroupMembershipsMembershipPreferredMemberKeyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Sequence[outputs.GetGroupMembershipsMembershipRoleResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupMembershipsMembershipMemberKeyResult(dict):
    def __init__(__self__, *, id: _builtins.str, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupMembershipsMembershipPreferredMemberKeyResult(dict):
    def __init__(__self__, *, id: _builtins.str, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupMembershipsMembershipRoleResult(dict):
    def __init__(__self__, *, expiry_details: Sequence[outputs.GetGroupMembershipsMembershipRoleExpiryDetailResult], name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDetails")
    def expiry_details(self) -> Sequence[outputs.GetGroupMembershipsMembershipRoleExpiryDetailResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupMembershipsMembershipRoleExpiryDetailResult(dict):
    def __init__(__self__, *, expire_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupTransitiveMembershipsMembershipResult(dict):
    def __init__(__self__, *, member: _builtins.str, preferred_member_keys: Sequence[outputs.GetGroupTransitiveMembershipsMembershipPreferredMemberKeyResult], relation_type: _builtins.str, roles: Sequence[outputs.GetGroupTransitiveMembershipsMembershipRoleResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def member(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredMemberKeys")
    def preferred_member_keys(self) -> Sequence[outputs.GetGroupTransitiveMembershipsMembershipPreferredMemberKeyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationType")
    def relation_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def roles(self) -> Sequence[outputs.GetGroupTransitiveMembershipsMembershipRoleResult]:
        
        ...
    


@pulumi.output_type
class GetGroupTransitiveMembershipsMembershipPreferredMemberKeyResult(dict):
    def __init__(__self__, *, id: _builtins.str, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupTransitiveMembershipsMembershipRoleResult(dict):
    def __init__(__self__, *, role: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupsGroupResult(dict):
    def __init__(__self__, *, additional_group_keys: Sequence[outputs.GetGroupsGroupAdditionalGroupKeyResult], create_time: _builtins.str, description: _builtins.str, display_name: _builtins.str, group_keys: Sequence[outputs.GetGroupsGroupGroupKeyResult], initial_group_config: _builtins.str, labels: Mapping[str, _builtins.str], name: _builtins.str, parent: _builtins.str, update_time: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalGroupKeys")
    def additional_group_keys(self) -> Sequence[outputs.GetGroupsGroupAdditionalGroupKeyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupKeys")
    def group_keys(self) -> Sequence[outputs.GetGroupsGroupGroupKeyResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialGroupConfig")
    def initial_group_config(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupsGroupAdditionalGroupKeyResult(dict):
    def __init__(__self__, *, id: _builtins.str, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetGroupsGroupGroupKeyResult(dict):
    def __init__(__self__, *, id: _builtins.str, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPoliciesPolicyResult(dict):
    def __init__(__self__, *, customer: _builtins.str, name: _builtins.str, policy_queries: Sequence[outputs.GetPoliciesPolicyPolicyQueryResult], setting: _builtins.str, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def customer(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyQueries")
    def policy_queries(self) -> Sequence[outputs.GetPoliciesPolicyPolicyQueryResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def setting(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetPoliciesPolicyPolicyQueryResult(dict):
    def __init__(__self__, *, group: _builtins.str, org_unit: _builtins.str, query: _builtins.str, sort_order: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgUnit")
    def org_unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> _builtins.float:
        
        ...
    


@pulumi.output_type
class GetPolicyPolicyQueryResult(dict):
    def __init__(__self__, *, group: _builtins.str, org_unit: _builtins.str, query: _builtins.str, sort_order: _builtins.float) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def group(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgUnit")
    def org_unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> _builtins.float:
        
        ...
    


