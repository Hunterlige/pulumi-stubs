import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ProviderArgs", "Provider"]

@pulumi.input_type
class ProviderArgs:
    def __init__(
        __self__,
        *,
        access_key: Optional[pulumi.Input[_builtins.str]] = ...,
        allowed_account_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        assume_role_with_web_identity: Optional[
            pulumi.Input[ProviderAssumeRoleWithWebIdentityArgs]
        ] = ...,
        assume_roles: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProviderAssumeRoleArgs]]]
        ] = ...,
        custom_ca_bundle: Optional[pulumi.Input[_builtins.str]] = ...,
        default_tags: Optional[pulumi.Input[ProviderDefaultTagsArgs]] = ...,
        ec2_metadata_service_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        ec2_metadata_service_endpoint_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[Sequence[pulumi.Input[ProviderEndpointArgs]]]
        ] = ...,
        forbidden_account_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        http_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
        https_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_tags: Optional[pulumi.Input[ProviderIgnoreTagsArgs]] = ...,
        insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        no_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_us_east1_regional_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_use_path_style: Optional[pulumi.Input[_builtins.bool]] = ...,
        secret_key: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_config_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        shared_credentials_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        skip_credentials_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        skip_metadata_api_check: Optional[pulumi.Input[_builtins.bool]] = ...,
        skip_region_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        skip_requesting_account_id: Optional[pulumi.Input[_builtins.bool]] = ...,
        sts_region: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_policy_compliance: Optional[pulumi.Input[_builtins.str]] = ...,
        token: Optional[pulumi.Input[_builtins.str]] = ...,
        token_bucket_rate_limiter_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        use_dualstack_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_fips_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        user_agents: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_key.setter
    def access_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="allowedAccountIds")
    def allowed_account_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowed_account_ids.setter
    def allowed_account_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="assumeRoleWithWebIdentity")
    def assume_role_with_web_identity(
        self,
    ) -> Optional[pulumi.Input[ProviderAssumeRoleWithWebIdentityArgs]]: ...
    @assume_role_with_web_identity.setter
    def assume_role_with_web_identity(
        self, value: Optional[pulumi.Input[ProviderAssumeRoleWithWebIdentityArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="assumeRoles")
    def assume_roles(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProviderAssumeRoleArgs]]]]: ...
    @assume_roles.setter
    def assume_roles(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ProviderAssumeRoleArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="customCaBundle")
    def custom_ca_bundle(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_ca_bundle.setter
    def custom_ca_bundle(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="defaultTags")
    def default_tags(self) -> Optional[pulumi.Input[ProviderDefaultTagsArgs]]: ...
    @default_tags.setter
    def default_tags(self, value: Optional[pulumi.Input[ProviderDefaultTagsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ec2MetadataServiceEndpoint")
    def ec2_metadata_service_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ec2_metadata_service_endpoint.setter
    def ec2_metadata_service_endpoint(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ec2MetadataServiceEndpointMode")
    def ec2_metadata_service_endpoint_mode(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ec2_metadata_service_endpoint_mode.setter
    def ec2_metadata_service_endpoint_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def endpoints(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ProviderEndpointArgs]]]]: ...
    @endpoints.setter
    def endpoints(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ProviderEndpointArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="forbiddenAccountIds")
    def forbidden_account_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @forbidden_account_ids.setter
    def forbidden_account_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpProxy")
    def http_proxy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @http_proxy.setter
    def http_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @https_proxy.setter
    def https_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreTags")
    def ignore_tags(self) -> Optional[pulumi.Input[ProviderIgnoreTagsArgs]]: ...
    @ignore_tags.setter
    def ignore_tags(self, value: Optional[pulumi.Input[ProviderIgnoreTagsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def insecure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @insecure.setter
    def insecure(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="noProxy")
    def no_proxy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @no_proxy.setter
    def no_proxy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile.setter
    def profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryMode")
    def retry_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retry_mode.setter
    def retry_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3UsEast1RegionalEndpoint")
    def s3_us_east1_regional_endpoint(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_us_east1_regional_endpoint.setter
    def s3_us_east1_regional_endpoint(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3UsePathStyle")
    def s3_use_path_style(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @s3_use_path_style.setter
    def s3_use_path_style(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_key.setter
    def secret_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sharedConfigFiles")
    def shared_config_files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_config_files.setter
    def shared_config_files(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sharedCredentialsFiles")
    def shared_credentials_files(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @shared_credentials_files.setter
    def shared_credentials_files(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipCredentialsValidation")
    def skip_credentials_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_credentials_validation.setter
    def skip_credentials_validation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipMetadataApiCheck")
    def skip_metadata_api_check(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_metadata_api_check.setter
    def skip_metadata_api_check(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipRegionValidation")
    def skip_region_validation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_region_validation.setter
    def skip_region_validation(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="skipRequestingAccountId")
    def skip_requesting_account_id(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_requesting_account_id.setter
    def skip_requesting_account_id(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="stsRegion")
    def sts_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sts_region.setter
    def sts_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagPolicyCompliance")
    def tag_policy_compliance(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_policy_compliance.setter
    def tag_policy_compliance(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tokenBucketRateLimiterCapacity")
    def token_bucket_rate_limiter_capacity(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @token_bucket_rate_limiter_capacity.setter
    def token_bucket_rate_limiter_capacity(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="useDualstackEndpoint")
    def use_dualstack_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_dualstack_endpoint.setter
    def use_dualstack_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="useFipsEndpoint")
    def use_fips_endpoint(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_fips_endpoint.setter
    def use_fips_endpoint(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="userAgents")
    def user_agents(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @user_agents.setter
    def user_agents(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.type_token("pulumi:providers:aws")
class Provider(pulumi.ProviderResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        access_key: Optional[pulumi.Input[_builtins.str]] = ...,
        allowed_account_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        assume_role_with_web_identity: Optional[
            pulumi.Input[
                Union[
                    ProviderAssumeRoleWithWebIdentityArgs,
                    ProviderAssumeRoleWithWebIdentityArgsDict,
                ]
            ]
        ] = ...,
        assume_roles: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[ProviderAssumeRoleArgs, ProviderAssumeRoleArgsDict]
                    ]
                ]
            ]
        ] = ...,
        custom_ca_bundle: Optional[pulumi.Input[_builtins.str]] = ...,
        default_tags: Optional[
            pulumi.Input[Union[ProviderDefaultTagsArgs, ProviderDefaultTagsArgsDict]]
        ] = ...,
        ec2_metadata_service_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        ec2_metadata_service_endpoint_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[ProviderEndpointArgs, ProviderEndpointArgsDict]]
                ]
            ]
        ] = ...,
        forbidden_account_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        http_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
        https_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_tags: Optional[
            pulumi.Input[Union[ProviderIgnoreTagsArgs, ProviderIgnoreTagsArgsDict]]
        ] = ...,
        insecure: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        no_proxy: Optional[pulumi.Input[_builtins.str]] = ...,
        profile: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_us_east1_regional_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_use_path_style: Optional[pulumi.Input[_builtins.bool]] = ...,
        secret_key: Optional[pulumi.Input[_builtins.str]] = ...,
        shared_config_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        shared_credentials_files: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        skip_credentials_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        skip_metadata_api_check: Optional[pulumi.Input[_builtins.bool]] = ...,
        skip_region_validation: Optional[pulumi.Input[_builtins.bool]] = ...,
        skip_requesting_account_id: Optional[pulumi.Input[_builtins.bool]] = ...,
        sts_region: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_policy_compliance: Optional[pulumi.Input[_builtins.str]] = ...,
        token: Optional[pulumi.Input[_builtins.str]] = ...,
        token_bucket_rate_limiter_capacity: Optional[pulumi.Input[_builtins.int]] = ...,
        use_dualstack_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        use_fips_endpoint: Optional[pulumi.Input[_builtins.bool]] = ...,
        user_agents: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ProviderArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="customCaBundle")
    def custom_ca_bundle(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ec2MetadataServiceEndpoint")
    def ec2_metadata_service_endpoint(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ec2MetadataServiceEndpointMode")
    def ec2_metadata_service_endpoint_mode(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpProxy")
    def http_proxy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="noProxy")
    def no_proxy(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def profile(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="retryMode")
    def retry_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="s3UsEast1RegionalEndpoint")
    def s3_us_east1_regional_endpoint(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretKey")
    def secret_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="stsRegion")
    def sts_region(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="tagPolicyCompliance")
    def tag_policy_compliance(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[_builtins.str]]: ...

    @pulumi.output_type
    class TerraformConfigResult:
        def __init__(__self__, result=...) -> None: ...
        @_builtins.property
        @pulumi.getter
        def result(self) -> Mapping[str, Any]: ...

    def terraform_config(__self__) -> pulumi.Output[Provider.TerraformConfigResult]: ...
