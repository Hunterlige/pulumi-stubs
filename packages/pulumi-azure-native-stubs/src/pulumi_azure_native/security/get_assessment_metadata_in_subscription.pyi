import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetAssessmentMetadataInSubscriptionResult",
    "AwaitableGetAssessmentMetadataInSubscriptionResult",
    "get_assessment_metadata_in_subscription",
    "get_assessment_metadata_in_subscription_output",
]

@pulumi.output_type
class GetAssessmentMetadataInSubscriptionResult:
    def __init__(
        __self__,
        assessment_type=...,
        azure_api_version=...,
        categories=...,
        description=...,
        display_name=...,
        id=...,
        implementation_effort=...,
        name=...,
        partner_data=...,
        planned_deprecation_date=...,
        policy_definition_id=...,
        preview=...,
        publish_dates=...,
        remediation_description=...,
        severity=...,
        tactics=...,
        techniques=...,
        threats=...,
        type=...,
        user_impact=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="azureApiVersion")
    def azure_api_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def categories(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="implementationEffort")
    def implementation_effort(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="partnerData")
    def partner_data(
        self,
    ) -> Optional[outputs.SecurityAssessmentMetadataPartnerDataResponse]: ...
    @_builtins.property
    @pulumi.getter(name="plannedDeprecationDate")
    def planned_deprecation_date(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def preview(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="publishDates")
    def publish_dates(
        self,
    ) -> Optional[
        outputs.SecurityAssessmentMetadataPropertiesResponseResponsePublishDates
    ]: ...
    @_builtins.property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tactics(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def techniques(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def threats(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userImpact")
    def user_impact(self) -> Optional[_builtins.str]: ...

class AwaitableGetAssessmentMetadataInSubscriptionResult(
    GetAssessmentMetadataInSubscriptionResult
):
    def __await__(self): ...

def get_assessment_metadata_in_subscription(
    assessment_metadata_name: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetAssessmentMetadataInSubscriptionResult: ...
def get_assessment_metadata_in_subscription_output(
    assessment_metadata_name: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetAssessmentMetadataInSubscriptionResult]: ...
