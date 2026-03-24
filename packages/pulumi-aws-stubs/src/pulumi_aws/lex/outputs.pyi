

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BotAbortStatement', 'BotAbortStatementMessage', 'BotAliasConversationLogs', 'BotAliasConversationLogsLogSetting', 'BotClarificationPrompt', 'BotClarificationPromptMessage', 'BotIntent', 'IntentConclusionStatement', 'IntentConclusionStatementMessage', 'IntentConfirmationPrompt', 'IntentConfirmationPromptMessage', 'IntentDialogCodeHook', 'IntentFollowUpPrompt', 'IntentFollowUpPromptPrompt', 'IntentFollowUpPromptPromptMessage', 'IntentFollowUpPromptRejectionStatement', 'IntentFollowUpPromptRejectionStatementMessage', 'IntentFulfillmentActivity', 'IntentFulfillmentActivityCodeHook', 'IntentRejectionStatement', 'IntentRejectionStatementMessage', 'IntentSlot', 'IntentSlotValueElicitationPrompt', 'IntentSlotValueElicitationPromptMessage', 'SlotTypeEnumerationValue', 'V2modelsBotDataPrivacy', 'V2modelsBotLocaleTimeouts', 'V2modelsBotLocaleVoiceSettings', 'V2modelsBotMember', 'V2modelsBotTimeouts', 'V2modelsBotVersionLocaleSpecification', 'V2modelsBotVersionTimeouts', 'V2modelsIntentClosingSetting', 'V2modelsIntentClosingSettingClosingResponse', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsIntentClosingSettingConditional', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsIntentClosingSettingNextStep', 'V2modelsIntentClosingSettingNextStepDialogAction', 'V2modelsIntentClosingSettingNextStepIntent', 'V2modelsIntentClosingSettingNextStepIntentSlot', ..., 'V2modelsIntentConfirmationSetting', 'V2modelsIntentConfirmationSettingCodeHook', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsIntentConfirmationSettingFailureNextStep', ..., ..., ..., ..., 'V2modelsIntentConfirmationSettingFailureResponse', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsIntentDialogCodeHook', 'V2modelsIntentFulfillmentCodeHook', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsIntentInitialResponseSetting', 'V2modelsIntentInitialResponseSettingCodeHook', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsIntentInitialResponseSettingConditional', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsIntentInitialResponseSettingNextStep', ..., 'V2modelsIntentInitialResponseSettingNextStepIntent', ..., ..., 'V2modelsIntentInputContext', 'V2modelsIntentKendraConfiguration', 'V2modelsIntentOutputContext', 'V2modelsIntentQnaIntentConfiguration', ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsIntentSampleUtterance', 'V2modelsIntentSlotPriority', 'V2modelsIntentTimeouts', 'V2modelsSlotMultipleValuesSetting', 'V2modelsSlotObfuscationSetting', 'V2modelsSlotSubSlotSetting', 'V2modelsSlotSubSlotSettingSlotSpecification', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsSlotTimeouts', 'V2modelsSlotTypeCompositeSlotTypeSetting', 'V2modelsSlotTypeCompositeSlotTypeSettingSubSlot', 'V2modelsSlotTypeExternalSourceSetting', ..., ..., 'V2modelsSlotTypeSlotTypeValue', 'V2modelsSlotTypeSlotTypeValueSampleValue', 'V2modelsSlotTypeSlotTypeValueSynonym', 'V2modelsSlotTypeTimeouts', 'V2modelsSlotTypeValueSelectionSetting', ..., 'V2modelsSlotTypeValueSelectionSettingRegexFilter', 'V2modelsSlotValueElicitationSetting', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'V2modelsSlotValueElicitationSettingSampleUtterance', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'GetSlotTypeEnumerationValueResult']
@pulumi.output_type
class BotAbortStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, messages: Sequence[outputs.BotAbortStatementMessage], response_card: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Sequence[outputs.BotAbortStatementMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCard")
    def response_card(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class BotAbortStatementMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, group_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNumber")
    def group_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BotAliasConversationLogs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, iam_role_arn: _builtins.str, log_settings: Optional[Sequence[outputs.BotAliasConversationLogsLogSetting]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamRoleArn")
    def iam_role_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logSettings")
    def log_settings(self) -> Optional[Sequence[outputs.BotAliasConversationLogsLogSetting]]:
        
        ...
    


@pulumi.output_type
class BotAliasConversationLogsLogSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, destination: _builtins.str, log_type: _builtins.str, resource_arn: _builtins.str, kms_key_arn: Optional[_builtins.str] = ..., resource_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def destination(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="logType")
    def log_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourcePrefix")
    def resource_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class BotClarificationPrompt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_attempts: _builtins.int, messages: Sequence[outputs.BotClarificationPromptMessage], response_card: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Sequence[outputs.BotClarificationPromptMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCard")
    def response_card(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class BotClarificationPromptMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, group_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNumber")
    def group_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class BotIntent(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, intent_name: _builtins.str, intent_version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intentName")
    def intent_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="intentVersion")
    def intent_version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IntentConclusionStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, messages: Sequence[outputs.IntentConclusionStatementMessage], response_card: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Sequence[outputs.IntentConclusionStatementMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCard")
    def response_card(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IntentConclusionStatementMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, group_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNumber")
    def group_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IntentConfirmationPrompt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_attempts: _builtins.int, messages: Sequence[outputs.IntentConfirmationPromptMessage], response_card: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Sequence[outputs.IntentConfirmationPromptMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCard")
    def response_card(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IntentConfirmationPromptMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, group_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNumber")
    def group_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IntentDialogCodeHook(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, message_version: _builtins.str, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageVersion")
    def message_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IntentFollowUpPrompt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, prompt: outputs.IntentFollowUpPromptPrompt, rejection_statement: outputs.IntentFollowUpPromptRejectionStatement) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> outputs.IntentFollowUpPromptPrompt:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rejectionStatement")
    def rejection_statement(self) -> outputs.IntentFollowUpPromptRejectionStatement:
        
        ...
    


@pulumi.output_type
class IntentFollowUpPromptPrompt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_attempts: _builtins.int, messages: Sequence[outputs.IntentFollowUpPromptPromptMessage], response_card: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Sequence[outputs.IntentFollowUpPromptPromptMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCard")
    def response_card(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class IntentFollowUpPromptPromptMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, group_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNumber")
    def group_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IntentFollowUpPromptRejectionStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, messages: Sequence[outputs.IntentFollowUpPromptRejectionStatementMessage], response_card: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Sequence[outputs.IntentFollowUpPromptRejectionStatementMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCard")
    def response_card(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IntentFollowUpPromptRejectionStatementMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, group_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNumber")
    def group_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IntentFulfillmentActivity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, code_hook: Optional[outputs.IntentFulfillmentActivityCodeHook] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeHook")
    def code_hook(self) -> Optional[outputs.IntentFulfillmentActivityCodeHook]:
        
        ...
    


@pulumi.output_type
class IntentFulfillmentActivityCodeHook(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, message_version: _builtins.str, uri: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageVersion")
    def message_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class IntentRejectionStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, messages: Sequence[outputs.IntentRejectionStatementMessage], response_card: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Sequence[outputs.IntentRejectionStatementMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCard")
    def response_card(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IntentRejectionStatementMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, group_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNumber")
    def group_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class IntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, slot_constraint: _builtins.str, slot_type: _builtins.str, description: Optional[_builtins.str] = ..., priority: Optional[_builtins.int] = ..., response_card: Optional[_builtins.str] = ..., sample_utterances: Optional[Sequence[_builtins.str]] = ..., slot_type_version: Optional[_builtins.str] = ..., value_elicitation_prompt: Optional[outputs.IntentSlotValueElicitationPrompt] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotConstraint")
    def slot_constraint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotType")
    def slot_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCard")
    def response_card(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleUtterances")
    def sample_utterances(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotTypeVersion")
    def slot_type_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueElicitationPrompt")
    def value_elicitation_prompt(self) -> Optional[outputs.IntentSlotValueElicitationPrompt]:
        
        ...
    


@pulumi.output_type
class IntentSlotValueElicitationPrompt(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_attempts: _builtins.int, messages: Sequence[outputs.IntentSlotValueElicitationPromptMessage], response_card: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxAttempts")
    def max_attempts(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Sequence[outputs.IntentSlotValueElicitationPromptMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCard")
    def response_card(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class IntentSlotValueElicitationPromptMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, group_number: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupNumber")
    def group_number(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class SlotTypeEnumerationValue(dict):
    def __init__(__self__, *, value: _builtins.str, synonyms: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def synonyms(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsBotDataPrivacy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, child_directed: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childDirected")
    def child_directed(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class V2modelsBotLocaleTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsBotLocaleVoiceSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, voice_id: _builtins.str, engine: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceId")
    def voice_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsBotMember(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, alias_id: _builtins.str, alias_name: _builtins.str, id: _builtins.str, name: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aliasId")
    def alias_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aliasName")
    def alias_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsBotTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsBotVersionLocaleSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, source_bot_version: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceBotVersion")
    def source_bot_version(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsBotVersionTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: Optional[_builtins.bool] = ..., closing_response: Optional[outputs.V2modelsIntentClosingSettingClosingResponse] = ..., conditional: Optional[outputs.V2modelsIntentClosingSettingConditional] = ..., next_step: Optional[outputs.V2modelsIntentClosingSettingNextStep] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="closingResponse")
    def closing_response(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditional(self) -> Optional[outputs.V2modelsIntentClosingSettingConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentClosingSettingNextStep]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingClosingResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingClosingResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentClosingSettingNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentClosingSettingNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentClosingSettingNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentClosingSettingNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentClosingSettingNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentClosingSettingNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentClosingSettingNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentClosingSettingNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentClosingSettingNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: Optional[_builtins.bool] = ..., code_hook: Optional[outputs.V2modelsIntentConfirmationSettingCodeHook] = ..., confirmation_conditional: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditional] = ..., confirmation_next_step: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationNextStep] = ..., confirmation_response: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponse] = ..., declination_conditional: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditional] = ..., declination_next_step: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationNextStep] = ..., declination_response: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponse] = ..., elicitation_code_hook: Optional[outputs.V2modelsIntentConfirmationSettingElicitationCodeHook] = ..., failure_conditional: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditional] = ..., failure_next_step: Optional[outputs.V2modelsIntentConfirmationSettingFailureNextStep] = ..., failure_response: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponse] = ..., prompt_specification: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeHook")
    def code_hook(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHook]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationConditional")
    def confirmation_conditional(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationNextStep")
    def confirmation_next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confirmationResponse")
    def confirmation_response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="declinationConditional")
    def declination_conditional(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="declinationNextStep")
    def declination_next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="declinationResponse")
    def declination_response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="elicitationCodeHook")
    def elicitation_code_hook(self) -> Optional[outputs.V2modelsIntentConfirmationSettingElicitationCodeHook]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureConditional")
    def failure_conditional(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureNextStep")
    def failure_next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureResponse")
    def failure_response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptSpecification")
    def prompt_specification(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecification]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHook(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, enable_code_hook_invocation: _builtins.bool, invocation_label: Optional[_builtins.str] = ..., post_code_hook_specification: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCodeHookInvocation")
    def enable_code_hook_invocation(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationLabel")
    def invocation_label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postCodeHookSpecification")
    def post_code_hook_specification(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecification]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_conditional: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditional] = ..., failure_next_step: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStep] = ..., failure_response: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponse] = ..., success_conditional: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditional] = ..., success_next_step: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStep] = ..., success_response: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponse] = ..., timeout_conditional: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditional] = ..., timeout_next_step: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStep] = ..., timeout_response: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureConditional")
    def failure_conditional(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureNextStep")
    def failure_next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureResponse")
    def failure_response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successConditional")
    def success_conditional(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successNextStep")
    def success_next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successResponse")
    def success_response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutConditional")
    def timeout_conditional(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutNextStep")
    def timeout_next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutResponse")
    def timeout_response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingConfirmationResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingDeclinationResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingElicitationCodeHook(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_code_hook_invocation: Optional[_builtins.bool] = ..., invocation_label: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCodeHookInvocation")
    def enable_code_hook_invocation(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationLabel")
    def invocation_label(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentConfirmationSettingFailureNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentConfirmationSettingFailureNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentConfirmationSettingFailureNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingFailureResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_retries: _builtins.int, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroup]] = ..., message_selection_strategy: Optional[_builtins.str] = ..., prompt_attempts_specifications: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecification]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroup]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageSelectionStrategy")
    def message_selection_strategy(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptAttemptsSpecifications")
    def prompt_attempts_specifications(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecification]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, allow_interrupt: Optional[_builtins.bool] = ..., allowed_input_types: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAllowedInputTypes] = ..., audio_and_dtmf_input_specification: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecification] = ..., text_input_specification: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationTextInputSpecification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInputTypes")
    def allowed_input_types(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAllowedInputTypes]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioAndDtmfInputSpecification")
    def audio_and_dtmf_input_specification(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textInputSpecification")
    def text_input_specification(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationTextInputSpecification]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAllowedInputTypes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_audio_input: _builtins.bool, allow_dtmf_input: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAudioInput")
    def allow_audio_input(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowDtmfInput")
    def allow_dtmf_input(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_timeout_ms: _builtins.int, audio_specification: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationAudioSpecification] = ..., dtmf_specification: Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationDtmfSpecification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeoutMs")
    def start_timeout_ms(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioSpecification")
    def audio_specification(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationAudioSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtmfSpecification")
    def dtmf_specification(self) -> Optional[outputs.V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationDtmfSpecification]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationAudioSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_timeout_ms: _builtins.int, max_length_ms: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeoutMs")
    def end_timeout_ms(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxLengthMs")
    def max_length_ms(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationDtmfSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deletion_character: _builtins.str, end_character: _builtins.str, end_timeout_ms: _builtins.int, max_length: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionCharacter")
    def deletion_character(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endCharacter")
    def end_character(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeoutMs")
    def end_timeout_ms(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class V2modelsIntentConfirmationSettingPromptSpecificationPromptAttemptsSpecificationTextInputSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_timeout_ms: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeoutMs")
    def start_timeout_ms(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class V2modelsIntentDialogCodeHook(dict):
    def __init__(__self__, *, enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHook(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enabled: _builtins.bool, active: Optional[_builtins.bool] = ..., fulfillment_updates_specification: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecification] = ..., post_fulfillment_status_specification: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fulfillmentUpdatesSpecification")
    def fulfillment_updates_specification(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postFulfillmentStatusSpecification")
    def post_fulfillment_status_specification(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecification]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, start_response: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponse] = ..., timeout_in_seconds: Optional[_builtins.int] = ..., update_response: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startResponse")
    def start_response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateResponse")
    def update_response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., delay_in_seconds: Optional[_builtins.int] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="delayInSeconds")
    def delay_in_seconds(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationStartResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, frequency_in_seconds: _builtins.int, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frequencyInSeconds")
    def frequency_in_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookFulfillmentUpdatesSpecificationUpdateResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_conditional: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditional] = ..., failure_next_step: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStep] = ..., failure_response: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponse] = ..., success_conditional: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditional] = ..., success_next_step: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStep] = ..., success_response: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponse] = ..., timeout_conditional: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditional] = ..., timeout_next_step: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStep] = ..., timeout_response: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureConditional")
    def failure_conditional(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureNextStep")
    def failure_next_step(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureResponse")
    def failure_response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successConditional")
    def success_conditional(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successNextStep")
    def success_next_step(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successResponse")
    def success_response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutConditional")
    def timeout_conditional(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutNextStep")
    def timeout_next_step(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutResponse")
    def timeout_response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationFailureResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationSuccessResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentFulfillmentCodeHookPostFulfillmentStatusSpecificationTimeoutResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, code_hook: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHook] = ..., conditional: Optional[outputs.V2modelsIntentInitialResponseSettingConditional] = ..., initial_response: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponse] = ..., next_step: Optional[outputs.V2modelsIntentInitialResponseSettingNextStep] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeHook")
    def code_hook(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHook]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditional(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialResponse")
    def initial_response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingNextStep]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHook(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, enable_code_hook_invocation: _builtins.bool, invocation_label: Optional[_builtins.str] = ..., post_code_hook_specification: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCodeHookInvocation")
    def enable_code_hook_invocation(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invocationLabel")
    def invocation_label(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="postCodeHookSpecification")
    def post_code_hook_specification(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecification]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_conditional: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditional] = ..., failure_next_step: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStep] = ..., failure_response: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponse] = ..., success_conditional: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditional] = ..., success_next_step: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStep] = ..., success_response: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponse] = ..., timeout_conditional: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditional] = ..., timeout_next_step: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStep] = ..., timeout_response: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureConditional")
    def failure_conditional(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureNextStep")
    def failure_next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureResponse")
    def failure_response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successConditional")
    def success_conditional(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successNextStep")
    def success_next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successResponse")
    def success_response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutConditional")
    def timeout_conditional(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditional]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutNextStep")
    def timeout_next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutResponse")
    def timeout_response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationFailureResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationSuccessResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingCodeHookPostCodeHookSpecificationTimeoutResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditional(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: _builtins.bool, conditional_branches: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranch]] = ..., default_branch: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalBranches")
    def conditional_branches(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBranch")
    def default_branch(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranch]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, condition: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchCondition] = ..., next_step: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expressionString")
    def expression_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalConditionalBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, next_step: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStep] = ..., response: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nextStep")
    def next_step(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStep]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponse]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingConditionalDefaultBranchResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessagePlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationCustomPayload]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationImageResponseCard]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationPlainTextMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationSsmlMessage]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationImageResponseCardButton]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingInitialResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingNextStep(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, dialog_action: Optional[outputs.V2modelsIntentInitialResponseSettingNextStepDialogAction] = ..., intent: Optional[outputs.V2modelsIntentInitialResponseSettingNextStepIntent] = ..., session_attributes: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogAction")
    def dialog_action(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingNextStepDialogAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingNextStepIntent]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionAttributes")
    def session_attributes(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingNextStepDialogAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, slot_to_elicit: Optional[_builtins.str] = ..., suppress_next_message: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotToElicit")
    def slot_to_elicit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="suppressNextMessage")
    def suppress_next_message(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingNextStepIntent(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., slots: Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingNextStepIntentSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def slots(self) -> Optional[Sequence[outputs.V2modelsIntentInitialResponseSettingNextStepIntentSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingNextStepIntentSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, shape: Optional[_builtins.str] = ..., value: Optional[outputs.V2modelsIntentInitialResponseSettingNextStepIntentSlotValue] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def shape(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[outputs.V2modelsIntentInitialResponseSettingNextStepIntentSlotValue]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInitialResponseSettingNextStepIntentSlotValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, interpreted_value: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpretedValue")
    def interpreted_value(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentInputContext(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentKendraConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kendra_index: _builtins.str, query_filter_string: Optional[_builtins.str] = ..., query_filter_string_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kendraIndex")
    def kendra_index(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFilterString")
    def query_filter_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFilterStringEnabled")
    def query_filter_string_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentOutputContext(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, time_to_live_in_seconds: _builtins.int, turns_to_live: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToLiveInSeconds")
    def time_to_live_in_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="turnsToLive")
    def turns_to_live(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class V2modelsIntentQnaIntentConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bedrock_model_configuration: Optional[outputs.V2modelsIntentQnaIntentConfigurationBedrockModelConfiguration] = ..., data_source_configuration: Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bedrockModelConfiguration")
    def bedrock_model_configuration(self) -> Optional[outputs.V2modelsIntentQnaIntentConfigurationBedrockModelConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSourceConfiguration")
    def data_source_configuration(self) -> Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfiguration]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentQnaIntentConfigurationBedrockModelConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, model_arn: _builtins.str, custom_prompt: Optional[_builtins.str] = ..., guardrail: Optional[outputs.V2modelsIntentQnaIntentConfigurationBedrockModelConfigurationGuardrail] = ..., trace_status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelArn")
    def model_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPrompt")
    def custom_prompt(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def guardrail(self) -> Optional[outputs.V2modelsIntentQnaIntentConfigurationBedrockModelConfigurationGuardrail]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="traceStatus")
    def trace_status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentQnaIntentConfigurationBedrockModelConfigurationGuardrail(dict):
    def __init__(__self__, *, identifier: _builtins.str, version: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentQnaIntentConfigurationDataSourceConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bedrock_knowledge_store_configuration: Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationBedrockKnowledgeStoreConfiguration] = ..., kendra_configuration: Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationKendraConfiguration] = ..., opensearch_configuration: Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationOpensearchConfiguration] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bedrockKnowledgeStoreConfiguration")
    def bedrock_knowledge_store_configuration(self) -> Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationBedrockKnowledgeStoreConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kendraConfiguration")
    def kendra_configuration(self) -> Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationKendraConfiguration]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="opensearchConfiguration")
    def opensearch_configuration(self) -> Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationOpensearchConfiguration]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentQnaIntentConfigurationDataSourceConfigurationBedrockKnowledgeStoreConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, bedrock_knowledge_base_arn: _builtins.str, exact_response: Optional[_builtins.bool] = ..., exact_response_fields: Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationBedrockKnowledgeStoreConfigurationExactResponseFields] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bedrockKnowledgeBaseArn")
    def bedrock_knowledge_base_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exactResponse")
    def exact_response(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exactResponseFields")
    def exact_response_fields(self) -> Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationBedrockKnowledgeStoreConfigurationExactResponseFields]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentQnaIntentConfigurationDataSourceConfigurationBedrockKnowledgeStoreConfigurationExactResponseFields(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, answer_field: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="answerField")
    def answer_field(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentQnaIntentConfigurationDataSourceConfigurationKendraConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kendra_index: _builtins.str, exact_response: Optional[_builtins.bool] = ..., query_filter_string: Optional[_builtins.str] = ..., query_filter_string_enabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kendraIndex")
    def kendra_index(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exactResponse")
    def exact_response(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFilterString")
    def query_filter_string(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryFilterStringEnabled")
    def query_filter_string_enabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentQnaIntentConfigurationDataSourceConfigurationOpensearchConfiguration(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_endpoint: _builtins.str, index_name: _builtins.str, exact_response: Optional[_builtins.bool] = ..., exact_response_fields: Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationOpensearchConfigurationExactResponseFields] = ..., include_fields: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainEndpoint")
    def domain_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="indexName")
    def index_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exactResponse")
    def exact_response(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exactResponseFields")
    def exact_response_fields(self) -> Optional[outputs.V2modelsIntentQnaIntentConfigurationDataSourceConfigurationOpensearchConfigurationExactResponseFields]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includeFields")
    def include_fields(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class V2modelsIntentQnaIntentConfigurationDataSourceConfigurationOpensearchConfigurationExactResponseFields(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, answer_field: _builtins.str, question_field: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="answerField")
    def answer_field(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="questionField")
    def question_field(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentSampleUtterance(dict):
    def __init__(__self__, *, utterance: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def utterance(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentSlotPriority(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, priority: _builtins.int, slot_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotId")
    def slot_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsIntentTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotMultipleValuesSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_multiple_values: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowMultipleValues")
    def allow_multiple_values(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotObfuscationSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, obfuscation_setting_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="obfuscationSettingType")
    def obfuscation_setting_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expression: Optional[_builtins.str] = ..., slot_specifications: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecification]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotSpecifications")
    def slot_specifications(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecification]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, slot_type_id: _builtins.str, value_elicitation_settings: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSetting]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotTypeId")
    def slot_type_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="valueElicitationSettings")
    def value_elicitation_settings(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSetting]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_value_specifications: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingDefaultValueSpecification]] = ..., prompt_specification: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecification] = ..., sample_utterances: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingSampleUtterance]] = ..., wait_and_continue_specifications: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecification]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValueSpecifications")
    def default_value_specifications(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingDefaultValueSpecification]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptSpecification")
    def prompt_specification(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleUtterances")
    def sample_utterances(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingSampleUtterance]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitAndContinueSpecifications")
    def wait_and_continue_specifications(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecification]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingDefaultValueSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_value_lists: Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingDefaultValueSpecificationDefaultValueList]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValueLists")
    def default_value_lists(self) -> Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingDefaultValueSpecificationDefaultValueList]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingDefaultValueSpecificationDefaultValueList(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_retries: _builtins.int, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroup]] = ..., message_selection_strategy: Optional[_builtins.str] = ..., prompt_attempts_specifications: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecification]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroup]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageSelectionStrategy")
    def message_selection_strategy(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptAttemptsSpecifications")
    def prompt_attempts_specifications(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecification]]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessagePlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationPlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, allow_interrupt: Optional[_builtins.bool] = ..., allowed_input_types: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAllowedInputTypes] = ..., audio_and_dtmf_input_specification: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecification] = ..., text_input_specification: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationTextInputSpecification] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInputTypes")
    def allowed_input_types(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAllowedInputTypes]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioAndDtmfInputSpecification")
    def audio_and_dtmf_input_specification(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecification]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textInputSpecification")
    def text_input_specification(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationTextInputSpecification]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAllowedInputTypes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_audio_input: _builtins.bool, allow_dtmf_input: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAudioInput")
    def allow_audio_input(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowDtmfInput")
    def allow_dtmf_input(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_timeout_ms: _builtins.int, audio_specification: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationAudioSpecification] = ..., dtmf_specification: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationDtmfSpecification] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeoutMs")
    def start_timeout_ms(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioSpecification")
    def audio_specification(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationAudioSpecification]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtmfSpecification")
    def dtmf_specification(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationDtmfSpecification]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationAudioSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_timeout_ms: _builtins.int, max_length_ms: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeoutMs")
    def end_timeout_ms(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxLengthMs")
    def max_length_ms(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationDtmfSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deletion_character: _builtins.str, end_character: _builtins.str, end_timeout_ms: _builtins.int, max_length: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionCharacter")
    def deletion_character(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endCharacter")
    def end_character(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeoutMs")
    def end_timeout_ms(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationTextInputSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_timeout_ms: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeoutMs")
    def start_timeout_ms(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingSampleUtterance(dict):
    def __init__(__self__, *, utterance: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def utterance(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: Optional[_builtins.bool] = ..., continue_responses: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponse]] = ..., still_waiting_responses: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponse]] = ..., waiting_responses: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continueResponses")
    def continue_responses(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stillWaitingResponses")
    def still_waiting_responses(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitingResponses")
    def waiting_responses(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponse]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessagePlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationPlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, frequency_in_seconds: _builtins.int, timeout_in_seconds: _builtins.int, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frequencyInSeconds")
    def frequency_in_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroup]]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessagePlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationPlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessagePlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationPlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotSubSlotSettingSlotSpecificationValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeCompositeSlotTypeSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, sub_slots: Optional[Sequence[outputs.V2modelsSlotTypeCompositeSlotTypeSettingSubSlot]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="subSlots")
    def sub_slots(self) -> Optional[Sequence[outputs.V2modelsSlotTypeCompositeSlotTypeSettingSubSlot]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeCompositeSlotTypeSettingSubSlot(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, slot_type_id: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotTypeId")
    def slot_type_id(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeExternalSourceSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, grammar_slot_type_settings: Optional[Sequence[outputs.V2modelsSlotTypeExternalSourceSettingGrammarSlotTypeSetting]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="grammarSlotTypeSettings")
    def grammar_slot_type_settings(self) -> Optional[Sequence[outputs.V2modelsSlotTypeExternalSourceSettingGrammarSlotTypeSetting]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeExternalSourceSettingGrammarSlotTypeSetting(dict):
    def __init__(__self__, *, sources: Optional[Sequence[outputs.V2modelsSlotTypeExternalSourceSettingGrammarSlotTypeSettingSource]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Optional[Sequence[outputs.V2modelsSlotTypeExternalSourceSettingGrammarSlotTypeSettingSource]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeExternalSourceSettingGrammarSlotTypeSettingSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, kms_key_arn: _builtins.str, s3_bucket_name: _builtins.str, s3_object_key: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3BucketName")
    def s3_bucket_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3ObjectKey")
    def s3_object_key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeSlotTypeValue(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, sample_values: Optional[Sequence[outputs.V2modelsSlotTypeSlotTypeValueSampleValue]] = ..., synonyms: Optional[Sequence[outputs.V2modelsSlotTypeSlotTypeValueSynonym]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleValues")
    def sample_values(self) -> Optional[Sequence[outputs.V2modelsSlotTypeSlotTypeValueSampleValue]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def synonyms(self) -> Optional[Sequence[outputs.V2modelsSlotTypeSlotTypeValueSynonym]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeSlotTypeValueSampleValue(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeSlotTypeValueSynonym(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ..., delete: Optional[_builtins.str] = ..., update: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeValueSelectionSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, resolution_strategy: _builtins.str, advanced_recognition_settings: Optional[Sequence[outputs.V2modelsSlotTypeValueSelectionSettingAdvancedRecognitionSetting]] = ..., regex_filters: Optional[Sequence[outputs.V2modelsSlotTypeValueSelectionSettingRegexFilter]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resolutionStrategy")
    def resolution_strategy(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedRecognitionSettings")
    def advanced_recognition_settings(self) -> Optional[Sequence[outputs.V2modelsSlotTypeValueSelectionSettingAdvancedRecognitionSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexFilters")
    def regex_filters(self) -> Optional[Sequence[outputs.V2modelsSlotTypeValueSelectionSettingRegexFilter]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeValueSelectionSettingAdvancedRecognitionSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audio_recognition_strategy: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioRecognitionStrategy")
    def audio_recognition_strategy(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotTypeValueSelectionSettingRegexFilter(dict):
    def __init__(__self__, *, pattern: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def pattern(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, slot_constraint: _builtins.str, default_value_specifications: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingDefaultValueSpecification]] = ..., prompt_specification: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecification] = ..., sample_utterances: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingSampleUtterance]] = ..., slot_resolution_settings: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingSlotResolutionSetting]] = ..., wait_and_continue_specifications: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecification]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotConstraint")
    def slot_constraint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValueSpecifications")
    def default_value_specifications(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingDefaultValueSpecification]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptSpecification")
    def prompt_specification(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecification]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleUtterances")
    def sample_utterances(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingSampleUtterance]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotResolutionSettings")
    def slot_resolution_settings(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingSlotResolutionSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitAndContinueSpecifications")
    def wait_and_continue_specifications(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecification]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingDefaultValueSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_value_lists: Sequence[outputs.V2modelsSlotValueElicitationSettingDefaultValueSpecificationDefaultValueList]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValueLists")
    def default_value_lists(self) -> Sequence[outputs.V2modelsSlotValueElicitationSettingDefaultValueSpecificationDefaultValueList]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingDefaultValueSpecificationDefaultValueList(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, max_retries: _builtins.int, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroup]] = ..., message_selection_strategy: Optional[_builtins.str] = ..., prompt_attempts_specifications: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecification]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroup]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageSelectionStrategy")
    def message_selection_strategy(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptAttemptsSpecifications")
    def prompt_attempts_specifications(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecification]]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessagePlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationPlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, map_block_key: _builtins.str, allow_interrupt: Optional[_builtins.bool] = ..., allowed_input_types: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAllowedInputTypes] = ..., audio_and_dtmf_input_specification: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecification] = ..., text_input_specification: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationTextInputSpecification] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mapBlockKey")
    def map_block_key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedInputTypes")
    def allowed_input_types(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAllowedInputTypes]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioAndDtmfInputSpecification")
    def audio_and_dtmf_input_specification(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecification]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textInputSpecification")
    def text_input_specification(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationTextInputSpecification]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAllowedInputTypes(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_audio_input: _builtins.bool, allow_dtmf_input: _builtins.bool) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowAudioInput")
    def allow_audio_input(self) -> _builtins.bool:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowDtmfInput")
    def allow_dtmf_input(self) -> _builtins.bool:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_timeout_ms: _builtins.int, audio_specification: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationAudioSpecification] = ..., dtmf_specification: Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationDtmfSpecification] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeoutMs")
    def start_timeout_ms(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioSpecification")
    def audio_specification(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationAudioSpecification]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtmfSpecification")
    def dtmf_specification(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationDtmfSpecification]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationAudioSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, end_timeout_ms: _builtins.int, max_length_ms: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeoutMs")
    def end_timeout_ms(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxLengthMs")
    def max_length_ms(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationAudioAndDtmfInputSpecificationDtmfSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deletion_character: _builtins.str, end_character: _builtins.str, end_timeout_ms: _builtins.int, max_length: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deletionCharacter")
    def deletion_character(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endCharacter")
    def end_character(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTimeoutMs")
    def end_timeout_ms(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingPromptSpecificationPromptAttemptsSpecificationTextInputSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, start_timeout_ms: _builtins.int) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTimeoutMs")
    def start_timeout_ms(self) -> _builtins.int:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingSampleUtterance(dict):
    def __init__(__self__, *, utterance: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def utterance(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingSlotResolutionSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, slot_resolution_strategy: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="slotResolutionStrategy")
    def slot_resolution_strategy(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecification(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, active: Optional[_builtins.bool] = ..., continue_responses: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponse]] = ..., still_waiting_responses: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponse]] = ..., waiting_responses: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def active(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="continueResponses")
    def continue_responses(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stillWaitingResponses")
    def still_waiting_responses(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitingResponses")
    def waiting_responses(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponse]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessagePlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationPlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationContinueResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, frequency_in_seconds: _builtins.int, timeout_in_seconds: _builtins.int, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="frequencyInSeconds")
    def frequency_in_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroup]]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessagePlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationPlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationStillWaitingResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, allow_interrupt: Optional[_builtins.bool] = ..., message_groups: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroup]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowInterrupt")
    def allow_interrupt(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageGroups")
    def message_groups(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroup]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroup(dict):
    def __init__(__self__, *, message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessage] = ..., variations: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariation]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def variations(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariation]]:
        
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessagePlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessagePlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessagePlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupMessageSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariation(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_payload: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationCustomPayload] = ..., image_response_card: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCard] = ..., plain_text_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationPlainTextMessage] = ..., ssml_message: Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationSsmlMessage] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPayload")
    def custom_payload(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationCustomPayload]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageResponseCard")
    def image_response_card(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCard]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="plainTextMessage")
    def plain_text_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationPlainTextMessage]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlMessage")
    def ssml_message(self) -> Optional[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationSsmlMessage]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationCustomPayload(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCard(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, title: _builtins.str, buttons: Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCardButton]] = ..., image_url: Optional[_builtins.str] = ..., subtitle: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def buttons(self) -> Optional[Sequence[outputs.V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCardButton]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subtitle(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationImageResponseCardButton(dict):
    def __init__(__self__, *, text: _builtins.str, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationPlainTextMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class V2modelsSlotValueElicitationSettingWaitAndContinueSpecificationWaitingResponseMessageGroupVariationSsmlMessage(dict):
    def __init__(__self__, *, value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetSlotTypeEnumerationValueResult(dict):
    def __init__(__self__, *, synonyms: Sequence[_builtins.str], value: _builtins.str) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def synonyms(self) -> Sequence[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


