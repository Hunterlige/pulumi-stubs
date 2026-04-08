import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "BudgetComparisonExpressionArgs",
    "BudgetComparisonExpressionArgsDict",
    "BudgetFilterPropertiesArgs",
    "BudgetFilterPropertiesArgsDict",
    "BudgetFilterArgs",
    "BudgetFilterArgsDict",
    "BudgetTimePeriodArgs",
    "BudgetTimePeriodArgsDict",
    "NotificationArgs",
    "NotificationArgsDict",
]

class BudgetComparisonExpressionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    operator: pulumi.Input[Union[_builtins.str, BudgetOperatorType]]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class BudgetComparisonExpressionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        operator: pulumi.Input[Union[_builtins.str, BudgetOperatorType]],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, BudgetOperatorType]]: ...
    @operator.setter
    def operator(
        self, value: pulumi.Input[Union[_builtins.str, BudgetOperatorType]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class BudgetFilterPropertiesArgsDict(TypedDict):
    dimensions: NotRequired[pulumi.Input[BudgetComparisonExpressionArgsDict]]
    tags: NotRequired[pulumi.Input[BudgetComparisonExpressionArgsDict]]

@pulumi.input_type
class BudgetFilterPropertiesArgs:
    def __init__(
        __self__,
        *,
        dimensions: Optional[pulumi.Input[BudgetComparisonExpressionArgs]] = ...,
        tags: Optional[pulumi.Input[BudgetComparisonExpressionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[BudgetComparisonExpressionArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetComparisonExpressionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetComparisonExpressionArgs]]: ...
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[BudgetComparisonExpressionArgs]]): ...

class BudgetFilterArgsDict(TypedDict):
    and_: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[BudgetFilterPropertiesArgsDict]]]
    ]
    dimensions: NotRequired[pulumi.Input[BudgetComparisonExpressionArgsDict]]
    tags: NotRequired[pulumi.Input[BudgetComparisonExpressionArgsDict]]

@pulumi.input_type
class BudgetFilterArgs:
    def __init__(
        __self__,
        *,
        and_: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterPropertiesArgs]]]
        ] = ...,
        dimensions: Optional[pulumi.Input[BudgetComparisonExpressionArgs]] = ...,
        tags: Optional[pulumi.Input[BudgetComparisonExpressionArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="and")
    def and_(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[BudgetFilterPropertiesArgs]]]]: ...
    @and_.setter
    def and_(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[BudgetFilterPropertiesArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input[BudgetComparisonExpressionArgs]]: ...
    @dimensions.setter
    def dimensions(
        self, value: Optional[pulumi.Input[BudgetComparisonExpressionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[BudgetComparisonExpressionArgs]]: ...
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[BudgetComparisonExpressionArgs]]): ...

class BudgetTimePeriodArgsDict(TypedDict):
    start_date: pulumi.Input[_builtins.str]
    end_date: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BudgetTimePeriodArgs:
    def __init__(
        __self__,
        *,
        start_date: pulumi.Input[_builtins.str],
        end_date: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Input[_builtins.str]: ...
    @start_date.setter
    def start_date(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class NotificationArgsDict(TypedDict):
    contact_emails: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    enabled: pulumi.Input[_builtins.bool]
    operator: pulumi.Input[Union[_builtins.str, OperatorType]]
    threshold: pulumi.Input[_builtins.float]
    contact_groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    contact_roles: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    locale: NotRequired[pulumi.Input[Union[_builtins.str, CultureCode]]]
    threshold_type: NotRequired[pulumi.Input[Union[_builtins.str, ThresholdType]]]

@pulumi.input_type
class NotificationArgs:
    def __init__(
        __self__,
        *,
        contact_emails: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        enabled: pulumi.Input[_builtins.bool],
        operator: pulumi.Input[Union[_builtins.str, OperatorType]],
        threshold: pulumi.Input[_builtins.float],
        contact_groups: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        contact_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        locale: Optional[pulumi.Input[Union[_builtins.str, CultureCode]]] = ...,
        threshold_type: Optional[
            pulumi.Input[Union[_builtins.str, ThresholdType]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactEmails")
    def contact_emails(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @contact_emails.setter
    def contact_emails(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[_builtins.str, OperatorType]]: ...
    @operator.setter
    def operator(self, value: pulumi.Input[Union[_builtins.str, OperatorType]]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.float]: ...
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="contactGroups")
    def contact_groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @contact_groups.setter
    def contact_groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="contactRoles")
    def contact_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @contact_roles.setter
    def contact_roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[Union[_builtins.str, CultureCode]]]: ...
    @locale.setter
    def locale(
        self, value: Optional[pulumi.Input[Union[_builtins.str, CultureCode]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="thresholdType")
    def threshold_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ThresholdType]]]: ...
    @threshold_type.setter
    def threshold_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ThresholdType]]]
    ): ...
