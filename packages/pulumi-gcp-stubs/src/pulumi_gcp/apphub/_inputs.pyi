

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ApplicationAttributesArgs', 'ApplicationAttributesArgsDict', 'ApplicationAttributesBusinessOwnerArgs', 'ApplicationAttributesBusinessOwnerArgsDict', 'ApplicationAttributesCriticalityArgs', 'ApplicationAttributesCriticalityArgsDict', 'ApplicationAttributesDeveloperOwnerArgs', 'ApplicationAttributesDeveloperOwnerArgsDict', 'ApplicationAttributesEnvironmentArgs', 'ApplicationAttributesEnvironmentArgsDict', 'ApplicationAttributesOperatorOwnerArgs', 'ApplicationAttributesOperatorOwnerArgsDict', 'ApplicationScopeArgs', 'ApplicationScopeArgsDict', 'ServiceAttributesArgs', 'ServiceAttributesArgsDict', 'ServiceAttributesBusinessOwnerArgs', 'ServiceAttributesBusinessOwnerArgsDict', 'ServiceAttributesCriticalityArgs', 'ServiceAttributesCriticalityArgsDict', 'ServiceAttributesDeveloperOwnerArgs', 'ServiceAttributesDeveloperOwnerArgsDict', 'ServiceAttributesEnvironmentArgs', 'ServiceAttributesEnvironmentArgsDict', 'ServiceAttributesOperatorOwnerArgs', 'ServiceAttributesOperatorOwnerArgsDict', 'ServiceServicePropertyArgs', 'ServiceServicePropertyArgsDict', 'ServiceServicePropertyExtendedMetadataArgs', 'ServiceServicePropertyExtendedMetadataArgsDict', 'ServiceServicePropertyExtendedMetadataValueArgs', ..., 'ServiceServicePropertyFunctionalTypeArgs', 'ServiceServicePropertyFunctionalTypeArgsDict', 'ServiceServicePropertyIdentityArgs', 'ServiceServicePropertyIdentityArgsDict', 'ServiceServicePropertyRegistrationTypeArgs', 'ServiceServicePropertyRegistrationTypeArgsDict', 'ServiceServiceReferenceArgs', 'ServiceServiceReferenceArgsDict', 'WorkloadAttributesArgs', 'WorkloadAttributesArgsDict', 'WorkloadAttributesBusinessOwnerArgs', 'WorkloadAttributesBusinessOwnerArgsDict', 'WorkloadAttributesCriticalityArgs', 'WorkloadAttributesCriticalityArgsDict', 'WorkloadAttributesDeveloperOwnerArgs', 'WorkloadAttributesDeveloperOwnerArgsDict', 'WorkloadAttributesEnvironmentArgs', 'WorkloadAttributesEnvironmentArgsDict', 'WorkloadAttributesOperatorOwnerArgs', 'WorkloadAttributesOperatorOwnerArgsDict', 'WorkloadWorkloadPropertyArgs', 'WorkloadWorkloadPropertyArgsDict', 'WorkloadWorkloadPropertyExtendedMetadataArgs', 'WorkloadWorkloadPropertyExtendedMetadataArgsDict', 'WorkloadWorkloadPropertyExtendedMetadataValueArgs', ..., 'WorkloadWorkloadPropertyFunctionalTypeArgs', 'WorkloadWorkloadPropertyFunctionalTypeArgsDict', 'WorkloadWorkloadPropertyIdentityArgs', 'WorkloadWorkloadPropertyIdentityArgsDict', 'WorkloadWorkloadReferenceArgs', 'WorkloadWorkloadReferenceArgsDict']
class ApplicationAttributesArgsDict(TypedDict):
    business_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesBusinessOwnerArgsDict]]]]
    criticality: NotRequired[pulumi.Input[ApplicationAttributesCriticalityArgsDict]]
    developer_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesDeveloperOwnerArgsDict]]]]
    environment: NotRequired[pulumi.Input[ApplicationAttributesEnvironmentArgsDict]]
    operator_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesOperatorOwnerArgsDict]]]]


@pulumi.input_type
class ApplicationAttributesArgs:
    def __init__(__self__, *, business_owners: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesBusinessOwnerArgs]]]] = ..., criticality: Optional[pulumi.Input[ApplicationAttributesCriticalityArgs]] = ..., developer_owners: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesDeveloperOwnerArgs]]]] = ..., environment: Optional[pulumi.Input[ApplicationAttributesEnvironmentArgs]] = ..., operator_owners: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesOperatorOwnerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessOwners")
    def business_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesBusinessOwnerArgs]]]]:
        
        ...
    
    @business_owners.setter
    def business_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesBusinessOwnerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[pulumi.Input[ApplicationAttributesCriticalityArgs]]:
        
        ...
    
    @criticality.setter
    def criticality(self, value: Optional[pulumi.Input[ApplicationAttributesCriticalityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerOwners")
    def developer_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesDeveloperOwnerArgs]]]]:
        
        ...
    
    @developer_owners.setter
    def developer_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesDeveloperOwnerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[ApplicationAttributesEnvironmentArgs]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[ApplicationAttributesEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorOwners")
    def operator_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesOperatorOwnerArgs]]]]:
        
        ...
    
    @operator_owners.setter
    def operator_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationAttributesOperatorOwnerArgs]]]]): # -> None:
        ...
    


class ApplicationAttributesBusinessOwnerArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationAttributesBusinessOwnerArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationAttributesCriticalityArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationAttributesCriticalityArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationAttributesDeveloperOwnerArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationAttributesDeveloperOwnerArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationAttributesEnvironmentArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationAttributesEnvironmentArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ApplicationAttributesOperatorOwnerArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationAttributesOperatorOwnerArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationScopeArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ApplicationScopeArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ServiceAttributesArgsDict(TypedDict):
    business_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesBusinessOwnerArgsDict]]]]
    criticality: NotRequired[pulumi.Input[ServiceAttributesCriticalityArgsDict]]
    developer_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesDeveloperOwnerArgsDict]]]]
    environment: NotRequired[pulumi.Input[ServiceAttributesEnvironmentArgsDict]]
    operator_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesOperatorOwnerArgsDict]]]]


@pulumi.input_type
class ServiceAttributesArgs:
    def __init__(__self__, *, business_owners: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesBusinessOwnerArgs]]]] = ..., criticality: Optional[pulumi.Input[ServiceAttributesCriticalityArgs]] = ..., developer_owners: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesDeveloperOwnerArgs]]]] = ..., environment: Optional[pulumi.Input[ServiceAttributesEnvironmentArgs]] = ..., operator_owners: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesOperatorOwnerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessOwners")
    def business_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesBusinessOwnerArgs]]]]:
        
        ...
    
    @business_owners.setter
    def business_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesBusinessOwnerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[pulumi.Input[ServiceAttributesCriticalityArgs]]:
        
        ...
    
    @criticality.setter
    def criticality(self, value: Optional[pulumi.Input[ServiceAttributesCriticalityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerOwners")
    def developer_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesDeveloperOwnerArgs]]]]:
        
        ...
    
    @developer_owners.setter
    def developer_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesDeveloperOwnerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[ServiceAttributesEnvironmentArgs]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[ServiceAttributesEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorOwners")
    def operator_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesOperatorOwnerArgs]]]]:
        
        ...
    
    @operator_owners.setter
    def operator_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceAttributesOperatorOwnerArgs]]]]): # -> None:
        ...
    


class ServiceAttributesBusinessOwnerArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceAttributesBusinessOwnerArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceAttributesCriticalityArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ServiceAttributesCriticalityArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ServiceAttributesDeveloperOwnerArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceAttributesDeveloperOwnerArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceAttributesEnvironmentArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class ServiceAttributesEnvironmentArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ServiceAttributesOperatorOwnerArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceAttributesOperatorOwnerArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceServicePropertyArgsDict(TypedDict):
    extended_metadatas: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyExtendedMetadataArgsDict]]]]
    functional_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyFunctionalTypeArgsDict]]]]
    gcp_project: NotRequired[pulumi.Input[_builtins.str]]
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyIdentityArgsDict]]]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    registration_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyRegistrationTypeArgsDict]]]]
    zone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceServicePropertyArgs:
    def __init__(__self__, *, extended_metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyExtendedMetadataArgs]]]] = ..., functional_types: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyFunctionalTypeArgs]]]] = ..., gcp_project: Optional[pulumi.Input[_builtins.str]] = ..., identities: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyIdentityArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., registration_types: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyRegistrationTypeArgs]]]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedMetadatas")
    def extended_metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyExtendedMetadataArgs]]]]:
        
        ...
    
    @extended_metadatas.setter
    def extended_metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyExtendedMetadataArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionalTypes")
    def functional_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyFunctionalTypeArgs]]]]:
        
        ...
    
    @functional_types.setter
    def functional_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyFunctionalTypeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpProject")
    def gcp_project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcp_project.setter
    def gcp_project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyIdentityArgs]]]]:
        
        ...
    
    @identities.setter
    def identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyIdentityArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationTypes")
    def registration_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyRegistrationTypeArgs]]]]:
        
        ...
    
    @registration_types.setter
    def registration_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyRegistrationTypeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceServicePropertyExtendedMetadataArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyExtendedMetadataValueArgsDict]]]]


@pulumi.input_type
class ServiceServicePropertyExtendedMetadataArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyExtendedMetadataValueArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyExtendedMetadataValueArgs]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceServicePropertyExtendedMetadataValueArgs]]]]): # -> None:
        ...
    


class ServiceServicePropertyExtendedMetadataValueArgsDict(TypedDict):
    extended_metadata_schema: NotRequired[pulumi.Input[_builtins.str]]
    metadata_struct: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceServicePropertyExtendedMetadataValueArgs:
    def __init__(__self__, *, extended_metadata_schema: Optional[pulumi.Input[_builtins.str]] = ..., metadata_struct: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedMetadataSchema")
    def extended_metadata_schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extended_metadata_schema.setter
    def extended_metadata_schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataStruct")
    def metadata_struct(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata_struct.setter
    def metadata_struct(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceServicePropertyFunctionalTypeArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceServicePropertyFunctionalTypeArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceServicePropertyIdentityArgsDict(TypedDict):
    principal: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceServicePropertyIdentityArgs:
    def __init__(__self__, *, principal: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceServicePropertyRegistrationTypeArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceServicePropertyRegistrationTypeArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceServiceReferenceArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ServiceServiceReferenceArgs:
    def __init__(__self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkloadAttributesArgsDict(TypedDict):
    business_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesBusinessOwnerArgsDict]]]]
    criticality: NotRequired[pulumi.Input[WorkloadAttributesCriticalityArgsDict]]
    developer_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesDeveloperOwnerArgsDict]]]]
    environment: NotRequired[pulumi.Input[WorkloadAttributesEnvironmentArgsDict]]
    operator_owners: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesOperatorOwnerArgsDict]]]]


@pulumi.input_type
class WorkloadAttributesArgs:
    def __init__(__self__, *, business_owners: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesBusinessOwnerArgs]]]] = ..., criticality: Optional[pulumi.Input[WorkloadAttributesCriticalityArgs]] = ..., developer_owners: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesDeveloperOwnerArgs]]]] = ..., environment: Optional[pulumi.Input[WorkloadAttributesEnvironmentArgs]] = ..., operator_owners: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesOperatorOwnerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessOwners")
    def business_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesBusinessOwnerArgs]]]]:
        
        ...
    
    @business_owners.setter
    def business_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesBusinessOwnerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[pulumi.Input[WorkloadAttributesCriticalityArgs]]:
        
        ...
    
    @criticality.setter
    def criticality(self, value: Optional[pulumi.Input[WorkloadAttributesCriticalityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerOwners")
    def developer_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesDeveloperOwnerArgs]]]]:
        
        ...
    
    @developer_owners.setter
    def developer_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesDeveloperOwnerArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[WorkloadAttributesEnvironmentArgs]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[WorkloadAttributesEnvironmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="operatorOwners")
    def operator_owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesOperatorOwnerArgs]]]]:
        
        ...
    
    @operator_owners.setter
    def operator_owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadAttributesOperatorOwnerArgs]]]]): # -> None:
        ...
    


class WorkloadAttributesBusinessOwnerArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkloadAttributesBusinessOwnerArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkloadAttributesCriticalityArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkloadAttributesCriticalityArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkloadAttributesDeveloperOwnerArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkloadAttributesDeveloperOwnerArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkloadAttributesEnvironmentArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkloadAttributesEnvironmentArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkloadAttributesOperatorOwnerArgsDict(TypedDict):
    email: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkloadAttributesOperatorOwnerArgs:
    def __init__(__self__, *, email: pulumi.Input[_builtins.str], display_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @email.setter
    def email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkloadWorkloadPropertyArgsDict(TypedDict):
    extended_metadatas: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyExtendedMetadataArgsDict]]]]
    functional_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyFunctionalTypeArgsDict]]]]
    gcp_project: NotRequired[pulumi.Input[_builtins.str]]
    identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyIdentityArgsDict]]]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    zone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkloadWorkloadPropertyArgs:
    def __init__(__self__, *, extended_metadatas: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyExtendedMetadataArgs]]]] = ..., functional_types: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyFunctionalTypeArgs]]]] = ..., gcp_project: Optional[pulumi.Input[_builtins.str]] = ..., identities: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyIdentityArgs]]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedMetadatas")
    def extended_metadatas(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyExtendedMetadataArgs]]]]:
        
        ...
    
    @extended_metadatas.setter
    def extended_metadatas(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyExtendedMetadataArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionalTypes")
    def functional_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyFunctionalTypeArgs]]]]:
        
        ...
    
    @functional_types.setter
    def functional_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyFunctionalTypeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcpProject")
    def gcp_project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcp_project.setter
    def gcp_project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyIdentityArgs]]]]:
        
        ...
    
    @identities.setter
    def identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyIdentityArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkloadWorkloadPropertyExtendedMetadataArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyExtendedMetadataValueArgsDict]]]]


@pulumi.input_type
class WorkloadWorkloadPropertyExtendedMetadataArgs:
    def __init__(__self__, *, key: Optional[pulumi.Input[_builtins.str]] = ..., values: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyExtendedMetadataValueArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyExtendedMetadataValueArgs]]]]:
        
        ...
    
    @values.setter
    def values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadWorkloadPropertyExtendedMetadataValueArgs]]]]): # -> None:
        ...
    


class WorkloadWorkloadPropertyExtendedMetadataValueArgsDict(TypedDict):
    extended_metadata_schema: NotRequired[pulumi.Input[_builtins.str]]
    metadata_struct: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkloadWorkloadPropertyExtendedMetadataValueArgs:
    def __init__(__self__, *, extended_metadata_schema: Optional[pulumi.Input[_builtins.str]] = ..., metadata_struct: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extendedMetadataSchema")
    def extended_metadata_schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @extended_metadata_schema.setter
    def extended_metadata_schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="metadataStruct")
    def metadata_struct(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata_struct.setter
    def metadata_struct(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkloadWorkloadPropertyFunctionalTypeArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkloadWorkloadPropertyFunctionalTypeArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkloadWorkloadPropertyIdentityArgsDict(TypedDict):
    principal: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkloadWorkloadPropertyIdentityArgs:
    def __init__(__self__, *, principal: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal.setter
    def principal(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkloadWorkloadReferenceArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkloadWorkloadReferenceArgs:
    def __init__(__self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


