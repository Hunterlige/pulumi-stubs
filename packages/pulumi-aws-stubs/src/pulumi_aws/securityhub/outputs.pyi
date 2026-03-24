

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AutomationRuleAction', 'AutomationRuleActionFindingFieldsUpdate', 'AutomationRuleActionFindingFieldsUpdateNote', ..., 'AutomationRuleActionFindingFieldsUpdateSeverity', 'AutomationRuleActionFindingFieldsUpdateWorkflow', 'AutomationRuleCriteria', 'AutomationRuleCriteriaAwsAccountId', 'AutomationRuleCriteriaAwsAccountName', 'AutomationRuleCriteriaCompanyName', ..., 'AutomationRuleCriteriaComplianceSecurityControlId', 'AutomationRuleCriteriaComplianceStatus', 'AutomationRuleCriteriaConfidence', 'AutomationRuleCriteriaCreatedAt', 'AutomationRuleCriteriaCreatedAtDateRange', 'AutomationRuleCriteriaCriticality', 'AutomationRuleCriteriaDescription', 'AutomationRuleCriteriaFirstObservedAt', 'AutomationRuleCriteriaFirstObservedAtDateRange', 'AutomationRuleCriteriaGeneratorId', 'AutomationRuleCriteriaId', 'AutomationRuleCriteriaLastObservedAt', 'AutomationRuleCriteriaLastObservedAtDateRange', 'AutomationRuleCriteriaNoteText', 'AutomationRuleCriteriaNoteUpdatedAt', 'AutomationRuleCriteriaNoteUpdatedAtDateRange', 'AutomationRuleCriteriaNoteUpdatedBy', 'AutomationRuleCriteriaProductArn', 'AutomationRuleCriteriaProductName', 'AutomationRuleCriteriaRecordState', 'AutomationRuleCriteriaRelatedFindingsId', 'AutomationRuleCriteriaRelatedFindingsProductArn', 'AutomationRuleCriteriaResourceApplicationArn', 'AutomationRuleCriteriaResourceApplicationName', 'AutomationRuleCriteriaResourceDetailsOther', 'AutomationRuleCriteriaResourceId', 'AutomationRuleCriteriaResourcePartition', 'AutomationRuleCriteriaResourceRegion', 'AutomationRuleCriteriaResourceTag', 'AutomationRuleCriteriaResourceType', 'AutomationRuleCriteriaSeverityLabel', 'AutomationRuleCriteriaSourceUrl', 'AutomationRuleCriteriaTitle', 'AutomationRuleCriteriaType', 'AutomationRuleCriteriaUpdatedAt', 'AutomationRuleCriteriaUpdatedAtDateRange', 'AutomationRuleCriteriaUserDefinedField', 'AutomationRuleCriteriaVerificationState', 'AutomationRuleCriteriaWorkflowStatus', 'ConfigurationPolicyConfigurationPolicy', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'InsightFilters', 'InsightFiltersAwsAccountId', 'InsightFiltersCompanyName', 'InsightFiltersComplianceStatus', 'InsightFiltersConfidence', 'InsightFiltersCreatedAt', 'InsightFiltersCreatedAtDateRange', 'InsightFiltersCriticality', 'InsightFiltersDescription', 'InsightFiltersFindingProviderFieldsConfidence', 'InsightFiltersFindingProviderFieldsCriticality', ..., ..., 'InsightFiltersFindingProviderFieldsSeverityLabel', ..., 'InsightFiltersFindingProviderFieldsType', 'InsightFiltersFirstObservedAt', 'InsightFiltersFirstObservedAtDateRange', 'InsightFiltersGeneratorId', 'InsightFiltersId', 'InsightFiltersKeyword', 'InsightFiltersLastObservedAt', 'InsightFiltersLastObservedAtDateRange', 'InsightFiltersMalwareName', 'InsightFiltersMalwarePath', 'InsightFiltersMalwareState', 'InsightFiltersMalwareType', 'InsightFiltersNetworkDestinationDomain', 'InsightFiltersNetworkDestinationIpv4', 'InsightFiltersNetworkDestinationIpv6', 'InsightFiltersNetworkDestinationPort', 'InsightFiltersNetworkDirection', 'InsightFiltersNetworkProtocol', 'InsightFiltersNetworkSourceDomain', 'InsightFiltersNetworkSourceIpv4', 'InsightFiltersNetworkSourceIpv6', 'InsightFiltersNetworkSourceMac', 'InsightFiltersNetworkSourcePort', 'InsightFiltersNoteText', 'InsightFiltersNoteUpdatedAt', 'InsightFiltersNoteUpdatedAtDateRange', 'InsightFiltersNoteUpdatedBy', 'InsightFiltersProcessLaunchedAt', 'InsightFiltersProcessLaunchedAtDateRange', 'InsightFiltersProcessName', 'InsightFiltersProcessParentPid', 'InsightFiltersProcessPath', 'InsightFiltersProcessPid', 'InsightFiltersProcessTerminatedAt', 'InsightFiltersProcessTerminatedAtDateRange', 'InsightFiltersProductArn', 'InsightFiltersProductField', 'InsightFiltersProductName', 'InsightFiltersRecommendationText', 'InsightFiltersRecordState', 'InsightFiltersRelatedFindingsId', 'InsightFiltersRelatedFindingsProductArn', ..., 'InsightFiltersResourceAwsEc2InstanceImageId', 'InsightFiltersResourceAwsEc2InstanceIpv4Address', 'InsightFiltersResourceAwsEc2InstanceIpv6Address', 'InsightFiltersResourceAwsEc2InstanceKeyName', 'InsightFiltersResourceAwsEc2InstanceLaunchedAt', ..., 'InsightFiltersResourceAwsEc2InstanceSubnetId', 'InsightFiltersResourceAwsEc2InstanceType', 'InsightFiltersResourceAwsEc2InstanceVpcId', 'InsightFiltersResourceAwsIamAccessKeyCreatedAt', ..., 'InsightFiltersResourceAwsIamAccessKeyStatus', 'InsightFiltersResourceAwsIamAccessKeyUserName', 'InsightFiltersResourceAwsS3BucketOwnerId', 'InsightFiltersResourceAwsS3BucketOwnerName', 'InsightFiltersResourceContainerImageId', 'InsightFiltersResourceContainerImageName', 'InsightFiltersResourceContainerLaunchedAt', 'InsightFiltersResourceContainerLaunchedAtDateRange', 'InsightFiltersResourceContainerName', 'InsightFiltersResourceDetailsOther', 'InsightFiltersResourceId', 'InsightFiltersResourcePartition', 'InsightFiltersResourceRegion', 'InsightFiltersResourceTag', 'InsightFiltersResourceType', 'InsightFiltersSeverityLabel', 'InsightFiltersSourceUrl', 'InsightFiltersThreatIntelIndicatorCategory', 'InsightFiltersThreatIntelIndicatorLastObservedAt', ..., 'InsightFiltersThreatIntelIndicatorSource', 'InsightFiltersThreatIntelIndicatorSourceUrl', 'InsightFiltersThreatIntelIndicatorType', 'InsightFiltersThreatIntelIndicatorValue', 'InsightFiltersTitle', 'InsightFiltersType', 'InsightFiltersUpdatedAt', 'InsightFiltersUpdatedAtDateRange', 'InsightFiltersUserDefinedValue', 'InsightFiltersVerificationState', 'InsightFiltersWorkflowStatus', 'OrganizationConfigurationOrganizationConfiguration', ...]
@pulumi.output_type
class AutomationRuleAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, finding_fields_update: Optional[outputs.AutomationRuleActionFindingFieldsUpdate] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingFieldsUpdate")
    def finding_fields_update(self) -> Optional[outputs.AutomationRuleActionFindingFieldsUpdate]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationRuleActionFindingFieldsUpdate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, confidence: Optional[_builtins.int] = ..., criticality: Optional[_builtins.int] = ..., note: Optional[outputs.AutomationRuleActionFindingFieldsUpdateNote] = ..., related_findings: Optional[Sequence[outputs.AutomationRuleActionFindingFieldsUpdateRelatedFinding]] = ..., severity: Optional[outputs.AutomationRuleActionFindingFieldsUpdateSeverity] = ..., types: Optional[Sequence[_builtins.str]] = ..., user_defined_fields: Optional[Mapping[str, _builtins.str]] = ..., verification_state: Optional[_builtins.str] = ..., workflow: Optional[outputs.AutomationRuleActionFindingFieldsUpdateWorkflow] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def confidence(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def criticality(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def note(self) -> Optional[outputs.AutomationRuleActionFindingFieldsUpdateNote]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedFindings")
    def related_findings(self) -> Optional[Sequence[outputs.AutomationRuleActionFindingFieldsUpdateRelatedFinding]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[outputs.AutomationRuleActionFindingFieldsUpdateSeverity]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationState")
    def verification_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def workflow(self) -> Optional[outputs.AutomationRuleActionFindingFieldsUpdateWorkflow]:
        
        ...
    


@pulumi.output_type
class AutomationRuleActionFindingFieldsUpdateNote(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text: _builtins.str, updated_by: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AutomationRuleActionFindingFieldsUpdateRelatedFinding(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, id: _builtins.str, product_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productArn")
    def product_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AutomationRuleActionFindingFieldsUpdateSeverity(dict):
    def __init__(__self__, *, label: Optional[_builtins.str] = ..., product: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def product(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AutomationRuleActionFindingFieldsUpdateWorkflow(dict):
    def __init__(__self__, *, status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteria(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_account_ids: Optional[Sequence[outputs.AutomationRuleCriteriaAwsAccountId]] = ..., aws_account_names: Optional[Sequence[outputs.AutomationRuleCriteriaAwsAccountName]] = ..., company_names: Optional[Sequence[outputs.AutomationRuleCriteriaCompanyName]] = ..., compliance_associated_standards_ids: Optional[Sequence[outputs.AutomationRuleCriteriaComplianceAssociatedStandardsId]] = ..., compliance_security_control_ids: Optional[Sequence[outputs.AutomationRuleCriteriaComplianceSecurityControlId]] = ..., compliance_statuses: Optional[Sequence[outputs.AutomationRuleCriteriaComplianceStatus]] = ..., confidences: Optional[Sequence[outputs.AutomationRuleCriteriaConfidence]] = ..., created_ats: Optional[Sequence[outputs.AutomationRuleCriteriaCreatedAt]] = ..., criticalities: Optional[Sequence[outputs.AutomationRuleCriteriaCriticality]] = ..., descriptions: Optional[Sequence[outputs.AutomationRuleCriteriaDescription]] = ..., first_observed_ats: Optional[Sequence[outputs.AutomationRuleCriteriaFirstObservedAt]] = ..., generator_ids: Optional[Sequence[outputs.AutomationRuleCriteriaGeneratorId]] = ..., ids: Optional[Sequence[outputs.AutomationRuleCriteriaId]] = ..., last_observed_ats: Optional[Sequence[outputs.AutomationRuleCriteriaLastObservedAt]] = ..., note_texts: Optional[Sequence[outputs.AutomationRuleCriteriaNoteText]] = ..., note_updated_ats: Optional[Sequence[outputs.AutomationRuleCriteriaNoteUpdatedAt]] = ..., note_updated_bies: Optional[Sequence[outputs.AutomationRuleCriteriaNoteUpdatedBy]] = ..., product_arns: Optional[Sequence[outputs.AutomationRuleCriteriaProductArn]] = ..., product_names: Optional[Sequence[outputs.AutomationRuleCriteriaProductName]] = ..., record_states: Optional[Sequence[outputs.AutomationRuleCriteriaRecordState]] = ..., related_findings_ids: Optional[Sequence[outputs.AutomationRuleCriteriaRelatedFindingsId]] = ..., related_findings_product_arns: Optional[Sequence[outputs.AutomationRuleCriteriaRelatedFindingsProductArn]] = ..., resource_application_arns: Optional[Sequence[outputs.AutomationRuleCriteriaResourceApplicationArn]] = ..., resource_application_names: Optional[Sequence[outputs.AutomationRuleCriteriaResourceApplicationName]] = ..., resource_details_others: Optional[Sequence[outputs.AutomationRuleCriteriaResourceDetailsOther]] = ..., resource_ids: Optional[Sequence[outputs.AutomationRuleCriteriaResourceId]] = ..., resource_partitions: Optional[Sequence[outputs.AutomationRuleCriteriaResourcePartition]] = ..., resource_regions: Optional[Sequence[outputs.AutomationRuleCriteriaResourceRegion]] = ..., resource_tags: Optional[Sequence[outputs.AutomationRuleCriteriaResourceTag]] = ..., resource_types: Optional[Sequence[outputs.AutomationRuleCriteriaResourceType]] = ..., severity_labels: Optional[Sequence[outputs.AutomationRuleCriteriaSeverityLabel]] = ..., source_urls: Optional[Sequence[outputs.AutomationRuleCriteriaSourceUrl]] = ..., titles: Optional[Sequence[outputs.AutomationRuleCriteriaTitle]] = ..., types: Optional[Sequence[outputs.AutomationRuleCriteriaType]] = ..., updated_ats: Optional[Sequence[outputs.AutomationRuleCriteriaUpdatedAt]] = ..., user_defined_fields: Optional[Sequence[outputs.AutomationRuleCriteriaUserDefinedField]] = ..., verification_states: Optional[Sequence[outputs.AutomationRuleCriteriaVerificationState]] = ..., workflow_statuses: Optional[Sequence[outputs.AutomationRuleCriteriaWorkflowStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountIds")
    def aws_account_ids(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaAwsAccountId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountNames")
    def aws_account_names(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaAwsAccountName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="companyNames")
    def company_names(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaCompanyName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceAssociatedStandardsIds")
    def compliance_associated_standards_ids(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaComplianceAssociatedStandardsId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceSecurityControlIds")
    def compliance_security_control_ids(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaComplianceSecurityControlId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceStatuses")
    def compliance_statuses(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaComplianceStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def confidences(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaConfidence]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAts")
    def created_ats(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaCreatedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def criticalities(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaCriticality]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def descriptions(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaDescription]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstObservedAts")
    def first_observed_ats(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaFirstObservedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatorIds")
    def generator_ids(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaGeneratorId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastObservedAts")
    def last_observed_ats(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaLastObservedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noteTexts")
    def note_texts(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaNoteText]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noteUpdatedAts")
    def note_updated_ats(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaNoteUpdatedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noteUpdatedBies")
    def note_updated_bies(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaNoteUpdatedBy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productArns")
    def product_arns(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaProductArn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productNames")
    def product_names(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaProductName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordStates")
    def record_states(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaRecordState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedFindingsIds")
    def related_findings_ids(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaRelatedFindingsId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedFindingsProductArns")
    def related_findings_product_arns(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaRelatedFindingsProductArn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceApplicationArns")
    def resource_application_arns(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaResourceApplicationArn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceApplicationNames")
    def resource_application_names(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaResourceApplicationName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceDetailsOthers")
    def resource_details_others(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaResourceDetailsOther]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIds")
    def resource_ids(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaResourceId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePartitions")
    def resource_partitions(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaResourcePartition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRegions")
    def resource_regions(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaResourceRegion]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaResourceTag]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaResourceType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="severityLabels")
    def severity_labels(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaSeverityLabel]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceUrls")
    def source_urls(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaSourceUrl]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def titles(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaTitle]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAts")
    def updated_ats(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaUpdatedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedFields")
    def user_defined_fields(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaUserDefinedField]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationStates")
    def verification_states(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaVerificationState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowStatuses")
    def workflow_statuses(self) -> Optional[Sequence[outputs.AutomationRuleCriteriaWorkflowStatus]]:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaAwsAccountId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaAwsAccountName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaCompanyName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaComplianceAssociatedStandardsId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaComplianceSecurityControlId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaComplianceStatus(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaConfidence(dict):
    def __init__(__self__, *, eq: Optional[_builtins.float] = ..., gt: Optional[_builtins.float] = ..., gte: Optional[_builtins.float] = ..., lt: Optional[_builtins.float] = ..., lte: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gt(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lt(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaCreatedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.AutomationRuleCriteriaCreatedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.AutomationRuleCriteriaCreatedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaCreatedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaCriticality(dict):
    def __init__(__self__, *, eq: Optional[_builtins.float] = ..., gt: Optional[_builtins.float] = ..., gte: Optional[_builtins.float] = ..., lt: Optional[_builtins.float] = ..., lte: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gt(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lt(self) -> Optional[_builtins.float]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaDescription(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaFirstObservedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.AutomationRuleCriteriaFirstObservedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.AutomationRuleCriteriaFirstObservedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaFirstObservedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaGeneratorId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaLastObservedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.AutomationRuleCriteriaLastObservedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.AutomationRuleCriteriaLastObservedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaLastObservedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaNoteText(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaNoteUpdatedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.AutomationRuleCriteriaNoteUpdatedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.AutomationRuleCriteriaNoteUpdatedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaNoteUpdatedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaNoteUpdatedBy(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaProductArn(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaProductName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaRecordState(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaRelatedFindingsId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaRelatedFindingsProductArn(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaResourceApplicationArn(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaResourceApplicationName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaResourceDetailsOther(dict):
    def __init__(__self__, *, comparison: _builtins.str, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaResourceId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaResourcePartition(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaResourceRegion(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaResourceTag(dict):
    def __init__(__self__, *, comparison: _builtins.str, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaResourceType(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaSeverityLabel(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaSourceUrl(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaTitle(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaType(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaUpdatedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.AutomationRuleCriteriaUpdatedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.AutomationRuleCriteriaUpdatedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaUpdatedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaUserDefinedField(dict):
    def __init__(__self__, *, comparison: _builtins.str, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaVerificationState(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class AutomationRuleCriteriaWorkflowStatus(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_enabled: _builtins.bool, enabled_standard_arns: Optional[Sequence[_builtins.str]] = ..., security_controls_configuration: Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceEnabled")
    def service_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledStandardArns")
    def enabled_standard_arns(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityControlsConfiguration")
    def security_controls_configuration(self) -> Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfiguration]:
        
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled_control_identifiers: Optional[Sequence[_builtins.str]] = ..., enabled_control_identifiers: Optional[Sequence[_builtins.str]] = ..., security_control_custom_parameters: Optional[Sequence[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disabledControlIdentifiers")
    def disabled_control_identifiers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enabledControlIdentifiers")
    def enabled_control_identifiers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityControlCustomParameters")
    def security_control_custom_parameters(self) -> Optional[Sequence[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameter]]:
        
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, parameters: Sequence[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameter], security_control_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Sequence[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameter]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityControlId")
    def security_control_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, value_type: _builtins.str, bool: Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterBool] = ..., double: Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterDouble] = ..., enum: Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnum] = ..., enum_list: Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumList] = ..., int: Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterInt] = ..., int_list: Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntList] = ..., string: Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterString] = ..., string_list: Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueType")
    def value_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bool(self) -> Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterBool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def double(self) -> Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterDouble]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enum(self) -> Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnum]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enumList")
    def enum_list(self) -> Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumList]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def int(self) -> Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterInt]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intList")
    def int_list(self) -> Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntList]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def string(self) -> Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stringList")
    def string_list(self) -> Optional[outputs.ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringList]:
        
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterBool(dict):
    def __init__(__self__, *, value: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterDouble(dict):
    def __init__(__self__, *, value: _builtins.float) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.float:
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnum(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterEnumList(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterInt(dict):
    def __init__(__self__, *, value: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterIntList(dict):
    def __init__(__self__, *, values: Sequence[_builtins.int]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.int]:
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterString(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class ConfigurationPolicyConfigurationPolicySecurityControlsConfigurationSecurityControlCustomParameterParameterStringList(dict):
    def __init__(__self__, *, values: Sequence[_builtins.str]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]:
        ...
    


@pulumi.output_type
class InsightFilters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_account_ids: Optional[Sequence[outputs.InsightFiltersAwsAccountId]] = ..., company_names: Optional[Sequence[outputs.InsightFiltersCompanyName]] = ..., compliance_statuses: Optional[Sequence[outputs.InsightFiltersComplianceStatus]] = ..., confidences: Optional[Sequence[outputs.InsightFiltersConfidence]] = ..., created_ats: Optional[Sequence[outputs.InsightFiltersCreatedAt]] = ..., criticalities: Optional[Sequence[outputs.InsightFiltersCriticality]] = ..., descriptions: Optional[Sequence[outputs.InsightFiltersDescription]] = ..., finding_provider_fields_confidences: Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsConfidence]] = ..., finding_provider_fields_criticalities: Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsCriticality]] = ..., finding_provider_fields_related_findings_ids: Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsRelatedFindingsId]] = ..., finding_provider_fields_related_findings_product_arns: Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsRelatedFindingsProductArn]] = ..., finding_provider_fields_severity_labels: Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsSeverityLabel]] = ..., finding_provider_fields_severity_originals: Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsSeverityOriginal]] = ..., finding_provider_fields_types: Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsType]] = ..., first_observed_ats: Optional[Sequence[outputs.InsightFiltersFirstObservedAt]] = ..., generator_ids: Optional[Sequence[outputs.InsightFiltersGeneratorId]] = ..., ids: Optional[Sequence[outputs.InsightFiltersId]] = ..., keywords: Optional[Sequence[outputs.InsightFiltersKeyword]] = ..., last_observed_ats: Optional[Sequence[outputs.InsightFiltersLastObservedAt]] = ..., malware_names: Optional[Sequence[outputs.InsightFiltersMalwareName]] = ..., malware_paths: Optional[Sequence[outputs.InsightFiltersMalwarePath]] = ..., malware_states: Optional[Sequence[outputs.InsightFiltersMalwareState]] = ..., malware_types: Optional[Sequence[outputs.InsightFiltersMalwareType]] = ..., network_destination_domains: Optional[Sequence[outputs.InsightFiltersNetworkDestinationDomain]] = ..., network_destination_ipv4s: Optional[Sequence[outputs.InsightFiltersNetworkDestinationIpv4]] = ..., network_destination_ipv6s: Optional[Sequence[outputs.InsightFiltersNetworkDestinationIpv6]] = ..., network_destination_ports: Optional[Sequence[outputs.InsightFiltersNetworkDestinationPort]] = ..., network_directions: Optional[Sequence[outputs.InsightFiltersNetworkDirection]] = ..., network_protocols: Optional[Sequence[outputs.InsightFiltersNetworkProtocol]] = ..., network_source_domains: Optional[Sequence[outputs.InsightFiltersNetworkSourceDomain]] = ..., network_source_ipv4s: Optional[Sequence[outputs.InsightFiltersNetworkSourceIpv4]] = ..., network_source_ipv6s: Optional[Sequence[outputs.InsightFiltersNetworkSourceIpv6]] = ..., network_source_macs: Optional[Sequence[outputs.InsightFiltersNetworkSourceMac]] = ..., network_source_ports: Optional[Sequence[outputs.InsightFiltersNetworkSourcePort]] = ..., note_texts: Optional[Sequence[outputs.InsightFiltersNoteText]] = ..., note_updated_ats: Optional[Sequence[outputs.InsightFiltersNoteUpdatedAt]] = ..., note_updated_bies: Optional[Sequence[outputs.InsightFiltersNoteUpdatedBy]] = ..., process_launched_ats: Optional[Sequence[outputs.InsightFiltersProcessLaunchedAt]] = ..., process_names: Optional[Sequence[outputs.InsightFiltersProcessName]] = ..., process_parent_pids: Optional[Sequence[outputs.InsightFiltersProcessParentPid]] = ..., process_paths: Optional[Sequence[outputs.InsightFiltersProcessPath]] = ..., process_pids: Optional[Sequence[outputs.InsightFiltersProcessPid]] = ..., process_terminated_ats: Optional[Sequence[outputs.InsightFiltersProcessTerminatedAt]] = ..., product_arns: Optional[Sequence[outputs.InsightFiltersProductArn]] = ..., product_fields: Optional[Sequence[outputs.InsightFiltersProductField]] = ..., product_names: Optional[Sequence[outputs.InsightFiltersProductName]] = ..., recommendation_texts: Optional[Sequence[outputs.InsightFiltersRecommendationText]] = ..., record_states: Optional[Sequence[outputs.InsightFiltersRecordState]] = ..., related_findings_ids: Optional[Sequence[outputs.InsightFiltersRelatedFindingsId]] = ..., related_findings_product_arns: Optional[Sequence[outputs.InsightFiltersRelatedFindingsProductArn]] = ..., resource_aws_ec2_instance_iam_instance_profile_arns: Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceIamInstanceProfileArn]] = ..., resource_aws_ec2_instance_image_ids: Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceImageId]] = ..., resource_aws_ec2_instance_ipv4_addresses: Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceIpv4Address]] = ..., resource_aws_ec2_instance_ipv6_addresses: Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceIpv6Address]] = ..., resource_aws_ec2_instance_key_names: Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceKeyName]] = ..., resource_aws_ec2_instance_launched_ats: Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceLaunchedAt]] = ..., resource_aws_ec2_instance_subnet_ids: Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceSubnetId]] = ..., resource_aws_ec2_instance_types: Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceType]] = ..., resource_aws_ec2_instance_vpc_ids: Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceVpcId]] = ..., resource_aws_iam_access_key_created_ats: Optional[Sequence[outputs.InsightFiltersResourceAwsIamAccessKeyCreatedAt]] = ..., resource_aws_iam_access_key_statuses: Optional[Sequence[outputs.InsightFiltersResourceAwsIamAccessKeyStatus]] = ..., resource_aws_iam_access_key_user_names: Optional[Sequence[outputs.InsightFiltersResourceAwsIamAccessKeyUserName]] = ..., resource_aws_s3_bucket_owner_ids: Optional[Sequence[outputs.InsightFiltersResourceAwsS3BucketOwnerId]] = ..., resource_aws_s3_bucket_owner_names: Optional[Sequence[outputs.InsightFiltersResourceAwsS3BucketOwnerName]] = ..., resource_container_image_ids: Optional[Sequence[outputs.InsightFiltersResourceContainerImageId]] = ..., resource_container_image_names: Optional[Sequence[outputs.InsightFiltersResourceContainerImageName]] = ..., resource_container_launched_ats: Optional[Sequence[outputs.InsightFiltersResourceContainerLaunchedAt]] = ..., resource_container_names: Optional[Sequence[outputs.InsightFiltersResourceContainerName]] = ..., resource_details_others: Optional[Sequence[outputs.InsightFiltersResourceDetailsOther]] = ..., resource_ids: Optional[Sequence[outputs.InsightFiltersResourceId]] = ..., resource_partitions: Optional[Sequence[outputs.InsightFiltersResourcePartition]] = ..., resource_regions: Optional[Sequence[outputs.InsightFiltersResourceRegion]] = ..., resource_tags: Optional[Sequence[outputs.InsightFiltersResourceTag]] = ..., resource_types: Optional[Sequence[outputs.InsightFiltersResourceType]] = ..., severity_labels: Optional[Sequence[outputs.InsightFiltersSeverityLabel]] = ..., source_urls: Optional[Sequence[outputs.InsightFiltersSourceUrl]] = ..., threat_intel_indicator_categories: Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorCategory]] = ..., threat_intel_indicator_last_observed_ats: Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorLastObservedAt]] = ..., threat_intel_indicator_source_urls: Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorSourceUrl]] = ..., threat_intel_indicator_sources: Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorSource]] = ..., threat_intel_indicator_types: Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorType]] = ..., threat_intel_indicator_values: Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorValue]] = ..., titles: Optional[Sequence[outputs.InsightFiltersTitle]] = ..., types: Optional[Sequence[outputs.InsightFiltersType]] = ..., updated_ats: Optional[Sequence[outputs.InsightFiltersUpdatedAt]] = ..., user_defined_values: Optional[Sequence[outputs.InsightFiltersUserDefinedValue]] = ..., verification_states: Optional[Sequence[outputs.InsightFiltersVerificationState]] = ..., workflow_statuses: Optional[Sequence[outputs.InsightFiltersWorkflowStatus]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountIds")
    def aws_account_ids(self) -> Optional[Sequence[outputs.InsightFiltersAwsAccountId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="companyNames")
    def company_names(self) -> Optional[Sequence[outputs.InsightFiltersCompanyName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="complianceStatuses")
    def compliance_statuses(self) -> Optional[Sequence[outputs.InsightFiltersComplianceStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def confidences(self) -> Optional[Sequence[outputs.InsightFiltersConfidence]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdAts")
    def created_ats(self) -> Optional[Sequence[outputs.InsightFiltersCreatedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def criticalities(self) -> Optional[Sequence[outputs.InsightFiltersCriticality]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def descriptions(self) -> Optional[Sequence[outputs.InsightFiltersDescription]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsConfidences")
    def finding_provider_fields_confidences(self) -> Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsConfidence]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsCriticalities")
    def finding_provider_fields_criticalities(self) -> Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsCriticality]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsRelatedFindingsIds")
    def finding_provider_fields_related_findings_ids(self) -> Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsRelatedFindingsId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsRelatedFindingsProductArns")
    def finding_provider_fields_related_findings_product_arns(self) -> Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsRelatedFindingsProductArn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsSeverityLabels")
    def finding_provider_fields_severity_labels(self) -> Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsSeverityLabel]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsSeverityOriginals")
    def finding_provider_fields_severity_originals(self) -> Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsSeverityOriginal]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="findingProviderFieldsTypes")
    def finding_provider_fields_types(self) -> Optional[Sequence[outputs.InsightFiltersFindingProviderFieldsType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstObservedAts")
    def first_observed_ats(self) -> Optional[Sequence[outputs.InsightFiltersFirstObservedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatorIds")
    def generator_ids(self) -> Optional[Sequence[outputs.InsightFiltersGeneratorId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ids(self) -> Optional[Sequence[outputs.InsightFiltersId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keywords(self) -> Optional[Sequence[outputs.InsightFiltersKeyword]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastObservedAts")
    def last_observed_ats(self) -> Optional[Sequence[outputs.InsightFiltersLastObservedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="malwareNames")
    def malware_names(self) -> Optional[Sequence[outputs.InsightFiltersMalwareName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="malwarePaths")
    def malware_paths(self) -> Optional[Sequence[outputs.InsightFiltersMalwarePath]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="malwareStates")
    def malware_states(self) -> Optional[Sequence[outputs.InsightFiltersMalwareState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="malwareTypes")
    def malware_types(self) -> Optional[Sequence[outputs.InsightFiltersMalwareType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkDestinationDomains")
    def network_destination_domains(self) -> Optional[Sequence[outputs.InsightFiltersNetworkDestinationDomain]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkDestinationIpv4s")
    def network_destination_ipv4s(self) -> Optional[Sequence[outputs.InsightFiltersNetworkDestinationIpv4]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkDestinationIpv6s")
    def network_destination_ipv6s(self) -> Optional[Sequence[outputs.InsightFiltersNetworkDestinationIpv6]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkDestinationPorts")
    def network_destination_ports(self) -> Optional[Sequence[outputs.InsightFiltersNetworkDestinationPort]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkDirections")
    def network_directions(self) -> Optional[Sequence[outputs.InsightFiltersNetworkDirection]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkProtocols")
    def network_protocols(self) -> Optional[Sequence[outputs.InsightFiltersNetworkProtocol]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSourceDomains")
    def network_source_domains(self) -> Optional[Sequence[outputs.InsightFiltersNetworkSourceDomain]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSourceIpv4s")
    def network_source_ipv4s(self) -> Optional[Sequence[outputs.InsightFiltersNetworkSourceIpv4]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSourceIpv6s")
    def network_source_ipv6s(self) -> Optional[Sequence[outputs.InsightFiltersNetworkSourceIpv6]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSourceMacs")
    def network_source_macs(self) -> Optional[Sequence[outputs.InsightFiltersNetworkSourceMac]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSourcePorts")
    def network_source_ports(self) -> Optional[Sequence[outputs.InsightFiltersNetworkSourcePort]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noteTexts")
    def note_texts(self) -> Optional[Sequence[outputs.InsightFiltersNoteText]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noteUpdatedAts")
    def note_updated_ats(self) -> Optional[Sequence[outputs.InsightFiltersNoteUpdatedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noteUpdatedBies")
    def note_updated_bies(self) -> Optional[Sequence[outputs.InsightFiltersNoteUpdatedBy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processLaunchedAts")
    def process_launched_ats(self) -> Optional[Sequence[outputs.InsightFiltersProcessLaunchedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processNames")
    def process_names(self) -> Optional[Sequence[outputs.InsightFiltersProcessName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processParentPids")
    def process_parent_pids(self) -> Optional[Sequence[outputs.InsightFiltersProcessParentPid]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processPaths")
    def process_paths(self) -> Optional[Sequence[outputs.InsightFiltersProcessPath]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processPids")
    def process_pids(self) -> Optional[Sequence[outputs.InsightFiltersProcessPid]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processTerminatedAts")
    def process_terminated_ats(self) -> Optional[Sequence[outputs.InsightFiltersProcessTerminatedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productArns")
    def product_arns(self) -> Optional[Sequence[outputs.InsightFiltersProductArn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productFields")
    def product_fields(self) -> Optional[Sequence[outputs.InsightFiltersProductField]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productNames")
    def product_names(self) -> Optional[Sequence[outputs.InsightFiltersProductName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recommendationTexts")
    def recommendation_texts(self) -> Optional[Sequence[outputs.InsightFiltersRecommendationText]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recordStates")
    def record_states(self) -> Optional[Sequence[outputs.InsightFiltersRecordState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedFindingsIds")
    def related_findings_ids(self) -> Optional[Sequence[outputs.InsightFiltersRelatedFindingsId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedFindingsProductArns")
    def related_findings_product_arns(self) -> Optional[Sequence[outputs.InsightFiltersRelatedFindingsProductArn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceIamInstanceProfileArns")
    def resource_aws_ec2_instance_iam_instance_profile_arns(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceIamInstanceProfileArn]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceImageIds")
    def resource_aws_ec2_instance_image_ids(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceImageId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceIpv4Addresses")
    def resource_aws_ec2_instance_ipv4_addresses(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceIpv4Address]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceIpv6Addresses")
    def resource_aws_ec2_instance_ipv6_addresses(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceIpv6Address]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceKeyNames")
    def resource_aws_ec2_instance_key_names(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceKeyName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceLaunchedAts")
    def resource_aws_ec2_instance_launched_ats(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceLaunchedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceSubnetIds")
    def resource_aws_ec2_instance_subnet_ids(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceSubnetId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceTypes")
    def resource_aws_ec2_instance_types(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsEc2InstanceVpcIds")
    def resource_aws_ec2_instance_vpc_ids(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsEc2InstanceVpcId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsIamAccessKeyCreatedAts")
    def resource_aws_iam_access_key_created_ats(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsIamAccessKeyCreatedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsIamAccessKeyStatuses")
    def resource_aws_iam_access_key_statuses(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsIamAccessKeyStatus]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsIamAccessKeyUserNames")
    def resource_aws_iam_access_key_user_names(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsIamAccessKeyUserName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsS3BucketOwnerIds")
    def resource_aws_s3_bucket_owner_ids(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsS3BucketOwnerId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceAwsS3BucketOwnerNames")
    def resource_aws_s3_bucket_owner_names(self) -> Optional[Sequence[outputs.InsightFiltersResourceAwsS3BucketOwnerName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceContainerImageIds")
    def resource_container_image_ids(self) -> Optional[Sequence[outputs.InsightFiltersResourceContainerImageId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceContainerImageNames")
    def resource_container_image_names(self) -> Optional[Sequence[outputs.InsightFiltersResourceContainerImageName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceContainerLaunchedAts")
    def resource_container_launched_ats(self) -> Optional[Sequence[outputs.InsightFiltersResourceContainerLaunchedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceContainerNames")
    def resource_container_names(self) -> Optional[Sequence[outputs.InsightFiltersResourceContainerName]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceDetailsOthers")
    def resource_details_others(self) -> Optional[Sequence[outputs.InsightFiltersResourceDetailsOther]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceIds")
    def resource_ids(self) -> Optional[Sequence[outputs.InsightFiltersResourceId]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePartitions")
    def resource_partitions(self) -> Optional[Sequence[outputs.InsightFiltersResourcePartition]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceRegions")
    def resource_regions(self) -> Optional[Sequence[outputs.InsightFiltersResourceRegion]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> Optional[Sequence[outputs.InsightFiltersResourceTag]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[Sequence[outputs.InsightFiltersResourceType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="severityLabels")
    def severity_labels(self) -> Optional[Sequence[outputs.InsightFiltersSeverityLabel]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceUrls")
    def source_urls(self) -> Optional[Sequence[outputs.InsightFiltersSourceUrl]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorCategories")
    def threat_intel_indicator_categories(self) -> Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorCategory]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorLastObservedAts")
    def threat_intel_indicator_last_observed_ats(self) -> Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorLastObservedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorSourceUrls")
    def threat_intel_indicator_source_urls(self) -> Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorSourceUrl]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorSources")
    def threat_intel_indicator_sources(self) -> Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorTypes")
    def threat_intel_indicator_types(self) -> Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="threatIntelIndicatorValues")
    def threat_intel_indicator_values(self) -> Optional[Sequence[outputs.InsightFiltersThreatIntelIndicatorValue]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def titles(self) -> Optional[Sequence[outputs.InsightFiltersTitle]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def types(self) -> Optional[Sequence[outputs.InsightFiltersType]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAts")
    def updated_ats(self) -> Optional[Sequence[outputs.InsightFiltersUpdatedAt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userDefinedValues")
    def user_defined_values(self) -> Optional[Sequence[outputs.InsightFiltersUserDefinedValue]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verificationStates")
    def verification_states(self) -> Optional[Sequence[outputs.InsightFiltersVerificationState]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowStatuses")
    def workflow_statuses(self) -> Optional[Sequence[outputs.InsightFiltersWorkflowStatus]]:
        
        ...
    


@pulumi.output_type
class InsightFiltersAwsAccountId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersCompanyName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersComplianceStatus(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersConfidence(dict):
    def __init__(__self__, *, eq: Optional[_builtins.str] = ..., gte: Optional[_builtins.str] = ..., lte: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersCreatedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersCreatedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersCreatedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersCreatedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersCriticality(dict):
    def __init__(__self__, *, eq: Optional[_builtins.str] = ..., gte: Optional[_builtins.str] = ..., lte: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersDescription(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersFindingProviderFieldsConfidence(dict):
    def __init__(__self__, *, eq: Optional[_builtins.str] = ..., gte: Optional[_builtins.str] = ..., lte: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersFindingProviderFieldsCriticality(dict):
    def __init__(__self__, *, eq: Optional[_builtins.str] = ..., gte: Optional[_builtins.str] = ..., lte: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersFindingProviderFieldsRelatedFindingsId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersFindingProviderFieldsRelatedFindingsProductArn(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersFindingProviderFieldsSeverityLabel(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersFindingProviderFieldsSeverityOriginal(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersFindingProviderFieldsType(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersFirstObservedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersFirstObservedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersFirstObservedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersFirstObservedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersGeneratorId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersKeyword(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InsightFiltersLastObservedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersLastObservedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersLastObservedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersLastObservedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersMalwareName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersMalwarePath(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersMalwareState(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersMalwareType(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersNetworkDestinationDomain(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersNetworkDestinationIpv4(dict):
    def __init__(__self__, *, cidr: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InsightFiltersNetworkDestinationIpv6(dict):
    def __init__(__self__, *, cidr: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InsightFiltersNetworkDestinationPort(dict):
    def __init__(__self__, *, eq: Optional[_builtins.str] = ..., gte: Optional[_builtins.str] = ..., lte: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersNetworkDirection(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersNetworkProtocol(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersNetworkSourceDomain(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersNetworkSourceIpv4(dict):
    def __init__(__self__, *, cidr: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InsightFiltersNetworkSourceIpv6(dict):
    def __init__(__self__, *, cidr: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InsightFiltersNetworkSourceMac(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersNetworkSourcePort(dict):
    def __init__(__self__, *, eq: Optional[_builtins.str] = ..., gte: Optional[_builtins.str] = ..., lte: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersNoteText(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersNoteUpdatedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersNoteUpdatedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersNoteUpdatedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersNoteUpdatedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersNoteUpdatedBy(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersProcessLaunchedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersProcessLaunchedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersProcessLaunchedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersProcessLaunchedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersProcessName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersProcessParentPid(dict):
    def __init__(__self__, *, eq: Optional[_builtins.str] = ..., gte: Optional[_builtins.str] = ..., lte: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersProcessPath(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersProcessPid(dict):
    def __init__(__self__, *, eq: Optional[_builtins.str] = ..., gte: Optional[_builtins.str] = ..., lte: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def eq(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gte(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def lte(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersProcessTerminatedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersProcessTerminatedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersProcessTerminatedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersProcessTerminatedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersProductArn(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersProductField(dict):
    def __init__(__self__, *, comparison: _builtins.str, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersProductName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersRecommendationText(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersRecordState(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersRelatedFindingsId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersRelatedFindingsProductArn(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceIamInstanceProfileArn(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceImageId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceIpv4Address(dict):
    def __init__(__self__, *, cidr: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceIpv6Address(dict):
    def __init__(__self__, *, cidr: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cidr(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceKeyName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceLaunchedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersResourceAwsEc2InstanceLaunchedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersResourceAwsEc2InstanceLaunchedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceLaunchedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceSubnetId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceType(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsEc2InstanceVpcId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsIamAccessKeyCreatedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersResourceAwsIamAccessKeyCreatedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersResourceAwsIamAccessKeyCreatedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsIamAccessKeyCreatedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsIamAccessKeyStatus(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsIamAccessKeyUserName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsS3BucketOwnerId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceAwsS3BucketOwnerName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceContainerImageId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceContainerImageName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceContainerLaunchedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersResourceContainerLaunchedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersResourceContainerLaunchedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersResourceContainerLaunchedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersResourceContainerName(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceDetailsOther(dict):
    def __init__(__self__, *, comparison: _builtins.str, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceId(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourcePartition(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceRegion(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceTag(dict):
    def __init__(__self__, *, comparison: _builtins.str, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersResourceType(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersSeverityLabel(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersSourceUrl(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersThreatIntelIndicatorCategory(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersThreatIntelIndicatorLastObservedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersThreatIntelIndicatorLastObservedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersThreatIntelIndicatorLastObservedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersThreatIntelIndicatorLastObservedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersThreatIntelIndicatorSource(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersThreatIntelIndicatorSourceUrl(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersThreatIntelIndicatorType(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersThreatIntelIndicatorValue(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersTitle(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersType(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersUpdatedAt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, date_range: Optional[outputs.InsightFiltersUpdatedAtDateRange] = ..., end: Optional[_builtins.str] = ..., start: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> Optional[outputs.InsightFiltersUpdatedAtDateRange]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class InsightFiltersUpdatedAtDateRange(dict):
    def __init__(__self__, *, unit: _builtins.str, value: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def unit(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class InsightFiltersUserDefinedValue(dict):
    def __init__(__self__, *, comparison: _builtins.str, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersVerificationState(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class InsightFiltersWorkflowStatus(dict):
    def __init__(__self__, *, comparison: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class OrganizationConfigurationOrganizationConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, configuration_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationType")
    def configuration_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetStandardsControlAssociationsStandardsControlAssociationResult(dict):
    def __init__(__self__, *, association_status: _builtins.str, related_requirements: Sequence[_builtins.str], security_control_arn: _builtins.str, security_control_id: _builtins.str, standards_arn: _builtins.str, standards_control_description: _builtins.str, standards_control_title: _builtins.str, updated_at: _builtins.str, updated_reason: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationStatus")
    def association_status(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relatedRequirements")
    def related_requirements(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityControlArn")
    def security_control_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityControlId")
    def security_control_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardsArn")
    def standards_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardsControlDescription")
    def standards_control_description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="standardsControlTitle")
    def standards_control_title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedReason")
    def updated_reason(self) -> _builtins.str:
        
        ...
    


