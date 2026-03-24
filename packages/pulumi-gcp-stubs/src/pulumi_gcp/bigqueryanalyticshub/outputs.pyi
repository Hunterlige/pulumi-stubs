import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataExchangeIamBindingCondition",
    "DataExchangeIamMemberCondition",
    "DataExchangeSharingEnvironmentConfig",
    ...,
    ...,
    "DataExchangeSubscriptionDestinationDataset",
    ...,
    "DataExchangeSubscriptionLinkedDatasetMap",
    "DataExchangeSubscriptionLinkedResource",
    "ListingBigqueryDataset",
    "ListingBigqueryDatasetEffectiveReplica",
    "ListingBigqueryDatasetSelectedResource",
    "ListingCommercialInfo",
    "ListingCommercialInfoCloudMarketplace",
    "ListingDataProvider",
    "ListingIamBindingCondition",
    "ListingIamMemberCondition",
    "ListingPublisher",
    "ListingPubsubTopic",
    "ListingRestrictedExportConfig",
    "ListingSubscriptionCommercialInfo",
    "ListingSubscriptionCommercialInfoCloudMarketplace",
    "ListingSubscriptionDestinationDataset",
    ...,
    "ListingSubscriptionLinkedDatasetMap",
    "ListingSubscriptionLinkedResource",
]

@pulumi.output_type
class DataExchangeIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataExchangeIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataExchangeSharingEnvironmentConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dcr_exchange_config: Optional[
            outputs.DataExchangeSharingEnvironmentConfigDcrExchangeConfig
        ] = ...,
        default_exchange_config: Optional[
            outputs.DataExchangeSharingEnvironmentConfigDefaultExchangeConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dcrExchangeConfig")
    def dcr_exchange_config(
        self,
    ) -> Optional[outputs.DataExchangeSharingEnvironmentConfigDcrExchangeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="defaultExchangeConfig")
    def default_exchange_config(
        self,
    ) -> Optional[
        outputs.DataExchangeSharingEnvironmentConfigDefaultExchangeConfig
    ]: ...

@pulumi.output_type
class DataExchangeSharingEnvironmentConfigDcrExchangeConfig(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DataExchangeSharingEnvironmentConfigDefaultExchangeConfig(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DataExchangeSubscriptionDestinationDataset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_reference: outputs.DataExchangeSubscriptionDestinationDatasetDatasetReference,
        location: _builtins.str,
        description: Optional[_builtins.str] = ...,
        friendly_name: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetReference")
    def dataset_reference(
        self,
    ) -> outputs.DataExchangeSubscriptionDestinationDatasetDatasetReference: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class DataExchangeSubscriptionDestinationDatasetDatasetReference(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dataset_id: _builtins.str, project_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...

@pulumi.output_type
class DataExchangeSubscriptionLinkedDatasetMap(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_name: _builtins.str,
        linked_dataset: Optional[_builtins.str] = ...,
        linked_pubsub_subscription: Optional[_builtins.str] = ...,
        listing: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkedDataset")
    def linked_dataset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkedPubsubSubscription")
    def linked_pubsub_subscription(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def listing(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataExchangeSubscriptionLinkedResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        linked_dataset: Optional[_builtins.str] = ...,
        listing: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedDataset")
    def linked_dataset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def listing(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingBigqueryDataset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset: _builtins.str,
        effective_replicas: Optional[
            Sequence[outputs.ListingBigqueryDatasetEffectiveReplica]
        ] = ...,
        replica_locations: Optional[Sequence[_builtins.str]] = ...,
        selected_resources: Optional[
            Sequence[outputs.ListingBigqueryDatasetSelectedResource]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="effectiveReplicas")
    def effective_replicas(
        self,
    ) -> Optional[Sequence[outputs.ListingBigqueryDatasetEffectiveReplica]]: ...
    @_builtins.property
    @pulumi.getter(name="replicaLocations")
    def replica_locations(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="selectedResources")
    def selected_resources(
        self,
    ) -> Optional[Sequence[outputs.ListingBigqueryDatasetSelectedResource]]: ...

@pulumi.output_type
class ListingBigqueryDatasetEffectiveReplica(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        location: Optional[_builtins.str] = ...,
        primary_state: Optional[_builtins.str] = ...,
        replica_state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryState")
    def primary_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="replicaState")
    def replica_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingBigqueryDatasetSelectedResource(dict):
    def __init__(
        __self__,
        *,
        routine: Optional[_builtins.str] = ...,
        table: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def routine(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingCommercialInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_marketplaces: Optional[
            Sequence[outputs.ListingCommercialInfoCloudMarketplace]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudMarketplaces")
    def cloud_marketplaces(
        self,
    ) -> Optional[Sequence[outputs.ListingCommercialInfoCloudMarketplace]]: ...

@pulumi.output_type
class ListingCommercialInfoCloudMarketplace(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        commercial_state: Optional[_builtins.str] = ...,
        service: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commercialState")
    def commercial_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingDataProvider(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, name: _builtins.str, primary_contact: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingIamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingIamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingPublisher(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, name: _builtins.str, primary_contact: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingPubsubTopic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        topic: _builtins.str,
        data_affinity_regions: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataAffinityRegions")
    def data_affinity_regions(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ListingRestrictedExportConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        restrict_direct_table_access: Optional[_builtins.bool] = ...,
        restrict_query_result: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="restrictDirectTableAccess")
    def restrict_direct_table_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="restrictQueryResult")
    def restrict_query_result(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ListingSubscriptionCommercialInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_marketplaces: Optional[
            Sequence[outputs.ListingSubscriptionCommercialInfoCloudMarketplace]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudMarketplaces")
    def cloud_marketplaces(
        self,
    ) -> Optional[
        Sequence[outputs.ListingSubscriptionCommercialInfoCloudMarketplace]
    ]: ...

@pulumi.output_type
class ListingSubscriptionCommercialInfoCloudMarketplace(dict):
    def __init__(__self__, *, order: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingSubscriptionDestinationDataset(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dataset_reference: outputs.ListingSubscriptionDestinationDatasetDatasetReference,
        location: _builtins.str,
        description: Optional[_builtins.str] = ...,
        friendly_name: Optional[_builtins.str] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        replica_locations: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetReference")
    def dataset_reference(
        self,
    ) -> outputs.ListingSubscriptionDestinationDatasetDatasetReference: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="replicaLocations")
    def replica_locations(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ListingSubscriptionDestinationDatasetDatasetReference(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dataset_id: _builtins.str, project_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> _builtins.str: ...

@pulumi.output_type
class ListingSubscriptionLinkedDatasetMap(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        resource_name: _builtins.str,
        linked_dataset: Optional[_builtins.str] = ...,
        listing: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="linkedDataset")
    def linked_dataset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def listing(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ListingSubscriptionLinkedResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        linked_dataset: Optional[_builtins.str] = ...,
        listing: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedDataset")
    def linked_dataset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def listing(self) -> Optional[_builtins.str]: ...
