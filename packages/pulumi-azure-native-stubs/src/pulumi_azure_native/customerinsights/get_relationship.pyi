import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetRelationshipResult",
    "AwaitableGetRelationshipResult",
    "get_relationship",
    "get_relationship_output",
]

@pulumi.output_type
class GetRelationshipResult:
    def __init__(
        __self__,
        azure_api_version=...,
        cardinality=...,
        description=...,
        display_name=...,
        expiry_date_time_utc=...,
        fields=...,
        id=...,
        lookup_mappings=...,
        name=...,
        profile_type=...,
        provisioning_state=...,
        related_profile_type=...,
        relationship_guid_id=...,
        relationship_name=...,
        tenant_id=...,
        type=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cardinality(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="expiryDateTimeUtc")
    def expiry_date_time_utc(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def fields(self) -> Optional[Sequence[outputs.PropertyDefinitionResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="lookupMappings")
    def lookup_mappings(
        self,
    ) -> Optional[Sequence[outputs.RelationshipTypeMappingResponse]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="profileType")
    def profile_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relatedProfileType")
    def related_profile_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relationshipGuidId")
    def relationship_guid_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relationshipName")
    def relationship_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

class AwaitableGetRelationshipResult(GetRelationshipResult):
    def __await__(self): ...

def get_relationship(
    hub_name: Optional[_builtins.str] = ...,
    relationship_name: Optional[_builtins.str] = ...,
    resource_group_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetRelationshipResult: ...
def get_relationship_output(
    hub_name: Optional[pulumi.Input[_builtins.str]] = ...,
    relationship_name: Optional[pulumi.Input[_builtins.str]] = ...,
    resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetRelationshipResult]: ...
