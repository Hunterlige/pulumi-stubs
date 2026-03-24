import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccessGrantArgs", "AccessGrant"]

@pulumi.input_type
class AccessGrantArgs:
    def __init__(
        __self__,
        *,
        access_grants_location_id: pulumi.Input[_builtins.str],
        grantee: pulumi.Input[AccessGrantGranteeArgs],
        permission: pulumi.Input[_builtins.str],
        access_grants_location_configuration: Optional[
            pulumi.Input[AccessGrantAccessGrantsLocationConfigurationArgs]
        ] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_prefix_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessGrantsLocationId")
    def access_grants_location_id(self) -> pulumi.Input[_builtins.str]: ...
    @access_grants_location_id.setter
    def access_grants_location_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> pulumi.Input[AccessGrantGranteeArgs]: ...
    @grantee.setter
    def grantee(self, value: pulumi.Input[AccessGrantGranteeArgs]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Input[_builtins.str]: ...
    @permission.setter
    def permission(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessGrantsLocationConfiguration")
    def access_grants_location_configuration(
        self,
    ) -> Optional[pulumi.Input[AccessGrantAccessGrantsLocationConfigurationArgs]]: ...
    @access_grants_location_configuration.setter
    def access_grants_location_configuration(
        self,
        value: Optional[pulumi.Input[AccessGrantAccessGrantsLocationConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3PrefixType")
    def s3_prefix_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_prefix_type.setter
    def s3_prefix_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
class _AccessGrantState:
    def __init__(
        __self__,
        *,
        access_grant_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        access_grant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        access_grants_location_configuration: Optional[
            pulumi.Input[AccessGrantAccessGrantsLocationConfigurationArgs]
        ] = ...,
        access_grants_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        grantee: Optional[pulumi.Input[AccessGrantGranteeArgs]] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_prefix_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessGrantArn")
    def access_grant_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_grant_arn.setter
    def access_grant_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="accessGrantId")
    def access_grant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_grant_id.setter
    def access_grant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="accessGrantsLocationConfiguration")
    def access_grants_location_configuration(
        self,
    ) -> Optional[pulumi.Input[AccessGrantAccessGrantsLocationConfigurationArgs]]: ...
    @access_grants_location_configuration.setter
    def access_grants_location_configuration(
        self,
        value: Optional[pulumi.Input[AccessGrantAccessGrantsLocationConfigurationArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="accessGrantsLocationId")
    def access_grants_location_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_grants_location_id.setter
    def access_grants_location_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="grantScope")
    def grant_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @grant_scope.setter
    def grant_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> Optional[pulumi.Input[AccessGrantGranteeArgs]]: ...
    @grantee.setter
    def grantee(self, value: Optional[pulumi.Input[AccessGrantGranteeArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @permission.setter
    def permission(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3PrefixType")
    def s3_prefix_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_prefix_type.setter
    def s3_prefix_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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

@pulumi.type_token("aws:s3control/accessGrant:AccessGrant")
class AccessGrant(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_grants_location_configuration: Optional[
            pulumi.Input[
                Union[
                    AccessGrantAccessGrantsLocationConfigurationArgs,
                    AccessGrantAccessGrantsLocationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        access_grants_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        grantee: Optional[
            pulumi.Input[Union[AccessGrantGranteeArgs, AccessGrantGranteeArgsDict]]
        ] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_prefix_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccessGrantArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_grant_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        access_grant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        access_grants_location_configuration: Optional[
            pulumi.Input[
                Union[
                    AccessGrantAccessGrantsLocationConfigurationArgs,
                    AccessGrantAccessGrantsLocationConfigurationArgsDict,
                ]
            ]
        ] = ...,
        access_grants_location_id: Optional[pulumi.Input[_builtins.str]] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        grant_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        grantee: Optional[
            pulumi.Input[Union[AccessGrantGranteeArgs, AccessGrantGranteeArgsDict]]
        ] = ...,
        permission: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_prefix_type: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> AccessGrant: ...
    @_builtins.property
    @pulumi.getter(name="accessGrantArn")
    def access_grant_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accessGrantId")
    def access_grant_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accessGrantsLocationConfiguration")
    def access_grants_location_configuration(
        self,
    ) -> pulumi.Output[
        Optional[outputs.AccessGrantAccessGrantsLocationConfiguration]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="accessGrantsLocationId")
    def access_grants_location_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="grantScope")
    def grant_scope(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def grantee(self) -> pulumi.Output[outputs.AccessGrantGrantee]: ...
    @_builtins.property
    @pulumi.getter
    def permission(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3PrefixType")
    def s3_prefix_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
