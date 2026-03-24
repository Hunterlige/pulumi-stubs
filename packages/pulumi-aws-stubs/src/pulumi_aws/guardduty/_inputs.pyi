import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DetectorDatasourcesArgs",
    "DetectorDatasourcesArgsDict",
    "DetectorDatasourcesKubernetesArgs",
    "DetectorDatasourcesKubernetesArgsDict",
    "DetectorDatasourcesKubernetesAuditLogsArgs",
    "DetectorDatasourcesKubernetesAuditLogsArgsDict",
    "DetectorDatasourcesMalwareProtectionArgs",
    "DetectorDatasourcesMalwareProtectionArgsDict",
    ...,
    ...,
    ...,
    ...,
    "DetectorDatasourcesS3LogsArgs",
    "DetectorDatasourcesS3LogsArgsDict",
    "DetectorFeatureAdditionalConfigurationArgs",
    "DetectorFeatureAdditionalConfigurationArgsDict",
    "FilterFindingCriteriaArgs",
    "FilterFindingCriteriaArgsDict",
    "FilterFindingCriteriaCriterionArgs",
    "FilterFindingCriteriaCriterionArgsDict",
    "MalwareProtectionPlanActionArgs",
    "MalwareProtectionPlanActionArgsDict",
    "MalwareProtectionPlanActionTaggingArgs",
    "MalwareProtectionPlanActionTaggingArgsDict",
    "MalwareProtectionPlanProtectedResourceArgs",
    "MalwareProtectionPlanProtectedResourceArgsDict",
    "MalwareProtectionPlanProtectedResourceS3BucketArgs",
    ...,
    "MemberDetectorFeatureAdditionalConfigurationArgs",
    ...,
    "OrganizationConfigurationDatasourcesArgs",
    "OrganizationConfigurationDatasourcesArgsDict",
    "OrganizationConfigurationDatasourcesKubernetesArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "OrganizationConfigurationDatasourcesS3LogsArgs",
    "OrganizationConfigurationDatasourcesS3LogsArgsDict",
    ...,
    ...,
]

class DetectorDatasourcesArgsDict(TypedDict):
    kubernetes: NotRequired[pulumi.Input[DetectorDatasourcesKubernetesArgsDict]]
    malware_protection: NotRequired[
        pulumi.Input[DetectorDatasourcesMalwareProtectionArgsDict]
    ]
    s3_logs: NotRequired[pulumi.Input[DetectorDatasourcesS3LogsArgsDict]]
    ...

@pulumi.input_type
class DetectorDatasourcesArgs:
    def __init__(
        __self__,
        *,
        kubernetes: Optional[pulumi.Input[DetectorDatasourcesKubernetesArgs]] = ...,
        malware_protection: Optional[
            pulumi.Input[DetectorDatasourcesMalwareProtectionArgs]
        ] = ...,
        s3_logs: Optional[pulumi.Input[DetectorDatasourcesS3LogsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kubernetes(
        self,
    ) -> Optional[pulumi.Input[DetectorDatasourcesKubernetesArgs]]: ...
    @kubernetes.setter
    def kubernetes(
        self, value: Optional[pulumi.Input[DetectorDatasourcesKubernetesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="malwareProtection")
    def malware_protection(
        self,
    ) -> Optional[pulumi.Input[DetectorDatasourcesMalwareProtectionArgs]]: ...
    @malware_protection.setter
    def malware_protection(
        self, value: Optional[pulumi.Input[DetectorDatasourcesMalwareProtectionArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Logs")
    def s3_logs(self) -> Optional[pulumi.Input[DetectorDatasourcesS3LogsArgs]]: ...
    @s3_logs.setter
    def s3_logs(self, value: Optional[pulumi.Input[DetectorDatasourcesS3LogsArgs]]): ...

class DetectorDatasourcesKubernetesArgsDict(TypedDict):
    audit_logs: pulumi.Input[DetectorDatasourcesKubernetesAuditLogsArgsDict]
    ...

@pulumi.input_type
class DetectorDatasourcesKubernetesArgs:
    def __init__(
        __self__,
        *,
        audit_logs: pulumi.Input[DetectorDatasourcesKubernetesAuditLogsArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogs")
    def audit_logs(
        self,
    ) -> pulumi.Input[DetectorDatasourcesKubernetesAuditLogsArgs]: ...
    @audit_logs.setter
    def audit_logs(
        self, value: pulumi.Input[DetectorDatasourcesKubernetesAuditLogsArgs]
    ): ...

class DetectorDatasourcesKubernetesAuditLogsArgsDict(TypedDict):
    enable: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class DetectorDatasourcesKubernetesAuditLogsArgs:
    def __init__(__self__, *, enable: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> pulumi.Input[_builtins.bool]: ...
    @enable.setter
    def enable(self, value: pulumi.Input[_builtins.bool]): ...

class DetectorDatasourcesMalwareProtectionArgsDict(TypedDict):
    scan_ec2_instance_with_findings: pulumi.Input[
        DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgsDict
    ]
    ...

@pulumi.input_type
class DetectorDatasourcesMalwareProtectionArgs:
    def __init__(
        __self__,
        *,
        scan_ec2_instance_with_findings: pulumi.Input[
            DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scanEc2InstanceWithFindings")
    def scan_ec2_instance_with_findings(
        self,
    ) -> pulumi.Input[
        DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgs
    ]: ...
    @scan_ec2_instance_with_findings.setter
    def scan_ec2_instance_with_findings(
        self,
        value: pulumi.Input[
            DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgs
        ],
    ): ...

class DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgsDict(
    TypedDict
):
    ebs_volumes: pulumi.Input[
        DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgsDict
    ]
    ...

@pulumi.input_type
class DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgs:
    def __init__(
        __self__,
        *,
        ebs_volumes: pulumi.Input[
            DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsVolumes")
    def ebs_volumes(
        self,
    ) -> pulumi.Input[
        DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgs
    ]: ...
    @ebs_volumes.setter
    def ebs_volumes(
        self,
        value: pulumi.Input[
            DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgs
        ],
    ): ...

class DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgsDict(
    TypedDict
):
    enable: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class DetectorDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgs:
    def __init__(__self__, *, enable: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> pulumi.Input[_builtins.bool]: ...
    @enable.setter
    def enable(self, value: pulumi.Input[_builtins.bool]): ...

class DetectorDatasourcesS3LogsArgsDict(TypedDict):
    enable: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class DetectorDatasourcesS3LogsArgs:
    def __init__(__self__, *, enable: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> pulumi.Input[_builtins.bool]: ...
    @enable.setter
    def enable(self, value: pulumi.Input[_builtins.bool]): ...

class DetectorFeatureAdditionalConfigurationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DetectorFeatureAdditionalConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class FilterFindingCriteriaArgsDict(TypedDict):
    criterions: pulumi.Input[
        Sequence[pulumi.Input[FilterFindingCriteriaCriterionArgsDict]]
    ]
    ...

@pulumi.input_type
class FilterFindingCriteriaArgs:
    def __init__(
        __self__,
        *,
        criterions: pulumi.Input[
            Sequence[pulumi.Input[FilterFindingCriteriaCriterionArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def criterions(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[FilterFindingCriteriaCriterionArgs]]]: ...
    @criterions.setter
    def criterions(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[FilterFindingCriteriaCriterionArgs]]],
    ): ...

class FilterFindingCriteriaCriterionArgsDict(TypedDict):
    field: pulumi.Input[_builtins.str]
    equals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    greater_than: NotRequired[pulumi.Input[_builtins.str]]
    greater_than_or_equal: NotRequired[pulumi.Input[_builtins.str]]
    less_than: NotRequired[pulumi.Input[_builtins.str]]
    less_than_or_equal: NotRequired[pulumi.Input[_builtins.str]]
    matches: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    not_equals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    not_matches: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class FilterFindingCriteriaCriterionArgs:
    def __init__(
        __self__,
        *,
        field: pulumi.Input[_builtins.str],
        equals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        greater_than: Optional[pulumi.Input[_builtins.str]] = ...,
        greater_than_or_equal: Optional[pulumi.Input[_builtins.str]] = ...,
        less_than: Optional[pulumi.Input[_builtins.str]] = ...,
        less_than_or_equal: Optional[pulumi.Input[_builtins.str]] = ...,
        matches: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        not_equals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        not_matches: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Input[_builtins.str]: ...
    @field.setter
    def field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def equals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @equals.setter
    def equals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="greaterThan")
    def greater_than(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @greater_than.setter
    def greater_than(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="greaterThanOrEqual")
    def greater_than_or_equal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @greater_than_or_equal.setter
    def greater_than_or_equal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lessThan")
    def less_than(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @less_than.setter
    def less_than(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lessThanOrEqual")
    def less_than_or_equal(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @less_than_or_equal.setter
    def less_than_or_equal(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def matches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @matches.setter
    def matches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notEquals")
    def not_equals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_equals.setter
    def not_equals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="notMatches")
    def not_matches(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @not_matches.setter
    def not_matches(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MalwareProtectionPlanActionArgsDict(TypedDict):
    taggings: pulumi.Input[
        Sequence[pulumi.Input[MalwareProtectionPlanActionTaggingArgsDict]]
    ]
    ...

@pulumi.input_type
class MalwareProtectionPlanActionArgs:
    def __init__(
        __self__,
        *,
        taggings: pulumi.Input[
            Sequence[pulumi.Input[MalwareProtectionPlanActionTaggingArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def taggings(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[MalwareProtectionPlanActionTaggingArgs]]
    ]: ...
    @taggings.setter
    def taggings(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[MalwareProtectionPlanActionTaggingArgs]]
        ],
    ): ...

class MalwareProtectionPlanActionTaggingArgsDict(TypedDict):
    status: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class MalwareProtectionPlanActionTaggingArgs:
    def __init__(__self__, *, status: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class MalwareProtectionPlanProtectedResourceArgsDict(TypedDict):
    s3_bucket: pulumi.Input[MalwareProtectionPlanProtectedResourceS3BucketArgsDict]
    ...

@pulumi.input_type
class MalwareProtectionPlanProtectedResourceArgs:
    def __init__(
        __self__,
        *,
        s3_bucket: pulumi.Input[MalwareProtectionPlanProtectedResourceS3BucketArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(
        self,
    ) -> pulumi.Input[MalwareProtectionPlanProtectedResourceS3BucketArgs]: ...
    @s3_bucket.setter
    def s3_bucket(
        self, value: pulumi.Input[MalwareProtectionPlanProtectedResourceS3BucketArgs]
    ): ...

class MalwareProtectionPlanProtectedResourceS3BucketArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    object_prefixes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class MalwareProtectionPlanProtectedResourceS3BucketArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        object_prefixes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="objectPrefixes")
    def object_prefixes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @object_prefixes.setter
    def object_prefixes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class MemberDetectorFeatureAdditionalConfigurationArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    status: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class MemberDetectorFeatureAdditionalConfigurationArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        status: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Input[_builtins.str]: ...
    @status.setter
    def status(self, value: pulumi.Input[_builtins.str]): ...

class OrganizationConfigurationDatasourcesArgsDict(TypedDict):
    kubernetes: NotRequired[
        pulumi.Input[OrganizationConfigurationDatasourcesKubernetesArgsDict]
    ]
    malware_protection: NotRequired[
        pulumi.Input[OrganizationConfigurationDatasourcesMalwareProtectionArgsDict]
    ]
    s3_logs: NotRequired[
        pulumi.Input[OrganizationConfigurationDatasourcesS3LogsArgsDict]
    ]
    ...

@pulumi.input_type
class OrganizationConfigurationDatasourcesArgs:
    def __init__(
        __self__,
        *,
        kubernetes: Optional[
            pulumi.Input[OrganizationConfigurationDatasourcesKubernetesArgs]
        ] = ...,
        malware_protection: Optional[
            pulumi.Input[OrganizationConfigurationDatasourcesMalwareProtectionArgs]
        ] = ...,
        s3_logs: Optional[
            pulumi.Input[OrganizationConfigurationDatasourcesS3LogsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def kubernetes(
        self,
    ) -> Optional[pulumi.Input[OrganizationConfigurationDatasourcesKubernetesArgs]]: ...
    @kubernetes.setter
    def kubernetes(
        self,
        value: Optional[
            pulumi.Input[OrganizationConfigurationDatasourcesKubernetesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="malwareProtection")
    def malware_protection(
        self,
    ) -> Optional[
        pulumi.Input[OrganizationConfigurationDatasourcesMalwareProtectionArgs]
    ]: ...
    @malware_protection.setter
    def malware_protection(
        self,
        value: Optional[
            pulumi.Input[OrganizationConfigurationDatasourcesMalwareProtectionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Logs")
    def s3_logs(
        self,
    ) -> Optional[pulumi.Input[OrganizationConfigurationDatasourcesS3LogsArgs]]: ...
    @s3_logs.setter
    def s3_logs(
        self,
        value: Optional[pulumi.Input[OrganizationConfigurationDatasourcesS3LogsArgs]],
    ): ...

class OrganizationConfigurationDatasourcesKubernetesArgsDict(TypedDict):
    audit_logs: pulumi.Input[
        OrganizationConfigurationDatasourcesKubernetesAuditLogsArgsDict
    ]
    ...

@pulumi.input_type
class OrganizationConfigurationDatasourcesKubernetesArgs:
    def __init__(
        __self__,
        *,
        audit_logs: pulumi.Input[
            OrganizationConfigurationDatasourcesKubernetesAuditLogsArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="auditLogs")
    def audit_logs(
        self,
    ) -> pulumi.Input[OrganizationConfigurationDatasourcesKubernetesAuditLogsArgs]: ...
    @audit_logs.setter
    def audit_logs(
        self,
        value: pulumi.Input[
            OrganizationConfigurationDatasourcesKubernetesAuditLogsArgs
        ],
    ): ...

class OrganizationConfigurationDatasourcesKubernetesAuditLogsArgsDict(TypedDict):
    enable: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class OrganizationConfigurationDatasourcesKubernetesAuditLogsArgs:
    def __init__(__self__, *, enable: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enable(self) -> pulumi.Input[_builtins.bool]: ...
    @enable.setter
    def enable(self, value: pulumi.Input[_builtins.bool]): ...

class OrganizationConfigurationDatasourcesMalwareProtectionArgsDict(TypedDict):
    scan_ec2_instance_with_findings: pulumi.Input[
        OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgsDict
    ]
    ...

@pulumi.input_type
class OrganizationConfigurationDatasourcesMalwareProtectionArgs:
    def __init__(
        __self__,
        *,
        scan_ec2_instance_with_findings: pulumi.Input[
            OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scanEc2InstanceWithFindings")
    def scan_ec2_instance_with_findings(
        self,
    ) -> pulumi.Input[
        OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgs
    ]: ...
    @scan_ec2_instance_with_findings.setter
    def scan_ec2_instance_with_findings(
        self,
        value: pulumi.Input[
            OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgs
        ],
    ): ...

class OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgsDict(
    TypedDict
):
    ebs_volumes: pulumi.Input[
        OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgsDict
    ]
    ...

@pulumi.input_type
class OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsArgs:
    def __init__(
        __self__,
        *,
        ebs_volumes: pulumi.Input[
            OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ebsVolumes")
    def ebs_volumes(
        self,
    ) -> pulumi.Input[
        OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgs
    ]: ...
    @ebs_volumes.setter
    def ebs_volumes(
        self,
        value: pulumi.Input[
            OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgs
        ],
    ): ...

class OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgsDict(
    TypedDict
):
    auto_enable: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class OrganizationConfigurationDatasourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesArgs:
    def __init__(__self__, *, auto_enable: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Input[_builtins.bool]: ...
    @auto_enable.setter
    def auto_enable(self, value: pulumi.Input[_builtins.bool]): ...

class OrganizationConfigurationDatasourcesS3LogsArgsDict(TypedDict):
    auto_enable: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class OrganizationConfigurationDatasourcesS3LogsArgs:
    def __init__(__self__, *, auto_enable: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Input[_builtins.bool]: ...
    @auto_enable.setter
    def auto_enable(self, value: pulumi.Input[_builtins.bool]): ...

class OrganizationConfigurationFeatureAdditionalConfigurationArgsDict(TypedDict):
    auto_enable: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class OrganizationConfigurationFeatureAdditionalConfigurationArgs:
    def __init__(
        __self__,
        *,
        auto_enable: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="autoEnable")
    def auto_enable(self) -> pulumi.Input[_builtins.str]: ...
    @auto_enable.setter
    def auto_enable(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
