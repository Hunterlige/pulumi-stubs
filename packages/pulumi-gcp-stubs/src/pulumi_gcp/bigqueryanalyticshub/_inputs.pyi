import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DataExchangeIamBindingConditionArgs",
    "DataExchangeIamBindingConditionArgsDict",
    "DataExchangeIamMemberConditionArgs",
    "DataExchangeIamMemberConditionArgsDict",
    "DataExchangeSharingEnvironmentConfigArgs",
    "DataExchangeSharingEnvironmentConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "DataExchangeSubscriptionDestinationDatasetArgs",
    "DataExchangeSubscriptionDestinationDatasetArgsDict",
    ...,
    ...,
    "DataExchangeSubscriptionLinkedDatasetMapArgs",
    "DataExchangeSubscriptionLinkedDatasetMapArgsDict",
    "DataExchangeSubscriptionLinkedResourceArgs",
    "DataExchangeSubscriptionLinkedResourceArgsDict",
    "ListingBigqueryDatasetArgs",
    "ListingBigqueryDatasetArgsDict",
    "ListingBigqueryDatasetEffectiveReplicaArgs",
    "ListingBigqueryDatasetEffectiveReplicaArgsDict",
    "ListingBigqueryDatasetSelectedResourceArgs",
    "ListingBigqueryDatasetSelectedResourceArgsDict",
    "ListingCommercialInfoArgs",
    "ListingCommercialInfoArgsDict",
    "ListingCommercialInfoCloudMarketplaceArgs",
    "ListingCommercialInfoCloudMarketplaceArgsDict",
    "ListingDataProviderArgs",
    "ListingDataProviderArgsDict",
    "ListingIamBindingConditionArgs",
    "ListingIamBindingConditionArgsDict",
    "ListingIamMemberConditionArgs",
    "ListingIamMemberConditionArgsDict",
    "ListingPublisherArgs",
    "ListingPublisherArgsDict",
    "ListingPubsubTopicArgs",
    "ListingPubsubTopicArgsDict",
    "ListingRestrictedExportConfigArgs",
    "ListingRestrictedExportConfigArgsDict",
    "ListingSubscriptionCommercialInfoArgs",
    "ListingSubscriptionCommercialInfoArgsDict",
    ...,
    ...,
    "ListingSubscriptionDestinationDatasetArgs",
    "ListingSubscriptionDestinationDatasetArgsDict",
    ...,
    ...,
    "ListingSubscriptionLinkedDatasetMapArgs",
    "ListingSubscriptionLinkedDatasetMapArgsDict",
    "ListingSubscriptionLinkedResourceArgs",
    "ListingSubscriptionLinkedResourceArgsDict",
]

class DataExchangeIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataExchangeIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataExchangeIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataExchangeIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataExchangeSharingEnvironmentConfigArgsDict(TypedDict):
    dcr_exchange_config: NotRequired[
        pulumi.Input[DataExchangeSharingEnvironmentConfigDcrExchangeConfigArgsDict]
    ]
    default_exchange_config: NotRequired[
        pulumi.Input[DataExchangeSharingEnvironmentConfigDefaultExchangeConfigArgsDict]
    ]

@pulumi.input_type
class DataExchangeSharingEnvironmentConfigArgs:
    def __init__(
        __self__,
        *,
        dcr_exchange_config: Optional[
            pulumi.Input[DataExchangeSharingEnvironmentConfigDcrExchangeConfigArgs]
        ] = ...,
        default_exchange_config: Optional[
            pulumi.Input[DataExchangeSharingEnvironmentConfigDefaultExchangeConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dcrExchangeConfig")
    def dcr_exchange_config(
        self,
    ) -> Optional[
        pulumi.Input[DataExchangeSharingEnvironmentConfigDcrExchangeConfigArgs]
    ]: ...
    @dcr_exchange_config.setter
    def dcr_exchange_config(
        self,
        value: Optional[
            pulumi.Input[DataExchangeSharingEnvironmentConfigDcrExchangeConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultExchangeConfig")
    def default_exchange_config(
        self,
    ) -> Optional[
        pulumi.Input[DataExchangeSharingEnvironmentConfigDefaultExchangeConfigArgs]
    ]: ...
    @default_exchange_config.setter
    def default_exchange_config(
        self,
        value: Optional[
            pulumi.Input[DataExchangeSharingEnvironmentConfigDefaultExchangeConfigArgs]
        ],
    ): ...

class DataExchangeSharingEnvironmentConfigDcrExchangeConfigArgsDict(TypedDict): ...

@pulumi.input_type
class DataExchangeSharingEnvironmentConfigDcrExchangeConfigArgs:
    def __init__(__self__) -> None: ...

class DataExchangeSharingEnvironmentConfigDefaultExchangeConfigArgsDict(TypedDict): ...

@pulumi.input_type
class DataExchangeSharingEnvironmentConfigDefaultExchangeConfigArgs:
    def __init__(__self__) -> None: ...

class DataExchangeSubscriptionDestinationDatasetArgsDict(TypedDict):
    dataset_reference: pulumi.Input[
        DataExchangeSubscriptionDestinationDatasetDatasetReferenceArgsDict
    ]
    location: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DataExchangeSubscriptionDestinationDatasetArgs:
    def __init__(
        __self__,
        *,
        dataset_reference: pulumi.Input[
            DataExchangeSubscriptionDestinationDatasetDatasetReferenceArgs
        ],
        location: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetReference")
    def dataset_reference(
        self,
    ) -> pulumi.Input[
        DataExchangeSubscriptionDestinationDatasetDatasetReferenceArgs
    ]: ...
    @dataset_reference.setter
    def dataset_reference(
        self,
        value: pulumi.Input[
            DataExchangeSubscriptionDestinationDatasetDatasetReferenceArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class DataExchangeSubscriptionDestinationDatasetDatasetReferenceArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class DataExchangeSubscriptionDestinationDatasetDatasetReferenceArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class DataExchangeSubscriptionLinkedDatasetMapArgsDict(TypedDict):
    resource_name: pulumi.Input[_builtins.str]
    linked_dataset: NotRequired[pulumi.Input[_builtins.str]]
    linked_pubsub_subscription: NotRequired[pulumi.Input[_builtins.str]]
    listing: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataExchangeSubscriptionLinkedDatasetMapArgs:
    def __init__(
        __self__,
        *,
        resource_name: pulumi.Input[_builtins.str],
        linked_dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_pubsub_subscription: Optional[pulumi.Input[_builtins.str]] = ...,
        listing: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="linkedDataset")
    def linked_dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_dataset.setter
    def linked_dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedPubsubSubscription")
    def linked_pubsub_subscription(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_pubsub_subscription.setter
    def linked_pubsub_subscription(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def listing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @listing.setter
    def listing(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataExchangeSubscriptionLinkedResourceArgsDict(TypedDict):
    linked_dataset: NotRequired[pulumi.Input[_builtins.str]]
    listing: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataExchangeSubscriptionLinkedResourceArgs:
    def __init__(
        __self__,
        *,
        linked_dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        listing: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedDataset")
    def linked_dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_dataset.setter
    def linked_dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def listing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @listing.setter
    def listing(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingBigqueryDatasetArgsDict(TypedDict):
    dataset: pulumi.Input[_builtins.str]
    effective_replicas: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ListingBigqueryDatasetEffectiveReplicaArgsDict]]
        ]
    ]
    replica_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    selected_resources: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ListingBigqueryDatasetSelectedResourceArgsDict]]
        ]
    ]

@pulumi.input_type
class ListingBigqueryDatasetArgs:
    def __init__(
        __self__,
        *,
        dataset: pulumi.Input[_builtins.str],
        effective_replicas: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ListingBigqueryDatasetEffectiveReplicaArgs]]
            ]
        ] = ...,
        replica_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        selected_resources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ListingBigqueryDatasetSelectedResourceArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> pulumi.Input[_builtins.str]: ...
    @dataset.setter
    def dataset(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveReplicas")
    def effective_replicas(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ListingBigqueryDatasetEffectiveReplicaArgs]]]
    ]: ...
    @effective_replicas.setter
    def effective_replicas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ListingBigqueryDatasetEffectiveReplicaArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaLocations")
    def replica_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @replica_locations.setter
    def replica_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectedResources")
    def selected_resources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ListingBigqueryDatasetSelectedResourceArgs]]]
    ]: ...
    @selected_resources.setter
    def selected_resources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ListingBigqueryDatasetSelectedResourceArgs]]
            ]
        ],
    ): ...

class ListingBigqueryDatasetEffectiveReplicaArgsDict(TypedDict):
    location: NotRequired[pulumi.Input[_builtins.str]]
    primary_state: NotRequired[pulumi.Input[_builtins.str]]
    replica_state: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingBigqueryDatasetEffectiveReplicaArgs:
    def __init__(
        __self__,
        *,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_state: Optional[pulumi.Input[_builtins.str]] = ...,
        replica_state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryState")
    def primary_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_state.setter
    def primary_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="replicaState")
    def replica_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @replica_state.setter
    def replica_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingBigqueryDatasetSelectedResourceArgsDict(TypedDict):
    routine: NotRequired[pulumi.Input[_builtins.str]]
    table: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingBigqueryDatasetSelectedResourceArgs:
    def __init__(
        __self__,
        *,
        routine: Optional[pulumi.Input[_builtins.str]] = ...,
        table: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def routine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @routine.setter
    def routine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @table.setter
    def table(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingCommercialInfoArgsDict(TypedDict):
    cloud_marketplaces: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ListingCommercialInfoCloudMarketplaceArgsDict]]
        ]
    ]

@pulumi.input_type
class ListingCommercialInfoArgs:
    def __init__(
        __self__,
        *,
        cloud_marketplaces: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ListingCommercialInfoCloudMarketplaceArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudMarketplaces")
    def cloud_marketplaces(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ListingCommercialInfoCloudMarketplaceArgs]]]
    ]: ...
    @cloud_marketplaces.setter
    def cloud_marketplaces(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ListingCommercialInfoCloudMarketplaceArgs]]
            ]
        ],
    ): ...

class ListingCommercialInfoCloudMarketplaceArgsDict(TypedDict):
    commercial_state: NotRequired[pulumi.Input[_builtins.str]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingCommercialInfoCloudMarketplaceArgs:
    def __init__(
        __self__,
        *,
        commercial_state: Optional[pulumi.Input[_builtins.str]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commercialState")
    def commercial_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commercial_state.setter
    def commercial_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingDataProviderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    primary_contact: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingDataProviderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        primary_contact: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_contact.setter
    def primary_contact(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingPublisherArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    primary_contact: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingPublisherArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        primary_contact: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_contact.setter
    def primary_contact(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingPubsubTopicArgsDict(TypedDict):
    topic: pulumi.Input[_builtins.str]
    data_affinity_regions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ListingPubsubTopicArgs:
    def __init__(
        __self__,
        *,
        topic: pulumi.Input[_builtins.str],
        data_affinity_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> pulumi.Input[_builtins.str]: ...
    @topic.setter
    def topic(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataAffinityRegions")
    def data_affinity_regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @data_affinity_regions.setter
    def data_affinity_regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ListingRestrictedExportConfigArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    restrict_direct_table_access: NotRequired[pulumi.Input[_builtins.bool]]
    restrict_query_result: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ListingRestrictedExportConfigArgs:
    def __init__(
        __self__,
        *,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        restrict_direct_table_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        restrict_query_result: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="restrictDirectTableAccess")
    def restrict_direct_table_access(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @restrict_direct_table_access.setter
    def restrict_direct_table_access(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="restrictQueryResult")
    def restrict_query_result(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @restrict_query_result.setter
    def restrict_query_result(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ListingSubscriptionCommercialInfoArgsDict(TypedDict):
    cloud_marketplaces: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ListingSubscriptionCommercialInfoCloudMarketplaceArgsDict]
            ]
        ]
    ]

@pulumi.input_type
class ListingSubscriptionCommercialInfoArgs:
    def __init__(
        __self__,
        *,
        cloud_marketplaces: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ListingSubscriptionCommercialInfoCloudMarketplaceArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudMarketplaces")
    def cloud_marketplaces(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ListingSubscriptionCommercialInfoCloudMarketplaceArgs]
            ]
        ]
    ]: ...
    @cloud_marketplaces.setter
    def cloud_marketplaces(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ListingSubscriptionCommercialInfoCloudMarketplaceArgs]
                ]
            ]
        ],
    ): ...

class ListingSubscriptionCommercialInfoCloudMarketplaceArgsDict(TypedDict):
    order: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingSubscriptionCommercialInfoCloudMarketplaceArgs:
    def __init__(
        __self__, *, order: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingSubscriptionDestinationDatasetArgsDict(TypedDict):
    dataset_reference: pulumi.Input[
        ListingSubscriptionDestinationDatasetDatasetReferenceArgsDict
    ]
    location: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    friendly_name: NotRequired[pulumi.Input[_builtins.str]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    replica_locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ListingSubscriptionDestinationDatasetArgs:
    def __init__(
        __self__,
        *,
        dataset_reference: pulumi.Input[
            ListingSubscriptionDestinationDatasetDatasetReferenceArgs
        ],
        location: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        friendly_name: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        replica_locations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetReference")
    def dataset_reference(
        self,
    ) -> pulumi.Input[ListingSubscriptionDestinationDatasetDatasetReferenceArgs]: ...
    @dataset_reference.setter
    def dataset_reference(
        self,
        value: pulumi.Input[ListingSubscriptionDestinationDatasetDatasetReferenceArgs],
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="replicaLocations")
    def replica_locations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @replica_locations.setter
    def replica_locations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ListingSubscriptionDestinationDatasetDatasetReferenceArgsDict(TypedDict):
    dataset_id: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ListingSubscriptionDestinationDatasetDatasetReferenceArgs:
    def __init__(
        __self__,
        *,
        dataset_id: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]: ...
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...

class ListingSubscriptionLinkedDatasetMapArgsDict(TypedDict):
    resource_name: pulumi.Input[_builtins.str]
    linked_dataset: NotRequired[pulumi.Input[_builtins.str]]
    listing: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingSubscriptionLinkedDatasetMapArgs:
    def __init__(
        __self__,
        *,
        resource_name: pulumi.Input[_builtins.str],
        linked_dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        listing: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_name.setter
    def resource_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="linkedDataset")
    def linked_dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_dataset.setter
    def linked_dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def listing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @listing.setter
    def listing(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ListingSubscriptionLinkedResourceArgsDict(TypedDict):
    linked_dataset: NotRequired[pulumi.Input[_builtins.str]]
    listing: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ListingSubscriptionLinkedResourceArgs:
    def __init__(
        __self__,
        *,
        linked_dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        listing: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="linkedDataset")
    def linked_dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @linked_dataset.setter
    def linked_dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def listing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @listing.setter
    def listing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
