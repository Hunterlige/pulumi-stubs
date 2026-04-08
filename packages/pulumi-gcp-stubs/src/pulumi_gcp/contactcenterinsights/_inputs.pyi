import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AnalysisRuleAnnotatorSelectorArgs",
    "AnalysisRuleAnnotatorSelectorArgsDict",
    "AnalysisRuleAnnotatorSelectorQaConfigArgs",
    "AnalysisRuleAnnotatorSelectorQaConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "AutoLabelingRuleConditionArgs",
    "AutoLabelingRuleConditionArgsDict",
]

class AnalysisRuleAnnotatorSelectorArgsDict(TypedDict):
    issue_models: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    phrase_matchers: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    qa_config: NotRequired[pulumi.Input[AnalysisRuleAnnotatorSelectorQaConfigArgsDict]]
    run_entity_annotator: NotRequired[pulumi.Input[_builtins.bool]]
    run_intent_annotator: NotRequired[pulumi.Input[_builtins.bool]]
    run_interruption_annotator: NotRequired[pulumi.Input[_builtins.bool]]
    run_issue_model_annotator: NotRequired[pulumi.Input[_builtins.bool]]
    run_phrase_matcher_annotator: NotRequired[pulumi.Input[_builtins.bool]]
    run_qa_annotator: NotRequired[pulumi.Input[_builtins.bool]]
    run_sentiment_annotator: NotRequired[pulumi.Input[_builtins.bool]]
    run_silence_annotator: NotRequired[pulumi.Input[_builtins.bool]]
    run_summarization_annotator: NotRequired[pulumi.Input[_builtins.bool]]
    summarization_config: NotRequired[
        pulumi.Input[AnalysisRuleAnnotatorSelectorSummarizationConfigArgsDict]
    ]

@pulumi.input_type
class AnalysisRuleAnnotatorSelectorArgs:
    def __init__(
        __self__,
        *,
        issue_models: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        phrase_matchers: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        qa_config: Optional[
            pulumi.Input[AnalysisRuleAnnotatorSelectorQaConfigArgs]
        ] = ...,
        run_entity_annotator: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_intent_annotator: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_interruption_annotator: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_issue_model_annotator: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_phrase_matcher_annotator: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_qa_annotator: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_sentiment_annotator: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_silence_annotator: Optional[pulumi.Input[_builtins.bool]] = ...,
        run_summarization_annotator: Optional[pulumi.Input[_builtins.bool]] = ...,
        summarization_config: Optional[
            pulumi.Input[AnalysisRuleAnnotatorSelectorSummarizationConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="issueModels")
    def issue_models(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @issue_models.setter
    def issue_models(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="phraseMatchers")
    def phrase_matchers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @phrase_matchers.setter
    def phrase_matchers(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="qaConfig")
    def qa_config(
        self,
    ) -> Optional[pulumi.Input[AnalysisRuleAnnotatorSelectorQaConfigArgs]]: ...
    @qa_config.setter
    def qa_config(
        self, value: Optional[pulumi.Input[AnalysisRuleAnnotatorSelectorQaConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runEntityAnnotator")
    def run_entity_annotator(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_entity_annotator.setter
    def run_entity_annotator(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="runIntentAnnotator")
    def run_intent_annotator(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_intent_annotator.setter
    def run_intent_annotator(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="runInterruptionAnnotator")
    def run_interruption_annotator(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_interruption_annotator.setter
    def run_interruption_annotator(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runIssueModelAnnotator")
    def run_issue_model_annotator(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_issue_model_annotator.setter
    def run_issue_model_annotator(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runPhraseMatcherAnnotator")
    def run_phrase_matcher_annotator(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_phrase_matcher_annotator.setter
    def run_phrase_matcher_annotator(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runQaAnnotator")
    def run_qa_annotator(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_qa_annotator.setter
    def run_qa_annotator(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="runSentimentAnnotator")
    def run_sentiment_annotator(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_sentiment_annotator.setter
    def run_sentiment_annotator(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runSilenceAnnotator")
    def run_silence_annotator(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_silence_annotator.setter
    def run_silence_annotator(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="runSummarizationAnnotator")
    def run_summarization_annotator(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @run_summarization_annotator.setter
    def run_summarization_annotator(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="summarizationConfig")
    def summarization_config(
        self,
    ) -> Optional[
        pulumi.Input[AnalysisRuleAnnotatorSelectorSummarizationConfigArgs]
    ]: ...
    @summarization_config.setter
    def summarization_config(
        self,
        value: Optional[
            pulumi.Input[AnalysisRuleAnnotatorSelectorSummarizationConfigArgs]
        ],
    ): ...

class AnalysisRuleAnnotatorSelectorQaConfigArgsDict(TypedDict):
    scorecard_list: NotRequired[
        pulumi.Input[AnalysisRuleAnnotatorSelectorQaConfigScorecardListArgsDict]
    ]

@pulumi.input_type
class AnalysisRuleAnnotatorSelectorQaConfigArgs:
    def __init__(
        __self__,
        *,
        scorecard_list: Optional[
            pulumi.Input[AnalysisRuleAnnotatorSelectorQaConfigScorecardListArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="scorecardList")
    def scorecard_list(
        self,
    ) -> Optional[
        pulumi.Input[AnalysisRuleAnnotatorSelectorQaConfigScorecardListArgs]
    ]: ...
    @scorecard_list.setter
    def scorecard_list(
        self,
        value: Optional[
            pulumi.Input[AnalysisRuleAnnotatorSelectorQaConfigScorecardListArgs]
        ],
    ): ...

class AnalysisRuleAnnotatorSelectorQaConfigScorecardListArgsDict(TypedDict):
    qa_scorecard_revisions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class AnalysisRuleAnnotatorSelectorQaConfigScorecardListArgs:
    def __init__(
        __self__,
        *,
        qa_scorecard_revisions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="qaScorecardRevisions")
    def qa_scorecard_revisions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @qa_scorecard_revisions.setter
    def qa_scorecard_revisions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AnalysisRuleAnnotatorSelectorSummarizationConfigArgsDict(TypedDict):
    conversation_profile: NotRequired[pulumi.Input[_builtins.str]]
    summarization_model: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AnalysisRuleAnnotatorSelectorSummarizationConfigArgs:
    def __init__(
        __self__,
        *,
        conversation_profile: Optional[pulumi.Input[_builtins.str]] = ...,
        summarization_model: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conversationProfile")
    def conversation_profile(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @conversation_profile.setter
    def conversation_profile(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="summarizationModel")
    def summarization_model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @summarization_model.setter
    def summarization_model(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AutoLabelingRuleConditionArgsDict(TypedDict):
    condition: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AutoLabelingRuleConditionArgs:
    def __init__(
        __self__,
        *,
        condition: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
