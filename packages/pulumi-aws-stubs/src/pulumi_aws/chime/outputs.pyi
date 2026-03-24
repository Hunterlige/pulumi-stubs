

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['SdkvoiceGlobalSettingsVoiceConnector', 'SdkvoiceSipMediaApplicationEndpoints', 'SdkvoiceSipRuleTargetApplication', ..., 'VoiceConnectorGroupConnector', 'VoiceConnectorOriginationRoute', 'VoiceConnectorStreamingMediaInsightsConfiguration', 'VoiceConnectorTerminationCredentialsCredential']
@pulumi.output_type
class SdkvoiceGlobalSettingsVoiceConnector(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cdr_bucket: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cdrBucket")
    def cdr_bucket(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class SdkvoiceSipMediaApplicationEndpoints(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, lambda_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SdkvoiceSipRuleTargetApplication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_region: _builtins.str, priority: _builtins.int, sip_media_application_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsRegion")
    def aws_region(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sipMediaApplicationId")
    def sip_media_application_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class SdkvoiceVoiceProfileDomainServerSideEncryptionConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VoiceConnectorGroupConnector(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, priority: _builtins.int, voice_connector_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceConnectorId")
    def voice_connector_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class VoiceConnectorOriginationRoute(dict):
    def __init__(__self__, *, host: _builtins.str, priority: _builtins.int, protocol: _builtins.str, weight: _builtins.int, port: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def weight(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class VoiceConnectorStreamingMediaInsightsConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, configuration_arn: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="configurationArn")
    def configuration_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class VoiceConnectorTerminationCredentialsCredential(dict):
    def __init__(__self__, *, password: _builtins.str, username: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str:
        
        ...
    


