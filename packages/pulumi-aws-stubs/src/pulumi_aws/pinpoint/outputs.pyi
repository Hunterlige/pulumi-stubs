import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppCampaignHook",
    "AppLimits",
    "AppQuietTime",
    "EmailTemplateEmailTemplate",
    "EmailTemplateEmailTemplateHeader",
    "Smsvoicev2PhoneNumberTimeouts",
]

@pulumi.output_type
class AppCampaignHook(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lambda_function_name: Optional[_builtins.str] = ...,
        mode: Optional[_builtins.str] = ...,
        web_url: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionName")
    def lambda_function_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webUrl")
    def web_url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AppLimits(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        daily: Optional[_builtins.int] = ...,
        maximum_duration: Optional[_builtins.int] = ...,
        messages_per_second: Optional[_builtins.int] = ...,
        total: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def daily(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maximumDuration")
    def maximum_duration(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="messagesPerSecond")
    def messages_per_second(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def total(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class AppQuietTime(dict):
    def __init__(
        __self__,
        *,
        end: Optional[_builtins.str] = ...,
        start: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EmailTemplateEmailTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_substitutions: Optional[_builtins.str] = ...,
        description: Optional[_builtins.str] = ...,
        headers: Optional[Sequence[outputs.EmailTemplateEmailTemplateHeader]] = ...,
        html_part: Optional[_builtins.str] = ...,
        recommender_id: Optional[_builtins.str] = ...,
        subject: Optional[_builtins.str] = ...,
        text_part: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultSubstitutions")
    def default_substitutions(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[Sequence[outputs.EmailTemplateEmailTemplateHeader]]: ...
    @_builtins.property
    @pulumi.getter(name="htmlPart")
    def html_part(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="recommenderId")
    def recommender_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="textPart")
    def text_part(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class EmailTemplateEmailTemplateHeader(dict):
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class Smsvoicev2PhoneNumberTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...
