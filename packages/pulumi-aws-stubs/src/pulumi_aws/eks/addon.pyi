import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AddonArgs", "Addon"]

@pulumi.input_type
class AddonArgs:
    def __init__(
        __self__,
        *,
        addon_name: pulumi.Input[_builtins.str],
        cluster_name: pulumi.Input[_builtins.str],
        addon_version: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_values: Optional[pulumi.Input[_builtins.str]] = ...,
        pod_identity_associations: Optional[
            pulumi.Input[Sequence[pulumi.Input[AddonPodIdentityAssociationArgs]]]
        ] = ...,
        preserve: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_conflicts_on_create: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_conflicts_on_update: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> pulumi.Input[_builtins.str]: ...
    @addon_name.setter
    def addon_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[_builtins.str]: ...
    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="addonVersion")
    def addon_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @addon_version.setter
    def addon_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationValues")
    def configuration_values(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_values.setter
    def configuration_values(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="podIdentityAssociations")
    def pod_identity_associations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AddonPodIdentityAssociationArgs]]]
    ]: ...
    @pod_identity_associations.setter
    def pod_identity_associations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AddonPodIdentityAssociationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def preserve(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preserve.setter
    def preserve(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resolveConflictsOnCreate")
    def resolve_conflicts_on_create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resolve_conflicts_on_create.setter
    def resolve_conflicts_on_create(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resolveConflictsOnUpdate")
    def resolve_conflicts_on_update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resolve_conflicts_on_update.setter
    def resolve_conflicts_on_update(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountRoleArn")
    def service_account_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_role_arn.setter
    def service_account_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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
class _AddonState:
    def __init__(
        __self__,
        *,
        addon_name: Optional[pulumi.Input[_builtins.str]] = ...,
        addon_version: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_values: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        modified_at: Optional[pulumi.Input[_builtins.str]] = ...,
        pod_identity_associations: Optional[
            pulumi.Input[Sequence[pulumi.Input[AddonPodIdentityAssociationArgs]]]
        ] = ...,
        preserve: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_conflicts_on_create: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_conflicts_on_update: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @addon_name.setter
    def addon_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="addonVersion")
    def addon_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @addon_version.setter
    def addon_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="configurationValues")
    def configuration_values(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @configuration_values.setter
    def configuration_values(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @modified_at.setter
    def modified_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="podIdentityAssociations")
    def pod_identity_associations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AddonPodIdentityAssociationArgs]]]
    ]: ...
    @pod_identity_associations.setter
    def pod_identity_associations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AddonPodIdentityAssociationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def preserve(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @preserve.setter
    def preserve(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resolveConflictsOnCreate")
    def resolve_conflicts_on_create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resolve_conflicts_on_create.setter
    def resolve_conflicts_on_create(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resolveConflictsOnUpdate")
    def resolve_conflicts_on_update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resolve_conflicts_on_update.setter
    def resolve_conflicts_on_update(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountRoleArn")
    def service_account_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_role_arn.setter
    def service_account_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
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

@pulumi.type_token("aws:eks/addon:Addon")
class Addon(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        addon_name: Optional[pulumi.Input[_builtins.str]] = ...,
        addon_version: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_values: Optional[pulumi.Input[_builtins.str]] = ...,
        pod_identity_associations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AddonPodIdentityAssociationArgs,
                            AddonPodIdentityAssociationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        preserve: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_conflicts_on_create: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_conflicts_on_update: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AddonArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        addon_name: Optional[pulumi.Input[_builtins.str]] = ...,
        addon_version: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        cluster_name: Optional[pulumi.Input[_builtins.str]] = ...,
        configuration_values: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        modified_at: Optional[pulumi.Input[_builtins.str]] = ...,
        pod_identity_associations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AddonPodIdentityAssociationArgs,
                            AddonPodIdentityAssociationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        preserve: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_conflicts_on_create: Optional[pulumi.Input[_builtins.str]] = ...,
        resolve_conflicts_on_update: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> Addon: ...
    @_builtins.property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="addonVersion")
    def addon_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="configurationValues")
    def configuration_values(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="podIdentityAssociations")
    def pod_identity_associations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.AddonPodIdentityAssociation]]]: ...
    @_builtins.property
    @pulumi.getter
    def preserve(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resolveConflictsOnCreate")
    def resolve_conflicts_on_create(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resolveConflictsOnUpdate")
    def resolve_conflicts_on_update(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountRoleArn")
    def service_account_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
