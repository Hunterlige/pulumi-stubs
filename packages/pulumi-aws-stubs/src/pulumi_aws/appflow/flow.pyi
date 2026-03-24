import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["FlowArgs", "Flow"]

@pulumi.input_type
class FlowArgs:
    def __init__(
        __self__,
        *,
        destination_flow_configs: pulumi.Input[
            Sequence[pulumi.Input[FlowDestinationFlowConfigArgs]]
        ],
        source_flow_config: pulumi.Input[FlowSourceFlowConfigArgs],
        tasks: pulumi.Input[Sequence[pulumi.Input[FlowTaskArgs]]],
        trigger_config: pulumi.Input[FlowTriggerConfigArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_catalog_config: Optional[
            pulumi.Input[FlowMetadataCatalogConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationFlowConfigs")
    def destination_flow_configs(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[FlowDestinationFlowConfigArgs]]]: ...
    @destination_flow_configs.setter
    def destination_flow_configs(
        self, value: pulumi.Input[Sequence[pulumi.Input[FlowDestinationFlowConfigArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceFlowConfig")
    def source_flow_config(self) -> pulumi.Input[FlowSourceFlowConfigArgs]: ...
    @source_flow_config.setter
    def source_flow_config(self, value: pulumi.Input[FlowSourceFlowConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def tasks(self) -> pulumi.Input[Sequence[pulumi.Input[FlowTaskArgs]]]: ...
    @tasks.setter
    def tasks(self, value: pulumi.Input[Sequence[pulumi.Input[FlowTaskArgs]]]): ...
    @_builtins.property
    @pulumi.getter(name="triggerConfig")
    def trigger_config(self) -> pulumi.Input[FlowTriggerConfigArgs]: ...
    @trigger_config.setter
    def trigger_config(self, value: pulumi.Input[FlowTriggerConfigArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_arn.setter
    def kms_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataCatalogConfig")
    def metadata_catalog_config(
        self,
    ) -> Optional[pulumi.Input[FlowMetadataCatalogConfigArgs]]: ...
    @metadata_catalog_config.setter
    def metadata_catalog_config(
        self, value: Optional[pulumi.Input[FlowMetadataCatalogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.input_type
class _FlowState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_flow_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[FlowDestinationFlowConfigArgs]]]
        ] = ...,
        flow_status: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_catalog_config: Optional[
            pulumi.Input[FlowMetadataCatalogConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_flow_config: Optional[pulumi.Input[FlowSourceFlowConfigArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tasks: Optional[pulumi.Input[Sequence[pulumi.Input[FlowTaskArgs]]]] = ...,
        trigger_config: Optional[pulumi.Input[FlowTriggerConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="destinationFlowConfigs")
    def destination_flow_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FlowDestinationFlowConfigArgs]]]
    ]: ...
    @destination_flow_configs.setter
    def destination_flow_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FlowDestinationFlowConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="flowStatus")
    def flow_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flow_status.setter
    def flow_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_arn.setter
    def kms_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="metadataCatalogConfig")
    def metadata_catalog_config(
        self,
    ) -> Optional[pulumi.Input[FlowMetadataCatalogConfigArgs]]: ...
    @metadata_catalog_config.setter
    def metadata_catalog_config(
        self, value: Optional[pulumi.Input[FlowMetadataCatalogConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFlowConfig")
    def source_flow_config(
        self,
    ) -> Optional[pulumi.Input[FlowSourceFlowConfigArgs]]: ...
    @source_flow_config.setter
    def source_flow_config(
        self, value: Optional[pulumi.Input[FlowSourceFlowConfigArgs]]
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
    def tasks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[FlowTaskArgs]]]]: ...
    @tasks.setter
    def tasks(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FlowTaskArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="triggerConfig")
    def trigger_config(self) -> Optional[pulumi.Input[FlowTriggerConfigArgs]]: ...
    @trigger_config.setter
    def trigger_config(self, value: Optional[pulumi.Input[FlowTriggerConfigArgs]]): ...

@pulumi.type_token("aws:appflow/flow:Flow")
class Flow(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_flow_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FlowDestinationFlowConfigArgs,
                            FlowDestinationFlowConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        kms_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_catalog_config: Optional[
            pulumi.Input[
                Union[FlowMetadataCatalogConfigArgs, FlowMetadataCatalogConfigArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_flow_config: Optional[
            pulumi.Input[Union[FlowSourceFlowConfigArgs, FlowSourceFlowConfigArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tasks: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[FlowTaskArgs, FlowTaskArgsDict]]]]
        ] = ...,
        trigger_config: Optional[
            pulumi.Input[Union[FlowTriggerConfigArgs, FlowTriggerConfigArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: FlowArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        destination_flow_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            FlowDestinationFlowConfigArgs,
                            FlowDestinationFlowConfigArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        flow_status: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        metadata_catalog_config: Optional[
            pulumi.Input[
                Union[FlowMetadataCatalogConfigArgs, FlowMetadataCatalogConfigArgsDict]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_flow_config: Optional[
            pulumi.Input[Union[FlowSourceFlowConfigArgs, FlowSourceFlowConfigArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        tasks: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[FlowTaskArgs, FlowTaskArgsDict]]]]
        ] = ...,
        trigger_config: Optional[
            pulumi.Input[Union[FlowTriggerConfigArgs, FlowTriggerConfigArgsDict]]
        ] = ...,
    ) -> Flow: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="destinationFlowConfigs")
    def destination_flow_configs(
        self,
    ) -> pulumi.Output[Sequence[outputs.FlowDestinationFlowConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="flowStatus")
    def flow_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsArn")
    def kms_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="metadataCatalogConfig")
    def metadata_catalog_config(
        self,
    ) -> pulumi.Output[outputs.FlowMetadataCatalogConfig]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceFlowConfig")
    def source_flow_config(self) -> pulumi.Output[outputs.FlowSourceFlowConfig]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tasks(self) -> pulumi.Output[Sequence[outputs.FlowTask]]: ...
    @_builtins.property
    @pulumi.getter(name="triggerConfig")
    def trigger_config(self) -> pulumi.Output[outputs.FlowTriggerConfig]: ...
