import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["IngestionDestinationArgs", "IngestionDestination"]

@pulumi.input_type
class IngestionDestinationArgs:
    def __init__(
        __self__,
        *,
        app_bundle_arn: pulumi.Input[_builtins.str],
        destination_configuration: pulumi.Input[
            IngestionDestinationDestinationConfigurationArgs
        ],
        ingestion_arn: pulumi.Input[_builtins.str],
        processing_configuration: pulumi.Input[
            IngestionDestinationProcessingConfigurationArgs
        ],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[IngestionDestinationTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> pulumi.Input[_builtins.str]: ...
    @app_bundle_arn.setter
    def app_bundle_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> pulumi.Input[IngestionDestinationDestinationConfigurationArgs]: ...
    @destination_configuration.setter
    def destination_configuration(
        self, value: pulumi.Input[IngestionDestinationDestinationConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingestionArn")
    def ingestion_arn(self) -> pulumi.Input[_builtins.str]: ...
    @ingestion_arn.setter
    def ingestion_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> pulumi.Input[IngestionDestinationProcessingConfigurationArgs]: ...
    @processing_configuration.setter
    def processing_configuration(
        self, value: pulumi.Input[IngestionDestinationProcessingConfigurationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[IngestionDestinationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[IngestionDestinationTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _IngestionDestinationState:
    def __init__(
        __self__,
        *,
        app_bundle_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_configuration: Optional[
            pulumi.Input[IngestionDestinationDestinationConfigurationArgs]
        ] = ...,
        ingestion_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        processing_configuration: Optional[
            pulumi.Input[IngestionDestinationProcessingConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[IngestionDestinationTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_bundle_arn.setter
    def app_bundle_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> Optional[pulumi.Input[IngestionDestinationDestinationConfigurationArgs]]: ...
    @destination_configuration.setter
    def destination_configuration(
        self,
        value: Optional[pulumi.Input[IngestionDestinationDestinationConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ingestionArn")
    def ingestion_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingestion_arn.setter
    def ingestion_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> Optional[pulumi.Input[IngestionDestinationProcessingConfigurationArgs]]: ...
    @processing_configuration.setter
    def processing_configuration(
        self,
        value: Optional[pulumi.Input[IngestionDestinationProcessingConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[IngestionDestinationTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[IngestionDestinationTimeoutsArgs]]
    ): ...

@pulumi.type_token(...)
class IngestionDestination(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_bundle_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_configuration: Optional[
            pulumi.Input[
                Union[
                    IngestionDestinationDestinationConfigurationArgs,
                    IngestionDestinationDestinationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        ingestion_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        processing_configuration: Optional[
            pulumi.Input[
                Union[
                    IngestionDestinationProcessingConfigurationArgs,
                    IngestionDestinationProcessingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    IngestionDestinationTimeoutsArgs,
                    IngestionDestinationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: IngestionDestinationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_bundle_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_configuration: Optional[
            pulumi.Input[
                Union[
                    IngestionDestinationDestinationConfigurationArgs,
                    IngestionDestinationDestinationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        ingestion_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        processing_configuration: Optional[
            pulumi.Input[
                Union[
                    IngestionDestinationProcessingConfigurationArgs,
                    IngestionDestinationProcessingConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    IngestionDestinationTimeoutsArgs,
                    IngestionDestinationTimeoutsArgsDict,
                ]
            ]
        ] = ...,
    ) -> IngestionDestination: ...
    @_builtins.property
    @pulumi.getter(name="appBundleArn")
    def app_bundle_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> pulumi.Output[outputs.IngestionDestinationDestinationConfiguration]: ...
    @_builtins.property
    @pulumi.getter(name="ingestionArn")
    def ingestion_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="processingConfiguration")
    def processing_configuration(
        self,
    ) -> pulumi.Output[outputs.IngestionDestinationProcessingConfiguration]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.IngestionDestinationTimeouts]]: ...
