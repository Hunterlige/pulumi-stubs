import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict
from .. import _utilities

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DomainMappingMetadataArgs",
    "DomainMappingMetadataArgsDict",
    "DomainMappingSpecArgs",
    "DomainMappingSpecArgsDict",
    "DomainMappingStatusArgs",
    "DomainMappingStatusArgsDict",
    "DomainMappingStatusConditionArgs",
    "DomainMappingStatusConditionArgsDict",
    "DomainMappingStatusResourceRecordArgs",
    "DomainMappingStatusResourceRecordArgsDict",
    "IamBindingConditionArgs",
    "IamBindingConditionArgsDict",
    "IamMemberConditionArgs",
    "IamMemberConditionArgsDict",
    "ServiceMetadataArgs",
    "ServiceMetadataArgsDict",
    "ServiceStatusArgs",
    "ServiceStatusArgsDict",
    "ServiceStatusConditionArgs",
    "ServiceStatusConditionArgsDict",
    "ServiceStatusTrafficArgs",
    "ServiceStatusTrafficArgsDict",
    "ServiceTemplateArgs",
    "ServiceTemplateArgsDict",
    "ServiceTemplateMetadataArgs",
    "ServiceTemplateMetadataArgsDict",
    "ServiceTemplateSpecArgs",
    "ServiceTemplateSpecArgsDict",
    "ServiceTemplateSpecContainerArgs",
    "ServiceTemplateSpecContainerArgsDict",
    "ServiceTemplateSpecContainerEnvArgs",
    "ServiceTemplateSpecContainerEnvArgsDict",
    "ServiceTemplateSpecContainerEnvFromArgs",
    "ServiceTemplateSpecContainerEnvFromArgsDict",
    ...,
    ...,
    ...,
    ...,
    "ServiceTemplateSpecContainerEnvFromSecretRefArgs",
    ...,
    ...,
    ...,
    "ServiceTemplateSpecContainerEnvValueFromArgs",
    "ServiceTemplateSpecContainerEnvValueFromArgsDict",
    ...,
    ...,
    "ServiceTemplateSpecContainerLivenessProbeArgs",
    "ServiceTemplateSpecContainerLivenessProbeArgsDict",
    "ServiceTemplateSpecContainerLivenessProbeGrpcArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServiceTemplateSpecContainerPortArgs",
    "ServiceTemplateSpecContainerPortArgsDict",
    "ServiceTemplateSpecContainerReadinessProbeArgs",
    "ServiceTemplateSpecContainerReadinessProbeArgsDict",
    "ServiceTemplateSpecContainerReadinessProbeGrpcArgs",
    ...,
    ...,
    ...,
    "ServiceTemplateSpecContainerResourcesArgs",
    "ServiceTemplateSpecContainerResourcesArgsDict",
    "ServiceTemplateSpecContainerStartupProbeArgs",
    "ServiceTemplateSpecContainerStartupProbeArgsDict",
    "ServiceTemplateSpecContainerStartupProbeGrpcArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ServiceTemplateSpecContainerVolumeMountArgs",
    "ServiceTemplateSpecContainerVolumeMountArgsDict",
    "ServiceTemplateSpecVolumeArgs",
    "ServiceTemplateSpecVolumeArgsDict",
    "ServiceTemplateSpecVolumeCsiArgs",
    "ServiceTemplateSpecVolumeCsiArgsDict",
    "ServiceTemplateSpecVolumeEmptyDirArgs",
    "ServiceTemplateSpecVolumeEmptyDirArgsDict",
    "ServiceTemplateSpecVolumeNfsArgs",
    "ServiceTemplateSpecVolumeNfsArgsDict",
    "ServiceTemplateSpecVolumeSecretArgs",
    "ServiceTemplateSpecVolumeSecretArgsDict",
    "ServiceTemplateSpecVolumeSecretItemArgs",
    "ServiceTemplateSpecVolumeSecretItemArgsDict",
    "ServiceTrafficArgs",
    "ServiceTrafficArgsDict",
]

class DomainMappingMetadataArgsDict(TypedDict):
    namespace: pulumi.Input[_builtins.str]
    annotations: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    effective_annotations: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    effective_labels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    pulumi_labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    resource_version: NotRequired[pulumi.Input[_builtins.str]]
    self_link: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainMappingMetadataArgs:
    def __init__(
        __self__,
        *,
        namespace: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_version: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[_builtins.str]: ...
    @namespace.setter
    def namespace(self, value: pulumi.Input[_builtins.str]): ...
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
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_version.setter
    def resource_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainMappingSpecArgsDict(TypedDict):
    route_name: pulumi.Input[_builtins.str]
    certificate_mode: NotRequired[pulumi.Input[_builtins.str]]
    force_override: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DomainMappingSpecArgs:
    def __init__(
        __self__,
        *,
        route_name: pulumi.Input[_builtins.str],
        certificate_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        force_override: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="routeName")
    def route_name(self) -> pulumi.Input[_builtins.str]: ...
    @route_name.setter
    def route_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="certificateMode")
    def certificate_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_mode.setter
    def certificate_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceOverride")
    def force_override(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_override.setter
    def force_override(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DomainMappingStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusConditionArgsDict]]]
    ]
    mapped_route_name: NotRequired[pulumi.Input[_builtins.str]]
    observed_generation: NotRequired[pulumi.Input[_builtins.int]]
    resource_records: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusResourceRecordArgsDict]]]
    ]

@pulumi.input_type
class DomainMappingStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusConditionArgs]]]
        ] = ...,
        mapped_route_name: Optional[pulumi.Input[_builtins.str]] = ...,
        observed_generation: Optional[pulumi.Input[_builtins.int]] = ...,
        resource_records: Optional[
            pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusResourceRecordArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusConditionArgs]]]
    ]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="mappedRouteName")
    def mapped_route_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mapped_route_name.setter
    def mapped_route_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @observed_generation.setter
    def observed_generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceRecords")
    def resource_records(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusResourceRecordArgs]]]
    ]: ...
    @resource_records.setter
    def resource_records(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DomainMappingStatusResourceRecordArgs]]]
        ],
    ): ...

class DomainMappingStatusConditionArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainMappingStatusConditionArgs:
    def __init__(
        __self__,
        *,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainMappingStatusResourceRecordArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    rrdata: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DomainMappingStatusResourceRecordArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        rrdata: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def rrdata(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rrdata.setter
    def rrdata(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class IamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class IamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceMetadataArgsDict(TypedDict):
    annotations: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    effective_annotations: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    effective_labels: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    pulumi_labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    resource_version: NotRequired[pulumi.Input[_builtins.str]]
    self_link: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceMetadataArgs:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_version: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
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
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_version.setter
    def resource_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceStatusArgsDict(TypedDict):
    conditions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceStatusConditionArgsDict]]]
    ]
    latest_created_revision_name: NotRequired[pulumi.Input[_builtins.str]]
    latest_ready_revision_name: NotRequired[pulumi.Input[_builtins.str]]
    observed_generation: NotRequired[pulumi.Input[_builtins.int]]
    traffics: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceStatusTrafficArgsDict]]]
    ]
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceStatusArgs:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceStatusConditionArgs]]]
        ] = ...,
        latest_created_revision_name: Optional[pulumi.Input[_builtins.str]] = ...,
        latest_ready_revision_name: Optional[pulumi.Input[_builtins.str]] = ...,
        observed_generation: Optional[pulumi.Input[_builtins.int]] = ...,
        traffics: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceStatusTrafficArgs]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceStatusConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceStatusConditionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="latestCreatedRevisionName")
    def latest_created_revision_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latest_created_revision_name.setter
    def latest_created_revision_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="latestReadyRevisionName")
    def latest_ready_revision_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @latest_ready_revision_name.setter
    def latest_ready_revision_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="observedGeneration")
    def observed_generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @observed_generation.setter
    def observed_generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def traffics(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceStatusTrafficArgs]]]]: ...
    @traffics.setter
    def traffics(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ServiceStatusTrafficArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceStatusConditionArgsDict(TypedDict):
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceStatusConditionArgs:
    def __init__(
        __self__,
        *,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceStatusTrafficArgsDict(TypedDict):
    latest_revision: NotRequired[pulumi.Input[_builtins.bool]]
    percent: NotRequired[pulumi.Input[_builtins.int]]
    revision_name: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceStatusTrafficArgs:
    def __init__(
        __self__,
        *,
        latest_revision: Optional[pulumi.Input[_builtins.bool]] = ...,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
        revision_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @latest_revision.setter
    def latest_revision(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionName")
    def revision_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_name.setter
    def revision_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[ServiceTemplateMetadataArgsDict]]
    spec: NotRequired[pulumi.Input[ServiceTemplateSpecArgsDict]]

@pulumi.input_type
class ServiceTemplateArgs:
    def __init__(
        __self__,
        *,
        metadata: Optional[pulumi.Input[ServiceTemplateMetadataArgs]] = ...,
        spec: Optional[pulumi.Input[ServiceTemplateSpecArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[ServiceTemplateMetadataArgs]]: ...
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[ServiceTemplateMetadataArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input[ServiceTemplateSpecArgs]]: ...
    @spec.setter
    def spec(self, value: Optional[pulumi.Input[ServiceTemplateSpecArgs]]): ...

class ServiceTemplateMetadataArgsDict(TypedDict):
    annotations: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    resource_version: NotRequired[pulumi.Input[_builtins.str]]
    self_link: NotRequired[pulumi.Input[_builtins.str]]
    uid: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateMetadataArgs:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_version: Optional[pulumi.Input[_builtins.str]] = ...,
        self_link: Optional[pulumi.Input[_builtins.str]] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
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
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_version.setter
    def resource_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecArgsDict(TypedDict):
    container_concurrency: NotRequired[pulumi.Input[_builtins.int]]
    containers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerArgsDict]]]
    ]
    node_selector: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    service_account_name: NotRequired[pulumi.Input[_builtins.str]]
    serving_state: NotRequired[pulumi.Input[_builtins.str]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    volumes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecVolumeArgsDict]]]
    ]

@pulumi.input_type
class ServiceTemplateSpecArgs:
    def __init__(
        __self__,
        *,
        container_concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        containers: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerArgs]]]
        ] = ...,
        node_selector: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        service_account_name: Optional[pulumi.Input[_builtins.str]] = ...,
        serving_state: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecVolumeArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerConcurrency")
    def container_concurrency(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_concurrency.setter
    def container_concurrency(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerArgs]]]
    ]: ...
    @containers.setter
    def containers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @node_selector.setter
    def node_selector(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountName")
    def service_account_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_name.setter
    def service_account_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="servingState")
    @_utilities.deprecated(...)
    def serving_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @serving_state.setter
    def serving_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecVolumeArgs]]]
    ]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecVolumeArgs]]]
        ],
    ): ...

class ServiceTemplateSpecContainerArgsDict(TypedDict):
    image: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    env_froms: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceTemplateSpecContainerEnvFromArgsDict]]
        ]
    ]
    envs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerEnvArgsDict]]]
    ]
    liveness_probe: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerLivenessProbeArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ports: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerPortArgsDict]]]
    ]
    readiness_probe: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerReadinessProbeArgsDict]
    ]
    resources: NotRequired[pulumi.Input[ServiceTemplateSpecContainerResourcesArgsDict]]
    startup_probe: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerStartupProbeArgsDict]
    ]
    volume_mounts: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceTemplateSpecContainerVolumeMountArgsDict]]
        ]
    ]
    working_dir: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateSpecContainerArgs:
    def __init__(
        __self__,
        *,
        image: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        env_froms: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateSpecContainerEnvFromArgs]]
            ]
        ] = ...,
        envs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerEnvArgs]]]
        ] = ...,
        liveness_probe: Optional[
            pulumi.Input[ServiceTemplateSpecContainerLivenessProbeArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerPortArgs]]]
        ] = ...,
        readiness_probe: Optional[
            pulumi.Input[ServiceTemplateSpecContainerReadinessProbeArgs]
        ] = ...,
        resources: Optional[
            pulumi.Input[ServiceTemplateSpecContainerResourcesArgs]
        ] = ...,
        startup_probe: Optional[
            pulumi.Input[ServiceTemplateSpecContainerStartupProbeArgs]
        ] = ...,
        volume_mounts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateSpecContainerVolumeMountArgs]]
            ]
        ] = ...,
        working_dir: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]: ...
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="envFroms")
    @_utilities.deprecated(...)
    def env_froms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerEnvFromArgs]]]
    ]: ...
    @env_froms.setter
    def env_froms(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateSpecContainerEnvFromArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerEnvArgs]]]
    ]: ...
    @envs.setter
    def envs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerEnvArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecContainerLivenessProbeArgs]]: ...
    @liveness_probe.setter
    def liveness_probe(
        self,
        value: Optional[pulumi.Input[ServiceTemplateSpecContainerLivenessProbeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerPortArgs]]]
    ]: ...
    @ports.setter
    def ports(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecContainerPortArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecContainerReadinessProbeArgs]]: ...
    @readiness_probe.setter
    def readiness_probe(
        self,
        value: Optional[pulumi.Input[ServiceTemplateSpecContainerReadinessProbeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecContainerResourcesArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[ServiceTemplateSpecContainerResourcesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecContainerStartupProbeArgs]]: ...
    @startup_probe.setter
    def startup_probe(
        self,
        value: Optional[pulumi.Input[ServiceTemplateSpecContainerStartupProbeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceTemplateSpecContainerVolumeMountArgs]]
        ]
    ]: ...
    @volume_mounts.setter
    def volume_mounts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateSpecContainerVolumeMountArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workingDir")
    @_utilities.deprecated(...)
    def working_dir(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @working_dir.setter
    def working_dir(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecContainerEnvArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    value_from: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerEnvValueFromArgsDict]
    ]

@pulumi.input_type
class ServiceTemplateSpecContainerEnvArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
        value_from: Optional[
            pulumi.Input[ServiceTemplateSpecContainerEnvValueFromArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueFrom")
    def value_from(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecContainerEnvValueFromArgs]]: ...
    @value_from.setter
    def value_from(
        self,
        value: Optional[pulumi.Input[ServiceTemplateSpecContainerEnvValueFromArgs]],
    ): ...

class ServiceTemplateSpecContainerEnvFromArgsDict(TypedDict):
    config_map_ref: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerEnvFromConfigMapRefArgsDict]
    ]
    prefix: NotRequired[pulumi.Input[_builtins.str]]
    secret_ref: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerEnvFromSecretRefArgsDict]
    ]

@pulumi.input_type
class ServiceTemplateSpecContainerEnvFromArgs:
    def __init__(
        __self__,
        *,
        config_map_ref: Optional[
            pulumi.Input[ServiceTemplateSpecContainerEnvFromConfigMapRefArgs]
        ] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        secret_ref: Optional[
            pulumi.Input[ServiceTemplateSpecContainerEnvFromSecretRefArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configMapRef")
    def config_map_ref(
        self,
    ) -> Optional[
        pulumi.Input[ServiceTemplateSpecContainerEnvFromConfigMapRefArgs]
    ]: ...
    @config_map_ref.setter
    def config_map_ref(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateSpecContainerEnvFromConfigMapRefArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secretRef")
    def secret_ref(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecContainerEnvFromSecretRefArgs]]: ...
    @secret_ref.setter
    def secret_ref(
        self,
        value: Optional[pulumi.Input[ServiceTemplateSpecContainerEnvFromSecretRefArgs]],
    ): ...

class ServiceTemplateSpecContainerEnvFromConfigMapRefArgsDict(TypedDict):
    local_object_reference: NotRequired[
        pulumi.Input[
            ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReferenceArgsDict
        ]
    ]
    optional: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServiceTemplateSpecContainerEnvFromConfigMapRefArgs:
    def __init__(
        __self__,
        *,
        local_object_reference: Optional[
            pulumi.Input[
                ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReferenceArgs
            ]
        ] = ...,
        optional: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localObjectReference")
    def local_object_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReferenceArgs
        ]
    ]: ...
    @local_object_reference.setter
    def local_object_reference(
        self,
        value: Optional[
            pulumi.Input[
                ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReferenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def optional(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @optional.setter
    def optional(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReferenceArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceTemplateSpecContainerEnvFromConfigMapRefLocalObjectReferenceArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ServiceTemplateSpecContainerEnvFromSecretRefArgsDict(TypedDict):
    local_object_reference: NotRequired[
        pulumi.Input[
            ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceArgsDict
        ]
    ]
    optional: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServiceTemplateSpecContainerEnvFromSecretRefArgs:
    def __init__(
        __self__,
        *,
        local_object_reference: Optional[
            pulumi.Input[
                ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceArgs
            ]
        ] = ...,
        optional: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="localObjectReference")
    def local_object_reference(
        self,
    ) -> Optional[
        pulumi.Input[
            ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceArgs
        ]
    ]: ...
    @local_object_reference.setter
    def local_object_reference(
        self,
        value: Optional[
            pulumi.Input[
                ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def optional(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @optional.setter
    def optional(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceTemplateSpecContainerEnvFromSecretRefLocalObjectReferenceArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ServiceTemplateSpecContainerEnvValueFromArgsDict(TypedDict):
    secret_key_ref: pulumi.Input[
        ServiceTemplateSpecContainerEnvValueFromSecretKeyRefArgsDict
    ]

@pulumi.input_type
class ServiceTemplateSpecContainerEnvValueFromArgs:
    def __init__(
        __self__,
        *,
        secret_key_ref: pulumi.Input[
            ServiceTemplateSpecContainerEnvValueFromSecretKeyRefArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretKeyRef")
    def secret_key_ref(
        self,
    ) -> pulumi.Input[ServiceTemplateSpecContainerEnvValueFromSecretKeyRefArgs]: ...
    @secret_key_ref.setter
    def secret_key_ref(
        self,
        value: pulumi.Input[ServiceTemplateSpecContainerEnvValueFromSecretKeyRefArgs],
    ): ...

class ServiceTemplateSpecContainerEnvValueFromSecretKeyRefArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceTemplateSpecContainerEnvValueFromSecretKeyRefArgs:
    def __init__(
        __self__, *, key: pulumi.Input[_builtins.str], name: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class ServiceTemplateSpecContainerLivenessProbeArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerLivenessProbeGrpcArgsDict]
    ]
    http_get: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerLivenessProbeHttpGetArgsDict]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateSpecContainerLivenessProbeArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[ServiceTemplateSpecContainerLivenessProbeGrpcArgs]
        ] = ...,
        http_get: Optional[
            pulumi.Input[ServiceTemplateSpecContainerLivenessProbeHttpGetArgs]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecContainerLivenessProbeGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateSpecContainerLivenessProbeGrpcArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        pulumi.Input[ServiceTemplateSpecContainerLivenessProbeHttpGetArgs]
    ]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateSpecContainerLivenessProbeHttpGetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateSpecContainerLivenessProbeGrpcArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateSpecContainerLivenessProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecContainerLivenessProbeHttpGetArgsDict(TypedDict):
    http_headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeaderArgsDict
                ]
            ]
        ]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateSpecContainerLivenessProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        http_headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeaderArgs
                ]
            ]
        ]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateSpecContainerLivenessProbeHttpGetHttpHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecContainerPortArgsDict(TypedDict):
    container_port: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    protocol: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateSpecContainerPortArgs:
    def __init__(
        __self__,
        *,
        container_port: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_port.setter
    def container_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecContainerReadinessProbeArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerReadinessProbeGrpcArgsDict]
    ]
    http_get: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerReadinessProbeHttpGetArgsDict]
    ]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateSpecContainerReadinessProbeArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[ServiceTemplateSpecContainerReadinessProbeGrpcArgs]
        ] = ...,
        http_get: Optional[
            pulumi.Input[ServiceTemplateSpecContainerReadinessProbeHttpGetArgs]
        ] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        success_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecContainerReadinessProbeGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateSpecContainerReadinessProbeGrpcArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        pulumi.Input[ServiceTemplateSpecContainerReadinessProbeHttpGetArgs]
    ]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateSpecContainerReadinessProbeHttpGetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateSpecContainerReadinessProbeGrpcArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateSpecContainerReadinessProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecContainerReadinessProbeHttpGetArgsDict(TypedDict):
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateSpecContainerReadinessProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateSpecContainerResourcesArgsDict(TypedDict):
    limits: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    requests: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServiceTemplateSpecContainerResourcesArgs:
    def __init__(
        __self__,
        *,
        limits: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        requests: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @limits.setter
    def limits(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def requests(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @requests.setter
    def requests(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceTemplateSpecContainerStartupProbeArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerStartupProbeGrpcArgsDict]
    ]
    http_get: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerStartupProbeHttpGetArgsDict]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[
        pulumi.Input[ServiceTemplateSpecContainerStartupProbeTcpSocketArgsDict]
    ]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateSpecContainerStartupProbeArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[ServiceTemplateSpecContainerStartupProbeGrpcArgs]
        ] = ...,
        http_get: Optional[
            pulumi.Input[ServiceTemplateSpecContainerStartupProbeHttpGetArgs]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_socket: Optional[
            pulumi.Input[ServiceTemplateSpecContainerStartupProbeTcpSocketArgs]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecContainerStartupProbeGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[pulumi.Input[ServiceTemplateSpecContainerStartupProbeGrpcArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        pulumi.Input[ServiceTemplateSpecContainerStartupProbeHttpGetArgs]
    ]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateSpecContainerStartupProbeHttpGetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        pulumi.Input[ServiceTemplateSpecContainerStartupProbeTcpSocketArgs]
    ]: ...
    @tcp_socket.setter
    def tcp_socket(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateSpecContainerStartupProbeTcpSocketArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateSpecContainerStartupProbeGrpcArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateSpecContainerStartupProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecContainerStartupProbeHttpGetArgsDict(TypedDict):
    http_headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceTemplateSpecContainerStartupProbeHttpGetHttpHeaderArgsDict
                ]
            ]
        ]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateSpecContainerStartupProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        http_headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceTemplateSpecContainerStartupProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceTemplateSpecContainerStartupProbeHttpGetHttpHeaderArgs
                ]
            ]
        ]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceTemplateSpecContainerStartupProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateSpecContainerStartupProbeHttpGetHttpHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateSpecContainerStartupProbeHttpGetHttpHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecContainerStartupProbeTcpSocketArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateSpecContainerStartupProbeTcpSocketArgs:
    def __init__(
        __self__, *, port: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateSpecContainerVolumeMountArgsDict(TypedDict):
    mount_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    sub_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateSpecContainerVolumeMountArgs:
    def __init__(
        __self__,
        *,
        mount_path: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        sub_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @mount_path.setter
    def mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sub_path.setter
    def sub_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecVolumeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    csi: NotRequired[pulumi.Input[ServiceTemplateSpecVolumeCsiArgsDict]]
    empty_dir: NotRequired[pulumi.Input[ServiceTemplateSpecVolumeEmptyDirArgsDict]]
    nfs: NotRequired[pulumi.Input[ServiceTemplateSpecVolumeNfsArgsDict]]
    secret: NotRequired[pulumi.Input[ServiceTemplateSpecVolumeSecretArgsDict]]

@pulumi.input_type
class ServiceTemplateSpecVolumeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        csi: Optional[pulumi.Input[ServiceTemplateSpecVolumeCsiArgs]] = ...,
        empty_dir: Optional[pulumi.Input[ServiceTemplateSpecVolumeEmptyDirArgs]] = ...,
        nfs: Optional[pulumi.Input[ServiceTemplateSpecVolumeNfsArgs]] = ...,
        secret: Optional[pulumi.Input[ServiceTemplateSpecVolumeSecretArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def csi(self) -> Optional[pulumi.Input[ServiceTemplateSpecVolumeCsiArgs]]: ...
    @csi.setter
    def csi(self, value: Optional[pulumi.Input[ServiceTemplateSpecVolumeCsiArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateSpecVolumeEmptyDirArgs]]: ...
    @empty_dir.setter
    def empty_dir(
        self, value: Optional[pulumi.Input[ServiceTemplateSpecVolumeEmptyDirArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[pulumi.Input[ServiceTemplateSpecVolumeNfsArgs]]: ...
    @nfs.setter
    def nfs(self, value: Optional[pulumi.Input[ServiceTemplateSpecVolumeNfsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[ServiceTemplateSpecVolumeSecretArgs]]: ...
    @secret.setter
    def secret(
        self, value: Optional[pulumi.Input[ServiceTemplateSpecVolumeSecretArgs]]
    ): ...

class ServiceTemplateSpecVolumeCsiArgsDict(TypedDict):
    driver: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]
    volume_attributes: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class ServiceTemplateSpecVolumeCsiArgs:
    def __init__(
        __self__,
        *,
        driver: pulumi.Input[_builtins.str],
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
        volume_attributes: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def driver(self) -> pulumi.Input[_builtins.str]: ...
    @driver.setter
    def driver(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeAttributes")
    def volume_attributes(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @volume_attributes.setter
    def volume_attributes(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceTemplateSpecVolumeEmptyDirArgsDict(TypedDict):
    medium: NotRequired[pulumi.Input[_builtins.str]]
    size_limit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateSpecVolumeEmptyDirArgs:
    def __init__(
        __self__,
        *,
        medium: Optional[pulumi.Input[_builtins.str]] = ...,
        size_limit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @medium.setter
    def medium(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size_limit.setter
    def size_limit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateSpecVolumeNfsArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    server: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServiceTemplateSpecVolumeNfsArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        server: pulumi.Input[_builtins.str],
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]: ...
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceTemplateSpecVolumeSecretArgsDict(TypedDict):
    secret_name: pulumi.Input[_builtins.str]
    default_mode: NotRequired[pulumi.Input[_builtins.int]]
    items: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceTemplateSpecVolumeSecretItemArgsDict]]
        ]
    ]

@pulumi.input_type
class ServiceTemplateSpecVolumeSecretArgs:
    def __init__(
        __self__,
        *,
        secret_name: pulumi.Input[_builtins.str],
        default_mode: Optional[pulumi.Input[_builtins.int]] = ...,
        items: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateSpecVolumeSecretItemArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[_builtins.str]: ...
    @secret_name.setter
    def secret_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_mode.setter
    def default_mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateSpecVolumeSecretItemArgs]]]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateSpecVolumeSecretItemArgs]]
            ]
        ],
    ): ...

class ServiceTemplateSpecVolumeSecretItemArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    path: pulumi.Input[_builtins.str]
    mode: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateSpecVolumeSecretItemArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        path: pulumi.Input[_builtins.str],
        mode: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTrafficArgsDict(TypedDict):
    percent: pulumi.Input[_builtins.int]
    latest_revision: NotRequired[pulumi.Input[_builtins.bool]]
    revision_name: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTrafficArgs:
    def __init__(
        __self__,
        *,
        percent: pulumi.Input[_builtins.int],
        latest_revision: Optional[pulumi.Input[_builtins.bool]] = ...,
        revision_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> pulumi.Input[_builtins.int]: ...
    @percent.setter
    def percent(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="latestRevision")
    def latest_revision(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @latest_revision.setter
    def latest_revision(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionName")
    def revision_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_name.setter
    def revision_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
