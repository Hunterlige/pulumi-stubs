

import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RegexPatternSetRegularExpression', 'RuleGroupCustomResponseBody', 'RuleGroupRule', 'RuleGroupRuleAction', 'RuleGroupRuleActionAllow', 'RuleGroupRuleActionAllowCustomRequestHandling', ..., 'RuleGroupRuleActionBlock', 'RuleGroupRuleActionBlockCustomResponse', ..., 'RuleGroupRuleActionCaptcha', 'RuleGroupRuleActionCaptchaCustomRequestHandling', ..., 'RuleGroupRuleActionChallenge', 'RuleGroupRuleActionChallengeCustomRequestHandling', ..., 'RuleGroupRuleActionCount', 'RuleGroupRuleActionCountCustomRequestHandling', ..., 'RuleGroupRuleCaptchaConfig', 'RuleGroupRuleCaptchaConfigImmunityTimeProperty', 'RuleGroupRuleRuleLabel', 'RuleGroupRuleStatement', 'RuleGroupRuleStatementAndStatement', 'RuleGroupRuleStatementAsnMatchStatement', ..., 'RuleGroupRuleStatementByteMatchStatement', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'RuleGroupRuleStatementGeoMatchStatement', ..., 'RuleGroupRuleStatementIpSetReferenceStatement', ..., 'RuleGroupRuleStatementLabelMatchStatement', 'RuleGroupRuleStatementNotStatement', 'RuleGroupRuleStatementOrStatement', 'RuleGroupRuleStatementRateBasedStatement', 'RuleGroupRuleStatementRateBasedStatementCustomKey', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'RuleGroupRuleStatementRegexMatchStatement', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'RuleGroupRuleStatementSizeConstraintStatement', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'RuleGroupRuleStatementSqliMatchStatement', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'RuleGroupRuleStatementXssMatchStatement', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'RuleGroupRuleVisibilityConfig', 'RuleGroupVisibilityConfig', 'WebAclAssociationConfig', 'WebAclAssociationConfigRequestBody', 'WebAclAssociationConfigRequestBodyApiGateway', 'WebAclAssociationConfigRequestBodyAppRunnerService', 'WebAclAssociationConfigRequestBodyCloudfront', 'WebAclAssociationConfigRequestBodyCognitoUserPool', ..., 'WebAclCaptchaConfig', 'WebAclCaptchaConfigImmunityTimeProperty', 'WebAclChallengeConfig', 'WebAclChallengeConfigImmunityTimeProperty', 'WebAclCustomResponseBody', 'WebAclDataProtectionConfig', 'WebAclDataProtectionConfigDataProtection', 'WebAclDataProtectionConfigDataProtectionField', 'WebAclDefaultAction', 'WebAclDefaultActionAllow', 'WebAclDefaultActionAllowCustomRequestHandling', ..., 'WebAclDefaultActionBlock', 'WebAclDefaultActionBlockCustomResponse', ..., 'WebAclLoggingConfigurationLoggingFilter', 'WebAclLoggingConfigurationLoggingFilterFilter', ..., ..., ..., 'WebAclLoggingConfigurationRedactedField', 'WebAclLoggingConfigurationRedactedFieldMethod', 'WebAclLoggingConfigurationRedactedFieldQueryString', ..., 'WebAclLoggingConfigurationRedactedFieldUriPath', 'WebAclRule', 'WebAclRuleAction', 'WebAclRuleActionAllow', 'WebAclRuleActionAllowCustomRequestHandling', ..., 'WebAclRuleActionBlock', 'WebAclRuleActionBlockCustomResponse', 'WebAclRuleActionBlockCustomResponseResponseHeader', 'WebAclRuleActionCaptcha', 'WebAclRuleActionCaptchaCustomRequestHandling', ..., 'WebAclRuleActionChallenge', 'WebAclRuleActionChallengeCustomRequestHandling', ..., 'WebAclRuleActionCount', 'WebAclRuleActionCountCustomRequestHandling', ..., 'WebAclRuleCaptchaConfig', 'WebAclRuleCaptchaConfigImmunityTimeProperty', 'WebAclRuleChallengeConfig', 'WebAclRuleChallengeConfigImmunityTimeProperty', 'WebAclRuleGroupAssociationManagedRuleGroup', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleGroupAssociationRuleGroupReference', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleGroupAssociationTimeouts', 'WebAclRuleGroupAssociationVisibilityConfig', 'WebAclRuleOverrideAction', 'WebAclRuleOverrideActionCount', 'WebAclRuleOverrideActionNone', 'WebAclRuleRuleLabel', 'WebAclRuleStatement', 'WebAclRuleStatementAndStatement', 'WebAclRuleStatementAsnMatchStatement', ..., 'WebAclRuleStatementByteMatchStatement', 'WebAclRuleStatementByteMatchStatementFieldToMatch', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleStatementGeoMatchStatement', ..., 'WebAclRuleStatementIpSetReferenceStatement', ..., 'WebAclRuleStatementLabelMatchStatement', 'WebAclRuleStatementManagedRuleGroupStatement', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleStatementNotStatement', 'WebAclRuleStatementOrStatement', 'WebAclRuleStatementRateBasedStatement', 'WebAclRuleStatementRateBasedStatementCustomKey', 'WebAclRuleStatementRateBasedStatementCustomKeyAsn', ..., ..., ..., ..., ..., ..., 'WebAclRuleStatementRateBasedStatementCustomKeyIp', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleStatementRegexMatchStatement', 'WebAclRuleStatementRegexMatchStatementFieldToMatch', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleStatementRuleGroupReferenceStatement', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleStatementSizeConstraintStatement', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleStatementSqliMatchStatement', 'WebAclRuleStatementSqliMatchStatementFieldToMatch', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleStatementXssMatchStatement', 'WebAclRuleStatementXssMatchStatementFieldToMatch', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'WebAclRuleVisibilityConfig', 'WebAclVisibilityConfig', 'GetManagedRuleGroupAvailableLabelResult', 'GetManagedRuleGroupConsumedLabelResult', 'GetManagedRuleGroupRuleResult', 'GetManagedRuleGroupRuleActionResult', 'GetManagedRuleGroupRuleActionAllowResult', ..., ..., 'GetManagedRuleGroupRuleActionBlockResult', ..., ..., 'GetManagedRuleGroupRuleActionCaptchaResult', ..., ..., 'GetManagedRuleGroupRuleActionChallengeResult', ..., ..., 'GetManagedRuleGroupRuleActionCountResult', ..., ..., 'GetRegexPatternSetRegularExpressionResult']
@pulumi.output_type
class RegexPatternSetRegularExpression(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regex_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupCustomResponseBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, key: _builtins.str) -> None:
        
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
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: outputs.RuleGroupRuleAction, name: _builtins.str, priority: _builtins.int, statement: outputs.RuleGroupRuleStatement, visibility_config: outputs.RuleGroupRuleVisibilityConfig, captcha_config: Optional[outputs.RuleGroupRuleCaptchaConfig] = ..., rule_labels: Optional[Sequence[outputs.RuleGroupRuleRuleLabel]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> outputs.RuleGroupRuleAction:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statement(self) -> outputs.RuleGroupRuleStatement:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> outputs.RuleGroupRuleVisibilityConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="captchaConfig")
    def captcha_config(self) -> Optional[outputs.RuleGroupRuleCaptchaConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleLabels")
    def rule_labels(self) -> Optional[Sequence[outputs.RuleGroupRuleRuleLabel]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleAction(dict):
    def __init__(__self__, *, allow: Optional[outputs.RuleGroupRuleActionAllow] = ..., block: Optional[outputs.RuleGroupRuleActionBlock] = ..., captcha: Optional[outputs.RuleGroupRuleActionCaptcha] = ..., challenge: Optional[outputs.RuleGroupRuleActionChallenge] = ..., count: Optional[outputs.RuleGroupRuleActionCount] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[outputs.RuleGroupRuleActionAllow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def block(self) -> Optional[outputs.RuleGroupRuleActionBlock]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def captcha(self) -> Optional[outputs.RuleGroupRuleActionCaptcha]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def challenge(self) -> Optional[outputs.RuleGroupRuleActionChallenge]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[outputs.RuleGroupRuleActionCount]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionAllow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.RuleGroupRuleActionAllowCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.RuleGroupRuleActionAllowCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionAllowCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionAllowCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionBlock(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_response: Optional[outputs.RuleGroupRuleActionBlockCustomResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponse")
    def custom_response(self) -> Optional[outputs.RuleGroupRuleActionBlockCustomResponse]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionBlockCustomResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response_code: _builtins.int, custom_response_body_key: Optional[_builtins.str] = ..., response_headers: Optional[Sequence[outputs.RuleGroupRuleActionBlockCustomResponseResponseHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodyKey")
    def custom_response_body_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Optional[Sequence[outputs.RuleGroupRuleActionBlockCustomResponseResponseHeader]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionBlockCustomResponseResponseHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionCaptcha(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.RuleGroupRuleActionCaptchaCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.RuleGroupRuleActionCaptchaCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionCaptchaCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.RuleGroupRuleActionCaptchaCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.RuleGroupRuleActionCaptchaCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionCaptchaCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionChallenge(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.RuleGroupRuleActionChallengeCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.RuleGroupRuleActionChallengeCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionChallengeCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.RuleGroupRuleActionChallengeCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.RuleGroupRuleActionChallengeCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionChallengeCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionCount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.RuleGroupRuleActionCountCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.RuleGroupRuleActionCountCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionCountCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.RuleGroupRuleActionCountCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.RuleGroupRuleActionCountCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleActionCountCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleCaptchaConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time_property: Optional[outputs.RuleGroupRuleCaptchaConfigImmunityTimeProperty] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTimeProperty")
    def immunity_time_property(self) -> Optional[outputs.RuleGroupRuleCaptchaConfigImmunityTimeProperty]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleCaptchaConfigImmunityTimeProperty(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTime")
    def immunity_time(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleRuleLabel(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, and_statement: Optional[outputs.RuleGroupRuleStatementAndStatement] = ..., asn_match_statement: Optional[outputs.RuleGroupRuleStatementAsnMatchStatement] = ..., byte_match_statement: Optional[outputs.RuleGroupRuleStatementByteMatchStatement] = ..., geo_match_statement: Optional[outputs.RuleGroupRuleStatementGeoMatchStatement] = ..., ip_set_reference_statement: Optional[outputs.RuleGroupRuleStatementIpSetReferenceStatement] = ..., label_match_statement: Optional[outputs.RuleGroupRuleStatementLabelMatchStatement] = ..., not_statement: Optional[outputs.RuleGroupRuleStatementNotStatement] = ..., or_statement: Optional[outputs.RuleGroupRuleStatementOrStatement] = ..., rate_based_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatement] = ..., regex_match_statement: Optional[outputs.RuleGroupRuleStatementRegexMatchStatement] = ..., regex_pattern_set_reference_statement: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatement] = ..., size_constraint_statement: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatement] = ..., sqli_match_statement: Optional[outputs.RuleGroupRuleStatementSqliMatchStatement] = ..., xss_match_statement: Optional[outputs.RuleGroupRuleStatementXssMatchStatement] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="andStatement")
    def and_statement(self) -> Optional[outputs.RuleGroupRuleStatementAndStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnMatchStatement")
    def asn_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementAsnMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="byteMatchStatement")
    def byte_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMatchStatement")
    def geo_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementGeoMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetReferenceStatement")
    def ip_set_reference_statement(self) -> Optional[outputs.RuleGroupRuleStatementIpSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelMatchStatement")
    def label_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementLabelMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notStatement")
    def not_statement(self) -> Optional[outputs.RuleGroupRuleStatementNotStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orStatement")
    def or_statement(self) -> Optional[outputs.RuleGroupRuleStatementOrStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateBasedStatement")
    def rate_based_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexMatchStatement")
    def regex_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexPatternSetReferenceStatement")
    def regex_pattern_set_reference_statement(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeConstraintStatement")
    def size_constraint_statement(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqliMatchStatement")
    def sqli_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xssMatchStatement")
    def xss_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatement]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementAndStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.RuleGroupRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.RuleGroupRuleStatement]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementAsnMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn_lists: Sequence[_builtins.int], forwarded_ip_config: Optional[outputs.RuleGroupRuleStatementAsnMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnLists")
    def asn_lists(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.RuleGroupRuleStatementAsnMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementAsnMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, positional_constraint: _builtins.str, search_string: _builtins.str, text_transformations: Sequence[outputs.RuleGroupRuleStatementByteMatchStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="positionalConstraint")
    def positional_constraint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchString")
    def search_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementByteMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementByteMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementGeoMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, country_codes: Sequence[_builtins.str], forwarded_ip_config: Optional[outputs.RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCodes")
    def country_codes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementGeoMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementIpSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, ip_set_forwarded_ip_config: Optional[outputs.RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetForwardedIpConfig")
    def ip_set_forwarded_ip_config(self) -> Optional[outputs.RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str, position: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementLabelMatchStatement(dict):
    def __init__(__self__, *, key: _builtins.str, scope: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementNotStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.RuleGroupRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.RuleGroupRuleStatement]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementOrStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.RuleGroupRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.RuleGroupRuleStatement]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, limit: _builtins.int, aggregate_key_type: Optional[_builtins.str] = ..., custom_keys: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKey]] = ..., evaluation_window_sec: Optional[_builtins.int] = ..., forwarded_ip_config: Optional[outputs.RuleGroupRuleStatementRateBasedStatementForwardedIpConfig] = ..., scope_down_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatement] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregateKeyType")
    def aggregate_key_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeys")
    def custom_keys(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationWindowSec")
    def evaluation_window_sec(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementForwardedIpConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeDownStatement")
    def scope_down_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatement]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyAsn] = ..., cookie: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyCookie] = ..., forwarded_ip: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyForwardedIp] = ..., header: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyHeader] = ..., http_method: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyHttpMethod] = ..., ip: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyIp] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyJa4Fingerprint] = ..., label_namespace: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyLabelNamespace] = ..., query_argument: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyQueryArgument] = ..., query_string: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyQueryString] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyAsn]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookie(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyCookie]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIp")
    def forwarded_ip(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyForwardedIp]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyHttpMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyIp]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelNamespace")
    def label_namespace(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyLabelNamespace]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryArgument")
    def query_argument(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyAsn(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyCookie(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyCookieTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyCookieTextTransformation]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyCookieTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyForwardedIp(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyHeaderTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyHeaderTextTransformation]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyHeaderTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyHttpMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyIp(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyLabelNamespace(dict):
    def __init__(__self__, *, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyQueryArgument(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyQueryArgumentTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyQueryArgumentTextTransformation]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyQueryArgumentTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyQueryString(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyQueryStringTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyQueryStringTextTransformation]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyQueryStringTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyUriPath(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyUriPathTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementCustomKeyUriPathTextTransformation]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementCustomKeyUriPathTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, and_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementAndStatement] = ..., asn_match_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatement] = ..., byte_match_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatement] = ..., geo_match_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatement] = ..., ip_set_reference_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatement] = ..., label_match_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementLabelMatchStatement] = ..., not_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementNotStatement] = ..., or_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementOrStatement] = ..., regex_match_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatement] = ..., regex_pattern_set_reference_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatement] = ..., size_constraint_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatement] = ..., sqli_match_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatement] = ..., xss_match_statement: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatement] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="andStatement")
    def and_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementAndStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnMatchStatement")
    def asn_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="byteMatchStatement")
    def byte_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMatchStatement")
    def geo_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetReferenceStatement")
    def ip_set_reference_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelMatchStatement")
    def label_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementLabelMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notStatement")
    def not_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementNotStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orStatement")
    def or_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementOrStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexMatchStatement")
    def regex_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexPatternSetReferenceStatement")
    def regex_pattern_set_reference_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeConstraintStatement")
    def size_constraint_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqliMatchStatement")
    def sqli_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xssMatchStatement")
    def xss_match_statement(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatement]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementAndStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.RuleGroupRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.RuleGroupRuleStatement]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn_lists: Sequence[_builtins.int], forwarded_ip_config: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnLists")
    def asn_lists(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, positional_constraint: _builtins.str, search_string: _builtins.str, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="positionalConstraint")
    def positional_constraint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchString")
    def search_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, country_codes: Sequence[_builtins.str], forwarded_ip_config: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCodes")
    def country_codes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, ip_set_forwarded_ip_config: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatementIpSetForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetForwardedIpConfig")
    def ip_set_forwarded_ip_config(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatementIpSetForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatementIpSetForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str, position: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementLabelMatchStatement(dict):
    def __init__(__self__, *, key: _builtins.str, scope: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementNotStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.RuleGroupRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.RuleGroupRuleStatement]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementOrStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.RuleGroupRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.RuleGroupRuleStatement]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regex_string: _builtins.str, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, comparison_operator: _builtins.str, size: _builtins.int, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatch] = ..., sensitivity_level: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatch]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityLevel")
    def sensitivity_level(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regex_string: _builtins.str, text_transformations: Sequence[outputs.RuleGroupRuleStatementRegexMatchStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRegexMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, text_transformations: Sequence[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementRegexPatternSetReferenceStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, comparison_operator: _builtins.str, size: _builtins.int, text_transformations: Sequence[outputs.RuleGroupRuleStatementSizeConstraintStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementSizeConstraintStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSizeConstraintStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.RuleGroupRuleStatementSqliMatchStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatch] = ..., sensitivity_level: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementSqliMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatch]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityLevel")
    def sensitivity_level(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementSqliMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.RuleGroupRuleStatementXssMatchStatementTextTransformation], field_to_match: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.RuleGroupRuleStatementXssMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class RuleGroupRuleStatementXssMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class RuleGroupRuleVisibilityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_metrics_enabled: _builtins.bool, metric_name: _builtins.str, sampled_requests_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetricsEnabled")
    def cloudwatch_metrics_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampledRequestsEnabled")
    def sampled_requests_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class RuleGroupVisibilityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_metrics_enabled: _builtins.bool, metric_name: _builtins.str, sampled_requests_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetricsEnabled")
    def cloudwatch_metrics_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampledRequestsEnabled")
    def sampled_requests_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class WebAclAssociationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, request_bodies: Optional[Sequence[outputs.WebAclAssociationConfigRequestBody]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestBodies")
    def request_bodies(self) -> Optional[Sequence[outputs.WebAclAssociationConfigRequestBody]]:
        
        ...
    


@pulumi.output_type
class WebAclAssociationConfigRequestBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_gateway: Optional[outputs.WebAclAssociationConfigRequestBodyApiGateway] = ..., app_runner_service: Optional[outputs.WebAclAssociationConfigRequestBodyAppRunnerService] = ..., cloudfront: Optional[outputs.WebAclAssociationConfigRequestBodyCloudfront] = ..., cognito_user_pool: Optional[outputs.WebAclAssociationConfigRequestBodyCognitoUserPool] = ..., verified_access_instance: Optional[outputs.WebAclAssociationConfigRequestBodyVerifiedAccessInstance] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiGateway")
    def api_gateway(self) -> Optional[outputs.WebAclAssociationConfigRequestBodyApiGateway]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="appRunnerService")
    def app_runner_service(self) -> Optional[outputs.WebAclAssociationConfigRequestBodyAppRunnerService]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cloudfront(self) -> Optional[outputs.WebAclAssociationConfigRequestBodyCloudfront]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cognitoUserPool")
    def cognito_user_pool(self) -> Optional[outputs.WebAclAssociationConfigRequestBodyCognitoUserPool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="verifiedAccessInstance")
    def verified_access_instance(self) -> Optional[outputs.WebAclAssociationConfigRequestBodyVerifiedAccessInstance]:
        
        ...
    


@pulumi.output_type
class WebAclAssociationConfigRequestBodyApiGateway(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_size_inspection_limit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSizeInspectionLimit")
    def default_size_inspection_limit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclAssociationConfigRequestBodyAppRunnerService(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_size_inspection_limit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSizeInspectionLimit")
    def default_size_inspection_limit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclAssociationConfigRequestBodyCloudfront(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_size_inspection_limit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSizeInspectionLimit")
    def default_size_inspection_limit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclAssociationConfigRequestBodyCognitoUserPool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_size_inspection_limit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSizeInspectionLimit")
    def default_size_inspection_limit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclAssociationConfigRequestBodyVerifiedAccessInstance(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_size_inspection_limit: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSizeInspectionLimit")
    def default_size_inspection_limit(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclCaptchaConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time_property: Optional[outputs.WebAclCaptchaConfigImmunityTimeProperty] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTimeProperty")
    def immunity_time_property(self) -> Optional[outputs.WebAclCaptchaConfigImmunityTimeProperty]:
        
        ...
    


@pulumi.output_type
class WebAclCaptchaConfigImmunityTimeProperty(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTime")
    def immunity_time(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WebAclChallengeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time_property: Optional[outputs.WebAclChallengeConfigImmunityTimeProperty] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTimeProperty")
    def immunity_time_property(self) -> Optional[outputs.WebAclChallengeConfigImmunityTimeProperty]:
        
        ...
    


@pulumi.output_type
class WebAclChallengeConfigImmunityTimeProperty(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTime")
    def immunity_time(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WebAclCustomResponseBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, content: _builtins.str, content_type: _builtins.str, key: _builtins.str) -> None:
        
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
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclDataProtectionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_protections: Optional[Sequence[outputs.WebAclDataProtectionConfigDataProtection]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataProtections")
    def data_protections(self) -> Optional[Sequence[outputs.WebAclDataProtectionConfigDataProtection]]:
        
        ...
    


@pulumi.output_type
class WebAclDataProtectionConfigDataProtection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action: _builtins.str, field: outputs.WebAclDataProtectionConfigDataProtectionField, exclude_rate_based_details: Optional[_builtins.bool] = ..., exclude_rule_match_details: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def field(self) -> outputs.WebAclDataProtectionConfigDataProtectionField:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeRateBasedDetails")
    def exclude_rate_based_details(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeRuleMatchDetails")
    def exclude_rule_match_details(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WebAclDataProtectionConfigDataProtectionField(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, field_type: _builtins.str, field_keys: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldType")
    def field_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldKeys")
    def field_keys(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclDefaultAction(dict):
    def __init__(__self__, *, allow: Optional[outputs.WebAclDefaultActionAllow] = ..., block: Optional[outputs.WebAclDefaultActionBlock] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[outputs.WebAclDefaultActionAllow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def block(self) -> Optional[outputs.WebAclDefaultActionBlock]:
        
        ...
    


@pulumi.output_type
class WebAclDefaultActionAllow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclDefaultActionAllowCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclDefaultActionAllowCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclDefaultActionAllowCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclDefaultActionAllowCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclDefaultActionAllowCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclDefaultActionAllowCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclDefaultActionBlock(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_response: Optional[outputs.WebAclDefaultActionBlockCustomResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponse")
    def custom_response(self) -> Optional[outputs.WebAclDefaultActionBlockCustomResponse]:
        
        ...
    


@pulumi.output_type
class WebAclDefaultActionBlockCustomResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response_code: _builtins.int, custom_response_body_key: Optional[_builtins.str] = ..., response_headers: Optional[Sequence[outputs.WebAclDefaultActionBlockCustomResponseResponseHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodyKey")
    def custom_response_body_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Optional[Sequence[outputs.WebAclDefaultActionBlockCustomResponseResponseHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclDefaultActionBlockCustomResponseResponseHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationLoggingFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_behavior: _builtins.str, filters: Sequence[outputs.WebAclLoggingConfigurationLoggingFilterFilter]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBehavior")
    def default_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filters(self) -> Sequence[outputs.WebAclLoggingConfigurationLoggingFilterFilter]:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationLoggingFilterFilter(dict):
    def __init__(__self__, *, behavior: _builtins.str, conditions: Sequence[outputs.WebAclLoggingConfigurationLoggingFilterFilterCondition], requirement: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def conditions(self) -> Sequence[outputs.WebAclLoggingConfigurationLoggingFilterFilterCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requirement(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationLoggingFilterFilterCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_condition: Optional[outputs.WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition] = ..., label_name_condition: Optional[outputs.WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionCondition")
    def action_condition(self) -> Optional[outputs.WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelNameCondition")
    def label_name_condition(self) -> Optional[outputs.WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition]:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationLoggingFilterFilterConditionActionCondition(dict):
    def __init__(__self__, *, action: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationLoggingFilterFilterConditionLabelNameCondition(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, label_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelName")
    def label_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationRedactedField(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, method: Optional[outputs.WebAclLoggingConfigurationRedactedFieldMethod] = ..., query_string: Optional[outputs.WebAclLoggingConfigurationRedactedFieldQueryString] = ..., single_header: Optional[outputs.WebAclLoggingConfigurationRedactedFieldSingleHeader] = ..., uri_path: Optional[outputs.WebAclLoggingConfigurationRedactedFieldUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclLoggingConfigurationRedactedFieldMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclLoggingConfigurationRedactedFieldQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclLoggingConfigurationRedactedFieldSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclLoggingConfigurationRedactedFieldUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationRedactedFieldMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationRedactedFieldQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationRedactedFieldSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclLoggingConfigurationRedactedFieldUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRule(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, priority: _builtins.int, statement: outputs.WebAclRuleStatement, visibility_config: outputs.WebAclRuleVisibilityConfig, action: Optional[outputs.WebAclRuleAction] = ..., captcha_config: Optional[outputs.WebAclRuleCaptchaConfig] = ..., challenge_config: Optional[outputs.WebAclRuleChallengeConfig] = ..., override_action: Optional[outputs.WebAclRuleOverrideAction] = ..., rule_labels: Optional[Sequence[outputs.WebAclRuleRuleLabel]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statement(self) -> outputs.WebAclRuleStatement:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> outputs.WebAclRuleVisibilityConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[outputs.WebAclRuleAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="captchaConfig")
    def captcha_config(self) -> Optional[outputs.WebAclRuleCaptchaConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="challengeConfig")
    def challenge_config(self) -> Optional[outputs.WebAclRuleChallengeConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideAction")
    def override_action(self) -> Optional[outputs.WebAclRuleOverrideAction]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleLabels")
    def rule_labels(self) -> Optional[Sequence[outputs.WebAclRuleRuleLabel]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleAction(dict):
    def __init__(__self__, *, allow: Optional[outputs.WebAclRuleActionAllow] = ..., block: Optional[outputs.WebAclRuleActionBlock] = ..., captcha: Optional[outputs.WebAclRuleActionCaptcha] = ..., challenge: Optional[outputs.WebAclRuleActionChallenge] = ..., count: Optional[outputs.WebAclRuleActionCount] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[outputs.WebAclRuleActionAllow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def block(self) -> Optional[outputs.WebAclRuleActionBlock]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def captcha(self) -> Optional[outputs.WebAclRuleActionCaptcha]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def challenge(self) -> Optional[outputs.WebAclRuleActionChallenge]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[outputs.WebAclRuleActionCount]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionAllow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleActionAllowCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleActionAllowCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionAllowCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleActionAllowCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleActionAllowCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionAllowCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionBlock(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_response: Optional[outputs.WebAclRuleActionBlockCustomResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponse")
    def custom_response(self) -> Optional[outputs.WebAclRuleActionBlockCustomResponse]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionBlockCustomResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response_code: _builtins.int, custom_response_body_key: Optional[_builtins.str] = ..., response_headers: Optional[Sequence[outputs.WebAclRuleActionBlockCustomResponseResponseHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodyKey")
    def custom_response_body_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Optional[Sequence[outputs.WebAclRuleActionBlockCustomResponseResponseHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionBlockCustomResponseResponseHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionCaptcha(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleActionCaptchaCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleActionCaptchaCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionCaptchaCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleActionCaptchaCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleActionCaptchaCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionCaptchaCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionChallenge(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleActionChallengeCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleActionChallengeCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionChallengeCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleActionChallengeCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleActionChallengeCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionChallengeCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionCount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleActionCountCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleActionCountCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionCountCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleActionCountCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleActionCountCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleActionCountCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleCaptchaConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time_property: Optional[outputs.WebAclRuleCaptchaConfigImmunityTimeProperty] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTimeProperty")
    def immunity_time_property(self) -> Optional[outputs.WebAclRuleCaptchaConfigImmunityTimeProperty]:
        
        ...
    


@pulumi.output_type
class WebAclRuleCaptchaConfigImmunityTimeProperty(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTime")
    def immunity_time(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WebAclRuleChallengeConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time_property: Optional[outputs.WebAclRuleChallengeConfigImmunityTimeProperty] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTimeProperty")
    def immunity_time_property(self) -> Optional[outputs.WebAclRuleChallengeConfigImmunityTimeProperty]:
        
        ...
    


@pulumi.output_type
class WebAclRuleChallengeConfigImmunityTimeProperty(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, immunity_time: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="immunityTime")
    def immunity_time(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroup(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, vendor_name: _builtins.str, managed_rule_group_configs: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigs] = ..., rule_action_overrides: Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverride]] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vendorName")
    def vendor_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedRuleGroupConfigs")
    def managed_rule_group_configs(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigs]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleActionOverrides")
    def rule_action_overrides(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverride]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigs(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_managed_rules_acfp_rule_set: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSet] = ..., aws_managed_rules_anti_ddos_rule_set: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSet] = ..., aws_managed_rules_atp_rule_set: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSet] = ..., aws_managed_rules_bot_control_rule_set: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesBotControlRuleSet] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsManagedRulesAcfpRuleSet")
    def aws_managed_rules_acfp_rule_set(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsManagedRulesAntiDdosRuleSet")
    def aws_managed_rules_anti_ddos_rule_set(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsManagedRulesAtpRuleSet")
    def aws_managed_rules_atp_rule_set(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsManagedRulesBotControlRuleSet")
    def aws_managed_rules_bot_control_rule_set(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesBotControlRuleSet]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_path: _builtins.str, registration_page_path: _builtins.str, enable_regex_in_path: Optional[_builtins.bool] = ..., request_inspection: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspection] = ..., response_inspection: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspection] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationPath")
    def creation_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationPagePath")
    def registration_page_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRegexInPath")
    def enable_regex_in_path(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestInspection")
    def request_inspection(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspection]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseInspection")
    def response_inspection(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspection]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, payload_type: _builtins.str, address_fields: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionAddressFields] = ..., email_field: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionEmailField] = ..., password_field: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionPasswordField] = ..., phone_number_fields: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionPhoneNumberFields] = ..., username_field: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionUsernameField] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadType")
    def payload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFields")
    def address_fields(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionAddressFields]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailField")
    def email_field(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionEmailField]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordField")
    def password_field(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionPasswordField]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumberFields")
    def phone_number_fields(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionPhoneNumberFields]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernameField")
    def username_field(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionUsernameField]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionAddressFields(dict):
    def __init__(__self__, *, identifiers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifiers(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionEmailField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionPasswordField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionPhoneNumberFields(dict):
    def __init__(__self__, *, identifiers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifiers(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetRequestInspectionUsernameField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, body_contains: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionBodyContains] = ..., header: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionHeader] = ..., json: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionJson] = ..., status_code: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionStatusCode] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bodyContains")
    def body_contains(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionBodyContains]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionJson]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionStatusCode]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionBodyContains(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_strings: Sequence[_builtins.str], success_strings: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureStrings")
    def failure_strings(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successStrings")
    def success_strings(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_values: Sequence[_builtins.str], name: _builtins.str, success_values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureValues")
    def failure_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successValues")
    def success_values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionJson(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_values: Sequence[_builtins.str], identifier: _builtins.str, success_values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureValues")
    def failure_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successValues")
    def success_values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAcfpRuleSetResponseInspectionStatusCode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_codes: Sequence[_builtins.int], success_codes: Sequence[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureCodes")
    def failure_codes(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successCodes")
    def success_codes(self) -> Sequence[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_side_action_config: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSetClientSideActionConfig] = ..., sensitivity_to_block: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSideActionConfig")
    def client_side_action_config(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSetClientSideActionConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityToBlock")
    def sensitivity_to_block(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSetClientSideActionConfig(dict):
    def __init__(__self__, *, challenge: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallenge] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def challenge(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallenge]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallenge(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, usage_of_action: _builtins.str, exempt_uri_regular_expressions: Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallengeExemptUriRegularExpression]] = ..., sensitivity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageOfAction")
    def usage_of_action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptUriRegularExpressions")
    def exempt_uri_regular_expressions(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallengeExemptUriRegularExpression]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sensitivity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallengeExemptUriRegularExpression(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regex_string: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, login_path: _builtins.str, enable_regex_in_path: Optional[_builtins.bool] = ..., request_inspection: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetRequestInspection] = ..., response_inspection: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspection] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginPath")
    def login_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRegexInPath")
    def enable_regex_in_path(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestInspection")
    def request_inspection(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetRequestInspection]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseInspection")
    def response_inspection(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspection]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetRequestInspection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, payload_type: _builtins.str, password_field: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetRequestInspectionPasswordField] = ..., username_field: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetRequestInspectionUsernameField] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadType")
    def payload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordField")
    def password_field(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetRequestInspectionPasswordField]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernameField")
    def username_field(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetRequestInspectionUsernameField]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetRequestInspectionPasswordField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetRequestInspectionUsernameField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, body_contains: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionBodyContains] = ..., header: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionHeader] = ..., json: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionJson] = ..., status_code: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionStatusCode] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bodyContains")
    def body_contains(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionBodyContains]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionJson]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionStatusCode]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionBodyContains(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_strings: Sequence[_builtins.str], success_strings: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureStrings")
    def failure_strings(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successStrings")
    def success_strings(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_values: Sequence[_builtins.str], name: _builtins.str, success_values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureValues")
    def failure_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successValues")
    def success_values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionJson(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_values: Sequence[_builtins.str], identifier: _builtins.str, success_values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureValues")
    def failure_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successValues")
    def success_values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesAtpRuleSetResponseInspectionStatusCode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_codes: Sequence[_builtins.int], success_codes: Sequence[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureCodes")
    def failure_codes(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successCodes")
    def success_codes(self) -> Sequence[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupManagedRuleGroupConfigsAwsManagedRulesBotControlRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, inspection_level: _builtins.str, enable_machine_learning: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectionLevel")
    def inspection_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMachineLearning")
    def enable_machine_learning(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, action_to_use: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionToUse")
    def action_to_use(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUse]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUse(dict):
    def __init__(__self__, *, allow: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseAllow] = ..., block: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseBlock] = ..., captcha: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCaptcha] = ..., challenge: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseChallenge] = ..., count: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCount] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseAllow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def block(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseBlock]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def captcha(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCaptcha]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def challenge(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseChallenge]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCount]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseAllow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseAllowCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseAllowCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseAllowCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseBlock(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_response: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseBlockCustomResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponse")
    def custom_response(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseBlockCustomResponse]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseBlockCustomResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response_code: _builtins.int, custom_response_body_key: Optional[_builtins.str] = ..., response_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseBlockCustomResponseResponseHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodyKey")
    def custom_response_body_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseBlockCustomResponseResponseHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseBlockCustomResponseResponseHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCaptcha(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCaptchaCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCaptchaCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCaptchaCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseChallenge(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseChallengeCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseChallengeCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseChallengeCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCountCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCountCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCountCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationManagedRuleGroupRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReference(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, rule_action_overrides: Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverride]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleActionOverrides")
    def rule_action_overrides(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverride]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, action_to_use: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionToUse")
    def action_to_use(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUse]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUse(dict):
    def __init__(__self__, *, allow: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseAllow] = ..., block: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseBlock] = ..., captcha: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCaptcha] = ..., challenge: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseChallenge] = ..., count: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCount] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseAllow]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def block(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseBlock]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def captcha(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCaptcha]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def challenge(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseChallenge]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCount]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseAllow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseAllowCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseAllowCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseAllowCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseBlock(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_response: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseBlockCustomResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponse")
    def custom_response(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseBlockCustomResponse]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseBlockCustomResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response_code: _builtins.int, custom_response_body_key: Optional[_builtins.str] = ..., response_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseBlockCustomResponseResponseHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodyKey")
    def custom_response_body_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseBlockCustomResponseResponseHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseBlockCustomResponseResponseHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCaptcha(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCaptchaCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCaptchaCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCaptchaCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseChallenge(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseChallengeCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseChallengeCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseChallengeCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCountCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCountCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCountCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Optional[Sequence[outputs.WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationRuleGroupReferenceRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleGroupAssociationTimeouts(dict):
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
class WebAclRuleGroupAssociationVisibilityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_metrics_enabled: _builtins.bool, metric_name: _builtins.str, sampled_requests_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetricsEnabled")
    def cloudwatch_metrics_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampledRequestsEnabled")
    def sampled_requests_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class WebAclRuleOverrideAction(dict):
    def __init__(__self__, *, count: Optional[outputs.WebAclRuleOverrideActionCount] = ..., none: Optional[outputs.WebAclRuleOverrideActionNone] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[outputs.WebAclRuleOverrideActionCount]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def none(self) -> Optional[outputs.WebAclRuleOverrideActionNone]:
        
        ...
    


@pulumi.output_type
class WebAclRuleOverrideActionCount(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleOverrideActionNone(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleRuleLabel(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, and_statement: Optional[outputs.WebAclRuleStatementAndStatement] = ..., asn_match_statement: Optional[outputs.WebAclRuleStatementAsnMatchStatement] = ..., byte_match_statement: Optional[outputs.WebAclRuleStatementByteMatchStatement] = ..., geo_match_statement: Optional[outputs.WebAclRuleStatementGeoMatchStatement] = ..., ip_set_reference_statement: Optional[outputs.WebAclRuleStatementIpSetReferenceStatement] = ..., label_match_statement: Optional[outputs.WebAclRuleStatementLabelMatchStatement] = ..., managed_rule_group_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatement] = ..., not_statement: Optional[outputs.WebAclRuleStatementNotStatement] = ..., or_statement: Optional[outputs.WebAclRuleStatementOrStatement] = ..., rate_based_statement: Optional[outputs.WebAclRuleStatementRateBasedStatement] = ..., regex_match_statement: Optional[outputs.WebAclRuleStatementRegexMatchStatement] = ..., regex_pattern_set_reference_statement: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatement] = ..., rule_group_reference_statement: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatement] = ..., size_constraint_statement: Optional[outputs.WebAclRuleStatementSizeConstraintStatement] = ..., sqli_match_statement: Optional[outputs.WebAclRuleStatementSqliMatchStatement] = ..., xss_match_statement: Optional[outputs.WebAclRuleStatementXssMatchStatement] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="andStatement")
    def and_statement(self) -> Optional[outputs.WebAclRuleStatementAndStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnMatchStatement")
    def asn_match_statement(self) -> Optional[outputs.WebAclRuleStatementAsnMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="byteMatchStatement")
    def byte_match_statement(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMatchStatement")
    def geo_match_statement(self) -> Optional[outputs.WebAclRuleStatementGeoMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetReferenceStatement")
    def ip_set_reference_statement(self) -> Optional[outputs.WebAclRuleStatementIpSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelMatchStatement")
    def label_match_statement(self) -> Optional[outputs.WebAclRuleStatementLabelMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedRuleGroupStatement")
    def managed_rule_group_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notStatement")
    def not_statement(self) -> Optional[outputs.WebAclRuleStatementNotStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orStatement")
    def or_statement(self) -> Optional[outputs.WebAclRuleStatementOrStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rateBasedStatement")
    def rate_based_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexMatchStatement")
    def regex_match_statement(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexPatternSetReferenceStatement")
    def regex_pattern_set_reference_statement(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleGroupReferenceStatement")
    def rule_group_reference_statement(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeConstraintStatement")
    def size_constraint_statement(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqliMatchStatement")
    def sqli_match_statement(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xssMatchStatement")
    def xss_match_statement(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementAndStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.WebAclRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.WebAclRuleStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementAsnMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn_lists: Sequence[_builtins.int], forwarded_ip_config: Optional[outputs.WebAclRuleStatementAsnMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnLists")
    def asn_lists(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementAsnMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementAsnMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, positional_constraint: _builtins.str, search_string: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementByteMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="positionalConstraint")
    def positional_constraint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchString")
    def search_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementByteMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementByteMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementByteMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementByteMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementGeoMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, country_codes: Sequence[_builtins.str], forwarded_ip_config: Optional[outputs.WebAclRuleStatementGeoMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCodes")
    def country_codes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementGeoMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementGeoMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementIpSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, ip_set_forwarded_ip_config: Optional[outputs.WebAclRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetForwardedIpConfig")
    def ip_set_forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementIpSetReferenceStatementIpSetForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str, position: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementLabelMatchStatement(dict):
    def __init__(__self__, *, key: _builtins.str, scope: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, vendor_name: _builtins.str, managed_rule_group_configs: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfig]] = ..., rule_action_overrides: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverride]] = ..., scope_down_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatement] = ..., version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="vendorName")
    def vendor_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedRuleGroupConfigs")
    def managed_rule_group_configs(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleActionOverrides")
    def rule_action_overrides(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverride]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeDownStatement")
    def scope_down_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, aws_managed_rules_acfp_rule_set: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSet] = ..., aws_managed_rules_anti_ddos_rule_set: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSet] = ..., aws_managed_rules_atp_rule_set: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSet] = ..., aws_managed_rules_bot_control_rule_set: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesBotControlRuleSet] = ..., login_path: Optional[_builtins.str] = ..., password_field: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigPasswordField] = ..., payload_type: Optional[_builtins.str] = ..., username_field: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigUsernameField] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsManagedRulesAcfpRuleSet")
    def aws_managed_rules_acfp_rule_set(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsManagedRulesAntiDdosRuleSet")
    def aws_managed_rules_anti_ddos_rule_set(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsManagedRulesAtpRuleSet")
    def aws_managed_rules_atp_rule_set(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsManagedRulesBotControlRuleSet")
    def aws_managed_rules_bot_control_rule_set(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesBotControlRuleSet]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginPath")
    def login_path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordField")
    def password_field(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigPasswordField]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadType")
    def payload_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernameField")
    def username_field(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigUsernameField]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, creation_path: _builtins.str, registration_page_path: _builtins.str, request_inspection: outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspection, enable_regex_in_path: Optional[_builtins.bool] = ..., response_inspection: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspection] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationPath")
    def creation_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="registrationPagePath")
    def registration_page_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestInspection")
    def request_inspection(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspection:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRegexInPath")
    def enable_regex_in_path(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseInspection")
    def response_inspection(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspection]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, payload_type: _builtins.str, address_fields: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionAddressFields] = ..., email_field: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionEmailField] = ..., password_field: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionPasswordField] = ..., phone_number_fields: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionPhoneNumberFields] = ..., username_field: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionUsernameField] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadType")
    def payload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressFields")
    def address_fields(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionAddressFields]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailField")
    def email_field(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionEmailField]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordField")
    def password_field(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionPasswordField]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumberFields")
    def phone_number_fields(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionPhoneNumberFields]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernameField")
    def username_field(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionUsernameField]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionAddressFields(dict):
    def __init__(__self__, *, identifiers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifiers(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionEmailField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionPasswordField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionPhoneNumberFields(dict):
    def __init__(__self__, *, identifiers: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifiers(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetRequestInspectionUsernameField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, body_contains: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionBodyContains] = ..., header: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionHeader] = ..., json: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionJson] = ..., status_code: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionStatusCode] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bodyContains")
    def body_contains(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionBodyContains]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionJson]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionStatusCode]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionBodyContains(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_strings: Sequence[_builtins.str], success_strings: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureStrings")
    def failure_strings(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successStrings")
    def success_strings(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_values: Sequence[_builtins.str], name: _builtins.str, success_values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureValues")
    def failure_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successValues")
    def success_values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionJson(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_values: Sequence[_builtins.str], identifier: _builtins.str, success_values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureValues")
    def failure_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successValues")
    def success_values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAcfpRuleSetResponseInspectionStatusCode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_codes: Sequence[_builtins.int], success_codes: Sequence[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureCodes")
    def failure_codes(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successCodes")
    def success_codes(self) -> Sequence[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_side_action_config: outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSetClientSideActionConfig, sensitivity_to_block: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSideActionConfig")
    def client_side_action_config(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSetClientSideActionConfig:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityToBlock")
    def sensitivity_to_block(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSetClientSideActionConfig(dict):
    def __init__(__self__, *, challenge: outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallenge) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def challenge(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallenge:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallenge(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, usage_of_action: _builtins.str, exempt_uri_regular_expressions: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallengeExemptUriRegularExpression]] = ..., sensitivity: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageOfAction")
    def usage_of_action(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="exemptUriRegularExpressions")
    def exempt_uri_regular_expressions(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallengeExemptUriRegularExpression]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def sensitivity(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAntiDdosRuleSetClientSideActionConfigChallengeExemptUriRegularExpression(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regex_string: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, login_path: _builtins.str, enable_regex_in_path: Optional[_builtins.bool] = ..., request_inspection: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetRequestInspection] = ..., response_inspection: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspection] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loginPath")
    def login_path(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRegexInPath")
    def enable_regex_in_path(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestInspection")
    def request_inspection(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetRequestInspection]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseInspection")
    def response_inspection(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspection]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetRequestInspection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, password_field: outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetRequestInspectionPasswordField, payload_type: _builtins.str, username_field: outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetRequestInspectionUsernameField) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordField")
    def password_field(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetRequestInspectionPasswordField:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="payloadType")
    def payload_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="usernameField")
    def username_field(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetRequestInspectionUsernameField:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetRequestInspectionPasswordField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetRequestInspectionUsernameField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspection(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, body_contains: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionBodyContains] = ..., header: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionHeader] = ..., json: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionJson] = ..., status_code: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionStatusCode] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bodyContains")
    def body_contains(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionBodyContains]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def json(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionJson]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionStatusCode]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionBodyContains(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_strings: Sequence[_builtins.str], success_strings: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureStrings")
    def failure_strings(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successStrings")
    def success_strings(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_values: Sequence[_builtins.str], name: _builtins.str, success_values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureValues")
    def failure_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successValues")
    def success_values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionJson(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_values: Sequence[_builtins.str], identifier: _builtins.str, success_values: Sequence[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureValues")
    def failure_values(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successValues")
    def success_values(self) -> Sequence[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesAtpRuleSetResponseInspectionStatusCode(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, failure_codes: Sequence[_builtins.int], success_codes: Sequence[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureCodes")
    def failure_codes(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="successCodes")
    def success_codes(self) -> Sequence[_builtins.int]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigAwsManagedRulesBotControlRuleSet(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, inspection_level: _builtins.str, enable_machine_learning: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectionLevel")
    def inspection_level(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMachineLearning")
    def enable_machine_learning(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigPasswordField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementManagedRuleGroupConfigUsernameField(dict):
    def __init__(__self__, *, identifier: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def identifier(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_to_use: outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUse, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionToUse")
    def action_to_use(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUse(dict):
    def __init__(__self__, *, allow: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseAllow] = ..., block: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseBlock] = ..., captcha: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCaptcha] = ..., challenge: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseChallenge] = ..., count: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCount] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseAllow]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def block(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseBlock]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def captcha(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCaptcha]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def challenge(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseChallenge]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCount]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseAllow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseAllowCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseAllowCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseAllowCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseBlock(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_response: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseBlockCustomResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponse")
    def custom_response(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseBlockCustomResponse]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseBlockCustomResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response_code: _builtins.int, custom_response_body_key: Optional[_builtins.str] = ..., response_headers: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseBlockCustomResponseResponseHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodyKey")
    def custom_response_body_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseBlockCustomResponseResponseHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseBlockCustomResponseResponseHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCaptcha(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseChallenge(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseChallengeCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseChallengeCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseChallengeCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCountCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCountCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCountCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, and_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementAndStatement] = ..., asn_match_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementAsnMatchStatement] = ..., byte_match_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatement] = ..., geo_match_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementGeoMatchStatement] = ..., ip_set_reference_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementIpSetReferenceStatement] = ..., label_match_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementLabelMatchStatement] = ..., not_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementNotStatement] = ..., or_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementOrStatement] = ..., regex_match_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatement] = ..., regex_pattern_set_reference_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatement] = ..., size_constraint_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatement] = ..., sqli_match_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatement] = ..., xss_match_statement: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatement] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="andStatement")
    def and_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementAndStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnMatchStatement")
    def asn_match_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementAsnMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="byteMatchStatement")
    def byte_match_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMatchStatement")
    def geo_match_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementGeoMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetReferenceStatement")
    def ip_set_reference_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementIpSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelMatchStatement")
    def label_match_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementLabelMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notStatement")
    def not_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementNotStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orStatement")
    def or_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementOrStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexMatchStatement")
    def regex_match_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexPatternSetReferenceStatement")
    def regex_pattern_set_reference_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeConstraintStatement")
    def size_constraint_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqliMatchStatement")
    def sqli_match_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xssMatchStatement")
    def xss_match_statement(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementAndStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.WebAclRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.WebAclRuleStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementAsnMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn_lists: Sequence[_builtins.int], forwarded_ip_config: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementAsnMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnLists")
    def asn_lists(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementAsnMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementAsnMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, positional_constraint: _builtins.str, search_string: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="positionalConstraint")
    def positional_constraint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchString")
    def search_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementByteMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementGeoMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, country_codes: Sequence[_builtins.str], forwarded_ip_config: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementGeoMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCodes")
    def country_codes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementGeoMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementGeoMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementIpSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, ip_set_forwarded_ip_config: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementIpSetReferenceStatementIpSetForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetForwardedIpConfig")
    def ip_set_forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementIpSetReferenceStatementIpSetForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementIpSetReferenceStatementIpSetForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str, position: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementLabelMatchStatement(dict):
    def __init__(__self__, *, key: _builtins.str, scope: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementNotStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.WebAclRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.WebAclRuleStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementOrStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.WebAclRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.WebAclRuleStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regex_string: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementRegexPatternSetReferenceStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, comparison_operator: _builtins.str, size: _builtins.int, text_transformations: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSizeConstraintStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatch] = ..., sensitivity_level: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatch]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityLevel")
    def sensitivity_level(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementSqliMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementManagedRuleGroupStatementScopeDownStatementXssMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementNotStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.WebAclRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.WebAclRuleStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementOrStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.WebAclRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.WebAclRuleStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, limit: _builtins.int, aggregate_key_type: Optional[_builtins.str] = ..., custom_keys: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKey]] = ..., evaluation_window_sec: Optional[_builtins.int] = ..., forwarded_ip_config: Optional[outputs.WebAclRuleStatementRateBasedStatementForwardedIpConfig] = ..., scope_down_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatement] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def limit(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aggregateKeyType")
    def aggregate_key_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customKeys")
    def custom_keys(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKey]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationWindowSec")
    def evaluation_window_sec(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementForwardedIpConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="scopeDownStatement")
    def scope_down_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKey(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyAsn] = ..., cookie: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyCookie] = ..., forwarded_ip: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyForwardedIp] = ..., header: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyHeader] = ..., http_method: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyHttpMethod] = ..., ip: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyIp] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyJa4Fingerprint] = ..., label_namespace: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyLabelNamespace] = ..., query_argument: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyQueryArgument] = ..., query_string: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyQueryString] = ..., uri_path: Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def asn(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyAsn]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookie(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyCookie]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIp")
    def forwarded_ip(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyForwardedIp]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def header(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyHttpMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ip(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyIp]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelNamespace")
    def label_namespace(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyLabelNamespace]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryArgument")
    def query_argument(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementCustomKeyUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyAsn(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyCookie(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyCookieTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyCookieTextTransformation]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyCookieTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyForwardedIp(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyHeaderTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyHeaderTextTransformation]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyHeaderTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyHttpMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyIp(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyLabelNamespace(dict):
    def __init__(__self__, *, namespace: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyQueryArgument(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyQueryArgumentTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyQueryArgumentTextTransformation]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyQueryArgumentTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyQueryString(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyQueryStringTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyQueryStringTextTransformation]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyQueryStringTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyUriPath(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyUriPathTextTransformation]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementCustomKeyUriPathTextTransformation]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementCustomKeyUriPathTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, and_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementAndStatement] = ..., asn_match_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatement] = ..., byte_match_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatement] = ..., geo_match_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatement] = ..., ip_set_reference_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatement] = ..., label_match_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementLabelMatchStatement] = ..., not_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementNotStatement] = ..., or_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementOrStatement] = ..., regex_match_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatement] = ..., regex_pattern_set_reference_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatement] = ..., size_constraint_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatement] = ..., sqli_match_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatement] = ..., xss_match_statement: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatement] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="andStatement")
    def and_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementAndStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnMatchStatement")
    def asn_match_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="byteMatchStatement")
    def byte_match_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="geoMatchStatement")
    def geo_match_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetReferenceStatement")
    def ip_set_reference_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="labelMatchStatement")
    def label_match_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementLabelMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notStatement")
    def not_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementNotStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="orStatement")
    def or_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementOrStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexMatchStatement")
    def regex_match_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexPatternSetReferenceStatement")
    def regex_pattern_set_reference_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeConstraintStatement")
    def size_constraint_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqliMatchStatement")
    def sqli_match_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xssMatchStatement")
    def xss_match_statement(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementAndStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.WebAclRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.WebAclRuleStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, asn_lists: Sequence[_builtins.int], forwarded_ip_config: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="asnLists")
    def asn_lists(self) -> Sequence[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementAsnMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, positional_constraint: _builtins.str, search_string: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="positionalConstraint")
    def positional_constraint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="searchString")
    def search_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementByteMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, country_codes: Sequence[_builtins.str], forwarded_ip_config: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatementForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="countryCodes")
    def country_codes(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="forwardedIpConfig")
    def forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatementForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementGeoMatchStatementForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, ip_set_forwarded_ip_config: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatementIpSetForwardedIpConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ipSetForwardedIpConfig")
    def ip_set_forwarded_ip_config(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatementIpSetForwardedIpConfig]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementIpSetReferenceStatementIpSetForwardedIpConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str, header_name: _builtins.str, position: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerName")
    def header_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def position(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementLabelMatchStatement(dict):
    def __init__(__self__, *, key: _builtins.str, scope: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scope(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementNotStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.WebAclRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.WebAclRuleStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementOrStatement(dict):
    def __init__(__self__, *, statements: Sequence[outputs.WebAclRuleStatement]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def statements(self) -> Sequence[outputs.WebAclRuleStatement]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regex_string: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementRegexPatternSetReferenceStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, comparison_operator: _builtins.str, size: _builtins.int, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSizeConstraintStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatch] = ..., sensitivity_level: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatch]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityLevel")
    def sensitivity_level(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementSqliMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRateBasedStatementScopeDownStatementXssMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, regex_string: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementRegexMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRegexMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, text_transformations: Sequence[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRegexPatternSetReferenceStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, arn: _builtins.str, rule_action_overrides: Optional[Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverride]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ruleActionOverrides")
    def rule_action_overrides(self) -> Optional[Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverride]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverride(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, action_to_use: outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUse, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionToUse")
    def action_to_use(self) -> outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUse:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUse(dict):
    def __init__(__self__, *, allow: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseAllow] = ..., block: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseBlock] = ..., captcha: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCaptcha] = ..., challenge: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseChallenge] = ..., count: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCount] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def allow(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseAllow]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def block(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseBlock]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def captcha(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCaptcha]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def challenge(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseChallenge]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCount]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseAllow(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseAllowCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseAllowCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseAllowCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseAllowCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseBlock(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_response: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseBlockCustomResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponse")
    def custom_response(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseBlockCustomResponse]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseBlockCustomResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response_code: _builtins.int, custom_response_body_key: Optional[_builtins.str] = ..., response_headers: Optional[Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseBlockCustomResponseResponseHeader]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodyKey")
    def custom_response_body_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseBlockCustomResponseResponseHeader]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseBlockCustomResponseResponseHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCaptcha(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCaptchaCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseChallenge(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseChallengeCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseChallengeCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseChallengeCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseChallengeCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCount(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_request_handling: Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCountCustomRequestHandling] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandling")
    def custom_request_handling(self) -> Optional[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCountCustomRequestHandling]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCountCustomRequestHandling(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, insert_headers: Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementRuleGroupReferenceStatementRuleActionOverrideActionToUseCountCustomRequestHandlingInsertHeader(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, comparison_operator: _builtins.str, size: _builtins.int, text_transformations: Sequence[outputs.WebAclRuleStatementSizeConstraintStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementSizeConstraintStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSizeConstraintStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.WebAclRuleStatementSqliMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatch] = ..., sensitivity_level: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementSqliMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatch]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sensitivityLevel")
    def sensitivity_level(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementSqliMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatement(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, text_transformations: Sequence[outputs.WebAclRuleStatementXssMatchStatementTextTransformation], field_to_match: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatch] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textTransformations")
    def text_transformations(self) -> Sequence[outputs.WebAclRuleStatementXssMatchStatementTextTransformation]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldToMatch")
    def field_to_match(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatch]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatch(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all_query_arguments: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchAllQueryArguments] = ..., body: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchBody] = ..., cookies: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchCookies] = ..., header_orders: Optional[Sequence[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchHeaderOrder]] = ..., headers: Optional[Sequence[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchHeader]] = ..., ja3_fingerprint: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJa3Fingerprint] = ..., ja4_fingerprint: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJa4Fingerprint] = ..., json_body: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJsonBody] = ..., method: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchMethod] = ..., query_string: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchQueryString] = ..., single_header: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchSingleHeader] = ..., single_query_argument: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument] = ..., uri_fragment: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchUriFragment] = ..., uri_path: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchUriPath] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allQueryArguments")
    def all_query_arguments(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchAllQueryArguments]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def body(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cookies(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchCookies]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerOrders")
    def header_orders(self) -> Optional[Sequence[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchHeaderOrder]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja3Fingerprint")
    def ja3_fingerprint(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJa3Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ja4Fingerprint")
    def ja4_fingerprint(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJa4Fingerprint]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jsonBody")
    def json_body(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJsonBody]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def method(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchMethod]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchQueryString]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleHeader")
    def single_header(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchSingleHeader]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="singleQueryArgument")
    def single_query_argument(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriFragment")
    def uri_fragment(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchUriFragment]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uriPath")
    def uri_path(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchUriPath]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchAllQueryArguments(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchCookies(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_patterns: Sequence[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern], match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPatterns")
    def match_patterns(self) -> Sequence[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchCookiesMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll] = ..., excluded_cookies: Optional[Sequence[_builtins.str]] = ..., included_cookies: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedCookies")
    def excluded_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedCookies")
    def included_cookies(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchCookiesMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchHeader(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementXssMatchStatementFieldToMatchHeaderMatchPattern, match_scope: _builtins.str, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementXssMatchStatementFieldToMatchHeaderMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchHeaderMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll] = ..., excluded_headers: Optional[Sequence[_builtins.str]] = ..., included_headers: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludedHeaders")
    def excluded_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedHeaders")
    def included_headers(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchHeaderMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchHeaderOrder(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, oversize_handling: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchJa3Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchJa4Fingerprint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchJsonBody(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_pattern: outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern, match_scope: _builtins.str, invalid_fallback_behavior: Optional[_builtins.str] = ..., oversize_handling: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchPattern")
    def match_pattern(self) -> outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchScope")
    def match_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="invalidFallbackBehavior")
    def invalid_fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oversizeHandling")
    def oversize_handling(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPattern(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, all: Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll] = ..., included_paths: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def all(self) -> Optional[outputs.WebAclRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="includedPaths")
    def included_paths(self) -> Optional[Sequence[_builtins.str]]:
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchJsonBodyMatchPatternAll(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchMethod(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchQueryString(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchSingleHeader(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchSingleQueryArgument(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchUriFragment(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fallback_behavior: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackBehavior")
    def fallback_behavior(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementFieldToMatchUriPath(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class WebAclRuleStatementXssMatchStatementTextTransformation(dict):
    def __init__(__self__, *, priority: _builtins.int, type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def priority(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class WebAclRuleVisibilityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_metrics_enabled: _builtins.bool, metric_name: _builtins.str, sampled_requests_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetricsEnabled")
    def cloudwatch_metrics_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampledRequestsEnabled")
    def sampled_requests_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class WebAclVisibilityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cloudwatch_metrics_enabled: _builtins.bool, metric_name: _builtins.str, sampled_requests_enabled: _builtins.bool) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudwatchMetricsEnabled")
    def cloudwatch_metrics_enabled(self) -> _builtins.bool:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampledRequestsEnabled")
    def sampled_requests_enabled(self) -> _builtins.bool:
        
        ...
    


@pulumi.output_type
class GetManagedRuleGroupAvailableLabelResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetManagedRuleGroupConsumedLabelResult(dict):
    def __init__(__self__, *, name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleResult(dict):
    def __init__(__self__, *, actions: Sequence[outputs.GetManagedRuleGroupRuleActionResult], name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionResult(dict):
    def __init__(__self__, *, allows: Sequence[outputs.GetManagedRuleGroupRuleActionAllowResult], blocks: Sequence[outputs.GetManagedRuleGroupRuleActionBlockResult], captchas: Sequence[outputs.GetManagedRuleGroupRuleActionCaptchaResult], challenges: Sequence[outputs.GetManagedRuleGroupRuleActionChallengeResult], counts: Sequence[outputs.GetManagedRuleGroupRuleActionCountResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def allows(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionAllowResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def blocks(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionBlockResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def captchas(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionCaptchaResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def challenges(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionChallengeResult]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def counts(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionCountResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionAllowResult(dict):
    def __init__(__self__, *, custom_request_handlings: Sequence[outputs.GetManagedRuleGroupRuleActionAllowCustomRequestHandlingResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandlings")
    def custom_request_handlings(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionAllowCustomRequestHandlingResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionAllowCustomRequestHandlingResult(dict):
    def __init__(__self__, *, insert_headers: Sequence[outputs.GetManagedRuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionAllowCustomRequestHandlingInsertHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionBlockResult(dict):
    def __init__(__self__, *, custom_responses: Sequence[outputs.GetManagedRuleGroupRuleActionBlockCustomResponseResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponses")
    def custom_responses(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionBlockCustomResponseResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionBlockCustomResponseResult(dict):
    def __init__(__self__, *, custom_response_body_key: _builtins.str, response_code: _builtins.int, response_headers: Sequence[outputs.GetManagedRuleGroupRuleActionBlockCustomResponseResponseHeaderResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customResponseBodyKey")
    def custom_response_body_key(self) -> _builtins.str:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> _builtins.int:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseHeaders")
    def response_headers(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionBlockCustomResponseResponseHeaderResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionBlockCustomResponseResponseHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionCaptchaResult(dict):
    def __init__(__self__, *, custom_request_handlings: Sequence[outputs.GetManagedRuleGroupRuleActionCaptchaCustomRequestHandlingResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandlings")
    def custom_request_handlings(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionCaptchaCustomRequestHandlingResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionCaptchaCustomRequestHandlingResult(dict):
    def __init__(__self__, *, insert_headers: Sequence[outputs.GetManagedRuleGroupRuleActionCaptchaCustomRequestHandlingInsertHeaderResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionCaptchaCustomRequestHandlingInsertHeaderResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionCaptchaCustomRequestHandlingInsertHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionChallengeResult(dict):
    def __init__(__self__, *, custom_request_handlings: Sequence[outputs.GetManagedRuleGroupRuleActionChallengeCustomRequestHandlingResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandlings")
    def custom_request_handlings(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionChallengeCustomRequestHandlingResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionChallengeCustomRequestHandlingResult(dict):
    def __init__(__self__, *, insert_headers: Sequence[outputs.GetManagedRuleGroupRuleActionChallengeCustomRequestHandlingInsertHeaderResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionChallengeCustomRequestHandlingInsertHeaderResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionChallengeCustomRequestHandlingInsertHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionCountResult(dict):
    def __init__(__self__, *, custom_request_handlings: Sequence[outputs.GetManagedRuleGroupRuleActionCountCustomRequestHandlingResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRequestHandlings")
    def custom_request_handlings(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionCountCustomRequestHandlingResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionCountCustomRequestHandlingResult(dict):
    def __init__(__self__, *, insert_headers: Sequence[outputs.GetManagedRuleGroupRuleActionCountCustomRequestHandlingInsertHeaderResult]) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="insertHeaders")
    def insert_headers(self) -> Sequence[outputs.GetManagedRuleGroupRuleActionCountCustomRequestHandlingInsertHeaderResult]:
        ...
    


@pulumi.output_type
class GetManagedRuleGroupRuleActionCountCustomRequestHandlingInsertHeaderResult(dict):
    def __init__(__self__, *, name: _builtins.str, value: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str:
        ...
    


@pulumi.output_type
class GetRegexPatternSetRegularExpressionResult(dict):
    def __init__(__self__, *, regex_string: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="regexString")
    def regex_string(self) -> _builtins.str:
        
        ...
    


