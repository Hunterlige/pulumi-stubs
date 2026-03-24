import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "RegistryScanningConfigurationRule",
    "RegistryScanningConfigurationRuleRepositoryFilter",
    "ReplicationConfigurationReplicationConfiguration",
    ...,
    ...,
    ...,
    "RepositoryCreationTemplateEncryptionConfiguration",
    ...,
    "RepositoryEncryptionConfiguration",
    "RepositoryImageScanningConfiguration",
    "RepositoryImageTagMutabilityExclusionFilter",
    "GetImagesImageIdResult",
    "GetLifecyclePolicyDocumentRuleResult",
    "GetLifecyclePolicyDocumentRuleActionResult",
    "GetLifecyclePolicyDocumentRuleSelectionResult",
    ...,
    ...,
    "GetRepositoryEncryptionConfigurationResult",
    "GetRepositoryImageScanningConfigurationResult",
    ...,
]

@pulumi.output_type
class RegistryScanningConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        repository_filters: Sequence[
            outputs.RegistryScanningConfigurationRuleRepositoryFilter
        ],
        scan_frequency: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repositoryFilters")
    def repository_filters(
        self,
    ) -> Sequence[outputs.RegistryScanningConfigurationRuleRepositoryFilter]: ...
    @_builtins.property
    @pulumi.getter(name="scanFrequency")
    def scan_frequency(self) -> _builtins.str: ...

@pulumi.output_type
class RegistryScanningConfigurationRuleRepositoryFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter: _builtins.str, filter_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> _builtins.str: ...

@pulumi.output_type
class ReplicationConfigurationReplicationConfiguration(dict):
    def __init__(
        __self__,
        *,
        rules: Sequence[outputs.ReplicationConfigurationReplicationConfigurationRule],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Sequence[outputs.ReplicationConfigurationReplicationConfigurationRule]: ...

@pulumi.output_type
class ReplicationConfigurationReplicationConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destinations: Sequence[
            outputs.ReplicationConfigurationReplicationConfigurationRuleDestination
        ],
        repository_filters: Optional[
            Sequence[
                outputs.ReplicationConfigurationReplicationConfigurationRuleRepositoryFilter
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Sequence[
        outputs.ReplicationConfigurationReplicationConfigurationRuleDestination
    ]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryFilters")
    def repository_filters(
        self,
    ) -> Optional[
        Sequence[
            outputs.ReplicationConfigurationReplicationConfigurationRuleRepositoryFilter
        ]
    ]: ...

@pulumi.output_type
class ReplicationConfigurationReplicationConfigurationRuleDestination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, region: _builtins.str, registry_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> _builtins.str: ...

@pulumi.output_type
class ReplicationConfigurationReplicationConfigurationRuleRepositoryFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter: _builtins.str, filter_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> _builtins.str: ...

@pulumi.output_type
class RepositoryCreationTemplateEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_type: Optional[_builtins.str] = ...,
        kms_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RepositoryCreationTemplateImageTagMutabilityExclusionFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter: _builtins.str, filter_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> _builtins.str: ...

@pulumi.output_type
class RepositoryEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        encryption_type: Optional[_builtins.str] = ...,
        kms_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RepositoryImageScanningConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, scan_on_push: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scanOnPush")
    def scan_on_push(self) -> _builtins.bool: ...

@pulumi.output_type
class RepositoryImageTagMutabilityExclusionFilter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, filter: _builtins.str, filter_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetImagesImageIdResult(dict):
    def __init__(
        __self__, *, image_digest: _builtins.str, image_tag: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="imageDigest")
    def image_digest(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="imageTag")
    def image_tag(self) -> _builtins.str: ...

@pulumi.output_type
class GetLifecyclePolicyDocumentRuleResult(dict):
    def __init__(
        __self__,
        *,
        priority: _builtins.int,
        selection: outputs.GetLifecyclePolicyDocumentRuleSelectionResult,
        action: Optional[outputs.GetLifecyclePolicyDocumentRuleActionResult] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def selection(self) -> outputs.GetLifecyclePolicyDocumentRuleSelectionResult: ...
    @_builtins.property
    @pulumi.getter
    def action(
        self,
    ) -> Optional[outputs.GetLifecyclePolicyDocumentRuleActionResult]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetLifecyclePolicyDocumentRuleActionResult(dict):
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        target_storage_class: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="targetStorageClass")
    def target_storage_class(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetLifecyclePolicyDocumentRuleSelectionResult(dict):
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
    @_builtins.property
    @pulumi.getter(name="countType")
    def count_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagStatus")
    def tag_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="countUnit")
    def count_unit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagPatternLists")
    def tag_pattern_lists(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tagPrefixLists")
    def tag_prefix_lists(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class GetRepositoryCreationTemplateEncryptionConfigurationResult(dict):
    def __init__(
        __self__, *, encryption_type: _builtins.str, kms_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetRepositoryCreationTemplateImageTagMutabilityExclusionFilterResult(dict):
    def __init__(
        __self__, *, filter: _builtins.str, filter_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetRepositoryEncryptionConfigurationResult(dict):
    def __init__(
        __self__, *, encryption_type: _builtins.str, kms_key: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str: ...

@pulumi.output_type
class GetRepositoryImageScanningConfigurationResult(dict):
    def __init__(__self__, *, scan_on_push: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scanOnPush")
    def scan_on_push(self) -> _builtins.bool: ...

@pulumi.output_type
class GetRepositoryImageTagMutabilityExclusionFilterResult(dict):
    def __init__(
        __self__, *, filter: _builtins.str, filter_type: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="filterType")
    def filter_type(self) -> _builtins.str: ...
