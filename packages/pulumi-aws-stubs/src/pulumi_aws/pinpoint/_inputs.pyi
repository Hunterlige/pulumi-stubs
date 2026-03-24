import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AppCampaignHookArgs",
    "AppCampaignHookArgsDict",
    "AppLimitsArgs",
    "AppLimitsArgsDict",
    "AppQuietTimeArgs",
    "AppQuietTimeArgsDict",
    "EmailTemplateEmailTemplateArgs",
    "EmailTemplateEmailTemplateArgsDict",
    "EmailTemplateEmailTemplateHeaderArgs",
    "EmailTemplateEmailTemplateHeaderArgsDict",
    "Smsvoicev2PhoneNumberTimeoutsArgs",
    "Smsvoicev2PhoneNumberTimeoutsArgsDict",
]

class AppCampaignHookArgsDict(TypedDict):
    lambda_function_name: NotRequired[pulumi.Input[_builtins.str]]
    mode: NotRequired[pulumi.Input[_builtins.str]]
    web_url: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppCampaignHookArgs:
    def __init__(
        __self__,
        *,
        lambda_function_name: Optional[pulumi.Input[_builtins.str]] = ...,
        mode: Optional[pulumi.Input[_builtins.str]] = ...,
        web_url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionName")
    def lambda_function_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @lambda_function_name.setter
    def lambda_function_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webUrl")
    def web_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_url.setter
    def web_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppLimitsArgsDict(TypedDict):
    daily: NotRequired[pulumi.Input[_builtins.int]]
    maximum_duration: NotRequired[pulumi.Input[_builtins.int]]
    messages_per_second: NotRequired[pulumi.Input[_builtins.int]]
    total: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AppLimitsArgs:
    def __init__(
        __self__,
        *,
        daily: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum_duration: Optional[pulumi.Input[_builtins.int]] = ...,
        messages_per_second: Optional[pulumi.Input[_builtins.int]] = ...,
        total: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def daily(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @daily.setter
    def daily(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maximumDuration")
    def maximum_duration(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @maximum_duration.setter
    def maximum_duration(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="messagesPerSecond")
    def messages_per_second(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @messages_per_second.setter
    def messages_per_second(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def total(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total.setter
    def total(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class AppQuietTimeArgsDict(TypedDict):
    end: NotRequired[pulumi.Input[_builtins.str]]
    start: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppQuietTimeArgs:
    def __init__(
        __self__,
        *,
        end: Optional[pulumi.Input[_builtins.str]] = ...,
        start: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end.setter
    def end(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start.setter
    def start(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EmailTemplateEmailTemplateArgsDict(TypedDict):
    default_substitutions: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    headers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[EmailTemplateEmailTemplateHeaderArgsDict]]]
    ]
    html_part: NotRequired[pulumi.Input[_builtins.str]]
    recommender_id: NotRequired[pulumi.Input[_builtins.str]]
    subject: NotRequired[pulumi.Input[_builtins.str]]
    text_part: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EmailTemplateEmailTemplateArgs:
    def __init__(
        __self__,
        *,
        default_substitutions: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        headers: Optional[
            pulumi.Input[Sequence[pulumi.Input[EmailTemplateEmailTemplateHeaderArgs]]]
        ] = ...,
        html_part: Optional[pulumi.Input[_builtins.str]] = ...,
        recommender_id: Optional[pulumi.Input[_builtins.str]] = ...,
        subject: Optional[pulumi.Input[_builtins.str]] = ...,
        text_part: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultSubstitutions")
    def default_substitutions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_substitutions.setter
    def default_substitutions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def headers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[EmailTemplateEmailTemplateHeaderArgs]]]
    ]: ...
    @headers.setter
    def headers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[EmailTemplateEmailTemplateHeaderArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="htmlPart")
    def html_part(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @html_part.setter
    def html_part(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="recommenderId")
    def recommender_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @recommender_id.setter
    def recommender_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subject.setter
    def subject(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="textPart")
    def text_part(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text_part.setter
    def text_part(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EmailTemplateEmailTemplateHeaderArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class EmailTemplateEmailTemplateHeaderArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class Smsvoicev2PhoneNumberTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class Smsvoicev2PhoneNumberTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...
