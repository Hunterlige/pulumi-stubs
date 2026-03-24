import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServiceArgs", "Service"]

@pulumi.input_type
class ServiceArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        template: pulumi.Input[ServiceTemplateArgs],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        binary_authorization: Optional[
            pulumi.Input[ServiceBinaryAuthorizationArgs]
        ] = ...,
        build_config: Optional[pulumi.Input[ServiceBuildConfigArgs]] = ...,
        client: Optional[pulumi.Input[_builtins.str]] = ...,
        client_version: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_audiences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_uri_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        iap_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ingress: Optional[pulumi.Input[_builtins.str]] = ...,
        invoker_iam_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_settings: Optional[
            pulumi.Input[ServiceMultiRegionSettingsArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling: Optional[pulumi.Input[ServiceScalingArgs]] = ...,
        traffics: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Input[ServiceTemplateArgs]: ...
    @template.setter
    def template(self, value: pulumi.Input[ServiceTemplateArgs]): ...
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
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> Optional[pulumi.Input[ServiceBinaryAuthorizationArgs]]: ...
    @binary_authorization.setter
    def binary_authorization(
        self, value: Optional[pulumi.Input[ServiceBinaryAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="buildConfig")
    def build_config(self) -> Optional[pulumi.Input[ServiceBuildConfigArgs]]: ...
    @build_config.setter
    def build_config(self, value: Optional[pulumi.Input[ServiceBuildConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client.setter
    def client(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_version.setter
    def client_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customAudiences")
    def custom_audiences(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_audiences.setter
    def custom_audiences(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultUriDisabled")
    def default_uri_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @default_uri_disabled.setter
    def default_uri_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iapEnabled")
    def iap_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @iap_enabled.setter
    def iap_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invokerIamDisabled")
    def invoker_iam_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invoker_iam_disabled.setter
    def invoker_iam_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_stage.setter
    def launch_stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiRegionSettings")
    def multi_region_settings(
        self,
    ) -> Optional[pulumi.Input[ServiceMultiRegionSettingsArgs]]: ...
    @multi_region_settings.setter
    def multi_region_settings(
        self, value: Optional[pulumi.Input[ServiceMultiRegionSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scaling(self) -> Optional[pulumi.Input[ServiceScalingArgs]]: ...
    @scaling.setter
    def scaling(self, value: Optional[pulumi.Input[ServiceScalingArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def traffics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]]: ...
    @traffics.setter
    def traffics(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]]
    ): ...

@pulumi.input_type
class _ServiceState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        binary_authorization: Optional[
            pulumi.Input[ServiceBinaryAuthorizationArgs]
        ] = ...,
        build_config: Optional[pulumi.Input[ServiceBuildConfigArgs]] = ...,
        client: Optional[pulumi.Input[_builtins.str]] = ...,
        client_version: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceConditionArgs]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_audiences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_uri_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
        iap_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ingress: Optional[pulumi.Input[_builtins.str]] = ...,
        invoker_iam_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        last_modifier: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_created_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_ready_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_settings: Optional[
            pulumi.Input[ServiceMultiRegionSettingsArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        observed_generation: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        scaling: Optional[pulumi.Input[ServiceScalingArgs]] = ...,
        template: Optional[pulumi.Input[ServiceTemplateArgs]] = ...,
        terminal_conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTerminalConditionArgs]]]
        ] = ...,
        traffic_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTrafficStatusArgs]]]
        ] = ...,
        traffics: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
        urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
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
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> Optional[pulumi.Input[ServiceBinaryAuthorizationArgs]]: ...
    @binary_authorization.setter
    def binary_authorization(
        self, value: Optional[pulumi.Input[ServiceBinaryAuthorizationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="buildConfig")
    def build_config(self) -> Optional[pulumi.Input[ServiceBuildConfigArgs]]: ...
    @build_config.setter
    def build_config(self, value: Optional[pulumi.Input[ServiceBuildConfigArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client.setter
    def client(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_version.setter
    def client_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceConditionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def creator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @creator.setter
    def creator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customAudiences")
    def custom_audiences(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @custom_audiences.setter
    def custom_audiences(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultUriDisabled")
    def default_uri_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @default_uri_disabled.setter
    def default_uri_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete_time.setter
    def delete_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @deletion_protection.setter
    def deletion_protection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @expire_time.setter
    def expire_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="iapEnabled")
    def iap_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @iap_enabled.setter
    def iap_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingress.setter
    def ingress(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invokerIamDisabled")
    def invoker_iam_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invoker_iam_disabled.setter
    def invoker_iam_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="lastModifier")
    def last_modifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_modifier.setter
    def last_modifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="latestCreatedRevision")
    def latest_created_revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latest_created_revision.setter
    def latest_created_revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="latestReadyRevision")
    def latest_ready_revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latest_ready_revision.setter
    def latest_ready_revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @launch_stage.setter
    def launch_stage(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multiRegionSettings")
    def multi_region_settings(
        self,
    ) -> Optional[pulumi.Input[ServiceMultiRegionSettingsArgs]]: ...
    @multi_region_settings.setter
    def multi_region_settings(
        self, value: Optional[pulumi.Input[ServiceMultiRegionSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @observed_generation.setter
    def observed_generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def reconciling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @reconciling.setter
    def reconciling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def scaling(self) -> Optional[pulumi.Input[ServiceScalingArgs]]: ...
    @scaling.setter
    def scaling(self, value: Optional[pulumi.Input[ServiceScalingArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[ServiceTemplateArgs]]: ...
    @template.setter
    def template(self, value: Optional[pulumi.Input[ServiceTemplateArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="terminalConditions")
    def terminal_conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTerminalConditionArgs]]]
    ]: ...
    @terminal_conditions.setter
    def terminal_conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTerminalConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="trafficStatuses")
    def traffic_statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficStatusArgs]]]]: ...
    @traffic_statuses.setter
    def traffic_statuses(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficStatusArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def traffics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]]: ...
    @traffics.setter
    def traffics(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTrafficArgs]]]]
    ): ...
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
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def urls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @urls.setter
    def urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("gcp:cloudrunv2/service:Service")
class Service(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        binary_authorization: Optional[
            pulumi.Input[
                Union[
                    ServiceBinaryAuthorizationArgs, ServiceBinaryAuthorizationArgsDict
                ]
            ]
        ] = ...,
        build_config: Optional[
            pulumi.Input[Union[ServiceBuildConfigArgs, ServiceBuildConfigArgsDict]]
        ] = ...,
        client: Optional[pulumi.Input[_builtins.str]] = ...,
        client_version: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_audiences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_uri_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        iap_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ingress: Optional[pulumi.Input[_builtins.str]] = ...,
        invoker_iam_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_settings: Optional[
            pulumi.Input[
                Union[
                    ServiceMultiRegionSettingsArgs, ServiceMultiRegionSettingsArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling: Optional[
            pulumi.Input[Union[ServiceScalingArgs, ServiceScalingArgsDict]]
        ] = ...,
        template: Optional[
            pulumi.Input[Union[ServiceTemplateArgs, ServiceTemplateArgsDict]]
        ] = ...,
        traffics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ServiceTrafficArgs, ServiceTrafficArgsDict]]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ServiceArgs,
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
        binary_authorization: Optional[
            pulumi.Input[
                Union[
                    ServiceBinaryAuthorizationArgs, ServiceBinaryAuthorizationArgsDict
                ]
            ]
        ] = ...,
        build_config: Optional[
            pulumi.Input[Union[ServiceBuildConfigArgs, ServiceBuildConfigArgsDict]]
        ] = ...,
        client: Optional[pulumi.Input[_builtins.str]] = ...,
        client_version: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ServiceConditionArgs, ServiceConditionArgsDict]]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        creator: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_audiences: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        default_uri_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        delete_time: Optional[pulumi.Input[_builtins.str]] = ...,
        deletion_protection: Optional[pulumi.Input[_builtins.bool]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        expire_time: Optional[pulumi.Input[_builtins.str]] = ...,
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
        iap_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        ingress: Optional[pulumi.Input[_builtins.str]] = ...,
        invoker_iam_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        last_modifier: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_created_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_ready_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        launch_stage: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        multi_region_settings: Optional[
            pulumi.Input[
                Union[
                    ServiceMultiRegionSettingsArgs, ServiceMultiRegionSettingsArgsDict
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        observed_generation: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        reconciling: Optional[pulumi.Input[_builtins.bool]] = ...,
        scaling: Optional[
            pulumi.Input[Union[ServiceScalingArgs, ServiceScalingArgsDict]]
        ] = ...,
        template: Optional[
            pulumi.Input[Union[ServiceTemplateArgs, ServiceTemplateArgsDict]]
        ] = ...,
        terminal_conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ServiceTerminalConditionArgs,
                            ServiceTerminalConditionArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        traffic_statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ServiceTrafficStatusArgs, ServiceTrafficStatusArgsDict]
                    ]
                ]
            ]
        ] = ...,
        traffics: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ServiceTrafficArgs, ServiceTrafficArgsDict]]
                ]
            ]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
        urls: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> Service: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorization")
    def binary_authorization(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceBinaryAuthorization]]: ...
    @_builtins.property
    @pulumi.getter(name="buildConfig")
    def build_config(self) -> pulumi.Output[Optional[outputs.ServiceBuildConfig]]: ...
    @_builtins.property
    @pulumi.getter
    def client(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="clientVersion")
    def client_version(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence[outputs.ServiceCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def creator(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="customAudiences")
    def custom_audiences(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultUriDisabled")
    def default_uri_disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="deleteTime")
    def delete_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
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
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="iapEnabled")
    def iap_enabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def ingress(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="invokerIamDisabled")
    def invoker_iam_disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="lastModifier")
    def last_modifier(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestCreatedRevision")
    def latest_created_revision(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestReadyRevision")
    def latest_ready_revision(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="launchStage")
    def launch_stage(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multiRegionSettings")
    def multi_region_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.ServiceMultiRegionSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def reconciling(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def scaling(self) -> pulumi.Output[outputs.ServiceScaling]: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Output[outputs.ServiceTemplate]: ...
    @_builtins.property
    @pulumi.getter(name="terminalConditions")
    def terminal_conditions(
        self,
    ) -> pulumi.Output[Sequence[outputs.ServiceTerminalCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="trafficStatuses")
    def traffic_statuses(
        self,
    ) -> pulumi.Output[Sequence[outputs.ServiceTrafficStatus]]: ...
    @_builtins.property
    @pulumi.getter
    def traffics(self) -> pulumi.Output[Sequence[outputs.ServiceTraffic]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def urls(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
