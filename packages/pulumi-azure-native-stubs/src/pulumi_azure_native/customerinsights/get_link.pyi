

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetLinkResult', 'AwaitableGetLinkResult', 'get_link', 'get_link_output']
@pulumi.output_type
class GetLinkResult:
    
    def __init__(__self__, azure_api_version=..., description=..., display_name=..., id=..., link_name=..., mappings=..., name=..., operation_type=..., participant_property_references=..., provisioning_state=..., reference_only=..., source_entity_type=..., source_entity_type_name=..., target_entity_type=..., target_entity_type_name=..., tenant_id=..., type=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="linkName")
    def link_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mappings(self) -> Optional[Sequence[outputs.TypePropertiesMappingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="participantPropertyReferences")
    def participant_property_references(self) -> Sequence[outputs.ParticipantPropertyReferenceResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="referenceOnly")
    def reference_only(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEntityType")
    def source_entity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceEntityTypeName")
    def source_entity_type_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEntityType")
    def target_entity_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetEntityTypeName")
    def target_entity_type_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


class AwaitableGetLinkResult(GetLinkResult):
    def __await__(self): # -> Generator[Never, Any, GetLinkResult]:
        ...
    


def get_link(hub_name: Optional[_builtins.str] = ..., link_name: Optional[_builtins.str] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetLinkResult:
    
    ...

def get_link_output(hub_name: Optional[pulumi.Input[_builtins.str]] = ..., link_name: Optional[pulumi.Input[_builtins.str]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetLinkResult]:
    
    ...

