import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._enums import *
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccessReviewHistoryDefinitionByIdArgs", "AccessReviewHistoryDefinitionById"]

@pulumi.input_type
class AccessReviewHistoryDefinitionByIdArgs:
    def __init__(
        __self__,
        *,
        decisions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AccessReviewResult]]]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        history_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        instances: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccessReviewHistoryInstanceArgs]]]
        ] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        range: Optional[pulumi.Input[AccessReviewRecurrenceRangeArgs]] = ...,
        scopes: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccessReviewScopeArgs]]]
        ] = ...,
        type: Optional[
            pulumi.Input[Union[_builtins.str, AccessReviewRecurrencePatternType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def decisions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, AccessReviewResult]]]]
    ]: ...
    @decisions.setter
    def decisions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AccessReviewResult]]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="historyDefinitionId")
    def history_definition_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @history_definition_id.setter
    def history_definition_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AccessReviewHistoryInstanceArgs]]]
    ]: ...
    @instances.setter
    def instances(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AccessReviewHistoryInstanceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def range(self) -> Optional[pulumi.Input[AccessReviewRecurrenceRangeArgs]]: ...
    @range.setter
    def range(self, value: Optional[pulumi.Input[AccessReviewRecurrenceRangeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AccessReviewScopeArgs]]]]: ...
    @scopes.setter
    def scopes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AccessReviewScopeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, AccessReviewRecurrencePatternType]]
    ]: ...
    @type.setter
    def type(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, AccessReviewRecurrencePatternType]]
        ],
    ): ...

@pulumi.type_token(...)
class AccessReviewHistoryDefinitionById(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        decisions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[_builtins.str, AccessReviewResult]]]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        history_definition_id: Optional[pulumi.Input[_builtins.str]] = ...,
        instances: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AccessReviewHistoryInstanceArgs,
                            AccessReviewHistoryInstanceArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        interval: Optional[pulumi.Input[_builtins.int]] = ...,
        range: Optional[
            pulumi.Input[
                Union[
                    AccessReviewRecurrenceRangeArgs, AccessReviewRecurrenceRangeArgsDict
                ]
            ]
        ] = ...,
        scopes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AccessReviewScopeArgs, AccessReviewScopeArgsDict]
                    ]
                ]
            ]
        ] = ...,
        type: Optional[
            pulumi.Input[Union[_builtins.str, AccessReviewRecurrencePatternType]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AccessReviewHistoryDefinitionByIdArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AccessReviewHistoryDefinitionById: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def decisions(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.AccessReviewHistoryInstanceResponse]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Output[Optional[_builtins.int]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def range(
        self,
    ) -> pulumi.Output[Optional[outputs.AccessReviewRecurrenceRangeResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="reviewHistoryPeriodEndDateTime")
    def review_history_period_end_date_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reviewHistoryPeriodStartDateTime")
    def review_history_period_start_date_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.AccessReviewScopeResponse]]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> pulumi.Output[_builtins.str]: ...
