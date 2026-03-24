import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClassificationExportConfigurationS3Destination",
    "ClassificationJobS3JobDefinition",
    "ClassificationJobS3JobDefinitionBucketCriteria",
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
    "ClassificationJobS3JobDefinitionBucketDefinition",
    "ClassificationJobS3JobDefinitionScoping",
    "ClassificationJobS3JobDefinitionScopingExcludes",
    "ClassificationJobS3JobDefinitionScopingExcludesAnd",
    ...,
    ...,
    ...,
    "ClassificationJobS3JobDefinitionScopingIncludes",
    "ClassificationJobS3JobDefinitionScopingIncludesAnd",
    ...,
    ...,
    ...,
    "ClassificationJobScheduleFrequency",
    "ClassificationJobUserPausedDetail",
]

@pulumi.output_type
class ClassificationExportConfigurationS3Destination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_name: _builtins.str,
        kms_key_arn: _builtins.str,
        key_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket_criteria: Optional[
            outputs.ClassificationJobS3JobDefinitionBucketCriteria
        ] = ...,
        bucket_definitions: Optional[
            Sequence[outputs.ClassificationJobS3JobDefinitionBucketDefinition]
        ] = ...,
        scoping: Optional[outputs.ClassificationJobS3JobDefinitionScoping] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketCriteria")
    def bucket_criteria(
        self,
    ) -> Optional[outputs.ClassificationJobS3JobDefinitionBucketCriteria]: ...
    @_builtins.property
    @pulumi.getter(name="bucketDefinitions")
    def bucket_definitions(
        self,
    ) -> Optional[
        Sequence[outputs.ClassificationJobS3JobDefinitionBucketDefinition]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def scoping(self) -> Optional[outputs.ClassificationJobS3JobDefinitionScoping]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteria(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[
            outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludes
        ] = ...,
        includes: Optional[
            outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludes
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludes]: ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludes]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludes(dict):
    def __init__(
        __self__,
        *,
        ands: Optional[
            Sequence[outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        Sequence[outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd]
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        simple_criterion: Optional[
            outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion
        ] = ...,
        tag_criterion: Optional[
            outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="simpleCriterion")
    def simple_criterion(
        self,
    ) -> Optional[
        outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tagCriterion")
    def tag_criterion(
        self,
    ) -> Optional[
        outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterion(dict):
    def __init__(
        __self__,
        *,
        comparator: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        comparator: Optional[_builtins.str] = ...,
        tag_values: Optional[
            Sequence[
                outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValue
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValue
        ]
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValue(
    dict
):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludes(dict):
    def __init__(
        __self__,
        *,
        ands: Optional[
            Sequence[outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        Sequence[outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd]
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        simple_criterion: Optional[
            outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion
        ] = ...,
        tag_criterion: Optional[
            outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="simpleCriterion")
    def simple_criterion(
        self,
    ) -> Optional[
        outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tagCriterion")
    def tag_criterion(
        self,
    ) -> Optional[
        outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterion(dict):
    def __init__(
        __self__,
        *,
        comparator: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        comparator: Optional[_builtins.str] = ...,
        tag_values: Optional[
            Sequence[
                outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValue
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValue
        ]
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValue(
    dict
):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionBucketDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, account_id: _builtins.str, buckets: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScoping(dict):
    def __init__(
        __self__,
        *,
        excludes: Optional[
            outputs.ClassificationJobS3JobDefinitionScopingExcludes
        ] = ...,
        includes: Optional[
            outputs.ClassificationJobS3JobDefinitionScopingIncludes
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[outputs.ClassificationJobS3JobDefinitionScopingExcludes]: ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[outputs.ClassificationJobS3JobDefinitionScopingIncludes]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingExcludes(dict):
    def __init__(
        __self__,
        *,
        ands: Optional[
            Sequence[outputs.ClassificationJobS3JobDefinitionScopingExcludesAnd]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        Sequence[outputs.ClassificationJobS3JobDefinitionScopingExcludesAnd]
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingExcludesAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        simple_scope_term: Optional[
            outputs.ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm
        ] = ...,
        tag_scope_term: Optional[
            outputs.ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="simpleScopeTerm")
    def simple_scope_term(
        self,
    ) -> Optional[
        outputs.ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tagScopeTerm")
    def tag_scope_term(
        self,
    ) -> Optional[
        outputs.ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTerm(dict):
    def __init__(
        __self__,
        *,
        comparator: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTerm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        comparator: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        tag_values: Optional[
            Sequence[
                outputs.ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValue
            ]
        ] = ...,
        target: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValue
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValue(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingIncludes(dict):
    def __init__(
        __self__,
        *,
        ands: Optional[
            Sequence[outputs.ClassificationJobS3JobDefinitionScopingIncludesAnd]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        Sequence[outputs.ClassificationJobS3JobDefinitionScopingIncludesAnd]
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingIncludesAnd(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        simple_scope_term: Optional[
            outputs.ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm
        ] = ...,
        tag_scope_term: Optional[
            outputs.ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="simpleScopeTerm")
    def simple_scope_term(
        self,
    ) -> Optional[
        outputs.ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tagScopeTerm")
    def tag_scope_term(
        self,
    ) -> Optional[
        outputs.ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm
    ]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTerm(dict):
    def __init__(
        __self__,
        *,
        comparator: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        values: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTerm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        comparator: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        tag_values: Optional[
            Sequence[
                outputs.ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValue
            ]
        ] = ...,
        target: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(
        self,
    ) -> Optional[
        Sequence[
            outputs.ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValue
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValue(dict):
    def __init__(
        __self__,
        *,
        key: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassificationJobScheduleFrequency(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        daily_schedule: Optional[_builtins.bool] = ...,
        monthly_schedule: Optional[_builtins.int] = ...,
        weekly_schedule: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ClassificationJobUserPausedDetail(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        job_expires_at: Optional[_builtins.str] = ...,
        job_imminent_expiration_health_event_arn: Optional[_builtins.str] = ...,
        job_paused_at: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobExpiresAt")
    def job_expires_at(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobImminentExpirationHealthEventArn")
    def job_imminent_expiration_health_event_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobPausedAt")
    def job_paused_at(self) -> Optional[_builtins.str]: ...
