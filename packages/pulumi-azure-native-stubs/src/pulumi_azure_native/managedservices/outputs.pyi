

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AuthorizationResponse', 'EligibleApproverResponse', 'EligibleAuthorizationResponse', 'JustInTimeAccessPolicyResponse', 'PlanResponse', 'RegistrationAssignmentPropertiesResponse', 'RegistrationAssignmentPropertiesResponseProperties', ..., 'RegistrationDefinitionPropertiesResponse', 'SystemDataResponse']
@pulumi.output_type
class AuthorizationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, role_definition_id: _builtins.str, delegated_role_definition_ids: Optional[Sequence[_builtins.str]] = ..., principal_id_display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delegatedRoleDefinitionIds")
    def delegated_role_definition_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalIdDisplayName")
    def principal_id_display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EligibleApproverResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, principal_id_display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalIdDisplayName")
    def principal_id_display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EligibleAuthorizationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, principal_id: _builtins.str, role_definition_id: _builtins.str, just_in_time_access_policy: Optional[outputs.JustInTimeAccessPolicyResponse] = ..., principal_id_display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="justInTimeAccessPolicy")
    def just_in_time_access_policy(self) -> Optional[outputs.JustInTimeAccessPolicyResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalIdDisplayName")
    def principal_id_display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class JustInTimeAccessPolicyResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, multi_factor_auth_provider: Optional[_builtins.str] = ..., managed_by_tenant_approvers: Optional[Sequence[outputs.EligibleApproverResponse]] = ..., maximum_activation_duration: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="multiFactorAuthProvider")
    def multi_factor_auth_provider(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedByTenantApprovers")
    def managed_by_tenant_approvers(self) -> Optional[Sequence[outputs.EligibleApproverResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maximumActivationDuration")
    def maximum_activation_duration(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class PlanResponse(dict):
    
    def __init__(__self__, *, name: _builtins.str, product: _builtins.str, publisher: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RegistrationAssignmentPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, registration_definition: outputs.RegistrationAssignmentPropertiesResponseRegistrationDefinition, registration_definition_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationDefinition")
    def registration_definition(self) -> outputs.RegistrationAssignmentPropertiesResponseRegistrationDefinition:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationDefinitionId")
    def registration_definition_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RegistrationAssignmentPropertiesResponseProperties(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorizations: Optional[Sequence[outputs.AuthorizationResponse]] = ..., description: Optional[_builtins.str] = ..., eligible_authorizations: Optional[Sequence[outputs.EligibleAuthorizationResponse]] = ..., managed_by_tenant_id: Optional[_builtins.str] = ..., managed_by_tenant_name: Optional[_builtins.str] = ..., managee_tenant_id: Optional[_builtins.str] = ..., managee_tenant_name: Optional[_builtins.str] = ..., provisioning_state: Optional[_builtins.str] = ..., registration_definition_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorizations(self) -> Optional[Sequence[outputs.AuthorizationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eligibleAuthorizations")
    def eligible_authorizations(self) -> Optional[Sequence[outputs.EligibleAuthorizationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedByTenantId")
    def managed_by_tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedByTenantName")
    def managed_by_tenant_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageeTenantId")
    def managee_tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageeTenantName")
    def managee_tenant_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationDefinitionName")
    def registration_definition_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegistrationAssignmentPropertiesResponseRegistrationDefinition(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, plan: Optional[outputs.PlanResponse] = ..., properties: Optional[outputs.RegistrationAssignmentPropertiesResponseProperties] = ...) -> None:
        
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
    @pulumi.getter(name="systemData")
    def system_data(self) -> outputs.SystemDataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def plan(self) -> Optional[outputs.PlanResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.RegistrationAssignmentPropertiesResponseProperties]:
        
        ...
    


@pulumi.output_type
class RegistrationDefinitionPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authorizations: Sequence[outputs.AuthorizationResponse], managed_by_tenant_id: _builtins.str, managed_by_tenant_name: _builtins.str, managee_tenant_id: _builtins.str, managee_tenant_name: _builtins.str, provisioning_state: _builtins.str, description: Optional[_builtins.str] = ..., eligible_authorizations: Optional[Sequence[outputs.EligibleAuthorizationResponse]] = ..., registration_definition_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authorizations(self) -> Sequence[outputs.AuthorizationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedByTenantId")
    def managed_by_tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedByTenantName")
    def managed_by_tenant_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageeTenantId")
    def managee_tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="manageeTenantName")
    def managee_tenant_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eligibleAuthorizations")
    def eligible_authorizations(self) -> Optional[Sequence[outputs.EligibleAuthorizationResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationDefinitionName")
    def registration_definition_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SystemDataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, created_at: Optional[_builtins.str] = ..., created_by: Optional[_builtins.str] = ..., created_by_type: Optional[_builtins.str] = ..., last_modified_at: Optional[_builtins.str] = ..., last_modified_by: Optional[_builtins.str] = ..., last_modified_by_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[_builtins.str]:
        
        ...
    


