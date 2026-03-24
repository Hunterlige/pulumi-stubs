

import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AddRemoveReplicaScalingMechanismArgs', 'AddRemoveReplicaScalingMechanismArgsDict', ..., ..., 'ApplicationScopedVolumeArgs', 'ApplicationScopedVolumeArgsDict', 'AutoScalingPolicyArgs', 'AutoScalingPolicyArgsDict', 'AutoScalingResourceMetricArgs', 'AutoScalingResourceMetricArgsDict', 'AverageLoadScalingTriggerArgs', 'AverageLoadScalingTriggerArgsDict', 'AzureInternalMonitoringPipelineSinkDescriptionArgs', ..., 'ContainerCodePackagePropertiesArgs', 'ContainerCodePackagePropertiesArgsDict', 'ContainerLabelArgs', 'ContainerLabelArgsDict', 'DiagnosticsDescriptionArgs', 'DiagnosticsDescriptionArgsDict', 'DiagnosticsRefArgs', 'DiagnosticsRefArgsDict', 'EndpointPropertiesArgs', 'EndpointPropertiesArgsDict', 'EndpointRefArgs', 'EndpointRefArgsDict', 'EnvironmentVariableArgs', 'EnvironmentVariableArgsDict', 'GatewayDestinationArgs', 'GatewayDestinationArgsDict', 'HttpConfigArgs', 'HttpConfigArgsDict', 'HttpHostConfigArgs', 'HttpHostConfigArgsDict', 'HttpRouteConfigArgs', 'HttpRouteConfigArgsDict', 'HttpRouteMatchHeaderArgs', 'HttpRouteMatchHeaderArgsDict', 'HttpRouteMatchPathArgs', 'HttpRouteMatchPathArgsDict', 'HttpRouteMatchRuleArgs', 'HttpRouteMatchRuleArgsDict', 'ImageRegistryCredentialArgs', 'ImageRegistryCredentialArgsDict', 'NetworkRefArgs', 'NetworkRefArgsDict', 'NetworkResourcePropertiesArgs', 'NetworkResourcePropertiesArgsDict', 'ReliableCollectionsRefArgs', 'ReliableCollectionsRefArgsDict', 'ResourceLimitsArgs', 'ResourceLimitsArgsDict', 'ResourceRequestsArgs', 'ResourceRequestsArgsDict', 'ResourceRequirementsArgs', 'ResourceRequirementsArgsDict', 'SecretResourcePropertiesArgs', 'SecretResourcePropertiesArgsDict', 'ServiceResourceDescriptionArgs', 'ServiceResourceDescriptionArgsDict', 'SettingArgs', 'SettingArgsDict', 'TcpConfigArgs', 'TcpConfigArgsDict', 'VolumeProviderParametersAzureFileArgs', 'VolumeProviderParametersAzureFileArgsDict', 'VolumeReferenceArgs', 'VolumeReferenceArgsDict']
class AddRemoveReplicaScalingMechanismArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    max_count: pulumi.Input[_builtins.int]
    min_count: pulumi.Input[_builtins.int]
    scale_increment: pulumi.Input[_builtins.int]


@pulumi.input_type
class AddRemoveReplicaScalingMechanismArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], max_count: pulumi.Input[_builtins.int], min_count: pulumi.Input[_builtins.int], scale_increment: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @max_count.setter
    def max_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minCount")
    def min_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @min_count.setter
    def min_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIncrement")
    def scale_increment(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @scale_increment.setter
    def scale_increment(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class ApplicationScopedVolumeCreationParametersServiceFabricVolumeDiskArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    size_disk: pulumi.Input[Union[_builtins.str, SizeTypes]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationScopedVolumeCreationParametersServiceFabricVolumeDiskArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], size_disk: pulumi.Input[Union[_builtins.str, SizeTypes]], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeDisk")
    def size_disk(self) -> pulumi.Input[Union[_builtins.str, SizeTypes]]:
        
        ...
    
    @size_disk.setter
    def size_disk(self, value: pulumi.Input[Union[_builtins.str, SizeTypes]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationScopedVolumeArgsDict(TypedDict):
    
    creation_parameters: pulumi.Input[ApplicationScopedVolumeCreationParametersServiceFabricVolumeDiskArgsDict]
    destination_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ApplicationScopedVolumeArgs:
    def __init__(__self__, *, creation_parameters: pulumi.Input[ApplicationScopedVolumeCreationParametersServiceFabricVolumeDiskArgs], destination_path: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], read_only: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationParameters")
    def creation_parameters(self) -> pulumi.Input[ApplicationScopedVolumeCreationParametersServiceFabricVolumeDiskArgs]:
        
        ...
    
    @creation_parameters.setter
    def creation_parameters(self, value: pulumi.Input[ApplicationScopedVolumeCreationParametersServiceFabricVolumeDiskArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPath")
    def destination_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_path.setter
    def destination_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class AutoScalingPolicyArgsDict(TypedDict):
    
    mechanism: pulumi.Input[AddRemoveReplicaScalingMechanismArgsDict]
    name: pulumi.Input[_builtins.str]
    trigger: pulumi.Input[AverageLoadScalingTriggerArgsDict]


@pulumi.input_type
class AutoScalingPolicyArgs:
    def __init__(__self__, *, mechanism: pulumi.Input[AddRemoveReplicaScalingMechanismArgs], name: pulumi.Input[_builtins.str], trigger: pulumi.Input[AverageLoadScalingTriggerArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mechanism(self) -> pulumi.Input[AddRemoveReplicaScalingMechanismArgs]:
        
        ...
    
    @mechanism.setter
    def mechanism(self, value: pulumi.Input[AddRemoveReplicaScalingMechanismArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> pulumi.Input[AverageLoadScalingTriggerArgs]:
        
        ...
    
    @trigger.setter
    def trigger(self, value: pulumi.Input[AverageLoadScalingTriggerArgs]): # -> None:
        ...
    


class AutoScalingResourceMetricArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    name: pulumi.Input[Union[_builtins.str, AutoScalingResourceMetricName]]


@pulumi.input_type
class AutoScalingResourceMetricArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], name: pulumi.Input[Union[_builtins.str, AutoScalingResourceMetricName]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, AutoScalingResourceMetricName]]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, AutoScalingResourceMetricName]]): # -> None:
        ...
    


class AverageLoadScalingTriggerArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    lower_load_threshold: pulumi.Input[_builtins.float]
    metric: pulumi.Input[AutoScalingResourceMetricArgsDict]
    scale_interval_in_seconds: pulumi.Input[_builtins.int]
    upper_load_threshold: pulumi.Input[_builtins.float]


@pulumi.input_type
class AverageLoadScalingTriggerArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], lower_load_threshold: pulumi.Input[_builtins.float], metric: pulumi.Input[AutoScalingResourceMetricArgs], scale_interval_in_seconds: pulumi.Input[_builtins.int], upper_load_threshold: pulumi.Input[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lowerLoadThreshold")
    def lower_load_threshold(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @lower_load_threshold.setter
    def lower_load_threshold(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metric(self) -> pulumi.Input[AutoScalingResourceMetricArgs]:
        
        ...
    
    @metric.setter
    def metric(self, value: pulumi.Input[AutoScalingResourceMetricArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="scaleIntervalInSeconds")
    def scale_interval_in_seconds(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @scale_interval_in_seconds.setter
    def scale_interval_in_seconds(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="upperLoadThreshold")
    def upper_load_threshold(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @upper_load_threshold.setter
    def upper_load_threshold(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    


class AzureInternalMonitoringPipelineSinkDescriptionArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    account_name: NotRequired[pulumi.Input[_builtins.str]]
    auto_key_config_url: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    fluentd_config_url: NotRequired[Any]
    ma_config_url: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AzureInternalMonitoringPipelineSinkDescriptionArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], account_name: Optional[pulumi.Input[_builtins.str]] = ..., auto_key_config_url: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., fluentd_config_url: Optional[Any] = ..., ma_config_url: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., namespace: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoKeyConfigUrl")
    def auto_key_config_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @auto_key_config_url.setter
    def auto_key_config_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fluentdConfigUrl")
    def fluentd_config_url(self) -> Optional[Any]:
        
        ...
    
    @fluentd_config_url.setter
    def fluentd_config_url(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maConfigUrl")
    def ma_config_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ma_config_url.setter
    def ma_config_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ContainerCodePackagePropertiesArgsDict(TypedDict):
    
    image: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    resources: pulumi.Input[ResourceRequirementsArgsDict]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    diagnostics: NotRequired[pulumi.Input[DiagnosticsRefArgsDict]]
    endpoints: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesArgsDict]]]]
    entrypoint: NotRequired[pulumi.Input[_builtins.str]]
    environment_variables: NotRequired[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgsDict]]]]
    image_registry_credential: NotRequired[pulumi.Input[ImageRegistryCredentialArgsDict]]
    labels: NotRequired[pulumi.Input[Sequence[pulumi.Input[ContainerLabelArgsDict]]]]
    reliable_collections_refs: NotRequired[pulumi.Input[Sequence[pulumi.Input[ReliableCollectionsRefArgsDict]]]]
    settings: NotRequired[pulumi.Input[Sequence[pulumi.Input[SettingArgsDict]]]]
    volume_refs: NotRequired[pulumi.Input[Sequence[pulumi.Input[VolumeReferenceArgsDict]]]]
    volumes: NotRequired[pulumi.Input[Sequence[pulumi.Input[ApplicationScopedVolumeArgsDict]]]]


@pulumi.input_type
class ContainerCodePackagePropertiesArgs:
    def __init__(__self__, *, image: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], resources: pulumi.Input[ResourceRequirementsArgs], commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., diagnostics: Optional[pulumi.Input[DiagnosticsRefArgs]] = ..., endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesArgs]]]] = ..., entrypoint: Optional[pulumi.Input[_builtins.str]] = ..., environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]] = ..., image_registry_credential: Optional[pulumi.Input[ImageRegistryCredentialArgs]] = ..., labels: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerLabelArgs]]]] = ..., reliable_collections_refs: Optional[pulumi.Input[Sequence[pulumi.Input[ReliableCollectionsRefArgs]]]] = ..., settings: Optional[pulumi.Input[Sequence[pulumi.Input[SettingArgs]]]] = ..., volume_refs: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReferenceArgs]]]] = ..., volumes: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationScopedVolumeArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Input[ResourceRequirementsArgs]:
        
        ...
    
    @resources.setter
    def resources(self, value: pulumi.Input[ResourceRequirementsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @commands.setter
    def commands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Optional[pulumi.Input[DiagnosticsRefArgs]]:
        
        ...
    
    @diagnostics.setter
    def diagnostics(self, value: Optional[pulumi.Input[DiagnosticsRefArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesArgs]]]]:
        
        ...
    
    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointPropertiesArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def entrypoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @entrypoint.setter
    def entrypoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EnvironmentVariableArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageRegistryCredential")
    def image_registry_credential(self) -> Optional[pulumi.Input[ImageRegistryCredentialArgs]]:
        
        ...
    
    @image_registry_credential.setter
    def image_registry_credential(self, value: Optional[pulumi.Input[ImageRegistryCredentialArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ContainerLabelArgs]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ContainerLabelArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reliableCollectionsRefs")
    def reliable_collections_refs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReliableCollectionsRefArgs]]]]:
        
        ...
    
    @reliable_collections_refs.setter
    def reliable_collections_refs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ReliableCollectionsRefArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[SettingArgs]]]]:
        
        ...
    
    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[SettingArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeRefs")
    def volume_refs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReferenceArgs]]]]:
        
        ...
    
    @volume_refs.setter
    def volume_refs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[VolumeReferenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationScopedVolumeArgs]]]]:
        
        ...
    
    @volumes.setter
    def volumes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ApplicationScopedVolumeArgs]]]]): # -> None:
        ...
    


class ContainerLabelArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class ContainerLabelArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class DiagnosticsDescriptionArgsDict(TypedDict):
    
    default_sink_refs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    sinks: NotRequired[pulumi.Input[Sequence[pulumi.Input[AzureInternalMonitoringPipelineSinkDescriptionArgsDict]]]]


@pulumi.input_type
class DiagnosticsDescriptionArgs:
    def __init__(__self__, *, default_sink_refs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., sinks: Optional[pulumi.Input[Sequence[pulumi.Input[AzureInternalMonitoringPipelineSinkDescriptionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSinkRefs")
    def default_sink_refs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @default_sink_refs.setter
    def default_sink_refs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sinks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AzureInternalMonitoringPipelineSinkDescriptionArgs]]]]:
        
        ...
    
    @sinks.setter
    def sinks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AzureInternalMonitoringPipelineSinkDescriptionArgs]]]]): # -> None:
        ...
    


class DiagnosticsRefArgsDict(TypedDict):
    
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    sink_refs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class DiagnosticsRefArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., sink_refs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sinkRefs")
    def sink_refs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @sink_refs.setter
    def sink_refs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class EndpointPropertiesArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class EndpointPropertiesArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class EndpointRefArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EndpointRefArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EnvironmentVariableArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EnvironmentVariableArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GatewayDestinationArgsDict(TypedDict):
    
    application_name: pulumi.Input[_builtins.str]
    endpoint_name: pulumi.Input[_builtins.str]
    service_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class GatewayDestinationArgs:
    def __init__(__self__, *, application_name: pulumi.Input[_builtins.str], endpoint_name: pulumi.Input[_builtins.str], service_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @application_name.setter
    def application_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_name.setter
    def service_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class HttpConfigArgsDict(TypedDict):
    
    hosts: pulumi.Input[Sequence[pulumi.Input[HttpHostConfigArgsDict]]]
    name: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]


@pulumi.input_type
class HttpConfigArgs:
    def __init__(__self__, *, hosts: pulumi.Input[Sequence[pulumi.Input[HttpHostConfigArgs]]], name: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hosts(self) -> pulumi.Input[Sequence[pulumi.Input[HttpHostConfigArgs]]]:
        
        ...
    
    @hosts.setter
    def hosts(self, value: pulumi.Input[Sequence[pulumi.Input[HttpHostConfigArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class HttpHostConfigArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    routes: pulumi.Input[Sequence[pulumi.Input[HttpRouteConfigArgsDict]]]


@pulumi.input_type
class HttpHostConfigArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], routes: pulumi.Input[Sequence[pulumi.Input[HttpRouteConfigArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def routes(self) -> pulumi.Input[Sequence[pulumi.Input[HttpRouteConfigArgs]]]:
        
        ...
    
    @routes.setter
    def routes(self, value: pulumi.Input[Sequence[pulumi.Input[HttpRouteConfigArgs]]]): # -> None:
        ...
    


class HttpRouteConfigArgsDict(TypedDict):
    
    destination: pulumi.Input[GatewayDestinationArgsDict]
    match: pulumi.Input[HttpRouteMatchRuleArgsDict]
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class HttpRouteConfigArgs:
    def __init__(__self__, *, destination: pulumi.Input[GatewayDestinationArgs], match: pulumi.Input[HttpRouteMatchRuleArgs], name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[GatewayDestinationArgs]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[GatewayDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def match(self) -> pulumi.Input[HttpRouteMatchRuleArgs]:
        
        ...
    
    @match.setter
    def match(self, value: pulumi.Input[HttpRouteMatchRuleArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class HttpRouteMatchHeaderArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    type: NotRequired[pulumi.Input[Union[_builtins.str, HeaderMatchType]]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HttpRouteMatchHeaderArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], type: Optional[pulumi.Input[Union[_builtins.str, HeaderMatchType]]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, HeaderMatchType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, HeaderMatchType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HttpRouteMatchPathArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, PathMatchType]]
    value: pulumi.Input[_builtins.str]
    rewrite: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HttpRouteMatchPathArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, PathMatchType]], value: pulumi.Input[_builtins.str], rewrite: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, PathMatchType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, PathMatchType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def rewrite(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rewrite.setter
    def rewrite(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class HttpRouteMatchRuleArgsDict(TypedDict):
    
    path: pulumi.Input[HttpRouteMatchPathArgsDict]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[HttpRouteMatchHeaderArgsDict]]]]


@pulumi.input_type
class HttpRouteMatchRuleArgs:
    def __init__(__self__, *, path: pulumi.Input[HttpRouteMatchPathArgs], headers: Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteMatchHeaderArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[HttpRouteMatchPathArgs]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[HttpRouteMatchPathArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteMatchHeaderArgs]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HttpRouteMatchHeaderArgs]]]]): # -> None:
        ...
    


class ImageRegistryCredentialArgsDict(TypedDict):
    
    server: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ImageRegistryCredentialArgs:
    def __init__(__self__, *, server: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str], password: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkRefArgsDict(TypedDict):
    
    endpoint_refs: NotRequired[pulumi.Input[Sequence[pulumi.Input[EndpointRefArgsDict]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkRefArgs:
    def __init__(__self__, *, endpoint_refs: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointRefArgs]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointRefs")
    def endpoint_refs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EndpointRefArgs]]]]:
        
        ...
    
    @endpoint_refs.setter
    def endpoint_refs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EndpointRefArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class NetworkResourcePropertiesArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkResourcePropertiesArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ReliableCollectionsRefArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    do_not_persist_state: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ReliableCollectionsRefArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], do_not_persist_state: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="doNotPersistState")
    def do_not_persist_state(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @do_not_persist_state.setter
    def do_not_persist_state(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ResourceLimitsArgsDict(TypedDict):
    
    cpu: NotRequired[pulumi.Input[_builtins.float]]
    memory_in_gb: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class ResourceLimitsArgs:
    def __init__(__self__, *, cpu: Optional[pulumi.Input[_builtins.float]] = ..., memory_in_gb: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryInGB")
    def memory_in_gb(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @memory_in_gb.setter
    def memory_in_gb(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class ResourceRequestsArgsDict(TypedDict):
    
    cpu: pulumi.Input[_builtins.float]
    memory_in_gb: pulumi.Input[_builtins.float]


@pulumi.input_type
class ResourceRequestsArgs:
    def __init__(__self__, *, cpu: pulumi.Input[_builtins.float], memory_in_gb: pulumi.Input[_builtins.float]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @cpu.setter
    def cpu(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryInGB")
    def memory_in_gb(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @memory_in_gb.setter
    def memory_in_gb(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    


class ResourceRequirementsArgsDict(TypedDict):
    
    requests: pulumi.Input[ResourceRequestsArgsDict]
    limits: NotRequired[pulumi.Input[ResourceLimitsArgsDict]]


@pulumi.input_type
class ResourceRequirementsArgs:
    def __init__(__self__, *, requests: pulumi.Input[ResourceRequestsArgs], limits: Optional[pulumi.Input[ResourceLimitsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requests(self) -> pulumi.Input[ResourceRequestsArgs]:
        
        ...
    
    @requests.setter
    def requests(self, value: pulumi.Input[ResourceRequestsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[pulumi.Input[ResourceLimitsArgs]]:
        
        ...
    
    @limits.setter
    def limits(self, value: Optional[pulumi.Input[ResourceLimitsArgs]]): # -> None:
        ...
    


class SecretResourcePropertiesArgsDict(TypedDict):
    
    kind: pulumi.Input[_builtins.str]
    content_type: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecretResourcePropertiesArgs:
    def __init__(__self__, *, kind: pulumi.Input[_builtins.str], content_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def kind(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kind.setter
    def kind(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ServiceResourceDescriptionArgsDict(TypedDict):
    
    code_packages: pulumi.Input[Sequence[pulumi.Input[ContainerCodePackagePropertiesArgsDict]]]
    os_type: pulumi.Input[Union[_builtins.str, OperatingSystemType]]
    auto_scaling_policies: NotRequired[pulumi.Input[Sequence[pulumi.Input[AutoScalingPolicyArgsDict]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    diagnostics: NotRequired[pulumi.Input[DiagnosticsRefArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    network_refs: NotRequired[pulumi.Input[Sequence[pulumi.Input[NetworkRefArgsDict]]]]
    replica_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ServiceResourceDescriptionArgs:
    def __init__(__self__, *, code_packages: pulumi.Input[Sequence[pulumi.Input[ContainerCodePackagePropertiesArgs]]], os_type: pulumi.Input[Union[_builtins.str, OperatingSystemType]], auto_scaling_policies: Optional[pulumi.Input[Sequence[pulumi.Input[AutoScalingPolicyArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., diagnostics: Optional[pulumi.Input[DiagnosticsRefArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., network_refs: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkRefArgs]]]] = ..., replica_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codePackages")
    def code_packages(self) -> pulumi.Input[Sequence[pulumi.Input[ContainerCodePackagePropertiesArgs]]]:
        
        ...
    
    @code_packages.setter
    def code_packages(self, value: pulumi.Input[Sequence[pulumi.Input[ContainerCodePackagePropertiesArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[Union[_builtins.str, OperatingSystemType]]:
        
        ...
    
    @os_type.setter
    def os_type(self, value: pulumi.Input[Union[_builtins.str, OperatingSystemType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoScalingPolicies")
    def auto_scaling_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AutoScalingPolicyArgs]]]]:
        
        ...
    
    @auto_scaling_policies.setter
    def auto_scaling_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AutoScalingPolicyArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def diagnostics(self) -> Optional[pulumi.Input[DiagnosticsRefArgs]]:
        
        ...
    
    @diagnostics.setter
    def diagnostics(self, value: Optional[pulumi.Input[DiagnosticsRefArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkRefs")
    def network_refs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[NetworkRefArgs]]]]:
        
        ...
    
    @network_refs.setter
    def network_refs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[NetworkRefArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replicaCount")
    def replica_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @replica_count.setter
    def replica_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class SettingArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SettingArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class TcpConfigArgsDict(TypedDict):
    
    destination: pulumi.Input[GatewayDestinationArgsDict]
    name: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]


@pulumi.input_type
class TcpConfigArgs:
    def __init__(__self__, *, destination: pulumi.Input[GatewayDestinationArgs], name: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[GatewayDestinationArgs]:
        
        ...
    
    @destination.setter
    def destination(self, value: pulumi.Input[GatewayDestinationArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class VolumeProviderParametersAzureFileArgsDict(TypedDict):
    
    account_name: pulumi.Input[_builtins.str]
    share_name: pulumi.Input[_builtins.str]
    account_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class VolumeProviderParametersAzureFileArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], share_name: pulumi.Input[_builtins.str], account_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareName")
    def share_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @share_name.setter
    def share_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountKey")
    def account_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_key.setter
    def account_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class VolumeReferenceArgsDict(TypedDict):
    
    destination_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VolumeReferenceArgs:
    def __init__(__self__, *, destination_path: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str], read_only: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationPath")
    def destination_path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @destination_path.setter
    def destination_path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


