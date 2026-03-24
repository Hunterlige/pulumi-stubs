import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "MediaInsightsPipelineConfigurationElement",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
]

@pulumi.output_type
class MediaInsightsPipelineConfigurationElement(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        amazon_transcribe_call_analytics_processor_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfiguration
        ] = ...,
        amazon_transcribe_processor_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationElementAmazonTranscribeProcessorConfiguration
        ] = ...,
        kinesis_data_stream_sink_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationElementKinesisDataStreamSinkConfiguration
        ] = ...,
        lambda_function_sink_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationElementLambdaFunctionSinkConfiguration
        ] = ...,
        s3_recording_sink_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationElementS3RecordingSinkConfiguration
        ] = ...,
        sns_topic_sink_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationElementSnsTopicSinkConfiguration
        ] = ...,
        sqs_queue_sink_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationElementSqsQueueSinkConfiguration
        ] = ...,
        voice_analytics_processor_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationElementVoiceAnalyticsProcessorConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name=...)
    def amazon_transcribe_call_analytics_processor_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="amazonTranscribeProcessorConfiguration")
    def amazon_transcribe_processor_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationElementAmazonTranscribeProcessorConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="kinesisDataStreamSinkConfiguration")
    def kinesis_data_stream_sink_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationElementKinesisDataStreamSinkConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionSinkConfiguration")
    def lambda_function_sink_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationElementLambdaFunctionSinkConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="s3RecordingSinkConfiguration")
    def s3_recording_sink_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationElementS3RecordingSinkConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicSinkConfiguration")
    def sns_topic_sink_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationElementSnsTopicSinkConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sqsQueueSinkConfiguration")
    def sqs_queue_sink_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationElementSqsQueueSinkConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="voiceAnalyticsProcessorConfiguration")
    def voice_analytics_processor_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationElementVoiceAnalyticsProcessorConfiguration
    ]: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        language_code: _builtins.str,
        call_analytics_stream_categories: Optional[Sequence[_builtins.str]] = ...,
        content_identification_type: Optional[_builtins.str] = ...,
        content_redaction_type: Optional[_builtins.str] = ...,
        enable_partial_results_stabilization: Optional[_builtins.bool] = ...,
        filter_partial_results: Optional[_builtins.bool] = ...,
        language_model_name: Optional[_builtins.str] = ...,
        partial_results_stability: Optional[_builtins.str] = ...,
        pii_entity_types: Optional[_builtins.str] = ...,
        post_call_analytics_settings: Optional[
            outputs.MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationPostCallAnalyticsSettings
        ] = ...,
        vocabulary_filter_method: Optional[_builtins.str] = ...,
        vocabulary_filter_name: Optional[_builtins.str] = ...,
        vocabulary_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="callAnalyticsStreamCategories")
    def call_analytics_stream_categories(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="contentIdentificationType")
    def content_identification_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentRedactionType")
    def content_redaction_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enablePartialResultsStabilization")
    def enable_partial_results_stabilization(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="filterPartialResults")
    def filter_partial_results(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="languageModelName")
    def language_model_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partialResultsStability")
    def partial_results_stability(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="piiEntityTypes")
    def pii_entity_types(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="postCallAnalyticsSettings")
    def post_call_analytics_settings(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationPostCallAnalyticsSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="vocabularyFilterMethod")
    def vocabulary_filter_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vocabularyFilterName")
    def vocabulary_filter_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vocabularyName")
    def vocabulary_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationElementAmazonTranscribeCallAnalyticsProcessorConfigurationPostCallAnalyticsSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_access_role_arn: _builtins.str,
        output_location: _builtins.str,
        content_redaction_output: Optional[_builtins.str] = ...,
        output_encryption_kms_key_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="outputLocation")
    def output_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contentRedactionOutput")
    def content_redaction_output(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputEncryptionKmsKeyId")
    def output_encryption_kms_key_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationElementAmazonTranscribeProcessorConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        language_code: _builtins.str,
        content_identification_type: Optional[_builtins.str] = ...,
        content_redaction_type: Optional[_builtins.str] = ...,
        enable_partial_results_stabilization: Optional[_builtins.bool] = ...,
        filter_partial_results: Optional[_builtins.bool] = ...,
        language_model_name: Optional[_builtins.str] = ...,
        partial_results_stability: Optional[_builtins.str] = ...,
        pii_entity_types: Optional[_builtins.str] = ...,
        show_speaker_label: Optional[_builtins.bool] = ...,
        vocabulary_filter_method: Optional[_builtins.str] = ...,
        vocabulary_filter_name: Optional[_builtins.str] = ...,
        vocabulary_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="contentIdentificationType")
    def content_identification_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="contentRedactionType")
    def content_redaction_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enablePartialResultsStabilization")
    def enable_partial_results_stabilization(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="filterPartialResults")
    def filter_partial_results(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="languageModelName")
    def language_model_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="partialResultsStability")
    def partial_results_stability(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="piiEntityTypes")
    def pii_entity_types(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="showSpeakerLabel")
    def show_speaker_label(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="vocabularyFilterMethod")
    def vocabulary_filter_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vocabularyFilterName")
    def vocabulary_filter_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="vocabularyName")
    def vocabulary_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationElementKinesisDataStreamSinkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, insights_target: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insightsTarget")
    def insights_target(self) -> _builtins.str: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationElementLambdaFunctionSinkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, insights_target: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insightsTarget")
    def insights_target(self) -> _builtins.str: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationElementS3RecordingSinkConfiguration(dict):
    def __init__(__self__, *, destination: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationElementSnsTopicSinkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, insights_target: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insightsTarget")
    def insights_target(self) -> _builtins.str: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationElementSqsQueueSinkConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, insights_target: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="insightsTarget")
    def insights_target(self) -> _builtins.str: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationElementVoiceAnalyticsProcessorConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        speaker_search_status: _builtins.str,
        voice_tone_analysis_status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="speakerSearchStatus")
    def speaker_search_status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="voiceToneAnalysisStatus")
    def voice_tone_analysis_status(self) -> _builtins.str: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfiguration(dict):
    def __init__(
        __self__,
        *,
        rules: Sequence[
            outputs.MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRule
        ],
        disabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def rules(
        self,
    ) -> Sequence[
        outputs.MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRule
    ]: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        issue_detection_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleIssueDetectionConfiguration
        ] = ...,
        keyword_match_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleKeywordMatchConfiguration
        ] = ...,
        sentiment_configuration: Optional[
            outputs.MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleSentimentConfiguration
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="issueDetectionConfiguration")
    def issue_detection_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleIssueDetectionConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="keywordMatchConfiguration")
    def keyword_match_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleKeywordMatchConfiguration
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sentimentConfiguration")
    def sentiment_configuration(
        self,
    ) -> Optional[
        outputs.MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleSentimentConfiguration
    ]: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleIssueDetectionConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, rule_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> _builtins.str: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleKeywordMatchConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        keywords: Sequence[_builtins.str],
        rule_name: _builtins.str,
        negate: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def keywords(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def negate(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class MediaInsightsPipelineConfigurationRealTimeAlertConfigurationRuleSentimentConfiguration(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        rule_name: _builtins.str,
        sentiment_type: _builtins.str,
        time_period: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sentimentType")
    def sentiment_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> _builtins.int: ...
