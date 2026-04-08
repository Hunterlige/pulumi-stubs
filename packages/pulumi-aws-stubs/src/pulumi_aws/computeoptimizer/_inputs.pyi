import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "EnrollmentStatusTimeoutsArgs",
    "EnrollmentStatusTimeoutsArgsDict",
    ...,
    ...,
    "RecommendationPreferencesPreferredResourceArgs",
    "RecommendationPreferencesPreferredResourceArgsDict",
    "RecommendationPreferencesScopeArgs",
    "RecommendationPreferencesScopeArgsDict",
    "RecommendationPreferencesUtilizationPreferenceArgs",
    ...,
    ...,
    ...,
]

class EnrollmentStatusTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EnrollmentStatusTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecommendationPreferencesExternalMetricsPreferenceArgsDict(TypedDict):
    source: pulumi.Input[_builtins.str]

@pulumi.input_type
class RecommendationPreferencesExternalMetricsPreferenceArgs:
    def __init__(__self__, *, source: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[_builtins.str]: ...
    @source.setter
    def source(self, value: pulumi.Input[_builtins.str]): ...

class RecommendationPreferencesPreferredResourceArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    exclude_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    include_lists: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class RecommendationPreferencesPreferredResourceArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        exclude_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        include_lists: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="excludeLists")
    def exclude_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_lists.setter
    def exclude_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeLists")
    def include_lists(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @include_lists.setter
    def include_lists(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class RecommendationPreferencesScopeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class RecommendationPreferencesScopeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class RecommendationPreferencesUtilizationPreferenceArgsDict(TypedDict):
    metric_name: pulumi.Input[_builtins.str]
    metric_parameters: pulumi.Input[
        RecommendationPreferencesUtilizationPreferenceMetricParametersArgsDict
    ]

@pulumi.input_type
class RecommendationPreferencesUtilizationPreferenceArgs:
    def __init__(
        __self__,
        *,
        metric_name: pulumi.Input[_builtins.str],
        metric_parameters: pulumi.Input[
            RecommendationPreferencesUtilizationPreferenceMetricParametersArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> pulumi.Input[_builtins.str]: ...
    @metric_name.setter
    def metric_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="metricParameters")
    def metric_parameters(
        self,
    ) -> pulumi.Input[
        RecommendationPreferencesUtilizationPreferenceMetricParametersArgs
    ]: ...
    @metric_parameters.setter
    def metric_parameters(
        self,
        value: pulumi.Input[
            RecommendationPreferencesUtilizationPreferenceMetricParametersArgs
        ],
    ): ...

class RecommendationPreferencesUtilizationPreferenceMetricParametersArgsDict(TypedDict):
    headroom: pulumi.Input[_builtins.str]
    threshold: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecommendationPreferencesUtilizationPreferenceMetricParametersArgs:
    def __init__(
        __self__,
        *,
        headroom: pulumi.Input[_builtins.str],
        threshold: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def headroom(self) -> pulumi.Input[_builtins.str]: ...
    @headroom.setter
    def headroom(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[_builtins.str]]): ...
