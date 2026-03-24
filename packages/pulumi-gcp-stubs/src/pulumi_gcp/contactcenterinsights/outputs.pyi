

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AnalysisRuleAnnotatorSelector', 'AnalysisRuleAnnotatorSelectorQaConfig', 'AnalysisRuleAnnotatorSelectorQaConfigScorecardList', 'AnalysisRuleAnnotatorSelectorSummarizationConfig', 'AutoLabelingRuleCondition']
@pulumi.output_type
class AnalysisRuleAnnotatorSelector(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, issue_models: Optional[Sequence[_builtins.str]] = ..., phrase_matchers: Optional[Sequence[_builtins.str]] = ..., qa_config: Optional[outputs.AnalysisRuleAnnotatorSelectorQaConfig] = ..., run_entity_annotator: Optional[_builtins.bool] = ..., run_intent_annotator: Optional[_builtins.bool] = ..., run_interruption_annotator: Optional[_builtins.bool] = ..., run_issue_model_annotator: Optional[_builtins.bool] = ..., run_phrase_matcher_annotator: Optional[_builtins.bool] = ..., run_qa_annotator: Optional[_builtins.bool] = ..., run_sentiment_annotator: Optional[_builtins.bool] = ..., run_silence_annotator: Optional[_builtins.bool] = ..., run_summarization_annotator: Optional[_builtins.bool] = ..., summarization_config: Optional[outputs.AnalysisRuleAnnotatorSelectorSummarizationConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="issueModels")
    def issue_models(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phraseMatchers")
    def phrase_matchers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qaConfig")
    def qa_config(self) -> Optional[outputs.AnalysisRuleAnnotatorSelectorQaConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runEntityAnnotator")
    def run_entity_annotator(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runIntentAnnotator")
    def run_intent_annotator(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runInterruptionAnnotator")
    def run_interruption_annotator(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runIssueModelAnnotator")
    def run_issue_model_annotator(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runPhraseMatcherAnnotator")
    def run_phrase_matcher_annotator(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runQaAnnotator")
    def run_qa_annotator(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runSentimentAnnotator")
    def run_sentiment_annotator(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runSilenceAnnotator")
    def run_silence_annotator(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runSummarizationAnnotator")
    def run_summarization_annotator(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationConfig")
    def summarization_config(self) -> Optional[outputs.AnalysisRuleAnnotatorSelectorSummarizationConfig]:
        
        ...
    


@pulumi.output_type
class AnalysisRuleAnnotatorSelectorQaConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, scorecard_list: Optional[outputs.AnalysisRuleAnnotatorSelectorQaConfigScorecardList] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scorecardList")
    def scorecard_list(self) -> Optional[outputs.AnalysisRuleAnnotatorSelectorQaConfigScorecardList]:
        
        ...
    


@pulumi.output_type
class AnalysisRuleAnnotatorSelectorQaConfigScorecardList(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, qa_scorecard_revisions: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="qaScorecardRevisions")
    def qa_scorecard_revisions(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AnalysisRuleAnnotatorSelectorSummarizationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, conversation_profile: Optional[_builtins.str] = ..., summarization_model: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationProfile")
    def conversation_profile(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationModel")
    def summarization_model(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AutoLabelingRuleCondition(dict):
    def __init__(__self__, *, condition: Optional[_builtins.str] = ..., value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]:
        
        ...
    


