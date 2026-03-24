

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListingArgs', 'Listing']
@pulumi.input_type
class ListingArgs:
    def __init__(__self__, *, data_exchange_id: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], listing_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], allow_only_metadata_sharing: Optional[pulumi.Input[_builtins.bool]] = ..., bigquery_dataset: Optional[pulumi.Input[ListingBigqueryDatasetArgs]] = ..., categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., data_provider: Optional[pulumi.Input[ListingDataProviderArgs]] = ..., delete_commercial: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovery_type: Optional[pulumi.Input[_builtins.str]] = ..., documentation: Optional[pulumi.Input[_builtins.str]] = ..., icon: Optional[pulumi.Input[_builtins.str]] = ..., log_linked_dataset_query_user_email: Optional[pulumi.Input[_builtins.bool]] = ..., primary_contact: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[ListingPublisherArgs]] = ..., pubsub_topic: Optional[pulumi.Input[ListingPubsubTopicArgs]] = ..., request_access: Optional[pulumi.Input[_builtins.str]] = ..., restricted_export_config: Optional[pulumi.Input[ListingRestrictedExportConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_exchange_id.setter
    def data_exchange_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @listing_id.setter
    def listing_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowOnlyMetadataSharing")
    def allow_only_metadata_sharing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_only_metadata_sharing.setter
    def allow_only_metadata_sharing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDataset")
    def bigquery_dataset(self) -> Optional[pulumi.Input[ListingBigqueryDatasetArgs]]:
        
        ...
    
    @bigquery_dataset.setter
    def bigquery_dataset(self, value: Optional[pulumi.Input[ListingBigqueryDatasetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProvider")
    def data_provider(self) -> Optional[pulumi.Input[ListingDataProviderArgs]]:
        
        ...
    
    @data_provider.setter
    def data_provider(self, value: Optional[pulumi.Input[ListingDataProviderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteCommercial")
    def delete_commercial(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_commercial.setter
    def delete_commercial(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @discovery_type.setter
    def discovery_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @documentation.setter
    def documentation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @icon.setter
    def icon(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLinkedDatasetQueryUserEmail")
    def log_linked_dataset_query_user_email(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_linked_dataset_query_user_email.setter
    def log_linked_dataset_query_user_email(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_contact.setter
    def primary_contact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[ListingPublisherArgs]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[ListingPublisherArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> Optional[pulumi.Input[ListingPubsubTopicArgs]]:
        
        ...
    
    @pubsub_topic.setter
    def pubsub_topic(self, value: Optional[pulumi.Input[ListingPubsubTopicArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestAccess")
    def request_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_access.setter
    def request_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictedExportConfig")
    def restricted_export_config(self) -> Optional[pulumi.Input[ListingRestrictedExportConfigArgs]]:
        
        ...
    
    @restricted_export_config.setter
    def restricted_export_config(self, value: Optional[pulumi.Input[ListingRestrictedExportConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ListingState:
    def __init__(__self__, *, allow_only_metadata_sharing: Optional[pulumi.Input[_builtins.bool]] = ..., bigquery_dataset: Optional[pulumi.Input[ListingBigqueryDatasetArgs]] = ..., categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., commercial_infos: Optional[pulumi.Input[Sequence[pulumi.Input[ListingCommercialInfoArgs]]]] = ..., data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ..., data_provider: Optional[pulumi.Input[ListingDataProviderArgs]] = ..., delete_commercial: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovery_type: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., documentation: Optional[pulumi.Input[_builtins.str]] = ..., icon: Optional[pulumi.Input[_builtins.str]] = ..., listing_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., log_linked_dataset_query_user_email: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., primary_contact: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[ListingPublisherArgs]] = ..., pubsub_topic: Optional[pulumi.Input[ListingPubsubTopicArgs]] = ..., request_access: Optional[pulumi.Input[_builtins.str]] = ..., restricted_export_config: Optional[pulumi.Input[ListingRestrictedExportConfigArgs]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowOnlyMetadataSharing")
    def allow_only_metadata_sharing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_only_metadata_sharing.setter
    def allow_only_metadata_sharing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDataset")
    def bigquery_dataset(self) -> Optional[pulumi.Input[ListingBigqueryDatasetArgs]]:
        
        ...
    
    @bigquery_dataset.setter
    def bigquery_dataset(self, value: Optional[pulumi.Input[ListingBigqueryDatasetArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="commercialInfos")
    def commercial_infos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ListingCommercialInfoArgs]]]]:
        
        ...
    
    @commercial_infos.setter
    def commercial_infos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ListingCommercialInfoArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_exchange_id.setter
    def data_exchange_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProvider")
    def data_provider(self) -> Optional[pulumi.Input[ListingDataProviderArgs]]:
        
        ...
    
    @data_provider.setter
    def data_provider(self, value: Optional[pulumi.Input[ListingDataProviderArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteCommercial")
    def delete_commercial(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_commercial.setter
    def delete_commercial(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @discovery_type.setter
    def discovery_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @documentation.setter
    def documentation(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @icon.setter
    def icon(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @listing_id.setter
    def listing_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLinkedDatasetQueryUserEmail")
    def log_linked_dataset_query_user_email(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @log_linked_dataset_query_user_email.setter
    def log_linked_dataset_query_user_email(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @primary_contact.setter
    def primary_contact(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[ListingPublisherArgs]]:
        
        ...
    
    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[ListingPublisherArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> Optional[pulumi.Input[ListingPubsubTopicArgs]]:
        
        ...
    
    @pubsub_topic.setter
    def pubsub_topic(self, value: Optional[pulumi.Input[ListingPubsubTopicArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestAccess")
    def request_access(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_access.setter
    def request_access(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictedExportConfig")
    def restricted_export_config(self) -> Optional[pulumi.Input[ListingRestrictedExportConfigArgs]]:
        
        ...
    
    @restricted_export_config.setter
    def restricted_export_config(self, value: Optional[pulumi.Input[ListingRestrictedExportConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:bigqueryanalyticshub/listing:Listing")
class Listing(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., allow_only_metadata_sharing: Optional[pulumi.Input[_builtins.bool]] = ..., bigquery_dataset: Optional[pulumi.Input[Union[ListingBigqueryDatasetArgs, ListingBigqueryDatasetArgsDict]]] = ..., categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ..., data_provider: Optional[pulumi.Input[Union[ListingDataProviderArgs, ListingDataProviderArgsDict]]] = ..., delete_commercial: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovery_type: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., documentation: Optional[pulumi.Input[_builtins.str]] = ..., icon: Optional[pulumi.Input[_builtins.str]] = ..., listing_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., log_linked_dataset_query_user_email: Optional[pulumi.Input[_builtins.bool]] = ..., primary_contact: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[Union[ListingPublisherArgs, ListingPublisherArgsDict]]] = ..., pubsub_topic: Optional[pulumi.Input[Union[ListingPubsubTopicArgs, ListingPubsubTopicArgsDict]]] = ..., request_access: Optional[pulumi.Input[_builtins.str]] = ..., restricted_export_config: Optional[pulumi.Input[Union[ListingRestrictedExportConfigArgs, ListingRestrictedExportConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ListingArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., allow_only_metadata_sharing: Optional[pulumi.Input[_builtins.bool]] = ..., bigquery_dataset: Optional[pulumi.Input[Union[ListingBigqueryDatasetArgs, ListingBigqueryDatasetArgsDict]]] = ..., categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., commercial_infos: Optional[pulumi.Input[Sequence[pulumi.Input[Union[ListingCommercialInfoArgs, ListingCommercialInfoArgsDict]]]]] = ..., data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ..., data_provider: Optional[pulumi.Input[Union[ListingDataProviderArgs, ListingDataProviderArgsDict]]] = ..., delete_commercial: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., discovery_type: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., documentation: Optional[pulumi.Input[_builtins.str]] = ..., icon: Optional[pulumi.Input[_builtins.str]] = ..., listing_id: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., log_linked_dataset_query_user_email: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., primary_contact: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., publisher: Optional[pulumi.Input[Union[ListingPublisherArgs, ListingPublisherArgsDict]]] = ..., pubsub_topic: Optional[pulumi.Input[Union[ListingPubsubTopicArgs, ListingPubsubTopicArgsDict]]] = ..., request_access: Optional[pulumi.Input[_builtins.str]] = ..., restricted_export_config: Optional[pulumi.Input[Union[ListingRestrictedExportConfigArgs, ListingRestrictedExportConfigArgsDict]]] = ..., state: Optional[pulumi.Input[_builtins.str]] = ...) -> Listing:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowOnlyMetadataSharing")
    def allow_only_metadata_sharing(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDataset")
    def bigquery_dataset(self) -> pulumi.Output[Optional[outputs.ListingBigqueryDataset]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commercialInfos")
    def commercial_infos(self) -> pulumi.Output[Sequence[outputs.ListingCommercialInfo]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProvider")
    def data_provider(self) -> pulumi.Output[Optional[outputs.ListingDataProvider]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteCommercial")
    def delete_commercial(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def icon(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="listingId")
    def listing_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logLinkedDatasetQueryUserEmail")
    def log_linked_dataset_query_user_email(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def publisher(self) -> pulumi.Output[Optional[outputs.ListingPublisher]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> pulumi.Output[Optional[outputs.ListingPubsubTopic]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestAccess")
    def request_access(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="restrictedExportConfig")
    def restricted_export_config(self) -> pulumi.Output[Optional[outputs.ListingRestrictedExportConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


