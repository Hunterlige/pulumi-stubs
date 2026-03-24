import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReleaseArgs", "Release"]

@pulumi.input_type
class ReleaseArgs:
    def __init__(
        __self__,
        *,
        location: pulumi.Input[_builtins.str],
        release_id: pulumi.Input[_builtins.str],
        unit_kind: pulumi.Input[_builtins.str],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        blueprint: Optional[pulumi.Input[ReleaseBlueprintArgs]] = ...,
        input_variable_defaults: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReleaseInputVariableDefaultArgs]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        release_requirements: Optional[
            pulumi.Input[ReleaseReleaseRequirementsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="releaseId")
    def release_id(self) -> pulumi.Input[_builtins.str]: ...
    @release_id.setter
    def release_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> pulumi.Input[_builtins.str]: ...
    @unit_kind.setter
    def unit_kind(self, value: pulumi.Input[_builtins.str]): ...
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
    def blueprint(self) -> Optional[pulumi.Input[ReleaseBlueprintArgs]]: ...
    @blueprint.setter
    def blueprint(self, value: Optional[pulumi.Input[ReleaseBlueprintArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="inputVariableDefaults")
    def input_variable_defaults(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReleaseInputVariableDefaultArgs]]]
    ]: ...
    @input_variable_defaults.setter
    def input_variable_defaults(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReleaseInputVariableDefaultArgs]]]
        ],
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
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseRequirements")
    def release_requirements(
        self,
    ) -> Optional[pulumi.Input[ReleaseReleaseRequirementsArgs]]: ...
    @release_requirements.setter
    def release_requirements(
        self, value: Optional[pulumi.Input[ReleaseReleaseRequirementsArgs]]
    ): ...

@pulumi.input_type
class _ReleaseState:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        blueprint: Optional[pulumi.Input[ReleaseBlueprintArgs]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        input_variable_defaults: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReleaseInputVariableDefaultArgs]]]
        ] = ...,
        input_variables: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReleaseInputVariableArgs]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_variables: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReleaseOutputVariableArgs]]]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        release_id: Optional[pulumi.Input[_builtins.str]] = ...,
        release_requirements: Optional[
            pulumi.Input[ReleaseReleaseRequirementsArgs]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_kind: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter
    def blueprint(self) -> Optional[pulumi.Input[ReleaseBlueprintArgs]]: ...
    @blueprint.setter
    def blueprint(self, value: Optional[pulumi.Input[ReleaseBlueprintArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="inputVariableDefaults")
    def input_variable_defaults(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ReleaseInputVariableDefaultArgs]]]
    ]: ...
    @input_variable_defaults.setter
    def input_variable_defaults(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReleaseInputVariableDefaultArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReleaseInputVariableArgs]]]]: ...
    @input_variables.setter
    def input_variables(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ReleaseInputVariableArgs]]]],
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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputVariables")
    def output_variables(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ReleaseOutputVariableArgs]]]]: ...
    @output_variables.setter
    def output_variables(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ReleaseOutputVariableArgs]]]
        ],
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
    @pulumi.getter(name="releaseId")
    def release_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @release_id.setter
    def release_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="releaseRequirements")
    def release_requirements(
        self,
    ) -> Optional[pulumi.Input[ReleaseReleaseRequirementsArgs]]: ...
    @release_requirements.setter
    def release_requirements(
        self, value: Optional[pulumi.Input[ReleaseReleaseRequirementsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uid.setter
    def uid(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @unit_kind.setter
    def unit_kind(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:saasruntime/release:Release")
class Release(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        blueprint: Optional[
            pulumi.Input[Union[ReleaseBlueprintArgs, ReleaseBlueprintArgsDict]]
        ] = ...,
        input_variable_defaults: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReleaseInputVariableDefaultArgs,
                            ReleaseInputVariableDefaultArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        release_id: Optional[pulumi.Input[_builtins.str]] = ...,
        release_requirements: Optional[
            pulumi.Input[
                Union[
                    ReleaseReleaseRequirementsArgs, ReleaseReleaseRequirementsArgsDict
                ]
            ]
        ] = ...,
        unit_kind: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReleaseArgs,
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
        blueprint: Optional[
            pulumi.Input[Union[ReleaseBlueprintArgs, ReleaseBlueprintArgsDict]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        input_variable_defaults: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            ReleaseInputVariableDefaultArgs,
                            ReleaseInputVariableDefaultArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        input_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReleaseInputVariableArgs, ReleaseInputVariableArgsDict]
                    ]
                ]
            ]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ReleaseOutputVariableArgs, ReleaseOutputVariableArgsDict]
                    ]
                ]
            ]
        ] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        release_id: Optional[pulumi.Input[_builtins.str]] = ...,
        release_requirements: Optional[
            pulumi.Input[
                Union[
                    ReleaseReleaseRequirementsArgs, ReleaseReleaseRequirementsArgsDict
                ]
            ]
        ] = ...,
        uid: Optional[pulumi.Input[_builtins.str]] = ...,
        unit_kind: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Release: ...
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def blueprint(self) -> pulumi.Output[Optional[outputs.ReleaseBlueprint]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
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
    @pulumi.getter(name="inputVariableDefaults")
    def input_variable_defaults(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ReleaseInputVariableDefault]]]: ...
    @_builtins.property
    @pulumi.getter(name="inputVariables")
    def input_variables(
        self,
    ) -> pulumi.Output[Sequence[outputs.ReleaseInputVariable]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputVariables")
    def output_variables(
        self,
    ) -> pulumi.Output[Sequence[outputs.ReleaseOutputVariable]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="releaseId")
    def release_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="releaseRequirements")
    def release_requirements(
        self,
    ) -> pulumi.Output[Optional[outputs.ReleaseReleaseRequirements]]: ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="unitKind")
    def unit_kind(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
