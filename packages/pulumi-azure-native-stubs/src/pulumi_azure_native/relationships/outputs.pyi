

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['DependencyOfRelationshipPropertiesResponse', 'RelationshipMetadataResponse', 'RelationshipOriginInformationResponse', 'ServiceGroupMemberRelationshipPropertiesResponse', 'SystemDataResponse']
@pulumi.output_type
class DependencyOfRelationshipPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metadata: outputs.RelationshipMetadataResponse, origin_information: outputs.RelationshipOriginInformationResponse, provisioning_state: _builtins.str, source_id: _builtins.str, target_id: _builtins.str, target_tenant: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> outputs.RelationshipMetadataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originInformation")
    def origin_information(self) -> outputs.RelationshipOriginInformationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTenant")
    def target_tenant(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RelationshipMetadataResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_type: _builtins.str, target_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetType")
    def target_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RelationshipOriginInformationResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, discovery_engine: _builtins.str, relationship_origin_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryEngine")
    def discovery_engine(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationshipOriginType")
    def relationship_origin_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServiceGroupMemberRelationshipPropertiesResponse(dict):
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, metadata: outputs.RelationshipMetadataResponse, origin_information: outputs.RelationshipOriginInformationResponse, provisioning_state: _builtins.str, source_id: _builtins.str, target_id: _builtins.str, target_tenant: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> outputs.RelationshipMetadataResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="originInformation")
    def origin_information(self) -> outputs.RelationshipOriginInformationResponse:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetId")
    def target_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetTenant")
    def target_tenant(self) -> Optional[_builtins.str]:
        
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
    


