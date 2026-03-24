import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ApplicationAttributes",
    "ApplicationAttributesBusinessOwner",
    "ApplicationAttributesCriticality",
    "ApplicationAttributesDeveloperOwner",
    "ApplicationAttributesEnvironment",
    "ApplicationAttributesOperatorOwner",
    "ApplicationScope",
    "ServiceAttributes",
    "ServiceAttributesBusinessOwner",
    "ServiceAttributesCriticality",
    "ServiceAttributesDeveloperOwner",
    "ServiceAttributesEnvironment",
    "ServiceAttributesOperatorOwner",
    "ServiceServiceProperty",
    "ServiceServicePropertyExtendedMetadata",
    "ServiceServicePropertyExtendedMetadataValue",
    "ServiceServicePropertyFunctionalType",
    "ServiceServicePropertyIdentity",
    "ServiceServicePropertyRegistrationType",
    "ServiceServiceReference",
    "WorkloadAttributes",
    "WorkloadAttributesBusinessOwner",
    "WorkloadAttributesCriticality",
    "WorkloadAttributesDeveloperOwner",
    "WorkloadAttributesEnvironment",
    "WorkloadAttributesOperatorOwner",
    "WorkloadWorkloadProperty",
    "WorkloadWorkloadPropertyExtendedMetadata",
    "WorkloadWorkloadPropertyExtendedMetadataValue",
    "WorkloadWorkloadPropertyFunctionalType",
    "WorkloadWorkloadPropertyIdentity",
    "WorkloadWorkloadReference",
    "GetApplicationAttributeResult",
    "GetApplicationAttributeBusinessOwnerResult",
    "GetApplicationAttributeCriticalityResult",
    "GetApplicationAttributeDeveloperOwnerResult",
    "GetApplicationAttributeEnvironmentResult",
    "GetApplicationAttributeOperatorOwnerResult",
    "GetApplicationScopeResult",
    "GetDiscoveredServiceServicePropertyResult",
    "GetDiscoveredServiceServiceReferenceResult",
    "GetDiscoveredWorkloadWorkloadPropertyResult",
    "GetDiscoveredWorkloadWorkloadReferenceResult",
]

@pulumi.output_type
class ApplicationAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        business_owners: Optional[
            Sequence[outputs.ApplicationAttributesBusinessOwner]
        ] = ...,
        criticality: Optional[outputs.ApplicationAttributesCriticality] = ...,
        developer_owners: Optional[
            Sequence[outputs.ApplicationAttributesDeveloperOwner]
        ] = ...,
        environment: Optional[outputs.ApplicationAttributesEnvironment] = ...,
        operator_owners: Optional[
            Sequence[outputs.ApplicationAttributesOperatorOwner]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="businessOwners")
    def business_owners(
        self,
    ) -> Optional[Sequence[outputs.ApplicationAttributesBusinessOwner]]: ...
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[outputs.ApplicationAttributesCriticality]: ...
    @_builtins.property
    @pulumi.getter(name="developerOwners")
    def developer_owners(
        self,
    ) -> Optional[Sequence[outputs.ApplicationAttributesDeveloperOwner]]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[outputs.ApplicationAttributesEnvironment]: ...
    @_builtins.property
    @pulumi.getter(name="operatorOwners")
    def operator_owners(
        self,
    ) -> Optional[Sequence[outputs.ApplicationAttributesOperatorOwner]]: ...

@pulumi.output_type
class ApplicationAttributesBusinessOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationAttributesCriticality(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationAttributesDeveloperOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationAttributesEnvironment(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ApplicationAttributesOperatorOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ApplicationScope(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        business_owners: Optional[
            Sequence[outputs.ServiceAttributesBusinessOwner]
        ] = ...,
        criticality: Optional[outputs.ServiceAttributesCriticality] = ...,
        developer_owners: Optional[
            Sequence[outputs.ServiceAttributesDeveloperOwner]
        ] = ...,
        environment: Optional[outputs.ServiceAttributesEnvironment] = ...,
        operator_owners: Optional[
            Sequence[outputs.ServiceAttributesOperatorOwner]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="businessOwners")
    def business_owners(
        self,
    ) -> Optional[Sequence[outputs.ServiceAttributesBusinessOwner]]: ...
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[outputs.ServiceAttributesCriticality]: ...
    @_builtins.property
    @pulumi.getter(name="developerOwners")
    def developer_owners(
        self,
    ) -> Optional[Sequence[outputs.ServiceAttributesDeveloperOwner]]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[outputs.ServiceAttributesEnvironment]: ...
    @_builtins.property
    @pulumi.getter(name="operatorOwners")
    def operator_owners(
        self,
    ) -> Optional[Sequence[outputs.ServiceAttributesOperatorOwner]]: ...

@pulumi.output_type
class ServiceAttributesBusinessOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceAttributesCriticality(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceAttributesDeveloperOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceAttributesEnvironment(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceAttributesOperatorOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceServiceProperty(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extended_metadatas: Optional[
            Sequence[outputs.ServiceServicePropertyExtendedMetadata]
        ] = ...,
        functional_types: Optional[
            Sequence[outputs.ServiceServicePropertyFunctionalType]
        ] = ...,
        gcp_project: Optional[_builtins.str] = ...,
        identities: Optional[Sequence[outputs.ServiceServicePropertyIdentity]] = ...,
        location: Optional[_builtins.str] = ...,
        registration_types: Optional[
            Sequence[outputs.ServiceServicePropertyRegistrationType]
        ] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extendedMetadatas")
    def extended_metadatas(
        self,
    ) -> Optional[Sequence[outputs.ServiceServicePropertyExtendedMetadata]]: ...
    @_builtins.property
    @pulumi.getter(name="functionalTypes")
    def functional_types(
        self,
    ) -> Optional[Sequence[outputs.ServiceServicePropertyFunctionalType]]: ...
    @_builtins.property
    @pulumi.getter(name="gcpProject")
    def gcp_project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[Sequence[outputs.ServiceServicePropertyIdentity]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registrationTypes")
    def registration_types(
        self,
    ) -> Optional[Sequence[outputs.ServiceServicePropertyRegistrationType]]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceServicePropertyExtendedMetadata(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        values: Optional[
            Sequence[outputs.ServiceServicePropertyExtendedMetadataValue]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[Sequence[outputs.ServiceServicePropertyExtendedMetadataValue]]: ...

@pulumi.output_type
class ServiceServicePropertyExtendedMetadataValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extended_metadata_schema: Optional[_builtins.str] = ...,
        metadata_struct: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extendedMetadataSchema")
    def extended_metadata_schema(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metadataStruct")
    def metadata_struct(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceServicePropertyFunctionalType(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceServicePropertyIdentity(dict):
    def __init__(__self__, *, principal: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceServicePropertyRegistrationType(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceServiceReference(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadAttributes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        business_owners: Optional[
            Sequence[outputs.WorkloadAttributesBusinessOwner]
        ] = ...,
        criticality: Optional[outputs.WorkloadAttributesCriticality] = ...,
        developer_owners: Optional[
            Sequence[outputs.WorkloadAttributesDeveloperOwner]
        ] = ...,
        environment: Optional[outputs.WorkloadAttributesEnvironment] = ...,
        operator_owners: Optional[
            Sequence[outputs.WorkloadAttributesOperatorOwner]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="businessOwners")
    def business_owners(
        self,
    ) -> Optional[Sequence[outputs.WorkloadAttributesBusinessOwner]]: ...
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[outputs.WorkloadAttributesCriticality]: ...
    @_builtins.property
    @pulumi.getter(name="developerOwners")
    def developer_owners(
        self,
    ) -> Optional[Sequence[outputs.WorkloadAttributesDeveloperOwner]]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[outputs.WorkloadAttributesEnvironment]: ...
    @_builtins.property
    @pulumi.getter(name="operatorOwners")
    def operator_owners(
        self,
    ) -> Optional[Sequence[outputs.WorkloadAttributesOperatorOwner]]: ...

@pulumi.output_type
class WorkloadAttributesBusinessOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadAttributesCriticality(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class WorkloadAttributesDeveloperOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadAttributesEnvironment(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class WorkloadAttributesOperatorOwner(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, email: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadWorkloadProperty(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extended_metadatas: Optional[
            Sequence[outputs.WorkloadWorkloadPropertyExtendedMetadata]
        ] = ...,
        functional_types: Optional[
            Sequence[outputs.WorkloadWorkloadPropertyFunctionalType]
        ] = ...,
        gcp_project: Optional[_builtins.str] = ...,
        identities: Optional[Sequence[outputs.WorkloadWorkloadPropertyIdentity]] = ...,
        location: Optional[_builtins.str] = ...,
        zone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extendedMetadatas")
    def extended_metadatas(
        self,
    ) -> Optional[Sequence[outputs.WorkloadWorkloadPropertyExtendedMetadata]]: ...
    @_builtins.property
    @pulumi.getter(name="functionalTypes")
    def functional_types(
        self,
    ) -> Optional[Sequence[outputs.WorkloadWorkloadPropertyFunctionalType]]: ...
    @_builtins.property
    @pulumi.getter(name="gcpProject")
    def gcp_project(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def identities(
        self,
    ) -> Optional[Sequence[outputs.WorkloadWorkloadPropertyIdentity]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadWorkloadPropertyExtendedMetadata(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        values: Optional[
            Sequence[outputs.WorkloadWorkloadPropertyExtendedMetadataValue]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[Sequence[outputs.WorkloadWorkloadPropertyExtendedMetadataValue]]: ...

@pulumi.output_type
class WorkloadWorkloadPropertyExtendedMetadataValue(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        extended_metadata_schema: Optional[_builtins.str] = ...,
        metadata_struct: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="extendedMetadataSchema")
    def extended_metadata_schema(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metadataStruct")
    def metadata_struct(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadWorkloadPropertyFunctionalType(dict):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadWorkloadPropertyIdentity(dict):
    def __init__(__self__, *, principal: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WorkloadWorkloadReference(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetApplicationAttributeResult(dict):
    def __init__(
        __self__,
        *,
        business_owners: Sequence[outputs.GetApplicationAttributeBusinessOwnerResult],
        criticalities: Sequence[outputs.GetApplicationAttributeCriticalityResult],
        developer_owners: Sequence[outputs.GetApplicationAttributeDeveloperOwnerResult],
        environments: Sequence[outputs.GetApplicationAttributeEnvironmentResult],
        operator_owners: Sequence[outputs.GetApplicationAttributeOperatorOwnerResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="businessOwners")
    def business_owners(
        self,
    ) -> Sequence[outputs.GetApplicationAttributeBusinessOwnerResult]: ...
    @_builtins.property
    @pulumi.getter
    def criticalities(
        self,
    ) -> Sequence[outputs.GetApplicationAttributeCriticalityResult]: ...
    @_builtins.property
    @pulumi.getter(name="developerOwners")
    def developer_owners(
        self,
    ) -> Sequence[outputs.GetApplicationAttributeDeveloperOwnerResult]: ...
    @_builtins.property
    @pulumi.getter
    def environments(
        self,
    ) -> Sequence[outputs.GetApplicationAttributeEnvironmentResult]: ...
    @_builtins.property
    @pulumi.getter(name="operatorOwners")
    def operator_owners(
        self,
    ) -> Sequence[outputs.GetApplicationAttributeOperatorOwnerResult]: ...

@pulumi.output_type
class GetApplicationAttributeBusinessOwnerResult(dict):
    def __init__(
        __self__, *, display_name: _builtins.str, email: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationAttributeCriticalityResult(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationAttributeDeveloperOwnerResult(dict):
    def __init__(
        __self__, *, display_name: _builtins.str, email: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationAttributeEnvironmentResult(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationAttributeOperatorOwnerResult(dict):
    def __init__(
        __self__, *, display_name: _builtins.str, email: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def email(self) -> _builtins.str: ...

@pulumi.output_type
class GetApplicationScopeResult(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDiscoveredServiceServicePropertyResult(dict):
    def __init__(
        __self__,
        *,
        gcp_project: _builtins.str,
        location: _builtins.str,
        zone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpProject")
    def gcp_project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class GetDiscoveredServiceServiceReferenceResult(dict):
    def __init__(__self__, *, path: _builtins.str, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...

@pulumi.output_type
class GetDiscoveredWorkloadWorkloadPropertyResult(dict):
    def __init__(
        __self__,
        *,
        gcp_project: _builtins.str,
        location: _builtins.str,
        zone: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcpProject")
    def gcp_project(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def zone(self) -> _builtins.str: ...

@pulumi.output_type
class GetDiscoveredWorkloadWorkloadReferenceResult(dict):
    def __init__(__self__, *, uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
