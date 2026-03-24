import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "DomainMatchingArgs",
    "DomainMatchingArgsDict",
    "DomainMatchingAutoMergingArgs",
    "DomainMatchingAutoMergingArgsDict",
    "DomainMatchingAutoMergingConflictResolutionArgs",
    ...,
    "DomainMatchingAutoMergingConsolidationArgs",
    "DomainMatchingAutoMergingConsolidationArgsDict",
    "DomainMatchingExportingConfigArgs",
    "DomainMatchingExportingConfigArgsDict",
    "DomainMatchingExportingConfigS3ExportingArgs",
    "DomainMatchingExportingConfigS3ExportingArgsDict",
    "DomainMatchingJobScheduleArgs",
    "DomainMatchingJobScheduleArgsDict",
    "DomainRuleBasedMatchingArgs",
    "DomainRuleBasedMatchingArgsDict",
    "DomainRuleBasedMatchingAttributeTypesSelectorArgs",
    ...,
    "DomainRuleBasedMatchingConflictResolutionArgs",
    "DomainRuleBasedMatchingConflictResolutionArgsDict",
    "DomainRuleBasedMatchingExportingConfigArgs",
    "DomainRuleBasedMatchingExportingConfigArgsDict",
    ...,
    ...,
    "DomainRuleBasedMatchingMatchingRuleArgs",
    "DomainRuleBasedMatchingMatchingRuleArgsDict",
    "ProfileAddressArgs",
    "ProfileAddressArgsDict",
    "ProfileBillingAddressArgs",
    "ProfileBillingAddressArgsDict",
    "ProfileMailingAddressArgs",
    "ProfileMailingAddressArgsDict",
    "ProfileShippingAddressArgs",
    "ProfileShippingAddressArgsDict",
]

class DomainMatchingArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    auto_merging: NotRequired[pulumi.Input[DomainMatchingAutoMergingArgsDict]]
    exporting_config: NotRequired[pulumi.Input[DomainMatchingExportingConfigArgsDict]]
    job_schedule: NotRequired[pulumi.Input[DomainMatchingJobScheduleArgsDict]]
    ...

@pulumi.input_type
class DomainMatchingArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        auto_merging: Optional[pulumi.Input[DomainMatchingAutoMergingArgs]] = ...,
        exporting_config: Optional[
            pulumi.Input[DomainMatchingExportingConfigArgs]
        ] = ...,
        job_schedule: Optional[pulumi.Input[DomainMatchingJobScheduleArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="autoMerging")
    def auto_merging(self) -> Optional[pulumi.Input[DomainMatchingAutoMergingArgs]]: ...
    @auto_merging.setter
    def auto_merging(
        self, value: Optional[pulumi.Input[DomainMatchingAutoMergingArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportingConfig")
    def exporting_config(
        self,
    ) -> Optional[pulumi.Input[DomainMatchingExportingConfigArgs]]: ...
    @exporting_config.setter
    def exporting_config(
        self, value: Optional[pulumi.Input[DomainMatchingExportingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobSchedule")
    def job_schedule(self) -> Optional[pulumi.Input[DomainMatchingJobScheduleArgs]]: ...
    @job_schedule.setter
    def job_schedule(
        self, value: Optional[pulumi.Input[DomainMatchingJobScheduleArgs]]
    ): ...

class DomainMatchingAutoMergingArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    conflict_resolution: NotRequired[
        pulumi.Input[DomainMatchingAutoMergingConflictResolutionArgsDict]
    ]
    consolidation: NotRequired[
        pulumi.Input[DomainMatchingAutoMergingConsolidationArgsDict]
    ]
    min_allowed_confidence_score_for_merging: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class DomainMatchingAutoMergingArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        conflict_resolution: Optional[
            pulumi.Input[DomainMatchingAutoMergingConflictResolutionArgs]
        ] = ...,
        consolidation: Optional[
            pulumi.Input[DomainMatchingAutoMergingConsolidationArgs]
        ] = ...,
        min_allowed_confidence_score_for_merging: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="conflictResolution")
    def conflict_resolution(
        self,
    ) -> Optional[pulumi.Input[DomainMatchingAutoMergingConflictResolutionArgs]]: ...
    @conflict_resolution.setter
    def conflict_resolution(
        self,
        value: Optional[pulumi.Input[DomainMatchingAutoMergingConflictResolutionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def consolidation(
        self,
    ) -> Optional[pulumi.Input[DomainMatchingAutoMergingConsolidationArgs]]: ...
    @consolidation.setter
    def consolidation(
        self, value: Optional[pulumi.Input[DomainMatchingAutoMergingConsolidationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minAllowedConfidenceScoreForMerging")
    def min_allowed_confidence_score_for_merging(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @min_allowed_confidence_score_for_merging.setter
    def min_allowed_confidence_score_for_merging(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class DomainMatchingAutoMergingConflictResolutionArgsDict(TypedDict):
    conflict_resolving_model: pulumi.Input[_builtins.str]
    source_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainMatchingAutoMergingConflictResolutionArgs:
    def __init__(
        __self__,
        *,
        conflict_resolving_model: pulumi.Input[_builtins.str],
        source_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conflictResolvingModel")
    def conflict_resolving_model(self) -> pulumi.Input[_builtins.str]: ...
    @conflict_resolving_model.setter
    def conflict_resolving_model(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_name.setter
    def source_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainMatchingAutoMergingConsolidationArgsDict(TypedDict):
    matching_attributes_lists: pulumi.Input[
        Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ]
    ...

@pulumi.input_type
class DomainMatchingAutoMergingConsolidationArgs:
    def __init__(
        __self__,
        *,
        matching_attributes_lists: pulumi.Input[
            Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchingAttributesLists")
    def matching_attributes_lists(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ]: ...
    @matching_attributes_lists.setter
    def matching_attributes_lists(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
        ],
    ): ...

class DomainMatchingExportingConfigArgsDict(TypedDict):
    s3_exporting: NotRequired[
        pulumi.Input[DomainMatchingExportingConfigS3ExportingArgsDict]
    ]
    ...

@pulumi.input_type
class DomainMatchingExportingConfigArgs:
    def __init__(
        __self__,
        *,
        s3_exporting: Optional[
            pulumi.Input[DomainMatchingExportingConfigS3ExportingArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Exporting")
    def s3_exporting(
        self,
    ) -> Optional[pulumi.Input[DomainMatchingExportingConfigS3ExportingArgs]]: ...
    @s3_exporting.setter
    def s3_exporting(
        self,
        value: Optional[pulumi.Input[DomainMatchingExportingConfigS3ExportingArgs]],
    ): ...

class DomainMatchingExportingConfigS3ExportingArgsDict(TypedDict):
    s3_bucket_name: pulumi.Input[_builtins.str]
    s3_key_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainMatchingExportingConfigS3ExportingArgs:
    def __init__(
        __self__,
        *,
        s3_bucket_name: pulumi.Input[_builtins.str],
        s3_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3KeyName")
    def s3_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_key_name.setter
    def s3_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainMatchingJobScheduleArgsDict(TypedDict):
    day_of_the_week: pulumi.Input[_builtins.str]
    time: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DomainMatchingJobScheduleArgs:
    def __init__(
        __self__,
        *,
        day_of_the_week: pulumi.Input[_builtins.str],
        time: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> pulumi.Input[_builtins.str]: ...
    @day_of_the_week.setter
    def day_of_the_week(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def time(self) -> pulumi.Input[_builtins.str]: ...
    @time.setter
    def time(self, value: pulumi.Input[_builtins.str]): ...

class DomainRuleBasedMatchingArgsDict(TypedDict):
    enabled: pulumi.Input[_builtins.bool]
    attribute_types_selector: NotRequired[
        pulumi.Input[DomainRuleBasedMatchingAttributeTypesSelectorArgsDict]
    ]
    conflict_resolution: NotRequired[
        pulumi.Input[DomainRuleBasedMatchingConflictResolutionArgsDict]
    ]
    exporting_config: NotRequired[
        pulumi.Input[DomainRuleBasedMatchingExportingConfigArgsDict]
    ]
    matching_rules: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DomainRuleBasedMatchingMatchingRuleArgsDict]]
        ]
    ]
    max_allowed_rule_level_for_matching: NotRequired[pulumi.Input[_builtins.int]]
    max_allowed_rule_level_for_merging: NotRequired[pulumi.Input[_builtins.int]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainRuleBasedMatchingArgs:
    def __init__(
        __self__,
        *,
        enabled: pulumi.Input[_builtins.bool],
        attribute_types_selector: Optional[
            pulumi.Input[DomainRuleBasedMatchingAttributeTypesSelectorArgs]
        ] = ...,
        conflict_resolution: Optional[
            pulumi.Input[DomainRuleBasedMatchingConflictResolutionArgs]
        ] = ...,
        exporting_config: Optional[
            pulumi.Input[DomainRuleBasedMatchingExportingConfigArgs]
        ] = ...,
        matching_rules: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DomainRuleBasedMatchingMatchingRuleArgs]]
            ]
        ] = ...,
        max_allowed_rule_level_for_matching: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        max_allowed_rule_level_for_merging: Optional[pulumi.Input[_builtins.int]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @enabled.setter
    def enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="attributeTypesSelector")
    def attribute_types_selector(
        self,
    ) -> Optional[pulumi.Input[DomainRuleBasedMatchingAttributeTypesSelectorArgs]]: ...
    @attribute_types_selector.setter
    def attribute_types_selector(
        self,
        value: Optional[
            pulumi.Input[DomainRuleBasedMatchingAttributeTypesSelectorArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="conflictResolution")
    def conflict_resolution(
        self,
    ) -> Optional[pulumi.Input[DomainRuleBasedMatchingConflictResolutionArgs]]: ...
    @conflict_resolution.setter
    def conflict_resolution(
        self,
        value: Optional[pulumi.Input[DomainRuleBasedMatchingConflictResolutionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportingConfig")
    def exporting_config(
        self,
    ) -> Optional[pulumi.Input[DomainRuleBasedMatchingExportingConfigArgs]]: ...
    @exporting_config.setter
    def exporting_config(
        self, value: Optional[pulumi.Input[DomainRuleBasedMatchingExportingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="matchingRules")
    def matching_rules(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DomainRuleBasedMatchingMatchingRuleArgs]]]
    ]: ...
    @matching_rules.setter
    def matching_rules(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DomainRuleBasedMatchingMatchingRuleArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAllowedRuleLevelForMatching")
    def max_allowed_rule_level_for_matching(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_allowed_rule_level_for_matching.setter
    def max_allowed_rule_level_for_matching(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxAllowedRuleLevelForMerging")
    def max_allowed_rule_level_for_merging(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_allowed_rule_level_for_merging.setter
    def max_allowed_rule_level_for_merging(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainRuleBasedMatchingAttributeTypesSelectorArgsDict(TypedDict):
    attribute_matching_model: pulumi.Input[_builtins.str]
    addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    email_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    phone_numbers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DomainRuleBasedMatchingAttributeTypesSelectorArgs:
    def __init__(
        __self__,
        *,
        attribute_matching_model: pulumi.Input[_builtins.str],
        addresses: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        email_addresses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        phone_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeMatchingModel")
    def attribute_matching_model(self) -> pulumi.Input[_builtins.str]: ...
    @attribute_matching_model.setter
    def attribute_matching_model(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @addresses.setter
    def addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emailAddresses")
    def email_addresses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @email_addresses.setter
    def email_addresses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @phone_numbers.setter
    def phone_numbers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DomainRuleBasedMatchingConflictResolutionArgsDict(TypedDict):
    conflict_resolving_model: pulumi.Input[_builtins.str]
    source_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainRuleBasedMatchingConflictResolutionArgs:
    def __init__(
        __self__,
        *,
        conflict_resolving_model: pulumi.Input[_builtins.str],
        source_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conflictResolvingModel")
    def conflict_resolving_model(self) -> pulumi.Input[_builtins.str]: ...
    @conflict_resolving_model.setter
    def conflict_resolving_model(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sourceName")
    def source_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_name.setter
    def source_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainRuleBasedMatchingExportingConfigArgsDict(TypedDict):
    s3_exporting: NotRequired[
        pulumi.Input[DomainRuleBasedMatchingExportingConfigS3ExportingArgsDict]
    ]
    ...

@pulumi.input_type
class DomainRuleBasedMatchingExportingConfigArgs:
    def __init__(
        __self__,
        *,
        s3_exporting: Optional[
            pulumi.Input[DomainRuleBasedMatchingExportingConfigS3ExportingArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3Exporting")
    def s3_exporting(
        self,
    ) -> Optional[
        pulumi.Input[DomainRuleBasedMatchingExportingConfigS3ExportingArgs]
    ]: ...
    @s3_exporting.setter
    def s3_exporting(
        self,
        value: Optional[
            pulumi.Input[DomainRuleBasedMatchingExportingConfigS3ExportingArgs]
        ],
    ): ...

class DomainRuleBasedMatchingExportingConfigS3ExportingArgsDict(TypedDict):
    s3_bucket_name: pulumi.Input[_builtins.str]
    s3_key_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DomainRuleBasedMatchingExportingConfigS3ExportingArgs:
    def __init__(
        __self__,
        *,
        s3_bucket_name: pulumi.Input[_builtins.str],
        s3_key_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket_name.setter
    def s3_bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3KeyName")
    def s3_key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_key_name.setter
    def s3_key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DomainRuleBasedMatchingMatchingRuleArgsDict(TypedDict):
    rules: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class DomainRuleBasedMatchingMatchingRuleArgs:
    def __init__(
        __self__, *, rules: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ProfileAddressArgsDict(TypedDict):
    address1: NotRequired[pulumi.Input[_builtins.str]]
    address2: NotRequired[pulumi.Input[_builtins.str]]
    address3: NotRequired[pulumi.Input[_builtins.str]]
    address4: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    country: NotRequired[pulumi.Input[_builtins.str]]
    county: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    province: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ProfileAddressArgs:
    def __init__(
        __self__,
        *,
        address1: Optional[pulumi.Input[_builtins.str]] = ...,
        address2: Optional[pulumi.Input[_builtins.str]] = ...,
        address3: Optional[pulumi.Input[_builtins.str]] = ...,
        address4: Optional[pulumi.Input[_builtins.str]] = ...,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        country: Optional[pulumi.Input[_builtins.str]] = ...,
        county: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        province: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address1.setter
    def address1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address2.setter
    def address2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address3(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address3.setter
    def address3(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address4(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address4.setter
    def address4(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country.setter
    def country(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def county(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @county.setter
    def county(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @province.setter
    def province(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProfileBillingAddressArgsDict(TypedDict):
    address1: NotRequired[pulumi.Input[_builtins.str]]
    address2: NotRequired[pulumi.Input[_builtins.str]]
    address3: NotRequired[pulumi.Input[_builtins.str]]
    address4: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    country: NotRequired[pulumi.Input[_builtins.str]]
    county: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    province: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ProfileBillingAddressArgs:
    def __init__(
        __self__,
        *,
        address1: Optional[pulumi.Input[_builtins.str]] = ...,
        address2: Optional[pulumi.Input[_builtins.str]] = ...,
        address3: Optional[pulumi.Input[_builtins.str]] = ...,
        address4: Optional[pulumi.Input[_builtins.str]] = ...,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        country: Optional[pulumi.Input[_builtins.str]] = ...,
        county: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        province: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address1.setter
    def address1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address2.setter
    def address2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address3(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address3.setter
    def address3(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address4(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address4.setter
    def address4(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country.setter
    def country(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def county(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @county.setter
    def county(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @province.setter
    def province(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProfileMailingAddressArgsDict(TypedDict):
    address1: NotRequired[pulumi.Input[_builtins.str]]
    address2: NotRequired[pulumi.Input[_builtins.str]]
    address3: NotRequired[pulumi.Input[_builtins.str]]
    address4: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    country: NotRequired[pulumi.Input[_builtins.str]]
    county: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    province: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ProfileMailingAddressArgs:
    def __init__(
        __self__,
        *,
        address1: Optional[pulumi.Input[_builtins.str]] = ...,
        address2: Optional[pulumi.Input[_builtins.str]] = ...,
        address3: Optional[pulumi.Input[_builtins.str]] = ...,
        address4: Optional[pulumi.Input[_builtins.str]] = ...,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        country: Optional[pulumi.Input[_builtins.str]] = ...,
        county: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        province: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address1.setter
    def address1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address2.setter
    def address2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address3(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address3.setter
    def address3(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address4(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address4.setter
    def address4(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country.setter
    def country(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def county(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @county.setter
    def county(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @province.setter
    def province(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ProfileShippingAddressArgsDict(TypedDict):
    address1: NotRequired[pulumi.Input[_builtins.str]]
    address2: NotRequired[pulumi.Input[_builtins.str]]
    address3: NotRequired[pulumi.Input[_builtins.str]]
    address4: NotRequired[pulumi.Input[_builtins.str]]
    city: NotRequired[pulumi.Input[_builtins.str]]
    country: NotRequired[pulumi.Input[_builtins.str]]
    county: NotRequired[pulumi.Input[_builtins.str]]
    postal_code: NotRequired[pulumi.Input[_builtins.str]]
    province: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ProfileShippingAddressArgs:
    def __init__(
        __self__,
        *,
        address1: Optional[pulumi.Input[_builtins.str]] = ...,
        address2: Optional[pulumi.Input[_builtins.str]] = ...,
        address3: Optional[pulumi.Input[_builtins.str]] = ...,
        address4: Optional[pulumi.Input[_builtins.str]] = ...,
        city: Optional[pulumi.Input[_builtins.str]] = ...,
        country: Optional[pulumi.Input[_builtins.str]] = ...,
        county: Optional[pulumi.Input[_builtins.str]] = ...,
        postal_code: Optional[pulumi.Input[_builtins.str]] = ...,
        province: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def address1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address1.setter
    def address1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address2.setter
    def address2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address3(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address3.setter
    def address3(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def address4(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @address4.setter
    def address4(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @city.setter
    def city(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def country(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @country.setter
    def country(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def county(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @county.setter
    def county(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def province(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @province.setter
    def province(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
