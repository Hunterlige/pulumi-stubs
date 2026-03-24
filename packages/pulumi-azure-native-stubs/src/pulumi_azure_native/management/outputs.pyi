

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DescendantParentGroupInfoResponse', 'EntityInfoResponse', 'EntityParentGroupInfoResponse', 'ManagementGroupChildInfoResponse', 'ManagementGroupDetailsResponse', 'ManagementGroupPathElementResponse', 'ParentGroupInfoResponse', 'ParentServiceGroupPropertiesResponse', 'ServiceGroupPropertiesResponse', 'ServiceGroupResponse', 'SystemDataResponse']
@pulumi.output_type
class DescendantParentGroupInfoResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EntityInfoResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, type: _builtins.str, display_name: Optional[_builtins.str] = ..., inherited_permissions: Optional[_builtins.str] = ..., number_of_child_groups: Optional[_builtins.int] = ..., number_of_children: Optional[_builtins.int] = ..., number_of_descendants: Optional[_builtins.int] = ..., parent: Optional[outputs.EntityParentGroupInfoResponse] = ..., parent_display_name_chain: Optional[Sequence[_builtins.str]] = ..., parent_name_chain: Optional[Sequence[_builtins.str]] = ..., permissions: Optional[_builtins.str] = ..., tenant_id: Optional[_builtins.str] = ...) -> None:
        
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
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inheritedPermissions")
    def inherited_permissions(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfChildGroups")
    def number_of_child_groups(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfChildren")
    def number_of_children(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="numberOfDescendants")
    def number_of_descendants(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[outputs.EntityParentGroupInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentDisplayNameChain")
    def parent_display_name_chain(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentNameChain")
    def parent_name_chain(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def permissions(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EntityParentGroupInfoResponse(dict):
    
    def __init__(__self__, *, id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagementGroupChildInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, children: Optional[Sequence[outputs.ManagementGroupChildInfoResponse]] = ..., display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def children(self) -> Optional[Sequence[outputs.ManagementGroupChildInfoResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ManagementGroupDetailsResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, management_group_ancestors: Optional[Sequence[_builtins.str]] = ..., management_group_ancestors_chain: Optional[Sequence[outputs.ManagementGroupPathElementResponse]] = ..., parent: Optional[outputs.ParentGroupInfoResponse] = ..., path: Optional[Sequence[outputs.ManagementGroupPathElementResponse]] = ..., updated_by: Optional[_builtins.str] = ..., updated_time: Optional[_builtins.str] = ..., version: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementGroupAncestors")
    def management_group_ancestors(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managementGroupAncestorsChain")
    def management_group_ancestors_chain(self) -> Optional[Sequence[outputs.ManagementGroupPathElementResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[outputs.ParentGroupInfoResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[Sequence[outputs.ManagementGroupPathElementResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ManagementGroupPathElementResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ParentGroupInfoResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ParentServiceGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServiceGroupPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, provisioning_state: _builtins.str, display_name: Optional[_builtins.str] = ..., parent: Optional[outputs.ParentServiceGroupPropertiesResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parent(self) -> Optional[outputs.ParentServiceGroupPropertiesResponse]:
        
        ...
    


@pulumi.output_type
class ServiceGroupResponse(dict):
    
    def __init__(__self__, *, id: _builtins.str, name: _builtins.str, system_data: outputs.SystemDataResponse, type: _builtins.str, kind: Optional[_builtins.str] = ..., properties: Optional[outputs.ServiceGroupPropertiesResponse] = ..., tags: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
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
    def kind(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[outputs.ServiceGroupPropertiesResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]:
        
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
    


