import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DomainMappingMetadata",
    "DomainMappingSpec",
    "DomainMappingStatus",
    "DomainMappingStatusCondition",
    "DomainMappingStatusResourceRecord",
    "IamBindingCondition",
    "IamMemberCondition",
    "ServiceMetadata",
    "ServiceStatus",
    "ServiceStatusCondition",
    "ServiceStatusTraffic",
    "ServiceTemplate",
    "ServiceTemplateMetadata",
    "ServiceTemplateSpec",
    "ServiceTemplateSpecContainer",
    "ServiceTemplateSpecContainerEnv",
    "ServiceTemplateSpecContainerEnvFrom",
    "ServiceTemplateSpecContainerEnvFromConfigMapRef",
    ...,
    "ServiceTemplateSpecContainerEnvFromSecretRef",
    ...,
    "ServiceTemplateSpecContainerEnvValueFrom",
    ...,
    "ServiceTemplateSpecContainerLivenessProbe",
    "ServiceTemplateSpecContainerLivenessProbeGrpc",
    "ServiceTemplateSpecContainerLivenessProbeHttpGet",
    ...,
    "ServiceTemplateSpecContainerPort",
    "ServiceTemplateSpecContainerReadinessProbe",
    "ServiceTemplateSpecContainerReadinessProbeGrpc",
    "ServiceTemplateSpecContainerReadinessProbeHttpGet",
    "ServiceTemplateSpecContainerResources",
    "ServiceTemplateSpecContainerStartupProbe",
    "ServiceTemplateSpecContainerStartupProbeGrpc",
    "ServiceTemplateSpecContainerStartupProbeHttpGet",
    ...,
    "ServiceTemplateSpecContainerStartupProbeTcpSocket",
    "ServiceTemplateSpecContainerVolumeMount",
    "ServiceTemplateSpecVolume",
    "ServiceTemplateSpecVolumeCsi",
    "ServiceTemplateSpecVolumeEmptyDir",
    "ServiceTemplateSpecVolumeNfs",
    "ServiceTemplateSpecVolumeSecret",
    "ServiceTemplateSpecVolumeSecretItem",
    "ServiceTraffic",
    "GetServiceMetadataResult",
    "GetServiceStatusResult",
    "GetServiceStatusConditionResult",
    "GetServiceStatusTrafficResult",
    "GetServiceTemplateResult",
    "GetServiceTemplateMetadataResult",
    "GetServiceTemplateSpecResult",
    "GetServiceTemplateSpecContainerResult",
    "GetServiceTemplateSpecContainerEnvResult",
    "GetServiceTemplateSpecContainerEnvFromResult",
    ...,
    ...,
    ...,
    ...,
    "GetServiceTemplateSpecContainerEnvValueFromResult",
    ...,
    "GetServiceTemplateSpecContainerLivenessProbeResult",
    ...,
    ...,
    ...,
    "GetServiceTemplateSpecContainerPortResult",
    ...,
    ...,
    ...,
    "GetServiceTemplateSpecContainerResourceResult",
    "GetServiceTemplateSpecContainerStartupProbeResult",
    ...,
    ...,
    ...,
    ...,
    "GetServiceTemplateSpecContainerVolumeMountResult",
    "GetServiceTemplateSpecVolumeResult",
    "GetServiceTemplateSpecVolumeCsiResult",
    "GetServiceTemplateSpecVolumeEmptyDirResult",
    "GetServiceTemplateSpecVolumeNfResult",
    "GetServiceTemplateSpecVolumeSecretResult",
    "GetServiceTemplateSpecVolumeSecretItemResult",
    "GetServiceTrafficResult",
]

@pulumi.output_type
class DomainMappingMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        namespace: _builtins.str,
        annotations: Optional[Mapping[str, _builtins.str]] = ...,
        effective_annotations: Optional[Mapping[str, _builtins.str]] = ...,
        effective_labels: Optional[Mapping[str, _builtins.str]] = ...,
        generation: Optional[_builtins.int] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        pulumi_labels: Optional[Mapping[str, _builtins.str]] = ...,
        resource_version: Optional[_builtins.str] = ...,
        self_link: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainMappingSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        route_name: _builtins.str,
        certificate_mode: Optional[_builtins.str] = ...,
        force_override: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routeName")
    def route_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="forceOverride")
    def force_override(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DomainMappingStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditions: Optional[Sequence[outputs.DomainMappingStatusCondition]] = ...,
        mapped_route_name: Optional[_builtins.str] = ...,
        observed_generation: Optional[_builtins.int] = ...,
        resource_records: Optional[
            Sequence[outputs.DomainMappingStatusResourceRecord]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[Sequence[outputs.DomainMappingStatusCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="mappedRouteName")
    def mapped_route_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="resourceRecords")
    def resource_records(
        self,
    ) -> Optional[Sequence[outputs.DomainMappingStatusResourceRecord]]: ...

@pulumi.output_type
class DomainMappingStatusCondition(dict):
    def __init__(
        __self__,
        *,
        message: Optional[_builtins.str] = ...,
        reason: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainMappingStatusResourceRecord(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        rrdata: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def rrdata(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IamBindingCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IamMemberCondition(dict):
    def __init__(
        __self__,
        *,
        expression: _builtins.str,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        annotations: Optional[Mapping[str, _builtins.str]] = ...,
        effective_annotations: Optional[Mapping[str, _builtins.str]] = ...,
        effective_labels: Optional[Mapping[str, _builtins.str]] = ...,
        generation: Optional[_builtins.int] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        namespace: Optional[_builtins.str] = ...,
        pulumi_labels: Optional[Mapping[str, _builtins.str]] = ...,
        resource_version: Optional[_builtins.str] = ...,
        self_link: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceStatus(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditions: Optional[Sequence[outputs.ServiceStatusCondition]] = ...,
        latest_created_revision_name: Optional[_builtins.str] = ...,
        latest_ready_revision_name: Optional[_builtins.str] = ...,
        observed_generation: Optional[_builtins.int] = ...,
        traffics: Optional[Sequence[outputs.ServiceStatusTraffic]] = ...,
        url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence[outputs.ServiceStatusCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="latestCreatedRevisionName")
    def latest_created_revision_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="latestReadyRevisionName")
    def latest_ready_revision_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def traffics(self) -> Optional[Sequence[outputs.ServiceStatusTraffic]]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceStatusCondition(dict):
    def __init__(
        __self__,
        *,
        message: Optional[_builtins.str] = ...,
        reason: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceStatusTraffic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        latest_revision: Optional[_builtins.bool] = ...,
        percent: Optional[_builtins.int] = ...,
        revision_name: Optional[_builtins.str] = ...,
        tag: Optional[_builtins.str] = ...,
        url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="revisionName")
    def revision_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplate(dict):
    def __init__(
        __self__,
        *,
        metadata: Optional[outputs.ServiceTemplateMetadata] = ...,
        spec: Optional[outputs.ServiceTemplateSpec] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[outputs.ServiceTemplateMetadata]: ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[outputs.ServiceTemplateSpec]: ...

@pulumi.output_type
class ServiceTemplateMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        annotations: Optional[Mapping[str, _builtins.str]] = ...,
        generation: Optional[_builtins.int] = ...,
        labels: Optional[Mapping[str, _builtins.str]] = ...,
        name: Optional[_builtins.str] = ...,
        namespace: Optional[_builtins.str] = ...,
        resource_version: Optional[_builtins.str] = ...,
        self_link: Optional[_builtins.str] = ...,
        uid: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_concurrency: Optional[_builtins.int] = ...,
        containers: Optional[Sequence[outputs.ServiceTemplateSpecContainer]] = ...,
        node_selector: Optional[Mapping[str, _builtins.str]] = ...,
        service_account_name: Optional[_builtins.str] = ...,
        serving_state: Optional[_builtins.str] = ...,
        timeout_seconds: Optional[_builtins.int] = ...,
        volumes: Optional[Sequence[outputs.ServiceTemplateSpecVolume]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerConcurrency")
    def container_concurrency(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[Sequence[outputs.ServiceTemplateSpecContainer]]: ...
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="servingState")
    @_utilities.deprecated(...)
    def serving_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence[outputs.ServiceTemplateSpecVolume]]: ...

@pulumi.output_type
class ServiceTemplateSpecContainer(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        image: _builtins.str,
        args: Optional[Sequence[_builtins.str]] = ...,
        commands: Optional[Sequence[_builtins.str]] = ...,
        env_froms: Optional[
            Sequence[outputs.ServiceTemplateSpecContainerEnvFrom]
        ] = ...,
        envs: Optional[Sequence[outputs.ServiceTemplateSpecContainerEnv]] = ...,
        liveness_probe: Optional[
            outputs.ServiceTemplateSpecContainerLivenessProbe
        ] = ...,
        name: Optional[_builtins.str] = ...,
        ports: Optional[Sequence[outputs.ServiceTemplateSpecContainerPort]] = ...,
        readiness_probe: Optional[
            outputs.ServiceTemplateSpecContainerReadinessProbe
        ] = ...,
        resources: Optional[outputs.ServiceTemplateSpecContainerResources] = ...,
        startup_probe: Optional[outputs.ServiceTemplateSpecContainerStartupProbe] = ...,
        volume_mounts: Optional[
            Sequence[outputs.ServiceTemplateSpecContainerVolumeMount]
        ] = ...,
        working_dir: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="envFroms")
    @_utilities.deprecated(...)
    def env_froms(
        self,
    ) -> Optional[Sequence[outputs.ServiceTemplateSpecContainerEnvFrom]]: ...
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Optional[Sequence[outputs.ServiceTemplateSpecContainerEnv]]: ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerLivenessProbe]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[Sequence[outputs.ServiceTemplateSpecContainerPort]]: ...
    @_builtins.property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerReadinessProbe]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> Optional[outputs.ServiceTemplateSpecContainerResources]: ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerStartupProbe]: ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[Sequence[outputs.ServiceTemplateSpecContainerVolumeMount]]: ...
    @_builtins.property
    @pulumi.getter(name="workingDir")
    @_utilities.deprecated(...)
    def working_dir(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerEnv(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
        value_from: Optional[outputs.ServiceTemplateSpecContainerEnvValueFrom] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="valueFrom")
    def value_from(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerEnvValueFrom]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerEnvFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        config_map_ref: Optional[
            outputs.ServiceTemplateSpecContainerEnvFromConfigMapRef
        ] = ...,
        prefix: Optional[_builtins.str] = ...,
        secret_ref: Optional[
            outputs.ServiceTemplateSpecContainerEnvFromSecretRef
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configMapRef")
    def config_map_ref(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerEnvFromConfigMapRef]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerEnvFromSecretRef]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerEnvFromConfigMapRef(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        local_object_reference: Optional[
            outputs.ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReference
        ] = ...,
        optional: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localObjectReference")
    def local_object_reference(
        self,
    ) -> Optional[
        outputs.ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReference
    ]: ...
    @_builtins.property
    @pulumi.getter
    def optional(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReference(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceTemplateSpecContainerEnvFromSecretRef(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        local_object_reference: Optional[
            outputs.ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReference
        ] = ...,
        optional: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localObjectReference")
    def local_object_reference(
        self,
    ) -> Optional[
        outputs.ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReference
    ]: ...
    @_builtins.property
    @pulumi.getter
    def optional(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReference(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceTemplateSpecContainerEnvValueFrom(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_key_ref: outputs.ServiceTemplateSpecContainerEnvValueFromSecretKeyRef,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretKeyRef")
    def secret_key_ref(
        self,
    ) -> outputs.ServiceTemplateSpecContainerEnvValueFromSecretKeyRef: ...

@pulumi.output_type
class ServiceTemplateSpecContainerEnvValueFromSecretKeyRef(dict):
    def __init__(__self__, *, key: _builtins.str, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class ServiceTemplateSpecContainerLivenessProbe(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[_builtins.int] = ...,
        grpc: Optional[outputs.ServiceTemplateSpecContainerLivenessProbeGrpc] = ...,
        http_get: Optional[
            outputs.ServiceTemplateSpecContainerLivenessProbeHttpGet
        ] = ...,
        initial_delay_seconds: Optional[_builtins.int] = ...,
        period_seconds: Optional[_builtins.int] = ...,
        timeout_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerLivenessProbeGrpc]: ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerLivenessProbeHttpGet]: ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerLivenessProbeGrpc(dict):
    def __init__(
        __self__,
        *,
        port: Optional[_builtins.int] = ...,
        service: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerLivenessProbeHttpGet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_headers: Optional[
            Sequence[outputs.ServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeader]
        ] = ...,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        Sequence[outputs.ServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeader]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeader(dict):
    def __init__(
        __self__, *, name: _builtins.str, value: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerPort(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        container_port: Optional[_builtins.int] = ...,
        name: Optional[_builtins.str] = ...,
        protocol: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerReadinessProbe(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[_builtins.int] = ...,
        grpc: Optional[outputs.ServiceTemplateSpecContainerReadinessProbeGrpc] = ...,
        http_get: Optional[
            outputs.ServiceTemplateSpecContainerReadinessProbeHttpGet
        ] = ...,
        period_seconds: Optional[_builtins.int] = ...,
        success_threshold: Optional[_builtins.int] = ...,
        timeout_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerReadinessProbeGrpc]: ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerReadinessProbeHttpGet]: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerReadinessProbeGrpc(dict):
    def __init__(
        __self__,
        *,
        port: Optional[_builtins.int] = ...,
        service: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerReadinessProbeHttpGet(dict):
    def __init__(
        __self__,
        *,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerResources(dict):
    def __init__(
        __self__,
        *,
        limits: Optional[Mapping[str, _builtins.str]] = ...,
        requests: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerStartupProbe(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[_builtins.int] = ...,
        grpc: Optional[outputs.ServiceTemplateSpecContainerStartupProbeGrpc] = ...,
        http_get: Optional[
            outputs.ServiceTemplateSpecContainerStartupProbeHttpGet
        ] = ...,
        initial_delay_seconds: Optional[_builtins.int] = ...,
        period_seconds: Optional[_builtins.int] = ...,
        tcp_socket: Optional[
            outputs.ServiceTemplateSpecContainerStartupProbeTcpSocket
        ] = ...,
        timeout_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerStartupProbeGrpc]: ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerStartupProbeHttpGet]: ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[outputs.ServiceTemplateSpecContainerStartupProbeTcpSocket]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerStartupProbeGrpc(dict):
    def __init__(
        __self__,
        *,
        port: Optional[_builtins.int] = ...,
        service: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerStartupProbeHttpGet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        http_headers: Optional[
            Sequence[outputs.ServiceTemplateSpecContainerStartupProbeHttpGetHttpHeader]
        ] = ...,
        path: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        Sequence[outputs.ServiceTemplateSpecContainerStartupProbeHttpGetHttpHeader]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerStartupProbeHttpGetHttpHeader(dict):
    def __init__(
        __self__, *, name: _builtins.str, value: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerStartupProbeTcpSocket(dict):
    def __init__(__self__, *, port: Optional[_builtins.int] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServiceTemplateSpecContainerVolumeMount(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        mount_path: _builtins.str,
        name: _builtins.str,
        sub_path: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpecVolume(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        csi: Optional[outputs.ServiceTemplateSpecVolumeCsi] = ...,
        empty_dir: Optional[outputs.ServiceTemplateSpecVolumeEmptyDir] = ...,
        nfs: Optional[outputs.ServiceTemplateSpecVolumeNfs] = ...,
        secret: Optional[outputs.ServiceTemplateSpecVolumeSecret] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def csi(self) -> Optional[outputs.ServiceTemplateSpecVolumeCsi]: ...
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(self) -> Optional[outputs.ServiceTemplateSpecVolumeEmptyDir]: ...
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[outputs.ServiceTemplateSpecVolumeNfs]: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[outputs.ServiceTemplateSpecVolumeSecret]: ...

@pulumi.output_type
class ServiceTemplateSpecVolumeCsi(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        driver: _builtins.str,
        read_only: Optional[_builtins.bool] = ...,
        volume_attributes: Optional[Mapping[str, _builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def driver(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="volumeAttributes")
    def volume_attributes(self) -> Optional[Mapping[str, _builtins.str]]: ...

@pulumi.output_type
class ServiceTemplateSpecVolumeEmptyDir(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        medium: Optional[_builtins.str] = ...,
        size_limit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ServiceTemplateSpecVolumeNfs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        server: _builtins.str,
        read_only: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ServiceTemplateSpecVolumeSecret(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_name: _builtins.str,
        default_mode: Optional[_builtins.int] = ...,
        items: Optional[Sequence[outputs.ServiceTemplateSpecVolumeSecretItem]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[Sequence[outputs.ServiceTemplateSpecVolumeSecretItem]]: ...

@pulumi.output_type
class ServiceTemplateSpecVolumeSecretItem(dict):
    def __init__(
        __self__,
        *,
        key: _builtins.str,
        path: _builtins.str,
        mode: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ServiceTraffic(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        percent: _builtins.int,
        latest_revision: Optional[_builtins.bool] = ...,
        revision_name: Optional[_builtins.str] = ...,
        tag: Optional[_builtins.str] = ...,
        url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="revisionName")
    def revision_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetServiceMetadataResult(dict):
    def __init__(
        __self__,
        *,
        annotations: Mapping[str, _builtins.str],
        effective_annotations: Mapping[str, _builtins.str],
        effective_labels: Mapping[str, _builtins.str],
        generation: _builtins.int,
        labels: Mapping[str, _builtins.str],
        namespace: _builtins.str,
        pulumi_labels: Mapping[str, _builtins.str],
        resource_version: _builtins.str,
        self_link: _builtins.str,
        uid: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceStatusResult(dict):
    def __init__(
        __self__,
        *,
        conditions: Sequence[outputs.GetServiceStatusConditionResult],
        latest_created_revision_name: _builtins.str,
        latest_ready_revision_name: _builtins.str,
        observed_generation: _builtins.int,
        traffics: Sequence[outputs.GetServiceStatusTrafficResult],
        url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.GetServiceStatusConditionResult]: ...
    @_builtins.property
    @pulumi.getter(name="latestCreatedRevisionName")
    def latest_created_revision_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="latestReadyRevisionName")
    def latest_ready_revision_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def traffics(self) -> Sequence[outputs.GetServiceStatusTrafficResult]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceStatusConditionResult(dict):
    def __init__(
        __self__,
        *,
        message: _builtins.str,
        reason: _builtins.str,
        status: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceStatusTrafficResult(dict):
    def __init__(
        __self__,
        *,
        latest_revision: _builtins.bool,
        percent: _builtins.int,
        revision_name: _builtins.str,
        tag: _builtins.str,
        url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="revisionName")
    def revision_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateResult(dict):
    def __init__(
        __self__,
        *,
        metadatas: Sequence[outputs.GetServiceTemplateMetadataResult],
        specs: Sequence[outputs.GetServiceTemplateSpecResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadatas(self) -> Sequence[outputs.GetServiceTemplateMetadataResult]: ...
    @_builtins.property
    @pulumi.getter
    def specs(self) -> Sequence[outputs.GetServiceTemplateSpecResult]: ...

@pulumi.output_type
class GetServiceTemplateMetadataResult(dict):
    def __init__(
        __self__,
        *,
        annotations: Mapping[str, _builtins.str],
        generation: _builtins.int,
        labels: Mapping[str, _builtins.str],
        name: _builtins.str,
        namespace: _builtins.str,
        resource_version: _builtins.str,
        self_link: _builtins.str,
        uid: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecResult(dict):
    def __init__(
        __self__,
        *,
        container_concurrency: _builtins.int,
        containers: Sequence[outputs.GetServiceTemplateSpecContainerResult],
        node_selector: Mapping[str, _builtins.str],
        service_account_name: _builtins.str,
        serving_state: _builtins.str,
        timeout_seconds: _builtins.int,
        volumes: Sequence[outputs.GetServiceTemplateSpecVolumeResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerConcurrency")
    def container_concurrency(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def containers(self) -> Sequence[outputs.GetServiceTemplateSpecContainerResult]: ...
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="servingState")
    def serving_state(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Sequence[outputs.GetServiceTemplateSpecVolumeResult]: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerResult(dict):
    def __init__(
        __self__,
        *,
        args: Sequence[_builtins.str],
        commands: Sequence[_builtins.str],
        env_froms: Sequence[outputs.GetServiceTemplateSpecContainerEnvFromResult],
        envs: Sequence[outputs.GetServiceTemplateSpecContainerEnvResult],
        image: _builtins.str,
        liveness_probes: Sequence[
            outputs.GetServiceTemplateSpecContainerLivenessProbeResult
        ],
        name: _builtins.str,
        ports: Sequence[outputs.GetServiceTemplateSpecContainerPortResult],
        readiness_probes: Sequence[
            outputs.GetServiceTemplateSpecContainerReadinessProbeResult
        ],
        resources: Sequence[outputs.GetServiceTemplateSpecContainerResourceResult],
        startup_probes: Sequence[
            outputs.GetServiceTemplateSpecContainerStartupProbeResult
        ],
        volume_mounts: Sequence[
            outputs.GetServiceTemplateSpecContainerVolumeMountResult
        ],
        working_dir: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="envFroms")
    def env_froms(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerEnvFromResult]: ...
    @_builtins.property
    @pulumi.getter
    def envs(self) -> Sequence[outputs.GetServiceTemplateSpecContainerEnvResult]: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="livenessProbes")
    def liveness_probes(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerLivenessProbeResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Sequence[outputs.GetServiceTemplateSpecContainerPortResult]: ...
    @_builtins.property
    @pulumi.getter(name="readinessProbes")
    def readiness_probes(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerReadinessProbeResult]: ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerResourceResult]: ...
    @_builtins.property
    @pulumi.getter(name="startupProbes")
    def startup_probes(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerStartupProbeResult]: ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerVolumeMountResult]: ...
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerEnvResult(dict):
    def __init__(
        __self__,
        *,
        name: _builtins.str,
        value: _builtins.str,
        value_froms: Sequence[
            outputs.GetServiceTemplateSpecContainerEnvValueFromResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="valueFroms")
    def value_froms(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerEnvValueFromResult]: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerEnvFromResult(dict):
    def __init__(
        __self__,
        *,
        config_map_reves: Sequence[
            outputs.GetServiceTemplateSpecContainerEnvFromConfigMapRefResult
        ],
        prefix: _builtins.str,
        secret_reves: Sequence[
            outputs.GetServiceTemplateSpecContainerEnvFromSecretRefResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configMapReves")
    def config_map_reves(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerEnvFromConfigMapRefResult]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretReves")
    def secret_reves(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerEnvFromSecretRefResult]: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerEnvFromConfigMapRefResult(dict):
    def __init__(
        __self__,
        *,
        local_object_references: Sequence[
            outputs.GetServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReferenceResult
        ],
        optional: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localObjectReferences")
    def local_object_references(
        self,
    ) -> Sequence[
        outputs.GetServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReferenceResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def optional(self) -> _builtins.bool: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReferenceResult(
    dict
):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerEnvFromSecretRefResult(dict):
    def __init__(
        __self__,
        *,
        local_object_references: Sequence[
            outputs.GetServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceResult
        ],
        optional: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localObjectReferences")
    def local_object_references(
        self,
    ) -> Sequence[
        outputs.GetServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def optional(self) -> _builtins.bool: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerEnvValueFromResult(dict):
    def __init__(
        __self__,
        *,
        secret_key_reves: Sequence[
            outputs.GetServiceTemplateSpecContainerEnvValueFromSecretKeyRefResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretKeyReves")
    def secret_key_reves(
        self,
    ) -> Sequence[
        outputs.GetServiceTemplateSpecContainerEnvValueFromSecretKeyRefResult
    ]: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerEnvValueFromSecretKeyRefResult(dict):
    def __init__(__self__, *, key: _builtins.str, name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerLivenessProbeResult(dict):
    def __init__(
        __self__,
        *,
        failure_threshold: _builtins.int,
        grpcs: Sequence[outputs.GetServiceTemplateSpecContainerLivenessProbeGrpcResult],
        http_gets: Sequence[
            outputs.GetServiceTemplateSpecContainerLivenessProbeHttpGetResult
        ],
        initial_delay_seconds: _builtins.int,
        period_seconds: _builtins.int,
        timeout_seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def grpcs(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerLivenessProbeGrpcResult]: ...
    @_builtins.property
    @pulumi.getter(name="httpGets")
    def http_gets(
        self,
    ) -> Sequence[
        outputs.GetServiceTemplateSpecContainerLivenessProbeHttpGetResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerLivenessProbeGrpcResult(dict):
    def __init__(__self__, *, port: _builtins.int, service: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerLivenessProbeHttpGetResult(dict):
    def __init__(
        __self__,
        *,
        http_headers: Sequence[
            outputs.GetServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeaderResult
        ],
        path: _builtins.str,
        port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Sequence[
        outputs.GetServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeaderResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerPortResult(dict):
    def __init__(
        __self__,
        *,
        container_port: _builtins.int,
        name: _builtins.str,
        protocol: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerReadinessProbeResult(dict):
    def __init__(
        __self__,
        *,
        failure_threshold: _builtins.int,
        grpcs: Sequence[
            outputs.GetServiceTemplateSpecContainerReadinessProbeGrpcResult
        ],
        http_gets: Sequence[
            outputs.GetServiceTemplateSpecContainerReadinessProbeHttpGetResult
        ],
        period_seconds: _builtins.int,
        success_threshold: _builtins.int,
        timeout_seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def grpcs(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerReadinessProbeGrpcResult]: ...
    @_builtins.property
    @pulumi.getter(name="httpGets")
    def http_gets(
        self,
    ) -> Sequence[
        outputs.GetServiceTemplateSpecContainerReadinessProbeHttpGetResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerReadinessProbeGrpcResult(dict):
    def __init__(__self__, *, port: _builtins.int, service: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerReadinessProbeHttpGetResult(dict):
    def __init__(__self__, *, path: _builtins.str, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerResourceResult(dict):
    def __init__(
        __self__,
        *,
        limits: Mapping[str, _builtins.str],
        requests: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(self) -> Mapping[str, _builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def requests(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerStartupProbeResult(dict):
    def __init__(
        __self__,
        *,
        failure_threshold: _builtins.int,
        grpcs: Sequence[outputs.GetServiceTemplateSpecContainerStartupProbeGrpcResult],
        http_gets: Sequence[
            outputs.GetServiceTemplateSpecContainerStartupProbeHttpGetResult
        ],
        initial_delay_seconds: _builtins.int,
        period_seconds: _builtins.int,
        tcp_sockets: Sequence[
            outputs.GetServiceTemplateSpecContainerStartupProbeTcpSocketResult
        ],
        timeout_seconds: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def grpcs(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerStartupProbeGrpcResult]: ...
    @_builtins.property
    @pulumi.getter(name="httpGets")
    def http_gets(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecContainerStartupProbeHttpGetResult]: ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="tcpSockets")
    def tcp_sockets(
        self,
    ) -> Sequence[
        outputs.GetServiceTemplateSpecContainerStartupProbeTcpSocketResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> _builtins.int: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerStartupProbeGrpcResult(dict):
    def __init__(__self__, *, port: _builtins.int, service: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerStartupProbeHttpGetResult(dict):
    def __init__(
        __self__,
        *,
        http_headers: Sequence[
            outputs.GetServiceTemplateSpecContainerStartupProbeHttpGetHttpHeaderResult
        ],
        path: _builtins.str,
        port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Sequence[
        outputs.GetServiceTemplateSpecContainerStartupProbeHttpGetHttpHeaderResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerStartupProbeHttpGetHttpHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerStartupProbeTcpSocketResult(dict):
    def __init__(__self__, *, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class GetServiceTemplateSpecContainerVolumeMountResult(dict):
    def __init__(
        __self__,
        *,
        mount_path: _builtins.str,
        name: _builtins.str,
        sub_path: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecVolumeResult(dict):
    def __init__(
        __self__,
        *,
        csis: Sequence[outputs.GetServiceTemplateSpecVolumeCsiResult],
        empty_dirs: Sequence[outputs.GetServiceTemplateSpecVolumeEmptyDirResult],
        name: _builtins.str,
        nfs: Sequence[outputs.GetServiceTemplateSpecVolumeNfResult],
        secrets: Sequence[outputs.GetServiceTemplateSpecVolumeSecretResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def csis(self) -> Sequence[outputs.GetServiceTemplateSpecVolumeCsiResult]: ...
    @_builtins.property
    @pulumi.getter(name="emptyDirs")
    def empty_dirs(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecVolumeEmptyDirResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Sequence[outputs.GetServiceTemplateSpecVolumeNfResult]: ...
    @_builtins.property
    @pulumi.getter
    def secrets(self) -> Sequence[outputs.GetServiceTemplateSpecVolumeSecretResult]: ...

@pulumi.output_type
class GetServiceTemplateSpecVolumeCsiResult(dict):
    def __init__(
        __self__,
        *,
        driver: _builtins.str,
        read_only: _builtins.bool,
        volume_attributes: Mapping[str, _builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def driver(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="volumeAttributes")
    def volume_attributes(self) -> Mapping[str, _builtins.str]: ...

@pulumi.output_type
class GetServiceTemplateSpecVolumeEmptyDirResult(dict):
    def __init__(
        __self__, *, medium: _builtins.str, size_limit: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecVolumeNfResult(dict):
    def __init__(
        __self__,
        *,
        path: _builtins.str,
        read_only: _builtins.bool,
        server: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecVolumeSecretResult(dict):
    def __init__(
        __self__,
        *,
        default_mode: _builtins.int,
        items: Sequence[outputs.GetServiceTemplateSpecVolumeSecretItemResult],
        secret_name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Sequence[outputs.GetServiceTemplateSpecVolumeSecretItemResult]: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTemplateSpecVolumeSecretItemResult(dict):
    def __init__(
        __self__, *, key: _builtins.str, mode: _builtins.int, path: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> _builtins.str: ...

@pulumi.output_type
class GetServiceTrafficResult(dict):
    def __init__(
        __self__,
        *,
        latest_revision: _builtins.bool,
        percent: _builtins.int,
        revision_name: _builtins.str,
        tag: _builtins.str,
        url: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="revisionName")
    def revision_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> _builtins.str: ...
