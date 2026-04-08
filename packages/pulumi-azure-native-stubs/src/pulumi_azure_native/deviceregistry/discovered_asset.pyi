import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DiscoveredAssetArgs", "DiscoveredAsset"]

@pulumi.input_type
class DiscoveredAssetArgs:
    def __init__(
        __self__,
        *,
        asset_endpoint_profile_ref: pulumi.Input[_builtins.str],
        discovery_id: pulumi.Input[_builtins.str],
        extended_location: pulumi.Input[ExtendedLocationArgs],
        resource_group_name: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.float],
        datasets: Optional[
            pulumi.Input[Sequence[pulumi.Input[DiscoveredDatasetArgs]]]
        ] = ...,
        default_datasets_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        default_events_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        default_topic: Optional[pulumi.Input[TopicArgs]] = ...,
        discovered_asset_name: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        events: Optional[
            pulumi.Input[Sequence[pulumi.Input[DiscoveredEventArgs]]]
        ] = ...,
        hardware_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        manufacturer: Optional[pulumi.Input[_builtins.str]] = ...,
        manufacturer_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        product_code: Optional[pulumi.Input[_builtins.str]] = ...,
        serial_number: Optional[pulumi.Input[_builtins.str]] = ...,
        software_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assetEndpointProfileRef")
    def asset_endpoint_profile_ref(self) -> pulumi.Input[_builtins.str]: ...
    @asset_endpoint_profile_ref.setter
    def asset_endpoint_profile_ref(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="discoveryId")
    def discovery_id(self) -> pulumi.Input[_builtins.str]: ...
    @discovery_id.setter
    def discovery_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input[ExtendedLocationArgs]: ...
    @extended_location.setter
    def extended_location(self, value: pulumi.Input[ExtendedLocationArgs]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.float]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter
    def datasets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DiscoveredDatasetArgs]]]]: ...
    @datasets.setter
    def datasets(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[DiscoveredDatasetArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultDatasetsConfiguration")
    def default_datasets_configuration(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_datasets_configuration.setter
    def default_datasets_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultEventsConfiguration")
    def default_events_configuration(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_events_configuration.setter
    def default_events_configuration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultTopic")
    def default_topic(self) -> Optional[pulumi.Input[TopicArgs]]: ...
    @default_topic.setter
    def default_topic(self, value: Optional[pulumi.Input[TopicArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="discoveredAssetName")
    def discovered_asset_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovered_asset_name.setter
    def discovered_asset_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentationUri")
    def documentation_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @documentation_uri.setter
    def documentation_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DiscoveredEventArgs]]]]: ...
    @events.setter
    def events(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DiscoveredEventArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hardwareRevision")
    def hardware_revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @hardware_revision.setter
    def hardware_revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def manufacturer(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manufacturer.setter
    def manufacturer(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manufacturerUri")
    def manufacturer_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manufacturer_uri.setter
    def manufacturer_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @product_code.setter
    def product_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="softwareRevision")
    def software_revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @software_revision.setter
    def software_revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:deviceregistry:DiscoveredAsset")
class DiscoveredAsset(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        asset_endpoint_profile_ref: Optional[pulumi.Input[_builtins.str]] = ...,
        datasets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[DiscoveredDatasetArgs, DiscoveredDatasetArgsDict]
                    ]
                ]
            ]
        ] = ...,
        default_datasets_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        default_events_configuration: Optional[pulumi.Input[_builtins.str]] = ...,
        default_topic: Optional[pulumi.Input[Union[TopicArgs, TopicArgsDict]]] = ...,
        discovered_asset_name: Optional[pulumi.Input[_builtins.str]] = ...,
        discovery_id: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        events: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[DiscoveredEventArgs, DiscoveredEventArgsDict]]
                ]
            ]
        ] = ...,
        extended_location: Optional[
            pulumi.Input[Union[ExtendedLocationArgs, ExtendedLocationArgsDict]]
        ] = ...,
        hardware_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        manufacturer: Optional[pulumi.Input[_builtins.str]] = ...,
        manufacturer_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        product_code: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        serial_number: Optional[pulumi.Input[_builtins.str]] = ...,
        software_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        version: Optional[pulumi.Input[_builtins.float]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DiscoveredAssetArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> DiscoveredAsset: ...
    @_builtins.property
    @pulumi.getter(name="assetEndpointProfileRef")
    def asset_endpoint_profile_ref(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def datasets(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DiscoveredDatasetResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultDatasetsConfiguration")
    def default_datasets_configuration(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultEventsConfiguration")
    def default_events_configuration(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultTopic")
    def default_topic(self) -> pulumi.Output[Optional[outputs.TopicResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryId")
    def discovery_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentationUri")
    def documentation_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def events(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.DiscoveredEventResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[outputs.ExtendedLocationResponse]: ...
    @_builtins.property
    @pulumi.getter(name="hardwareRevision")
    def hardware_revision(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def manufacturer(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="manufacturerUri")
    def manufacturer_uri(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="softwareRevision")
    def software_revision(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output[outputs.SystemDataResponse]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.float]: ...
