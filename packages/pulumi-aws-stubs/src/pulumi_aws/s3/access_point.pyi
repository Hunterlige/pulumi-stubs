import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AccessPointArgs", "AccessPoint"]

@pulumi.input_type
class AccessPointArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        public_access_block_configuration: Optional[
            pulumi.Input[AccessPointPublicAccessBlockConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_configuration: Optional[
            pulumi.Input[AccessPointVpcConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_account_id.setter
    def bucket_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(
        self,
    ) -> Optional[pulumi.Input[AccessPointPublicAccessBlockConfigurationArgs]]: ...
    @public_access_block_configuration.setter
    def public_access_block_configuration(
        self,
        value: Optional[pulumi.Input[AccessPointPublicAccessBlockConfigurationArgs]],
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
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> Optional[pulumi.Input[AccessPointVpcConfigurationArgs]]: ...
    @vpc_configuration.setter
    def vpc_configuration(
        self, value: Optional[pulumi.Input[AccessPointVpcConfigurationArgs]]
    ): ...

@pulumi.input_type
class _AccessPointState:
    def __init__(
        __self__,
        *,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        has_public_access_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        public_access_block_configuration: Optional[
            pulumi.Input[AccessPointPublicAccessBlockConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_configuration: Optional[
            pulumi.Input[AccessPointVpcConfigurationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @alias.setter
    def alias(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket_account_id.setter
    def bucket_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @endpoints.setter
    def endpoints(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="hasPublicAccessPolicy")
    def has_public_access_policy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @has_public_access_policy.setter
    def has_public_access_policy(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkOrigin")
    def network_origin(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_origin.setter
    def network_origin(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(
        self,
    ) -> Optional[pulumi.Input[AccessPointPublicAccessBlockConfigurationArgs]]: ...
    @public_access_block_configuration.setter
    def public_access_block_configuration(
        self,
        value: Optional[pulumi.Input[AccessPointPublicAccessBlockConfigurationArgs]],
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
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> Optional[pulumi.Input[AccessPointVpcConfigurationArgs]]: ...
    @vpc_configuration.setter
    def vpc_configuration(
        self, value: Optional[pulumi.Input[AccessPointVpcConfigurationArgs]]
    ): ...

@pulumi.type_token("aws:s3/accessPoint:AccessPoint")
class AccessPoint(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        public_access_block_configuration: Optional[
            pulumi.Input[
                Union[
                    AccessPointPublicAccessBlockConfigurationArgs,
                    AccessPointPublicAccessBlockConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        vpc_configuration: Optional[
            pulumi.Input[
                Union[
                    AccessPointVpcConfigurationArgs, AccessPointVpcConfigurationArgsDict
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AccessPointArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        alias: Optional[pulumi.Input[_builtins.str]] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        bucket_account_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain_name: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        has_public_access_policy: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        network_origin: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        public_access_block_configuration: Optional[
            pulumi.Input[
                Union[
                    AccessPointPublicAccessBlockConfigurationArgs,
                    AccessPointPublicAccessBlockConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_configuration: Optional[
            pulumi.Input[
                Union[
                    AccessPointVpcConfigurationArgs, AccessPointVpcConfigurationArgsDict
                ]
            ]
        ] = ...,
    ) -> AccessPoint: ...
    @_builtins.property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="bucketAccountId")
    def bucket_account_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hasPublicAccessPolicy")
    def has_public_access_policy(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkOrigin")
    def network_origin(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.AccessPointPublicAccessBlockConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="vpcConfiguration")
    def vpc_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.AccessPointVpcConfiguration]]: ...
