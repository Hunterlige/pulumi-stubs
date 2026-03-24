import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PipelineArgs", "Pipeline"]

@pulumi.input_type
class PipelineArgs:
    def __init__(
        __self__,
        *,
        destinations: pulumi.Input[Sequence[pulumi.Input[PipelineDestinationArgs]]],
        location: pulumi.Input[_builtins.str],
        pipeline_id: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        crypto_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        input_payload_format: Optional[
            pulumi.Input[PipelineInputPayloadFormatArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        logging_config: Optional[pulumi.Input[PipelineLoggingConfigArgs]] = ...,
        mediations: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineMediationArgs]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_policy: Optional[pulumi.Input[PipelineRetryPolicyArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[PipelineDestinationArgs]]]: ...
    @destinations.setter
    def destinations(
        self, value: pulumi.Input[Sequence[pulumi.Input[PipelineDestinationArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> pulumi.Input[_builtins.str]: ...
    @pipeline_id.setter
    def pipeline_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputPayloadFormat")
    def input_payload_format(
        self,
    ) -> Optional[pulumi.Input[PipelineInputPayloadFormatArgs]]: ...
    @input_payload_format.setter
    def input_payload_format(
        self, value: Optional[pulumi.Input[PipelineInputPayloadFormatArgs]]
    ): ...
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
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[PipelineLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[PipelineLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mediations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineMediationArgs]]]]: ...
    @mediations.setter
    def mediations(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineMediationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[PipelineRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input[PipelineRetryPolicyArgs]]): ...

@pulumi.input_type
class _PipelineState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        crypto_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineDestinationArgs]]]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        input_payload_format: Optional[
            pulumi.Input[PipelineInputPayloadFormatArgs]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_config: Optional[pulumi.Input[PipelineLoggingConfigArgs]] = ...,
        mediations: Optional[
            pulumi.Input[Sequence[pulumi.Input[PipelineMediationArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        retry_policy: Optional[pulumi.Input[PipelineRetryPolicyArgs]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @crypto_key_name.setter
    def crypto_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineDestinationArgs]]]]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineDestinationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_annotations.setter
    def effective_annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputPayloadFormat")
    def input_payload_format(
        self,
    ) -> Optional[pulumi.Input[PipelineInputPayloadFormatArgs]]: ...
    @input_payload_format.setter
    def input_payload_format(
        self, value: Optional[pulumi.Input[PipelineInputPayloadFormatArgs]]
    ): ...
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
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[PipelineLoggingConfigArgs]]: ...
    @logging_config.setter
    def logging_config(
        self, value: Optional[pulumi.Input[PipelineLoggingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mediations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PipelineMediationArgs]]]]: ...
    @mediations.setter
    def mediations(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[PipelineMediationArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pipeline_id.setter
    def pipeline_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[PipelineRetryPolicyArgs]]: ...
    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input[PipelineRetryPolicyArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:eventarc/pipeline:Pipeline")
class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        crypto_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PipelineDestinationArgs, PipelineDestinationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        input_payload_format: Optional[
            pulumi.Input[
                Union[
                    PipelineInputPayloadFormatArgs, PipelineInputPayloadFormatArgsDict
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_config: Optional[
            pulumi.Input[
                Union[PipelineLoggingConfigArgs, PipelineLoggingConfigArgsDict]
            ]
        ] = ...,
        mediations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PipelineMediationArgs, PipelineMediationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        pipeline_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_policy: Optional[
            pulumi.Input[Union[PipelineRetryPolicyArgs, PipelineRetryPolicyArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PipelineArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        crypto_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        destinations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PipelineDestinationArgs, PipelineDestinationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        input_payload_format: Optional[
            pulumi.Input[
                Union[
                    PipelineInputPayloadFormatArgs, PipelineInputPayloadFormatArgsDict
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_config: Optional[
            pulumi.Input[
                Union[PipelineLoggingConfigArgs, PipelineLoggingConfigArgsDict]
            ]
        ] = ...,
        mediations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[PipelineMediationArgs, PipelineMediationArgsDict]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pipeline_id: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        retry_policy: Optional[
            pulumi.Input[Union[PipelineRetryPolicyArgs, PipelineRetryPolicyArgsDict]]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Pipeline: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="cryptoKeyName")
    def crypto_key_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Sequence[outputs.PipelineDestination]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="inputPayloadFormat")
    def input_payload_format(
        self,
    ) -> pulumi.Output[Optional[outputs.PipelineInputPayloadFormat]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[outputs.PipelineLoggingConfig]: ...
    @_builtins.property
    @pulumi.getter
    def mediations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.PipelineMediation]]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> pulumi.Output[outputs.PipelineRetryPolicy]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
