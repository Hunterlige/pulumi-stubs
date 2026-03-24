

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegionalSecretCustomerManagedEncryption', 'RegionalSecretIamBindingCondition', 'RegionalSecretIamMemberCondition', 'RegionalSecretRotation', 'RegionalSecretTopic', 'RegionalSecretVersionCustomerManagedEncryption', 'SecretIamBindingCondition', 'SecretIamMemberCondition', 'SecretReplication', 'SecretReplicationAuto', 'SecretReplicationAutoCustomerManagedEncryption', 'SecretReplicationUserManaged', 'SecretReplicationUserManagedReplica', ..., 'SecretRotation', 'SecretTopic', 'GetRegionalSecretCustomerManagedEncryptionResult', 'GetRegionalSecretRotationResult', 'GetRegionalSecretTopicResult', ..., 'GetRegionalSecretsSecretResult', ..., 'GetRegionalSecretsSecretRotationResult', 'GetRegionalSecretsSecretTopicResult', 'GetSecretReplicationResult', 'GetSecretReplicationAutoResult', ..., 'GetSecretReplicationUserManagedResult', 'GetSecretReplicationUserManagedReplicaResult', ..., 'GetSecretRotationResult', 'GetSecretTopicResult', 'GetSecretsSecretResult', 'GetSecretsSecretReplicationResult', 'GetSecretsSecretReplicationAutoResult', ..., 'GetSecretsSecretReplicationUserManagedResult', ..., ..., 'GetSecretsSecretRotationResult', 'GetSecretsSecretTopicResult']
@pulumi.output_type
class RegionalSecretCustomerManagedEncryption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RegionalSecretIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegionalSecretIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegionalSecretRotation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_rotation_time: Optional[_builtins.str] = ..., rotation_period: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RegionalSecretTopic(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RegionalSecretVersionCustomerManagedEncryption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_version_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecretIamBindingCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecretIamMemberCondition(dict):
    def __init__(__self__, *, expression: _builtins.str, title: _builtins.str, description: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecretReplication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, auto: Optional[outputs.SecretReplicationAuto] = ..., user_managed: Optional[outputs.SecretReplicationUserManaged] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auto(self) -> Optional[outputs.SecretReplicationAuto]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManaged")
    def user_managed(self) -> Optional[outputs.SecretReplicationUserManaged]:
        
        ...
    


@pulumi.output_type
class SecretReplicationAuto(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, customer_managed_encryption: Optional[outputs.SecretReplicationAutoCustomerManagedEncryption] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryption")
    def customer_managed_encryption(self) -> Optional[outputs.SecretReplicationAutoCustomerManagedEncryption]:
        
        ...
    


@pulumi.output_type
class SecretReplicationAutoCustomerManagedEncryption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecretReplicationUserManaged(dict):
    def __init__(__self__, *, replicas: Sequence[outputs.SecretReplicationUserManagedReplica]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Sequence[outputs.SecretReplicationUserManagedReplica]:
        
        ...
    


@pulumi.output_type
class SecretReplicationUserManagedReplica(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location: _builtins.str, customer_managed_encryption: Optional[outputs.SecretReplicationUserManagedReplicaCustomerManagedEncryption] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryption")
    def customer_managed_encryption(self) -> Optional[outputs.SecretReplicationUserManagedReplicaCustomerManagedEncryption]:
        
        ...
    


@pulumi.output_type
class SecretReplicationUserManagedReplicaCustomerManagedEncryption(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SecretRotation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_rotation_time: Optional[_builtins.str] = ..., rotation_period: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SecretTopic(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRegionalSecretCustomerManagedEncryptionResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRegionalSecretRotationResult(dict):
    def __init__(__self__, *, next_rotation_time: _builtins.str, rotation_period: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRegionalSecretTopicResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRegionalSecretVersionCustomerManagedEncryptionResult(dict):
    def __init__(__self__, *, kms_key_version_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRegionalSecretsSecretResult(dict):
    def __init__(__self__, *, annotations: Mapping[str, _builtins.str], create_time: _builtins.str, customer_managed_encryptions: Sequence[outputs.GetRegionalSecretsSecretCustomerManagedEncryptionResult], deletion_protection: _builtins.bool, effective_annotations: Mapping[str, _builtins.str], effective_labels: Mapping[str, _builtins.str], expire_time: _builtins.str, labels: Mapping[str, _builtins.str], location: _builtins.str, name: _builtins.str, project: _builtins.str, pulumi_labels: Mapping[str, _builtins.str], rotations: Sequence[outputs.GetRegionalSecretsSecretRotationResult], secret_id: _builtins.str, tags: Mapping[str, _builtins.str], topics: Sequence[outputs.GetRegionalSecretsSecretTopicResult], ttl: _builtins.str, version_aliases: Mapping[str, _builtins.str], version_destroy_ttl: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptions")
    def customer_managed_encryptions(self) -> Sequence[outputs.GetRegionalSecretsSecretCustomerManagedEncryptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rotations(self) -> Sequence[outputs.GetRegionalSecretsSecretRotationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topics(self) -> Sequence[outputs.GetRegionalSecretsSecretTopicResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionAliases")
    def version_aliases(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionDestroyTtl")
    def version_destroy_ttl(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRegionalSecretsSecretCustomerManagedEncryptionResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRegionalSecretsSecretRotationResult(dict):
    def __init__(__self__, *, next_rotation_time: _builtins.str, rotation_period: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetRegionalSecretsSecretTopicResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretReplicationResult(dict):
    def __init__(__self__, *, autos: Sequence[outputs.GetSecretReplicationAutoResult], user_manageds: Sequence[outputs.GetSecretReplicationUserManagedResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def autos(self) -> Sequence[outputs.GetSecretReplicationAutoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManageds")
    def user_manageds(self) -> Sequence[outputs.GetSecretReplicationUserManagedResult]:
        
        ...
    


@pulumi.output_type
class GetSecretReplicationAutoResult(dict):
    def __init__(__self__, *, customer_managed_encryptions: Sequence[outputs.GetSecretReplicationAutoCustomerManagedEncryptionResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptions")
    def customer_managed_encryptions(self) -> Sequence[outputs.GetSecretReplicationAutoCustomerManagedEncryptionResult]:
        
        ...
    


@pulumi.output_type
class GetSecretReplicationAutoCustomerManagedEncryptionResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretReplicationUserManagedResult(dict):
    def __init__(__self__, *, replicas: Sequence[outputs.GetSecretReplicationUserManagedReplicaResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Sequence[outputs.GetSecretReplicationUserManagedReplicaResult]:
        
        ...
    


@pulumi.output_type
class GetSecretReplicationUserManagedReplicaResult(dict):
    def __init__(__self__, *, customer_managed_encryptions: Sequence[outputs.GetSecretReplicationUserManagedReplicaCustomerManagedEncryptionResult], location: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptions")
    def customer_managed_encryptions(self) -> Sequence[outputs.GetSecretReplicationUserManagedReplicaCustomerManagedEncryptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretReplicationUserManagedReplicaCustomerManagedEncryptionResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretRotationResult(dict):
    def __init__(__self__, *, next_rotation_time: _builtins.str, rotation_period: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretTopicResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretsSecretResult(dict):
    def __init__(__self__, *, annotations: Mapping[str, _builtins.str], create_time: _builtins.str, deletion_protection: _builtins.bool, effective_annotations: Mapping[str, _builtins.str], effective_labels: Mapping[str, _builtins.str], expire_time: _builtins.str, labels: Mapping[str, _builtins.str], name: _builtins.str, project: _builtins.str, pulumi_labels: Mapping[str, _builtins.str], replications: Sequence[outputs.GetSecretsSecretReplicationResult], rotations: Sequence[outputs.GetSecretsSecretRotationResult], secret_id: _builtins.str, tags: Mapping[str, _builtins.str], topics: Sequence[outputs.GetSecretsSecretTopicResult], ttl: _builtins.str, version_aliases: Mapping[str, _builtins.str], version_destroy_ttl: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def annotations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveAnnotations")
    def effective_annotations(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replications(self) -> Sequence[outputs.GetSecretsSecretReplicationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rotations(self) -> Sequence[outputs.GetSecretsSecretRotationResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def topics(self) -> Sequence[outputs.GetSecretsSecretTopicResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ttl(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionAliases")
    def version_aliases(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionDestroyTtl")
    def version_destroy_ttl(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretsSecretReplicationResult(dict):
    def __init__(__self__, *, autos: Sequence[outputs.GetSecretsSecretReplicationAutoResult], user_manageds: Sequence[outputs.GetSecretsSecretReplicationUserManagedResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def autos(self) -> Sequence[outputs.GetSecretsSecretReplicationAutoResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManageds")
    def user_manageds(self) -> Sequence[outputs.GetSecretsSecretReplicationUserManagedResult]:
        
        ...
    


@pulumi.output_type
class GetSecretsSecretReplicationAutoResult(dict):
    def __init__(__self__, *, customer_managed_encryptions: Sequence[outputs.GetSecretsSecretReplicationAutoCustomerManagedEncryptionResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptions")
    def customer_managed_encryptions(self) -> Sequence[outputs.GetSecretsSecretReplicationAutoCustomerManagedEncryptionResult]:
        
        ...
    


@pulumi.output_type
class GetSecretsSecretReplicationAutoCustomerManagedEncryptionResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretsSecretReplicationUserManagedResult(dict):
    def __init__(__self__, *, replicas: Sequence[outputs.GetSecretsSecretReplicationUserManagedReplicaResult]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> Sequence[outputs.GetSecretsSecretReplicationUserManagedReplicaResult]:
        
        ...
    


@pulumi.output_type
class GetSecretsSecretReplicationUserManagedReplicaResult(dict):
    def __init__(__self__, *, customer_managed_encryptions: Sequence[outputs.GetSecretsSecretReplicationUserManagedReplicaCustomerManagedEncryptionResult], location: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryptions")
    def customer_managed_encryptions(self) -> Sequence[outputs.GetSecretsSecretReplicationUserManagedReplicaCustomerManagedEncryptionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretsSecretReplicationUserManagedReplicaCustomerManagedEncryptionResult(dict):
    def __init__(__self__, *, kms_key_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretsSecretRotationResult(dict):
    def __init__(__self__, *, next_rotation_time: _builtins.str, rotation_period: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetSecretsSecretTopicResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


