import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ServerArgs", "Server"]

@pulumi.input_type
class ServerArgs:
    def __init__(
        __self__,
        *,
        certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_details: Optional[pulumi.Input[ServerEndpointDetailsArgs]] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        function: Optional[pulumi.Input[_builtins.str]] = ...,
        host_key: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_provider_type: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_role: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_role: Optional[pulumi.Input[_builtins.str]] = ...,
        post_authentication_login_banner: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_authentication_login_banner: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_details: Optional[pulumi.Input[ServerProtocolDetailsArgs]] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_storage_options: Optional[pulumi.Input[ServerS3StorageOptionsArgs]] = ...,
        security_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sftp_authentication_methods: Optional[pulumi.Input[_builtins.str]] = ...,
        structured_log_destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow_details: Optional[pulumi.Input[ServerWorkflowDetailsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> Optional[pulumi.Input[ServerEndpointDetailsArgs]]: ...
    @endpoint_details.setter
    def endpoint_details(
        self, value: Optional[pulumi.Input[ServerEndpointDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function.setter
    def function(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_key.setter
    def host_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityProviderType")
    def identity_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_provider_type.setter
    def identity_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invocationRole")
    def invocation_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @invocation_role.setter
    def invocation_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging_role.setter
    def logging_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postAuthenticationLoginBanner")
    def post_authentication_login_banner(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_authentication_login_banner.setter
    def post_authentication_login_banner(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preAuthenticationLoginBanner")
    def pre_authentication_login_banner(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pre_authentication_login_banner.setter
    def pre_authentication_login_banner(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protocolDetails")
    def protocol_details(self) -> Optional[pulumi.Input[ServerProtocolDetailsArgs]]: ...
    @protocol_details.setter
    def protocol_details(
        self, value: Optional[pulumi.Input[ServerProtocolDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocols(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @protocols.setter
    def protocols(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3StorageOptions")
    def s3_storage_options(
        self,
    ) -> Optional[pulumi.Input[ServerS3StorageOptionsArgs]]: ...
    @s3_storage_options.setter
    def s3_storage_options(
        self, value: Optional[pulumi.Input[ServerS3StorageOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy_name.setter
    def security_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sftpAuthenticationMethods")
    def sftp_authentication_methods(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sftp_authentication_methods.setter
    def sftp_authentication_methods(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="structuredLogDestinations")
    def structured_log_destinations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @structured_log_destinations.setter
    def structured_log_destinations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workflowDetails")
    def workflow_details(self) -> Optional[pulumi.Input[ServerWorkflowDetailsArgs]]: ...
    @workflow_details.setter
    def workflow_details(
        self, value: Optional[pulumi.Input[ServerWorkflowDetailsArgs]]
    ): ...

@pulumi.input_type
class _ServerState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_details: Optional[pulumi.Input[ServerEndpointDetailsArgs]] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        function: Optional[pulumi.Input[_builtins.str]] = ...,
        host_key: Optional[pulumi.Input[_builtins.str]] = ...,
        host_key_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_provider_type: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_role: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_role: Optional[pulumi.Input[_builtins.str]] = ...,
        post_authentication_login_banner: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_authentication_login_banner: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_details: Optional[pulumi.Input[ServerProtocolDetailsArgs]] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_storage_options: Optional[pulumi.Input[ServerS3StorageOptionsArgs]] = ...,
        security_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sftp_authentication_methods: Optional[pulumi.Input[_builtins.str]] = ...,
        structured_log_destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow_details: Optional[pulumi.Input[ServerWorkflowDetailsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @domain.setter
    def domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> Optional[pulumi.Input[ServerEndpointDetailsArgs]]: ...
    @endpoint_details.setter
    def endpoint_details(
        self, value: Optional[pulumi.Input[ServerEndpointDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function.setter
    def function(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_key.setter
    def host_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="hostKeyFingerprint")
    def host_key_fingerprint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host_key_fingerprint.setter
    def host_key_fingerprint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="identityProviderType")
    def identity_provider_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @identity_provider_type.setter
    def identity_provider_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invocationRole")
    def invocation_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @invocation_role.setter
    def invocation_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @logging_role.setter
    def logging_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="postAuthenticationLoginBanner")
    def post_authentication_login_banner(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @post_authentication_login_banner.setter
    def post_authentication_login_banner(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preAuthenticationLoginBanner")
    def pre_authentication_login_banner(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pre_authentication_login_banner.setter
    def pre_authentication_login_banner(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="protocolDetails")
    def protocol_details(self) -> Optional[pulumi.Input[ServerProtocolDetailsArgs]]: ...
    @protocol_details.setter
    def protocol_details(
        self, value: Optional[pulumi.Input[ServerProtocolDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def protocols(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @protocols.setter
    def protocols(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3StorageOptions")
    def s3_storage_options(
        self,
    ) -> Optional[pulumi.Input[ServerS3StorageOptionsArgs]]: ...
    @s3_storage_options.setter
    def s3_storage_options(
        self, value: Optional[pulumi.Input[ServerS3StorageOptionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @security_policy_name.setter
    def security_policy_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sftpAuthenticationMethods")
    def sftp_authentication_methods(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sftp_authentication_methods.setter
    def sftp_authentication_methods(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="structuredLogDestinations")
    def structured_log_destinations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @structured_log_destinations.setter
    def structured_log_destinations(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
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
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workflowDetails")
    def workflow_details(self) -> Optional[pulumi.Input[ServerWorkflowDetailsArgs]]: ...
    @workflow_details.setter
    def workflow_details(
        self, value: Optional[pulumi.Input[ServerWorkflowDetailsArgs]]
    ): ...

@pulumi.type_token("aws:transfer/server:Server")
class Server(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_details: Optional[
            pulumi.Input[
                Union[ServerEndpointDetailsArgs, ServerEndpointDetailsArgsDict]
            ]
        ] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        function: Optional[pulumi.Input[_builtins.str]] = ...,
        host_key: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_provider_type: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_role: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_role: Optional[pulumi.Input[_builtins.str]] = ...,
        post_authentication_login_banner: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_authentication_login_banner: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_details: Optional[
            pulumi.Input[
                Union[ServerProtocolDetailsArgs, ServerProtocolDetailsArgsDict]
            ]
        ] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_storage_options: Optional[
            pulumi.Input[
                Union[ServerS3StorageOptionsArgs, ServerS3StorageOptionsArgsDict]
            ]
        ] = ...,
        security_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sftp_authentication_methods: Optional[pulumi.Input[_builtins.str]] = ...,
        structured_log_destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow_details: Optional[
            pulumi.Input[
                Union[ServerWorkflowDetailsArgs, ServerWorkflowDetailsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[ServerArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        certificate: Optional[pulumi.Input[_builtins.str]] = ...,
        directory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        domain: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        endpoint_details: Optional[
            pulumi.Input[
                Union[ServerEndpointDetailsArgs, ServerEndpointDetailsArgsDict]
            ]
        ] = ...,
        endpoint_type: Optional[pulumi.Input[_builtins.str]] = ...,
        force_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        function: Optional[pulumi.Input[_builtins.str]] = ...,
        host_key: Optional[pulumi.Input[_builtins.str]] = ...,
        host_key_fingerprint: Optional[pulumi.Input[_builtins.str]] = ...,
        identity_provider_type: Optional[pulumi.Input[_builtins.str]] = ...,
        invocation_role: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_role: Optional[pulumi.Input[_builtins.str]] = ...,
        post_authentication_login_banner: Optional[pulumi.Input[_builtins.str]] = ...,
        pre_authentication_login_banner: Optional[pulumi.Input[_builtins.str]] = ...,
        protocol_details: Optional[
            pulumi.Input[
                Union[ServerProtocolDetailsArgs, ServerProtocolDetailsArgsDict]
            ]
        ] = ...,
        protocols: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_storage_options: Optional[
            pulumi.Input[
                Union[ServerS3StorageOptionsArgs, ServerS3StorageOptionsArgsDict]
            ]
        ] = ...,
        security_policy_name: Optional[pulumi.Input[_builtins.str]] = ...,
        sftp_authentication_methods: Optional[pulumi.Input[_builtins.str]] = ...,
        structured_log_destinations: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
        workflow_details: Optional[
            pulumi.Input[
                Union[ServerWorkflowDetailsArgs, ServerWorkflowDetailsArgsDict]
            ]
        ] = ...,
    ) -> Server: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(
        self,
    ) -> pulumi.Output[Optional[outputs.ServerEndpointDetails]]: ...
    @_builtins.property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def function(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostKey")
    def host_key(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="hostKeyFingerprint")
    def host_key_fingerprint(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="identityProviderType")
    def identity_provider_type(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="invocationRole")
    def invocation_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="postAuthenticationLoginBanner")
    def post_authentication_login_banner(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="preAuthenticationLoginBanner")
    def pre_authentication_login_banner(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="protocolDetails")
    def protocol_details(self) -> pulumi.Output[outputs.ServerProtocolDetails]: ...
    @_builtins.property
    @pulumi.getter
    def protocols(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3StorageOptions")
    def s3_storage_options(self) -> pulumi.Output[outputs.ServerS3StorageOptions]: ...
    @_builtins.property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="sftpAuthenticationMethods")
    def sftp_authentication_methods(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="structuredLogDestinations")
    def structured_log_destinations(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="workflowDetails")
    def workflow_details(
        self,
    ) -> pulumi.Output[Optional[outputs.ServerWorkflowDetails]]: ...
