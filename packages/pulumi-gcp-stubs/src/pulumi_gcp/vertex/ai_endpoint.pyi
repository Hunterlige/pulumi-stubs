import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AiEndpointArgs", "AiEndpoint"]

@pulumi.input_type
class AiEndpointArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        dedicated_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_spec: Optional[pulumi.Input[AiEndpointEncryptionSpecArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        predict_request_response_logging_config: Optional[
            pulumi.Input[AiEndpointPredictRequestResponseLoggingConfigArgs]
        ] = ...,
        private_service_connect_config: Optional[
            pulumi.Input[AiEndpointPrivateServiceConnectConfigArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_split: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @pulumi.getter(name="dedicatedEndpointEnabled")
    def dedicated_endpoint_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dedicated_endpoint_enabled.setter
    def dedicated_endpoint_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> Optional[pulumi.Input[AiEndpointEncryptionSpecArgs]]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: Optional[pulumi.Input[AiEndpointEncryptionSpecArgs]]
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
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="predictRequestResponseLoggingConfig")
    def predict_request_response_logging_config(
        self,
    ) -> Optional[pulumi.Input[AiEndpointPredictRequestResponseLoggingConfigArgs]]: ...
    @predict_request_response_logging_config.setter
    def predict_request_response_logging_config(
        self,
        value: Optional[
            pulumi.Input[AiEndpointPredictRequestResponseLoggingConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateServiceConnectConfig")
    def private_service_connect_config(
        self,
    ) -> Optional[pulumi.Input[AiEndpointPrivateServiceConnectConfigArgs]]: ...
    @private_service_connect_config.setter
    def private_service_connect_config(
        self, value: Optional[pulumi.Input[AiEndpointPrivateServiceConnectConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trafficSplit")
    def traffic_split(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @traffic_split.setter
    def traffic_split(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _AiEndpointState:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dedicated_endpoint_dns: Optional[pulumi.Input[_builtins.str]] = ...,
        dedicated_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        deployed_models: Optional[
            pulumi.Input[Sequence[pulumi.Input[AiEndpointDeployedModelArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_spec: Optional[pulumi.Input[AiEndpointEncryptionSpecArgs]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        model_deployment_monitoring_job: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        predict_request_response_logging_config: Optional[
            pulumi.Input[AiEndpointPredictRequestResponseLoggingConfigArgs]
        ] = ...,
        private_service_connect_config: Optional[
            pulumi.Input[AiEndpointPrivateServiceConnectConfigArgs]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_split: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dedicatedEndpointDns")
    def dedicated_endpoint_dns(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dedicated_endpoint_dns.setter
    def dedicated_endpoint_dns(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dedicatedEndpointEnabled")
    def dedicated_endpoint_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @dedicated_endpoint_enabled.setter
    def dedicated_endpoint_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deployedModels")
    def deployed_models(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AiEndpointDeployedModelArgs]]]
    ]: ...
    @deployed_models.setter
    def deployed_models(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AiEndpointDeployedModelArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> Optional[pulumi.Input[AiEndpointEncryptionSpecArgs]]: ...
    @encryption_spec.setter
    def encryption_spec(
        self, value: Optional[pulumi.Input[AiEndpointEncryptionSpecArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="modelDeploymentMonitoringJob")
    def model_deployment_monitoring_job(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_deployment_monitoring_job.setter
    def model_deployment_monitoring_job(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="predictRequestResponseLoggingConfig")
    def predict_request_response_logging_config(
        self,
    ) -> Optional[pulumi.Input[AiEndpointPredictRequestResponseLoggingConfigArgs]]: ...
    @predict_request_response_logging_config.setter
    def predict_request_response_logging_config(
        self,
        value: Optional[
            pulumi.Input[AiEndpointPredictRequestResponseLoggingConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="privateServiceConnectConfig")
    def private_service_connect_config(
        self,
    ) -> Optional[pulumi.Input[AiEndpointPrivateServiceConnectConfigArgs]]: ...
    @private_service_connect_config.setter
    def private_service_connect_config(
        self, value: Optional[pulumi.Input[AiEndpointPrivateServiceConnectConfigArgs]]
    ): ...
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
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trafficSplit")
    def traffic_split(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @traffic_split.setter
    def traffic_split(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:vertex/aiEndpoint:AiEndpoint")
class AiEndpoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        dedicated_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_spec: Optional[
            pulumi.Input[
                Union[AiEndpointEncryptionSpecArgs, AiEndpointEncryptionSpecArgsDict]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        predict_request_response_logging_config: Optional[
            pulumi.Input[
                Union[
                    AiEndpointPredictRequestResponseLoggingConfigArgs,
                    AiEndpointPredictRequestResponseLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        private_service_connect_config: Optional[
            pulumi.Input[
                Union[
                    AiEndpointPrivateServiceConnectConfigArgs,
                    AiEndpointPrivateServiceConnectConfigArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_split: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AiEndpointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        dedicated_endpoint_dns: Optional[pulumi.Input[_builtins.str]] = ...,
        dedicated_endpoint_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        deployed_models: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AiEndpointDeployedModelArgs, AiEndpointDeployedModelArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        encryption_spec: Optional[
            pulumi.Input[
                Union[AiEndpointEncryptionSpecArgs, AiEndpointEncryptionSpecArgsDict]
            ]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        model_deployment_monitoring_job: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        predict_request_response_logging_config: Optional[
            pulumi.Input[
                Union[
                    AiEndpointPredictRequestResponseLoggingConfigArgs,
                    AiEndpointPredictRequestResponseLoggingConfigArgsDict,
                ]
            ]
        ] = ...,
        private_service_connect_config: Optional[
            pulumi.Input[
                Union[
                    AiEndpointPrivateServiceConnectConfigArgs,
                    AiEndpointPrivateServiceConnectConfigArgsDict,
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        traffic_split: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AiEndpoint: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedEndpointDns")
    def dedicated_endpoint_dns(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dedicatedEndpointEnabled")
    def dedicated_endpoint_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="deployedModels")
    def deployed_models(
        self,
    ) -> pulumi.Output[Sequence[outputs.AiEndpointDeployedModel]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionSpec")
    def encryption_spec(
        self,
    ) -> pulumi.Output[Optional[outputs.AiEndpointEncryptionSpec]]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelDeploymentMonitoringJob")
    def model_deployment_monitoring_job(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="predictRequestResponseLoggingConfig")
    def predict_request_response_logging_config(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AiEndpointPredictRequestResponseLoggingConfig]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="privateServiceConnectConfig")
    def private_service_connect_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AiEndpointPrivateServiceConnectConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trafficSplit")
    def traffic_split(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
