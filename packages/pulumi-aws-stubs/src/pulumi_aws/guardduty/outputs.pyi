import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DetectorDatasources",
    "DetectorDatasourcesKubernetes",
    "DetectorDatasourcesKubernetesAuditLogs",
    "DetectorDatasourcesMalwareProtection",
    ...,
    ...,
    "DetectorDatasourcesS3Logs",
    "DetectorFeatureAdditionalConfiguration",
    "FilterFindingCriteria",
    "FilterFindingCriteriaCriterion",
    "MalwareProtectionPlanAction",
    "MalwareProtectionPlanActionTagging",
    "MalwareProtectionPlanProtectedResource",
    "MalwareProtectionPlanProtectedResourceS3Bucket",
    "MemberDetectorFeatureAdditionalConfiguration",
    "OrganizationConfigurationDatasources",
    "OrganizationConfigurationDatasourcesKubernetes",
    ...,
    ...,
    ...,
    ...,
    "OrganizationConfigurationDatasourcesS3Logs",
    ...,
    "GetDetectorFeatureResult",
    "GetDetectorFeatureAdditionalConfigurationResult",
]

@pulumi.output_type
class DetectorDatasources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kubernetes: Optional[outputs.DetectorDatasourcesKubernetes] = ...,
        malware_protection: Optional[
            outputs.DetectorDatasourcesMalwareProtection
        ] = ...,
        s3_logs: Optional[outputs.DetectorDatasourcesS3Logs] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kubernetes(self) -> Optional[outputs.DetectorDatasourcesKubernetes]: ...
    @_builtins.property
    @pulumi.getter(name="malwareProtection")
    def malware_protection(
        self,
    ) -> Optional[outputs.DetectorDatasourcesMalwareProtection]: ...
    @_builtins.property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> Optional[outputs.DetectorDatasourcesS3Logs]: ...

@pulumi.output_type
class DetectorDatasourcesKubernetes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, audit_logs: outputs.DetectorDatasourcesKubernetesAuditLogs
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogs")
    def audit_logs(self) -> outputs.DetectorDatasourcesKubernetesAuditLogs: ...

@pulumi.output_type
class DetectorDatasourcesKubernetesAuditLogs(dict):
    def __init__(__self__, *, enable: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> _builtins.bool: ...

@pulumi.output_type
class DetectorDatasourcesMalwareProtection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        scan_ec2_instance_with_findings: outputs.DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scanEc2InstanceWithFindings")
    def scan_ec2_instance_with_findings(
        self,
    ) -> outputs.DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings: ...

@pulumi.output_type
class DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ebs_volumes: outputs.DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsVolumes")
    def ebs_volumes(
        self,
    ) -> outputs.DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes: ...

@pulumi.output_type
class DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes(dict):
    def __init__(__self__, *, enable: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> _builtins.bool: ...

@pulumi.output_type
class DetectorDatasourcesS3Logs(dict):
    def __init__(__self__, *, enable: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> _builtins.bool: ...

@pulumi.output_type
class DetectorFeatureAdditionalConfiguration(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFindingCriteria(dict):
    def __init__(
        __self__, *, criterions: Sequence[outputs.FilterFindingCriteriaCriterion]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def criterions(self) -> Sequence[outputs.FilterFindingCriteriaCriterion]: ...

@pulumi.output_type
class FilterFindingCriteriaCriterion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field: _builtins.str,
        equals: Optional[Sequence[_builtins.str]] = ...,
        greater_than: Optional[_builtins.str] = ...,
        greater_than_or_equal: Optional[_builtins.str] = ...,
        less_than: Optional[_builtins.str] = ...,
        less_than_or_equal: Optional[_builtins.str] = ...,
        matches: Optional[Sequence[_builtins.str]] = ...,
        not_equals: Optional[Sequence[_builtins.str]] = ...,
        not_matches: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def equals(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="greaterThan")
    def greater_than(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="greaterThanOrEqual")
    def greater_than_or_equal(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lessThan")
    def less_than(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="lessThanOrEqual")
    def less_than_or_equal(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def matches(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notEquals")
    def not_equals(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="notMatches")
    def not_matches(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MalwareProtectionPlanAction(dict):
    def __init__(
        __self__, *, taggings: Sequence[outputs.MalwareProtectionPlanActionTagging]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def taggings(self) -> Sequence[outputs.MalwareProtectionPlanActionTagging]: ...

@pulumi.output_type
class MalwareProtectionPlanActionTagging(dict):
    def __init__(__self__, *, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class MalwareProtectionPlanProtectedResource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, s3_bucket: outputs.MalwareProtectionPlanProtectedResourceS3Bucket
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> outputs.MalwareProtectionPlanProtectedResourceS3Bucket: ...

@pulumi.output_type
class MalwareProtectionPlanProtectedResourceS3Bucket(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        object_prefixes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectPrefixes")
    def object_prefixes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class MemberDetectorFeatureAdditionalConfiguration(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class OrganizationConfigurationDatasources(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kubernetes: Optional[
            outputs.OrganizationConfigurationDatasourcesKubernetes
        ] = ...,
        malware_protection: Optional[
            outputs.OrganizationConfigurationDatasourcesMalwareProtection
        ] = ...,
        s3_logs: Optional[outputs.OrganizationConfigurationDatasourcesS3Logs] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kubernetes(
        self,
    ) -> Optional[outputs.OrganizationConfigurationDatasourcesKubernetes]: ...
    @_builtins.property
    @pulumi.getter(name="malwareProtection")
    def malware_protection(
        self,
    ) -> Optional[outputs.OrganizationConfigurationDatasourcesMalwareProtection]: ...
    @_builtins.property
    @pulumi.getter(name="s3Logs")
    def s3_logs(
        self,
    ) -> Optional[outputs.OrganizationConfigurationDatasourcesS3Logs]: ...

@pulumi.output_type
class OrganizationConfigurationDatasourcesKubernetes(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audit_logs: outputs.OrganizationConfigurationDatasourcesKubernetesAuditLogs,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogs")
    def audit_logs(
        self,
    ) -> outputs.OrganizationConfigurationDatasourcesKubernetesAuditLogs: ...

@pulumi.output_type
class OrganizationConfigurationDatasourcesKubernetesAuditLogs(dict):
    def __init__(__self__, *, enable: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> _builtins.bool: ...

@pulumi.output_type
class OrganizationConfigurationDatasourcesMalwareProtection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        scan_ec2_instance_with_findings: outputs.OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scanEc2InstanceWithFindings")
    def scan_ec2_instance_with_findings(
        self,
    ) -> outputs.OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings: ...

@pulumi.output_type
class OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ebs_volumes: outputs.OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsVolumes")
    def ebs_volumes(
        self,
    ) -> outputs.OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes: ...

@pulumi.output_type
class OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumes(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, auto_enable: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> _builtins.bool: ...

@pulumi.output_type
class OrganizationConfigurationDatasourcesS3Logs(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, auto_enable: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> _builtins.bool: ...

@pulumi.output_type
class OrganizationConfigurationFeatureAdditionalConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, auto_enable: _builtins.str, name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetDetectorFeatureResult(dict):
    def __init__(
        __self__,
        *,
        additional_configurations: Sequence[
            outputs.GetDetectorFeatureAdditionalConfigurationResult
        ],
        name: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalConfigurations")
    def additional_configurations(
        self,
    ) -> Sequence[outputs.GetDetectorFeatureAdditionalConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetDetectorFeatureAdditionalConfigurationResult(dict):
    def __init__(__self__, *, name: _builtins.str, status: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
