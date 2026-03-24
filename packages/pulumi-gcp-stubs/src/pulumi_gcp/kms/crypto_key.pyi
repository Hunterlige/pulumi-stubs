

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CryptoKeyArgs', 'CryptoKey']
@pulumi.input_type
class CryptoKeyArgs:
    def __init__(__self__, *, key_ring: pulumi.Input[_builtins.str], crypto_key_backend: Optional[pulumi.Input[_builtins.str]] = ..., destroy_scheduled_duration: Optional[pulumi.Input[_builtins.str]] = ..., import_only: Optional[pulumi.Input[_builtins.bool]] = ..., key_access_justifications_policy: Optional[pulumi.Input[CryptoKeyKeyAccessJustificationsPolicyArgs]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., purpose: Optional[pulumi.Input[_builtins.str]] = ..., rotation_period: Optional[pulumi.Input[_builtins.str]] = ..., skip_initial_version_creation: Optional[pulumi.Input[_builtins.bool]] = ..., version_template: Optional[pulumi.Input[CryptoKeyVersionTemplateArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRing")
    def key_ring(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_ring.setter
    def key_ring(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyBackend")
    def crypto_key_backend(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @crypto_key_backend.setter
    def crypto_key_backend(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destroyScheduledDuration")
    def destroy_scheduled_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destroy_scheduled_duration.setter
    def destroy_scheduled_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importOnly")
    def import_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @import_only.setter
    def import_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAccessJustificationsPolicy")
    def key_access_justifications_policy(self) -> Optional[pulumi.Input[CryptoKeyKeyAccessJustificationsPolicyArgs]]:
        
        ...
    
    @key_access_justifications_policy.setter
    def key_access_justifications_policy(self, value: Optional[pulumi.Input[CryptoKeyKeyAccessJustificationsPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def purpose(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rotation_period.setter
    def rotation_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipInitialVersionCreation")
    def skip_initial_version_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_initial_version_creation.setter
    def skip_initial_version_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionTemplate")
    def version_template(self) -> Optional[pulumi.Input[CryptoKeyVersionTemplateArgs]]:
        
        ...
    
    @version_template.setter
    def version_template(self, value: Optional[pulumi.Input[CryptoKeyVersionTemplateArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _CryptoKeyState:
    def __init__(__self__, *, crypto_key_backend: Optional[pulumi.Input[_builtins.str]] = ..., destroy_scheduled_duration: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., import_only: Optional[pulumi.Input[_builtins.bool]] = ..., key_access_justifications_policy: Optional[pulumi.Input[CryptoKeyKeyAccessJustificationsPolicyArgs]] = ..., key_ring: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., primaries: Optional[pulumi.Input[Sequence[pulumi.Input[CryptoKeyPrimaryArgs]]]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., purpose: Optional[pulumi.Input[_builtins.str]] = ..., rotation_period: Optional[pulumi.Input[_builtins.str]] = ..., skip_initial_version_creation: Optional[pulumi.Input[_builtins.bool]] = ..., version_template: Optional[pulumi.Input[CryptoKeyVersionTemplateArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyBackend")
    def crypto_key_backend(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @crypto_key_backend.setter
    def crypto_key_backend(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="destroyScheduledDuration")
    def destroy_scheduled_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destroy_scheduled_duration.setter
    def destroy_scheduled_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effective_labels.setter
    def effective_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importOnly")
    def import_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @import_only.setter
    def import_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAccessJustificationsPolicy")
    def key_access_justifications_policy(self) -> Optional[pulumi.Input[CryptoKeyKeyAccessJustificationsPolicyArgs]]:
        
        ...
    
    @key_access_justifications_policy.setter
    def key_access_justifications_policy(self, value: Optional[pulumi.Input[CryptoKeyKeyAccessJustificationsPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRing")
    def key_ring(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_ring.setter
    def key_ring(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
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
    def primaries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CryptoKeyPrimaryArgs]]]]:
        
        ...
    
    @primaries.setter
    def primaries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CryptoKeyPrimaryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @pulumi_labels.setter
    def pulumi_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @rotation_period.setter
    def rotation_period(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipInitialVersionCreation")
    def skip_initial_version_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_initial_version_creation.setter
    def skip_initial_version_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionTemplate")
    def version_template(self) -> Optional[pulumi.Input[CryptoKeyVersionTemplateArgs]]:
        
        ...
    
    @version_template.setter
    def version_template(self, value: Optional[pulumi.Input[CryptoKeyVersionTemplateArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:kms/cryptoKey:CryptoKey")
class CryptoKey(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., crypto_key_backend: Optional[pulumi.Input[_builtins.str]] = ..., destroy_scheduled_duration: Optional[pulumi.Input[_builtins.str]] = ..., import_only: Optional[pulumi.Input[_builtins.bool]] = ..., key_access_justifications_policy: Optional[pulumi.Input[Union[CryptoKeyKeyAccessJustificationsPolicyArgs, CryptoKeyKeyAccessJustificationsPolicyArgsDict]]] = ..., key_ring: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., purpose: Optional[pulumi.Input[_builtins.str]] = ..., rotation_period: Optional[pulumi.Input[_builtins.str]] = ..., skip_initial_version_creation: Optional[pulumi.Input[_builtins.bool]] = ..., version_template: Optional[pulumi.Input[Union[CryptoKeyVersionTemplateArgs, CryptoKeyVersionTemplateArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CryptoKeyArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., crypto_key_backend: Optional[pulumi.Input[_builtins.str]] = ..., destroy_scheduled_duration: Optional[pulumi.Input[_builtins.str]] = ..., effective_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., import_only: Optional[pulumi.Input[_builtins.bool]] = ..., key_access_justifications_policy: Optional[pulumi.Input[Union[CryptoKeyKeyAccessJustificationsPolicyArgs, CryptoKeyKeyAccessJustificationsPolicyArgsDict]]] = ..., key_ring: Optional[pulumi.Input[_builtins.str]] = ..., labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., primaries: Optional[pulumi.Input[Sequence[pulumi.Input[Union[CryptoKeyPrimaryArgs, CryptoKeyPrimaryArgsDict]]]]] = ..., pulumi_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., purpose: Optional[pulumi.Input[_builtins.str]] = ..., rotation_period: Optional[pulumi.Input[_builtins.str]] = ..., skip_initial_version_creation: Optional[pulumi.Input[_builtins.bool]] = ..., version_template: Optional[pulumi.Input[Union[CryptoKeyVersionTemplateArgs, CryptoKeyVersionTemplateArgsDict]]] = ...) -> CryptoKey:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cryptoKeyBackend")
    def crypto_key_backend(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="destroyScheduledDuration")
    def destroy_scheduled_duration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importOnly")
    def import_only(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyAccessJustificationsPolicy")
    def key_access_justifications_policy(self) -> pulumi.Output[outputs.CryptoKeyKeyAccessJustificationsPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyRing")
    def key_ring(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def primaries(self) -> pulumi.Output[Sequence[outputs.CryptoKeyPrimary]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def purpose(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="skipInitialVersionCreation")
    def skip_initial_version_creation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="versionTemplate")
    def version_template(self) -> pulumi.Output[outputs.CryptoKeyVersionTemplate]:
        
        ...
    


