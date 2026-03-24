

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegionalSecretCustomerManagedEncryptionArgs', 'RegionalSecretCustomerManagedEncryptionArgsDict', 'RegionalSecretIamBindingConditionArgs', 'RegionalSecretIamBindingConditionArgsDict', 'RegionalSecretIamMemberConditionArgs', 'RegionalSecretIamMemberConditionArgsDict', 'RegionalSecretRotationArgs', 'RegionalSecretRotationArgsDict', 'RegionalSecretTopicArgs', 'RegionalSecretTopicArgsDict', 'RegionalSecretVersionCustomerManagedEncryptionArgs', ..., 'SecretIamBindingConditionArgs', 'SecretIamBindingConditionArgsDict', 'SecretIamMemberConditionArgs', 'SecretIamMemberConditionArgsDict', 'SecretReplicationArgs', 'SecretReplicationArgsDict', 'SecretReplicationAutoArgs', 'SecretReplicationAutoArgsDict', 'SecretReplicationAutoCustomerManagedEncryptionArgs', ..., 'SecretReplicationUserManagedArgs', 'SecretReplicationUserManagedArgsDict', 'SecretReplicationUserManagedReplicaArgs', 'SecretReplicationUserManagedReplicaArgsDict', ..., ..., 'SecretRotationArgs', 'SecretRotationArgsDict', 'SecretTopicArgs', 'SecretTopicArgsDict']
class RegionalSecretCustomerManagedEncryptionArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class RegionalSecretCustomerManagedEncryptionArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RegionalSecretIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegionalSecretIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegionalSecretIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegionalSecretIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegionalSecretRotationArgsDict(TypedDict):
    next_rotation_time: NotRequired[pulumi.Input[_builtins.str]]
    rotation_period: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegionalSecretRotationArgs:
    def __init__(__self__, *, next_rotation_time: Optional[pulumi.Input[_builtins.str]] = ..., rotation_period: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @next_rotation_time.setter
    def next_rotation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rotation_period.setter
    def rotation_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RegionalSecretTopicArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class RegionalSecretTopicArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class RegionalSecretVersionCustomerManagedEncryptionArgsDict(TypedDict):
    kms_key_version_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RegionalSecretVersionCustomerManagedEncryptionArgs:
    def __init__(__self__, *, kms_key_version_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyVersionName")
    def kms_key_version_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @kms_key_version_name.setter
    def kms_key_version_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecretIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecretIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecretIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecretIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecretReplicationArgsDict(TypedDict):
    auto: NotRequired[pulumi.Input[SecretReplicationAutoArgsDict]]
    user_managed: NotRequired[pulumi.Input[SecretReplicationUserManagedArgsDict]]


@pulumi.input_type
class SecretReplicationArgs:
    def __init__(__self__, *, auto: Optional[pulumi.Input[SecretReplicationAutoArgs]] = ..., user_managed: Optional[pulumi.Input[SecretReplicationUserManagedArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def auto(self) -> Optional[pulumi.Input[SecretReplicationAutoArgs]]:
        
        ...
    
    @auto.setter
    def auto(self, value: Optional[pulumi.Input[SecretReplicationAutoArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userManaged")
    def user_managed(self) -> Optional[pulumi.Input[SecretReplicationUserManagedArgs]]:
        
        ...
    
    @user_managed.setter
    def user_managed(self, value: Optional[pulumi.Input[SecretReplicationUserManagedArgs]]): # -> None:
        ...
    


class SecretReplicationAutoArgsDict(TypedDict):
    customer_managed_encryption: NotRequired[pulumi.Input[SecretReplicationAutoCustomerManagedEncryptionArgsDict]]


@pulumi.input_type
class SecretReplicationAutoArgs:
    def __init__(__self__, *, customer_managed_encryption: Optional[pulumi.Input[SecretReplicationAutoCustomerManagedEncryptionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryption")
    def customer_managed_encryption(self) -> Optional[pulumi.Input[SecretReplicationAutoCustomerManagedEncryptionArgs]]:
        
        ...
    
    @customer_managed_encryption.setter
    def customer_managed_encryption(self, value: Optional[pulumi.Input[SecretReplicationAutoCustomerManagedEncryptionArgs]]): # -> None:
        ...
    


class SecretReplicationAutoCustomerManagedEncryptionArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecretReplicationAutoCustomerManagedEncryptionArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SecretReplicationUserManagedArgsDict(TypedDict):
    replicas: pulumi.Input[Sequence[pulumi.Input[SecretReplicationUserManagedReplicaArgsDict]]]


@pulumi.input_type
class SecretReplicationUserManagedArgs:
    def __init__(__self__, *, replicas: pulumi.Input[Sequence[pulumi.Input[SecretReplicationUserManagedReplicaArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def replicas(self) -> pulumi.Input[Sequence[pulumi.Input[SecretReplicationUserManagedReplicaArgs]]]:
        
        ...
    
    @replicas.setter
    def replicas(self, value: pulumi.Input[Sequence[pulumi.Input[SecretReplicationUserManagedReplicaArgs]]]): # -> None:
        ...
    


class SecretReplicationUserManagedReplicaArgsDict(TypedDict):
    location: pulumi.Input[_builtins.str]
    customer_managed_encryption: NotRequired[pulumi.Input[SecretReplicationUserManagedReplicaCustomerManagedEncryptionArgsDict]]


@pulumi.input_type
class SecretReplicationUserManagedReplicaArgs:
    def __init__(__self__, *, location: pulumi.Input[_builtins.str], customer_managed_encryption: Optional[pulumi.Input[SecretReplicationUserManagedReplicaCustomerManagedEncryptionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerManagedEncryption")
    def customer_managed_encryption(self) -> Optional[pulumi.Input[SecretReplicationUserManagedReplicaCustomerManagedEncryptionArgs]]:
        
        ...
    
    @customer_managed_encryption.setter
    def customer_managed_encryption(self, value: Optional[pulumi.Input[SecretReplicationUserManagedReplicaCustomerManagedEncryptionArgs]]): # -> None:
        ...
    


class SecretReplicationUserManagedReplicaCustomerManagedEncryptionArgsDict(TypedDict):
    kms_key_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecretReplicationUserManagedReplicaCustomerManagedEncryptionArgs:
    def __init__(__self__, *, kms_key_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyName")
    def kms_key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_name.setter
    def kms_key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SecretRotationArgsDict(TypedDict):
    next_rotation_time: NotRequired[pulumi.Input[_builtins.str]]
    rotation_period: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SecretRotationArgs:
    def __init__(__self__, *, next_rotation_time: Optional[pulumi.Input[_builtins.str]] = ..., rotation_period: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @next_rotation_time.setter
    def next_rotation_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rotation_period.setter
    def rotation_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SecretTopicArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]


@pulumi.input_type
class SecretTopicArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


