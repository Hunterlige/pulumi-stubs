import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["StandardsControlArgs", "StandardsControl"]

@pulumi.input_type
class StandardsControlArgs:
    def __init__(
        __self__,
        *,
        control_status: pulumi.Input[_builtins.str],
        standards_control_arn: pulumi.Input[_builtins.str],
        disabled_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlStatus")
    def control_status(self) -> pulumi.Input[_builtins.str]: ...
    @control_status.setter
    def control_status(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="standardsControlArn")
    def standards_control_arn(self) -> pulumi.Input[_builtins.str]: ...
    @standards_control_arn.setter
    def standards_control_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disabled_reason.setter
    def disabled_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _StandardsControlState:
    def __init__(
        __self__,
        *,
        control_id: Optional[pulumi.Input[_builtins.str]] = ...,
        control_status: Optional[pulumi.Input[_builtins.str]] = ...,
        control_status_updated_at: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        related_requirements: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        remediation_url: Optional[pulumi.Input[_builtins.str]] = ...,
        severity_rating: Optional[pulumi.Input[_builtins.str]] = ...,
        standards_control_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="controlId")
    def control_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control_id.setter
    def control_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="controlStatus")
    def control_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control_status.setter
    def control_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="controlStatusUpdatedAt")
    def control_status_updated_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @control_status_updated_at.setter
    def control_status_updated_at(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @disabled_reason.setter
    def disabled_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="relatedRequirements")
    def related_requirements(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @related_requirements.setter
    def related_requirements(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="remediationUrl")
    def remediation_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remediation_url.setter
    def remediation_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="severityRating")
    def severity_rating(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity_rating.setter
    def severity_rating(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="standardsControlArn")
    def standards_control_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @standards_control_arn.setter
    def standards_control_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:securityhub/standardsControl:StandardsControl")
class StandardsControl(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        control_status: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        standards_control_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: StandardsControlArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        control_id: Optional[pulumi.Input[_builtins.str]] = ...,
        control_status: Optional[pulumi.Input[_builtins.str]] = ...,
        control_status_updated_at: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        related_requirements: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        remediation_url: Optional[pulumi.Input[_builtins.str]] = ...,
        severity_rating: Optional[pulumi.Input[_builtins.str]] = ...,
        standards_control_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> StandardsControl: ...
    @_builtins.property
    @pulumi.getter(name="controlId")
    def control_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="controlStatus")
    def control_status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="controlStatusUpdatedAt")
    def control_status_updated_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="relatedRequirements")
    def related_requirements(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="remediationUrl")
    def remediation_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="severityRating")
    def severity_rating(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="standardsControlArn")
    def standards_control_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Output[_builtins.str]: ...
