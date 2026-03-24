import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AssessmentArgs", "Assessment"]

@pulumi.input_type
class AssessmentArgs:
    def __init__(
        __self__,
        *,
        framework_id: pulumi.Input[_builtins.str],
        roles: pulumi.Input[Sequence[pulumi.Input[AssessmentRoleArgs]]],
        assessment_reports_destination: Optional[
            pulumi.Input[AssessmentAssessmentReportsDestinationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scope: Optional[pulumi.Input[AssessmentScopeArgs]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="frameworkId")
    def framework_id(self) -> pulumi.Input[_builtins.str]: ...
    @framework_id.setter
    def framework_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> pulumi.Input[Sequence[pulumi.Input[AssessmentRoleArgs]]]: ...
    @roles.setter
    def roles(
        self, value: pulumi.Input[Sequence[pulumi.Input[AssessmentRoleArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="assessmentReportsDestination")
    def assessment_reports_destination(
        self,
    ) -> Optional[pulumi.Input[AssessmentAssessmentReportsDestinationArgs]]: ...
    @assessment_reports_destination.setter
    def assessment_reports_destination(
        self, value: Optional[pulumi.Input[AssessmentAssessmentReportsDestinationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[AssessmentScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[AssessmentScopeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _AssessmentState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        assessment_reports_destination: Optional[
            pulumi.Input[AssessmentAssessmentReportsDestinationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        framework_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        roles: Optional[pulumi.Input[Sequence[pulumi.Input[AssessmentRoleArgs]]]] = ...,
        roles_alls: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssessmentRolesAllArgs]]]
        ] = ...,
        scope: Optional[pulumi.Input[AssessmentScopeArgs]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="assessmentReportsDestination")
    def assessment_reports_destination(
        self,
    ) -> Optional[pulumi.Input[AssessmentAssessmentReportsDestinationArgs]]: ...
    @assessment_reports_destination.setter
    def assessment_reports_destination(
        self, value: Optional[pulumi.Input[AssessmentAssessmentReportsDestinationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="frameworkId")
    def framework_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @framework_id.setter
    def framework_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssessmentRoleArgs]]]]: ...
    @roles.setter
    def roles(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AssessmentRoleArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="rolesAlls")
    def roles_alls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssessmentRolesAllArgs]]]]: ...
    @roles_alls.setter
    def roles_alls(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AssessmentRolesAllArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[AssessmentScopeArgs]]: ...
    @scope.setter
    def scope(self, value: Optional[pulumi.Input[AssessmentScopeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:auditmanager/assessment:Assessment")
class Assessment(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        assessment_reports_destination: Optional[
            pulumi.Input[
                Union[
                    AssessmentAssessmentReportsDestinationArgs,
                    AssessmentAssessmentReportsDestinationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        framework_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        roles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[AssessmentRoleArgs, AssessmentRoleArgsDict]]
                ]
            ]
        ] = ...,
        scope: Optional[
            pulumi.Input[Union[AssessmentScopeArgs, AssessmentScopeArgsDict]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AssessmentArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        assessment_reports_destination: Optional[
            pulumi.Input[
                Union[
                    AssessmentAssessmentReportsDestinationArgs,
                    AssessmentAssessmentReportsDestinationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        framework_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        roles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[AssessmentRoleArgs, AssessmentRoleArgsDict]]
                ]
            ]
        ] = ...,
        roles_alls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AssessmentRolesAllArgs, AssessmentRolesAllArgsDict]
                    ]
                ]
            ]
        ] = ...,
        scope: Optional[
            pulumi.Input[Union[AssessmentScopeArgs, AssessmentScopeArgsDict]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Assessment: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="assessmentReportsDestination")
    def assessment_reports_destination(
        self,
    ) -> pulumi.Output[Optional[outputs.AssessmentAssessmentReportsDestination]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="frameworkId")
    def framework_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Sequence[outputs.AssessmentRole]]: ...
    @_builtins.property
    @pulumi.getter(name="rolesAlls")
    def roles_alls(self) -> pulumi.Output[Sequence[outputs.AssessmentRolesAll]]: ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[outputs.AssessmentScope]]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
