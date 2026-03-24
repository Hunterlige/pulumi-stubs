

import builtins as _builtins
import sys
import pulumi
from typing import Any, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = [..., ..., 'ApplicationInsightsComponentDataVolumeCapArgs', 'ApplicationInsightsComponentDataVolumeCapArgsDict', ..., ..., 'HeaderFieldArgs', 'HeaderFieldArgsDict', 'MyWorkbookManagedIdentityArgs', 'MyWorkbookManagedIdentityArgsDict', 'WebTestGeolocationArgs', 'WebTestGeolocationArgsDict', 'WebTestPropertiesConfigurationArgs', 'WebTestPropertiesConfigurationArgsDict', 'WebTestPropertiesContentValidationArgs', 'WebTestPropertiesContentValidationArgsDict', 'WebTestPropertiesRequestArgs', 'WebTestPropertiesRequestArgsDict', 'WebTestPropertiesValidationRulesArgs', 'WebTestPropertiesValidationRulesArgsDict', 'WorkbookResourceIdentityArgs', 'WorkbookResourceIdentityArgsDict', 'WorkbookTemplateGalleryArgs', 'WorkbookTemplateGalleryArgsDict', 'WorkbookTemplateLocalizedGalleryArgs', 'WorkbookTemplateLocalizedGalleryArgsDict']
class ApplicationInsightsComponentAnalyticsItemPropertiesArgsDict(TypedDict):
    
    function_alias: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ApplicationInsightsComponentAnalyticsItemPropertiesArgs:
    def __init__(__self__, *, function_alias: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionAlias")
    def function_alias(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @function_alias.setter
    def function_alias(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ApplicationInsightsComponentDataVolumeCapArgsDict(TypedDict):
    
    cap: NotRequired[pulumi.Input[_builtins.float]]
    stop_send_notification_when_hit_cap: NotRequired[pulumi.Input[_builtins.bool]]
    stop_send_notification_when_hit_threshold: NotRequired[pulumi.Input[_builtins.bool]]
    warning_threshold: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ApplicationInsightsComponentDataVolumeCapArgs:
    def __init__(__self__, *, cap: Optional[pulumi.Input[_builtins.float]] = ..., stop_send_notification_when_hit_cap: Optional[pulumi.Input[_builtins.bool]] = ..., stop_send_notification_when_hit_threshold: Optional[pulumi.Input[_builtins.bool]] = ..., warning_threshold: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cap(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @cap.setter
    def cap(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stopSendNotificationWhenHitCap")
    def stop_send_notification_when_hit_cap(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @stop_send_notification_when_hit_cap.setter
    def stop_send_notification_when_hit_cap(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="stopSendNotificationWhenHitThreshold")
    def stop_send_notification_when_hit_threshold(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @stop_send_notification_when_hit_threshold.setter
    def stop_send_notification_when_hit_threshold(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="warningThreshold")
    def warning_threshold(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @warning_threshold.setter
    def warning_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    help_url: NotRequired[pulumi.Input[_builtins.str]]
    is_enabled_by_default: NotRequired[pulumi.Input[_builtins.bool]]
    is_hidden: NotRequired[pulumi.Input[_builtins.bool]]
    is_in_preview: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    supports_email_notifications: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ApplicationInsightsComponentProactiveDetectionConfigurationPropertiesRuleDefinitionsArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., help_url: Optional[pulumi.Input[_builtins.str]] = ..., is_enabled_by_default: Optional[pulumi.Input[_builtins.bool]] = ..., is_hidden: Optional[pulumi.Input[_builtins.bool]] = ..., is_in_preview: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., supports_email_notifications: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="helpUrl")
    def help_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @help_url.setter
    def help_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isEnabledByDefault")
    def is_enabled_by_default(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_enabled_by_default.setter
    def is_enabled_by_default(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isHidden")
    def is_hidden(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_hidden.setter
    def is_hidden(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isInPreview")
    def is_in_preview(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_in_preview.setter
    def is_in_preview(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportsEmailNotifications")
    def supports_email_notifications(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @supports_email_notifications.setter
    def supports_email_notifications(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class HeaderFieldArgsDict(TypedDict):
    
    header_field_name: NotRequired[pulumi.Input[_builtins.str]]
    header_field_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class HeaderFieldArgs:
    def __init__(__self__, *, header_field_name: Optional[pulumi.Input[_builtins.str]] = ..., header_field_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerFieldName")
    def header_field_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @header_field_name.setter
    def header_field_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerFieldValue")
    def header_field_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @header_field_value.setter
    def header_field_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class MyWorkbookManagedIdentityArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class MyWorkbookManagedIdentityArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebTestGeolocationArgsDict(TypedDict):
    
    location: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebTestGeolocationArgs:
    def __init__(__self__, *, location: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebTestPropertiesConfigurationArgsDict(TypedDict):
    
    web_test: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebTestPropertiesConfigurationArgs:
    def __init__(__self__, *, web_test: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webTest")
    def web_test(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @web_test.setter
    def web_test(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebTestPropertiesContentValidationArgsDict(TypedDict):
    
    content_match: NotRequired[pulumi.Input[_builtins.str]]
    ignore_case: NotRequired[pulumi.Input[_builtins.bool]]
    pass_if_text_found: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class WebTestPropertiesContentValidationArgs:
    def __init__(__self__, *, content_match: Optional[pulumi.Input[_builtins.str]] = ..., ignore_case: Optional[pulumi.Input[_builtins.bool]] = ..., pass_if_text_found: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentMatch")
    def content_match(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_match.setter
    def content_match(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_case.setter
    def ignore_case(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passIfTextFound")
    def pass_if_text_found(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @pass_if_text_found.setter
    def pass_if_text_found(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class WebTestPropertiesRequestArgsDict(TypedDict):
    
    follow_redirects: NotRequired[pulumi.Input[_builtins.bool]]
    headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[HeaderFieldArgsDict]]]]
    http_verb: NotRequired[pulumi.Input[_builtins.str]]
    parse_dependent_requests: NotRequired[pulumi.Input[_builtins.bool]]
    request_body: NotRequired[pulumi.Input[_builtins.str]]
    request_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WebTestPropertiesRequestArgs:
    def __init__(__self__, *, follow_redirects: Optional[pulumi.Input[_builtins.bool]] = ..., headers: Optional[pulumi.Input[Sequence[pulumi.Input[HeaderFieldArgs]]]] = ..., http_verb: Optional[pulumi.Input[_builtins.str]] = ..., parse_dependent_requests: Optional[pulumi.Input[_builtins.bool]] = ..., request_body: Optional[pulumi.Input[_builtins.str]] = ..., request_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="followRedirects")
    def follow_redirects(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @follow_redirects.setter
    def follow_redirects(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[HeaderFieldArgs]]]]:
        
        ...
    
    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[HeaderFieldArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpVerb")
    def http_verb(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_verb.setter
    def http_verb(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parseDependentRequests")
    def parse_dependent_requests(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @parse_dependent_requests.setter
    def parse_dependent_requests(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestBody")
    def request_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_body.setter
    def request_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestUrl")
    def request_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_url.setter
    def request_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WebTestPropertiesValidationRulesArgsDict(TypedDict):
    
    content_validation: NotRequired[pulumi.Input[WebTestPropertiesContentValidationArgsDict]]
    expected_http_status_code: NotRequired[pulumi.Input[_builtins.int]]
    ignore_http_status_code: NotRequired[pulumi.Input[_builtins.bool]]
    s_sl_cert_remaining_lifetime_check: NotRequired[pulumi.Input[_builtins.int]]
    s_sl_check: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class WebTestPropertiesValidationRulesArgs:
    def __init__(__self__, *, content_validation: Optional[pulumi.Input[WebTestPropertiesContentValidationArgs]] = ..., expected_http_status_code: Optional[pulumi.Input[_builtins.int]] = ..., ignore_http_status_code: Optional[pulumi.Input[_builtins.bool]] = ..., s_sl_cert_remaining_lifetime_check: Optional[pulumi.Input[_builtins.int]] = ..., s_sl_check: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentValidation")
    def content_validation(self) -> Optional[pulumi.Input[WebTestPropertiesContentValidationArgs]]:
        
        ...
    
    @content_validation.setter
    def content_validation(self, value: Optional[pulumi.Input[WebTestPropertiesContentValidationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectedHttpStatusCode")
    def expected_http_status_code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @expected_http_status_code.setter
    def expected_http_status_code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreHttpStatusCode")
    def ignore_http_status_code(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @ignore_http_status_code.setter
    def ignore_http_status_code(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sSLCertRemainingLifetimeCheck")
    def s_sl_cert_remaining_lifetime_check(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @s_sl_cert_remaining_lifetime_check.setter
    def s_sl_cert_remaining_lifetime_check(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sSLCheck")
    def s_sl_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @s_sl_check.setter
    def s_sl_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class WorkbookResourceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class WorkbookResourceIdentityArgs:
    def __init__(__self__, *, type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]], user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class WorkbookTemplateGalleryArgsDict(TypedDict):
    
    category: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    order: NotRequired[pulumi.Input[_builtins.int]]
    resource_type: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkbookTemplateGalleryArgs:
    def __init__(__self__, *, category: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., order: Optional[pulumi.Input[_builtins.int]] = ..., resource_type: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @order.setter
    def order(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkbookTemplateLocalizedGalleryArgsDict(TypedDict):
    
    galleries: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkbookTemplateGalleryArgsDict]]]]
    template_data: NotRequired[Any]


@pulumi.input_type
class WorkbookTemplateLocalizedGalleryArgs:
    def __init__(__self__, *, galleries: Optional[pulumi.Input[Sequence[pulumi.Input[WorkbookTemplateGalleryArgs]]]] = ..., template_data: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def galleries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkbookTemplateGalleryArgs]]]]:
        
        ...
    
    @galleries.setter
    def galleries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkbookTemplateGalleryArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="templateData")
    def template_data(self) -> Optional[Any]:
        
        ...
    
    @template_data.setter
    def template_data(self, value: Optional[Any]): # -> None:
        ...
    


