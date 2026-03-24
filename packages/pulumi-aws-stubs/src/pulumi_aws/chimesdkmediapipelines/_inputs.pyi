

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['MediaInsightsPipelineConfigurationElementArgs', 'MediaInsightsPipelineConfigurationElementArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ...]
class MediaInsightsPipelineConfigurationElementArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    amazon_transcribe_call_analytics_processor_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationArgsDict]]
    amazon_transcribe_processor_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeProcessorConfigurationArgsDict]]
    kinesis_data_stream_sink_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationElementKinesisDataStreamSinkConfigurationArgsDict]]
    lambda_function_sink_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationElementLambdaFunctionSinkConfigurationArgsDict]]
    s3_recording_sink_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationElementS3RecordingSinkConfigurationArgsDict]]
    sns_topic_sink_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationElementSnsTopicSinkConfigurationArgsDict]]
    sqs_queue_sink_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationElementSqsQueueSinkConfigurationArgsDict]]
    voice_analytics_processor_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationElementVoiceAnalyticsProcessorConfigurationArgsDict]]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], amazon_transcribe_call_analytics_processor_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationArgs]] = ..., amazon_transcribe_processor_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeProcessorConfigurationArgs]] = ..., kinesis_data_stream_sink_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementKinesisDataStreamSinkConfigurationArgs]] = ..., lambda_function_sink_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementLambdaFunctionSinkConfigurationArgs]] = ..., s3_recording_sink_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementS3RecordingSinkConfigurationArgs]] = ..., sns_topic_sink_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementSnsTopicSinkConfigurationArgs]] = ..., sqs_queue_sink_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementSqsQueueSinkConfigurationArgs]] = ..., voice_analytics_processor_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementVoiceAnalyticsProcessorConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name=...)
    def amazon_transcribe_call_analytics_processor_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationArgs]]:
        
        ...
    
    @amazon_transcribe_call_analytics_processor_configuration.setter
    def amazon_transcribe_call_analytics_processor_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="amazonTranscribeProcessorConfiguration")
    def amazon_transcribe_processor_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeProcessorConfigurationArgs]]:
        
        ...
    
    @amazon_transcribe_processor_configuration.setter
    def amazon_transcribe_processor_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeProcessorConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisDataStreamSinkConfiguration")
    def kinesis_data_stream_sink_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementKinesisDataStreamSinkConfigurationArgs]]:
        
        ...
    
    @kinesis_data_stream_sink_configuration.setter
    def kinesis_data_stream_sink_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementKinesisDataStreamSinkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionSinkConfiguration")
    def lambda_function_sink_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementLambdaFunctionSinkConfigurationArgs]]:
        
        ...
    
    @lambda_function_sink_configuration.setter
    def lambda_function_sink_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementLambdaFunctionSinkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3RecordingSinkConfiguration")
    def s3_recording_sink_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementS3RecordingSinkConfigurationArgs]]:
        
        ...
    
    @s3_recording_sink_configuration.setter
    def s3_recording_sink_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementS3RecordingSinkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicSinkConfiguration")
    def sns_topic_sink_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementSnsTopicSinkConfigurationArgs]]:
        
        ...
    
    @sns_topic_sink_configuration.setter
    def sns_topic_sink_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementSnsTopicSinkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqsQueueSinkConfiguration")
    def sqs_queue_sink_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementSqsQueueSinkConfigurationArgs]]:
        
        ...
    
    @sqs_queue_sink_configuration.setter
    def sqs_queue_sink_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementSqsQueueSinkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceAnalyticsProcessorConfiguration")
    def voice_analytics_processor_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementVoiceAnalyticsProcessorConfigurationArgs]]:
        
        ...
    
    @voice_analytics_processor_configuration.setter
    def voice_analytics_processor_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementVoiceAnalyticsProcessorConfigurationArgs]]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationArgsDict(TypedDict):
    language_code: pulumi.Input[_builtins.str]
    call_analytics_stream_categories: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    content_identification_type: NotRequired[pulumi.Input[_builtins.str]]
    content_redaction_type: NotRequired[pulumi.Input[_builtins.str]]
    enable_partial_results_stabilization: NotRequired[pulumi.Input[_builtins.bool]]
    filter_partial_results: NotRequired[pulumi.Input[_builtins.bool]]
    language_model_name: NotRequired[pulumi.Input[_builtins.str]]
    partial_results_stability: NotRequired[pulumi.Input[_builtins.str]]
    pii_entity_types: NotRequired[pulumi.Input[_builtins.str]]
    post_call_analytics_settings: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationPostCallAnalyticsSettingsArgsDict]]
    vocabulary_filter_method: NotRequired[pulumi.Input[_builtins.str]]
    vocabulary_filter_name: NotRequired[pulumi.Input[_builtins.str]]
    vocabulary_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationArgs:
    def __init__(__self__, *, language_code: pulumi.Input[_builtins.str], call_analytics_stream_categories: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., content_identification_type: Optional[pulumi.Input[_builtins.str]] = ..., content_redaction_type: Optional[pulumi.Input[_builtins.str]] = ..., enable_partial_results_stabilization: Optional[pulumi.Input[_builtins.bool]] = ..., filter_partial_results: Optional[pulumi.Input[_builtins.bool]] = ..., language_model_name: Optional[pulumi.Input[_builtins.str]] = ..., partial_results_stability: Optional[pulumi.Input[_builtins.str]] = ..., pii_entity_types: Optional[pulumi.Input[_builtins.str]] = ..., post_call_analytics_settings: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationPostCallAnalyticsSettingsArgs]] = ..., vocabulary_filter_method: Optional[pulumi.Input[_builtins.str]] = ..., vocabulary_filter_name: Optional[pulumi.Input[_builtins.str]] = ..., vocabulary_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="callAnalyticsStreamCategories")
    def call_analytics_stream_categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @call_analytics_stream_categories.setter
    def call_analytics_stream_categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentIdentificationType")
    def content_identification_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_identification_type.setter
    def content_identification_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentRedactionType")
    def content_redaction_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_redaction_type.setter
    def content_redaction_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePartialResultsStabilization")
    def enable_partial_results_stabilization(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_partial_results_stabilization.setter
    def enable_partial_results_stabilization(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPartialResults")
    def filter_partial_results(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @filter_partial_results.setter
    def filter_partial_results(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageModelName")
    def language_model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_model_name.setter
    def language_model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partialResultsStability")
    def partial_results_stability(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partial_results_stability.setter
    def partial_results_stability(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="piiEntityTypes")
    def pii_entity_types(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pii_entity_types.setter
    def pii_entity_types(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="postCallAnalyticsSettings")
    def post_call_analytics_settings(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationPostCallAnalyticsSettingsArgs]]:
        
        ...
    
    @post_call_analytics_settings.setter
    def post_call_analytics_settings(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationPostCallAnalyticsSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vocabularyFilterMethod")
    def vocabulary_filter_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vocabulary_filter_method.setter
    def vocabulary_filter_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vocabularyFilterName")
    def vocabulary_filter_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vocabulary_filter_name.setter
    def vocabulary_filter_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vocabularyName")
    def vocabulary_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vocabulary_name.setter
    def vocabulary_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationPostCallAnalyticsSettingsArgsDict(TypedDict):
    data_access_role_arn: pulumi.Input[_builtins.str]
    output_location: pulumi.Input[_builtins.str]
    content_redaction_output: NotRequired[pulumi.Input[_builtins.str]]
    output_encryption_kms_key_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationPostCallAnalyticsSettingsArgs:
    def __init__(__self__, *, data_access_role_arn: pulumi.Input[_builtins.str], output_location: pulumi.Input[_builtins.str], content_redaction_output: Optional[pulumi.Input[_builtins.str]] = ..., output_encryption_kms_key_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @data_access_role_arn.setter
    def data_access_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputLocation")
    def output_location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @output_location.setter
    def output_location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentRedactionOutput")
    def content_redaction_output(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_redaction_output.setter
    def content_redaction_output(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputEncryptionKmsKeyId")
    def output_encryption_kms_key_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_encryption_kms_key_id.setter
    def output_encryption_kms_key_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationElementAmazonTranscribeProcessorConfigurationArgsDict(TypedDict):
    language_code: pulumi.Input[_builtins.str]
    content_identification_type: NotRequired[pulumi.Input[_builtins.str]]
    content_redaction_type: NotRequired[pulumi.Input[_builtins.str]]
    enable_partial_results_stabilization: NotRequired[pulumi.Input[_builtins.bool]]
    filter_partial_results: NotRequired[pulumi.Input[_builtins.bool]]
    language_model_name: NotRequired[pulumi.Input[_builtins.str]]
    partial_results_stability: NotRequired[pulumi.Input[_builtins.str]]
    pii_entity_types: NotRequired[pulumi.Input[_builtins.str]]
    show_speaker_label: NotRequired[pulumi.Input[_builtins.bool]]
    vocabulary_filter_method: NotRequired[pulumi.Input[_builtins.str]]
    vocabulary_filter_name: NotRequired[pulumi.Input[_builtins.str]]
    vocabulary_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementAmazonTranscribeProcessorConfigurationArgs:
    def __init__(__self__, *, language_code: pulumi.Input[_builtins.str], content_identification_type: Optional[pulumi.Input[_builtins.str]] = ..., content_redaction_type: Optional[pulumi.Input[_builtins.str]] = ..., enable_partial_results_stabilization: Optional[pulumi.Input[_builtins.bool]] = ..., filter_partial_results: Optional[pulumi.Input[_builtins.bool]] = ..., language_model_name: Optional[pulumi.Input[_builtins.str]] = ..., partial_results_stability: Optional[pulumi.Input[_builtins.str]] = ..., pii_entity_types: Optional[pulumi.Input[_builtins.str]] = ..., show_speaker_label: Optional[pulumi.Input[_builtins.bool]] = ..., vocabulary_filter_method: Optional[pulumi.Input[_builtins.str]] = ..., vocabulary_filter_name: Optional[pulumi.Input[_builtins.str]] = ..., vocabulary_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentIdentificationType")
    def content_identification_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_identification_type.setter
    def content_identification_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentRedactionType")
    def content_redaction_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_redaction_type.setter
    def content_redaction_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePartialResultsStabilization")
    def enable_partial_results_stabilization(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_partial_results_stabilization.setter
    def enable_partial_results_stabilization(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filterPartialResults")
    def filter_partial_results(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @filter_partial_results.setter
    def filter_partial_results(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageModelName")
    def language_model_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_model_name.setter
    def language_model_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="partialResultsStability")
    def partial_results_stability(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @partial_results_stability.setter
    def partial_results_stability(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="piiEntityTypes")
    def pii_entity_types(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @pii_entity_types.setter
    def pii_entity_types(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="showSpeakerLabel")
    def show_speaker_label(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @show_speaker_label.setter
    def show_speaker_label(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vocabularyFilterMethod")
    def vocabulary_filter_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vocabulary_filter_method.setter
    def vocabulary_filter_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vocabularyFilterName")
    def vocabulary_filter_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vocabulary_filter_name.setter
    def vocabulary_filter_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vocabularyName")
    def vocabulary_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @vocabulary_name.setter
    def vocabulary_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationElementKinesisDataStreamSinkConfigurationArgsDict(TypedDict):
    insights_target: pulumi.Input[_builtins.str]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementKinesisDataStreamSinkConfigurationArgs:
    def __init__(__self__, *, insights_target: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsTarget")
    def insights_target(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @insights_target.setter
    def insights_target(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationElementLambdaFunctionSinkConfigurationArgsDict(TypedDict):
    insights_target: pulumi.Input[_builtins.str]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementLambdaFunctionSinkConfigurationArgs:
    def __init__(__self__, *, insights_target: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsTarget")
    def insights_target(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @insights_target.setter
    def insights_target(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationElementS3RecordingSinkConfigurationArgsDict(TypedDict):
    destination: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementS3RecordingSinkConfigurationArgs:
    def __init__(__self__, *, destination: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationElementSnsTopicSinkConfigurationArgsDict(TypedDict):
    insights_target: pulumi.Input[_builtins.str]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementSnsTopicSinkConfigurationArgs:
    def __init__(__self__, *, insights_target: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsTarget")
    def insights_target(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @insights_target.setter
    def insights_target(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationElementSqsQueueSinkConfigurationArgsDict(TypedDict):
    insights_target: pulumi.Input[_builtins.str]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementSqsQueueSinkConfigurationArgs:
    def __init__(__self__, *, insights_target: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insightsTarget")
    def insights_target(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @insights_target.setter
    def insights_target(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationElementVoiceAnalyticsProcessorConfigurationArgsDict(TypedDict):
    speaker_search_status: pulumi.Input[_builtins.str]
    voice_tone_analysis_status: pulumi.Input[_builtins.str]


@pulumi.input_type
class MediaInsightsPipelineConfigurationElementVoiceAnalyticsProcessorConfigurationArgs:
    def __init__(__self__, *, speaker_search_status: pulumi.Input[_builtins.str], voice_tone_analysis_status: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="speakerSearchStatus")
    def speaker_search_status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @speaker_search_status.setter
    def speaker_search_status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceToneAnalysisStatus")
    def voice_tone_analysis_status(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @voice_tone_analysis_status.setter
    def voice_tone_analysis_status(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgsDict(TypedDict):
    rules: pulumi.Input[Sequence[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleArgsDict]]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationArgs:
    def __init__(__self__, *, rules: pulumi.Input[Sequence[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleArgs]]], disabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleArgs]]]:
        
        ...
    
    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    issue_detection_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleIssueDetectionConfigurationArgsDict]]
    keyword_match_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleKeywordMatchConfigurationArgsDict]]
    sentiment_configuration: NotRequired[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleSentimentConfigurationArgsDict]]


@pulumi.input_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str], issue_detection_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleIssueDetectionConfigurationArgs]] = ..., keyword_match_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleKeywordMatchConfigurationArgs]] = ..., sentiment_configuration: Optional[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleSentimentConfigurationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="issueDetectionConfiguration")
    def issue_detection_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleIssueDetectionConfigurationArgs]]:
        
        ...
    
    @issue_detection_configuration.setter
    def issue_detection_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleIssueDetectionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keywordMatchConfiguration")
    def keyword_match_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleKeywordMatchConfigurationArgs]]:
        
        ...
    
    @keyword_match_configuration.setter
    def keyword_match_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleKeywordMatchConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sentimentConfiguration")
    def sentiment_configuration(self) -> Optional[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleSentimentConfigurationArgs]]:
        
        ...
    
    @sentiment_configuration.setter
    def sentiment_configuration(self, value: Optional[pulumi.Input[MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleSentimentConfigurationArgs]]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleIssueDetectionConfigurationArgsDict(TypedDict):
    rule_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleIssueDetectionConfigurationArgs:
    def __init__(__self__, *, rule_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleKeywordMatchConfigurationArgsDict(TypedDict):
    keywords: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    rule_name: pulumi.Input[_builtins.str]
    negate: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleKeywordMatchConfigurationArgs:
    def __init__(__self__, *, keywords: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], rule_name: pulumi.Input[_builtins.str], negate: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def keywords(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @keywords.setter
    def keywords(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def negate(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @negate.setter
    def negate(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleSentimentConfigurationArgsDict(TypedDict):
    rule_name: pulumi.Input[_builtins.str]
    sentiment_type: pulumi.Input[_builtins.str]
    time_period: pulumi.Input[_builtins.int]


@pulumi.input_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleSentimentConfigurationArgs:
    def __init__(__self__, *, rule_name: pulumi.Input[_builtins.str], sentiment_type: pulumi.Input[_builtins.str], time_period: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @rule_name.setter
    def rule_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sentimentType")
    def sentiment_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sentiment_type.setter
    def sentiment_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @time_period.setter
    def time_period(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


