

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConfigurationSetDeliveryOptions', 'ConfigurationSetTrackingOptions', 'EventDestinationCloudwatchDestination', 'EventDestinationKinesisDestination', 'EventDestinationSnsDestination', 'ReceiptRuleAddHeaderAction', 'ReceiptRuleBounceAction', 'ReceiptRuleLambdaAction', 'ReceiptRuleS3Action', 'ReceiptRuleSnsAction', 'ReceiptRuleStopAction', 'ReceiptRuleWorkmailAction']
@pulumi.output_type
class ConfigurationSetDeliveryOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tls_policy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ConfigurationSetTrackingOptions(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_redirect_domain: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRedirectDomain")
    def custom_redirect_domain(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class EventDestinationCloudwatchDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_value: _builtins.str, dimension_name: _builtins.str, value_source: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueSource")
    def value_source(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EventDestinationKinesisDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, role_arn: _builtins.str, stream_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class EventDestinationSnsDestination(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, topic_arn: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ReceiptRuleAddHeaderAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, header_name: _builtins.str, header_value: _builtins.str, position: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ReceiptRuleBounceAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, message: _builtins.str, position: _builtins.int, sender: _builtins.str, smtp_reply_code: _builtins.str, status_code: Optional[_builtins.str] = ..., topic_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sender(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="smtpReplyCode")
    def smtp_reply_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReceiptRuleLambdaAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, function_arn: _builtins.str, position: _builtins.int, invocation_type: Optional[_builtins.str] = ..., topic_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationType")
    def invocation_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReceiptRuleS3Action(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bucket_name: _builtins.str, position: _builtins.int, iam_role_arn: Optional[_builtins.str] = ..., kms_key_arn: Optional[_builtins.str] = ..., object_key_prefix: Optional[_builtins.str] = ..., topic_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReceiptRuleSnsAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, position: _builtins.int, topic_arn: _builtins.str, encoding: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReceiptRuleStopAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, position: _builtins.int, scope: _builtins.str, topic_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ReceiptRuleWorkmailAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, organization_arn: _builtins.str, position: _builtins.int, topic_arn: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="organizationArn")
    def organization_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[_builtins.str]:
        
        ...
    


