

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['KeySigningKeyArgs', 'KeySigningKey']
@pulumi.input_type
class KeySigningKeyArgs:
    def __init__(__self__, *, hosted_zone_id: pulumi.Input[_builtins.str], key_management_service_arn: pulumi.Input[_builtins.str], name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyManagementServiceArn")
    def key_management_service_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_management_service_arn.setter
    def key_management_service_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _KeySigningKeyState:
    def __init__(__self__, *, digest_algorithm_mnemonic: Optional[pulumi.Input[_builtins.str]] = ..., digest_algorithm_type: Optional[pulumi.Input[_builtins.int]] = ..., digest_value: Optional[pulumi.Input[_builtins.str]] = ..., dnskey_record: Optional[pulumi.Input[_builtins.str]] = ..., ds_record: Optional[pulumi.Input[_builtins.str]] = ..., flag: Optional[pulumi.Input[_builtins.int]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., key_management_service_arn: Optional[pulumi.Input[_builtins.str]] = ..., key_tag: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., signing_algorithm_mnemonic: Optional[pulumi.Input[_builtins.str]] = ..., signing_algorithm_type: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="digestAlgorithmMnemonic")
    def digest_algorithm_mnemonic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @digest_algorithm_mnemonic.setter
    def digest_algorithm_mnemonic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="digestAlgorithmType")
    def digest_algorithm_type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @digest_algorithm_type.setter
    def digest_algorithm_type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="digestValue")
    def digest_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @digest_value.setter
    def digest_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnskeyRecord")
    def dnskey_record(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dnskey_record.setter
    def dnskey_record(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dsRecord")
    def ds_record(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ds_record.setter
    def ds_record(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def flag(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @flag.setter
    def flag(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @hosted_zone_id.setter
    def hosted_zone_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyManagementServiceArn")
    def key_management_service_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_management_service_arn.setter
    def key_management_service_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @key_tag.setter
    def key_tag(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithmMnemonic")
    def signing_algorithm_mnemonic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @signing_algorithm_mnemonic.setter
    def signing_algorithm_mnemonic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithmType")
    def signing_algorithm_type(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @signing_algorithm_type.setter
    def signing_algorithm_type(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:route53/keySigningKey:KeySigningKey")
class KeySigningKey(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., key_management_service_arn: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: KeySigningKeyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., digest_algorithm_mnemonic: Optional[pulumi.Input[_builtins.str]] = ..., digest_algorithm_type: Optional[pulumi.Input[_builtins.int]] = ..., digest_value: Optional[pulumi.Input[_builtins.str]] = ..., dnskey_record: Optional[pulumi.Input[_builtins.str]] = ..., ds_record: Optional[pulumi.Input[_builtins.str]] = ..., flag: Optional[pulumi.Input[_builtins.int]] = ..., hosted_zone_id: Optional[pulumi.Input[_builtins.str]] = ..., key_management_service_arn: Optional[pulumi.Input[_builtins.str]] = ..., key_tag: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., public_key: Optional[pulumi.Input[_builtins.str]] = ..., signing_algorithm_mnemonic: Optional[pulumi.Input[_builtins.str]] = ..., signing_algorithm_type: Optional[pulumi.Input[_builtins.int]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ...) -> KeySigningKey:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="digestAlgorithmMnemonic")
    def digest_algorithm_mnemonic(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="digestAlgorithmType")
    def digest_algorithm_type(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="digestValue")
    def digest_value(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnskeyRecord")
    def dnskey_record(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dsRecord")
    def ds_record(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flag(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyManagementServiceArn")
    def key_management_service_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyTag")
    def key_tag(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithmMnemonic")
    def signing_algorithm_mnemonic(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithmType")
    def signing_algorithm_type(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    


