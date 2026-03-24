import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AssociationArgs", "Association"]

@pulumi.input_type
class AssociationArgs:
    def __init__(
        __self__,
        *,
        apply_only_at_cron_interval: Optional[pulumi.Input[_builtins.bool]] = ...,
        association_name: Optional[pulumi.Input[_builtins.str]] = ...,
        automation_target_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        calendar_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        compliance_severity: Optional[pulumi.Input[_builtins.str]] = ...,
        document_version: Optional[pulumi.Input[_builtins.str]] = ...,
        max_concurrency: Optional[pulumi.Input[_builtins.str]] = ...,
        max_errors: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_location: Optional[pulumi.Input[AssociationOutputLocationArgs]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_compliance: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssociationTargetArgs]]]
        ] = ...,
        wait_for_success_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyOnlyAtCronInterval")
    def apply_only_at_cron_interval(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_only_at_cron_interval.setter
    def apply_only_at_cron_interval(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="associationName")
    def association_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @association_name.setter
    def association_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="automationTargetParameterName")
    def automation_target_parameter_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @automation_target_parameter_name.setter
    def automation_target_parameter_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="calendarNames")
    def calendar_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @calendar_names.setter
    def calendar_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="complianceSeverity")
    def compliance_severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compliance_severity.setter
    def compliance_severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_version.setter
    def document_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_concurrency.setter
    def max_concurrency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxErrors")
    def max_errors(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_errors.setter
    def max_errors(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputLocation")
    def output_location(
        self,
    ) -> Optional[pulumi.Input[AssociationOutputLocationArgs]]: ...
    @output_location.setter
    def output_location(
        self, value: Optional[pulumi.Input[AssociationOutputLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_expression.setter
    def schedule_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="syncCompliance")
    def sync_compliance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sync_compliance.setter
    def sync_compliance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def targets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssociationTargetArgs]]]]: ...
    @targets.setter
    def targets(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AssociationTargetArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitForSuccessTimeoutSeconds")
    def wait_for_success_timeout_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @wait_for_success_timeout_seconds.setter
    def wait_for_success_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

@pulumi.input_type
class _AssociationState:
    def __init__(
        __self__,
        *,
        apply_only_at_cron_interval: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        association_name: Optional[pulumi.Input[_builtins.str]] = ...,
        automation_target_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        calendar_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        compliance_severity: Optional[pulumi.Input[_builtins.str]] = ...,
        document_version: Optional[pulumi.Input[_builtins.str]] = ...,
        max_concurrency: Optional[pulumi.Input[_builtins.str]] = ...,
        max_errors: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_location: Optional[pulumi.Input[AssociationOutputLocationArgs]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_compliance: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        targets: Optional[
            pulumi.Input[Sequence[pulumi.Input[AssociationTargetArgs]]]
        ] = ...,
        wait_for_success_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applyOnlyAtCronInterval")
    def apply_only_at_cron_interval(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @apply_only_at_cron_interval.setter
    def apply_only_at_cron_interval(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="associationName")
    def association_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @association_name.setter
    def association_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="automationTargetParameterName")
    def automation_target_parameter_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @automation_target_parameter_name.setter
    def automation_target_parameter_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="calendarNames")
    def calendar_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @calendar_names.setter
    def calendar_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="complianceSeverity")
    def compliance_severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compliance_severity.setter
    def compliance_severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_version.setter
    def document_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_concurrency.setter
    def max_concurrency(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxErrors")
    def max_errors(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @max_errors.setter
    def max_errors(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="outputLocation")
    def output_location(
        self,
    ) -> Optional[pulumi.Input[AssociationOutputLocationArgs]]: ...
    @output_location.setter
    def output_location(
        self, value: Optional[pulumi.Input[AssociationOutputLocationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schedule_expression.setter
    def schedule_expression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="syncCompliance")
    def sync_compliance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sync_compliance.setter
    def sync_compliance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter
    def targets(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AssociationTargetArgs]]]]: ...
    @targets.setter
    def targets(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[AssociationTargetArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="waitForSuccessTimeoutSeconds")
    def wait_for_success_timeout_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @wait_for_success_timeout_seconds.setter
    def wait_for_success_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

@pulumi.type_token("aws:ssm/association:Association")
class Association(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_only_at_cron_interval: Optional[pulumi.Input[_builtins.bool]] = ...,
        association_name: Optional[pulumi.Input[_builtins.str]] = ...,
        automation_target_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        calendar_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        compliance_severity: Optional[pulumi.Input[_builtins.str]] = ...,
        document_version: Optional[pulumi.Input[_builtins.str]] = ...,
        max_concurrency: Optional[pulumi.Input[_builtins.str]] = ...,
        max_errors: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_location: Optional[
            pulumi.Input[
                Union[AssociationOutputLocationArgs, AssociationOutputLocationArgsDict]
            ]
        ] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_compliance: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AssociationTargetArgs, AssociationTargetArgsDict]
                    ]
                ]
            ]
        ] = ...,
        wait_for_success_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[AssociationArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        apply_only_at_cron_interval: Optional[pulumi.Input[_builtins.bool]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        association_name: Optional[pulumi.Input[_builtins.str]] = ...,
        automation_target_parameter_name: Optional[pulumi.Input[_builtins.str]] = ...,
        calendar_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        compliance_severity: Optional[pulumi.Input[_builtins.str]] = ...,
        document_version: Optional[pulumi.Input[_builtins.str]] = ...,
        max_concurrency: Optional[pulumi.Input[_builtins.str]] = ...,
        max_errors: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        output_location: Optional[
            pulumi.Input[
                Union[AssociationOutputLocationArgs, AssociationOutputLocationArgsDict]
            ]
        ] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        schedule_expression: Optional[pulumi.Input[_builtins.str]] = ...,
        sync_compliance: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        targets: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[AssociationTargetArgs, AssociationTargetArgsDict]
                    ]
                ]
            ]
        ] = ...,
        wait_for_success_timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> Association: ...
    @_builtins.property
    @pulumi.getter(name="applyOnlyAtCronInterval")
    def apply_only_at_cron_interval(
        self,
    ) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associationName")
    def association_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="automationTargetParameterName")
    def automation_target_parameter_name(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="calendarNames")
    def calendar_names(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="complianceSeverity")
    def compliance_severity(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="documentVersion")
    def document_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrency")
    def max_concurrency(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="maxErrors")
    def max_errors(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputLocation")
    def output_location(
        self,
    ) -> pulumi.Output[Optional[outputs.AssociationOutputLocation]]: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="scheduleExpression")
    def schedule_expression(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="syncCompliance")
    def sync_compliance(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def targets(self) -> pulumi.Output[Sequence[outputs.AssociationTarget]]: ...
    @_builtins.property
    @pulumi.getter(name="waitForSuccessTimeoutSeconds")
    def wait_for_success_timeout_seconds(
        self,
    ) -> pulumi.Output[Optional[_builtins.int]]: ...
