import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ControlArgs", "Control"]

@pulumi.input_type
class ControlArgs:
    def __init__(
        __self__,
        *,
        control_id: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        engine_id: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        solution_type: pulumi.Input[_builtins.str],
        boost_action: Optional[pulumi.Input[ControlBoostActionArgs]] = ...,
        collection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlConditionArgs]]]
        ] = ...,
        filter_action: Optional[pulumi.Input[ControlFilterActionArgs]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        promote_action: Optional[pulumi.Input[ControlPromoteActionArgs]] = ...,
        redirect_action: Optional[pulumi.Input[ControlRedirectActionArgs]] = ...,
        synonyms_action: Optional[pulumi.Input[ControlSynonymsActionArgs]] = ...,
        use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlId")
    def control_id(self) -> pulumi.Input[_builtins.str]: ...
    @control_id.setter
    def control_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Input[_builtins.str]: ...
    @engine_id.setter
    def engine_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="solutionType")
    def solution_type(self) -> pulumi.Input[_builtins.str]: ...
    @solution_type.setter
    def solution_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="boostAction")
    def boost_action(self) -> Optional[pulumi.Input[ControlBoostActionArgs]]: ...
    @boost_action.setter
    def boost_action(self, value: Optional[pulumi.Input[ControlBoostActionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ControlConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ControlConditionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterAction")
    def filter_action(self) -> Optional[pulumi.Input[ControlFilterActionArgs]]: ...
    @filter_action.setter
    def filter_action(self, value: Optional[pulumi.Input[ControlFilterActionArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="promoteAction")
    def promote_action(self) -> Optional[pulumi.Input[ControlPromoteActionArgs]]: ...
    @promote_action.setter
    def promote_action(
        self, value: Optional[pulumi.Input[ControlPromoteActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectAction")
    def redirect_action(self) -> Optional[pulumi.Input[ControlRedirectActionArgs]]: ...
    @redirect_action.setter
    def redirect_action(
        self, value: Optional[pulumi.Input[ControlRedirectActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="synonymsAction")
    def synonyms_action(self) -> Optional[pulumi.Input[ControlSynonymsActionArgs]]: ...
    @synonyms_action.setter
    def synonyms_action(
        self, value: Optional[pulumi.Input[ControlSynonymsActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useCases")
    def use_cases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @use_cases.setter
    def use_cases(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ControlState:
    def __init__(
        __self__,
        *,
        boost_action: Optional[pulumi.Input[ControlBoostActionArgs]] = ...,
        collection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlConditionArgs]]]
        ] = ...,
        control_id: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_action: Optional[pulumi.Input[ControlFilterActionArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        promote_action: Optional[pulumi.Input[ControlPromoteActionArgs]] = ...,
        redirect_action: Optional[pulumi.Input[ControlRedirectActionArgs]] = ...,
        solution_type: Optional[pulumi.Input[_builtins.str]] = ...,
        synonyms_action: Optional[pulumi.Input[ControlSynonymsActionArgs]] = ...,
        use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boostAction")
    def boost_action(self) -> Optional[pulumi.Input[ControlBoostActionArgs]]: ...
    @boost_action.setter
    def boost_action(self, value: Optional[pulumi.Input[ControlBoostActionArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ControlConditionArgs]]]]: ...
    @conditions.setter
    def conditions(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ControlConditionArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="controlId")
    def control_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control_id.setter
    def control_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine_id.setter
    def engine_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="filterAction")
    def filter_action(self) -> Optional[pulumi.Input[ControlFilterActionArgs]]: ...
    @filter_action.setter
    def filter_action(self, value: Optional[pulumi.Input[ControlFilterActionArgs]]): ...
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
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="promoteAction")
    def promote_action(self) -> Optional[pulumi.Input[ControlPromoteActionArgs]]: ...
    @promote_action.setter
    def promote_action(
        self, value: Optional[pulumi.Input[ControlPromoteActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="redirectAction")
    def redirect_action(self) -> Optional[pulumi.Input[ControlRedirectActionArgs]]: ...
    @redirect_action.setter
    def redirect_action(
        self, value: Optional[pulumi.Input[ControlRedirectActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="solutionType")
    def solution_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @solution_type.setter
    def solution_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="synonymsAction")
    def synonyms_action(self) -> Optional[pulumi.Input[ControlSynonymsActionArgs]]: ...
    @synonyms_action.setter
    def synonyms_action(
        self, value: Optional[pulumi.Input[ControlSynonymsActionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useCases")
    def use_cases(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @use_cases.setter
    def use_cases(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("gcp:discoveryengine/control:Control")
class Control(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        boost_action: Optional[
            pulumi.Input[Union[ControlBoostActionArgs, ControlBoostActionArgsDict]]
        ] = ...,
        collection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ControlConditionArgs, ControlConditionArgsDict]]
                ]
            ]
        ] = ...,
        control_id: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_action: Optional[
            pulumi.Input[Union[ControlFilterActionArgs, ControlFilterActionArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        promote_action: Optional[
            pulumi.Input[Union[ControlPromoteActionArgs, ControlPromoteActionArgsDict]]
        ] = ...,
        redirect_action: Optional[
            pulumi.Input[
                Union[ControlRedirectActionArgs, ControlRedirectActionArgsDict]
            ]
        ] = ...,
        solution_type: Optional[pulumi.Input[_builtins.str]] = ...,
        synonyms_action: Optional[
            pulumi.Input[
                Union[ControlSynonymsActionArgs, ControlSynonymsActionArgsDict]
            ]
        ] = ...,
        use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ControlArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        boost_action: Optional[
            pulumi.Input[Union[ControlBoostActionArgs, ControlBoostActionArgsDict]]
        ] = ...,
        collection_id: Optional[pulumi.Input[_builtins.str]] = ...,
        conditions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ControlConditionArgs, ControlConditionArgsDict]]
                ]
            ]
        ] = ...,
        control_id: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_id: Optional[pulumi.Input[_builtins.str]] = ...,
        filter_action: Optional[
            pulumi.Input[Union[ControlFilterActionArgs, ControlFilterActionArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        promote_action: Optional[
            pulumi.Input[Union[ControlPromoteActionArgs, ControlPromoteActionArgsDict]]
        ] = ...,
        redirect_action: Optional[
            pulumi.Input[
                Union[ControlRedirectActionArgs, ControlRedirectActionArgsDict]
            ]
        ] = ...,
        solution_type: Optional[pulumi.Input[_builtins.str]] = ...,
        synonyms_action: Optional[
            pulumi.Input[
                Union[ControlSynonymsActionArgs, ControlSynonymsActionArgsDict]
            ]
        ] = ...,
        use_cases: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> Control: ...
    @_builtins.property
    @pulumi.getter(name="boostAction")
    def boost_action(self) -> pulumi.Output[Optional[outputs.ControlBoostAction]]: ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def conditions(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.ControlCondition]]]: ...
    @_builtins.property
    @pulumi.getter(name="controlId")
    def control_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="engineId")
    def engine_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="filterAction")
    def filter_action(self) -> pulumi.Output[Optional[outputs.ControlFilterAction]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="promoteAction")
    def promote_action(
        self,
    ) -> pulumi.Output[Optional[outputs.ControlPromoteAction]]: ...
    @_builtins.property
    @pulumi.getter(name="redirectAction")
    def redirect_action(
        self,
    ) -> pulumi.Output[Optional[outputs.ControlRedirectAction]]: ...
    @_builtins.property
    @pulumi.getter(name="solutionType")
    def solution_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="synonymsAction")
    def synonyms_action(
        self,
    ) -> pulumi.Output[Optional[outputs.ControlSynonymsAction]]: ...
    @_builtins.property
    @pulumi.getter(name="useCases")
    def use_cases(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
