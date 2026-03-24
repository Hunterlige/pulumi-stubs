import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SelectionArgs", "Selection"]

@pulumi.input_type
class SelectionArgs:
    def __init__(
        __self__,
        *,
        iam_role_arn: pulumi.Input[_builtins.str],
        plan_id: pulumi.Input[_builtins.str],
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        not_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        selection_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionSelectionTagArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @iam_role_arn.setter
    def iam_role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> pulumi.Input[_builtins.str]: ...
    @plan_id.setter
    def plan_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SelectionConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SelectionConditionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notResources")
    def not_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_resources.setter
    def not_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectionTags")
    def selection_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SelectionSelectionTagArgs]]]]: ...
    @selection_tags.setter
    def selection_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionSelectionTagArgs]]]
        ],
    ): ...

@pulumi.input_type
class _SelectionState:
    def __init__(
        __self__,
        *,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionConditionArgs]]]
        ] = ...,
        iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        not_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        selection_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionSelectionTagArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SelectionConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[SelectionConditionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="notResources")
    def not_resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_resources.setter
    def not_resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @plan_id.setter
    def plan_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="selectionTags")
    def selection_tags(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SelectionSelectionTagArgs]]]]: ...
    @selection_tags.setter
    def selection_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SelectionSelectionTagArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:backup/selection:Selection")
class Selection(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[SelectionConditionArgs, SelectionConditionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        not_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        selection_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[SelectionSelectionTagArgs, SelectionSelectionTagArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SelectionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[SelectionConditionArgs, SelectionConditionArgsDict]
                    ]
                ]
            ]
        ] = ...,
        iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        not_resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        plan_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resources: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        selection_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[SelectionSelectionTagArgs, SelectionSelectionTagArgsDict]
                    ]
                ]
            ]
        ] = ...,
    ) -> Selection: ...
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence[outputs.SelectionCondition]]: ...
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="notResources")
    def not_resources(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="planId")
    def plan_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="selectionTags")
    def selection_tags(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.SelectionSelectionTag]]]: ...
