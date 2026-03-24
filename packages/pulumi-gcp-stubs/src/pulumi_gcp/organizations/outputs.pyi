

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessApprovalSettingsEnrolledService', 'IAMBindingCondition', 'IAMMemberCondition', 'IamAuditConfigAuditLogConfig', 'PolicyBooleanPolicy', 'PolicyListPolicy', 'PolicyListPolicyAllow', 'PolicyListPolicyDeny', 'PolicyRestorePolicy', 'GetFoldersFolderResult', 'GetIAMPolicyAuditConfigResult', 'GetIAMPolicyAuditConfigAuditLogConfigResult', 'GetIAMPolicyBindingResult', 'GetIAMPolicyBindingConditionResult', 'GetIamCustomRolesRoleResult', 'GetSOrganizationResult']
@pulumi.output_type
class AccessApprovalSettingsEnrolledService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloud_product: _builtins.str, enrollment_level: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudProduct")
    def cloud_product(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enrollmentLevel")
    def enrollment_level(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IAMBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IAMMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IamAuditConfigAuditLogConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, log_type: _builtins.str, exempted_members: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptedMembers")
    def exempted_members(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PolicyBooleanPolicy(dict):
    def __init__(__self__, *, enforced: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enforced(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class PolicyListPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow: Optional[outputs.PolicyListPolicyAllow] = ..., deny: Optional[outputs.PolicyListPolicyDeny] = ..., inherit_from_parent: Optional[_builtins.bool] = ..., suggested_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[outputs.PolicyListPolicyAllow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deny(self) -> Optional[outputs.PolicyListPolicyDeny]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritFromParent")
    def inherit_from_parent(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suggestedValue")
    def suggested_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PolicyListPolicyAllow(dict):
    def __init__(__self__, *, all: Optional[_builtins.bool] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PolicyListPolicyDeny(dict):
    def __init__(__self__, *, all: Optional[_builtins.bool] = ..., values: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class PolicyRestorePolicy(dict):
    def __init__(__self__, *, default: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetFoldersFolderResult(dict):
    def __init__(__self__, *, create_time: _builtins.str, delete_time: _builtins.str, display_name: _builtins.str, etag: _builtins.str, name: _builtins.str, parent: _builtins.str, state: _builtins.str, update_time: _builtins.str) -> None:
        
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
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> _builtins.str:
        
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
    @pulumi.getter
    def state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetIAMPolicyAuditConfigResult(dict):
    def __init__(__self__, *, audit_log_configs: Sequence[outputs.GetIAMPolicyAuditConfigAuditLogConfigResult], service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="auditLogConfigs")
    def audit_log_configs(self) -> Sequence[outputs.GetIAMPolicyAuditConfigAuditLogConfigResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetIAMPolicyAuditConfigAuditLogConfigResult(dict):
    def __init__(__self__, *, log_type: _builtins.str, exempted_members: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptedMembers")
    def exempted_members(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class GetIAMPolicyBindingResult(dict):
    def __init__(__self__, *, members: Sequence[_builtins.str], role: _builtins.str, condition: Optional[outputs.GetIAMPolicyBindingConditionResult] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def members(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.GetIAMPolicyBindingConditionResult]:
        
        ...
    


@pulumi.output_type
class GetIAMPolicyBindingConditionResult(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GetIamCustomRolesRoleResult(dict):
    def __init__(__self__, *, deleted: _builtins.bool, description: _builtins.str, id: _builtins.str, name: _builtins.str, permissions: Sequence[_builtins.str], role_id: _builtins.str, stage: _builtins.str, title: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def deleted(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleId")
    def role_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def stage(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSOrganizationResult(dict):
    def __init__(__self__, *, directory_customer_id: _builtins.str, display_name: _builtins.str, lifecycle_state: _builtins.str, name: _builtins.str, org_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryCustomerId")
    def directory_customer_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lifecycleState")
    def lifecycle_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgId")
    def org_id(self) -> _builtins.str:
        
        ...
    


