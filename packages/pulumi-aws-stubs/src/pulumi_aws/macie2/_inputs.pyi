import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ClassificationExportConfigurationS3DestinationArgs",
    ...,
    "ClassificationJobS3JobDefinitionArgs",
    "ClassificationJobS3JobDefinitionArgsDict",
    "ClassificationJobS3JobDefinitionBucketCriteriaArgs",
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
    ...,
    "ClassificationJobS3JobDefinitionScopingArgs",
    "ClassificationJobS3JobDefinitionScopingArgsDict",
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
    "ClassificationJobScheduleFrequencyArgs",
    "ClassificationJobScheduleFrequencyArgsDict",
    "ClassificationJobUserPausedDetailArgs",
    "ClassificationJobUserPausedDetailArgsDict",
]

class ClassificationExportConfigurationS3DestinationArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    kms_key_arn: pulumi.Input[_builtins.str]
    key_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClassificationExportConfigurationS3DestinationArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        kms_key_arn: pulumi.Input[_builtins.str],
        key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_prefix.setter
    def key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClassificationJobS3JobDefinitionArgsDict(TypedDict):
    bucket_criteria: NotRequired[
        pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaArgsDict]
    ]
    bucket_definitions: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClassificationJobS3JobDefinitionBucketDefinitionArgsDict]
            ]
        ]
    ]
    scoping: NotRequired[pulumi.Input[ClassificationJobS3JobDefinitionScopingArgsDict]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionArgs:
    def __init__(
        __self__,
        *,
        bucket_criteria: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaArgs]
        ] = ...,
        bucket_definitions: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClassificationJobS3JobDefinitionBucketDefinitionArgs]
                ]
            ]
        ] = ...,
        scoping: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionScopingArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketCriteria")
    def bucket_criteria(
        self,
    ) -> Optional[pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaArgs]]: ...
    @bucket_criteria.setter
    def bucket_criteria(
        self,
        value: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bucketDefinitions")
    def bucket_definitions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ClassificationJobS3JobDefinitionBucketDefinitionArgs]]
        ]
    ]: ...
    @bucket_definitions.setter
    def bucket_definitions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClassificationJobS3JobDefinitionBucketDefinitionArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def scoping(
        self,
    ) -> Optional[pulumi.Input[ClassificationJobS3JobDefinitionScopingArgs]]: ...
    @scoping.setter
    def scoping(
        self, value: Optional[pulumi.Input[ClassificationJobS3JobDefinitionScopingArgs]]
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaArgsDict(TypedDict):
    excludes: NotRequired[
        pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaExcludesArgsDict]
    ]
    includes: NotRequired[
        pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaIncludesArgsDict]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaExcludesArgs]
        ] = ...,
        includes: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaIncludesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[
        pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaExcludesArgs]
    ]: ...
    @excludes.setter
    def excludes(
        self,
        value: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaExcludesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[
        pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaIncludesArgs]
    ]: ...
    @includes.setter
    def includes(
        self,
        value: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionBucketCriteriaIncludesArgs]
        ],
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaExcludesArgsDict(TypedDict):
    ands: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludesArgs:
    def __init__(
        __self__,
        *,
        ands: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndArgs
                ]
            ]
        ]
    ]: ...
    @ands.setter
    def ands(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndArgsDict(TypedDict):
    simple_criterion: NotRequired[
        pulumi.Input[
            ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionArgsDict
        ]
    ]
    tag_criterion: NotRequired[
        pulumi.Input[
            ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndArgs:
    def __init__(
        __self__,
        *,
        simple_criterion: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionArgs
            ]
        ] = ...,
        tag_criterion: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="simpleCriterion")
    def simple_criterion(
        self,
    ) -> Optional[
        pulumi.Input[
            ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionArgs
        ]
    ]: ...
    @simple_criterion.setter
    def simple_criterion(
        self,
        value: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagCriterion")
    def tag_criterion(
        self,
    ) -> Optional[
        pulumi.Input[
            ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionArgs
        ]
    ]: ...
    @tag_criterion.setter
    def tag_criterion(
        self,
        value: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionArgs
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionArgsDict(
    TypedDict
):
    comparator: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndSimpleCriterionArgs:
    def __init__(
        __self__,
        *,
        comparator: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comparator.setter
    def comparator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionArgsDict(
    TypedDict
):
    comparator: NotRequired[pulumi.Input[_builtins.str]]
    tag_values: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValueArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionArgs:
    def __init__(
        __self__,
        *,
        comparator: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_values: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValueArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comparator.setter
    def comparator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValueArgs
                ]
            ]
        ]
    ]: ...
    @tag_values.setter
    def tag_values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValueArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValueArgsDict(
    TypedDict
):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaExcludesAndTagCriterionTagValueArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClassificationJobS3JobDefinitionBucketCriteriaIncludesArgsDict(TypedDict):
    ands: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludesArgs:
    def __init__(
        __self__,
        *,
        ands: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndArgs
                ]
            ]
        ]
    ]: ...
    @ands.setter
    def ands(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndArgsDict(TypedDict):
    simple_criterion: NotRequired[
        pulumi.Input[
            ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionArgsDict
        ]
    ]
    tag_criterion: NotRequired[
        pulumi.Input[
            ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndArgs:
    def __init__(
        __self__,
        *,
        simple_criterion: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionArgs
            ]
        ] = ...,
        tag_criterion: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="simpleCriterion")
    def simple_criterion(
        self,
    ) -> Optional[
        pulumi.Input[
            ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionArgs
        ]
    ]: ...
    @simple_criterion.setter
    def simple_criterion(
        self,
        value: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagCriterion")
    def tag_criterion(
        self,
    ) -> Optional[
        pulumi.Input[
            ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionArgs
        ]
    ]: ...
    @tag_criterion.setter
    def tag_criterion(
        self,
        value: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionArgs
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionArgsDict(
    TypedDict
):
    comparator: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndSimpleCriterionArgs:
    def __init__(
        __self__,
        *,
        comparator: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comparator.setter
    def comparator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionArgsDict(
    TypedDict
):
    comparator: NotRequired[pulumi.Input[_builtins.str]]
    tag_values: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValueArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionArgs:
    def __init__(
        __self__,
        *,
        comparator: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_values: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValueArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comparator.setter
    def comparator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValueArgs
                ]
            ]
        ]
    ]: ...
    @tag_values.setter
    def tag_values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValueArgs
                    ]
                ]
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValueArgsDict(
    TypedDict
):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketCriteriaIncludesAndTagCriterionTagValueArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClassificationJobS3JobDefinitionBucketDefinitionArgsDict(TypedDict):
    account_id: pulumi.Input[_builtins.str]
    buckets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionBucketDefinitionArgs:
    def __init__(
        __self__,
        *,
        account_id: pulumi.Input[_builtins.str],
        buckets: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[_builtins.str]: ...
    @account_id.setter
    def account_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def buckets(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @buckets.setter
    def buckets(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class ClassificationJobS3JobDefinitionScopingArgsDict(TypedDict):
    excludes: NotRequired[
        pulumi.Input[ClassificationJobS3JobDefinitionScopingExcludesArgsDict]
    ]
    includes: NotRequired[
        pulumi.Input[ClassificationJobS3JobDefinitionScopingIncludesArgsDict]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingArgs:
    def __init__(
        __self__,
        *,
        excludes: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionScopingExcludesArgs]
        ] = ...,
        includes: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionScopingIncludesArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def excludes(
        self,
    ) -> Optional[
        pulumi.Input[ClassificationJobS3JobDefinitionScopingExcludesArgs]
    ]: ...
    @excludes.setter
    def excludes(
        self,
        value: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionScopingExcludesArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def includes(
        self,
    ) -> Optional[
        pulumi.Input[ClassificationJobS3JobDefinitionScopingIncludesArgs]
    ]: ...
    @includes.setter
    def includes(
        self,
        value: Optional[
            pulumi.Input[ClassificationJobS3JobDefinitionScopingIncludesArgs]
        ],
    ): ...

class ClassificationJobS3JobDefinitionScopingExcludesArgsDict(TypedDict):
    ands: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClassificationJobS3JobDefinitionScopingExcludesAndArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingExcludesArgs:
    def __init__(
        __self__,
        *,
        ands: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClassificationJobS3JobDefinitionScopingExcludesAndArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClassificationJobS3JobDefinitionScopingExcludesAndArgs]
            ]
        ]
    ]: ...
    @ands.setter
    def ands(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClassificationJobS3JobDefinitionScopingExcludesAndArgs]
                ]
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionScopingExcludesAndArgsDict(TypedDict):
    simple_scope_term: NotRequired[
        pulumi.Input[
            ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermArgsDict
        ]
    ]
    tag_scope_term: NotRequired[
        pulumi.Input[
            ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingExcludesAndArgs:
    def __init__(
        __self__,
        *,
        simple_scope_term: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermArgs
            ]
        ] = ...,
        tag_scope_term: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="simpleScopeTerm")
    def simple_scope_term(
        self,
    ) -> Optional[
        pulumi.Input[
            ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermArgs
        ]
    ]: ...
    @simple_scope_term.setter
    def simple_scope_term(
        self,
        value: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagScopeTerm")
    def tag_scope_term(
        self,
    ) -> Optional[
        pulumi.Input[ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermArgs]
    ]: ...
    @tag_scope_term.setter
    def tag_scope_term(
        self,
        value: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermArgs
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermArgsDict(
    TypedDict
):
    comparator: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingExcludesAndSimpleScopeTermArgs:
    def __init__(
        __self__,
        *,
        comparator: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comparator.setter
    def comparator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermArgsDict(TypedDict):
    comparator: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    tag_values: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValueArgsDict
                ]
            ]
        ]
    ]
    target: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermArgs:
    def __init__(
        __self__,
        *,
        comparator: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_values: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValueArgs
                    ]
                ]
            ]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comparator.setter
    def comparator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValueArgs
                ]
            ]
        ]
    ]: ...
    @tag_values.setter
    def tag_values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValueArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValueArgsDict(
    TypedDict
):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingExcludesAndTagScopeTermTagValueArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClassificationJobS3JobDefinitionScopingIncludesArgsDict(TypedDict):
    ands: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClassificationJobS3JobDefinitionScopingIncludesAndArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingIncludesArgs:
    def __init__(
        __self__,
        *,
        ands: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClassificationJobS3JobDefinitionScopingIncludesAndArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ands(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ClassificationJobS3JobDefinitionScopingIncludesAndArgs]
            ]
        ]
    ]: ...
    @ands.setter
    def ands(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ClassificationJobS3JobDefinitionScopingIncludesAndArgs]
                ]
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionScopingIncludesAndArgsDict(TypedDict):
    simple_scope_term: NotRequired[
        pulumi.Input[
            ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermArgsDict
        ]
    ]
    tag_scope_term: NotRequired[
        pulumi.Input[
            ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingIncludesAndArgs:
    def __init__(
        __self__,
        *,
        simple_scope_term: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermArgs
            ]
        ] = ...,
        tag_scope_term: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="simpleScopeTerm")
    def simple_scope_term(
        self,
    ) -> Optional[
        pulumi.Input[
            ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermArgs
        ]
    ]: ...
    @simple_scope_term.setter
    def simple_scope_term(
        self,
        value: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagScopeTerm")
    def tag_scope_term(
        self,
    ) -> Optional[
        pulumi.Input[ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermArgs]
    ]: ...
    @tag_scope_term.setter
    def tag_scope_term(
        self,
        value: Optional[
            pulumi.Input[
                ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermArgs
            ]
        ],
    ): ...

class ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermArgsDict(
    TypedDict
):
    comparator: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    values: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingIncludesAndSimpleScopeTermArgs:
    def __init__(
        __self__,
        *,
        comparator: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        values: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comparator.setter
    def comparator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def values(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @values.setter
    def values(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermArgsDict(TypedDict):
    comparator: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    tag_values: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValueArgsDict
                ]
            ]
        ]
    ]
    target: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermArgs:
    def __init__(
        __self__,
        *,
        comparator: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_values: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValueArgs
                    ]
                ]
            ]
        ] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @comparator.setter
    def comparator(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagValues")
    def tag_values(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValueArgs
                ]
            ]
        ]
    ]: ...
    @tag_values.setter
    def tag_values(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValueArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValueArgsDict(
    TypedDict
):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClassificationJobS3JobDefinitionScopingIncludesAndTagScopeTermTagValueArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClassificationJobScheduleFrequencyArgsDict(TypedDict):
    daily_schedule: NotRequired[pulumi.Input[_builtins.bool]]
    monthly_schedule: NotRequired[pulumi.Input[_builtins.int]]
    weekly_schedule: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClassificationJobScheduleFrequencyArgs:
    def __init__(
        __self__,
        *,
        daily_schedule: Optional[pulumi.Input[_builtins.bool]] = ...,
        monthly_schedule: Optional[pulumi.Input[_builtins.int]] = ...,
        weekly_schedule: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dailySchedule")
    def daily_schedule(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @daily_schedule.setter
    def daily_schedule(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="monthlySchedule")
    def monthly_schedule(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @monthly_schedule.setter
    def monthly_schedule(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="weeklySchedule")
    def weekly_schedule(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weekly_schedule.setter
    def weekly_schedule(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ClassificationJobUserPausedDetailArgsDict(TypedDict):
    job_expires_at: NotRequired[pulumi.Input[_builtins.str]]
    job_imminent_expiration_health_event_arn: NotRequired[pulumi.Input[_builtins.str]]
    job_paused_at: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ClassificationJobUserPausedDetailArgs:
    def __init__(
        __self__,
        *,
        job_expires_at: Optional[pulumi.Input[_builtins.str]] = ...,
        job_imminent_expiration_health_event_arn: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        job_paused_at: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobExpiresAt")
    def job_expires_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_expires_at.setter
    def job_expires_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobImminentExpirationHealthEventArn")
    def job_imminent_expiration_health_event_arn(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_imminent_expiration_health_event_arn.setter
    def job_imminent_expiration_health_event_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobPausedAt")
    def job_paused_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_paused_at.setter
    def job_paused_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
