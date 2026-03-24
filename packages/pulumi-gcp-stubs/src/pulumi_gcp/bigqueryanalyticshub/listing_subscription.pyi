import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ListingSubscriptionArgs", "ListingSubscription"]

@pulumi.input_type
class ListingSubscriptionArgs:
    def __init__(
        __self__,
        *,
        data_exchange_id: pulumi.Input[_builtins.str],
        destination_dataset: pulumi.Input[ListingSubscriptionDestinationDatasetArgs],
        listing_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_exchange_id.setter
    def data_exchange_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationDataset")
    def destination_dataset(
        self,
    ) -> pulumi.Input[ListingSubscriptionDestinationDatasetArgs]: ...
    @destination_dataset.setter
    def destination_dataset(
        self, value: pulumi.Input[ListingSubscriptionDestinationDatasetArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> pulumi.Input[_builtins.str]: ...
    @listing_id.setter
    def listing_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _ListingSubscriptionState:
    def __init__(
        __self__,
        *,
        commercial_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[ListingSubscriptionCommercialInfoArgs]]]
        ] = ...,
        creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_dataset: Optional[
            pulumi.Input[ListingSubscriptionDestinationDatasetArgs]
        ] = ...,
        last_modify_time: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_dataset_maps: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ListingSubscriptionLinkedDatasetMapArgs]]
            ]
        ] = ...,
        linked_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[ListingSubscriptionLinkedResourceArgs]]]
        ] = ...,
        listing_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_linked_dataset_query_user_email: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subscriber_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="commercialInfos")
    def commercial_infos(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ListingSubscriptionCommercialInfoArgs]]]
    ]: ...
    @commercial_infos.setter
    def commercial_infos(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ListingSubscriptionCommercialInfoArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_exchange_id.setter
    def data_exchange_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationDataset")
    def destination_dataset(
        self,
    ) -> Optional[pulumi.Input[ListingSubscriptionDestinationDatasetArgs]]: ...
    @destination_dataset.setter
    def destination_dataset(
        self, value: Optional[pulumi.Input[ListingSubscriptionDestinationDatasetArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastModifyTime")
    def last_modify_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modify_time.setter
    def last_modify_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="linkedDatasetMaps")
    def linked_dataset_maps(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ListingSubscriptionLinkedDatasetMapArgs]]]
    ]: ...
    @linked_dataset_maps.setter
    def linked_dataset_maps(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ListingSubscriptionLinkedDatasetMapArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="linkedResources")
    def linked_resources(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ListingSubscriptionLinkedResourceArgs]]]
    ]: ...
    @linked_resources.setter
    def linked_resources(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ListingSubscriptionLinkedResourceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @listing_id.setter
    def listing_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logLinkedDatasetQueryUserEmail")
    def log_linked_dataset_query_user_email(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @log_linked_dataset_query_user_email.setter
    def log_linked_dataset_query_user_email(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="organizationDisplayName")
    def organization_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization_display_name.setter
    def organization_display_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriberContact")
    def subscriber_contact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscriber_contact.setter
    def subscriber_contact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class ListingSubscription(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_dataset: Optional[
            pulumi.Input[
                Union[
                    ListingSubscriptionDestinationDatasetArgs,
                    ListingSubscriptionDestinationDatasetArgsDict,
                ]
            ]
        ] = ...,
        listing_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ListingSubscriptionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        commercial_infos: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ListingSubscriptionCommercialInfoArgs,
                            ListingSubscriptionCommercialInfoArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        creation_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_dataset: Optional[
            pulumi.Input[
                Union[
                    ListingSubscriptionDestinationDatasetArgs,
                    ListingSubscriptionDestinationDatasetArgsDict,
                ]
            ]
        ] = ...,
        last_modify_time: Optional[pulumi.Input[_builtins.str]] = ...,
        linked_dataset_maps: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ListingSubscriptionLinkedDatasetMapArgs,
                            ListingSubscriptionLinkedDatasetMapArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        linked_resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ListingSubscriptionLinkedResourceArgs,
                            ListingSubscriptionLinkedResourceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        listing_id: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_linked_dataset_query_user_email: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        subscriber_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        subscription_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ListingSubscription: ...
    @_builtins.property
    @pulumi.getter(name="commercialInfos")
    def commercial_infos(
        self,
    ) -> pulumi.Output[Sequence[outputs.ListingSubscriptionCommercialInfo]]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationDataset")
    def destination_dataset(
        self,
    ) -> pulumi.Output[outputs.ListingSubscriptionDestinationDataset]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifyTime")
    def last_modify_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="linkedDatasetMaps")
    def linked_dataset_maps(
        self,
    ) -> pulumi.Output[Sequence[outputs.ListingSubscriptionLinkedDatasetMap]]: ...
    @_builtins.property
    @pulumi.getter(name="linkedResources")
    def linked_resources(
        self,
    ) -> pulumi.Output[Sequence[outputs.ListingSubscriptionLinkedResource]]: ...
    @_builtins.property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logLinkedDatasetQueryUserEmail")
    def log_linked_dataset_query_user_email(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationDisplayName")
    def organization_display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriberContact")
    def subscriber_contact(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[_builtins.str]: ...
