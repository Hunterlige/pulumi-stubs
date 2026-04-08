import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConfigurationSetDeliveryOptionsArgs",
    "ConfigurationSetDeliveryOptionsArgsDict",
    "ConfigurationSetTrackingOptionsArgs",
    "ConfigurationSetTrackingOptionsArgsDict",
    "EventDestinationCloudwatchDestinationArgs",
    "EventDestinationCloudwatchDestinationArgsDict",
    "EventDestinationKinesisDestinationArgs",
    "EventDestinationKinesisDestinationArgsDict",
    "EventDestinationSnsDestinationArgs",
    "EventDestinationSnsDestinationArgsDict",
    "ReceiptRuleAddHeaderActionArgs",
    "ReceiptRuleAddHeaderActionArgsDict",
    "ReceiptRuleBounceActionArgs",
    "ReceiptRuleBounceActionArgsDict",
    "ReceiptRuleLambdaActionArgs",
    "ReceiptRuleLambdaActionArgsDict",
    "ReceiptRuleS3ActionArgs",
    "ReceiptRuleS3ActionArgsDict",
    "ReceiptRuleSnsActionArgs",
    "ReceiptRuleSnsActionArgsDict",
    "ReceiptRuleStopActionArgs",
    "ReceiptRuleStopActionArgsDict",
    "ReceiptRuleWorkmailActionArgs",
    "ReceiptRuleWorkmailActionArgsDict",
]

class ConfigurationSetDeliveryOptionsArgsDict(TypedDict):
    tls_policy: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigurationSetDeliveryOptionsArgs:
    def __init__(
        __self__, *, tls_policy: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_policy.setter
    def tls_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConfigurationSetTrackingOptionsArgsDict(TypedDict):
    custom_redirect_domain: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConfigurationSetTrackingOptionsArgs:
    def __init__(
        __self__, *, custom_redirect_domain: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customRedirectDomain")
    def custom_redirect_domain(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_redirect_domain.setter
    def custom_redirect_domain(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EventDestinationCloudwatchDestinationArgsDict(TypedDict):
    default_value: pulumi.Input[_builtins.str]
    dimension_name: pulumi.Input[_builtins.str]
    value_source: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventDestinationCloudwatchDestinationArgs:
    def __init__(
        __self__,
        *,
        default_value: pulumi.Input[_builtins.str],
        dimension_name: pulumi.Input[_builtins.str],
        value_source: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> pulumi.Input[_builtins.str]: ...
    @default_value.setter
    def default_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> pulumi.Input[_builtins.str]: ...
    @dimension_name.setter
    def dimension_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueSource")
    def value_source(self) -> pulumi.Input[_builtins.str]: ...
    @value_source.setter
    def value_source(self, value: pulumi.Input[_builtins.str]): ...

class EventDestinationKinesisDestinationArgsDict(TypedDict):
    role_arn: pulumi.Input[_builtins.str]
    stream_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventDestinationKinesisDestinationArgs:
    def __init__(
        __self__,
        *,
        role_arn: pulumi.Input[_builtins.str],
        stream_arn: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Input[_builtins.str]: ...
    @stream_arn.setter
    def stream_arn(self, value: pulumi.Input[_builtins.str]): ...

class EventDestinationSnsDestinationArgsDict(TypedDict):
    topic_arn: pulumi.Input[_builtins.str]

@pulumi.input_type
class EventDestinationSnsDestinationArgs:
    def __init__(__self__, *, topic_arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[_builtins.str]: ...
    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[_builtins.str]): ...

class ReceiptRuleAddHeaderActionArgsDict(TypedDict):
    header_name: pulumi.Input[_builtins.str]
    header_value: pulumi.Input[_builtins.str]
    position: pulumi.Input[_builtins.int]

@pulumi.input_type
class ReceiptRuleAddHeaderActionArgs:
    def __init__(
        __self__,
        *,
        header_name: pulumi.Input[_builtins.str],
        header_value: pulumi.Input[_builtins.str],
        position: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[_builtins.str]: ...
    @header_name.setter
    def header_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> pulumi.Input[_builtins.str]: ...
    @header_value.setter
    def header_value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def position(self) -> pulumi.Input[_builtins.int]: ...
    @position.setter
    def position(self, value: pulumi.Input[_builtins.int]): ...

class ReceiptRuleBounceActionArgsDict(TypedDict):
    message: pulumi.Input[_builtins.str]
    position: pulumi.Input[_builtins.int]
    sender: pulumi.Input[_builtins.str]
    smtp_reply_code: pulumi.Input[_builtins.str]
    status_code: NotRequired[pulumi.Input[_builtins.str]]
    topic_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReceiptRuleBounceActionArgs:
    def __init__(
        __self__,
        *,
        message: pulumi.Input[_builtins.str],
        position: pulumi.Input[_builtins.int],
        sender: pulumi.Input[_builtins.str],
        smtp_reply_code: pulumi.Input[_builtins.str],
        status_code: Optional[pulumi.Input[_builtins.str]] = ...,
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> pulumi.Input[_builtins.str]: ...
    @message.setter
    def message(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def position(self) -> pulumi.Input[_builtins.int]: ...
    @position.setter
    def position(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def sender(self) -> pulumi.Input[_builtins.str]: ...
    @sender.setter
    def sender(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="smtpReplyCode")
    def smtp_reply_code(self) -> pulumi.Input[_builtins.str]: ...
    @smtp_reply_code.setter
    def smtp_reply_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReceiptRuleLambdaActionArgsDict(TypedDict):
    function_arn: pulumi.Input[_builtins.str]
    position: pulumi.Input[_builtins.int]
    invocation_type: NotRequired[pulumi.Input[_builtins.str]]
    topic_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReceiptRuleLambdaActionArgs:
    def __init__(
        __self__,
        *,
        function_arn: pulumi.Input[_builtins.str],
        position: pulumi.Input[_builtins.int],
        invocation_type: Optional[pulumi.Input[_builtins.str]] = ...,
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[_builtins.str]: ...
    @function_arn.setter
    def function_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def position(self) -> pulumi.Input[_builtins.int]: ...
    @position.setter
    def position(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="invocationType")
    def invocation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @invocation_type.setter
    def invocation_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReceiptRuleS3ActionArgsDict(TypedDict):
    bucket_name: pulumi.Input[_builtins.str]
    position: pulumi.Input[_builtins.int]
    iam_role_arn: NotRequired[pulumi.Input[_builtins.str]]
    kms_key_arn: NotRequired[pulumi.Input[_builtins.str]]
    object_key_prefix: NotRequired[pulumi.Input[_builtins.str]]
    topic_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReceiptRuleS3ActionArgs:
    def __init__(
        __self__,
        *,
        bucket_name: pulumi.Input[_builtins.str],
        position: pulumi.Input[_builtins.int],
        iam_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_key_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        object_key_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[_builtins.str]: ...
    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def position(self) -> pulumi.Input[_builtins.int]: ...
    @position.setter
    def position(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @iam_role_arn.setter
    def iam_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_key_prefix.setter
    def object_key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReceiptRuleSnsActionArgsDict(TypedDict):
    position: pulumi.Input[_builtins.int]
    topic_arn: pulumi.Input[_builtins.str]
    encoding: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReceiptRuleSnsActionArgs:
    def __init__(
        __self__,
        *,
        position: pulumi.Input[_builtins.int],
        topic_arn: pulumi.Input[_builtins.str],
        encoding: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def position(self) -> pulumi.Input[_builtins.int]: ...
    @position.setter
    def position(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[_builtins.str]: ...
    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReceiptRuleStopActionArgsDict(TypedDict):
    position: pulumi.Input[_builtins.int]
    scope: pulumi.Input[_builtins.str]
    topic_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReceiptRuleStopActionArgs:
    def __init__(
        __self__,
        *,
        position: pulumi.Input[_builtins.int],
        scope: pulumi.Input[_builtins.str],
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def position(self) -> pulumi.Input[_builtins.int]: ...
    @position.setter
    def position(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def scope(self) -> pulumi.Input[_builtins.str]: ...
    @scope.setter
    def scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ReceiptRuleWorkmailActionArgsDict(TypedDict):
    organization_arn: pulumi.Input[_builtins.str]
    position: pulumi.Input[_builtins.int]
    topic_arn: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ReceiptRuleWorkmailActionArgs:
    def __init__(
        __self__,
        *,
        organization_arn: pulumi.Input[_builtins.str],
        position: pulumi.Input[_builtins.int],
        topic_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="organizationArn")
    def organization_arn(self) -> pulumi.Input[_builtins.str]: ...
    @organization_arn.setter
    def organization_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def position(self) -> pulumi.Input[_builtins.int]: ...
    @position.setter
    def position(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
