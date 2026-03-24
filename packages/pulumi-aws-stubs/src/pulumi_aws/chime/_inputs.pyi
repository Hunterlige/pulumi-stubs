

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SdkvoiceGlobalSettingsVoiceConnectorArgs', 'SdkvoiceGlobalSettingsVoiceConnectorArgsDict', 'SdkvoiceSipMediaApplicationEndpointsArgs', 'SdkvoiceSipMediaApplicationEndpointsArgsDict', 'SdkvoiceSipRuleTargetApplicationArgs', 'SdkvoiceSipRuleTargetApplicationArgsDict', ..., ..., 'VoiceConnectorGroupConnectorArgs', 'VoiceConnectorGroupConnectorArgsDict', 'VoiceConnectorOriginationRouteArgs', 'VoiceConnectorOriginationRouteArgsDict', ..., ..., 'VoiceConnectorTerminationCredentialsCredentialArgs', ...]
class SdkvoiceGlobalSettingsVoiceConnectorArgsDict(TypedDict):
    cdr_bucket: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class SdkvoiceGlobalSettingsVoiceConnectorArgs:
    def __init__(__self__, *, cdr_bucket: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdrBucket")
    def cdr_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cdr_bucket.setter
    def cdr_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class SdkvoiceSipMediaApplicationEndpointsArgsDict(TypedDict):
    lambda_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class SdkvoiceSipMediaApplicationEndpointsArgs:
    def __init__(__self__, *, lambda_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SdkvoiceSipRuleTargetApplicationArgsDict(TypedDict):
    aws_region: pulumi.Input[_builtins.str]
    priority: pulumi.Input[_builtins.int]
    sip_media_application_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class SdkvoiceSipRuleTargetApplicationArgs:
    def __init__(__self__, *, aws_region: pulumi.Input[_builtins.str], priority: pulumi.Input[_builtins.int], sip_media_application_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @aws_region.setter
    def aws_region(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sipMediaApplicationId")
    def sip_media_application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sip_media_application_id.setter
    def sip_media_application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class SdkvoiceVoiceProfileDomainServerSideEncryptionConfigurationArgsDict(TypedDict):
    kms_key_arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class SdkvoiceVoiceProfileDomainServerSideEncryptionConfigurationArgs:
    def __init__(__self__, *, kms_key_arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_arn.setter
    def kms_key_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VoiceConnectorGroupConnectorArgsDict(TypedDict):
    priority: pulumi.Input[_builtins.int]
    voice_connector_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class VoiceConnectorGroupConnectorArgs:
    def __init__(__self__, *, priority: pulumi.Input[_builtins.int], voice_connector_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @voice_connector_id.setter
    def voice_connector_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class VoiceConnectorOriginationRouteArgsDict(TypedDict):
    host: pulumi.Input[_builtins.str]
    priority: pulumi.Input[_builtins.int]
    protocol: pulumi.Input[_builtins.str]
    weight: pulumi.Input[_builtins.int]
    port: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class VoiceConnectorOriginationRouteArgs:
    def __init__(__self__, *, host: pulumi.Input[_builtins.str], priority: pulumi.Input[_builtins.int], protocol: pulumi.Input[_builtins.str], weight: pulumi.Input[_builtins.int], port: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @priority.setter
    def priority(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @weight.setter
    def weight(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class VoiceConnectorStreamingMediaInsightsConfigurationArgsDict(TypedDict):
    configuration_arn: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class VoiceConnectorStreamingMediaInsightsConfigurationArgs:
    def __init__(__self__, *, configuration_arn: Optional[pulumi.Input[_builtins.str]] = ..., disabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationArn")
    def configuration_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @configuration_arn.setter
    def configuration_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class VoiceConnectorTerminationCredentialsCredentialArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]


@pulumi.input_type
class VoiceConnectorTerminationCredentialsCredentialArgs:
    def __init__(__self__, *, password: pulumi.Input[_builtins.str], username: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


