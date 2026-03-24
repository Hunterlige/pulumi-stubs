import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PipeArgs", "Pipe"]

@pulumi.input_type
class PipeArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        source: pulumi.Input[_builtins.str],
        target: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        enrichment: Optional[pulumi.Input[_builtins.str]] = ...,
        enrichment_parameters: Optional[
            pulumi.Input[PipeEnrichmentParametersArgs]
        ] = ...,
        kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        log_configuration: Optional[pulumi.Input[PipeLogConfigurationArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source_parameters: Optional[pulumi.Input[PipeSourceParametersArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target_parameters: Optional[pulumi.Input[PipeTargetParametersArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enrichment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enrichment.setter
    def enrichment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enrichmentParameters")
    def enrichment_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeEnrichmentParametersArgs]]: ...
    @enrichment_parameters.setter
    def enrichment_parameters(
        self, value: Optional[pulumi.Input[PipeEnrichmentParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> Optional[pulumi.Input[PipeLogConfigurationArgs]]: ...
    @log_configuration.setter
    def log_configuration(
        self, value: Optional[pulumi.Input[PipeLogConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceParameters")
    def source_parameters(self) -> Optional[pulumi.Input[PipeSourceParametersArgs]]: ...
    @source_parameters.setter
    def source_parameters(
        self, value: Optional[pulumi.Input[PipeSourceParametersArgs]]
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
    @pulumi.getter(name="targetParameters")
    def target_parameters(self) -> Optional[pulumi.Input[PipeTargetParametersArgs]]: ...
    @target_parameters.setter
    def target_parameters(
        self, value: Optional[pulumi.Input[PipeTargetParametersArgs]]
    ): ...

@pulumi.input_type
class _PipeState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        enrichment: Optional[pulumi.Input[_builtins.str]] = ...,
        enrichment_parameters: Optional[
            pulumi.Input[PipeEnrichmentParametersArgs]
        ] = ...,
        kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        log_configuration: Optional[pulumi.Input[PipeLogConfigurationArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        source_parameters: Optional[pulumi.Input[PipeSourceParametersArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        target_parameters: Optional[pulumi.Input[PipeTargetParametersArgs]] = ...,
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
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @desired_state.setter
    def desired_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enrichment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @enrichment.setter
    def enrichment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enrichmentParameters")
    def enrichment_parameters(
        self,
    ) -> Optional[pulumi.Input[PipeEnrichmentParametersArgs]]: ...
    @enrichment_parameters.setter
    def enrichment_parameters(
        self, value: Optional[pulumi.Input[PipeEnrichmentParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(self) -> Optional[pulumi.Input[PipeLogConfigurationArgs]]: ...
    @log_configuration.setter
    def log_configuration(
        self, value: Optional[pulumi.Input[PipeLogConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceParameters")
    def source_parameters(self) -> Optional[pulumi.Input[PipeSourceParametersArgs]]: ...
    @source_parameters.setter
    def source_parameters(
        self, value: Optional[pulumi.Input[PipeSourceParametersArgs]]
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
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetParameters")
    def target_parameters(self) -> Optional[pulumi.Input[PipeTargetParametersArgs]]: ...
    @target_parameters.setter
    def target_parameters(
        self, value: Optional[pulumi.Input[PipeTargetParametersArgs]]
    ): ...

@pulumi.type_token("aws:pipes/pipe:Pipe")
class Pipe(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        enrichment: Optional[pulumi.Input[_builtins.str]] = ...,
        enrichment_parameters: Optional[
            pulumi.Input[
                Union[PipeEnrichmentParametersArgs, PipeEnrichmentParametersArgsDict]
            ]
        ] = ...,
        kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        log_configuration: Optional[
            pulumi.Input[Union[PipeLogConfigurationArgs, PipeLogConfigurationArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        source_parameters: Optional[
            pulumi.Input[Union[PipeSourceParametersArgs, PipeSourceParametersArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        target_parameters: Optional[
            pulumi.Input[Union[PipeTargetParametersArgs, PipeTargetParametersArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PipeArgs,
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
        desired_state: Optional[pulumi.Input[_builtins.str]] = ...,
        enrichment: Optional[pulumi.Input[_builtins.str]] = ...,
        enrichment_parameters: Optional[
            pulumi.Input[
                Union[PipeEnrichmentParametersArgs, PipeEnrichmentParametersArgsDict]
            ]
        ] = ...,
        kms_key_identifier: Optional[pulumi.Input[_builtins.str]] = ...,
        log_configuration: Optional[
            pulumi.Input[Union[PipeLogConfigurationArgs, PipeLogConfigurationArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        name_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[_builtins.str]] = ...,
        source_parameters: Optional[
            pulumi.Input[Union[PipeSourceParametersArgs, PipeSourceParametersArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        target_parameters: Optional[
            pulumi.Input[Union[PipeTargetParametersArgs, PipeTargetParametersArgsDict]]
        ] = ...,
    ) -> Pipe: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="desiredState")
    def desired_state(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def enrichment(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enrichmentParameters")
    def enrichment_parameters(
        self,
    ) -> pulumi.Output[Optional[outputs.PipeEnrichmentParameters]]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="logConfiguration")
    def log_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.PipeLogConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sourceParameters")
    def source_parameters(self) -> pulumi.Output[outputs.PipeSourceParameters]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetParameters")
    def target_parameters(
        self,
    ) -> pulumi.Output[Optional[outputs.PipeTargetParameters]]: ...
