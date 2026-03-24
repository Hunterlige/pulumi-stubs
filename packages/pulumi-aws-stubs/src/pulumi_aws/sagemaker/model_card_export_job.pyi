import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ModelCardExportJobArgs", "ModelCardExportJob"]

@pulumi.input_type
class ModelCardExportJobArgs:
    def __init__(
        __self__,
        *,
        model_card_export_job_name: pulumi.Input[_builtins.str],
        model_card_name: pulumi.Input[_builtins.str],
        output_config: pulumi.Input[ModelCardExportJobOutputConfigArgs],
        model_card_version: Optional[pulumi.Input[_builtins.int]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[ModelCardExportJobTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelCardExportJobName")
    def model_card_export_job_name(self) -> pulumi.Input[_builtins.str]: ...
    @model_card_export_job_name.setter
    def model_card_export_job_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="modelCardName")
    def model_card_name(self) -> pulumi.Input[_builtins.str]: ...
    @model_card_name.setter
    def model_card_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(self) -> pulumi.Input[ModelCardExportJobOutputConfigArgs]: ...
    @output_config.setter
    def output_config(
        self, value: pulumi.Input[ModelCardExportJobOutputConfigArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelCardVersion")
    def model_card_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @model_card_version.setter
    def model_card_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ModelCardExportJobTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[ModelCardExportJobTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _ModelCardExportJobState:
    def __init__(
        __self__,
        *,
        export_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[ModelCardExportJobExportArtifactArgs]]]
        ] = ...,
        model_card_export_job_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_export_job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_version: Optional[pulumi.Input[_builtins.int]] = ...,
        output_config: Optional[pulumi.Input[ModelCardExportJobOutputConfigArgs]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[ModelCardExportJobTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="exportArtifacts")
    def export_artifacts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ModelCardExportJobExportArtifactArgs]]]
    ]: ...
    @export_artifacts.setter
    def export_artifacts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ModelCardExportJobExportArtifactArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelCardExportJobArn")
    def model_card_export_job_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_card_export_job_arn.setter
    def model_card_export_job_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelCardExportJobName")
    def model_card_export_job_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_card_export_job_name.setter
    def model_card_export_job_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelCardName")
    def model_card_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_card_name.setter
    def model_card_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelCardVersion")
    def model_card_version(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @model_card_version.setter
    def model_card_version(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(
        self,
    ) -> Optional[pulumi.Input[ModelCardExportJobOutputConfigArgs]]: ...
    @output_config.setter
    def output_config(
        self, value: Optional[pulumi.Input[ModelCardExportJobOutputConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[ModelCardExportJobTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[ModelCardExportJobTimeoutsArgs]]
    ): ...

@pulumi.type_token(...)
class ModelCardExportJob(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        model_card_export_job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_version: Optional[pulumi.Input[_builtins.int]] = ...,
        output_config: Optional[
            pulumi.Input[
                Union[
                    ModelCardExportJobOutputConfigArgs,
                    ModelCardExportJobOutputConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ModelCardExportJobTimeoutsArgs, ModelCardExportJobTimeoutsArgsDict
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ModelCardExportJobArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        export_artifacts: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ModelCardExportJobExportArtifactArgs,
                            ModelCardExportJobExportArtifactArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        model_card_export_job_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_export_job_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_name: Optional[pulumi.Input[_builtins.str]] = ...,
        model_card_version: Optional[pulumi.Input[_builtins.int]] = ...,
        output_config: Optional[
            pulumi.Input[
                Union[
                    ModelCardExportJobOutputConfigArgs,
                    ModelCardExportJobOutputConfigArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    ModelCardExportJobTimeoutsArgs, ModelCardExportJobTimeoutsArgsDict
                ]
            ]
        ] = ...,
    ) -> ModelCardExportJob: ...
    @_builtins.property
    @pulumi.getter(name="exportArtifacts")
    def export_artifacts(
        self,
    ) -> pulumi.Output[Sequence[outputs.ModelCardExportJobExportArtifact]]: ...
    @_builtins.property
    @pulumi.getter(name="modelCardExportJobArn")
    def model_card_export_job_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelCardExportJobName")
    def model_card_export_job_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelCardName")
    def model_card_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelCardVersion")
    def model_card_version(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="outputConfig")
    def output_config(
        self,
    ) -> pulumi.Output[outputs.ModelCardExportJobOutputConfig]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.ModelCardExportJobTimeouts]]: ...
