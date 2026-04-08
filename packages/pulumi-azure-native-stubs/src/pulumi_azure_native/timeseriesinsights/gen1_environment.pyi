import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["Gen1EnvironmentArgs", "Gen1Environment"]

@pulumi.input_type
class Gen1EnvironmentArgs:
    def __init__(
        __self__,
        *,
        data_retention_time: pulumi.Input[_builtins.str],
        kind: pulumi.Input[_builtins.str],
        resource_group_name: pulumi.Input[_builtins.str],
        sku: pulumi.Input[SkuArgs],
        environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        partition_key_properties: Optional[
            pulumi.Input[Sequence[pulumi.Input[TimeSeriesIdPropertyArgs]]]
        ] = ...,
        storage_limit_exceeded_behavior: Optional[
            pulumi.Input[Union[_builtins.str, StorageLimitExceededBehavior]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataRetentionTime")
    def data_retention_time(self) -> pulumi.Input[_builtins.str]: ...
    @data_retention_time.setter
    def data_retention_time(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]: ...
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[_builtins.str]: ...
    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Input[SkuArgs]: ...
    @sku.setter
    def sku(self, value: pulumi.Input[SkuArgs]): ...
    @_builtins.property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partitionKeyProperties")
    def partition_key_properties(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TimeSeriesIdPropertyArgs]]]]: ...
    @partition_key_properties.setter
    def partition_key_properties(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TimeSeriesIdPropertyArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageLimitExceededBehavior")
    def storage_limit_exceeded_behavior(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, StorageLimitExceededBehavior]]]: ...
    @storage_limit_exceeded_behavior.setter
    def storage_limit_exceeded_behavior(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, StorageLimitExceededBehavior]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("azure-native:timeseriesinsights:Gen1Environment")
class Gen1Environment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        data_retention_time: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_name: Optional[pulumi.Input[_builtins.str]] = ...,
        kind: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        partition_key_properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TimeSeriesIdPropertyArgs, TimeSeriesIdPropertyArgsDict]
                    ]
                ]
            ]
        ] = ...,
        resource_group_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sku: Optional[pulumi.Input[Union[SkuArgs, SkuArgsDict]]] = ...,
        storage_limit_exceeded_behavior: Optional[
            pulumi.Input[Union[_builtins.str, StorageLimitExceededBehavior]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Gen1EnvironmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> Gen1Environment: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessFqdn")
    def data_access_fqdn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessId")
    def data_access_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataRetentionTime")
    def data_retention_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partitionKeyProperties")
    def partition_key_properties(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TimeSeriesIdPropertyResponse]]]: ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def sku(self) -> pulumi.Output[outputs.SkuResponse]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[outputs.EnvironmentStatusResponse]: ...
    @_builtins.property
    @pulumi.getter(name="storageLimitExceededBehavior")
    def storage_limit_exceeded_behavior(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
