import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccessHomeDirectoryMappingArgs",
    "AccessHomeDirectoryMappingArgsDict",
    "AccessPosixProfileArgs",
    "AccessPosixProfileArgsDict",
    "ConnectorAs2ConfigArgs",
    "ConnectorAs2ConfigArgsDict",
    "ConnectorEgressConfigArgs",
    "ConnectorEgressConfigArgsDict",
    "ConnectorEgressConfigVpcLatticeArgs",
    "ConnectorEgressConfigVpcLatticeArgsDict",
    "ConnectorSftpConfigArgs",
    "ConnectorSftpConfigArgsDict",
    "ServerEndpointDetailsArgs",
    "ServerEndpointDetailsArgsDict",
    "ServerProtocolDetailsArgs",
    "ServerProtocolDetailsArgsDict",
    "ServerS3StorageOptionsArgs",
    "ServerS3StorageOptionsArgsDict",
    "ServerWorkflowDetailsArgs",
    "ServerWorkflowDetailsArgsDict",
    "ServerWorkflowDetailsOnPartialUploadArgs",
    "ServerWorkflowDetailsOnPartialUploadArgsDict",
    "ServerWorkflowDetailsOnUploadArgs",
    "ServerWorkflowDetailsOnUploadArgsDict",
    "UserHomeDirectoryMappingArgs",
    "UserHomeDirectoryMappingArgsDict",
    "UserPosixProfileArgs",
    "UserPosixProfileArgsDict",
    "WebAppEndpointDetailsArgs",
    "WebAppEndpointDetailsArgsDict",
    "WebAppEndpointDetailsVpcArgs",
    "WebAppEndpointDetailsVpcArgsDict",
    "WebAppIdentityProviderDetailsArgs",
    "WebAppIdentityProviderDetailsArgsDict",
    ...,
    ...,
    "WebAppWebAppUnitArgs",
    "WebAppWebAppUnitArgsDict",
    "WorkflowOnExceptionStepArgs",
    "WorkflowOnExceptionStepArgsDict",
    "WorkflowOnExceptionStepCopyStepDetailsArgs",
    "WorkflowOnExceptionStepCopyStepDetailsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkflowOnExceptionStepCustomStepDetailsArgs",
    "WorkflowOnExceptionStepCustomStepDetailsArgsDict",
    "WorkflowOnExceptionStepDecryptStepDetailsArgs",
    "WorkflowOnExceptionStepDecryptStepDetailsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkflowOnExceptionStepDeleteStepDetailsArgs",
    "WorkflowOnExceptionStepDeleteStepDetailsArgsDict",
    "WorkflowOnExceptionStepTagStepDetailsArgs",
    "WorkflowOnExceptionStepTagStepDetailsArgsDict",
    "WorkflowOnExceptionStepTagStepDetailsTagArgs",
    "WorkflowOnExceptionStepTagStepDetailsTagArgsDict",
    "WorkflowStepArgs",
    "WorkflowStepArgsDict",
    "WorkflowStepCopyStepDetailsArgs",
    "WorkflowStepCopyStepDetailsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkflowStepCustomStepDetailsArgs",
    "WorkflowStepCustomStepDetailsArgsDict",
    "WorkflowStepDecryptStepDetailsArgs",
    "WorkflowStepDecryptStepDetailsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkflowStepDeleteStepDetailsArgs",
    "WorkflowStepDeleteStepDetailsArgsDict",
    "WorkflowStepTagStepDetailsArgs",
    "WorkflowStepTagStepDetailsArgsDict",
    "WorkflowStepTagStepDetailsTagArgs",
    "WorkflowStepTagStepDetailsTagArgsDict",
]

class AccessHomeDirectoryMappingArgsDict(TypedDict):
    entry: pulumi.Input[_builtins.str]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class AccessHomeDirectoryMappingArgs:
    def __init__(
        __self__,
        *,
        entry: pulumi.Input[_builtins.str],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entry(self) -> pulumi.Input[_builtins.str]: ...
    @entry.setter
    def entry(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class AccessPosixProfileArgsDict(TypedDict):
    gid: pulumi.Input[_builtins.int]
    uid: pulumi.Input[_builtins.int]
    secondary_gids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class AccessPosixProfileArgs:
    def __init__(
        __self__,
        *,
        gid: pulumi.Input[_builtins.int],
        uid: pulumi.Input[_builtins.int],
        secondary_gids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> pulumi.Input[_builtins.int]: ...
    @gid.setter
    def gid(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Input[_builtins.int]: ...
    @uid.setter
    def uid(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @secondary_gids.setter
    def secondary_gids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class ConnectorAs2ConfigArgsDict(TypedDict):
    compression: pulumi.Input[_builtins.str]
    encryption_algorithm: pulumi.Input[_builtins.str]
    local_profile_id: pulumi.Input[_builtins.str]
    mdn_response: pulumi.Input[_builtins.str]
    partner_profile_id: pulumi.Input[_builtins.str]
    signing_algorithm: pulumi.Input[_builtins.str]
    mdn_signing_algorithm: NotRequired[pulumi.Input[_builtins.str]]
    message_subject: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectorAs2ConfigArgs:
    def __init__(
        __self__,
        *,
        compression: pulumi.Input[_builtins.str],
        encryption_algorithm: pulumi.Input[_builtins.str],
        local_profile_id: pulumi.Input[_builtins.str],
        mdn_response: pulumi.Input[_builtins.str],
        partner_profile_id: pulumi.Input[_builtins.str],
        signing_algorithm: pulumi.Input[_builtins.str],
        mdn_signing_algorithm: Optional[pulumi.Input[_builtins.str]] = ...,
        message_subject: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> pulumi.Input[_builtins.str]: ...
    @compression.setter
    def compression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> pulumi.Input[_builtins.str]: ...
    @encryption_algorithm.setter
    def encryption_algorithm(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localProfileId")
    def local_profile_id(self) -> pulumi.Input[_builtins.str]: ...
    @local_profile_id.setter
    def local_profile_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mdnResponse")
    def mdn_response(self) -> pulumi.Input[_builtins.str]: ...
    @mdn_response.setter
    def mdn_response(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="partnerProfileId")
    def partner_profile_id(self) -> pulumi.Input[_builtins.str]: ...
    @partner_profile_id.setter
    def partner_profile_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="signingAlgorithm")
    def signing_algorithm(self) -> pulumi.Input[_builtins.str]: ...
    @signing_algorithm.setter
    def signing_algorithm(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mdnSigningAlgorithm")
    def mdn_signing_algorithm(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mdn_signing_algorithm.setter
    def mdn_signing_algorithm(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="messageSubject")
    def message_subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message_subject.setter
    def message_subject(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectorEgressConfigArgsDict(TypedDict):
    vpc_lattice: NotRequired[pulumi.Input[ConnectorEgressConfigVpcLatticeArgsDict]]

@pulumi.input_type
class ConnectorEgressConfigArgs:
    def __init__(
        __self__,
        *,
        vpc_lattice: Optional[pulumi.Input[ConnectorEgressConfigVpcLatticeArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcLattice")
    def vpc_lattice(
        self,
    ) -> Optional[pulumi.Input[ConnectorEgressConfigVpcLatticeArgs]]: ...
    @vpc_lattice.setter
    def vpc_lattice(
        self, value: Optional[pulumi.Input[ConnectorEgressConfigVpcLatticeArgs]]
    ): ...

class ConnectorEgressConfigVpcLatticeArgsDict(TypedDict):
    resource_configuration_arn: pulumi.Input[_builtins.str]
    port_number: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ConnectorEgressConfigVpcLatticeArgs:
    def __init__(
        __self__,
        *,
        resource_configuration_arn: pulumi.Input[_builtins.str],
        port_number: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> pulumi.Input[_builtins.str]: ...
    @resource_configuration_arn.setter
    def resource_configuration_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port_number.setter
    def port_number(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ConnectorSftpConfigArgsDict(TypedDict):
    trusted_host_keys: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    user_secret_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectorSftpConfigArgs:
    def __init__(
        __self__,
        *,
        trusted_host_keys: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        user_secret_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="trustedHostKeys")
    def trusted_host_keys(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @trusted_host_keys.setter
    def trusted_host_keys(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userSecretId")
    def user_secret_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_secret_id.setter
    def user_secret_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServerEndpointDetailsArgsDict(TypedDict):
    address_allocation_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    subnet_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_endpoint_id: NotRequired[pulumi.Input[_builtins.str]]
    vpc_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServerEndpointDetailsArgs:
    def __init__(
        __self__,
        *,
        address_allocation_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addressAllocationIds")
    def address_allocation_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @address_allocation_ids.setter
    def address_allocation_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServerProtocolDetailsArgsDict(TypedDict):
    as2_transports: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    passive_ip: NotRequired[pulumi.Input[_builtins.str]]
    set_stat_option: NotRequired[pulumi.Input[_builtins.str]]
    tls_session_resumption_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServerProtocolDetailsArgs:
    def __init__(
        __self__,
        *,
        as2_transports: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        passive_ip: Optional[pulumi.Input[_builtins.str]] = ...,
        set_stat_option: Optional[pulumi.Input[_builtins.str]] = ...,
        tls_session_resumption_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="as2Transports")
    def as2_transports(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @as2_transports.setter
    def as2_transports(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="passiveIp")
    def passive_ip(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @passive_ip.setter
    def passive_ip(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="setStatOption")
    def set_stat_option(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @set_stat_option.setter
    def set_stat_option(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsSessionResumptionMode")
    def tls_session_resumption_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_session_resumption_mode.setter
    def tls_session_resumption_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ServerS3StorageOptionsArgsDict(TypedDict):
    directory_listing_optimization: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServerS3StorageOptionsArgs:
    def __init__(
        __self__,
        *,
        directory_listing_optimization: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directoryListingOptimization")
    def directory_listing_optimization(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @directory_listing_optimization.setter
    def directory_listing_optimization(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ServerWorkflowDetailsArgsDict(TypedDict):
    on_partial_upload: NotRequired[
        pulumi.Input[ServerWorkflowDetailsOnPartialUploadArgsDict]
    ]
    on_upload: NotRequired[pulumi.Input[ServerWorkflowDetailsOnUploadArgsDict]]

@pulumi.input_type
class ServerWorkflowDetailsArgs:
    def __init__(
        __self__,
        *,
        on_partial_upload: Optional[
            pulumi.Input[ServerWorkflowDetailsOnPartialUploadArgs]
        ] = ...,
        on_upload: Optional[pulumi.Input[ServerWorkflowDetailsOnUploadArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="onPartialUpload")
    def on_partial_upload(
        self,
    ) -> Optional[pulumi.Input[ServerWorkflowDetailsOnPartialUploadArgs]]: ...
    @on_partial_upload.setter
    def on_partial_upload(
        self, value: Optional[pulumi.Input[ServerWorkflowDetailsOnPartialUploadArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onUpload")
    def on_upload(
        self,
    ) -> Optional[pulumi.Input[ServerWorkflowDetailsOnUploadArgs]]: ...
    @on_upload.setter
    def on_upload(
        self, value: Optional[pulumi.Input[ServerWorkflowDetailsOnUploadArgs]]
    ): ...

class ServerWorkflowDetailsOnPartialUploadArgsDict(TypedDict):
    execution_role: pulumi.Input[_builtins.str]
    workflow_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServerWorkflowDetailsOnPartialUploadArgs:
    def __init__(
        __self__,
        *,
        execution_role: pulumi.Input[_builtins.str],
        workflow_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Input[_builtins.str]: ...
    @execution_role.setter
    def execution_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> pulumi.Input[_builtins.str]: ...
    @workflow_id.setter
    def workflow_id(self, value: pulumi.Input[_builtins.str]): ...

class ServerWorkflowDetailsOnUploadArgsDict(TypedDict):
    execution_role: pulumi.Input[_builtins.str]
    workflow_id: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServerWorkflowDetailsOnUploadArgs:
    def __init__(
        __self__,
        *,
        execution_role: pulumi.Input[_builtins.str],
        workflow_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> pulumi.Input[_builtins.str]: ...
    @execution_role.setter
    def execution_role(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> pulumi.Input[_builtins.str]: ...
    @workflow_id.setter
    def workflow_id(self, value: pulumi.Input[_builtins.str]): ...

class UserHomeDirectoryMappingArgsDict(TypedDict):
    entry: pulumi.Input[_builtins.str]
    target: pulumi.Input[_builtins.str]

@pulumi.input_type
class UserHomeDirectoryMappingArgs:
    def __init__(
        __self__,
        *,
        entry: pulumi.Input[_builtins.str],
        target: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def entry(self) -> pulumi.Input[_builtins.str]: ...
    @entry.setter
    def entry(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> pulumi.Input[_builtins.str]: ...
    @target.setter
    def target(self, value: pulumi.Input[_builtins.str]): ...

class UserPosixProfileArgsDict(TypedDict):
    gid: pulumi.Input[_builtins.int]
    uid: pulumi.Input[_builtins.int]
    secondary_gids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]

@pulumi.input_type
class UserPosixProfileArgs:
    def __init__(
        __self__,
        *,
        gid: pulumi.Input[_builtins.int],
        uid: pulumi.Input[_builtins.int],
        secondary_gids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gid(self) -> pulumi.Input[_builtins.int]: ...
    @gid.setter
    def gid(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def uid(self) -> pulumi.Input[_builtins.int]: ...
    @uid.setter
    def uid(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]: ...
    @secondary_gids.setter
    def secondary_gids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    ): ...

class WebAppEndpointDetailsArgsDict(TypedDict):
    vpc: NotRequired[pulumi.Input[WebAppEndpointDetailsVpcArgsDict]]

@pulumi.input_type
class WebAppEndpointDetailsArgs:
    def __init__(
        __self__, *, vpc: Optional[pulumi.Input[WebAppEndpointDetailsVpcArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> Optional[pulumi.Input[WebAppEndpointDetailsVpcArgs]]: ...
    @vpc.setter
    def vpc(self, value: Optional[pulumi.Input[WebAppEndpointDetailsVpcArgs]]): ...

class WebAppEndpointDetailsVpcArgsDict(TypedDict):
    subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    vpc_id: pulumi.Input[_builtins.str]
    security_group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vpc_endpoint_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WebAppEndpointDetailsVpcArgs:
    def __init__(
        __self__,
        *,
        subnet_ids: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        vpc_id: pulumi.Input[_builtins.str],
        security_group_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        vpc_endpoint_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @subnet_ids.setter
    def subnet_ids(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @security_group_ids.setter
    def security_group_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebAppIdentityProviderDetailsArgsDict(TypedDict):
    identity_center_config: NotRequired[
        pulumi.Input[WebAppIdentityProviderDetailsIdentityCenterConfigArgsDict]
    ]

@pulumi.input_type
class WebAppIdentityProviderDetailsArgs:
    def __init__(
        __self__,
        *,
        identity_center_config: Optional[
            pulumi.Input[WebAppIdentityProviderDetailsIdentityCenterConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="identityCenterConfig")
    def identity_center_config(
        self,
    ) -> Optional[
        pulumi.Input[WebAppIdentityProviderDetailsIdentityCenterConfigArgs]
    ]: ...
    @identity_center_config.setter
    def identity_center_config(
        self,
        value: Optional[
            pulumi.Input[WebAppIdentityProviderDetailsIdentityCenterConfigArgs]
        ],
    ): ...

class WebAppIdentityProviderDetailsIdentityCenterConfigArgsDict(TypedDict):
    application_arn: NotRequired[pulumi.Input[_builtins.str]]
    instance_arn: NotRequired[pulumi.Input[_builtins.str]]
    role: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WebAppIdentityProviderDetailsIdentityCenterConfigArgs:
    def __init__(
        __self__,
        *,
        application_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        instance_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @application_arn.setter
    def application_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instance_arn.setter
    def instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebAppWebAppUnitArgsDict(TypedDict):
    provisioned: pulumi.Input[_builtins.int]

@pulumi.input_type
class WebAppWebAppUnitArgs:
    def __init__(__self__, *, provisioned: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def provisioned(self) -> pulumi.Input[_builtins.int]: ...
    @provisioned.setter
    def provisioned(self, value: pulumi.Input[_builtins.int]): ...

class WorkflowOnExceptionStepArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    copy_step_details: NotRequired[
        pulumi.Input[WorkflowOnExceptionStepCopyStepDetailsArgsDict]
    ]
    custom_step_details: NotRequired[
        pulumi.Input[WorkflowOnExceptionStepCustomStepDetailsArgsDict]
    ]
    decrypt_step_details: NotRequired[
        pulumi.Input[WorkflowOnExceptionStepDecryptStepDetailsArgsDict]
    ]
    delete_step_details: NotRequired[
        pulumi.Input[WorkflowOnExceptionStepDeleteStepDetailsArgsDict]
    ]
    tag_step_details: NotRequired[
        pulumi.Input[WorkflowOnExceptionStepTagStepDetailsArgsDict]
    ]

@pulumi.input_type
class WorkflowOnExceptionStepArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        copy_step_details: Optional[
            pulumi.Input[WorkflowOnExceptionStepCopyStepDetailsArgs]
        ] = ...,
        custom_step_details: Optional[
            pulumi.Input[WorkflowOnExceptionStepCustomStepDetailsArgs]
        ] = ...,
        decrypt_step_details: Optional[
            pulumi.Input[WorkflowOnExceptionStepDecryptStepDetailsArgs]
        ] = ...,
        delete_step_details: Optional[
            pulumi.Input[WorkflowOnExceptionStepDeleteStepDetailsArgs]
        ] = ...,
        tag_step_details: Optional[
            pulumi.Input[WorkflowOnExceptionStepTagStepDetailsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="copyStepDetails")
    def copy_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowOnExceptionStepCopyStepDetailsArgs]]: ...
    @copy_step_details.setter
    def copy_step_details(
        self, value: Optional[pulumi.Input[WorkflowOnExceptionStepCopyStepDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customStepDetails")
    def custom_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowOnExceptionStepCustomStepDetailsArgs]]: ...
    @custom_step_details.setter
    def custom_step_details(
        self,
        value: Optional[pulumi.Input[WorkflowOnExceptionStepCustomStepDetailsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="decryptStepDetails")
    def decrypt_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowOnExceptionStepDecryptStepDetailsArgs]]: ...
    @decrypt_step_details.setter
    def decrypt_step_details(
        self,
        value: Optional[pulumi.Input[WorkflowOnExceptionStepDecryptStepDetailsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteStepDetails")
    def delete_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowOnExceptionStepDeleteStepDetailsArgs]]: ...
    @delete_step_details.setter
    def delete_step_details(
        self,
        value: Optional[pulumi.Input[WorkflowOnExceptionStepDeleteStepDetailsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagStepDetails")
    def tag_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowOnExceptionStepTagStepDetailsArgs]]: ...
    @tag_step_details.setter
    def tag_step_details(
        self, value: Optional[pulumi.Input[WorkflowOnExceptionStepTagStepDetailsArgs]]
    ): ...

class WorkflowOnExceptionStepCopyStepDetailsArgsDict(TypedDict):
    destination_file_location: NotRequired[
        pulumi.Input[
            WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationArgsDict
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    overwrite_existing: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowOnExceptionStepCopyStepDetailsArgs:
    def __init__(
        __self__,
        *,
        destination_file_location: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationArgs
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        overwrite_existing: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationFileLocation")
    def destination_file_location(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationArgs]
    ]: ...
    @destination_file_location.setter
    def destination_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteExisting")
    def overwrite_existing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @overwrite_existing.setter
    def overwrite_existing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationArgsDict(TypedDict):
    efs_file_location: NotRequired[
        pulumi.Input[
            WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgsDict
        ]
    ]
    s3_file_location: NotRequired[
        pulumi.Input[
            WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationS3FileLocationArgsDict
        ]
    ]

@pulumi.input_type
class WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationArgs:
    def __init__(
        __self__,
        *,
        efs_file_location: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgs
            ]
        ] = ...,
        s3_file_location: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationS3FileLocationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="efsFileLocation")
    def efs_file_location(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgs
        ]
    ]: ...
    @efs_file_location.setter
    def efs_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3FileLocation")
    def s3_file_location(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationS3FileLocationArgs
        ]
    ]: ...
    @s3_file_location.setter
    def s3_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationS3FileLocationArgs
            ]
        ],
    ): ...

class WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgsDict(
    TypedDict
):
    file_system_id: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgs:
    def __init__(
        __self__,
        *,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationS3FileLocationArgsDict(
    TypedDict
):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationS3FileLocationArgs:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowOnExceptionStepCustomStepDetailsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkflowOnExceptionStepCustomStepDetailsArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkflowOnExceptionStepDecryptStepDetailsArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    destination_file_location: NotRequired[
        pulumi.Input[
            WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationArgsDict
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    overwrite_existing: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowOnExceptionStepDecryptStepDetailsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        destination_file_location: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationArgs
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        overwrite_existing: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationFileLocation")
    def destination_file_location(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationArgs
        ]
    ]: ...
    @destination_file_location.setter
    def destination_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteExisting")
    def overwrite_existing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @overwrite_existing.setter
    def overwrite_existing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationArgsDict(
    TypedDict
):
    efs_file_location: NotRequired[
        pulumi.Input[
            WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgsDict
        ]
    ]
    s3_file_location: NotRequired[
        pulumi.Input[
            WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgsDict
        ]
    ]

@pulumi.input_type
class WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationArgs:
    def __init__(
        __self__,
        *,
        efs_file_location: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgs
            ]
        ] = ...,
        s3_file_location: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="efsFileLocation")
    def efs_file_location(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgs
        ]
    ]: ...
    @efs_file_location.setter
    def efs_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3FileLocation")
    def s3_file_location(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgs
        ]
    ]: ...
    @s3_file_location.setter
    def s3_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgs
            ]
        ],
    ): ...

class WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgsDict(
    TypedDict
):
    file_system_id: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgs:
    def __init__(
        __self__,
        *,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgsDict(
    TypedDict
):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgs:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowOnExceptionStepDeleteStepDetailsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowOnExceptionStepDeleteStepDetailsArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowOnExceptionStepTagStepDetailsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[WorkflowOnExceptionStepTagStepDetailsTagArgsDict]]
        ]
    ]

@pulumi.input_type
class WorkflowOnExceptionStepTagStepDetailsArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkflowOnExceptionStepTagStepDetailsTagArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[WorkflowOnExceptionStepTagStepDetailsTagArgs]]
        ]
    ]: ...
    @tags.setter
    def tags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkflowOnExceptionStepTagStepDetailsTagArgs]]
            ]
        ],
    ): ...

class WorkflowOnExceptionStepTagStepDetailsTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkflowOnExceptionStepTagStepDetailsTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class WorkflowStepArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    copy_step_details: NotRequired[pulumi.Input[WorkflowStepCopyStepDetailsArgsDict]]
    custom_step_details: NotRequired[
        pulumi.Input[WorkflowStepCustomStepDetailsArgsDict]
    ]
    decrypt_step_details: NotRequired[
        pulumi.Input[WorkflowStepDecryptStepDetailsArgsDict]
    ]
    delete_step_details: NotRequired[
        pulumi.Input[WorkflowStepDeleteStepDetailsArgsDict]
    ]
    tag_step_details: NotRequired[pulumi.Input[WorkflowStepTagStepDetailsArgsDict]]

@pulumi.input_type
class WorkflowStepArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        copy_step_details: Optional[
            pulumi.Input[WorkflowStepCopyStepDetailsArgs]
        ] = ...,
        custom_step_details: Optional[
            pulumi.Input[WorkflowStepCustomStepDetailsArgs]
        ] = ...,
        decrypt_step_details: Optional[
            pulumi.Input[WorkflowStepDecryptStepDetailsArgs]
        ] = ...,
        delete_step_details: Optional[
            pulumi.Input[WorkflowStepDeleteStepDetailsArgs]
        ] = ...,
        tag_step_details: Optional[pulumi.Input[WorkflowStepTagStepDetailsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="copyStepDetails")
    def copy_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowStepCopyStepDetailsArgs]]: ...
    @copy_step_details.setter
    def copy_step_details(
        self, value: Optional[pulumi.Input[WorkflowStepCopyStepDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customStepDetails")
    def custom_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowStepCustomStepDetailsArgs]]: ...
    @custom_step_details.setter
    def custom_step_details(
        self, value: Optional[pulumi.Input[WorkflowStepCustomStepDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="decryptStepDetails")
    def decrypt_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowStepDecryptStepDetailsArgs]]: ...
    @decrypt_step_details.setter
    def decrypt_step_details(
        self, value: Optional[pulumi.Input[WorkflowStepDecryptStepDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="deleteStepDetails")
    def delete_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowStepDeleteStepDetailsArgs]]: ...
    @delete_step_details.setter
    def delete_step_details(
        self, value: Optional[pulumi.Input[WorkflowStepDeleteStepDetailsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagStepDetails")
    def tag_step_details(
        self,
    ) -> Optional[pulumi.Input[WorkflowStepTagStepDetailsArgs]]: ...
    @tag_step_details.setter
    def tag_step_details(
        self, value: Optional[pulumi.Input[WorkflowStepTagStepDetailsArgs]]
    ): ...

class WorkflowStepCopyStepDetailsArgsDict(TypedDict):
    destination_file_location: NotRequired[
        pulumi.Input[WorkflowStepCopyStepDetailsDestinationFileLocationArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    overwrite_existing: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowStepCopyStepDetailsArgs:
    def __init__(
        __self__,
        *,
        destination_file_location: Optional[
            pulumi.Input[WorkflowStepCopyStepDetailsDestinationFileLocationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        overwrite_existing: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationFileLocation")
    def destination_file_location(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowStepCopyStepDetailsDestinationFileLocationArgs]
    ]: ...
    @destination_file_location.setter
    def destination_file_location(
        self,
        value: Optional[
            pulumi.Input[WorkflowStepCopyStepDetailsDestinationFileLocationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteExisting")
    def overwrite_existing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @overwrite_existing.setter
    def overwrite_existing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowStepCopyStepDetailsDestinationFileLocationArgsDict(TypedDict):
    efs_file_location: NotRequired[
        pulumi.Input[
            WorkflowStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgsDict
        ]
    ]
    s3_file_location: NotRequired[
        pulumi.Input[
            WorkflowStepCopyStepDetailsDestinationFileLocationS3FileLocationArgsDict
        ]
    ]

@pulumi.input_type
class WorkflowStepCopyStepDetailsDestinationFileLocationArgs:
    def __init__(
        __self__,
        *,
        efs_file_location: Optional[
            pulumi.Input[
                WorkflowStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgs
            ]
        ] = ...,
        s3_file_location: Optional[
            pulumi.Input[
                WorkflowStepCopyStepDetailsDestinationFileLocationS3FileLocationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="efsFileLocation")
    def efs_file_location(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgs
        ]
    ]: ...
    @efs_file_location.setter
    def efs_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3FileLocation")
    def s3_file_location(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowStepCopyStepDetailsDestinationFileLocationS3FileLocationArgs
        ]
    ]: ...
    @s3_file_location.setter
    def s3_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowStepCopyStepDetailsDestinationFileLocationS3FileLocationArgs
            ]
        ],
    ): ...

class WorkflowStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgsDict(
    TypedDict
):
    file_system_id: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowStepCopyStepDetailsDestinationFileLocationEfsFileLocationArgs:
    def __init__(
        __self__,
        *,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowStepCopyStepDetailsDestinationFileLocationS3FileLocationArgsDict(
    TypedDict
):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowStepCopyStepDetailsDestinationFileLocationS3FileLocationArgs:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowStepCustomStepDetailsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]
    target: NotRequired[pulumi.Input[_builtins.str]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkflowStepCustomStepDetailsArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
        target: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target.setter
    def target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkflowStepDecryptStepDetailsArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    destination_file_location: NotRequired[
        pulumi.Input[WorkflowStepDecryptStepDetailsDestinationFileLocationArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    overwrite_existing: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowStepDecryptStepDetailsArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        destination_file_location: Optional[
            pulumi.Input[WorkflowStepDecryptStepDetailsDestinationFileLocationArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        overwrite_existing: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="destinationFileLocation")
    def destination_file_location(
        self,
    ) -> Optional[
        pulumi.Input[WorkflowStepDecryptStepDetailsDestinationFileLocationArgs]
    ]: ...
    @destination_file_location.setter
    def destination_file_location(
        self,
        value: Optional[
            pulumi.Input[WorkflowStepDecryptStepDetailsDestinationFileLocationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="overwriteExisting")
    def overwrite_existing(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @overwrite_existing.setter
    def overwrite_existing(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowStepDecryptStepDetailsDestinationFileLocationArgsDict(TypedDict):
    efs_file_location: NotRequired[
        pulumi.Input[
            WorkflowStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgsDict
        ]
    ]
    s3_file_location: NotRequired[
        pulumi.Input[
            WorkflowStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgsDict
        ]
    ]

@pulumi.input_type
class WorkflowStepDecryptStepDetailsDestinationFileLocationArgs:
    def __init__(
        __self__,
        *,
        efs_file_location: Optional[
            pulumi.Input[
                WorkflowStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgs
            ]
        ] = ...,
        s3_file_location: Optional[
            pulumi.Input[
                WorkflowStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="efsFileLocation")
    def efs_file_location(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgs
        ]
    ]: ...
    @efs_file_location.setter
    def efs_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3FileLocation")
    def s3_file_location(
        self,
    ) -> Optional[
        pulumi.Input[
            WorkflowStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgs
        ]
    ]: ...
    @s3_file_location.setter
    def s3_file_location(
        self,
        value: Optional[
            pulumi.Input[
                WorkflowStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgs
            ]
        ],
    ): ...

class WorkflowStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgsDict(
    TypedDict
):
    file_system_id: NotRequired[pulumi.Input[_builtins.str]]
    path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowStepDecryptStepDetailsDestinationFileLocationEfsFileLocationArgs:
    def __init__(
        __self__,
        *,
        file_system_id: Optional[pulumi.Input[_builtins.str]] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @file_system_id.setter
    def file_system_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgsDict(
    TypedDict
):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowStepDecryptStepDetailsDestinationFileLocationS3FileLocationArgs:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowStepDeleteStepDetailsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkflowStepDeleteStepDetailsArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkflowStepTagStepDetailsArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    source_file_location: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WorkflowStepTagStepDetailsTagArgsDict]]]
    ]

@pulumi.input_type
class WorkflowStepTagStepDetailsArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        source_file_location: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkflowStepTagStepDetailsTagArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_file_location.setter
    def source_file_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkflowStepTagStepDetailsTagArgs]]]
    ]: ...
    @tags.setter
    def tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkflowStepTagStepDetailsTagArgs]]]
        ],
    ): ...

class WorkflowStepTagStepDetailsTagArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkflowStepTagStepDetailsTagArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
