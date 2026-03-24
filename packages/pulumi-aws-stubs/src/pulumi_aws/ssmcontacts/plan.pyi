import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["PlanArgs", "Plan"]

@pulumi.input_type
class PlanArgs:
    def __init__(
        __self__,
        *,
        contact_id: pulumi.Input[_builtins.str],
        stages: pulumi.Input[Sequence[pulumi.Input[PlanStageArgs]]],
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> pulumi.Input[_builtins.str]: ...
    @contact_id.setter
    def contact_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def stages(self) -> pulumi.Input[Sequence[pulumi.Input[PlanStageArgs]]]: ...
    @stages.setter
    def stages(self, value: pulumi.Input[Sequence[pulumi.Input[PlanStageArgs]]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _PlanState:
    def __init__(
        __self__,
        *,
        contact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stages: Optional[pulumi.Input[Sequence[pulumi.Input[PlanStageArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @contact_id.setter
    def contact_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def stages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[PlanStageArgs]]]]: ...
    @stages.setter
    def stages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[PlanStageArgs]]]]
    ): ...

@pulumi.type_token("aws:ssmcontacts/plan:Plan")
class Plan(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        contact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stages: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[PlanStageArgs, PlanStageArgsDict]]]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: PlanArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        contact_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        stages: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[PlanStageArgs, PlanStageArgsDict]]]
            ]
        ] = ...,
    ) -> Plan: ...
    @_builtins.property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def stages(self) -> pulumi.Output[Sequence[outputs.PlanStage]]: ...
