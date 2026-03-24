import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RepositoryArgs", "Repository"]

@pulumi.input_type
class RepositoryArgs:
    def __init__(
        __self__,
        *,
        encryption_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepositoryEncryptionConfigurationArgs]]]
        ] = ...,
        force_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[RepositoryImageScanningConfigurationArgs]
        ] = ...,
        image_tag_mutability: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag_mutability_exclusion_filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RepositoryImageTagMutabilityExclusionFilterArgs]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RepositoryEncryptionConfigurationArgs]]]
    ]: ...
    @encryption_configurations.setter
    def encryption_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepositoryEncryptionConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> Optional[pulumi.Input[RepositoryImageScanningConfigurationArgs]]: ...
    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self, value: Optional[pulumi.Input[RepositoryImageScanningConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_tag_mutability.setter
    def image_tag_mutability(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutabilityExclusionFilters")
    def image_tag_mutability_exclusion_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RepositoryImageTagMutabilityExclusionFilterArgs]]
        ]
    ]: ...
    @image_tag_mutability_exclusion_filters.setter
    def image_tag_mutability_exclusion_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RepositoryImageTagMutabilityExclusionFilterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _RepositoryState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configurations: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepositoryEncryptionConfigurationArgs]]]
        ] = ...,
        force_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[RepositoryImageScanningConfigurationArgs]
        ] = ...,
        image_tag_mutability: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag_mutability_exclusion_filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RepositoryImageTagMutabilityExclusionFilterArgs]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_url: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RepositoryEncryptionConfigurationArgs]]]
    ]: ...
    @encryption_configurations.setter
    def encryption_configurations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RepositoryEncryptionConfigurationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_delete.setter
    def force_delete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> Optional[pulumi.Input[RepositoryImageScanningConfigurationArgs]]: ...
    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self, value: Optional[pulumi.Input[RepositoryImageScanningConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_tag_mutability.setter
    def image_tag_mutability(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutabilityExclusionFilters")
    def image_tag_mutability_exclusion_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RepositoryImageTagMutabilityExclusionFilterArgs]]
        ]
    ]: ...
    @image_tag_mutability_exclusion_filters.setter
    def image_tag_mutability_exclusion_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RepositoryImageTagMutabilityExclusionFilterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @registry_id.setter
    def registry_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_url.setter
    def repository_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("aws:ecr/repository:Repository")
class Repository(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        encryption_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryEncryptionConfigurationArgs,
                            RepositoryEncryptionConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        force_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[
                Union[
                    RepositoryImageScanningConfigurationArgs,
                    RepositoryImageScanningConfigurationArgsDict,
                ]
            ]
        ] = ...,
        image_tag_mutability: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag_mutability_exclusion_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryImageTagMutabilityExclusionFilterArgs,
                            RepositoryImageTagMutabilityExclusionFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[RepositoryArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryEncryptionConfigurationArgs,
                            RepositoryEncryptionConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        force_delete: Optional[pulumi.Input[_builtins.bool]] = ...,
        image_scanning_configuration: Optional[
            pulumi.Input[
                Union[
                    RepositoryImageScanningConfigurationArgs,
                    RepositoryImageScanningConfigurationArgsDict,
                ]
            ]
        ] = ...,
        image_tag_mutability: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag_mutability_exclusion_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryImageTagMutabilityExclusionFilterArgs,
                            RepositoryImageTagMutabilityExclusionFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_url: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Repository: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.RepositoryEncryptionConfiguration]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.RepositoryImageScanningConfiguration]]: ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutabilityExclusionFilters")
    def image_tag_mutability_exclusion_filters(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.RepositoryImageTagMutabilityExclusionFilter]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
