import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RepositoryAssociationArgs", "RepositoryAssociation"]

@pulumi.input_type
class RepositoryAssociationArgs:
    def __init__(
        __self__,
        *,
        repository: pulumi.Input[RepositoryAssociationRepositoryArgs],
        kms_key_details: Optional[
            pulumi.Input[RepositoryAssociationKmsKeyDetailsArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Input[RepositoryAssociationRepositoryArgs]: ...
    @repository.setter
    def repository(self, value: pulumi.Input[RepositoryAssociationRepositoryArgs]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyDetails")
    def kms_key_details(
        self,
    ) -> Optional[pulumi.Input[RepositoryAssociationKmsKeyDetailsArgs]]: ...
    @kms_key_details.setter
    def kms_key_details(
        self, value: Optional[pulumi.Input[RepositoryAssociationKmsKeyDetailsArgs]]
    ): ...
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
class _RepositoryAssociationState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_details: Optional[
            pulumi.Input[RepositoryAssociationKmsKeyDetailsArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[pulumi.Input[RepositoryAssociationRepositoryArgs]] = ...,
        s3_repository_details: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RepositoryAssociationS3RepositoryDetailArgs]]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_reason: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter(name="associationId")
    def association_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @association_id.setter
    def association_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connection_arn.setter
    def connection_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyDetails")
    def kms_key_details(
        self,
    ) -> Optional[pulumi.Input[RepositoryAssociationKmsKeyDetailsArgs]]: ...
    @kms_key_details.setter
    def kms_key_details(
        self, value: Optional[pulumi.Input[RepositoryAssociationKmsKeyDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @owner.setter
    def owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_type.setter
    def provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def repository(
        self,
    ) -> Optional[pulumi.Input[RepositoryAssociationRepositoryArgs]]: ...
    @repository.setter
    def repository(
        self, value: Optional[pulumi.Input[RepositoryAssociationRepositoryArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3RepositoryDetails")
    def s3_repository_details(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[RepositoryAssociationS3RepositoryDetailArgs]]
        ]
    ]: ...
    @s3_repository_details.setter
    def s3_repository_details(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[RepositoryAssociationS3RepositoryDetailArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state_reason.setter
    def state_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token(...)
class RepositoryAssociation(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        kms_key_details: Optional[
            pulumi.Input[
                Union[
                    RepositoryAssociationKmsKeyDetailsArgs,
                    RepositoryAssociationKmsKeyDetailsArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[
            pulumi.Input[
                Union[
                    RepositoryAssociationRepositoryArgs,
                    RepositoryAssociationRepositoryArgsDict,
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: RepositoryAssociationArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        association_id: Optional[pulumi.Input[_builtins.str]] = ...,
        connection_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_details: Optional[
            pulumi.Input[
                Union[
                    RepositoryAssociationKmsKeyDetailsArgs,
                    RepositoryAssociationKmsKeyDetailsArgsDict,
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        owner: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_type: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        repository: Optional[
            pulumi.Input[
                Union[
                    RepositoryAssociationRepositoryArgs,
                    RepositoryAssociationRepositoryArgsDict,
                ]
            ]
        ] = ...,
        s3_repository_details: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RepositoryAssociationS3RepositoryDetailArgs,
                            RepositoryAssociationS3RepositoryDetailArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        state_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> RepositoryAssociation: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="associationId")
    def association_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyDetails")
    def kms_key_details(
        self,
    ) -> pulumi.Output[Optional[outputs.RepositoryAssociationKmsKeyDetails]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def owner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Output[outputs.RepositoryAssociationRepository]: ...
    @_builtins.property
    @pulumi.getter(name="s3RepositoryDetails")
    def s3_repository_details(
        self,
    ) -> pulumi.Output[Sequence[outputs.RepositoryAssociationS3RepositoryDetail]]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
