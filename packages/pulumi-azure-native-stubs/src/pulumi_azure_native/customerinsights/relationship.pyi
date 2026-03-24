

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RelationshipArgs', 'Relationship']
@pulumi.input_type
class RelationshipArgs:
    def __init__(__self__, *, hub_name: pulumi.Input[_builtins.str], profile_type: pulumi.Input[_builtins.str], related_profile_type: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], cardinality: Optional[pulumi.Input[CardinalityTypes]] = ..., description: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., expiry_date_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., fields: Optional[pulumi.Input[Sequence[pulumi.Input[PropertyDefinitionArgs]]]] = ..., lookup_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[RelationshipTypeMappingArgs]]]] = ..., relationship_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hub_name.setter
    def hub_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileType")
    def profile_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @profile_type.setter
    def profile_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedProfileType")
    def related_profile_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @related_profile_type.setter
    def related_profile_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cardinality(self) -> Optional[pulumi.Input[CardinalityTypes]]:
        
        ...
    
    @cardinality.setter
    def cardinality(self, value: Optional[pulumi.Input[CardinalityTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDateTimeUtc")
    def expiry_date_time_utc(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @expiry_date_time_utc.setter
    def expiry_date_time_utc(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[PropertyDefinitionArgs]]]]:
        
        ...
    
    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PropertyDefinitionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookupMappings")
    def lookup_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RelationshipTypeMappingArgs]]]]:
        
        ...
    
    @lookup_mappings.setter
    def lookup_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RelationshipTypeMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationshipName")
    def relationship_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @relationship_name.setter
    def relationship_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:customerinsights:Relationship")
class Relationship(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., cardinality: Optional[pulumi.Input[CardinalityTypes]] = ..., description: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., expiry_date_time_utc: Optional[pulumi.Input[_builtins.str]] = ..., fields: Optional[pulumi.Input[Sequence[pulumi.Input[Union[PropertyDefinitionArgs, PropertyDefinitionArgsDict]]]]] = ..., hub_name: Optional[pulumi.Input[_builtins.str]] = ..., lookup_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RelationshipTypeMappingArgs, RelationshipTypeMappingArgsDict]]]]] = ..., profile_type: Optional[pulumi.Input[_builtins.str]] = ..., related_profile_type: Optional[pulumi.Input[_builtins.str]] = ..., relationship_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RelationshipArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> Relationship:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cardinality(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expiryDateTimeUtc")
    def expiry_date_time_utc(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Optional[Sequence[outputs.PropertyDefinitionResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookupMappings")
    def lookup_mappings(self) -> pulumi.Output[Optional[Sequence[outputs.RelationshipTypeMappingResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileType")
    def profile_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedProfileType")
    def related_profile_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationshipGuidId")
    def relationship_guid_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationshipName")
    def relationship_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


