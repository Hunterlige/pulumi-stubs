

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
__all__ = ['RelationshipLinkArgs', 'RelationshipLink']
@pulumi.input_type
class RelationshipLinkArgs:
    def __init__(__self__, *, hub_name: pulumi.Input[_builtins.str], interaction_type: pulumi.Input[_builtins.str], profile_property_references: pulumi.Input[Sequence[pulumi.Input[ParticipantProfilePropertyReferenceArgs]]], related_profile_property_references: pulumi.Input[Sequence[pulumi.Input[ParticipantProfilePropertyReferenceArgs]]], relationship_name: pulumi.Input[_builtins.str], resource_group_name: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., mappings: Optional[pulumi.Input[Sequence[pulumi.Input[RelationshipLinkFieldMappingArgs]]]] = ..., relationship_link_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hub_name.setter
    def hub_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interactionType")
    def interaction_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @interaction_type.setter
    def interaction_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="profilePropertyReferences")
    def profile_property_references(self) -> pulumi.Input[Sequence[pulumi.Input[ParticipantProfilePropertyReferenceArgs]]]:
        
        ...
    
    @profile_property_references.setter
    def profile_property_references(self, value: pulumi.Input[Sequence[pulumi.Input[ParticipantProfilePropertyReferenceArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedProfilePropertyReferences")
    def related_profile_property_references(self) -> pulumi.Input[Sequence[pulumi.Input[ParticipantProfilePropertyReferenceArgs]]]:
        
        ...
    
    @related_profile_property_references.setter
    def related_profile_property_references(self, value: pulumi.Input[Sequence[pulumi.Input[ParticipantProfilePropertyReferenceArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationshipName")
    def relationship_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @relationship_name.setter
    def relationship_name(self, value: pulumi.Input[_builtins.str]): # -> None:
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
    @pulumi.getter
    def mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RelationshipLinkFieldMappingArgs]]]]:
        
        ...
    
    @mappings.setter
    def mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RelationshipLinkFieldMappingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relationshipLinkName")
    def relationship_link_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @relationship_link_name.setter
    def relationship_link_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("azure-native:customerinsights:RelationshipLink")
class RelationshipLink(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., description: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., hub_name: Optional[pulumi.Input[_builtins.str]] = ..., interaction_type: Optional[pulumi.Input[_builtins.str]] = ..., mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RelationshipLinkFieldMappingArgs, RelationshipLinkFieldMappingArgsDict]]]]] = ..., profile_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ParticipantProfilePropertyReferenceArgs, ParticipantProfilePropertyReferenceArgsDict]]]]] = ..., related_profile_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ParticipantProfilePropertyReferenceArgs, ParticipantProfilePropertyReferenceArgsDict]]]]] = ..., relationship_link_name: Optional[pulumi.Input[_builtins.str]] = ..., relationship_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RelationshipLinkArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ...) -> RelationshipLink:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="interactionType")
    def interaction_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkName")
    def link_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mappings(self) -> pulumi.Output[Optional[Sequence[outputs.RelationshipLinkFieldMappingResponse]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profilePropertyReferences")
    def profile_property_references(self) -> pulumi.Output[Sequence[outputs.ParticipantProfilePropertyReferenceResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedProfilePropertyReferences")
    def related_profile_property_references(self) -> pulumi.Output[Sequence[outputs.ParticipantProfilePropertyReferenceResponse]]:
        
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
    


