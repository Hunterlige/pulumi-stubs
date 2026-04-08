import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AutomationRuleActionArgs",
    "AutomationRuleActionArgsDict",
    "AutomationRuleActionFindingFieldsUpdateArgs",
    "AutomationRuleActionFindingFieldsUpdateArgsDict",
    "AutomationRuleActionFindingFieldsUpdateNoteArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AutomationRuleCriteriaArgs",
    "AutomationRuleCriteriaArgsDict",
    "AutomationRuleCriteriaAwsAccountIdArgs",
    "AutomationRuleCriteriaAwsAccountIdArgsDict",
    "AutomationRuleCriteriaAwsAccountNameArgs",
    "AutomationRuleCriteriaAwsAccountNameArgsDict",
    "AutomationRuleCriteriaCompanyNameArgs",
    "AutomationRuleCriteriaCompanyNameArgsDict",
    ...,
    ...,
    ...,
    ...,
    "AutomationRuleCriteriaComplianceStatusArgs",
    "AutomationRuleCriteriaComplianceStatusArgsDict",
    "AutomationRuleCriteriaConfidenceArgs",
    "AutomationRuleCriteriaConfidenceArgsDict",
    "AutomationRuleCriteriaCreatedAtArgs",
    "AutomationRuleCriteriaCreatedAtArgsDict",
    "AutomationRuleCriteriaCreatedAtDateRangeArgs",
    "AutomationRuleCriteriaCreatedAtDateRangeArgsDict",
    "AutomationRuleCriteriaCriticalityArgs",
    "AutomationRuleCriteriaCriticalityArgsDict",
    "AutomationRuleCriteriaDescriptionArgs",
    "AutomationRuleCriteriaDescriptionArgsDict",
    "AutomationRuleCriteriaFirstObservedAtArgs",
    "AutomationRuleCriteriaFirstObservedAtArgsDict",
    "AutomationRuleCriteriaFirstObservedAtDateRangeArgs",
    ...,
    "AutomationRuleCriteriaGeneratorIdArgs",
    "AutomationRuleCriteriaGeneratorIdArgsDict",
    "AutomationRuleCriteriaIdArgs",
    "AutomationRuleCriteriaIdArgsDict",
    "AutomationRuleCriteriaLastObservedAtArgs",
    "AutomationRuleCriteriaLastObservedAtArgsDict",
    "AutomationRuleCriteriaLastObservedAtDateRangeArgs",
    ...,
    "AutomationRuleCriteriaNoteTextArgs",
    "AutomationRuleCriteriaNoteTextArgsDict",
    "AutomationRuleCriteriaNoteUpdatedAtArgs",
    "AutomationRuleCriteriaNoteUpdatedAtArgsDict",
    "AutomationRuleCriteriaNoteUpdatedAtDateRangeArgs",
    ...,
    "AutomationRuleCriteriaNoteUpdatedByArgs",
    "AutomationRuleCriteriaNoteUpdatedByArgsDict",
    "AutomationRuleCriteriaProductArnArgs",
    "AutomationRuleCriteriaProductArnArgsDict",
    "AutomationRuleCriteriaProductNameArgs",
    "AutomationRuleCriteriaProductNameArgsDict",
    "AutomationRuleCriteriaRecordStateArgs",
    "AutomationRuleCriteriaRecordStateArgsDict",
    "AutomationRuleCriteriaRelatedFindingsIdArgs",
    "AutomationRuleCriteriaRelatedFindingsIdArgsDict",
    ...,
    ...,
    "AutomationRuleCriteriaResourceApplicationArnArgs",
    ...,
    "AutomationRuleCriteriaResourceApplicationNameArgs",
    ...,
    "AutomationRuleCriteriaResourceDetailsOtherArgs",
    "AutomationRuleCriteriaResourceDetailsOtherArgsDict",
    "AutomationRuleCriteriaResourceIdArgs",
    "AutomationRuleCriteriaResourceIdArgsDict",
    "AutomationRuleCriteriaResourcePartitionArgs",
    "AutomationRuleCriteriaResourcePartitionArgsDict",
    "AutomationRuleCriteriaResourceRegionArgs",
    "AutomationRuleCriteriaResourceRegionArgsDict",
    "AutomationRuleCriteriaResourceTagArgs",
    "AutomationRuleCriteriaResourceTagArgsDict",
    "AutomationRuleCriteriaResourceTypeArgs",
    "AutomationRuleCriteriaResourceTypeArgsDict",
    "AutomationRuleCriteriaSeverityLabelArgs",
    "AutomationRuleCriteriaSeverityLabelArgsDict",
    "AutomationRuleCriteriaSourceUrlArgs",
    "AutomationRuleCriteriaSourceUrlArgsDict",
    "AutomationRuleCriteriaTitleArgs",
    "AutomationRuleCriteriaTitleArgsDict",
    "AutomationRuleCriteriaTypeArgs",
    "AutomationRuleCriteriaTypeArgsDict",
    "AutomationRuleCriteriaUpdatedAtArgs",
    "AutomationRuleCriteriaUpdatedAtArgsDict",
    "AutomationRuleCriteriaUpdatedAtDateRangeArgs",
    "AutomationRuleCriteriaUpdatedAtDateRangeArgsDict",
    "AutomationRuleCriteriaUserDefinedFieldArgs",
    "AutomationRuleCriteriaUserDefinedFieldArgsDict",
    "AutomationRuleCriteriaVerificationStateArgs",
    "AutomationRuleCriteriaVerificationStateArgsDict",
    "AutomationRuleCriteriaWorkflowStatusArgs",
    "AutomationRuleCriteriaWorkflowStatusArgsDict",
    "ConfigurationPolicyConfigurationPolicyArgs",
    "ConfigurationPolicyConfigurationPolicyArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "InsightFiltersArgs",
    "InsightFiltersArgsDict",
    "InsightFiltersAwsAccountIdArgs",
    "InsightFiltersAwsAccountIdArgsDict",
    "InsightFiltersCompanyNameArgs",
    "InsightFiltersCompanyNameArgsDict",
    "InsightFiltersComplianceStatusArgs",
    "InsightFiltersComplianceStatusArgsDict",
    "InsightFiltersConfidenceArgs",
    "InsightFiltersConfidenceArgsDict",
    "InsightFiltersCreatedAtArgs",
    "InsightFiltersCreatedAtArgsDict",
    "InsightFiltersCreatedAtDateRangeArgs",
    "InsightFiltersCreatedAtDateRangeArgsDict",
    "InsightFiltersCriticalityArgs",
    "InsightFiltersCriticalityArgsDict",
    "InsightFiltersDescriptionArgs",
    "InsightFiltersDescriptionArgsDict",
    "InsightFiltersFindingProviderFieldsConfidenceArgs",
    ...,
    "InsightFiltersFindingProviderFieldsCriticalityArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "InsightFiltersFindingProviderFieldsTypeArgs",
    "InsightFiltersFindingProviderFieldsTypeArgsDict",
    "InsightFiltersFirstObservedAtArgs",
    "InsightFiltersFirstObservedAtArgsDict",
    "InsightFiltersFirstObservedAtDateRangeArgs",
    "InsightFiltersFirstObservedAtDateRangeArgsDict",
    "InsightFiltersGeneratorIdArgs",
    "InsightFiltersGeneratorIdArgsDict",
    "InsightFiltersIdArgs",
    "InsightFiltersIdArgsDict",
    "InsightFiltersKeywordArgs",
    "InsightFiltersKeywordArgsDict",
    "InsightFiltersLastObservedAtArgs",
    "InsightFiltersLastObservedAtArgsDict",
    "InsightFiltersLastObservedAtDateRangeArgs",
    "InsightFiltersLastObservedAtDateRangeArgsDict",
    "InsightFiltersMalwareNameArgs",
    "InsightFiltersMalwareNameArgsDict",
    "InsightFiltersMalwarePathArgs",
    "InsightFiltersMalwarePathArgsDict",
    "InsightFiltersMalwareStateArgs",
    "InsightFiltersMalwareStateArgsDict",
    "InsightFiltersMalwareTypeArgs",
    "InsightFiltersMalwareTypeArgsDict",
    "InsightFiltersNetworkDestinationDomainArgs",
    "InsightFiltersNetworkDestinationDomainArgsDict",
    "InsightFiltersNetworkDestinationIpv4Args",
    "InsightFiltersNetworkDestinationIpv4ArgsDict",
    "InsightFiltersNetworkDestinationIpv6Args",
    "InsightFiltersNetworkDestinationIpv6ArgsDict",
    "InsightFiltersNetworkDestinationPortArgs",
    "InsightFiltersNetworkDestinationPortArgsDict",
    "InsightFiltersNetworkDirectionArgs",
    "InsightFiltersNetworkDirectionArgsDict",
    "InsightFiltersNetworkProtocolArgs",
    "InsightFiltersNetworkProtocolArgsDict",
    "InsightFiltersNetworkSourceDomainArgs",
    "InsightFiltersNetworkSourceDomainArgsDict",
    "InsightFiltersNetworkSourceIpv4Args",
    "InsightFiltersNetworkSourceIpv4ArgsDict",
    "InsightFiltersNetworkSourceIpv6Args",
    "InsightFiltersNetworkSourceIpv6ArgsDict",
    "InsightFiltersNetworkSourceMacArgs",
    "InsightFiltersNetworkSourceMacArgsDict",
    "InsightFiltersNetworkSourcePortArgs",
    "InsightFiltersNetworkSourcePortArgsDict",
    "InsightFiltersNoteTextArgs",
    "InsightFiltersNoteTextArgsDict",
    "InsightFiltersNoteUpdatedAtArgs",
    "InsightFiltersNoteUpdatedAtArgsDict",
    "InsightFiltersNoteUpdatedAtDateRangeArgs",
    "InsightFiltersNoteUpdatedAtDateRangeArgsDict",
    "InsightFiltersNoteUpdatedByArgs",
    "InsightFiltersNoteUpdatedByArgsDict",
    "InsightFiltersProcessLaunchedAtArgs",
    "InsightFiltersProcessLaunchedAtArgsDict",
    "InsightFiltersProcessLaunchedAtDateRangeArgs",
    "InsightFiltersProcessLaunchedAtDateRangeArgsDict",
    "InsightFiltersProcessNameArgs",
    "InsightFiltersProcessNameArgsDict",
    "InsightFiltersProcessParentPidArgs",
    "InsightFiltersProcessParentPidArgsDict",
    "InsightFiltersProcessPathArgs",
    "InsightFiltersProcessPathArgsDict",
    "InsightFiltersProcessPidArgs",
    "InsightFiltersProcessPidArgsDict",
    "InsightFiltersProcessTerminatedAtArgs",
    "InsightFiltersProcessTerminatedAtArgsDict",
    "InsightFiltersProcessTerminatedAtDateRangeArgs",
    "InsightFiltersProcessTerminatedAtDateRangeArgsDict",
    "InsightFiltersProductArnArgs",
    "InsightFiltersProductArnArgsDict",
    "InsightFiltersProductFieldArgs",
    "InsightFiltersProductFieldArgsDict",
    "InsightFiltersProductNameArgs",
    "InsightFiltersProductNameArgsDict",
    "InsightFiltersRecommendationTextArgs",
    "InsightFiltersRecommendationTextArgsDict",
    "InsightFiltersRecordStateArgs",
    "InsightFiltersRecordStateArgsDict",
    "InsightFiltersRelatedFindingsIdArgs",
    "InsightFiltersRelatedFindingsIdArgsDict",
    "InsightFiltersRelatedFindingsProductArnArgs",
    "InsightFiltersRelatedFindingsProductArnArgsDict",
    ...,
    ...,
    "InsightFiltersResourceAwsEc2InstanceImageIdArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "InsightFiltersResourceAwsEc2InstanceKeyNameArgs",
    ...,
    "InsightFiltersResourceAwsEc2InstanceLaunchedAtArgs",
    ...,
    ...,
    ...,
    "InsightFiltersResourceAwsEc2InstanceSubnetIdArgs",
    ...,
    "InsightFiltersResourceAwsEc2InstanceTypeArgs",
    "InsightFiltersResourceAwsEc2InstanceTypeArgsDict",
    "InsightFiltersResourceAwsEc2InstanceVpcIdArgs",
    "InsightFiltersResourceAwsEc2InstanceVpcIdArgsDict",
    "InsightFiltersResourceAwsIamAccessKeyCreatedAtArgs",
    ...,
    ...,
    ...,
    "InsightFiltersResourceAwsIamAccessKeyStatusArgs",
    ...,
    "InsightFiltersResourceAwsIamAccessKeyUserNameArgs",
    ...,
    "InsightFiltersResourceAwsS3BucketOwnerIdArgs",
    "InsightFiltersResourceAwsS3BucketOwnerIdArgsDict",
    "InsightFiltersResourceAwsS3BucketOwnerNameArgs",
    "InsightFiltersResourceAwsS3BucketOwnerNameArgsDict",
    "InsightFiltersResourceContainerImageIdArgs",
    "InsightFiltersResourceContainerImageIdArgsDict",
    "InsightFiltersResourceContainerImageNameArgs",
    "InsightFiltersResourceContainerImageNameArgsDict",
    "InsightFiltersResourceContainerLaunchedAtArgs",
    "InsightFiltersResourceContainerLaunchedAtArgsDict",
    ...,
    ...,
    "InsightFiltersResourceContainerNameArgs",
    "InsightFiltersResourceContainerNameArgsDict",
    "InsightFiltersResourceDetailsOtherArgs",
    "InsightFiltersResourceDetailsOtherArgsDict",
    "InsightFiltersResourceIdArgs",
    "InsightFiltersResourceIdArgsDict",
    "InsightFiltersResourcePartitionArgs",
    "InsightFiltersResourcePartitionArgsDict",
    "InsightFiltersResourceRegionArgs",
    "InsightFiltersResourceRegionArgsDict",
    "InsightFiltersResourceTagArgs",
    "InsightFiltersResourceTagArgsDict",
    "InsightFiltersResourceTypeArgs",
    "InsightFiltersResourceTypeArgsDict",
    "InsightFiltersSeverityLabelArgs",
    "InsightFiltersSeverityLabelArgsDict",
    "InsightFiltersSourceUrlArgs",
    "InsightFiltersSourceUrlArgsDict",
    "InsightFiltersThreatIntelIndicatorCategoryArgs",
    "InsightFiltersThreatIntelIndicatorCategoryArgsDict",
    ...,
    ...,
    ...,
    ...,
    "InsightFiltersThreatIntelIndicatorSourceArgs",
    "InsightFiltersThreatIntelIndicatorSourceArgsDict",
    "InsightFiltersThreatIntelIndicatorSourceUrlArgs",
    ...,
    "InsightFiltersThreatIntelIndicatorTypeArgs",
    "InsightFiltersThreatIntelIndicatorTypeArgsDict",
    "InsightFiltersThreatIntelIndicatorValueArgs",
    "InsightFiltersThreatIntelIndicatorValueArgsDict",
    "InsightFiltersTitleArgs",
    "InsightFiltersTitleArgsDict",
    "InsightFiltersTypeArgs",
    "InsightFiltersTypeArgsDict",
    "InsightFiltersUpdatedAtArgs",
    "InsightFiltersUpdatedAtArgsDict",
    "InsightFiltersUpdatedAtDateRangeArgs",
    "InsightFiltersUpdatedAtDateRangeArgsDict",
    "InsightFiltersUserDefinedValueArgs",
    "InsightFiltersUserDefinedValueArgsDict",
    "InsightFiltersVerificationStateArgs",
    "InsightFiltersVerificationStateArgsDict",
    "InsightFiltersWorkflowStatusArgs",
    "InsightFiltersWorkflowStatusArgsDict",
    ...,
    ...,
]

class AutomationRuleActionArgsDict(TypedDict):
    finding_fields_update: NotRequired[
        pulumi.Input[AutomationRuleActionFindingFieldsUpdateArgsDict]
    ]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleActionArgs:
    def __init__(
        __self__,
        *,
        finding_fields_update: Optional[
            pulumi.Input[AutomationRuleActionFindingFieldsUpdateArgs]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="findingFieldsUpdate")
    def finding_fields_update(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleActionFindingFieldsUpdateArgs]]: ...
    @finding_fields_update.setter
    def finding_fields_update(
        self, value: Optional[pulumi.Input[AutomationRuleActionFindingFieldsUpdateArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRuleActionFindingFieldsUpdateArgsDict(TypedDict):
    confidence: NotRequired[pulumi.Input[_builtins.int]]
    criticality: NotRequired[pulumi.Input[_builtins.int]]
    note: NotRequired[pulumi.Input[AutomationRuleActionFindingFieldsUpdateNoteArgsDict]]
    related_findings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutomationRuleActionFindingFieldsUpdateRelatedFindingArgsDict
                ]
            ]
        ]
    ]
    severity: NotRequired[
        pulumi.Input[AutomationRuleActionFindingFieldsUpdateSeverityArgsDict]
    ]
    types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    user_defined_fields: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    verification_state: NotRequired[pulumi.Input[_builtins.str]]
    workflow: NotRequired[
        pulumi.Input[AutomationRuleActionFindingFieldsUpdateWorkflowArgsDict]
    ]

@pulumi.input_type
class AutomationRuleActionFindingFieldsUpdateArgs:
    def __init__(
        __self__,
        *,
        confidence: Optional[pulumi.Input[_builtins.int]] = ...,
        criticality: Optional[pulumi.Input[_builtins.int]] = ...,
        note: Optional[
            pulumi.Input[AutomationRuleActionFindingFieldsUpdateNoteArgs]
        ] = ...,
        related_findings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutomationRuleActionFindingFieldsUpdateRelatedFindingArgs
                    ]
                ]
            ]
        ] = ...,
        severity: Optional[
            pulumi.Input[AutomationRuleActionFindingFieldsUpdateSeverityArgs]
        ] = ...,
        types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        user_defined_fields: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        verification_state: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow: Optional[
            pulumi.Input[AutomationRuleActionFindingFieldsUpdateWorkflowArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def confidence(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @confidence.setter
    def confidence(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @criticality.setter
    def criticality(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def note(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleActionFindingFieldsUpdateNoteArgs]]: ...
    @note.setter
    def note(
        self,
        value: Optional[pulumi.Input[AutomationRuleActionFindingFieldsUpdateNoteArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="relatedFindings")
    def related_findings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AutomationRuleActionFindingFieldsUpdateRelatedFindingArgs]
            ]
        ]
    ]: ...
    @related_findings.setter
    def related_findings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutomationRuleActionFindingFieldsUpdateRelatedFindingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def severity(
        self,
    ) -> Optional[
        pulumi.Input[AutomationRuleActionFindingFieldsUpdateSeverityArgs]
    ]: ...
    @severity.setter
    def severity(
        self,
        value: Optional[
            pulumi.Input[AutomationRuleActionFindingFieldsUpdateSeverityArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @types.setter
    def types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @user_defined_fields.setter
    def user_defined_fields(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="verificationState")
    def verification_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @verification_state.setter
    def verification_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def workflow(
        self,
    ) -> Optional[
        pulumi.Input[AutomationRuleActionFindingFieldsUpdateWorkflowArgs]
    ]: ...
    @workflow.setter
    def workflow(
        self,
        value: Optional[
            pulumi.Input[AutomationRuleActionFindingFieldsUpdateWorkflowArgs]
        ],
    ): ...

class AutomationRuleActionFindingFieldsUpdateNoteArgsDict(TypedDict):
    text: pulumi.Input[_builtins.str]
    updated_by: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleActionFindingFieldsUpdateNoteArgs:
    def __init__(
        __self__,
        *,
        text: pulumi.Input[_builtins.str],
        updated_by: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]: ...
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Input[_builtins.str]: ...
    @updated_by.setter
    def updated_by(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleActionFindingFieldsUpdateRelatedFindingArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    product_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleActionFindingFieldsUpdateRelatedFindingArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        product_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="productArn")
    def product_arn(self) -> pulumi.Input[_builtins.str]: ...
    @product_arn.setter
    def product_arn(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleActionFindingFieldsUpdateSeverityArgsDict(TypedDict):
    label: NotRequired[pulumi.Input[_builtins.str]]
    product: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class AutomationRuleActionFindingFieldsUpdateSeverityArgs:
    def __init__(
        __self__,
        *,
        label: Optional[pulumi.Input[_builtins.str]] = ...,
        product: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @label.setter
    def label(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def product(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @product.setter
    def product(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AutomationRuleActionFindingFieldsUpdateWorkflowArgsDict(TypedDict):
    status: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleActionFindingFieldsUpdateWorkflowArgs:
    def __init__(
        __self__, *, status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRuleCriteriaArgsDict(TypedDict):
    aws_account_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaAwsAccountIdArgsDict]]]
    ]
    aws_account_names: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaAwsAccountNameArgsDict]]
        ]
    ]
    company_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCompanyNameArgsDict]]]
    ]
    compliance_associated_standards_ids: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AutomationRuleCriteriaComplianceAssociatedStandardsIdArgsDict
                ]
            ]
        ]
    ]
    compliance_security_control_ids: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AutomationRuleCriteriaComplianceSecurityControlIdArgsDict]
            ]
        ]
    ]
    compliance_statuses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaComplianceStatusArgsDict]]
        ]
    ]
    confidences: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaConfidenceArgsDict]]]
    ]
    created_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCreatedAtArgsDict]]]
    ]
    criticalities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCriticalityArgsDict]]]
    ]
    descriptions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaDescriptionArgsDict]]]
    ]
    first_observed_ats: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaFirstObservedAtArgsDict]]
        ]
    ]
    generator_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaGeneratorIdArgsDict]]]
    ]
    ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaIdArgsDict]]]
    ]
    last_observed_ats: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaLastObservedAtArgsDict]]
        ]
    ]
    note_texts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaNoteTextArgsDict]]]
    ]
    note_updated_ats: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaNoteUpdatedAtArgsDict]]
        ]
    ]
    note_updated_bies: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaNoteUpdatedByArgsDict]]
        ]
    ]
    product_arns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaProductArnArgsDict]]]
    ]
    product_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaProductNameArgsDict]]]
    ]
    record_states: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaRecordStateArgsDict]]]
    ]
    related_findings_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaRelatedFindingsIdArgsDict]]
        ]
    ]
    related_findings_product_arns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AutomationRuleCriteriaRelatedFindingsProductArnArgsDict]
            ]
        ]
    ]
    resource_application_arns: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaResourceApplicationArnArgsDict]]
        ]
    ]
    resource_application_names: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AutomationRuleCriteriaResourceApplicationNameArgsDict]
            ]
        ]
    ]
    resource_details_others: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaResourceDetailsOtherArgsDict]]
        ]
    ]
    resource_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceIdArgsDict]]]
    ]
    resource_partitions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaResourcePartitionArgsDict]]
        ]
    ]
    resource_regions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaResourceRegionArgsDict]]
        ]
    ]
    resource_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceTagArgsDict]]]
    ]
    resource_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceTypeArgsDict]]]
    ]
    severity_labels: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaSeverityLabelArgsDict]]
        ]
    ]
    source_urls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaSourceUrlArgsDict]]]
    ]
    titles: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaTitleArgsDict]]]
    ]
    types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaTypeArgsDict]]]
    ]
    updated_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaUpdatedAtArgsDict]]]
    ]
    user_defined_fields: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaUserDefinedFieldArgsDict]]
        ]
    ]
    verification_states: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaVerificationStateArgsDict]]
        ]
    ]
    workflow_statuses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaWorkflowStatusArgsDict]]
        ]
    ]

@pulumi.input_type
class AutomationRuleCriteriaArgs:
    def __init__(
        __self__,
        *,
        aws_account_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaAwsAccountIdArgs]]]
        ] = ...,
        aws_account_names: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaAwsAccountNameArgs]]
            ]
        ] = ...,
        company_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCompanyNameArgs]]]
        ] = ...,
        compliance_associated_standards_ids: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutomationRuleCriteriaComplianceAssociatedStandardsIdArgs
                    ]
                ]
            ]
        ] = ...,
        compliance_security_control_ids: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AutomationRuleCriteriaComplianceSecurityControlIdArgs]
                ]
            ]
        ] = ...,
        compliance_statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaComplianceStatusArgs]]
            ]
        ] = ...,
        confidences: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaConfidenceArgs]]]
        ] = ...,
        created_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCreatedAtArgs]]]
        ] = ...,
        criticalities: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCriticalityArgs]]]
        ] = ...,
        descriptions: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaDescriptionArgs]]]
        ] = ...,
        first_observed_ats: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaFirstObservedAtArgs]]
            ]
        ] = ...,
        generator_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaGeneratorIdArgs]]]
        ] = ...,
        ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaIdArgs]]]
        ] = ...,
        last_observed_ats: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaLastObservedAtArgs]]
            ]
        ] = ...,
        note_texts: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaNoteTextArgs]]]
        ] = ...,
        note_updated_ats: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaNoteUpdatedAtArgs]]
            ]
        ] = ...,
        note_updated_bies: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaNoteUpdatedByArgs]]
            ]
        ] = ...,
        product_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaProductArnArgs]]]
        ] = ...,
        product_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaProductNameArgs]]]
        ] = ...,
        record_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaRecordStateArgs]]]
        ] = ...,
        related_findings_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaRelatedFindingsIdArgs]]
            ]
        ] = ...,
        related_findings_product_arns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AutomationRuleCriteriaRelatedFindingsProductArnArgs]
                ]
            ]
        ] = ...,
        resource_application_arns: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaResourceApplicationArnArgs]]
            ]
        ] = ...,
        resource_application_names: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AutomationRuleCriteriaResourceApplicationNameArgs]
                ]
            ]
        ] = ...,
        resource_details_others: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaResourceDetailsOtherArgs]]
            ]
        ] = ...,
        resource_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceIdArgs]]]
        ] = ...,
        resource_partitions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaResourcePartitionArgs]]
            ]
        ] = ...,
        resource_regions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaResourceRegionArgs]]
            ]
        ] = ...,
        resource_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceTagArgs]]]
        ] = ...,
        resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceTypeArgs]]]
        ] = ...,
        severity_labels: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaSeverityLabelArgs]]
            ]
        ] = ...,
        source_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaSourceUrlArgs]]]
        ] = ...,
        titles: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaTitleArgs]]]
        ] = ...,
        types: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaTypeArgs]]]
        ] = ...,
        updated_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaUpdatedAtArgs]]]
        ] = ...,
        user_defined_fields: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaUserDefinedFieldArgs]]
            ]
        ] = ...,
        verification_states: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaVerificationStateArgs]]
            ]
        ] = ...,
        workflow_statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaWorkflowStatusArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountIds")
    def aws_account_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaAwsAccountIdArgs]]]
    ]: ...
    @aws_account_ids.setter
    def aws_account_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaAwsAccountIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="awsAccountNames")
    def aws_account_names(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaAwsAccountNameArgs]]]
    ]: ...
    @aws_account_names.setter
    def aws_account_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaAwsAccountNameArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="companyNames")
    def company_names(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCompanyNameArgs]]]
    ]: ...
    @company_names.setter
    def company_names(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCompanyNameArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="complianceAssociatedStandardsIds")
    def compliance_associated_standards_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AutomationRuleCriteriaComplianceAssociatedStandardsIdArgs]
            ]
        ]
    ]: ...
    @compliance_associated_standards_ids.setter
    def compliance_associated_standards_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AutomationRuleCriteriaComplianceAssociatedStandardsIdArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="complianceSecurityControlIds")
    def compliance_security_control_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AutomationRuleCriteriaComplianceSecurityControlIdArgs]
            ]
        ]
    ]: ...
    @compliance_security_control_ids.setter
    def compliance_security_control_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AutomationRuleCriteriaComplianceSecurityControlIdArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="complianceStatuses")
    def compliance_statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaComplianceStatusArgs]]]
    ]: ...
    @compliance_statuses.setter
    def compliance_statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaComplianceStatusArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def confidences(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaConfidenceArgs]]]
    ]: ...
    @confidences.setter
    def confidences(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaConfidenceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdAts")
    def created_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCreatedAtArgs]]]
    ]: ...
    @created_ats.setter
    def created_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCreatedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def criticalities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCriticalityArgs]]]
    ]: ...
    @criticalities.setter
    def criticalities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaCriticalityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def descriptions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaDescriptionArgs]]]
    ]: ...
    @descriptions.setter
    def descriptions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaDescriptionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="firstObservedAts")
    def first_observed_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaFirstObservedAtArgs]]]
    ]: ...
    @first_observed_ats.setter
    def first_observed_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaFirstObservedAtArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="generatorIds")
    def generator_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaGeneratorIdArgs]]]
    ]: ...
    @generator_ids.setter
    def generator_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaGeneratorIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaIdArgs]]]
    ]: ...
    @ids.setter
    def ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastObservedAts")
    def last_observed_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaLastObservedAtArgs]]]
    ]: ...
    @last_observed_ats.setter
    def last_observed_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaLastObservedAtArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="noteTexts")
    def note_texts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaNoteTextArgs]]]
    ]: ...
    @note_texts.setter
    def note_texts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaNoteTextArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="noteUpdatedAts")
    def note_updated_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaNoteUpdatedAtArgs]]]
    ]: ...
    @note_updated_ats.setter
    def note_updated_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaNoteUpdatedAtArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="noteUpdatedBies")
    def note_updated_bies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaNoteUpdatedByArgs]]]
    ]: ...
    @note_updated_bies.setter
    def note_updated_bies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaNoteUpdatedByArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="productArns")
    def product_arns(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaProductArnArgs]]]
    ]: ...
    @product_arns.setter
    def product_arns(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaProductArnArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="productNames")
    def product_names(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaProductNameArgs]]]
    ]: ...
    @product_names.setter
    def product_names(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaProductNameArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recordStates")
    def record_states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaRecordStateArgs]]]
    ]: ...
    @record_states.setter
    def record_states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaRecordStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="relatedFindingsIds")
    def related_findings_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaRelatedFindingsIdArgs]]
        ]
    ]: ...
    @related_findings_ids.setter
    def related_findings_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaRelatedFindingsIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="relatedFindingsProductArns")
    def related_findings_product_arns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaRelatedFindingsProductArnArgs]]
        ]
    ]: ...
    @related_findings_product_arns.setter
    def related_findings_product_arns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AutomationRuleCriteriaRelatedFindingsProductArnArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceApplicationArns")
    def resource_application_arns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaResourceApplicationArnArgs]]
        ]
    ]: ...
    @resource_application_arns.setter
    def resource_application_arns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaResourceApplicationArnArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceApplicationNames")
    def resource_application_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaResourceApplicationNameArgs]]
        ]
    ]: ...
    @resource_application_names.setter
    def resource_application_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AutomationRuleCriteriaResourceApplicationNameArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceDetailsOthers")
    def resource_details_others(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaResourceDetailsOtherArgs]]
        ]
    ]: ...
    @resource_details_others.setter
    def resource_details_others(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaResourceDetailsOtherArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceIds")
    def resource_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceIdArgs]]]
    ]: ...
    @resource_ids.setter
    def resource_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourcePartitions")
    def resource_partitions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaResourcePartitionArgs]]
        ]
    ]: ...
    @resource_partitions.setter
    def resource_partitions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaResourcePartitionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceRegions")
    def resource_regions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceRegionArgs]]]
    ]: ...
    @resource_regions.setter
    def resource_regions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaResourceRegionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceTagArgs]]]
    ]: ...
    @resource_tags.setter
    def resource_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceTypeArgs]]]
    ]: ...
    @resource_types.setter
    def resource_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaResourceTypeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="severityLabels")
    def severity_labels(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaSeverityLabelArgs]]]
    ]: ...
    @severity_labels.setter
    def severity_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaSeverityLabelArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceUrls")
    def source_urls(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaSourceUrlArgs]]]
    ]: ...
    @source_urls.setter
    def source_urls(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaSourceUrlArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def titles(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaTitleArgs]]]
    ]: ...
    @titles.setter
    def titles(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaTitleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaTypeArgs]]]
    ]: ...
    @types.setter
    def types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaTypeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updatedAts")
    def updated_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaUpdatedAtArgs]]]
    ]: ...
    @updated_ats.setter
    def updated_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaUpdatedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaUserDefinedFieldArgs]]]
    ]: ...
    @user_defined_fields.setter
    def user_defined_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaUserDefinedFieldArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="verificationStates")
    def verification_states(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AutomationRuleCriteriaVerificationStateArgs]]
        ]
    ]: ...
    @verification_states.setter
    def verification_states(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaVerificationStateArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workflowStatuses")
    def workflow_statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AutomationRuleCriteriaWorkflowStatusArgs]]]
    ]: ...
    @workflow_statuses.setter
    def workflow_statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AutomationRuleCriteriaWorkflowStatusArgs]]
            ]
        ],
    ): ...

class AutomationRuleCriteriaAwsAccountIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaAwsAccountIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaAwsAccountNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaAwsAccountNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaCompanyNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaCompanyNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaComplianceAssociatedStandardsIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaComplianceAssociatedStandardsIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaComplianceSecurityControlIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaComplianceSecurityControlIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaComplianceStatusArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaComplianceStatusArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaConfidenceArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.float]]
    gt: NotRequired[pulumi.Input[_builtins.float]]
    gte: NotRequired[pulumi.Input[_builtins.float]]
    lt: NotRequired[pulumi.Input[_builtins.float]]
    lte: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class AutomationRuleCriteriaConfidenceArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.float]] = ...,
        gt: Optional[pulumi.Input[_builtins.float]] = ...,
        gte: Optional[pulumi.Input[_builtins.float]] = ...,
        lt: Optional[pulumi.Input[_builtins.float]] = ...,
        lte: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def gt(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @gt.setter
    def gt(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def lt(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @lt.setter
    def lt(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AutomationRuleCriteriaCreatedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[AutomationRuleCriteriaCreatedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleCriteriaCreatedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[AutomationRuleCriteriaCreatedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleCriteriaCreatedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[pulumi.Input[AutomationRuleCriteriaCreatedAtDateRangeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRuleCriteriaCreatedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class AutomationRuleCriteriaCreatedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class AutomationRuleCriteriaCriticalityArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.float]]
    gt: NotRequired[pulumi.Input[_builtins.float]]
    gte: NotRequired[pulumi.Input[_builtins.float]]
    lt: NotRequired[pulumi.Input[_builtins.float]]
    lte: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class AutomationRuleCriteriaCriticalityArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.float]] = ...,
        gt: Optional[pulumi.Input[_builtins.float]] = ...,
        gte: Optional[pulumi.Input[_builtins.float]] = ...,
        lt: Optional[pulumi.Input[_builtins.float]] = ...,
        lte: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def gt(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @gt.setter
    def gt(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def lt(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @lt.setter
    def lt(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AutomationRuleCriteriaDescriptionArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaDescriptionArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaFirstObservedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[AutomationRuleCriteriaFirstObservedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleCriteriaFirstObservedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[AutomationRuleCriteriaFirstObservedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleCriteriaFirstObservedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[
            pulumi.Input[AutomationRuleCriteriaFirstObservedAtDateRangeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRuleCriteriaFirstObservedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class AutomationRuleCriteriaFirstObservedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class AutomationRuleCriteriaGeneratorIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaGeneratorIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaLastObservedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[AutomationRuleCriteriaLastObservedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleCriteriaLastObservedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[AutomationRuleCriteriaLastObservedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleCriteriaLastObservedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[
            pulumi.Input[AutomationRuleCriteriaLastObservedAtDateRangeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRuleCriteriaLastObservedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class AutomationRuleCriteriaLastObservedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class AutomationRuleCriteriaNoteTextArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaNoteTextArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaNoteUpdatedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[AutomationRuleCriteriaNoteUpdatedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleCriteriaNoteUpdatedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[AutomationRuleCriteriaNoteUpdatedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleCriteriaNoteUpdatedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[pulumi.Input[AutomationRuleCriteriaNoteUpdatedAtDateRangeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRuleCriteriaNoteUpdatedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class AutomationRuleCriteriaNoteUpdatedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class AutomationRuleCriteriaNoteUpdatedByArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaNoteUpdatedByArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaProductArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaProductArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaProductNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaProductNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaRecordStateArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaRecordStateArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaRelatedFindingsIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaRelatedFindingsIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaRelatedFindingsProductArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaRelatedFindingsProductArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaResourceApplicationArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaResourceApplicationArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaResourceApplicationNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaResourceApplicationNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaResourceDetailsOtherArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaResourceDetailsOtherArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaResourceIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaResourceIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaResourcePartitionArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaResourcePartitionArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaResourceRegionArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaResourceRegionArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaResourceTagArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaResourceTagArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaResourceTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaResourceTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaSeverityLabelArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaSeverityLabelArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaSourceUrlArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaSourceUrlArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaTitleArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaTitleArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaUpdatedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[AutomationRuleCriteriaUpdatedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutomationRuleCriteriaUpdatedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[AutomationRuleCriteriaUpdatedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[AutomationRuleCriteriaUpdatedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[pulumi.Input[AutomationRuleCriteriaUpdatedAtDateRangeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutomationRuleCriteriaUpdatedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class AutomationRuleCriteriaUpdatedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class AutomationRuleCriteriaUserDefinedFieldArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaUserDefinedFieldArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaVerificationStateArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaVerificationStateArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class AutomationRuleCriteriaWorkflowStatusArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class AutomationRuleCriteriaWorkflowStatusArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ConfigurationPolicyConfigurationPolicyArgsDict(TypedDict):
    service_enabled: pulumi.Input[_builtins.bool]
    enabled_standard_arns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    security_controls_configuration: NotRequired[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationArgsDict
        ]
    ]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicyArgs:
    def __init__(
        __self__,
        *,
        service_enabled: pulumi.Input[_builtins.bool],
        enabled_standard_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_controls_configuration: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceEnabled")
    def service_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @service_enabled.setter
    def service_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="enabledStandardArns")
    def enabled_standard_arns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enabled_standard_arns.setter
    def enabled_standard_arns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityControlsConfiguration")
    def security_controls_configuration(
        self,
    ) -> Optional[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationArgs
        ]
    ]: ...
    @security_controls_configuration.setter
    def security_controls_configuration(
        self,
        value: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationArgs
            ]
        ],
    ): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationArgsDict(
    TypedDict
):
    disabled_control_identifiers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    enabled_control_identifiers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    security_control_custom_parameters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationArgs:
    def __init__(
        __self__,
        *,
        disabled_control_identifiers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enabled_control_identifiers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_control_custom_parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disabledControlIdentifiers")
    def disabled_control_identifiers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @disabled_control_identifiers.setter
    def disabled_control_identifiers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enabledControlIdentifiers")
    def enabled_control_identifiers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enabled_control_identifiers.setter
    def enabled_control_identifiers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityControlCustomParameters")
    def security_control_custom_parameters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterArgs
                ]
            ]
        ]
    ]: ...
    @security_control_custom_parameters.setter
    def security_control_custom_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterArgs
                    ]
                ]
            ]
        ],
    ): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterArgsDict(
    TypedDict
):
    parameters: pulumi.Input[
        Sequence[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterArgsDict
            ]
        ]
    ]
    security_control_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterArgs:
    def __init__(
        __self__,
        *,
        parameters: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterArgs
                ]
            ]
        ],
        security_control_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterArgs
            ]
        ]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityControlId")
    def security_control_id(self) -> pulumi.Input[_builtins.str]: ...
    @security_control_id.setter
    def security_control_id(self, value: pulumi.Input[_builtins.str]): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterArgsDict(
    TypedDict
):
    name: pulumi.Input[_builtins.str]
    value_type: pulumi.Input[_builtins.str]
    bool: NotRequired[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterBoolArgsDict
        ]
    ]
    double: NotRequired[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterDoubleArgsDict
        ]
    ]
    enum: NotRequired[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumArgsDict
        ]
    ]
    enum_list: NotRequired[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumListArgsDict
        ]
    ]
    int: NotRequired[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntArgsDict
        ]
    ]
    int_list: NotRequired[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntListArgsDict
        ]
    ]
    string: NotRequired[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringArgsDict
        ]
    ]
    string_list: NotRequired[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringListArgsDict
        ]
    ]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value_type: pulumi.Input[_builtins.str],
        bool: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterBoolArgs
            ]
        ] = ...,
        double: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterDoubleArgs
            ]
        ] = ...,
        enum: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumArgs
            ]
        ] = ...,
        enum_list: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumListArgs
            ]
        ] = ...,
        int: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntArgs
            ]
        ] = ...,
        int_list: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntListArgs
            ]
        ] = ...,
        string: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringArgs
            ]
        ] = ...,
        string_list: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringListArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> pulumi.Input[_builtins.str]: ...
    @value_type.setter
    def value_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def bool(
        self,
    ) -> Optional[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterBoolArgs
        ]
    ]: ...
    @bool.setter
    def bool(
        self,
        value: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterBoolArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def double(
        self,
    ) -> Optional[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterDoubleArgs
        ]
    ]: ...
    @double.setter
    def double(
        self,
        value: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterDoubleArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def enum(
        self,
    ) -> Optional[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumArgs
        ]
    ]: ...
    @enum.setter
    def enum(
        self,
        value: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enumList")
    def enum_list(
        self,
    ) -> Optional[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumListArgs
        ]
    ]: ...
    @enum_list.setter
    def enum_list(
        self,
        value: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumListArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def int(
        self,
    ) -> Optional[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntArgs
        ]
    ]: ...
    @int.setter
    def int(
        self,
        value: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="intList")
    def int_list(
        self,
    ) -> Optional[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntListArgs
        ]
    ]: ...
    @int_list.setter
    def int_list(
        self,
        value: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntListArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def string(
        self,
    ) -> Optional[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringArgs
        ]
    ]: ...
    @string.setter
    def string(
        self,
        value: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringList")
    def string_list(
        self,
    ) -> Optional[
        pulumi.Input[
            ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringListArgs
        ]
    ]: ...
    @string_list.setter
    def string_list(
        self,
        value: Optional[
            pulumi.Input[
                ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringListArgs
            ]
        ],
    ): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterBoolArgsDict(
    TypedDict
):
    value: pulumi.Input[_builtins.bool]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterBoolArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.bool]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.bool]): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterDoubleArgsDict(
    TypedDict
):
    value: pulumi.Input[_builtins.float]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterDoubleArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.float]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.float]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.float]): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumArgsDict(
    TypedDict
):
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumListArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumListArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntArgsDict(
    TypedDict
):
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntListArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntListArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringArgsDict(
    TypedDict
):
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringListArgsDict(
    TypedDict
):
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]

@pulumi.input_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringListArgs:
    def __init__(
        __self__, *, values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class InsightFiltersArgsDict(TypedDict):
    aws_account_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersAwsAccountIdArgsDict]]]
    ]
    company_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersCompanyNameArgsDict]]]
    ]
    compliance_statuses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersComplianceStatusArgsDict]]]
    ]
    confidences: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersConfidenceArgsDict]]]
    ]
    created_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersCreatedAtArgsDict]]]
    ]
    criticalities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersCriticalityArgsDict]]]
    ]
    descriptions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersDescriptionArgsDict]]]
    ]
    finding_provider_fields_confidences: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersFindingProviderFieldsConfidenceArgsDict]
            ]
        ]
    ]
    finding_provider_fields_criticalities: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersFindingProviderFieldsCriticalityArgsDict]
            ]
        ]
    ]
    finding_provider_fields_related_findings_ids: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InsightFiltersFindingProviderFieldsRelatedFindingsIdArgsDict
                ]
            ]
        ]
    ]
    finding_provider_fields_related_findings_product_arns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InsightFiltersFindingProviderFieldsRelatedFindingsProductArnArgsDict
                ]
            ]
        ]
    ]
    finding_provider_fields_severity_labels: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersFindingProviderFieldsSeverityLabelArgsDict]
            ]
        ]
    ]
    finding_provider_fields_severity_originals: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InsightFiltersFindingProviderFieldsSeverityOriginalArgsDict
                ]
            ]
        ]
    ]
    finding_provider_fields_types: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersFindingProviderFieldsTypeArgsDict]]
        ]
    ]
    first_observed_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersFirstObservedAtArgsDict]]]
    ]
    generator_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersGeneratorIdArgsDict]]]
    ]
    ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[InsightFiltersIdArgsDict]]]]
    keywords: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersKeywordArgsDict]]]
    ]
    last_observed_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersLastObservedAtArgsDict]]]
    ]
    malware_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareNameArgsDict]]]
    ]
    malware_paths: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwarePathArgsDict]]]
    ]
    malware_states: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareStateArgsDict]]]
    ]
    malware_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareTypeArgsDict]]]
    ]
    network_destination_domains: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersNetworkDestinationDomainArgsDict]]
        ]
    ]
    network_destination_ipv4s: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersNetworkDestinationIpv4ArgsDict]]
        ]
    ]
    network_destination_ipv6s: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersNetworkDestinationIpv6ArgsDict]]
        ]
    ]
    network_destination_ports: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersNetworkDestinationPortArgsDict]]
        ]
    ]
    network_directions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkDirectionArgsDict]]]
    ]
    network_protocols: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkProtocolArgsDict]]]
    ]
    network_source_domains: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceDomainArgsDict]]]
    ]
    network_source_ipv4s: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceIpv4ArgsDict]]]
    ]
    network_source_ipv6s: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceIpv6ArgsDict]]]
    ]
    network_source_macs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceMacArgsDict]]]
    ]
    network_source_ports: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourcePortArgsDict]]]
    ]
    note_texts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteTextArgsDict]]]
    ]
    note_updated_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteUpdatedAtArgsDict]]]
    ]
    note_updated_bies: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteUpdatedByArgsDict]]]
    ]
    process_launched_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessLaunchedAtArgsDict]]]
    ]
    process_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessNameArgsDict]]]
    ]
    process_parent_pids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessParentPidArgsDict]]]
    ]
    process_paths: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessPathArgsDict]]]
    ]
    process_pids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessPidArgsDict]]]
    ]
    process_terminated_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessTerminatedAtArgsDict]]]
    ]
    product_arns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductArnArgsDict]]]
    ]
    product_fields: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductFieldArgsDict]]]
    ]
    product_names: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductNameArgsDict]]]
    ]
    recommendation_texts: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersRecommendationTextArgsDict]]]
    ]
    record_states: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersRecordStateArgsDict]]]
    ]
    related_findings_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersRelatedFindingsIdArgsDict]]]
    ]
    related_findings_product_arns: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersRelatedFindingsProductArnArgsDict]]
        ]
    ]
    resource_aws_ec2_instance_iam_instance_profile_arns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnArgsDict
                ]
            ]
        ]
    ]
    resource_aws_ec2_instance_image_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceImageIdArgsDict]]
        ]
    ]
    resource_aws_ec2_instance_ipv4_addresses: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersResourceAwsEc2InstanceIpv4AddressArgsDict]
            ]
        ]
    ]
    resource_aws_ec2_instance_ipv6_addresses: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersResourceAwsEc2InstanceIpv6AddressArgsDict]
            ]
        ]
    ]
    resource_aws_ec2_instance_key_names: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceKeyNameArgsDict]]
        ]
    ]
    resource_aws_ec2_instance_launched_ats: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersResourceAwsEc2InstanceLaunchedAtArgsDict]
            ]
        ]
    ]
    resource_aws_ec2_instance_subnet_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceSubnetIdArgsDict]]
        ]
    ]
    resource_aws_ec2_instance_types: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceTypeArgsDict]]
        ]
    ]
    resource_aws_ec2_instance_vpc_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceVpcIdArgsDict]]
        ]
    ]
    resource_aws_iam_access_key_created_ats: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersResourceAwsIamAccessKeyCreatedAtArgsDict]
            ]
        ]
    ]
    resource_aws_iam_access_key_statuses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsIamAccessKeyStatusArgsDict]]
        ]
    ]
    resource_aws_iam_access_key_user_names: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersResourceAwsIamAccessKeyUserNameArgsDict]
            ]
        ]
    ]
    resource_aws_s3_bucket_owner_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsS3BucketOwnerIdArgsDict]]
        ]
    ]
    resource_aws_s3_bucket_owner_names: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsS3BucketOwnerNameArgsDict]]
        ]
    ]
    resource_container_image_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceContainerImageIdArgsDict]]
        ]
    ]
    resource_container_image_names: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceContainerImageNameArgsDict]]
        ]
    ]
    resource_container_launched_ats: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceContainerLaunchedAtArgsDict]]
        ]
    ]
    resource_container_names: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceContainerNameArgsDict]]
        ]
    ]
    resource_details_others: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceDetailsOtherArgsDict]]]
    ]
    resource_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceIdArgsDict]]]
    ]
    resource_partitions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourcePartitionArgsDict]]]
    ]
    resource_regions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceRegionArgsDict]]]
    ]
    resource_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceTagArgsDict]]]
    ]
    resource_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceTypeArgsDict]]]
    ]
    severity_labels: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersSeverityLabelArgsDict]]]
    ]
    source_urls: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersSourceUrlArgsDict]]]
    ]
    threat_intel_indicator_categories: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorCategoryArgsDict]]
        ]
    ]
    threat_intel_indicator_last_observed_ats: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersThreatIntelIndicatorLastObservedAtArgsDict]
            ]
        ]
    ]
    threat_intel_indicator_source_urls: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorSourceUrlArgsDict]]
        ]
    ]
    threat_intel_indicator_sources: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorSourceArgsDict]]
        ]
    ]
    threat_intel_indicator_types: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorTypeArgsDict]]
        ]
    ]
    threat_intel_indicator_values: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorValueArgsDict]]
        ]
    ]
    titles: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersTitleArgsDict]]]
    ]
    types: NotRequired[pulumi.Input[Sequence[pulumi.Input[InsightFiltersTypeArgsDict]]]]
    updated_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersUpdatedAtArgsDict]]]
    ]
    user_defined_values: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersUserDefinedValueArgsDict]]]
    ]
    verification_states: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersVerificationStateArgsDict]]]
    ]
    workflow_statuses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersWorkflowStatusArgsDict]]]
    ]

@pulumi.input_type
class InsightFiltersArgs:
    def __init__(
        __self__,
        *,
        aws_account_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersAwsAccountIdArgs]]]
        ] = ...,
        company_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersCompanyNameArgs]]]
        ] = ...,
        compliance_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersComplianceStatusArgs]]]
        ] = ...,
        confidences: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersConfidenceArgs]]]
        ] = ...,
        created_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersCreatedAtArgs]]]
        ] = ...,
        criticalities: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersCriticalityArgs]]]
        ] = ...,
        descriptions: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersDescriptionArgs]]]
        ] = ...,
        finding_provider_fields_confidences: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersFindingProviderFieldsConfidenceArgs]
                ]
            ]
        ] = ...,
        finding_provider_fields_criticalities: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersFindingProviderFieldsCriticalityArgs]
                ]
            ]
        ] = ...,
        finding_provider_fields_related_findings_ids: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InsightFiltersFindingProviderFieldsRelatedFindingsIdArgs
                    ]
                ]
            ]
        ] = ...,
        finding_provider_fields_related_findings_product_arns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InsightFiltersFindingProviderFieldsRelatedFindingsProductArnArgs
                    ]
                ]
            ]
        ] = ...,
        finding_provider_fields_severity_labels: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersFindingProviderFieldsSeverityLabelArgs]
                ]
            ]
        ] = ...,
        finding_provider_fields_severity_originals: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InsightFiltersFindingProviderFieldsSeverityOriginalArgs
                    ]
                ]
            ]
        ] = ...,
        finding_provider_fields_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersFindingProviderFieldsTypeArgs]]
            ]
        ] = ...,
        first_observed_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersFirstObservedAtArgs]]]
        ] = ...,
        generator_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersGeneratorIdArgs]]]
        ] = ...,
        ids: Optional[pulumi.Input[Sequence[pulumi.Input[InsightFiltersIdArgs]]]] = ...,
        keywords: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersKeywordArgs]]]
        ] = ...,
        last_observed_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersLastObservedAtArgs]]]
        ] = ...,
        malware_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareNameArgs]]]
        ] = ...,
        malware_paths: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwarePathArgs]]]
        ] = ...,
        malware_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareStateArgs]]]
        ] = ...,
        malware_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareTypeArgs]]]
        ] = ...,
        network_destination_domains: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersNetworkDestinationDomainArgs]]
            ]
        ] = ...,
        network_destination_ipv4s: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersNetworkDestinationIpv4Args]]
            ]
        ] = ...,
        network_destination_ipv6s: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersNetworkDestinationIpv6Args]]
            ]
        ] = ...,
        network_destination_ports: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersNetworkDestinationPortArgs]]
            ]
        ] = ...,
        network_directions: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkDirectionArgs]]]
        ] = ...,
        network_protocols: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkProtocolArgs]]]
        ] = ...,
        network_source_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceDomainArgs]]]
        ] = ...,
        network_source_ipv4s: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceIpv4Args]]]
        ] = ...,
        network_source_ipv6s: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceIpv6Args]]]
        ] = ...,
        network_source_macs: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceMacArgs]]]
        ] = ...,
        network_source_ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourcePortArgs]]]
        ] = ...,
        note_texts: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteTextArgs]]]
        ] = ...,
        note_updated_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteUpdatedAtArgs]]]
        ] = ...,
        note_updated_bies: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteUpdatedByArgs]]]
        ] = ...,
        process_launched_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessLaunchedAtArgs]]]
        ] = ...,
        process_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessNameArgs]]]
        ] = ...,
        process_parent_pids: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessParentPidArgs]]]
        ] = ...,
        process_paths: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessPathArgs]]]
        ] = ...,
        process_pids: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessPidArgs]]]
        ] = ...,
        process_terminated_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessTerminatedAtArgs]]]
        ] = ...,
        product_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductArnArgs]]]
        ] = ...,
        product_fields: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductFieldArgs]]]
        ] = ...,
        product_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductNameArgs]]]
        ] = ...,
        recommendation_texts: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersRecommendationTextArgs]]]
        ] = ...,
        record_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersRecordStateArgs]]]
        ] = ...,
        related_findings_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersRelatedFindingsIdArgs]]]
        ] = ...,
        related_findings_product_arns: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersRelatedFindingsProductArnArgs]]
            ]
        ] = ...,
        resource_aws_ec2_instance_iam_instance_profile_arns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnArgs
                    ]
                ]
            ]
        ] = ...,
        resource_aws_ec2_instance_image_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceImageIdArgs]]
            ]
        ] = ...,
        resource_aws_ec2_instance_ipv4_addresses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsEc2InstanceIpv4AddressArgs]
                ]
            ]
        ] = ...,
        resource_aws_ec2_instance_ipv6_addresses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsEc2InstanceIpv6AddressArgs]
                ]
            ]
        ] = ...,
        resource_aws_ec2_instance_key_names: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceKeyNameArgs]]
            ]
        ] = ...,
        resource_aws_ec2_instance_launched_ats: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsEc2InstanceLaunchedAtArgs]
                ]
            ]
        ] = ...,
        resource_aws_ec2_instance_subnet_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceSubnetIdArgs]]
            ]
        ] = ...,
        resource_aws_ec2_instance_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceTypeArgs]]
            ]
        ] = ...,
        resource_aws_ec2_instance_vpc_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceVpcIdArgs]]
            ]
        ] = ...,
        resource_aws_iam_access_key_created_ats: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsIamAccessKeyCreatedAtArgs]
                ]
            ]
        ] = ...,
        resource_aws_iam_access_key_statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsIamAccessKeyStatusArgs]]
            ]
        ] = ...,
        resource_aws_iam_access_key_user_names: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsIamAccessKeyUserNameArgs]
                ]
            ]
        ] = ...,
        resource_aws_s3_bucket_owner_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsS3BucketOwnerIdArgs]]
            ]
        ] = ...,
        resource_aws_s3_bucket_owner_names: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsS3BucketOwnerNameArgs]]
            ]
        ] = ...,
        resource_container_image_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceContainerImageIdArgs]]
            ]
        ] = ...,
        resource_container_image_names: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceContainerImageNameArgs]]
            ]
        ] = ...,
        resource_container_launched_ats: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceContainerLaunchedAtArgs]]
            ]
        ] = ...,
        resource_container_names: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceContainerNameArgs]]
            ]
        ] = ...,
        resource_details_others: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceDetailsOtherArgs]]]
        ] = ...,
        resource_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceIdArgs]]]
        ] = ...,
        resource_partitions: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourcePartitionArgs]]]
        ] = ...,
        resource_regions: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceRegionArgs]]]
        ] = ...,
        resource_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceTagArgs]]]
        ] = ...,
        resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceTypeArgs]]]
        ] = ...,
        severity_labels: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersSeverityLabelArgs]]]
        ] = ...,
        source_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersSourceUrlArgs]]]
        ] = ...,
        threat_intel_indicator_categories: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorCategoryArgs]]
            ]
        ] = ...,
        threat_intel_indicator_last_observed_ats: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersThreatIntelIndicatorLastObservedAtArgs]
                ]
            ]
        ] = ...,
        threat_intel_indicator_source_urls: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorSourceUrlArgs]]
            ]
        ] = ...,
        threat_intel_indicator_sources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorSourceArgs]]
            ]
        ] = ...,
        threat_intel_indicator_types: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorTypeArgs]]
            ]
        ] = ...,
        threat_intel_indicator_values: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorValueArgs]]
            ]
        ] = ...,
        titles: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersTitleArgs]]]
        ] = ...,
        types: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersTypeArgs]]]
        ] = ...,
        updated_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersUpdatedAtArgs]]]
        ] = ...,
        user_defined_values: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersUserDefinedValueArgs]]]
        ] = ...,
        verification_states: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersVerificationStateArgs]]]
        ] = ...,
        workflow_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersWorkflowStatusArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountIds")
    def aws_account_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersAwsAccountIdArgs]]]
    ]: ...
    @aws_account_ids.setter
    def aws_account_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersAwsAccountIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="companyNames")
    def company_names(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersCompanyNameArgs]]]
    ]: ...
    @company_names.setter
    def company_names(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersCompanyNameArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="complianceStatuses")
    def compliance_statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersComplianceStatusArgs]]]
    ]: ...
    @compliance_statuses.setter
    def compliance_statuses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersComplianceStatusArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def confidences(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersConfidenceArgs]]]
    ]: ...
    @confidences.setter
    def confidences(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersConfidenceArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createdAts")
    def created_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersCreatedAtArgs]]]
    ]: ...
    @created_ats.setter
    def created_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersCreatedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def criticalities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersCriticalityArgs]]]
    ]: ...
    @criticalities.setter
    def criticalities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersCriticalityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def descriptions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersDescriptionArgs]]]
    ]: ...
    @descriptions.setter
    def descriptions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersDescriptionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsConfidences")
    def finding_provider_fields_confidences(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersFindingProviderFieldsConfidenceArgs]]
        ]
    ]: ...
    @finding_provider_fields_confidences.setter
    def finding_provider_fields_confidences(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersFindingProviderFieldsConfidenceArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsCriticalities")
    def finding_provider_fields_criticalities(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersFindingProviderFieldsCriticalityArgs]]
        ]
    ]: ...
    @finding_provider_fields_criticalities.setter
    def finding_provider_fields_criticalities(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersFindingProviderFieldsCriticalityArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsRelatedFindingsIds")
    def finding_provider_fields_related_findings_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersFindingProviderFieldsRelatedFindingsIdArgs]
            ]
        ]
    ]: ...
    @finding_provider_fields_related_findings_ids.setter
    def finding_provider_fields_related_findings_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InsightFiltersFindingProviderFieldsRelatedFindingsIdArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsRelatedFindingsProductArns")
    def finding_provider_fields_related_findings_product_arns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InsightFiltersFindingProviderFieldsRelatedFindingsProductArnArgs
                ]
            ]
        ]
    ]: ...
    @finding_provider_fields_related_findings_product_arns.setter
    def finding_provider_fields_related_findings_product_arns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InsightFiltersFindingProviderFieldsRelatedFindingsProductArnArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsSeverityLabels")
    def finding_provider_fields_severity_labels(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersFindingProviderFieldsSeverityLabelArgs]]
        ]
    ]: ...
    @finding_provider_fields_severity_labels.setter
    def finding_provider_fields_severity_labels(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersFindingProviderFieldsSeverityLabelArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsSeverityOriginals")
    def finding_provider_fields_severity_originals(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[InsightFiltersFindingProviderFieldsSeverityOriginalArgs]
            ]
        ]
    ]: ...
    @finding_provider_fields_severity_originals.setter
    def finding_provider_fields_severity_originals(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InsightFiltersFindingProviderFieldsSeverityOriginalArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsTypes")
    def finding_provider_fields_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersFindingProviderFieldsTypeArgs]]
        ]
    ]: ...
    @finding_provider_fields_types.setter
    def finding_provider_fields_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersFindingProviderFieldsTypeArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="firstObservedAts")
    def first_observed_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersFirstObservedAtArgs]]]
    ]: ...
    @first_observed_ats.setter
    def first_observed_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersFirstObservedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="generatorIds")
    def generator_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersGeneratorIdArgs]]]
    ]: ...
    @generator_ids.setter
    def generator_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersGeneratorIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InsightFiltersIdArgs]]]]: ...
    @ids.setter
    def ids(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InsightFiltersIdArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def keywords(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InsightFiltersKeywordArgs]]]]: ...
    @keywords.setter
    def keywords(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersKeywordArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastObservedAts")
    def last_observed_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersLastObservedAtArgs]]]
    ]: ...
    @last_observed_ats.setter
    def last_observed_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersLastObservedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="malwareNames")
    def malware_names(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareNameArgs]]]
    ]: ...
    @malware_names.setter
    def malware_names(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareNameArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="malwarePaths")
    def malware_paths(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwarePathArgs]]]
    ]: ...
    @malware_paths.setter
    def malware_paths(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwarePathArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="malwareStates")
    def malware_states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareStateArgs]]]
    ]: ...
    @malware_states.setter
    def malware_states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="malwareTypes")
    def malware_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareTypeArgs]]]
    ]: ...
    @malware_types.setter
    def malware_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersMalwareTypeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkDestinationDomains")
    def network_destination_domains(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkDestinationDomainArgs]]]
    ]: ...
    @network_destination_domains.setter
    def network_destination_domains(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersNetworkDestinationDomainArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkDestinationIpv4s")
    def network_destination_ipv4s(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkDestinationIpv4Args]]]
    ]: ...
    @network_destination_ipv4s.setter
    def network_destination_ipv4s(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersNetworkDestinationIpv4Args]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkDestinationIpv6s")
    def network_destination_ipv6s(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkDestinationIpv6Args]]]
    ]: ...
    @network_destination_ipv6s.setter
    def network_destination_ipv6s(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersNetworkDestinationIpv6Args]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkDestinationPorts")
    def network_destination_ports(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkDestinationPortArgs]]]
    ]: ...
    @network_destination_ports.setter
    def network_destination_ports(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersNetworkDestinationPortArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkDirections")
    def network_directions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkDirectionArgs]]]
    ]: ...
    @network_directions.setter
    def network_directions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkDirectionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkProtocols")
    def network_protocols(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkProtocolArgs]]]
    ]: ...
    @network_protocols.setter
    def network_protocols(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkProtocolArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkSourceDomains")
    def network_source_domains(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceDomainArgs]]]
    ]: ...
    @network_source_domains.setter
    def network_source_domains(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceDomainArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkSourceIpv4s")
    def network_source_ipv4s(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceIpv4Args]]]
    ]: ...
    @network_source_ipv4s.setter
    def network_source_ipv4s(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceIpv4Args]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkSourceIpv6s")
    def network_source_ipv6s(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceIpv6Args]]]
    ]: ...
    @network_source_ipv6s.setter
    def network_source_ipv6s(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceIpv6Args]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkSourceMacs")
    def network_source_macs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceMacArgs]]]
    ]: ...
    @network_source_macs.setter
    def network_source_macs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourceMacArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkSourcePorts")
    def network_source_ports(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourcePortArgs]]]
    ]: ...
    @network_source_ports.setter
    def network_source_ports(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNetworkSourcePortArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="noteTexts")
    def note_texts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteTextArgs]]]]: ...
    @note_texts.setter
    def note_texts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteTextArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="noteUpdatedAts")
    def note_updated_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteUpdatedAtArgs]]]
    ]: ...
    @note_updated_ats.setter
    def note_updated_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteUpdatedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="noteUpdatedBies")
    def note_updated_bies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteUpdatedByArgs]]]
    ]: ...
    @note_updated_bies.setter
    def note_updated_bies(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersNoteUpdatedByArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="processLaunchedAts")
    def process_launched_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessLaunchedAtArgs]]]
    ]: ...
    @process_launched_ats.setter
    def process_launched_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessLaunchedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="processNames")
    def process_names(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessNameArgs]]]
    ]: ...
    @process_names.setter
    def process_names(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessNameArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="processParentPids")
    def process_parent_pids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessParentPidArgs]]]
    ]: ...
    @process_parent_pids.setter
    def process_parent_pids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessParentPidArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="processPaths")
    def process_paths(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessPathArgs]]]
    ]: ...
    @process_paths.setter
    def process_paths(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessPathArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="processPids")
    def process_pids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessPidArgs]]]
    ]: ...
    @process_pids.setter
    def process_pids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessPidArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="processTerminatedAts")
    def process_terminated_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessTerminatedAtArgs]]]
    ]: ...
    @process_terminated_ats.setter
    def process_terminated_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProcessTerminatedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="productArns")
    def product_arns(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductArnArgs]]]
    ]: ...
    @product_arns.setter
    def product_arns(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductArnArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="productFields")
    def product_fields(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductFieldArgs]]]
    ]: ...
    @product_fields.setter
    def product_fields(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductFieldArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="productNames")
    def product_names(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductNameArgs]]]
    ]: ...
    @product_names.setter
    def product_names(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersProductNameArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recommendationTexts")
    def recommendation_texts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersRecommendationTextArgs]]]
    ]: ...
    @recommendation_texts.setter
    def recommendation_texts(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersRecommendationTextArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recordStates")
    def record_states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersRecordStateArgs]]]
    ]: ...
    @record_states.setter
    def record_states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersRecordStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="relatedFindingsIds")
    def related_findings_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersRelatedFindingsIdArgs]]]
    ]: ...
    @related_findings_ids.setter
    def related_findings_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersRelatedFindingsIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="relatedFindingsProductArns")
    def related_findings_product_arns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersRelatedFindingsProductArnArgs]]
        ]
    ]: ...
    @related_findings_product_arns.setter
    def related_findings_product_arns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersRelatedFindingsProductArnArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceIamInstanceProfileArns")
    def resource_aws_ec2_instance_iam_instance_profile_arns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    InsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnArgs
                ]
            ]
        ]
    ]: ...
    @resource_aws_ec2_instance_iam_instance_profile_arns.setter
    def resource_aws_ec2_instance_iam_instance_profile_arns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        InsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceImageIds")
    def resource_aws_ec2_instance_image_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceImageIdArgs]]
        ]
    ]: ...
    @resource_aws_ec2_instance_image_ids.setter
    def resource_aws_ec2_instance_image_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceImageIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceIpv4Addresses")
    def resource_aws_ec2_instance_ipv4_addresses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceIpv4AddressArgs]]
        ]
    ]: ...
    @resource_aws_ec2_instance_ipv4_addresses.setter
    def resource_aws_ec2_instance_ipv4_addresses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsEc2InstanceIpv4AddressArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceIpv6Addresses")
    def resource_aws_ec2_instance_ipv6_addresses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceIpv6AddressArgs]]
        ]
    ]: ...
    @resource_aws_ec2_instance_ipv6_addresses.setter
    def resource_aws_ec2_instance_ipv6_addresses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsEc2InstanceIpv6AddressArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceKeyNames")
    def resource_aws_ec2_instance_key_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceKeyNameArgs]]
        ]
    ]: ...
    @resource_aws_ec2_instance_key_names.setter
    def resource_aws_ec2_instance_key_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceKeyNameArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceLaunchedAts")
    def resource_aws_ec2_instance_launched_ats(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceLaunchedAtArgs]]
        ]
    ]: ...
    @resource_aws_ec2_instance_launched_ats.setter
    def resource_aws_ec2_instance_launched_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsEc2InstanceLaunchedAtArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceSubnetIds")
    def resource_aws_ec2_instance_subnet_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceSubnetIdArgs]]
        ]
    ]: ...
    @resource_aws_ec2_instance_subnet_ids.setter
    def resource_aws_ec2_instance_subnet_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceSubnetIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceTypes")
    def resource_aws_ec2_instance_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceTypeArgs]]
        ]
    ]: ...
    @resource_aws_ec2_instance_types.setter
    def resource_aws_ec2_instance_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceTypeArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceVpcIds")
    def resource_aws_ec2_instance_vpc_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceVpcIdArgs]]
        ]
    ]: ...
    @resource_aws_ec2_instance_vpc_ids.setter
    def resource_aws_ec2_instance_vpc_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsEc2InstanceVpcIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsIamAccessKeyCreatedAts")
    def resource_aws_iam_access_key_created_ats(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsIamAccessKeyCreatedAtArgs]]
        ]
    ]: ...
    @resource_aws_iam_access_key_created_ats.setter
    def resource_aws_iam_access_key_created_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsIamAccessKeyCreatedAtArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsIamAccessKeyStatuses")
    def resource_aws_iam_access_key_statuses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsIamAccessKeyStatusArgs]]
        ]
    ]: ...
    @resource_aws_iam_access_key_statuses.setter
    def resource_aws_iam_access_key_statuses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsIamAccessKeyStatusArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsIamAccessKeyUserNames")
    def resource_aws_iam_access_key_user_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsIamAccessKeyUserNameArgs]]
        ]
    ]: ...
    @resource_aws_iam_access_key_user_names.setter
    def resource_aws_iam_access_key_user_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersResourceAwsIamAccessKeyUserNameArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsS3BucketOwnerIds")
    def resource_aws_s3_bucket_owner_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsS3BucketOwnerIdArgs]]
        ]
    ]: ...
    @resource_aws_s3_bucket_owner_ids.setter
    def resource_aws_s3_bucket_owner_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsS3BucketOwnerIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceAwsS3BucketOwnerNames")
    def resource_aws_s3_bucket_owner_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceAwsS3BucketOwnerNameArgs]]
        ]
    ]: ...
    @resource_aws_s3_bucket_owner_names.setter
    def resource_aws_s3_bucket_owner_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceAwsS3BucketOwnerNameArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceContainerImageIds")
    def resource_container_image_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceContainerImageIdArgs]]]
    ]: ...
    @resource_container_image_ids.setter
    def resource_container_image_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceContainerImageIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceContainerImageNames")
    def resource_container_image_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceContainerImageNameArgs]]
        ]
    ]: ...
    @resource_container_image_names.setter
    def resource_container_image_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceContainerImageNameArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceContainerLaunchedAts")
    def resource_container_launched_ats(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersResourceContainerLaunchedAtArgs]]
        ]
    ]: ...
    @resource_container_launched_ats.setter
    def resource_container_launched_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceContainerLaunchedAtArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceContainerNames")
    def resource_container_names(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceContainerNameArgs]]]
    ]: ...
    @resource_container_names.setter
    def resource_container_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersResourceContainerNameArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceDetailsOthers")
    def resource_details_others(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceDetailsOtherArgs]]]
    ]: ...
    @resource_details_others.setter
    def resource_details_others(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceDetailsOtherArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceIds")
    def resource_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceIdArgs]]]
    ]: ...
    @resource_ids.setter
    def resource_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourcePartitions")
    def resource_partitions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourcePartitionArgs]]]
    ]: ...
    @resource_partitions.setter
    def resource_partitions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourcePartitionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceRegions")
    def resource_regions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceRegionArgs]]]
    ]: ...
    @resource_regions.setter
    def resource_regions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceRegionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceTagArgs]]]
    ]: ...
    @resource_tags.setter
    def resource_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceTypeArgs]]]
    ]: ...
    @resource_types.setter
    def resource_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersResourceTypeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="severityLabels")
    def severity_labels(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersSeverityLabelArgs]]]
    ]: ...
    @severity_labels.setter
    def severity_labels(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersSeverityLabelArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceUrls")
    def source_urls(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersSourceUrlArgs]]]
    ]: ...
    @source_urls.setter
    def source_urls(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersSourceUrlArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorCategories")
    def threat_intel_indicator_categories(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorCategoryArgs]]
        ]
    ]: ...
    @threat_intel_indicator_categories.setter
    def threat_intel_indicator_categories(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorCategoryArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorLastObservedAts")
    def threat_intel_indicator_last_observed_ats(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorLastObservedAtArgs]]
        ]
    ]: ...
    @threat_intel_indicator_last_observed_ats.setter
    def threat_intel_indicator_last_observed_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[InsightFiltersThreatIntelIndicatorLastObservedAtArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorSourceUrls")
    def threat_intel_indicator_source_urls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorSourceUrlArgs]]
        ]
    ]: ...
    @threat_intel_indicator_source_urls.setter
    def threat_intel_indicator_source_urls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorSourceUrlArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorSources")
    def threat_intel_indicator_sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorSourceArgs]]
        ]
    ]: ...
    @threat_intel_indicator_sources.setter
    def threat_intel_indicator_sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorSourceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorTypes")
    def threat_intel_indicator_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorTypeArgs]]]
    ]: ...
    @threat_intel_indicator_types.setter
    def threat_intel_indicator_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorTypeArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorValues")
    def threat_intel_indicator_values(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorValueArgs]]
        ]
    ]: ...
    @threat_intel_indicator_values.setter
    def threat_intel_indicator_values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[InsightFiltersThreatIntelIndicatorValueArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def titles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InsightFiltersTitleArgs]]]]: ...
    @titles.setter
    def titles(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InsightFiltersTitleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[InsightFiltersTypeArgs]]]]: ...
    @types.setter
    def types(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[InsightFiltersTypeArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updatedAts")
    def updated_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersUpdatedAtArgs]]]
    ]: ...
    @updated_ats.setter
    def updated_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersUpdatedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="userDefinedValues")
    def user_defined_values(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersUserDefinedValueArgs]]]
    ]: ...
    @user_defined_values.setter
    def user_defined_values(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersUserDefinedValueArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="verificationStates")
    def verification_states(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersVerificationStateArgs]]]
    ]: ...
    @verification_states.setter
    def verification_states(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersVerificationStateArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workflowStatuses")
    def workflow_statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[InsightFiltersWorkflowStatusArgs]]]
    ]: ...
    @workflow_statuses.setter
    def workflow_statuses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[InsightFiltersWorkflowStatusArgs]]]
        ],
    ): ...

class InsightFiltersAwsAccountIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersAwsAccountIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersCompanyNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersCompanyNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersComplianceStatusArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersComplianceStatusArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersConfidenceArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.str]]
    gte: NotRequired[pulumi.Input[_builtins.str]]
    lte: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersConfidenceArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.str]] = ...,
        gte: Optional[pulumi.Input[_builtins.str]] = ...,
        lte: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersCreatedAtArgsDict(TypedDict):
    date_range: NotRequired[pulumi.Input[InsightFiltersCreatedAtDateRangeArgsDict]]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersCreatedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[pulumi.Input[InsightFiltersCreatedAtDateRangeArgs]] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[InsightFiltersCreatedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self, value: Optional[pulumi.Input[InsightFiltersCreatedAtDateRangeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersCreatedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersCreatedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersCriticalityArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.str]]
    gte: NotRequired[pulumi.Input[_builtins.str]]
    lte: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersCriticalityArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.str]] = ...,
        gte: Optional[pulumi.Input[_builtins.str]] = ...,
        lte: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersDescriptionArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersDescriptionArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersFindingProviderFieldsConfidenceArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.str]]
    gte: NotRequired[pulumi.Input[_builtins.str]]
    lte: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersFindingProviderFieldsConfidenceArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.str]] = ...,
        gte: Optional[pulumi.Input[_builtins.str]] = ...,
        lte: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersFindingProviderFieldsCriticalityArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.str]]
    gte: NotRequired[pulumi.Input[_builtins.str]]
    lte: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersFindingProviderFieldsCriticalityArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.str]] = ...,
        gte: Optional[pulumi.Input[_builtins.str]] = ...,
        lte: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersFindingProviderFieldsRelatedFindingsIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersFindingProviderFieldsRelatedFindingsIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersFindingProviderFieldsRelatedFindingsProductArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersFindingProviderFieldsRelatedFindingsProductArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersFindingProviderFieldsSeverityLabelArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersFindingProviderFieldsSeverityLabelArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersFindingProviderFieldsSeverityOriginalArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersFindingProviderFieldsSeverityOriginalArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersFindingProviderFieldsTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersFindingProviderFieldsTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersFirstObservedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[InsightFiltersFirstObservedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersFirstObservedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[InsightFiltersFirstObservedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[InsightFiltersFirstObservedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self, value: Optional[pulumi.Input[InsightFiltersFirstObservedAtDateRangeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersFirstObservedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersFirstObservedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersGeneratorIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersGeneratorIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersKeywordArgsDict(TypedDict):
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersKeywordArgs:
    def __init__(__self__, *, value: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersLastObservedAtArgsDict(TypedDict):
    date_range: NotRequired[pulumi.Input[InsightFiltersLastObservedAtDateRangeArgsDict]]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersLastObservedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[InsightFiltersLastObservedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[InsightFiltersLastObservedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self, value: Optional[pulumi.Input[InsightFiltersLastObservedAtDateRangeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersLastObservedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersLastObservedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersMalwareNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersMalwareNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersMalwarePathArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersMalwarePathArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersMalwareStateArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersMalwareStateArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersMalwareTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersMalwareTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkDestinationDomainArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNetworkDestinationDomainArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkDestinationIpv4ArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNetworkDestinationIpv4Args:
    def __init__(__self__, *, cidr: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]: ...
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkDestinationIpv6ArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNetworkDestinationIpv6Args:
    def __init__(__self__, *, cidr: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]: ...
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkDestinationPortArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.str]]
    gte: NotRequired[pulumi.Input[_builtins.str]]
    lte: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersNetworkDestinationPortArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.str]] = ...,
        gte: Optional[pulumi.Input[_builtins.str]] = ...,
        lte: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersNetworkDirectionArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNetworkDirectionArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkProtocolArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNetworkProtocolArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkSourceDomainArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNetworkSourceDomainArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkSourceIpv4ArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNetworkSourceIpv4Args:
    def __init__(__self__, *, cidr: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]: ...
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkSourceIpv6ArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNetworkSourceIpv6Args:
    def __init__(__self__, *, cidr: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]: ...
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkSourceMacArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNetworkSourceMacArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNetworkSourcePortArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.str]]
    gte: NotRequired[pulumi.Input[_builtins.str]]
    lte: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersNetworkSourcePortArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.str]] = ...,
        gte: Optional[pulumi.Input[_builtins.str]] = ...,
        lte: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersNoteTextArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNoteTextArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersNoteUpdatedAtArgsDict(TypedDict):
    date_range: NotRequired[pulumi.Input[InsightFiltersNoteUpdatedAtDateRangeArgsDict]]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersNoteUpdatedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[InsightFiltersNoteUpdatedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[InsightFiltersNoteUpdatedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self, value: Optional[pulumi.Input[InsightFiltersNoteUpdatedAtDateRangeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersNoteUpdatedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersNoteUpdatedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersNoteUpdatedByArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersNoteUpdatedByArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersProcessLaunchedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[InsightFiltersProcessLaunchedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersProcessLaunchedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[InsightFiltersProcessLaunchedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[InsightFiltersProcessLaunchedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[pulumi.Input[InsightFiltersProcessLaunchedAtDateRangeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersProcessLaunchedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersProcessLaunchedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersProcessNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersProcessNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersProcessParentPidArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.str]]
    gte: NotRequired[pulumi.Input[_builtins.str]]
    lte: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersProcessParentPidArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.str]] = ...,
        gte: Optional[pulumi.Input[_builtins.str]] = ...,
        lte: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersProcessPathArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersProcessPathArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersProcessPidArgsDict(TypedDict):
    eq: NotRequired[pulumi.Input[_builtins.str]]
    gte: NotRequired[pulumi.Input[_builtins.str]]
    lte: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersProcessPidArgs:
    def __init__(
        __self__,
        *,
        eq: Optional[pulumi.Input[_builtins.str]] = ...,
        gte: Optional[pulumi.Input[_builtins.str]] = ...,
        lte: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @eq.setter
    def eq(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gte.setter
    def gte(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lte.setter
    def lte(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersProcessTerminatedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[InsightFiltersProcessTerminatedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersProcessTerminatedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[InsightFiltersProcessTerminatedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[InsightFiltersProcessTerminatedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[pulumi.Input[InsightFiltersProcessTerminatedAtDateRangeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersProcessTerminatedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersProcessTerminatedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersProductArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersProductArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersProductFieldArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersProductFieldArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersProductNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersProductNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersRecommendationTextArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersRecommendationTextArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersRecordStateArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersRecordStateArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersRelatedFindingsIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersRelatedFindingsIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersRelatedFindingsProductArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersRelatedFindingsProductArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceIamInstanceProfileArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsEc2InstanceImageIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceImageIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsEc2InstanceIpv4AddressArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceIpv4AddressArgs:
    def __init__(__self__, *, cidr: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]: ...
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsEc2InstanceIpv6AddressArgsDict(TypedDict):
    cidr: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceIpv6AddressArgs:
    def __init__(__self__, *, cidr: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> pulumi.Input[_builtins.str]: ...
    @cidr.setter
    def cidr(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsEc2InstanceKeyNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceKeyNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsEc2InstanceLaunchedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[InsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceLaunchedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[InsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[
        pulumi.Input[InsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeArgs]
    ]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[
            pulumi.Input[InsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceLaunchedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersResourceAwsEc2InstanceSubnetIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceSubnetIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsEc2InstanceTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsEc2InstanceVpcIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsEc2InstanceVpcIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsIamAccessKeyCreatedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[InsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersResourceAwsIamAccessKeyCreatedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[InsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[
        pulumi.Input[InsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeArgs]
    ]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[
            pulumi.Input[InsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersResourceAwsIamAccessKeyCreatedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersResourceAwsIamAccessKeyStatusArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsIamAccessKeyStatusArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsIamAccessKeyUserNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsIamAccessKeyUserNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsS3BucketOwnerIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsS3BucketOwnerIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceAwsS3BucketOwnerNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceAwsS3BucketOwnerNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceContainerImageIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceContainerImageIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceContainerImageNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceContainerImageNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceContainerLaunchedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[InsightFiltersResourceContainerLaunchedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersResourceContainerLaunchedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[InsightFiltersResourceContainerLaunchedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[
        pulumi.Input[InsightFiltersResourceContainerLaunchedAtDateRangeArgs]
    ]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[
            pulumi.Input[InsightFiltersResourceContainerLaunchedAtDateRangeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersResourceContainerLaunchedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersResourceContainerLaunchedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersResourceContainerNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceContainerNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceDetailsOtherArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceDetailsOtherArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourcePartitionArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourcePartitionArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceRegionArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceRegionArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceTagArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceTagArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersResourceTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersResourceTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersSeverityLabelArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersSeverityLabelArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersSourceUrlArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersSourceUrlArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersThreatIntelIndicatorCategoryArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersThreatIntelIndicatorCategoryArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersThreatIntelIndicatorLastObservedAtArgsDict(TypedDict):
    date_range: NotRequired[
        pulumi.Input[InsightFiltersThreatIntelIndicatorLastObservedAtDateRangeArgsDict]
    ]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersThreatIntelIndicatorLastObservedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[
            pulumi.Input[InsightFiltersThreatIntelIndicatorLastObservedAtDateRangeArgs]
        ] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[
        pulumi.Input[InsightFiltersThreatIntelIndicatorLastObservedAtDateRangeArgs]
    ]: ...
    @date_range.setter
    def date_range(
        self,
        value: Optional[
            pulumi.Input[InsightFiltersThreatIntelIndicatorLastObservedAtDateRangeArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersThreatIntelIndicatorLastObservedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersThreatIntelIndicatorLastObservedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersThreatIntelIndicatorSourceArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersThreatIntelIndicatorSourceArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersThreatIntelIndicatorSourceUrlArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersThreatIntelIndicatorSourceUrlArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersThreatIntelIndicatorTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersThreatIntelIndicatorTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersThreatIntelIndicatorValueArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersThreatIntelIndicatorValueArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersTitleArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersTitleArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersUpdatedAtArgsDict(TypedDict):
    date_range: NotRequired[pulumi.Input[InsightFiltersUpdatedAtDateRangeArgsDict]]
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class InsightFiltersUpdatedAtArgs:
    def __init__(
        __self__,
        *,
        date_range: Optional[pulumi.Input[InsightFiltersUpdatedAtDateRangeArgs]] = ...,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(
        self,
    ) -> Optional[pulumi.Input[InsightFiltersUpdatedAtDateRangeArgs]]: ...
    @date_range.setter
    def date_range(
        self, value: Optional[pulumi.Input[InsightFiltersUpdatedAtDateRangeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class InsightFiltersUpdatedAtDateRangeArgsDict(TypedDict):
    unit: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.int]

@pulumi.input_type
class InsightFiltersUpdatedAtDateRangeArgs:
    def __init__(
        __self__,
        *,
        unit: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def unit(self) -> pulumi.Input[_builtins.str]: ...
    @unit.setter
    def unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.int]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.int]): ...

class InsightFiltersUserDefinedValueArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersUserDefinedValueArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersVerificationStateArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersVerificationStateArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class InsightFiltersWorkflowStatusArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class InsightFiltersWorkflowStatusArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class OrganizationConfigurationOrganizationConfigurationArgsDict(TypedDict):
    configuration_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class OrganizationConfigurationOrganizationConfigurationArgs:
    def __init__(
        __self__, *, configuration_type: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> pulumi.Input[_builtins.str]: ...
    @configuration_type.setter
    def configuration_type(self, value: pulumi.Input[_builtins.str]): ...
