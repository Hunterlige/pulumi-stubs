import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RepositoryCreationTemplateArgs", "RepositoryCreationTemplate"]

@pulumi.input_type
class RepositoryCreationTemplateArgs:
    def __init__(
        __self__,
        *,
        applied_fors: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        prefix: pulumi.Input[_builtins.str],
        custom_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RepositoryCreationTemplateEncryptionConfigurationArgs]
                ]
            ]
        ] = ...,
        image_tag_mutability: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag_mutability_exclusion_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgs
                    ]
                ]
            ]
        ] = ...,
        lifecycle_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appliedFors")
    def applied_fors(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @applied_fors.setter
    def applied_fors(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[_builtins.str]: ...
    @prefix.setter
    def prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customRoleArn")
    def custom_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_role_arn.setter
    def custom_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RepositoryCreationTemplateEncryptionConfigurationArgs]
            ]
        ]
    ]: ...
    @encryption_configurations.setter
    def encryption_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RepositoryCreationTemplateEncryptionConfigurationArgs]
                ]
            ]
        ],
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
            Sequence[
                pulumi.Input[
                    RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgs
                ]
            ]
        ]
    ]: ...
    @image_tag_mutability_exclusion_filters.setter
    def image_tag_mutability_exclusion_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecyclePolicy")
    def lifecycle_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_policy.setter
    def lifecycle_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repositoryPolicy")
    def repository_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_policy.setter
    def repository_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_tags.setter
    def resource_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _RepositoryCreationTemplateState:
    def __init__(
        __self__,
        *,
        applied_fors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RepositoryCreationTemplateEncryptionConfigurationArgs]
                ]
            ]
        ] = ...,
        image_tag_mutability: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag_mutability_exclusion_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgs
                    ]
                ]
            ]
        ] = ...,
        lifecycle_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appliedFors")
    def applied_fors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @applied_fors.setter
    def applied_fors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customRoleArn")
    def custom_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_role_arn.setter
    def custom_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[RepositoryCreationTemplateEncryptionConfigurationArgs]
            ]
        ]
    ]: ...
    @encryption_configurations.setter
    def encryption_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[RepositoryCreationTemplateEncryptionConfigurationArgs]
                ]
            ]
        ],
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
            Sequence[
                pulumi.Input[
                    RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgs
                ]
            ]
        ]
    ]: ...
    @image_tag_mutability_exclusion_filters.setter
    def image_tag_mutability_exclusion_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lifecyclePolicy")
    def lifecycle_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lifecycle_policy.setter
    def lifecycle_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter(name="repositoryPolicy")
    def repository_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repository_policy.setter
    def repository_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @resource_tags.setter
    def resource_tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token(...)
class RepositoryCreationTemplate(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        applied_fors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryCreationTemplateEncryptionConfigurationArgs,
                            RepositoryCreationTemplateEncryptionConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        image_tag_mutability: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag_mutability_exclusion_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgs,
                            RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        lifecycle_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RepositoryCreationTemplateArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        applied_fors: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        custom_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryCreationTemplateEncryptionConfigurationArgs,
                            RepositoryCreationTemplateEncryptionConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        image_tag_mutability: Optional[pulumi.Input[_builtins.str]] = ...,
        image_tag_mutability_exclusion_filters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgs,
                            RepositoryCreationTemplateImageTagMutabilityExclusionFilterArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        lifecycle_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        registry_id: Optional[pulumi.Input[_builtins.str]] = ...,
        repository_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_tags: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> RepositoryCreationTemplate: ...
    @_builtins.property
    @pulumi.getter(name="appliedFors")
    def applied_fors(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customRoleArn")
    def custom_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="encryptionConfigurations")
    def encryption_configurations(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.RepositoryCreationTemplateEncryptionConfiguration]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutability")
    def image_tag_mutability(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="imageTagMutabilityExclusionFilters")
    def image_tag_mutability_exclusion_filters(
        self,
    ) -> pulumi.Output[
        Optional[
            Sequence[
                outputs.RepositoryCreationTemplateImageTagMutabilityExclusionFilter
            ]
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lifecyclePolicy")
    def lifecycle_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryPolicy")
    def repository_policy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
