import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DomainMatching",
    "DomainMatchingAutoMerging",
    "DomainMatchingAutoMergingConflictResolution",
    "DomainMatchingAutoMergingConsolidation",
    "DomainMatchingExportingConfig",
    "DomainMatchingExportingConfigS3Exporting",
    "DomainMatchingJobSchedule",
    "DomainRuleBasedMatching",
    "DomainRuleBasedMatchingAttributeTypesSelector",
    "DomainRuleBasedMatchingConflictResolution",
    "DomainRuleBasedMatchingExportingConfig",
    "DomainRuleBasedMatchingExportingConfigS3Exporting",
    "DomainRuleBasedMatchingMatchingRule",
    "ProfileAddress",
    "ProfileBillingAddress",
    "ProfileMailingAddress",
    "ProfileShippingAddress",
]

@pulumi.output_type
class DomainMatching(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        auto_merging: Optional[outputs.DomainMatchingAutoMerging] = ...,
        exporting_config: Optional[outputs.DomainMatchingExportingConfig] = ...,
        job_schedule: Optional[outputs.DomainMatchingJobSchedule] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="autoMerging")
    def auto_merging(self) -> Optional[outputs.DomainMatchingAutoMerging]: ...
    @_builtins.property
    @pulumi.getter(name="exportingConfig")
    def exporting_config(self) -> Optional[outputs.DomainMatchingExportingConfig]: ...
    @_builtins.property
    @pulumi.getter(name="jobSchedule")
    def job_schedule(self) -> Optional[outputs.DomainMatchingJobSchedule]: ...

@pulumi.output_type
class DomainMatchingAutoMerging(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        conflict_resolution: Optional[
            outputs.DomainMatchingAutoMergingConflictResolution
        ] = ...,
        consolidation: Optional[outputs.DomainMatchingAutoMergingConsolidation] = ...,
        min_allowed_confidence_score_for_merging: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="conflictResolution")
    def conflict_resolution(
        self,
    ) -> Optional[outputs.DomainMatchingAutoMergingConflictResolution]: ...
    @_builtins.property
    @pulumi.getter
    def consolidation(
        self,
    ) -> Optional[outputs.DomainMatchingAutoMergingConsolidation]: ...
    @_builtins.property
    @pulumi.getter(name="minAllowedConfidenceScoreForMerging")
    def min_allowed_confidence_score_for_merging(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class DomainMatchingAutoMergingConflictResolution(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conflict_resolving_model: _builtins.str,
        source_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conflictResolvingModel")
    def conflict_resolving_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainMatchingAutoMergingConsolidation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, matching_attributes_lists: Sequence[Sequence[_builtins.str]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchingAttributesLists")
    def matching_attributes_lists(self) -> Sequence[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainMatchingExportingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_exporting: Optional[outputs.DomainMatchingExportingConfigS3Exporting] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Exporting")
    def s3_exporting(
        self,
    ) -> Optional[outputs.DomainMatchingExportingConfigS3Exporting]: ...

@pulumi.output_type
class DomainMatchingExportingConfigS3Exporting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_bucket_name: _builtins.str,
        s3_key_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3KeyName")
    def s3_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainMatchingJobSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, day_of_the_week: _builtins.str, time: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> _builtins.str: ...

@pulumi.output_type
class DomainRuleBasedMatching(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: _builtins.bool,
        attribute_types_selector: Optional[
            outputs.DomainRuleBasedMatchingAttributeTypesSelector
        ] = ...,
        conflict_resolution: Optional[
            outputs.DomainRuleBasedMatchingConflictResolution
        ] = ...,
        exporting_config: Optional[
            outputs.DomainRuleBasedMatchingExportingConfig
        ] = ...,
        matching_rules: Optional[
            Sequence[outputs.DomainRuleBasedMatchingMatchingRule]
        ] = ...,
        max_allowed_rule_level_for_matching: Optional[_builtins.int] = ...,
        max_allowed_rule_level_for_merging: Optional[_builtins.int] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="attributeTypesSelector")
    def attribute_types_selector(
        self,
    ) -> Optional[outputs.DomainRuleBasedMatchingAttributeTypesSelector]: ...
    @_builtins.property
    @pulumi.getter(name="conflictResolution")
    def conflict_resolution(
        self,
    ) -> Optional[outputs.DomainRuleBasedMatchingConflictResolution]: ...
    @_builtins.property
    @pulumi.getter(name="exportingConfig")
    def exporting_config(
        self,
    ) -> Optional[outputs.DomainRuleBasedMatchingExportingConfig]: ...
    @_builtins.property
    @pulumi.getter(name="matchingRules")
    def matching_rules(
        self,
    ) -> Optional[Sequence[outputs.DomainRuleBasedMatchingMatchingRule]]: ...
    @_builtins.property
    @pulumi.getter(name="maxAllowedRuleLevelForMatching")
    def max_allowed_rule_level_for_matching(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxAllowedRuleLevelForMerging")
    def max_allowed_rule_level_for_merging(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainRuleBasedMatchingAttributeTypesSelector(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attribute_matching_model: _builtins.str,
        addresses: Optional[Sequence[_builtins.str]] = ...,
        email_addresses: Optional[Sequence[_builtins.str]] = ...,
        phone_numbers: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeMatchingModel")
    def attribute_matching_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DomainRuleBasedMatchingConflictResolution(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conflict_resolving_model: _builtins.str,
        source_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conflictResolvingModel")
    def conflict_resolving_model(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainRuleBasedMatchingExportingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_exporting: Optional[
            outputs.DomainRuleBasedMatchingExportingConfigS3Exporting
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Exporting")
    def s3_exporting(
        self,
    ) -> Optional[outputs.DomainRuleBasedMatchingExportingConfigS3Exporting]: ...

@pulumi.output_type
class DomainRuleBasedMatchingExportingConfigS3Exporting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        s3_bucket_name: _builtins.str,
        s3_key_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="s3KeyName")
    def s3_key_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DomainRuleBasedMatchingMatchingRule(dict):
    def __init__(__self__, *, rules: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ProfileAddress(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address1: Optional[_builtins.str] = ...,
        address2: Optional[_builtins.str] = ...,
        address3: Optional[_builtins.str] = ...,
        address4: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        country: Optional[_builtins.str] = ...,
        county: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        province: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address4(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def county(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProfileBillingAddress(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address1: Optional[_builtins.str] = ...,
        address2: Optional[_builtins.str] = ...,
        address3: Optional[_builtins.str] = ...,
        address4: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        country: Optional[_builtins.str] = ...,
        county: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        province: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address4(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def county(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProfileMailingAddress(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address1: Optional[_builtins.str] = ...,
        address2: Optional[_builtins.str] = ...,
        address3: Optional[_builtins.str] = ...,
        address4: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        country: Optional[_builtins.str] = ...,
        county: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        province: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address4(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def county(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProfileShippingAddress(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        address1: Optional[_builtins.str] = ...,
        address2: Optional[_builtins.str] = ...,
        address3: Optional[_builtins.str] = ...,
        address4: Optional[_builtins.str] = ...,
        city: Optional[_builtins.str] = ...,
        country: Optional[_builtins.str] = ...,
        county: Optional[_builtins.str] = ...,
        postal_code: Optional[_builtins.str] = ...,
        province: Optional[_builtins.str] = ...,
        state: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address1(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address2(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address3(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def address4(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def county(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]: ...
