import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ContainerServiceArgs", "ContainerService"]

@pulumi.input_type
class ContainerServiceArgs:
    def __init__(
        __self__,
        *,
        power: pulumi.Input[_builtins.str],
        scale: pulumi.Input[_builtins.int],
        is_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_registry_access: Optional[
            pulumi.Input[ContainerServicePrivateRegistryAccessArgs]
        ] = ...,
        public_domain_names: Optional[
            pulumi.Input[ContainerServicePublicDomainNamesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def power(self) -> pulumi.Input[_builtins.str]: ...
    @power.setter
    def power(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> pulumi.Input[_builtins.int]: ...
    @scale.setter
    def scale(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_disabled.setter
    def is_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccess")
    def private_registry_access(
        self,
    ) -> Optional[pulumi.Input[ContainerServicePrivateRegistryAccessArgs]]: ...
    @private_registry_access.setter
    def private_registry_access(
        self, value: Optional[pulumi.Input[ContainerServicePrivateRegistryAccessArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicDomainNames")
    def public_domain_names(
        self,
    ) -> Optional[pulumi.Input[ContainerServicePublicDomainNamesArgs]]: ...
    @public_domain_names.setter
    def public_domain_names(
        self, value: Optional[pulumi.Input[ContainerServicePublicDomainNamesArgs]]
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
class _ContainerServiceState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        is_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        power: Optional[pulumi.Input[_builtins.str]] = ...,
        power_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        private_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_registry_access: Optional[
            pulumi.Input[ContainerServicePrivateRegistryAccessArgs]
        ] = ...,
        public_domain_names: Optional[
            pulumi.Input[ContainerServicePublicDomainNamesArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_disabled.setter
    def is_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def power(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @power.setter
    def power(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="powerId")
    def power_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @power_id.setter
    def power_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @principal_arn.setter
    def principal_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateDomainName")
    def private_domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_domain_name.setter
    def private_domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccess")
    def private_registry_access(
        self,
    ) -> Optional[pulumi.Input[ContainerServicePrivateRegistryAccessArgs]]: ...
    @private_registry_access.setter
    def private_registry_access(
        self, value: Optional[pulumi.Input[ContainerServicePrivateRegistryAccessArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicDomainNames")
    def public_domain_names(
        self,
    ) -> Optional[pulumi.Input[ContainerServicePublicDomainNamesArgs]]: ...
    @public_domain_names.setter
    def public_domain_names(
        self, value: Optional[pulumi.Input[ContainerServicePublicDomainNamesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @scale.setter
    def scale(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:lightsail/containerService:ContainerService")
class ContainerService(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        is_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        power: Optional[pulumi.Input[_builtins.str]] = ...,
        private_registry_access: Optional[
            pulumi.Input[
                Union[
                    ContainerServicePrivateRegistryAccessArgs,
                    ContainerServicePrivateRegistryAccessArgsDict,
                ]
            ]
        ] = ...,
        public_domain_names: Optional[
            pulumi.Input[
                Union[
                    ContainerServicePublicDomainNamesArgs,
                    ContainerServicePublicDomainNamesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ContainerServiceArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        availability_zone: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        is_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        power: Optional[pulumi.Input[_builtins.str]] = ...,
        power_id: Optional[pulumi.Input[_builtins.str]] = ...,
        principal_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        private_domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        private_registry_access: Optional[
            pulumi.Input[
                Union[
                    ContainerServicePrivateRegistryAccessArgs,
                    ContainerServicePrivateRegistryAccessArgsDict,
                ]
            ]
        ] = ...,
        public_domain_names: Optional[
            pulumi.Input[
                Union[
                    ContainerServicePublicDomainNamesArgs,
                    ContainerServicePublicDomainNamesArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_type: Optional[pulumi.Input[_builtins.str]] = ...,
        scale: Optional[pulumi.Input[_builtins.int]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ContainerService: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def power(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="powerId")
    def power_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateDomainName")
    def private_domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="privateRegistryAccess")
    def private_registry_access(
        self,
    ) -> pulumi.Output[outputs.ContainerServicePrivateRegistryAccess]: ...
    @_builtins.property
    @pulumi.getter(name="publicDomainNames")
    def public_domain_names(
        self,
    ) -> pulumi.Output[Optional[outputs.ContainerServicePublicDomainNames]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scale(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[_builtins.str]: ...
