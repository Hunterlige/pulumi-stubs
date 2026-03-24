

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccessHomeDirectoryMapping', 'AccessPosixProfile', 'ConnectorAs2Config', 'ConnectorEgressConfig', 'ConnectorEgressConfigVpcLattice', 'ConnectorSftpConfig', 'ServerEndpointDetails', 'ServerProtocolDetails', 'ServerS3StorageOptions', 'ServerWorkflowDetails', 'ServerWorkflowDetailsOnPartialUpload', 'ServerWorkflowDetailsOnUpload', 'UserHomeDirectoryMapping', 'UserPosixProfile', 'WebAppEndpointDetails', 'WebAppEndpointDetailsVpc', 'WebAppIdentityProviderDetails', 'WebAppIdentityProviderDetailsIdentityCenterConfig', 'WebAppWebAppUnit', 'WorkflowOnExceptionStep', 'WorkflowOnExceptionStepCopyStepDetails', ..., ..., ..., 'WorkflowOnExceptionStepCustomStepDetails', 'WorkflowOnExceptionStepDecryptStepDetails', ..., ..., ..., 'WorkflowOnExceptionStepDeleteStepDetails', 'WorkflowOnExceptionStepTagStepDetails', 'WorkflowOnExceptionStepTagStepDetailsTag', 'WorkflowStep', 'WorkflowStepCopyStepDetails', 'WorkflowStepCopyStepDetailsDestinationFileLocation', ..., ..., 'WorkflowStepCustomStepDetails', 'WorkflowStepDecryptStepDetails', ..., ..., ..., 'WorkflowStepDeleteStepDetails', 'WorkflowStepTagStepDetails', 'WorkflowStepTagStepDetailsTag', 'GetConnectorAs2ConfigResult', 'GetConnectorEgressConfigResult', 'GetConnectorEgressConfigVpcLatticeResult', 'GetConnectorSftpConfigResult']
@pulumi.output_type
class AccessHomeDirectoryMapping(dict):
    def __init__(__self__, *, entry: _builtins.str, target: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entry(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AccessPosixProfile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gid: _builtins.int, uid: _builtins.int, secondary_gids: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


@pulumi.output_type
class ConnectorAs2Config(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, compression: _builtins.str, encryption_algorithm: _builtins.str, local_profile_id: _builtins.str, mdn_response: _builtins.str, partner_profile_id: _builtins.str, signing_algorithm: _builtins.str, mdn_signing_algorithm: Optional[_builtins.str] = ..., message_subject: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localProfileId")
    def local_profile_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mdnResponse")
    def mdn_response(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerProfileId")
    def partner_profile_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithm")
    def signing_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mdnSigningAlgorithm")
    def mdn_signing_algorithm(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageSubject")
    def message_subject(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConnectorEgressConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, vpc_lattice: Optional[outputs.ConnectorEgressConfigVpcLattice] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLattice")
    def vpc_lattice(self) -> Optional[outputs.ConnectorEgressConfigVpcLattice]:
        
        ...
    


@pulumi.output_type
class ConnectorEgressConfigVpcLattice(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resource_configuration_arn: _builtins.str, port_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class ConnectorSftpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, trusted_host_keys: Optional[Sequence[_builtins.str]] = ..., user_secret_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedHostKeys")
    def trusted_host_keys(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSecretId")
    def user_secret_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServerEndpointDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, address_allocation_ids: Optional[Sequence[_builtins.str]] = ..., security_group_ids: Optional[Sequence[_builtins.str]] = ..., subnet_ids: Optional[Sequence[_builtins.str]] = ..., vpc_endpoint_id: Optional[_builtins.str] = ..., vpc_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressAllocationIds")
    def address_allocation_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServerProtocolDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, as2_transports: Optional[Sequence[_builtins.str]] = ..., passive_ip: Optional[_builtins.str] = ..., set_stat_option: Optional[_builtins.str] = ..., tls_session_resumption_mode: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="as2Transports")
    def as2_transports(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passiveIp")
    def passive_ip(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="setStatOption")
    def set_stat_option(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsSessionResumptionMode")
    def tls_session_resumption_mode(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServerS3StorageOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, directory_listing_optimization: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryListingOptimization")
    def directory_listing_optimization(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ServerWorkflowDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, on_partial_upload: Optional[outputs.ServerWorkflowDetailsOnPartialUpload] = ..., on_upload: Optional[outputs.ServerWorkflowDetailsOnUpload] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onPartialUpload")
    def on_partial_upload(self) -> Optional[outputs.ServerWorkflowDetailsOnPartialUpload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="onUpload")
    def on_upload(self) -> Optional[outputs.ServerWorkflowDetailsOnUpload]:
        
        ...
    


@pulumi.output_type
class ServerWorkflowDetailsOnPartialUpload(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_role: _builtins.str, workflow_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ServerWorkflowDetailsOnUpload(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, execution_role: _builtins.str, workflow_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UserHomeDirectoryMapping(dict):
    def __init__(__self__, *, entry: _builtins.str, target: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def entry(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class UserPosixProfile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gid: _builtins.int, uid: _builtins.int, secondary_gids: Optional[Sequence[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def gid(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uid(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Optional[Sequence[_builtins.int]]:
        
        ...
    


@pulumi.output_type
class WebAppEndpointDetails(dict):
    def __init__(__self__, *, vpc: Optional[outputs.WebAppEndpointDetailsVpc] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vpc(self) -> Optional[outputs.WebAppEndpointDetailsVpc]:
        
        ...
    


@pulumi.output_type
class WebAppEndpointDetailsVpc(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, subnet_ids: Sequence[_builtins.str], vpc_id: _builtins.str, security_group_ids: Optional[Sequence[_builtins.str]] = ..., vpc_endpoint_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcEndpointId")
    def vpc_endpoint_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAppIdentityProviderDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, identity_center_config: Optional[outputs.WebAppIdentityProviderDetailsIdentityCenterConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityCenterConfig")
    def identity_center_config(self) -> Optional[outputs.WebAppIdentityProviderDetailsIdentityCenterConfig]:
        
        ...
    


@pulumi.output_type
class WebAppIdentityProviderDetailsIdentityCenterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, application_arn: Optional[_builtins.str] = ..., instance_arn: Optional[_builtins.str] = ..., role: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationArn")
    def application_arn(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAppWebAppUnit(dict):
    def __init__(__self__, *, provisioned: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def provisioned(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, copy_step_details: Optional[outputs.WorkflowOnExceptionStepCopyStepDetails] = ..., custom_step_details: Optional[outputs.WorkflowOnExceptionStepCustomStepDetails] = ..., decrypt_step_details: Optional[outputs.WorkflowOnExceptionStepDecryptStepDetails] = ..., delete_step_details: Optional[outputs.WorkflowOnExceptionStepDeleteStepDetails] = ..., tag_step_details: Optional[outputs.WorkflowOnExceptionStepTagStepDetails] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyStepDetails")
    def copy_step_details(self) -> Optional[outputs.WorkflowOnExceptionStepCopyStepDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customStepDetails")
    def custom_step_details(self) -> Optional[outputs.WorkflowOnExceptionStepCustomStepDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="decryptStepDetails")
    def decrypt_step_details(self) -> Optional[outputs.WorkflowOnExceptionStepDecryptStepDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteStepDetails")
    def delete_step_details(self) -> Optional[outputs.WorkflowOnExceptionStepDeleteStepDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagStepDetails")
    def tag_step_details(self) -> Optional[outputs.WorkflowOnExceptionStepTagStepDetails]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepCopyStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_file_location: Optional[outputs.WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocation] = ..., name: Optional[_builtins.str] = ..., overwrite_existing: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationFileLocation")
    def destination_file_location(self) -> Optional[outputs.WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteExisting")
    def overwrite_existing(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, efs_file_location: Optional[outputs.WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationEfsFileLocation] = ..., s3_file_location: Optional[outputs.WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationS3FileLocation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileLocation")
    def efs_file_location(self) -> Optional[outputs.WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3FileLocation")
    def s3_file_location(self) -> Optional[outputs.WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationS3FileLocation]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationEfsFileLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_system_id: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepCopyStepDetailsDestinationFileLocationS3FileLocation(dict):
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepCustomStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ..., target: Optional[_builtins.str] = ..., timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepDecryptStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, destination_file_location: Optional[outputs.WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocation] = ..., name: Optional[_builtins.str] = ..., overwrite_existing: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationFileLocation")
    def destination_file_location(self) -> Optional[outputs.WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteExisting")
    def overwrite_existing(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, efs_file_location: Optional[outputs.WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationEfsFileLocation] = ..., s3_file_location: Optional[outputs.WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationS3FileLocation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileLocation")
    def efs_file_location(self) -> Optional[outputs.WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationEfsFileLocation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3FileLocation")
    def s3_file_location(self) -> Optional[outputs.WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationS3FileLocation]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationEfsFileLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_system_id: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepDecryptStepDetailsDestinationFileLocationS3FileLocation(dict):
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepDeleteStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepTagStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ..., tags: Optional[Sequence[outputs.WorkflowOnExceptionStepTagStepDetailsTag]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[outputs.WorkflowOnExceptionStepTagStepDetailsTag]]:
        
        ...
    


@pulumi.output_type
class WorkflowOnExceptionStepTagStepDetailsTag(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WorkflowStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, copy_step_details: Optional[outputs.WorkflowStepCopyStepDetails] = ..., custom_step_details: Optional[outputs.WorkflowStepCustomStepDetails] = ..., decrypt_step_details: Optional[outputs.WorkflowStepDecryptStepDetails] = ..., delete_step_details: Optional[outputs.WorkflowStepDeleteStepDetails] = ..., tag_step_details: Optional[outputs.WorkflowStepTagStepDetails] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="copyStepDetails")
    def copy_step_details(self) -> Optional[outputs.WorkflowStepCopyStepDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customStepDetails")
    def custom_step_details(self) -> Optional[outputs.WorkflowStepCustomStepDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="decryptStepDetails")
    def decrypt_step_details(self) -> Optional[outputs.WorkflowStepDecryptStepDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteStepDetails")
    def delete_step_details(self) -> Optional[outputs.WorkflowStepDeleteStepDetails]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagStepDetails")
    def tag_step_details(self) -> Optional[outputs.WorkflowStepTagStepDetails]:
        
        ...
    


@pulumi.output_type
class WorkflowStepCopyStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination_file_location: Optional[outputs.WorkflowStepCopyStepDetailsDestinationFileLocation] = ..., name: Optional[_builtins.str] = ..., overwrite_existing: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationFileLocation")
    def destination_file_location(self) -> Optional[outputs.WorkflowStepCopyStepDetailsDestinationFileLocation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteExisting")
    def overwrite_existing(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowStepCopyStepDetailsDestinationFileLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, efs_file_location: Optional[outputs.WorkflowStepCopyStepDetailsDestinationFileLocationEfsFileLocation] = ..., s3_file_location: Optional[outputs.WorkflowStepCopyStepDetailsDestinationFileLocationS3FileLocation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileLocation")
    def efs_file_location(self) -> Optional[outputs.WorkflowStepCopyStepDetailsDestinationFileLocationEfsFileLocation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3FileLocation")
    def s3_file_location(self) -> Optional[outputs.WorkflowStepCopyStepDetailsDestinationFileLocationS3FileLocation]:
        
        ...
    


@pulumi.output_type
class WorkflowStepCopyStepDetailsDestinationFileLocationEfsFileLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_system_id: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowStepCopyStepDetailsDestinationFileLocationS3FileLocation(dict):
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowStepCustomStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ..., target: Optional[_builtins.str] = ..., timeout_seconds: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def target(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WorkflowStepDecryptStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, destination_file_location: Optional[outputs.WorkflowStepDecryptStepDetailsDestinationFileLocation] = ..., name: Optional[_builtins.str] = ..., overwrite_existing: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destinationFileLocation")
    def destination_file_location(self) -> Optional[outputs.WorkflowStepDecryptStepDetailsDestinationFileLocation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteExisting")
    def overwrite_existing(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowStepDecryptStepDetailsDestinationFileLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, efs_file_location: Optional[outputs.WorkflowStepDecryptStepDetailsDestinationFileLocationEfsFileLocation] = ..., s3_file_location: Optional[outputs.WorkflowStepDecryptStepDetailsDestinationFileLocationS3FileLocation] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="efsFileLocation")
    def efs_file_location(self) -> Optional[outputs.WorkflowStepDecryptStepDetailsDestinationFileLocationEfsFileLocation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3FileLocation")
    def s3_file_location(self) -> Optional[outputs.WorkflowStepDecryptStepDetailsDestinationFileLocationS3FileLocation]:
        
        ...
    


@pulumi.output_type
class WorkflowStepDecryptStepDetailsDestinationFileLocationEfsFileLocation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, file_system_id: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowStepDecryptStepDetailsDestinationFileLocationS3FileLocation(dict):
    def __init__(__self__, *, bucket: Optional[_builtins.str] = ..., key: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowStepDeleteStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WorkflowStepTagStepDetails(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., source_file_location: Optional[_builtins.str] = ..., tags: Optional[Sequence[outputs.WorkflowStepTagStepDetailsTag]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceFileLocation")
    def source_file_location(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[outputs.WorkflowStepTagStepDetailsTag]]:
        
        ...
    


@pulumi.output_type
class WorkflowStepTagStepDetailsTag(dict):
    def __init__(__self__, *, key: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetConnectorAs2ConfigResult(dict):
    def __init__(__self__, *, basic_auth_secret_id: _builtins.str, compression: _builtins.str, encryption_algorithm: _builtins.str, local_profile_id: _builtins.str, mdn_response: _builtins.str, mdn_signing_algorithm: _builtins.str, message_subject: _builtins.str, partner_profile_id: _builtins.str, singing_algorithm: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuthSecretId")
    def basic_auth_secret_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def compression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="localProfileId")
    def local_profile_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mdnResponse")
    def mdn_response(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mdnSigningAlgorithm")
    def mdn_signing_algorithm(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageSubject")
    def message_subject(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="partnerProfileId")
    def partner_profile_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singingAlgorithm")
    def singing_algorithm(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetConnectorEgressConfigResult(dict):
    def __init__(__self__, *, vpc_lattices: Sequence[outputs.GetConnectorEgressConfigVpcLatticeResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcLattices")
    def vpc_lattices(self) -> Sequence[outputs.GetConnectorEgressConfigVpcLatticeResult]:
        
        ...
    


@pulumi.output_type
class GetConnectorEgressConfigVpcLatticeResult(dict):
    def __init__(__self__, *, port_number: _builtins.int, resource_configuration_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portNumber")
    def port_number(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceConfigurationArn")
    def resource_configuration_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetConnectorSftpConfigResult(dict):
    def __init__(__self__, *, trusted_host_keys: Sequence[_builtins.str], user_secret_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="trustedHostKeys")
    def trusted_host_keys(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userSecretId")
    def user_secret_id(self) -> _builtins.str:
        
        ...
    


