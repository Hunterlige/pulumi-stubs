import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict
from .. import iam
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "LifecyclePolicyActionArgs",
    "LifecyclePolicyActionArgsDict",
    "LifecyclePolicyDocumentArgs",
    "LifecyclePolicyDocumentArgsDict",
    "LifecyclePolicyRuleArgs",
    "LifecyclePolicyRuleArgsDict",
    "LifecyclePolicySelectionArgs",
    "LifecyclePolicySelectionArgsDict",
    "PolicyDocumentArgs",
    "PolicyDocumentArgsDict",
    "RegistryScanningConfigurationRuleArgs",
    "RegistryScanningConfigurationRuleArgsDict",
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
    "RepositoryEncryptionConfigurationArgs",
    "RepositoryEncryptionConfigurationArgsDict",
    "RepositoryImageScanningConfigurationArgs",
    "RepositoryImageScanningConfigurationArgsDict",
    "RepositoryImageTagMutabilityExclusionFilterArgs",
    ...,
    "GetLifecyclePolicyDocumentRuleArgs",
    "GetLifecyclePolicyDocumentRuleArgsDict",
    "GetLifecyclePolicyDocumentRuleActionArgs",
    "GetLifecyclePolicyDocumentRuleActionArgsDict",
    "GetLifecyclePolicyDocumentRuleSelectionArgs",
    "GetLifecyclePolicyDocumentRuleSelectionArgsDict",
]

class LifecyclePolicyActionArgsDict(TypedDict):
    type: pulumi.Input[LifecyclePolicyActionType]

@pulumi.input_type
class LifecyclePolicyActionArgs:
    def __init__(
        __self__, *, type: pulumi.Input[LifecyclePolicyActionType]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[LifecyclePolicyActionType]: ...
    @type.setter
    def type(self, value: pulumi.Input[LifecyclePolicyActionType]): ...

class LifecyclePolicyDocumentArgsDict(TypedDict):
    rules: pulumi.Input[Sequence[pulumi.Input[LifecyclePolicyRuleArgsDict]]]

@pulumi.input_type
class LifecyclePolicyDocumentArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[Sequence[pulumi.Input[LifecyclePolicyRuleArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[LifecyclePolicyRuleArgs]]]: ...
    @rules.setter
    def rules(
        self, value: pulumi.Input[Sequence[pulumi.Input[LifecyclePolicyRuleArgs]]]
    ): ...

class LifecyclePolicyRuleArgsDict(TypedDict):
    action: pulumi.Input[LifecyclePolicyActionArgsDict]
    rule_priority: pulumi.Input[_builtins.int]
    selection: pulumi.Input[LifecyclePolicySelectionArgsDict]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LifecyclePolicyRuleArgs:
    def __init__(
        __self__,
        *,
        action: pulumi.Input[LifecyclePolicyActionArgs],
        rule_priority: pulumi.Input[_builtins.int],
        selection: pulumi.Input[LifecyclePolicySelectionArgs],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[LifecyclePolicyActionArgs]: ...
    @action.setter
    def action(self, value: pulumi.Input[LifecyclePolicyActionArgs]): ...
    @_builtins.property
    @pulumi.getter(name="rulePriority")
    def rule_priority(self) -> pulumi.Input[_builtins.int]: ...
    @rule_priority.setter
    def rule_priority(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def selection(self) -> pulumi.Input[LifecyclePolicySelectionArgs]: ...
    @selection.setter
    def selection(self, value: pulumi.Input[LifecyclePolicySelectionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class LifecyclePolicySelectionArgsDict(TypedDict):
    count_number: pulumi.Input[_builtins.int]
    count_type: pulumi.Input[LifecyclePolicyCountType]
    tag_status: pulumi.Input[LifecyclePolicyTagStatus]
    count_unit: NotRequired[pulumi.Input[_builtins.str]]
    tag_prefix_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class LifecyclePolicySelectionArgs:
    def __init__(
        __self__,
        *,
        count_number: pulumi.Input[_builtins.int],
        count_type: pulumi.Input[LifecyclePolicyCountType],
        tag_status: pulumi.Input[LifecyclePolicyTagStatus],
        count_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_prefix_list: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="countNumber")
    def count_number(self) -> pulumi.Input[_builtins.int]: ...
    @count_number.setter
    def count_number(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="countType")
    def count_type(self) -> pulumi.Input[LifecyclePolicyCountType]: ...
    @count_type.setter
    def count_type(self, value: pulumi.Input[LifecyclePolicyCountType]): ...
    @_builtins.property
    @pulumi.getter(name="tagStatus")
    def tag_status(self) -> pulumi.Input[LifecyclePolicyTagStatus]: ...
    @tag_status.setter
    def tag_status(self, value: pulumi.Input[LifecyclePolicyTagStatus]): ...
    @_builtins.property
    @pulumi.getter(name="countUnit")
    def count_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @count_unit.setter
    def count_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagPrefixList")
    def tag_prefix_list(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tag_prefix_list.setter
    def tag_prefix_list(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class PolicyDocumentArgsDict(TypedDict):
    statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgsDict]]]
    version: pulumi.Input[iam.PolicyDocumentVersion]
    id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class PolicyDocumentArgs:
    def __init__(
        __self__,
        *,
        statement: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]],
        version: pulumi.Input[iam.PolicyDocumentVersion],
        id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="Statement")
    def statement(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]: ...
    @statement.setter
    def statement(
        self, value: pulumi.Input[Sequence[pulumi.Input[_iam.PolicyStatementArgs]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="Version")
    def version(self) -> pulumi.Input[iam.PolicyDocumentVersion]: ...
    @version.setter
    def version(self, value: pulumi.Input[iam.PolicyDocumentVersion]): ...
    @_builtins.property
    @pulumi.getter(name="Id")
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RegistryScanningConfigurationRuleArgsDict(TypedDict):
    repository_filters: pulumi.Input[
        Sequence[
            pulumi.Input[RegistryScanningConfigurationRuleRepositoryFilterArgsDict]
        ]
    ]
    scan_frequency: pulumi.Input[_builtins.str]

@pulumi.input_type
class RegistryScanningConfigurationRuleArgs:
    def __init__(
        __self__,
        *,
        repository_filters: pulumi.Input[
            Sequence[
                pulumi.Input[RegistryScanningConfigurationRuleRepositoryFilterArgs]
            ]
        ],
        scan_frequency: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryFilters")
    def repository_filters(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[RegistryScanningConfigurationRuleRepositoryFilterArgs]]
    ]: ...
    @repository_filters.setter
    def repository_filters(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[RegistryScanningConfigurationRuleRepositoryFilterArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="scanFrequency")
    def scan_frequency(self) -> pulumi.Input[_builtins.str]: ...
    @scan_frequency.setter
    def scan_frequency(self, value: pulumi.Input[_builtins.str]): ...

class RegistryScanningConfigurationRuleRepositoryFilterArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]
    filter_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class RegistryScanningConfigurationRuleRepositoryFilterArgs:
    def __init__(
        __self__,
        *,
        filter: pulumi.Input[_builtins.str],
        filter_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input[_builtins.str]: ...
    @filter_type.setter
    def filter_type(self, value: pulumi.Input[_builtins.str]): ...

class ReplicationConfigurationReplicationConfigurationArgsDict(TypedDict):
    rules: pulumi.Input[
        Sequence[
            pulumi.Input[ReplicationConfigurationReplicationConfigurationRuleArgsDict]
        ]
    ]

@pulumi.input_type
class ReplicationConfigurationReplicationConfigurationArgs:
    def __init__(
        __self__,
        *,
        rules: pulumi.Input[
            Sequence[
                pulumi.Input[ReplicationConfigurationReplicationConfigurationRuleArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ReplicationConfigurationReplicationConfigurationRuleArgs]]
    ]: ...
    @rules.setter
    def rules(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[ReplicationConfigurationReplicationConfigurationRuleArgs]
            ]
        ],
    ): ...

class ReplicationConfigurationReplicationConfigurationRuleArgsDict(TypedDict):
    destinations: pulumi.Input[
        Sequence[
            pulumi.Input[
                ReplicationConfigurationReplicationConfigurationRuleDestinationArgsDict
            ]
        ]
    ]
    repository_filters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ReplicationConfigurationReplicationConfigurationRuleRepositoryFilterArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class ReplicationConfigurationReplicationConfigurationRuleArgs:
    def __init__(
        __self__,
        *,
        destinations: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ReplicationConfigurationReplicationConfigurationRuleDestinationArgs
                ]
            ]
        ],
        repository_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ReplicationConfigurationReplicationConfigurationRuleRepositoryFilterArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                ReplicationConfigurationReplicationConfigurationRuleDestinationArgs
            ]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    ReplicationConfigurationReplicationConfigurationRuleDestinationArgs
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="repositoryFilters")
    def repository_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ReplicationConfigurationReplicationConfigurationRuleRepositoryFilterArgs
                ]
            ]
        ]
    ]: ...
    @repository_filters.setter
    def repository_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ReplicationConfigurationReplicationConfigurationRuleRepositoryFilterArgs
                    ]
                ]
            ]
        ],
    ): ...

class ReplicationConfigurationReplicationConfigurationRuleDestinationArgsDict(
    TypedDict
):
    region: pulumi.Input[_builtins.str]
    registry_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ReplicationConfigurationReplicationConfigurationRuleDestinationArgs:
    def __init__(
        __self__,
        *,
        region: pulumi.Input[_builtins.str],
        registry_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Input[_builtins.str]: ...
    @region.setter
    def region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Input[_builtins.str]: ...
    @registry_id.setter
    def registry_id(self, value: pulumi.Input[_builtins.str]): ...

class ReplicationConfigurationReplicationConfigurationRuleRepositoryFilterArgsDict(
    TypedDict
):
    filter: pulumi.Input[_builtins.str]
    filter_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class ReplicationConfigurationReplicationConfigurationRuleRepositoryFilterArgs:
    def __init__(
        __self__,
        *,
        filter: pulumi.Input[_builtins.str],
        filter_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input[_builtins.str]: ...
    @filter_type.setter
    def filter_type(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryCreationTemplateEncryptionConfigurationArgsDict(TypedDict):
    encryption_type: NotRequired[pulumi.Input[_builtins.str]]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RepositoryCreationTemplateEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        encryption_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]
    filter_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgs:
    def __init__(
        __self__,
        *,
        filter: pulumi.Input[_builtins.str],
        filter_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input[_builtins.str]: ...
    @filter_type.setter
    def filter_type(self, value: pulumi.Input[_builtins.str]): ...

class RepositoryEncryptionConfigurationArgsDict(TypedDict):
    encryption_type: NotRequired[pulumi.Input[_builtins.str]]
    kms_key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RepositoryEncryptionConfigurationArgs:
    def __init__(
        __self__,
        *,
        encryption_type: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_type.setter
    def encryption_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RepositoryImageScanningConfigurationArgsDict(TypedDict):
    scan_on_push: pulumi.Input[_builtins.bool]

@pulumi.input_type
class RepositoryImageScanningConfigurationArgs:
    def __init__(__self__, *, scan_on_push: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scanOnPush")
    def scan_on_push(self) -> pulumi.Input[_builtins.bool]: ...
    @scan_on_push.setter
    def scan_on_push(self, value: pulumi.Input[_builtins.bool]): ...

class RepositoryImageTagMutabilityExclusionFilterArgsDict(TypedDict):
    filter: pulumi.Input[_builtins.str]
    filter_type: pulumi.Input[_builtins.str]

@pulumi.input_type
class RepositoryImageTagMutabilityExclusionFilterArgs:
    def __init__(
        __self__,
        *,
        filter: pulumi.Input[_builtins.str],
        filter_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> pulumi.Input[_builtins.str]: ...
    @filter_type.setter
    def filter_type(self, value: pulumi.Input[_builtins.str]): ...

class GetLifecyclePolicyDocumentRuleArgsDict(TypedDict):
    priority: _builtins.int
    selection: GetLifecyclePolicyDocumentRuleSelectionArgsDict
    action: NotRequired[GetLifecyclePolicyDocumentRuleActionArgsDict]
    description: NotRequired[_builtins.str]

@pulumi.input_type
class GetLifecyclePolicyDocumentRuleArgs:
    def __init__(
        __self__,
        *,
        priority: _builtins.int,
        selection: GetLifecyclePolicyDocumentRuleSelectionArgs,
        action: Optional[GetLifecyclePolicyDocumentRuleActionArgs] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @priority.setter
    def priority(self, value: _builtins.int): ...
    @_builtins.property
    @pulumi.getter
    def selection(self) -> GetLifecyclePolicyDocumentRuleSelectionArgs: ...
    @selection.setter
    def selection(self, value: GetLifecyclePolicyDocumentRuleSelectionArgs): ...
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[GetLifecyclePolicyDocumentRuleActionArgs]: ...
    @action.setter
    def action(self, value: Optional[GetLifecyclePolicyDocumentRuleActionArgs]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @description.setter
    def description(self, value: Optional[_builtins.str]): ...

class GetLifecyclePolicyDocumentRuleActionArgsDict(TypedDict):
    type: _builtins.str
    target_storage_class: NotRequired[_builtins.str]

@pulumi.input_type
class GetLifecyclePolicyDocumentRuleActionArgs:
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        target_storage_class: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @type.setter
    def type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="targetStorageClass")
    def target_storage_class(self) -> Optional[_builtins.str]: ...
    @target_storage_class.setter
    def target_storage_class(self, value: Optional[_builtins.str]): ...

class GetLifecyclePolicyDocumentRuleSelectionArgsDict(TypedDict):
    count_number: _builtins.int
    count_type: _builtins.str
    tag_status: _builtins.str
    count_unit: NotRequired[_builtins.str]
    storage_class: NotRequired[_builtins.str]
    tag_pattern_lists: NotRequired[Sequence[_builtins.str]]
    tag_prefix_lists: NotRequired[Sequence[_builtins.str]]

@pulumi.input_type
class GetLifecyclePolicyDocumentRuleSelectionArgs:
    def __init__(
        __self__,
        *,
        count_number: _builtins.int,
        count_type: _builtins.str,
        tag_status: _builtins.str,
        count_unit: Optional[_builtins.str] = ...,
        storage_class: Optional[_builtins.str] = ...,
        tag_pattern_lists: Optional[Sequence[_builtins.str]] = ...,
        tag_prefix_lists: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="countNumber")
    def count_number(self) -> _builtins.int: ...
    @count_number.setter
    def count_number(self, value: _builtins.int): ...
    @_builtins.property
    @pulumi.getter(name="countType")
    def count_type(self) -> _builtins.str: ...
    @count_type.setter
    def count_type(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="tagStatus")
    def tag_status(self) -> _builtins.str: ...
    @tag_status.setter
    def tag_status(self, value: _builtins.str): ...
    @_builtins.property
    @pulumi.getter(name="countUnit")
    def count_unit(self) -> Optional[_builtins.str]: ...
    @count_unit.setter
    def count_unit(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]: ...
    @storage_class.setter
    def storage_class(self, value: Optional[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tagPatternLists")
    def tag_pattern_lists(self) -> Optional[Sequence[_builtins.str]]: ...
    @tag_pattern_lists.setter
    def tag_pattern_lists(self, value: Optional[Sequence[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagPrefixLists")
    def tag_prefix_lists(self) -> Optional[Sequence[_builtins.str]]: ...
    @tag_prefix_lists.setter
    def tag_prefix_lists(self, value: Optional[Sequence[_builtins.str]]): ...
