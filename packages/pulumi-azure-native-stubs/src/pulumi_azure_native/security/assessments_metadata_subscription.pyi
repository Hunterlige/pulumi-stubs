import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AssessmentsMetadataSubscriptionArgs", "AssessmentsMetadataSubscription"]

@pulumi.input_type
class AssessmentsMetadataSubscriptionArgs:
    def __init__(
        __self__,
        *,
        assessment_type: pulumi.Input[Union[_builtins.str, AssessmentType]],
        display_name: pulumi.Input[_builtins.str],
        severity: pulumi.Input[Union[_builtins.str, Severity]],
        assessment_metadata_name: Optional[pulumi.Input[_builtins.str]] = ...,
        categories: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Categories]]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        implementation_effort: Optional[
            pulumi.Input[Union[_builtins.str, ImplementationEffort]]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        remediation_description: Optional[pulumi.Input[_builtins.str]] = ...,
        threats: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Threats]]]]
        ] = ...,
        user_impact: Optional[pulumi.Input[Union[_builtins.str, UserImpact]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> pulumi.Input[Union[_builtins.str, AssessmentType]]: ...
    @assessment_type.setter
    def assessment_type(
        self, value: pulumi.Input[Union[_builtins.str, AssessmentType]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Input[Union[_builtins.str, Severity]]: ...
    @severity.setter
    def severity(self, value: pulumi.Input[Union[_builtins.str, Severity]]): ...
    @_builtins.property
    @pulumi.getter(name="assessmentMetadataName")
    def assessment_metadata_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @assessment_metadata_name.setter
    def assessment_metadata_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def categories(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Categories]]]]
    ]: ...
    @categories.setter
    def categories(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Categories]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="implementationEffort")
    def implementation_effort(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, ImplementationEffort]]]: ...
    @implementation_effort.setter
    def implementation_effort(
        self, value: Optional[pulumi.Input[Union[_builtins.str, ImplementationEffort]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preview.setter
    def preview(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @remediation_description.setter
    def remediation_description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def threats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Threats]]]]
    ]: ...
    @threats.setter
    def threats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Threats]]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userImpact")
    def user_impact(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, UserImpact]]]: ...
    @user_impact.setter
    def user_impact(
        self, value: Optional[pulumi.Input[Union[_builtins.str, UserImpact]]]
    ): ...

@pulumi.type_token(...)
class AssessmentsMetadataSubscription(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        assessment_metadata_name: Optional[pulumi.Input[_builtins.str]] = ...,
        assessment_type: Optional[
            pulumi.Input[Union[_builtins.str, AssessmentType]]
        ] = ...,
        categories: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Categories]]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        implementation_effort: Optional[
            pulumi.Input[Union[_builtins.str, ImplementationEffort]]
        ] = ...,
        preview: Optional[pulumi.Input[_builtins.bool]] = ...,
        remediation_description: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[Union[_builtins.str, Severity]]] = ...,
        threats: Optional[
            pulumi.Input[Sequence[pulumi.Input[Union[_builtins.str, Threats]]]]
        ] = ...,
        user_impact: Optional[pulumi.Input[Union[_builtins.str, UserImpact]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AssessmentsMetadataSubscriptionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> AssessmentsMetadataSubscription: ...
    @_builtins.property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="implementationEffort")
    def implementation_effort(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def preview(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def threats(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="userImpact")
    def user_impact(self) -> pulumi.Output[Optional[_builtins.str]]: ...
