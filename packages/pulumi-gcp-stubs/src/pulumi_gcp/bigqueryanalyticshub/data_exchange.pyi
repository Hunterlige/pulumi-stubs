import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["DataExchangeArgs", "DataExchange"]

@pulumi.input_type
class DataExchangeArgs:
    def __init__(
        __self__,
        *,
        data_exchange_id: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        discovery_type: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation: Optional[pulumi.Input[_builtins.str]] = ...,
        icon: Optional[pulumi.Input[_builtins.str]] = ...,
        log_linked_dataset_query_user_email: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        primary_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        sharing_environment_config: Optional[
            pulumi.Input[DataExchangeSharingEnvironmentConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> pulumi.Input[_builtins.str]: ...
    @data_exchange_id.setter
    def data_exchange_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
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
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovery_type.setter
    def discovery_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @documentation.setter
    def documentation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @icon.setter
    def icon(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_contact.setter
    def primary_contact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharingEnvironmentConfig")
    def sharing_environment_config(
        self,
    ) -> Optional[pulumi.Input[DataExchangeSharingEnvironmentConfigArgs]]: ...
    @sharing_environment_config.setter
    def sharing_environment_config(
        self, value: Optional[pulumi.Input[DataExchangeSharingEnvironmentConfigArgs]]
    ): ...

@pulumi.input_type
class _DataExchangeState:
    def __init__(
        __self__,
        *,
        data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        discovery_type: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation: Optional[pulumi.Input[_builtins.str]] = ...,
        icon: Optional[pulumi.Input[_builtins.str]] = ...,
        listing_count: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_linked_dataset_query_user_email: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        sharing_environment_config: Optional[
            pulumi.Input[DataExchangeSharingEnvironmentConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_exchange_id.setter
    def data_exchange_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @discovery_type.setter
    def discovery_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @documentation.setter
    def documentation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @icon.setter
    def icon(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="listingCount")
    def listing_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @listing_count.setter
    def listing_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_contact.setter
    def primary_contact(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharingEnvironmentConfig")
    def sharing_environment_config(
        self,
    ) -> Optional[pulumi.Input[DataExchangeSharingEnvironmentConfigArgs]]: ...
    @sharing_environment_config.setter
    def sharing_environment_config(
        self, value: Optional[pulumi.Input[DataExchangeSharingEnvironmentConfigArgs]]
    ): ...

@pulumi.type_token("gcp:bigqueryanalyticshub/dataExchange:DataExchange")
class DataExchange(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        discovery_type: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation: Optional[pulumi.Input[_builtins.str]] = ...,
        icon: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_linked_dataset_query_user_email: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        primary_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        sharing_environment_config: Optional[
            pulumi.Input[
                Union[
                    DataExchangeSharingEnvironmentConfigArgs,
                    DataExchangeSharingEnvironmentConfigArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: DataExchangeArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_exchange_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        discovery_type: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        documentation: Optional[pulumi.Input[_builtins.str]] = ...,
        icon: Optional[pulumi.Input[_builtins.str]] = ...,
        listing_count: Optional[pulumi.Input[_builtins.int]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        log_linked_dataset_query_user_email: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_contact: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        sharing_environment_config: Optional[
            pulumi.Input[
                Union[
                    DataExchangeSharingEnvironmentConfigArgs,
                    DataExchangeSharingEnvironmentConfigArgsDict,
                ]
            ]
        ] = ...,
    ) -> DataExchange: ...
    @_builtins.property
    @pulumi.getter(name="dataExchangeId")
    def data_exchange_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="discoveryType")
    def discovery_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def documentation(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def icon(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="listingCount")
    def listing_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="logLinkedDatasetQueryUserEmail")
    def log_linked_dataset_query_user_email(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryContact")
    def primary_contact(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sharingEnvironmentConfig")
    def sharing_environment_config(
        self,
    ) -> pulumi.Output[outputs.DataExchangeSharingEnvironmentConfig]: ...
