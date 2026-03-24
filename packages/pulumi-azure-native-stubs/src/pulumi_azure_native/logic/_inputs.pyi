

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AS2AcknowledgementConnectionSettingsArgs', 'AS2AcknowledgementConnectionSettingsArgsDict', 'AS2AgreementContentArgs', 'AS2AgreementContentArgsDict', 'AS2EnvelopeSettingsArgs', 'AS2EnvelopeSettingsArgsDict', 'AS2ErrorSettingsArgs', 'AS2ErrorSettingsArgsDict', 'AS2MdnSettingsArgs', 'AS2MdnSettingsArgsDict', 'AS2MessageConnectionSettingsArgs', 'AS2MessageConnectionSettingsArgsDict', 'AS2OneWayAgreementArgs', 'AS2OneWayAgreementArgsDict', 'AS2ProtocolSettingsArgs', 'AS2ProtocolSettingsArgsDict', 'AS2SecuritySettingsArgs', 'AS2SecuritySettingsArgsDict', 'AS2ValidationSettingsArgs', 'AS2ValidationSettingsArgsDict', 'AgreementContentArgs', 'AgreementContentArgsDict', 'AssemblyPropertiesArgs', 'AssemblyPropertiesArgsDict', 'B2BPartnerContentArgs', 'B2BPartnerContentArgsDict', 'BatchConfigurationPropertiesArgs', 'BatchConfigurationPropertiesArgsDict', 'BatchReleaseCriteriaArgs', 'BatchReleaseCriteriaArgsDict', 'BusinessIdentityArgs', 'BusinessIdentityArgsDict', 'ContentLinkArgs', 'ContentLinkArgsDict', 'EdifactAcknowledgementSettingsArgs', 'EdifactAcknowledgementSettingsArgsDict', 'EdifactAgreementContentArgs', 'EdifactAgreementContentArgsDict', 'EdifactDelimiterOverrideArgs', 'EdifactDelimiterOverrideArgsDict', 'EdifactEnvelopeOverrideArgs', 'EdifactEnvelopeOverrideArgsDict', 'EdifactEnvelopeSettingsArgs', 'EdifactEnvelopeSettingsArgsDict', 'EdifactFramingSettingsArgs', 'EdifactFramingSettingsArgsDict', 'EdifactMessageFilterArgs', 'EdifactMessageFilterArgsDict', 'EdifactMessageIdentifierArgs', 'EdifactMessageIdentifierArgsDict', 'EdifactOneWayAgreementArgs', 'EdifactOneWayAgreementArgsDict', 'EdifactProcessingSettingsArgs', 'EdifactProcessingSettingsArgsDict', 'EdifactProtocolSettingsArgs', 'EdifactProtocolSettingsArgsDict', 'EdifactSchemaReferenceArgs', 'EdifactSchemaReferenceArgsDict', 'EdifactValidationOverrideArgs', 'EdifactValidationOverrideArgsDict', 'EdifactValidationSettingsArgs', 'EdifactValidationSettingsArgsDict', 'FlowAccessControlConfigurationPolicyArgs', 'FlowAccessControlConfigurationPolicyArgsDict', 'FlowAccessControlConfigurationArgs', 'FlowAccessControlConfigurationArgsDict', 'FlowEndpointsConfigurationArgs', 'FlowEndpointsConfigurationArgsDict', 'FlowEndpointsArgs', 'FlowEndpointsArgsDict', ..., ..., 'IntegrationAccountSkuArgs', 'IntegrationAccountSkuArgsDict', ..., ..., ..., ..., 'IntegrationServiceEnvironmentAccessEndpointArgs', ..., ..., ..., 'IntegrationServiceEnvironmentPropertiesArgs', 'IntegrationServiceEnvironmentPropertiesArgsDict', 'IntegrationServiceEnvironmentSkuArgs', 'IntegrationServiceEnvironmentSkuArgsDict', 'IpAddressRangeArgs', 'IpAddressRangeArgsDict', 'IpAddressArgs', 'IpAddressArgsDict', 'KeyVaultKeyReferenceKeyVaultArgs', 'KeyVaultKeyReferenceKeyVaultArgsDict', 'KeyVaultKeyReferenceArgs', 'KeyVaultKeyReferenceArgsDict', 'KeyVaultReference', 'KeyVaultReferenceDict', 'ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict', 'NetworkConfigurationArgs', 'NetworkConfigurationArgsDict', 'OpenAuthenticationAccessPoliciesArgs', 'OpenAuthenticationAccessPoliciesArgsDict', 'OpenAuthenticationAccessPolicyArgs', 'OpenAuthenticationAccessPolicyArgsDict', 'OpenAuthenticationPolicyClaimArgs', 'OpenAuthenticationPolicyClaimArgsDict', 'PartnerContentArgs', 'PartnerContentArgsDict', 'RecurrenceScheduleOccurrenceArgs', 'RecurrenceScheduleOccurrenceArgsDict', 'RecurrenceScheduleArgs', 'RecurrenceScheduleArgsDict', 'ResourceReferenceArgs', 'ResourceReferenceArgsDict', 'RosettaNetPipAcknowledgmentOfReceiptSettingsArgs', ..., 'RosettaNetPipActivityBehaviorArgs', 'RosettaNetPipActivityBehaviorArgsDict', 'RosettaNetPipActivitySettingsArgs', 'RosettaNetPipActivitySettingsArgsDict', 'RosettaNetPipBusinessDocumentArgs', 'RosettaNetPipBusinessDocumentArgsDict', 'RosettaNetPipRoleSettingsArgs', 'RosettaNetPipRoleSettingsArgsDict', 'WorkflowParameterArgs', 'WorkflowParameterArgsDict', 'WorkflowTriggerRecurrenceArgs', 'WorkflowTriggerRecurrenceArgsDict', 'X12AcknowledgementSettingsArgs', 'X12AcknowledgementSettingsArgsDict', 'X12AgreementContentArgs', 'X12AgreementContentArgsDict', 'X12DelimiterOverridesArgs', 'X12DelimiterOverridesArgsDict', 'X12EnvelopeOverrideArgs', 'X12EnvelopeOverrideArgsDict', 'X12EnvelopeSettingsArgs', 'X12EnvelopeSettingsArgsDict', 'X12FramingSettingsArgs', 'X12FramingSettingsArgsDict', 'X12MessageFilterArgs', 'X12MessageFilterArgsDict', 'X12MessageIdentifierArgs', 'X12MessageIdentifierArgsDict', 'X12OneWayAgreementArgs', 'X12OneWayAgreementArgsDict', 'X12ProcessingSettingsArgs', 'X12ProcessingSettingsArgsDict', 'X12ProtocolSettingsArgs', 'X12ProtocolSettingsArgsDict', 'X12SchemaReferenceArgs', 'X12SchemaReferenceArgsDict', 'X12SecuritySettingsArgs', 'X12SecuritySettingsArgsDict', 'X12ValidationOverrideArgs', 'X12ValidationOverrideArgsDict', 'X12ValidationSettingsArgs', 'X12ValidationSettingsArgsDict']
class AS2AcknowledgementConnectionSettingsArgsDict(TypedDict):
    
    ignore_certificate_name_mismatch: pulumi.Input[_builtins.bool]
    keep_http_connection_alive: pulumi.Input[_builtins.bool]
    support_http_status_code_continue: pulumi.Input[_builtins.bool]
    unfold_http_headers: pulumi.Input[_builtins.bool]


@pulumi.input_type
class AS2AcknowledgementConnectionSettingsArgs:
    def __init__(__self__, *, ignore_certificate_name_mismatch: pulumi.Input[_builtins.bool], keep_http_connection_alive: pulumi.Input[_builtins.bool], support_http_status_code_continue: pulumi.Input[_builtins.bool], unfold_http_headers: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCertificateNameMismatch")
    def ignore_certificate_name_mismatch(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @ignore_certificate_name_mismatch.setter
    def ignore_certificate_name_mismatch(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keepHttpConnectionAlive")
    def keep_http_connection_alive(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @keep_http_connection_alive.setter
    def keep_http_connection_alive(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportHttpStatusCodeContinue")
    def support_http_status_code_continue(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @support_http_status_code_continue.setter
    def support_http_status_code_continue(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unfoldHttpHeaders")
    def unfold_http_headers(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @unfold_http_headers.setter
    def unfold_http_headers(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class AS2AgreementContentArgsDict(TypedDict):
    
    receive_agreement: pulumi.Input[AS2OneWayAgreementArgsDict]
    send_agreement: pulumi.Input[AS2OneWayAgreementArgsDict]


@pulumi.input_type
class AS2AgreementContentArgs:
    def __init__(__self__, *, receive_agreement: pulumi.Input[AS2OneWayAgreementArgs], send_agreement: pulumi.Input[AS2OneWayAgreementArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiveAgreement")
    def receive_agreement(self) -> pulumi.Input[AS2OneWayAgreementArgs]:
        
        ...
    
    @receive_agreement.setter
    def receive_agreement(self, value: pulumi.Input[AS2OneWayAgreementArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAgreement")
    def send_agreement(self) -> pulumi.Input[AS2OneWayAgreementArgs]:
        
        ...
    
    @send_agreement.setter
    def send_agreement(self, value: pulumi.Input[AS2OneWayAgreementArgs]): # -> None:
        ...
    


class AS2EnvelopeSettingsArgsDict(TypedDict):
    
    autogenerate_file_name: pulumi.Input[_builtins.bool]
    file_name_template: pulumi.Input[_builtins.str]
    message_content_type: pulumi.Input[_builtins.str]
    suspend_message_on_file_name_generation_error: pulumi.Input[_builtins.bool]
    transmit_file_name_in_mime_header: pulumi.Input[_builtins.bool]


@pulumi.input_type
class AS2EnvelopeSettingsArgs:
    def __init__(__self__, *, autogenerate_file_name: pulumi.Input[_builtins.bool], file_name_template: pulumi.Input[_builtins.str], message_content_type: pulumi.Input[_builtins.str], suspend_message_on_file_name_generation_error: pulumi.Input[_builtins.bool], transmit_file_name_in_mime_header: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autogenerateFileName")
    def autogenerate_file_name(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @autogenerate_file_name.setter
    def autogenerate_file_name(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fileNameTemplate")
    def file_name_template(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @file_name_template.setter
    def file_name_template(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageContentType")
    def message_content_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_content_type.setter
    def message_content_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspendMessageOnFileNameGenerationError")
    def suspend_message_on_file_name_generation_error(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @suspend_message_on_file_name_generation_error.setter
    def suspend_message_on_file_name_generation_error(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transmitFileNameInMimeHeader")
    def transmit_file_name_in_mime_header(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @transmit_file_name_in_mime_header.setter
    def transmit_file_name_in_mime_header(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class AS2ErrorSettingsArgsDict(TypedDict):
    
    resend_if_mdn_not_received: pulumi.Input[_builtins.bool]
    suspend_duplicate_message: pulumi.Input[_builtins.bool]


@pulumi.input_type
class AS2ErrorSettingsArgs:
    def __init__(__self__, *, resend_if_mdn_not_received: pulumi.Input[_builtins.bool], suspend_duplicate_message: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="resendIfMDNNotReceived")
    def resend_if_mdn_not_received(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @resend_if_mdn_not_received.setter
    def resend_if_mdn_not_received(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspendDuplicateMessage")
    def suspend_duplicate_message(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @suspend_duplicate_message.setter
    def suspend_duplicate_message(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class AS2MdnSettingsArgsDict(TypedDict):
    
    mic_hashing_algorithm: pulumi.Input[Union[_builtins.str, HashingAlgorithm]]
    need_mdn: pulumi.Input[_builtins.bool]
    send_inbound_mdn_to_message_box: pulumi.Input[_builtins.bool]
    send_mdnasynchronously: pulumi.Input[_builtins.bool]
    sign_mdn: pulumi.Input[_builtins.bool]
    sign_outbound_mdn_if_optional: pulumi.Input[_builtins.bool]
    disposition_notification_to: NotRequired[pulumi.Input[_builtins.str]]
    mdn_text: NotRequired[pulumi.Input[_builtins.str]]
    receipt_delivery_url: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AS2MdnSettingsArgs:
    def __init__(__self__, *, mic_hashing_algorithm: pulumi.Input[Union[_builtins.str, HashingAlgorithm]], need_mdn: pulumi.Input[_builtins.bool], send_inbound_mdn_to_message_box: pulumi.Input[_builtins.bool], send_mdnasynchronously: pulumi.Input[_builtins.bool], sign_mdn: pulumi.Input[_builtins.bool], sign_outbound_mdn_if_optional: pulumi.Input[_builtins.bool], disposition_notification_to: Optional[pulumi.Input[_builtins.str]] = ..., mdn_text: Optional[pulumi.Input[_builtins.str]] = ..., receipt_delivery_url: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="micHashingAlgorithm")
    def mic_hashing_algorithm(self) -> pulumi.Input[Union[_builtins.str, HashingAlgorithm]]:
        
        ...
    
    @mic_hashing_algorithm.setter
    def mic_hashing_algorithm(self, value: pulumi.Input[Union[_builtins.str, HashingAlgorithm]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="needMDN")
    def need_mdn(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @need_mdn.setter
    def need_mdn(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendInboundMDNToMessageBox")
    def send_inbound_mdn_to_message_box(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @send_inbound_mdn_to_message_box.setter
    def send_inbound_mdn_to_message_box(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendMDNAsynchronously")
    def send_mdnasynchronously(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @send_mdnasynchronously.setter
    def send_mdnasynchronously(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signMDN")
    def sign_mdn(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @sign_mdn.setter
    def sign_mdn(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signOutboundMDNIfOptional")
    def sign_outbound_mdn_if_optional(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @sign_outbound_mdn_if_optional.setter
    def sign_outbound_mdn_if_optional(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dispositionNotificationTo")
    def disposition_notification_to(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disposition_notification_to.setter
    def disposition_notification_to(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mdnText")
    def mdn_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mdn_text.setter
    def mdn_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiptDeliveryUrl")
    def receipt_delivery_url(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @receipt_delivery_url.setter
    def receipt_delivery_url(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AS2MessageConnectionSettingsArgsDict(TypedDict):
    
    ignore_certificate_name_mismatch: pulumi.Input[_builtins.bool]
    keep_http_connection_alive: pulumi.Input[_builtins.bool]
    support_http_status_code_continue: pulumi.Input[_builtins.bool]
    unfold_http_headers: pulumi.Input[_builtins.bool]


@pulumi.input_type
class AS2MessageConnectionSettingsArgs:
    def __init__(__self__, *, ignore_certificate_name_mismatch: pulumi.Input[_builtins.bool], keep_http_connection_alive: pulumi.Input[_builtins.bool], support_http_status_code_continue: pulumi.Input[_builtins.bool], unfold_http_headers: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreCertificateNameMismatch")
    def ignore_certificate_name_mismatch(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @ignore_certificate_name_mismatch.setter
    def ignore_certificate_name_mismatch(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keepHttpConnectionAlive")
    def keep_http_connection_alive(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @keep_http_connection_alive.setter
    def keep_http_connection_alive(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportHttpStatusCodeContinue")
    def support_http_status_code_continue(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @support_http_status_code_continue.setter
    def support_http_status_code_continue(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="unfoldHttpHeaders")
    def unfold_http_headers(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @unfold_http_headers.setter
    def unfold_http_headers(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class AS2OneWayAgreementArgsDict(TypedDict):
    
    protocol_settings: pulumi.Input[AS2ProtocolSettingsArgsDict]
    receiver_business_identity: pulumi.Input[BusinessIdentityArgsDict]
    sender_business_identity: pulumi.Input[BusinessIdentityArgsDict]


@pulumi.input_type
class AS2OneWayAgreementArgs:
    def __init__(__self__, *, protocol_settings: pulumi.Input[AS2ProtocolSettingsArgs], receiver_business_identity: pulumi.Input[BusinessIdentityArgs], sender_business_identity: pulumi.Input[BusinessIdentityArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolSettings")
    def protocol_settings(self) -> pulumi.Input[AS2ProtocolSettingsArgs]:
        
        ...
    
    @protocol_settings.setter
    def protocol_settings(self, value: pulumi.Input[AS2ProtocolSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverBusinessIdentity")
    def receiver_business_identity(self) -> pulumi.Input[BusinessIdentityArgs]:
        
        ...
    
    @receiver_business_identity.setter
    def receiver_business_identity(self, value: pulumi.Input[BusinessIdentityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderBusinessIdentity")
    def sender_business_identity(self) -> pulumi.Input[BusinessIdentityArgs]:
        
        ...
    
    @sender_business_identity.setter
    def sender_business_identity(self, value: pulumi.Input[BusinessIdentityArgs]): # -> None:
        ...
    


class AS2ProtocolSettingsArgsDict(TypedDict):
    
    acknowledgement_connection_settings: pulumi.Input[AS2AcknowledgementConnectionSettingsArgsDict]
    envelope_settings: pulumi.Input[AS2EnvelopeSettingsArgsDict]
    error_settings: pulumi.Input[AS2ErrorSettingsArgsDict]
    mdn_settings: pulumi.Input[AS2MdnSettingsArgsDict]
    message_connection_settings: pulumi.Input[AS2MessageConnectionSettingsArgsDict]
    security_settings: pulumi.Input[AS2SecuritySettingsArgsDict]
    validation_settings: pulumi.Input[AS2ValidationSettingsArgsDict]


@pulumi.input_type
class AS2ProtocolSettingsArgs:
    def __init__(__self__, *, acknowledgement_connection_settings: pulumi.Input[AS2AcknowledgementConnectionSettingsArgs], envelope_settings: pulumi.Input[AS2EnvelopeSettingsArgs], error_settings: pulumi.Input[AS2ErrorSettingsArgs], mdn_settings: pulumi.Input[AS2MdnSettingsArgs], message_connection_settings: pulumi.Input[AS2MessageConnectionSettingsArgs], security_settings: pulumi.Input[AS2SecuritySettingsArgs], validation_settings: pulumi.Input[AS2ValidationSettingsArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementConnectionSettings")
    def acknowledgement_connection_settings(self) -> pulumi.Input[AS2AcknowledgementConnectionSettingsArgs]:
        
        ...
    
    @acknowledgement_connection_settings.setter
    def acknowledgement_connection_settings(self, value: pulumi.Input[AS2AcknowledgementConnectionSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envelopeSettings")
    def envelope_settings(self) -> pulumi.Input[AS2EnvelopeSettingsArgs]:
        
        ...
    
    @envelope_settings.setter
    def envelope_settings(self, value: pulumi.Input[AS2EnvelopeSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorSettings")
    def error_settings(self) -> pulumi.Input[AS2ErrorSettingsArgs]:
        
        ...
    
    @error_settings.setter
    def error_settings(self, value: pulumi.Input[AS2ErrorSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mdnSettings")
    def mdn_settings(self) -> pulumi.Input[AS2MdnSettingsArgs]:
        
        ...
    
    @mdn_settings.setter
    def mdn_settings(self, value: pulumi.Input[AS2MdnSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageConnectionSettings")
    def message_connection_settings(self) -> pulumi.Input[AS2MessageConnectionSettingsArgs]:
        
        ...
    
    @message_connection_settings.setter
    def message_connection_settings(self, value: pulumi.Input[AS2MessageConnectionSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> pulumi.Input[AS2SecuritySettingsArgs]:
        
        ...
    
    @security_settings.setter
    def security_settings(self, value: pulumi.Input[AS2SecuritySettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationSettings")
    def validation_settings(self) -> pulumi.Input[AS2ValidationSettingsArgs]:
        
        ...
    
    @validation_settings.setter
    def validation_settings(self, value: pulumi.Input[AS2ValidationSettingsArgs]): # -> None:
        ...
    


class AS2SecuritySettingsArgsDict(TypedDict):
    
    enable_nrr_for_inbound_decoded_messages: pulumi.Input[_builtins.bool]
    enable_nrr_for_inbound_encoded_messages: pulumi.Input[_builtins.bool]
    enable_nrr_for_inbound_mdn: pulumi.Input[_builtins.bool]
    enable_nrr_for_outbound_decoded_messages: pulumi.Input[_builtins.bool]
    enable_nrr_for_outbound_encoded_messages: pulumi.Input[_builtins.bool]
    enable_nrr_for_outbound_mdn: pulumi.Input[_builtins.bool]
    override_group_signing_certificate: pulumi.Input[_builtins.bool]
    encryption_certificate_name: NotRequired[pulumi.Input[_builtins.str]]
    sha2_algorithm_format: NotRequired[pulumi.Input[_builtins.str]]
    signing_certificate_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class AS2SecuritySettingsArgs:
    def __init__(__self__, *, enable_nrr_for_inbound_decoded_messages: pulumi.Input[_builtins.bool], enable_nrr_for_inbound_encoded_messages: pulumi.Input[_builtins.bool], enable_nrr_for_inbound_mdn: pulumi.Input[_builtins.bool], enable_nrr_for_outbound_decoded_messages: pulumi.Input[_builtins.bool], enable_nrr_for_outbound_encoded_messages: pulumi.Input[_builtins.bool], enable_nrr_for_outbound_mdn: pulumi.Input[_builtins.bool], override_group_signing_certificate: pulumi.Input[_builtins.bool], encryption_certificate_name: Optional[pulumi.Input[_builtins.str]] = ..., sha2_algorithm_format: Optional[pulumi.Input[_builtins.str]] = ..., signing_certificate_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNRRForInboundDecodedMessages")
    def enable_nrr_for_inbound_decoded_messages(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_nrr_for_inbound_decoded_messages.setter
    def enable_nrr_for_inbound_decoded_messages(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNRRForInboundEncodedMessages")
    def enable_nrr_for_inbound_encoded_messages(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_nrr_for_inbound_encoded_messages.setter
    def enable_nrr_for_inbound_encoded_messages(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNRRForInboundMDN")
    def enable_nrr_for_inbound_mdn(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_nrr_for_inbound_mdn.setter
    def enable_nrr_for_inbound_mdn(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNRRForOutboundDecodedMessages")
    def enable_nrr_for_outbound_decoded_messages(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_nrr_for_outbound_decoded_messages.setter
    def enable_nrr_for_outbound_decoded_messages(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNRRForOutboundEncodedMessages")
    def enable_nrr_for_outbound_encoded_messages(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_nrr_for_outbound_encoded_messages.setter
    def enable_nrr_for_outbound_encoded_messages(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNRRForOutboundMDN")
    def enable_nrr_for_outbound_mdn(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_nrr_for_outbound_mdn.setter
    def enable_nrr_for_outbound_mdn(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideGroupSigningCertificate")
    def override_group_signing_certificate(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @override_group_signing_certificate.setter
    def override_group_signing_certificate(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionCertificateName")
    def encryption_certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @encryption_certificate_name.setter
    def encryption_certificate_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sha2AlgorithmFormat")
    def sha2_algorithm_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sha2_algorithm_format.setter
    def sha2_algorithm_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingCertificateName")
    def signing_certificate_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @signing_certificate_name.setter
    def signing_certificate_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class AS2ValidationSettingsArgsDict(TypedDict):
    
    check_certificate_revocation_list_on_receive: pulumi.Input[_builtins.bool]
    check_certificate_revocation_list_on_send: pulumi.Input[_builtins.bool]
    check_duplicate_message: pulumi.Input[_builtins.bool]
    compress_message: pulumi.Input[_builtins.bool]
    encrypt_message: pulumi.Input[_builtins.bool]
    encryption_algorithm: pulumi.Input[Union[_builtins.str, EncryptionAlgorithm]]
    interchange_duplicates_validity_days: pulumi.Input[_builtins.int]
    override_message_properties: pulumi.Input[_builtins.bool]
    sign_message: pulumi.Input[_builtins.bool]
    signing_algorithm: NotRequired[pulumi.Input[Union[_builtins.str, SigningAlgorithm]]]


@pulumi.input_type
class AS2ValidationSettingsArgs:
    def __init__(__self__, *, check_certificate_revocation_list_on_receive: pulumi.Input[_builtins.bool], check_certificate_revocation_list_on_send: pulumi.Input[_builtins.bool], check_duplicate_message: pulumi.Input[_builtins.bool], compress_message: pulumi.Input[_builtins.bool], encrypt_message: pulumi.Input[_builtins.bool], encryption_algorithm: pulumi.Input[Union[_builtins.str, EncryptionAlgorithm]], interchange_duplicates_validity_days: pulumi.Input[_builtins.int], override_message_properties: pulumi.Input[_builtins.bool], sign_message: pulumi.Input[_builtins.bool], signing_algorithm: Optional[pulumi.Input[Union[_builtins.str, SigningAlgorithm]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkCertificateRevocationListOnReceive")
    def check_certificate_revocation_list_on_receive(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @check_certificate_revocation_list_on_receive.setter
    def check_certificate_revocation_list_on_receive(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkCertificateRevocationListOnSend")
    def check_certificate_revocation_list_on_send(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @check_certificate_revocation_list_on_send.setter
    def check_certificate_revocation_list_on_send(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkDuplicateMessage")
    def check_duplicate_message(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @check_duplicate_message.setter
    def check_duplicate_message(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="compressMessage")
    def compress_message(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @compress_message.setter
    def compress_message(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptMessage")
    def encrypt_message(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @encrypt_message.setter
    def encrypt_message(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> pulumi.Input[Union[_builtins.str, EncryptionAlgorithm]]:
        
        ...
    
    @encryption_algorithm.setter
    def encryption_algorithm(self, value: pulumi.Input[Union[_builtins.str, EncryptionAlgorithm]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interchangeDuplicatesValidityDays")
    def interchange_duplicates_validity_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @interchange_duplicates_validity_days.setter
    def interchange_duplicates_validity_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overrideMessageProperties")
    def override_message_properties(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @override_message_properties.setter
    def override_message_properties(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signMessage")
    def sign_message(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @sign_message.setter
    def sign_message(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="signingAlgorithm")
    def signing_algorithm(self) -> Optional[pulumi.Input[Union[_builtins.str, SigningAlgorithm]]]:
        
        ...
    
    @signing_algorithm.setter
    def signing_algorithm(self, value: Optional[pulumi.Input[Union[_builtins.str, SigningAlgorithm]]]): # -> None:
        ...
    


class AgreementContentArgsDict(TypedDict):
    
    a_s2: NotRequired[pulumi.Input[AS2AgreementContentArgsDict]]
    edifact: NotRequired[pulumi.Input[EdifactAgreementContentArgsDict]]
    x12: NotRequired[pulumi.Input[X12AgreementContentArgsDict]]


@pulumi.input_type
class AgreementContentArgs:
    def __init__(__self__, *, a_s2: Optional[pulumi.Input[AS2AgreementContentArgs]] = ..., edifact: Optional[pulumi.Input[EdifactAgreementContentArgs]] = ..., x12: Optional[pulumi.Input[X12AgreementContentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="aS2")
    def a_s2(self) -> Optional[pulumi.Input[AS2AgreementContentArgs]]:
        
        ...
    
    @a_s2.setter
    def a_s2(self, value: Optional[pulumi.Input[AS2AgreementContentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edifact(self) -> Optional[pulumi.Input[EdifactAgreementContentArgs]]:
        
        ...
    
    @edifact.setter
    def edifact(self, value: Optional[pulumi.Input[EdifactAgreementContentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def x12(self) -> Optional[pulumi.Input[X12AgreementContentArgs]]:
        
        ...
    
    @x12.setter
    def x12(self, value: Optional[pulumi.Input[X12AgreementContentArgs]]): # -> None:
        ...
    


class AssemblyPropertiesArgsDict(TypedDict):
    
    assembly_name: pulumi.Input[_builtins.str]
    assembly_culture: NotRequired[pulumi.Input[_builtins.str]]
    assembly_public_key_token: NotRequired[pulumi.Input[_builtins.str]]
    assembly_version: NotRequired[pulumi.Input[_builtins.str]]
    changed_time: NotRequired[pulumi.Input[_builtins.str]]
    content: NotRequired[Any]
    content_link: NotRequired[pulumi.Input[ContentLinkArgsDict]]
    content_type: NotRequired[pulumi.Input[_builtins.str]]
    created_time: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[Any]


@pulumi.input_type
class AssemblyPropertiesArgs:
    def __init__(__self__, *, assembly_name: pulumi.Input[_builtins.str], assembly_culture: Optional[pulumi.Input[_builtins.str]] = ..., assembly_public_key_token: Optional[pulumi.Input[_builtins.str]] = ..., assembly_version: Optional[pulumi.Input[_builtins.str]] = ..., changed_time: Optional[pulumi.Input[_builtins.str]] = ..., content: Optional[Any] = ..., content_link: Optional[pulumi.Input[ContentLinkArgs]] = ..., content_type: Optional[pulumi.Input[_builtins.str]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="assemblyName")
    def assembly_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @assembly_name.setter
    def assembly_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assemblyCulture")
    def assembly_culture(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assembly_culture.setter
    def assembly_culture(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assemblyPublicKeyToken")
    def assembly_public_key_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assembly_public_key_token.setter
    def assembly_public_key_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assemblyVersion")
    def assembly_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @assembly_version.setter
    def assembly_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @changed_time.setter
    def changed_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def content(self) -> Optional[Any]:
        ...
    
    @content.setter
    def content(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> Optional[pulumi.Input[ContentLinkArgs]]:
        
        ...
    
    @content_link.setter
    def content_link(self, value: Optional[pulumi.Input[ContentLinkArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[Any]): # -> None:
        ...
    


class B2BPartnerContentArgsDict(TypedDict):
    
    business_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[BusinessIdentityArgsDict]]]]


@pulumi.input_type
class B2BPartnerContentArgs:
    def __init__(__self__, *, business_identities: Optional[pulumi.Input[Sequence[pulumi.Input[BusinessIdentityArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessIdentities")
    def business_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BusinessIdentityArgs]]]]:
        
        ...
    
    @business_identities.setter
    def business_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BusinessIdentityArgs]]]]): # -> None:
        ...
    


class BatchConfigurationPropertiesArgsDict(TypedDict):
    
    batch_group_name: pulumi.Input[_builtins.str]
    release_criteria: pulumi.Input[BatchReleaseCriteriaArgsDict]
    changed_time: NotRequired[pulumi.Input[_builtins.str]]
    created_time: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[Any]


@pulumi.input_type
class BatchConfigurationPropertiesArgs:
    def __init__(__self__, *, batch_group_name: pulumi.Input[_builtins.str], release_criteria: pulumi.Input[BatchReleaseCriteriaArgs], changed_time: Optional[pulumi.Input[_builtins.str]] = ..., created_time: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchGroupName")
    def batch_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @batch_group_name.setter
    def batch_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseCriteria")
    def release_criteria(self) -> pulumi.Input[BatchReleaseCriteriaArgs]:
        
        ...
    
    @release_criteria.setter
    def release_criteria(self, value: pulumi.Input[BatchReleaseCriteriaArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @changed_time.setter
    def changed_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[Any]): # -> None:
        ...
    


class BatchReleaseCriteriaArgsDict(TypedDict):
    
    batch_size: NotRequired[pulumi.Input[_builtins.int]]
    message_count: NotRequired[pulumi.Input[_builtins.int]]
    recurrence: NotRequired[pulumi.Input[WorkflowTriggerRecurrenceArgsDict]]


@pulumi.input_type
class BatchReleaseCriteriaArgs:
    def __init__(__self__, *, batch_size: Optional[pulumi.Input[_builtins.int]] = ..., message_count: Optional[pulumi.Input[_builtins.int]] = ..., recurrence: Optional[pulumi.Input[WorkflowTriggerRecurrenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchSize")
    def batch_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @batch_size.setter
    def batch_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageCount")
    def message_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @message_count.setter
    def message_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input[WorkflowTriggerRecurrenceArgs]]:
        
        ...
    
    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input[WorkflowTriggerRecurrenceArgs]]): # -> None:
        ...
    


class BusinessIdentityArgsDict(TypedDict):
    
    qualifier: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class BusinessIdentityArgs:
    def __init__(__self__, *, qualifier: pulumi.Input[_builtins.str], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def qualifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @qualifier.setter
    def qualifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ContentLinkArgsDict(TypedDict):
    
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ContentLinkArgs:
    def __init__(__self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EdifactAcknowledgementSettingsArgsDict(TypedDict):
    
    acknowledgement_control_number_lower_bound: pulumi.Input[_builtins.int]
    acknowledgement_control_number_upper_bound: pulumi.Input[_builtins.int]
    batch_functional_acknowledgements: pulumi.Input[_builtins.bool]
    batch_technical_acknowledgements: pulumi.Input[_builtins.bool]
    need_functional_acknowledgement: pulumi.Input[_builtins.bool]
    need_loop_for_valid_messages: pulumi.Input[_builtins.bool]
    need_technical_acknowledgement: pulumi.Input[_builtins.bool]
    rollover_acknowledgement_control_number: pulumi.Input[_builtins.bool]
    send_synchronous_acknowledgement: pulumi.Input[_builtins.bool]
    acknowledgement_control_number_prefix: NotRequired[pulumi.Input[_builtins.str]]
    acknowledgement_control_number_suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EdifactAcknowledgementSettingsArgs:
    def __init__(__self__, *, acknowledgement_control_number_lower_bound: pulumi.Input[_builtins.int], acknowledgement_control_number_upper_bound: pulumi.Input[_builtins.int], batch_functional_acknowledgements: pulumi.Input[_builtins.bool], batch_technical_acknowledgements: pulumi.Input[_builtins.bool], need_functional_acknowledgement: pulumi.Input[_builtins.bool], need_loop_for_valid_messages: pulumi.Input[_builtins.bool], need_technical_acknowledgement: pulumi.Input[_builtins.bool], rollover_acknowledgement_control_number: pulumi.Input[_builtins.bool], send_synchronous_acknowledgement: pulumi.Input[_builtins.bool], acknowledgement_control_number_prefix: Optional[pulumi.Input[_builtins.str]] = ..., acknowledgement_control_number_suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementControlNumberLowerBound")
    def acknowledgement_control_number_lower_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @acknowledgement_control_number_lower_bound.setter
    def acknowledgement_control_number_lower_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementControlNumberUpperBound")
    def acknowledgement_control_number_upper_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @acknowledgement_control_number_upper_bound.setter
    def acknowledgement_control_number_upper_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchFunctionalAcknowledgements")
    def batch_functional_acknowledgements(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @batch_functional_acknowledgements.setter
    def batch_functional_acknowledgements(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchTechnicalAcknowledgements")
    def batch_technical_acknowledgements(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @batch_technical_acknowledgements.setter
    def batch_technical_acknowledgements(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="needFunctionalAcknowledgement")
    def need_functional_acknowledgement(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @need_functional_acknowledgement.setter
    def need_functional_acknowledgement(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="needLoopForValidMessages")
    def need_loop_for_valid_messages(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @need_loop_for_valid_messages.setter
    def need_loop_for_valid_messages(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="needTechnicalAcknowledgement")
    def need_technical_acknowledgement(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @need_technical_acknowledgement.setter
    def need_technical_acknowledgement(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloverAcknowledgementControlNumber")
    def rollover_acknowledgement_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @rollover_acknowledgement_control_number.setter
    def rollover_acknowledgement_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendSynchronousAcknowledgement")
    def send_synchronous_acknowledgement(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @send_synchronous_acknowledgement.setter
    def send_synchronous_acknowledgement(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementControlNumberPrefix")
    def acknowledgement_control_number_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acknowledgement_control_number_prefix.setter
    def acknowledgement_control_number_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementControlNumberSuffix")
    def acknowledgement_control_number_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acknowledgement_control_number_suffix.setter
    def acknowledgement_control_number_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EdifactAgreementContentArgsDict(TypedDict):
    
    receive_agreement: pulumi.Input[EdifactOneWayAgreementArgsDict]
    send_agreement: pulumi.Input[EdifactOneWayAgreementArgsDict]


@pulumi.input_type
class EdifactAgreementContentArgs:
    def __init__(__self__, *, receive_agreement: pulumi.Input[EdifactOneWayAgreementArgs], send_agreement: pulumi.Input[EdifactOneWayAgreementArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiveAgreement")
    def receive_agreement(self) -> pulumi.Input[EdifactOneWayAgreementArgs]:
        
        ...
    
    @receive_agreement.setter
    def receive_agreement(self, value: pulumi.Input[EdifactOneWayAgreementArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAgreement")
    def send_agreement(self) -> pulumi.Input[EdifactOneWayAgreementArgs]:
        
        ...
    
    @send_agreement.setter
    def send_agreement(self, value: pulumi.Input[EdifactOneWayAgreementArgs]): # -> None:
        ...
    


class EdifactDelimiterOverrideArgsDict(TypedDict):
    
    component_separator: pulumi.Input[_builtins.int]
    data_element_separator: pulumi.Input[_builtins.int]
    decimal_point_indicator: pulumi.Input[EdifactDecimalIndicator]
    release_indicator: pulumi.Input[_builtins.int]
    repetition_separator: pulumi.Input[_builtins.int]
    segment_terminator: pulumi.Input[_builtins.int]
    segment_terminator_suffix: pulumi.Input[SegmentTerminatorSuffix]
    message_association_assigned_code: NotRequired[pulumi.Input[_builtins.str]]
    message_id: NotRequired[pulumi.Input[_builtins.str]]
    message_release: NotRequired[pulumi.Input[_builtins.str]]
    message_version: NotRequired[pulumi.Input[_builtins.str]]
    target_namespace: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EdifactDelimiterOverrideArgs:
    def __init__(__self__, *, component_separator: pulumi.Input[_builtins.int], data_element_separator: pulumi.Input[_builtins.int], decimal_point_indicator: pulumi.Input[EdifactDecimalIndicator], release_indicator: pulumi.Input[_builtins.int], repetition_separator: pulumi.Input[_builtins.int], segment_terminator: pulumi.Input[_builtins.int], segment_terminator_suffix: pulumi.Input[SegmentTerminatorSuffix], message_association_assigned_code: Optional[pulumi.Input[_builtins.str]] = ..., message_id: Optional[pulumi.Input[_builtins.str]] = ..., message_release: Optional[pulumi.Input[_builtins.str]] = ..., message_version: Optional[pulumi.Input[_builtins.str]] = ..., target_namespace: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentSeparator")
    def component_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @component_separator.setter
    def component_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataElementSeparator")
    def data_element_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @data_element_separator.setter
    def data_element_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="decimalPointIndicator")
    def decimal_point_indicator(self) -> pulumi.Input[EdifactDecimalIndicator]:
        
        ...
    
    @decimal_point_indicator.setter
    def decimal_point_indicator(self, value: pulumi.Input[EdifactDecimalIndicator]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseIndicator")
    def release_indicator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @release_indicator.setter
    def release_indicator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repetitionSeparator")
    def repetition_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @repetition_separator.setter
    def repetition_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentTerminator")
    def segment_terminator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @segment_terminator.setter
    def segment_terminator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentTerminatorSuffix")
    def segment_terminator_suffix(self) -> pulumi.Input[SegmentTerminatorSuffix]:
        
        ...
    
    @segment_terminator_suffix.setter
    def segment_terminator_suffix(self, value: pulumi.Input[SegmentTerminatorSuffix]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageAssociationAssignedCode")
    def message_association_assigned_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_association_assigned_code.setter
    def message_association_assigned_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRelease")
    def message_release(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_release.setter
    def message_release(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageVersion")
    def message_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_version.setter
    def message_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_namespace.setter
    def target_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EdifactEnvelopeOverrideArgsDict(TypedDict):
    
    application_password: NotRequired[pulumi.Input[_builtins.str]]
    association_assigned_code: NotRequired[pulumi.Input[_builtins.str]]
    controlling_agency_code: NotRequired[pulumi.Input[_builtins.str]]
    functional_group_id: NotRequired[pulumi.Input[_builtins.str]]
    group_header_message_release: NotRequired[pulumi.Input[_builtins.str]]
    group_header_message_version: NotRequired[pulumi.Input[_builtins.str]]
    message_association_assigned_code: NotRequired[pulumi.Input[_builtins.str]]
    message_id: NotRequired[pulumi.Input[_builtins.str]]
    message_release: NotRequired[pulumi.Input[_builtins.str]]
    message_version: NotRequired[pulumi.Input[_builtins.str]]
    receiver_application_id: NotRequired[pulumi.Input[_builtins.str]]
    receiver_application_qualifier: NotRequired[pulumi.Input[_builtins.str]]
    sender_application_id: NotRequired[pulumi.Input[_builtins.str]]
    sender_application_qualifier: NotRequired[pulumi.Input[_builtins.str]]
    target_namespace: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EdifactEnvelopeOverrideArgs:
    def __init__(__self__, *, application_password: Optional[pulumi.Input[_builtins.str]] = ..., association_assigned_code: Optional[pulumi.Input[_builtins.str]] = ..., controlling_agency_code: Optional[pulumi.Input[_builtins.str]] = ..., functional_group_id: Optional[pulumi.Input[_builtins.str]] = ..., group_header_message_release: Optional[pulumi.Input[_builtins.str]] = ..., group_header_message_version: Optional[pulumi.Input[_builtins.str]] = ..., message_association_assigned_code: Optional[pulumi.Input[_builtins.str]] = ..., message_id: Optional[pulumi.Input[_builtins.str]] = ..., message_release: Optional[pulumi.Input[_builtins.str]] = ..., message_version: Optional[pulumi.Input[_builtins.str]] = ..., receiver_application_id: Optional[pulumi.Input[_builtins.str]] = ..., receiver_application_qualifier: Optional[pulumi.Input[_builtins.str]] = ..., sender_application_id: Optional[pulumi.Input[_builtins.str]] = ..., sender_application_qualifier: Optional[pulumi.Input[_builtins.str]] = ..., target_namespace: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationPassword")
    def application_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_password.setter
    def application_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationAssignedCode")
    def association_assigned_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @association_assigned_code.setter
    def association_assigned_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controllingAgencyCode")
    def controlling_agency_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @controlling_agency_code.setter
    def controlling_agency_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionalGroupId")
    def functional_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @functional_group_id.setter
    def functional_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupHeaderMessageRelease")
    def group_header_message_release(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_header_message_release.setter
    def group_header_message_release(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupHeaderMessageVersion")
    def group_header_message_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_header_message_version.setter
    def group_header_message_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageAssociationAssignedCode")
    def message_association_assigned_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_association_assigned_code.setter
    def message_association_assigned_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRelease")
    def message_release(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_release.setter
    def message_release(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageVersion")
    def message_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_version.setter
    def message_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverApplicationId")
    def receiver_application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @receiver_application_id.setter
    def receiver_application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverApplicationQualifier")
    def receiver_application_qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @receiver_application_qualifier.setter
    def receiver_application_qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderApplicationId")
    def sender_application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sender_application_id.setter
    def sender_application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderApplicationQualifier")
    def sender_application_qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sender_application_qualifier.setter
    def sender_application_qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_namespace.setter
    def target_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EdifactEnvelopeSettingsArgsDict(TypedDict):
    
    apply_delimiter_string_advice: pulumi.Input[_builtins.bool]
    create_grouping_segments: pulumi.Input[_builtins.bool]
    enable_default_group_headers: pulumi.Input[_builtins.bool]
    group_control_number_lower_bound: pulumi.Input[_builtins.float]
    group_control_number_upper_bound: pulumi.Input[_builtins.float]
    interchange_control_number_lower_bound: pulumi.Input[_builtins.float]
    interchange_control_number_upper_bound: pulumi.Input[_builtins.float]
    is_test_interchange: pulumi.Input[_builtins.bool]
    overwrite_existing_transaction_set_control_number: pulumi.Input[_builtins.bool]
    rollover_group_control_number: pulumi.Input[_builtins.bool]
    rollover_interchange_control_number: pulumi.Input[_builtins.bool]
    rollover_transaction_set_control_number: pulumi.Input[_builtins.bool]
    transaction_set_control_number_lower_bound: pulumi.Input[_builtins.float]
    transaction_set_control_number_upper_bound: pulumi.Input[_builtins.float]
    application_reference_id: NotRequired[pulumi.Input[_builtins.str]]
    communication_agreement_id: NotRequired[pulumi.Input[_builtins.str]]
    functional_group_id: NotRequired[pulumi.Input[_builtins.str]]
    group_application_password: NotRequired[pulumi.Input[_builtins.str]]
    group_application_receiver_id: NotRequired[pulumi.Input[_builtins.str]]
    group_application_receiver_qualifier: NotRequired[pulumi.Input[_builtins.str]]
    group_application_sender_id: NotRequired[pulumi.Input[_builtins.str]]
    group_application_sender_qualifier: NotRequired[pulumi.Input[_builtins.str]]
    group_association_assigned_code: NotRequired[pulumi.Input[_builtins.str]]
    group_control_number_prefix: NotRequired[pulumi.Input[_builtins.str]]
    group_control_number_suffix: NotRequired[pulumi.Input[_builtins.str]]
    group_controlling_agency_code: NotRequired[pulumi.Input[_builtins.str]]
    group_message_release: NotRequired[pulumi.Input[_builtins.str]]
    group_message_version: NotRequired[pulumi.Input[_builtins.str]]
    interchange_control_number_prefix: NotRequired[pulumi.Input[_builtins.str]]
    interchange_control_number_suffix: NotRequired[pulumi.Input[_builtins.str]]
    processing_priority_code: NotRequired[pulumi.Input[_builtins.str]]
    receiver_internal_identification: NotRequired[pulumi.Input[_builtins.str]]
    receiver_internal_sub_identification: NotRequired[pulumi.Input[_builtins.str]]
    receiver_reverse_routing_address: NotRequired[pulumi.Input[_builtins.str]]
    recipient_reference_password_qualifier: NotRequired[pulumi.Input[_builtins.str]]
    recipient_reference_password_value: NotRequired[pulumi.Input[_builtins.str]]
    sender_internal_identification: NotRequired[pulumi.Input[_builtins.str]]
    sender_internal_sub_identification: NotRequired[pulumi.Input[_builtins.str]]
    sender_reverse_routing_address: NotRequired[pulumi.Input[_builtins.str]]
    transaction_set_control_number_prefix: NotRequired[pulumi.Input[_builtins.str]]
    transaction_set_control_number_suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EdifactEnvelopeSettingsArgs:
    def __init__(__self__, *, apply_delimiter_string_advice: pulumi.Input[_builtins.bool], create_grouping_segments: pulumi.Input[_builtins.bool], enable_default_group_headers: pulumi.Input[_builtins.bool], group_control_number_lower_bound: pulumi.Input[_builtins.float], group_control_number_upper_bound: pulumi.Input[_builtins.float], interchange_control_number_lower_bound: pulumi.Input[_builtins.float], interchange_control_number_upper_bound: pulumi.Input[_builtins.float], is_test_interchange: pulumi.Input[_builtins.bool], overwrite_existing_transaction_set_control_number: pulumi.Input[_builtins.bool], rollover_group_control_number: pulumi.Input[_builtins.bool], rollover_interchange_control_number: pulumi.Input[_builtins.bool], rollover_transaction_set_control_number: pulumi.Input[_builtins.bool], transaction_set_control_number_lower_bound: pulumi.Input[_builtins.float], transaction_set_control_number_upper_bound: pulumi.Input[_builtins.float], application_reference_id: Optional[pulumi.Input[_builtins.str]] = ..., communication_agreement_id: Optional[pulumi.Input[_builtins.str]] = ..., functional_group_id: Optional[pulumi.Input[_builtins.str]] = ..., group_application_password: Optional[pulumi.Input[_builtins.str]] = ..., group_application_receiver_id: Optional[pulumi.Input[_builtins.str]] = ..., group_application_receiver_qualifier: Optional[pulumi.Input[_builtins.str]] = ..., group_application_sender_id: Optional[pulumi.Input[_builtins.str]] = ..., group_application_sender_qualifier: Optional[pulumi.Input[_builtins.str]] = ..., group_association_assigned_code: Optional[pulumi.Input[_builtins.str]] = ..., group_control_number_prefix: Optional[pulumi.Input[_builtins.str]] = ..., group_control_number_suffix: Optional[pulumi.Input[_builtins.str]] = ..., group_controlling_agency_code: Optional[pulumi.Input[_builtins.str]] = ..., group_message_release: Optional[pulumi.Input[_builtins.str]] = ..., group_message_version: Optional[pulumi.Input[_builtins.str]] = ..., interchange_control_number_prefix: Optional[pulumi.Input[_builtins.str]] = ..., interchange_control_number_suffix: Optional[pulumi.Input[_builtins.str]] = ..., processing_priority_code: Optional[pulumi.Input[_builtins.str]] = ..., receiver_internal_identification: Optional[pulumi.Input[_builtins.str]] = ..., receiver_internal_sub_identification: Optional[pulumi.Input[_builtins.str]] = ..., receiver_reverse_routing_address: Optional[pulumi.Input[_builtins.str]] = ..., recipient_reference_password_qualifier: Optional[pulumi.Input[_builtins.str]] = ..., recipient_reference_password_value: Optional[pulumi.Input[_builtins.str]] = ..., sender_internal_identification: Optional[pulumi.Input[_builtins.str]] = ..., sender_internal_sub_identification: Optional[pulumi.Input[_builtins.str]] = ..., sender_reverse_routing_address: Optional[pulumi.Input[_builtins.str]] = ..., transaction_set_control_number_prefix: Optional[pulumi.Input[_builtins.str]] = ..., transaction_set_control_number_suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="applyDelimiterStringAdvice")
    def apply_delimiter_string_advice(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @apply_delimiter_string_advice.setter
    def apply_delimiter_string_advice(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createGroupingSegments")
    def create_grouping_segments(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @create_grouping_segments.setter
    def create_grouping_segments(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultGroupHeaders")
    def enable_default_group_headers(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_default_group_headers.setter
    def enable_default_group_headers(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupControlNumberLowerBound")
    def group_control_number_lower_bound(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @group_control_number_lower_bound.setter
    def group_control_number_lower_bound(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupControlNumberUpperBound")
    def group_control_number_upper_bound(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @group_control_number_upper_bound.setter
    def group_control_number_upper_bound(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interchangeControlNumberLowerBound")
    def interchange_control_number_lower_bound(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @interchange_control_number_lower_bound.setter
    def interchange_control_number_lower_bound(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interchangeControlNumberUpperBound")
    def interchange_control_number_upper_bound(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @interchange_control_number_upper_bound.setter
    def interchange_control_number_upper_bound(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isTestInterchange")
    def is_test_interchange(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @is_test_interchange.setter
    def is_test_interchange(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteExistingTransactionSetControlNumber")
    def overwrite_existing_transaction_set_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @overwrite_existing_transaction_set_control_number.setter
    def overwrite_existing_transaction_set_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloverGroupControlNumber")
    def rollover_group_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @rollover_group_control_number.setter
    def rollover_group_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloverInterchangeControlNumber")
    def rollover_interchange_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @rollover_interchange_control_number.setter
    def rollover_interchange_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloverTransactionSetControlNumber")
    def rollover_transaction_set_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @rollover_transaction_set_control_number.setter
    def rollover_transaction_set_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionSetControlNumberLowerBound")
    def transaction_set_control_number_lower_bound(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @transaction_set_control_number_lower_bound.setter
    def transaction_set_control_number_lower_bound(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionSetControlNumberUpperBound")
    def transaction_set_control_number_upper_bound(self) -> pulumi.Input[_builtins.float]:
        
        ...
    
    @transaction_set_control_number_upper_bound.setter
    def transaction_set_control_number_upper_bound(self, value: pulumi.Input[_builtins.float]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="applicationReferenceId")
    def application_reference_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @application_reference_id.setter
    def application_reference_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="communicationAgreementId")
    def communication_agreement_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @communication_agreement_id.setter
    def communication_agreement_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionalGroupId")
    def functional_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @functional_group_id.setter
    def functional_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupApplicationPassword")
    def group_application_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_application_password.setter
    def group_application_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupApplicationReceiverId")
    def group_application_receiver_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_application_receiver_id.setter
    def group_application_receiver_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupApplicationReceiverQualifier")
    def group_application_receiver_qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_application_receiver_qualifier.setter
    def group_application_receiver_qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupApplicationSenderId")
    def group_application_sender_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_application_sender_id.setter
    def group_application_sender_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupApplicationSenderQualifier")
    def group_application_sender_qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_application_sender_qualifier.setter
    def group_application_sender_qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupAssociationAssignedCode")
    def group_association_assigned_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_association_assigned_code.setter
    def group_association_assigned_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupControlNumberPrefix")
    def group_control_number_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_control_number_prefix.setter
    def group_control_number_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupControlNumberSuffix")
    def group_control_number_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_control_number_suffix.setter
    def group_control_number_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupControllingAgencyCode")
    def group_controlling_agency_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_controlling_agency_code.setter
    def group_controlling_agency_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupMessageRelease")
    def group_message_release(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_message_release.setter
    def group_message_release(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupMessageVersion")
    def group_message_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @group_message_version.setter
    def group_message_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interchangeControlNumberPrefix")
    def interchange_control_number_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interchange_control_number_prefix.setter
    def interchange_control_number_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interchangeControlNumberSuffix")
    def interchange_control_number_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interchange_control_number_suffix.setter
    def interchange_control_number_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingPriorityCode")
    def processing_priority_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @processing_priority_code.setter
    def processing_priority_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverInternalIdentification")
    def receiver_internal_identification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @receiver_internal_identification.setter
    def receiver_internal_identification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverInternalSubIdentification")
    def receiver_internal_sub_identification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @receiver_internal_sub_identification.setter
    def receiver_internal_sub_identification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverReverseRoutingAddress")
    def receiver_reverse_routing_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @receiver_reverse_routing_address.setter
    def receiver_reverse_routing_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recipientReferencePasswordQualifier")
    def recipient_reference_password_qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recipient_reference_password_qualifier.setter
    def recipient_reference_password_qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recipientReferencePasswordValue")
    def recipient_reference_password_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @recipient_reference_password_value.setter
    def recipient_reference_password_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderInternalIdentification")
    def sender_internal_identification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sender_internal_identification.setter
    def sender_internal_identification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderInternalSubIdentification")
    def sender_internal_sub_identification(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sender_internal_sub_identification.setter
    def sender_internal_sub_identification(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderReverseRoutingAddress")
    def sender_reverse_routing_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sender_reverse_routing_address.setter
    def sender_reverse_routing_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionSetControlNumberPrefix")
    def transaction_set_control_number_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transaction_set_control_number_prefix.setter
    def transaction_set_control_number_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionSetControlNumberSuffix")
    def transaction_set_control_number_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transaction_set_control_number_suffix.setter
    def transaction_set_control_number_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EdifactFramingSettingsArgsDict(TypedDict):
    
    character_set: pulumi.Input[Union[_builtins.str, EdifactCharacterSet]]
    component_separator: pulumi.Input[_builtins.int]
    data_element_separator: pulumi.Input[_builtins.int]
    decimal_point_indicator: pulumi.Input[EdifactDecimalIndicator]
    protocol_version: pulumi.Input[_builtins.int]
    release_indicator: pulumi.Input[_builtins.int]
    repetition_separator: pulumi.Input[_builtins.int]
    segment_terminator: pulumi.Input[_builtins.int]
    segment_terminator_suffix: pulumi.Input[SegmentTerminatorSuffix]
    character_encoding: NotRequired[pulumi.Input[_builtins.str]]
    service_code_list_directory_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EdifactFramingSettingsArgs:
    def __init__(__self__, *, character_set: pulumi.Input[Union[_builtins.str, EdifactCharacterSet]], component_separator: pulumi.Input[_builtins.int], data_element_separator: pulumi.Input[_builtins.int], decimal_point_indicator: pulumi.Input[EdifactDecimalIndicator], protocol_version: pulumi.Input[_builtins.int], release_indicator: pulumi.Input[_builtins.int], repetition_separator: pulumi.Input[_builtins.int], segment_terminator: pulumi.Input[_builtins.int], segment_terminator_suffix: pulumi.Input[SegmentTerminatorSuffix], character_encoding: Optional[pulumi.Input[_builtins.str]] = ..., service_code_list_directory_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="characterSet")
    def character_set(self) -> pulumi.Input[Union[_builtins.str, EdifactCharacterSet]]:
        
        ...
    
    @character_set.setter
    def character_set(self, value: pulumi.Input[Union[_builtins.str, EdifactCharacterSet]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentSeparator")
    def component_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @component_separator.setter
    def component_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataElementSeparator")
    def data_element_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @data_element_separator.setter
    def data_element_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="decimalPointIndicator")
    def decimal_point_indicator(self) -> pulumi.Input[EdifactDecimalIndicator]:
        
        ...
    
    @decimal_point_indicator.setter
    def decimal_point_indicator(self, value: pulumi.Input[EdifactDecimalIndicator]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @protocol_version.setter
    def protocol_version(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="releaseIndicator")
    def release_indicator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @release_indicator.setter
    def release_indicator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repetitionSeparator")
    def repetition_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @repetition_separator.setter
    def repetition_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentTerminator")
    def segment_terminator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @segment_terminator.setter
    def segment_terminator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentTerminatorSuffix")
    def segment_terminator_suffix(self) -> pulumi.Input[SegmentTerminatorSuffix]:
        
        ...
    
    @segment_terminator_suffix.setter
    def segment_terminator_suffix(self, value: pulumi.Input[SegmentTerminatorSuffix]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="characterEncoding")
    def character_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @character_encoding.setter
    def character_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceCodeListDirectoryVersion")
    def service_code_list_directory_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_code_list_directory_version.setter
    def service_code_list_directory_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EdifactMessageFilterArgsDict(TypedDict):
    
    message_filter_type: pulumi.Input[Union[_builtins.str, MessageFilterType]]


@pulumi.input_type
class EdifactMessageFilterArgs:
    def __init__(__self__, *, message_filter_type: pulumi.Input[Union[_builtins.str, MessageFilterType]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFilterType")
    def message_filter_type(self) -> pulumi.Input[Union[_builtins.str, MessageFilterType]]:
        
        ...
    
    @message_filter_type.setter
    def message_filter_type(self, value: pulumi.Input[Union[_builtins.str, MessageFilterType]]): # -> None:
        ...
    


class EdifactMessageIdentifierArgsDict(TypedDict):
    
    message_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class EdifactMessageIdentifierArgs:
    def __init__(__self__, *, message_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EdifactOneWayAgreementArgsDict(TypedDict):
    
    protocol_settings: pulumi.Input[EdifactProtocolSettingsArgsDict]
    receiver_business_identity: pulumi.Input[BusinessIdentityArgsDict]
    sender_business_identity: pulumi.Input[BusinessIdentityArgsDict]


@pulumi.input_type
class EdifactOneWayAgreementArgs:
    def __init__(__self__, *, protocol_settings: pulumi.Input[EdifactProtocolSettingsArgs], receiver_business_identity: pulumi.Input[BusinessIdentityArgs], sender_business_identity: pulumi.Input[BusinessIdentityArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolSettings")
    def protocol_settings(self) -> pulumi.Input[EdifactProtocolSettingsArgs]:
        
        ...
    
    @protocol_settings.setter
    def protocol_settings(self, value: pulumi.Input[EdifactProtocolSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverBusinessIdentity")
    def receiver_business_identity(self) -> pulumi.Input[BusinessIdentityArgs]:
        
        ...
    
    @receiver_business_identity.setter
    def receiver_business_identity(self, value: pulumi.Input[BusinessIdentityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderBusinessIdentity")
    def sender_business_identity(self) -> pulumi.Input[BusinessIdentityArgs]:
        
        ...
    
    @sender_business_identity.setter
    def sender_business_identity(self, value: pulumi.Input[BusinessIdentityArgs]): # -> None:
        ...
    


class EdifactProcessingSettingsArgsDict(TypedDict):
    
    create_empty_xml_tags_for_trailing_separators: pulumi.Input[_builtins.bool]
    mask_security_info: pulumi.Input[_builtins.bool]
    preserve_interchange: pulumi.Input[_builtins.bool]
    suspend_interchange_on_error: pulumi.Input[_builtins.bool]
    use_dot_as_decimal_separator: pulumi.Input[_builtins.bool]


@pulumi.input_type
class EdifactProcessingSettingsArgs:
    def __init__(__self__, *, create_empty_xml_tags_for_trailing_separators: pulumi.Input[_builtins.bool], mask_security_info: pulumi.Input[_builtins.bool], preserve_interchange: pulumi.Input[_builtins.bool], suspend_interchange_on_error: pulumi.Input[_builtins.bool], use_dot_as_decimal_separator: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createEmptyXmlTagsForTrailingSeparators")
    def create_empty_xml_tags_for_trailing_separators(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @create_empty_xml_tags_for_trailing_separators.setter
    def create_empty_xml_tags_for_trailing_separators(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maskSecurityInfo")
    def mask_security_info(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @mask_security_info.setter
    def mask_security_info(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveInterchange")
    def preserve_interchange(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @preserve_interchange.setter
    def preserve_interchange(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspendInterchangeOnError")
    def suspend_interchange_on_error(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @suspend_interchange_on_error.setter
    def suspend_interchange_on_error(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDotAsDecimalSeparator")
    def use_dot_as_decimal_separator(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @use_dot_as_decimal_separator.setter
    def use_dot_as_decimal_separator(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class EdifactProtocolSettingsArgsDict(TypedDict):
    
    acknowledgement_settings: pulumi.Input[EdifactAcknowledgementSettingsArgsDict]
    envelope_settings: pulumi.Input[EdifactEnvelopeSettingsArgsDict]
    framing_settings: pulumi.Input[EdifactFramingSettingsArgsDict]
    message_filter: pulumi.Input[EdifactMessageFilterArgsDict]
    processing_settings: pulumi.Input[EdifactProcessingSettingsArgsDict]
    schema_references: pulumi.Input[Sequence[pulumi.Input[EdifactSchemaReferenceArgsDict]]]
    validation_settings: pulumi.Input[EdifactValidationSettingsArgsDict]
    edifact_delimiter_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[EdifactDelimiterOverrideArgsDict]]]]
    envelope_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[EdifactEnvelopeOverrideArgsDict]]]]
    message_filter_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[EdifactMessageIdentifierArgsDict]]]]
    validation_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[EdifactValidationOverrideArgsDict]]]]


@pulumi.input_type
class EdifactProtocolSettingsArgs:
    def __init__(__self__, *, acknowledgement_settings: pulumi.Input[EdifactAcknowledgementSettingsArgs], envelope_settings: pulumi.Input[EdifactEnvelopeSettingsArgs], framing_settings: pulumi.Input[EdifactFramingSettingsArgs], message_filter: pulumi.Input[EdifactMessageFilterArgs], processing_settings: pulumi.Input[EdifactProcessingSettingsArgs], schema_references: pulumi.Input[Sequence[pulumi.Input[EdifactSchemaReferenceArgs]]], validation_settings: pulumi.Input[EdifactValidationSettingsArgs], edifact_delimiter_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[EdifactDelimiterOverrideArgs]]]] = ..., envelope_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[EdifactEnvelopeOverrideArgs]]]] = ..., message_filter_list: Optional[pulumi.Input[Sequence[pulumi.Input[EdifactMessageIdentifierArgs]]]] = ..., validation_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[EdifactValidationOverrideArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementSettings")
    def acknowledgement_settings(self) -> pulumi.Input[EdifactAcknowledgementSettingsArgs]:
        
        ...
    
    @acknowledgement_settings.setter
    def acknowledgement_settings(self, value: pulumi.Input[EdifactAcknowledgementSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envelopeSettings")
    def envelope_settings(self) -> pulumi.Input[EdifactEnvelopeSettingsArgs]:
        
        ...
    
    @envelope_settings.setter
    def envelope_settings(self, value: pulumi.Input[EdifactEnvelopeSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="framingSettings")
    def framing_settings(self) -> pulumi.Input[EdifactFramingSettingsArgs]:
        
        ...
    
    @framing_settings.setter
    def framing_settings(self, value: pulumi.Input[EdifactFramingSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFilter")
    def message_filter(self) -> pulumi.Input[EdifactMessageFilterArgs]:
        
        ...
    
    @message_filter.setter
    def message_filter(self, value: pulumi.Input[EdifactMessageFilterArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingSettings")
    def processing_settings(self) -> pulumi.Input[EdifactProcessingSettingsArgs]:
        
        ...
    
    @processing_settings.setter
    def processing_settings(self, value: pulumi.Input[EdifactProcessingSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaReferences")
    def schema_references(self) -> pulumi.Input[Sequence[pulumi.Input[EdifactSchemaReferenceArgs]]]:
        
        ...
    
    @schema_references.setter
    def schema_references(self, value: pulumi.Input[Sequence[pulumi.Input[EdifactSchemaReferenceArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationSettings")
    def validation_settings(self) -> pulumi.Input[EdifactValidationSettingsArgs]:
        
        ...
    
    @validation_settings.setter
    def validation_settings(self, value: pulumi.Input[EdifactValidationSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edifactDelimiterOverrides")
    def edifact_delimiter_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EdifactDelimiterOverrideArgs]]]]:
        
        ...
    
    @edifact_delimiter_overrides.setter
    def edifact_delimiter_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EdifactDelimiterOverrideArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envelopeOverrides")
    def envelope_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EdifactEnvelopeOverrideArgs]]]]:
        
        ...
    
    @envelope_overrides.setter
    def envelope_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EdifactEnvelopeOverrideArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFilterList")
    def message_filter_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EdifactMessageIdentifierArgs]]]]:
        
        ...
    
    @message_filter_list.setter
    def message_filter_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EdifactMessageIdentifierArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationOverrides")
    def validation_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[EdifactValidationOverrideArgs]]]]:
        
        ...
    
    @validation_overrides.setter
    def validation_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[EdifactValidationOverrideArgs]]]]): # -> None:
        ...
    


class EdifactSchemaReferenceArgsDict(TypedDict):
    
    message_id: pulumi.Input[_builtins.str]
    message_release: pulumi.Input[_builtins.str]
    message_version: pulumi.Input[_builtins.str]
    schema_name: pulumi.Input[_builtins.str]
    association_assigned_code: NotRequired[pulumi.Input[_builtins.str]]
    sender_application_id: NotRequired[pulumi.Input[_builtins.str]]
    sender_application_qualifier: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class EdifactSchemaReferenceArgs:
    def __init__(__self__, *, message_id: pulumi.Input[_builtins.str], message_release: pulumi.Input[_builtins.str], message_version: pulumi.Input[_builtins.str], schema_name: pulumi.Input[_builtins.str], association_assigned_code: Optional[pulumi.Input[_builtins.str]] = ..., sender_application_id: Optional[pulumi.Input[_builtins.str]] = ..., sender_application_qualifier: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageRelease")
    def message_release(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_release.setter
    def message_release(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageVersion")
    def message_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_version.setter
    def message_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schema_name.setter
    def schema_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="associationAssignedCode")
    def association_assigned_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @association_assigned_code.setter
    def association_assigned_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderApplicationId")
    def sender_application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sender_application_id.setter
    def sender_application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderApplicationQualifier")
    def sender_application_qualifier(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sender_application_qualifier.setter
    def sender_application_qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class EdifactValidationOverrideArgsDict(TypedDict):
    
    allow_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool]
    enforce_character_set: pulumi.Input[_builtins.bool]
    message_id: pulumi.Input[_builtins.str]
    trailing_separator_policy: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]
    trim_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool]
    validate_edi_types: pulumi.Input[_builtins.bool]
    validate_xsd_types: pulumi.Input[_builtins.bool]


@pulumi.input_type
class EdifactValidationOverrideArgs:
    def __init__(__self__, *, allow_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool], enforce_character_set: pulumi.Input[_builtins.bool], message_id: pulumi.Input[_builtins.str], trailing_separator_policy: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]], trim_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool], validate_edi_types: pulumi.Input[_builtins.bool], validate_xsd_types: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowLeadingAndTrailingSpacesAndZeroes")
    def allow_leading_and_trailing_spaces_and_zeroes(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @allow_leading_and_trailing_spaces_and_zeroes.setter
    def allow_leading_and_trailing_spaces_and_zeroes(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enforceCharacterSet")
    def enforce_character_set(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enforce_character_set.setter
    def enforce_character_set(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trailingSeparatorPolicy")
    def trailing_separator_policy(self) -> pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]:
        
        ...
    
    @trailing_separator_policy.setter
    def trailing_separator_policy(self, value: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trimLeadingAndTrailingSpacesAndZeroes")
    def trim_leading_and_trailing_spaces_and_zeroes(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @trim_leading_and_trailing_spaces_and_zeroes.setter
    def trim_leading_and_trailing_spaces_and_zeroes(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateEDITypes")
    def validate_edi_types(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_edi_types.setter
    def validate_edi_types(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateXSDTypes")
    def validate_xsd_types(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_xsd_types.setter
    def validate_xsd_types(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class EdifactValidationSettingsArgsDict(TypedDict):
    
    allow_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool]
    check_duplicate_group_control_number: pulumi.Input[_builtins.bool]
    check_duplicate_interchange_control_number: pulumi.Input[_builtins.bool]
    check_duplicate_transaction_set_control_number: pulumi.Input[_builtins.bool]
    interchange_control_number_validity_days: pulumi.Input[_builtins.int]
    trailing_separator_policy: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]
    trim_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool]
    validate_character_set: pulumi.Input[_builtins.bool]
    validate_edi_types: pulumi.Input[_builtins.bool]
    validate_xsd_types: pulumi.Input[_builtins.bool]


@pulumi.input_type
class EdifactValidationSettingsArgs:
    def __init__(__self__, *, allow_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool], check_duplicate_group_control_number: pulumi.Input[_builtins.bool], check_duplicate_interchange_control_number: pulumi.Input[_builtins.bool], check_duplicate_transaction_set_control_number: pulumi.Input[_builtins.bool], interchange_control_number_validity_days: pulumi.Input[_builtins.int], trailing_separator_policy: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]], trim_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool], validate_character_set: pulumi.Input[_builtins.bool], validate_edi_types: pulumi.Input[_builtins.bool], validate_xsd_types: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowLeadingAndTrailingSpacesAndZeroes")
    def allow_leading_and_trailing_spaces_and_zeroes(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @allow_leading_and_trailing_spaces_and_zeroes.setter
    def allow_leading_and_trailing_spaces_and_zeroes(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkDuplicateGroupControlNumber")
    def check_duplicate_group_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @check_duplicate_group_control_number.setter
    def check_duplicate_group_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkDuplicateInterchangeControlNumber")
    def check_duplicate_interchange_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @check_duplicate_interchange_control_number.setter
    def check_duplicate_interchange_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkDuplicateTransactionSetControlNumber")
    def check_duplicate_transaction_set_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @check_duplicate_transaction_set_control_number.setter
    def check_duplicate_transaction_set_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interchangeControlNumberValidityDays")
    def interchange_control_number_validity_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @interchange_control_number_validity_days.setter
    def interchange_control_number_validity_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trailingSeparatorPolicy")
    def trailing_separator_policy(self) -> pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]:
        
        ...
    
    @trailing_separator_policy.setter
    def trailing_separator_policy(self, value: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trimLeadingAndTrailingSpacesAndZeroes")
    def trim_leading_and_trailing_spaces_and_zeroes(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @trim_leading_and_trailing_spaces_and_zeroes.setter
    def trim_leading_and_trailing_spaces_and_zeroes(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateCharacterSet")
    def validate_character_set(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_character_set.setter
    def validate_character_set(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateEDITypes")
    def validate_edi_types(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_edi_types.setter
    def validate_edi_types(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateXSDTypes")
    def validate_xsd_types(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_xsd_types.setter
    def validate_xsd_types(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class FlowAccessControlConfigurationPolicyArgsDict(TypedDict):
    
    allowed_caller_ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpAddressRangeArgsDict]]]]
    open_authentication_policies: NotRequired[pulumi.Input[OpenAuthenticationAccessPoliciesArgsDict]]


@pulumi.input_type
class FlowAccessControlConfigurationPolicyArgs:
    def __init__(__self__, *, allowed_caller_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressRangeArgs]]]] = ..., open_authentication_policies: Optional[pulumi.Input[OpenAuthenticationAccessPoliciesArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedCallerIpAddresses")
    def allowed_caller_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressRangeArgs]]]]:
        
        ...
    
    @allowed_caller_ip_addresses.setter
    def allowed_caller_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressRangeArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openAuthenticationPolicies")
    def open_authentication_policies(self) -> Optional[pulumi.Input[OpenAuthenticationAccessPoliciesArgs]]:
        
        ...
    
    @open_authentication_policies.setter
    def open_authentication_policies(self, value: Optional[pulumi.Input[OpenAuthenticationAccessPoliciesArgs]]): # -> None:
        ...
    


class FlowAccessControlConfigurationArgsDict(TypedDict):
    
    actions: NotRequired[pulumi.Input[FlowAccessControlConfigurationPolicyArgsDict]]
    contents: NotRequired[pulumi.Input[FlowAccessControlConfigurationPolicyArgsDict]]
    triggers: NotRequired[pulumi.Input[FlowAccessControlConfigurationPolicyArgsDict]]
    workflow_management: NotRequired[pulumi.Input[FlowAccessControlConfigurationPolicyArgsDict]]


@pulumi.input_type
class FlowAccessControlConfigurationArgs:
    def __init__(__self__, *, actions: Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]] = ..., contents: Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]] = ..., triggers: Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]] = ..., workflow_management: Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]]:
        
        ...
    
    @actions.setter
    def actions(self, value: Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def contents(self) -> Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]]:
        
        ...
    
    @contents.setter
    def contents(self, value: Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]]:
        
        ...
    
    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowManagement")
    def workflow_management(self) -> Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]]:
        
        ...
    
    @workflow_management.setter
    def workflow_management(self, value: Optional[pulumi.Input[FlowAccessControlConfigurationPolicyArgs]]): # -> None:
        ...
    


class FlowEndpointsConfigurationArgsDict(TypedDict):
    
    connector: NotRequired[pulumi.Input[FlowEndpointsArgsDict]]
    workflow: NotRequired[pulumi.Input[FlowEndpointsArgsDict]]


@pulumi.input_type
class FlowEndpointsConfigurationArgs:
    def __init__(__self__, *, connector: Optional[pulumi.Input[FlowEndpointsArgs]] = ..., workflow: Optional[pulumi.Input[FlowEndpointsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def connector(self) -> Optional[pulumi.Input[FlowEndpointsArgs]]:
        
        ...
    
    @connector.setter
    def connector(self, value: Optional[pulumi.Input[FlowEndpointsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def workflow(self) -> Optional[pulumi.Input[FlowEndpointsArgs]]:
        
        ...
    
    @workflow.setter
    def workflow(self, value: Optional[pulumi.Input[FlowEndpointsArgs]]): # -> None:
        ...
    


class FlowEndpointsArgsDict(TypedDict):
    
    access_endpoint_ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpAddressArgsDict]]]]
    outgoing_ip_addresses: NotRequired[pulumi.Input[Sequence[pulumi.Input[IpAddressArgsDict]]]]


@pulumi.input_type
class FlowEndpointsArgs:
    def __init__(__self__, *, access_endpoint_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressArgs]]]] = ..., outgoing_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpointIpAddresses")
    def access_endpoint_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressArgs]]]]:
        
        ...
    
    @access_endpoint_ip_addresses.setter
    def access_endpoint_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outgoingIpAddresses")
    def outgoing_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressArgs]]]]:
        
        ...
    
    @outgoing_ip_addresses.setter
    def outgoing_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[IpAddressArgs]]]]): # -> None:
        ...
    


class IntegrationAccountMapPropertiesParametersSchemaArgsDict(TypedDict):
    
    ref: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IntegrationAccountMapPropertiesParametersSchemaArgs:
    def __init__(__self__, *, ref: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ref.setter
    def ref(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IntegrationAccountSkuArgsDict(TypedDict):
    
    name: pulumi.Input[Union[_builtins.str, IntegrationAccountSkuName]]


@pulumi.input_type
class IntegrationAccountSkuArgs:
    def __init__(__self__, *, name: pulumi.Input[Union[_builtins.str, IntegrationAccountSkuName]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, IntegrationAccountSkuName]]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, IntegrationAccountSkuName]]): # -> None:
        ...
    


class IntegrationServiceEnvironmenEncryptionConfigurationArgsDict(TypedDict):
    
    encryption_key_reference: NotRequired[pulumi.Input[IntegrationServiceEnvironmenEncryptionKeyReferenceArgsDict]]


@pulumi.input_type
class IntegrationServiceEnvironmenEncryptionConfigurationArgs:
    def __init__(__self__, *, encryption_key_reference: Optional[pulumi.Input[IntegrationServiceEnvironmenEncryptionKeyReferenceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionKeyReference")
    def encryption_key_reference(self) -> Optional[pulumi.Input[IntegrationServiceEnvironmenEncryptionKeyReferenceArgs]]:
        
        ...
    
    @encryption_key_reference.setter
    def encryption_key_reference(self, value: Optional[pulumi.Input[IntegrationServiceEnvironmenEncryptionKeyReferenceArgs]]): # -> None:
        ...
    


class IntegrationServiceEnvironmenEncryptionKeyReferenceArgsDict(TypedDict):
    
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    key_vault: NotRequired[pulumi.Input[ResourceReferenceArgsDict]]
    key_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IntegrationServiceEnvironmenEncryptionKeyReferenceArgs:
    def __init__(__self__, *, key_name: Optional[pulumi.Input[_builtins.str]] = ..., key_vault: Optional[pulumi.Input[ResourceReferenceArgs]] = ..., key_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[pulumi.Input[ResourceReferenceArgs]]:
        
        ...
    
    @key_vault.setter
    def key_vault(self, value: Optional[pulumi.Input[ResourceReferenceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IntegrationServiceEnvironmentAccessEndpointArgsDict(TypedDict):
    
    type: NotRequired[pulumi.Input[Union[_builtins.str, IntegrationServiceEnvironmentAccessEndpointType]]]


@pulumi.input_type
class IntegrationServiceEnvironmentAccessEndpointArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[Union[_builtins.str, IntegrationServiceEnvironmentAccessEndpointType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, IntegrationServiceEnvironmentAccessEndpointType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, IntegrationServiceEnvironmentAccessEndpointType]]]): # -> None:
        ...
    


class IntegrationServiceEnvironmentManagedApiDeploymentParametersArgsDict(TypedDict):
    
    content_link_definition: NotRequired[pulumi.Input[ContentLinkArgsDict]]


@pulumi.input_type
class IntegrationServiceEnvironmentManagedApiDeploymentParametersArgs:
    def __init__(__self__, *, content_link_definition: Optional[pulumi.Input[ContentLinkArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentLinkDefinition")
    def content_link_definition(self) -> Optional[pulumi.Input[ContentLinkArgs]]:
        
        ...
    
    @content_link_definition.setter
    def content_link_definition(self, value: Optional[pulumi.Input[ContentLinkArgs]]): # -> None:
        ...
    


class IntegrationServiceEnvironmentPropertiesArgsDict(TypedDict):
    
    encryption_configuration: NotRequired[pulumi.Input[IntegrationServiceEnvironmenEncryptionConfigurationArgsDict]]
    endpoints_configuration: NotRequired[pulumi.Input[FlowEndpointsConfigurationArgsDict]]
    integration_service_environment_id: NotRequired[pulumi.Input[_builtins.str]]
    network_configuration: NotRequired[pulumi.Input[NetworkConfigurationArgsDict]]
    provisioning_state: NotRequired[pulumi.Input[Union[_builtins.str, WorkflowProvisioningState]]]
    state: NotRequired[pulumi.Input[Union[_builtins.str, WorkflowState]]]


@pulumi.input_type
class IntegrationServiceEnvironmentPropertiesArgs:
    def __init__(__self__, *, encryption_configuration: Optional[pulumi.Input[IntegrationServiceEnvironmenEncryptionConfigurationArgs]] = ..., endpoints_configuration: Optional[pulumi.Input[FlowEndpointsConfigurationArgs]] = ..., integration_service_environment_id: Optional[pulumi.Input[_builtins.str]] = ..., network_configuration: Optional[pulumi.Input[NetworkConfigurationArgs]] = ..., provisioning_state: Optional[pulumi.Input[Union[_builtins.str, WorkflowProvisioningState]]] = ..., state: Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input[IntegrationServiceEnvironmenEncryptionConfigurationArgs]]:
        
        ...
    
    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input[IntegrationServiceEnvironmenEncryptionConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointsConfiguration")
    def endpoints_configuration(self) -> Optional[pulumi.Input[FlowEndpointsConfigurationArgs]]:
        
        ...
    
    @endpoints_configuration.setter
    def endpoints_configuration(self, value: Optional[pulumi.Input[FlowEndpointsConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationServiceEnvironmentId")
    def integration_service_environment_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @integration_service_environment_id.setter
    def integration_service_environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(self) -> Optional[pulumi.Input[NetworkConfigurationArgs]]:
        
        ...
    
    @network_configuration.setter
    def network_configuration(self, value: Optional[pulumi.Input[NetworkConfigurationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[_builtins.str, WorkflowProvisioningState]]]:
        
        ...
    
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[_builtins.str, WorkflowProvisioningState]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]]:
        
        ...
    
    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[_builtins.str, WorkflowState]]]): # -> None:
        ...
    


class IntegrationServiceEnvironmentSkuArgsDict(TypedDict):
    
    capacity: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[Union[_builtins.str, IntegrationServiceEnvironmentSkuName]]]


@pulumi.input_type
class IntegrationServiceEnvironmentSkuArgs:
    def __init__(__self__, *, capacity: Optional[pulumi.Input[_builtins.int]] = ..., name: Optional[pulumi.Input[Union[_builtins.str, IntegrationServiceEnvironmentSkuName]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[_builtins.str, IntegrationServiceEnvironmentSkuName]]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[_builtins.str, IntegrationServiceEnvironmentSkuName]]]): # -> None:
        ...
    


class IpAddressRangeArgsDict(TypedDict):
    
    address_range: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IpAddressRangeArgs:
    def __init__(__self__, *, address_range: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="addressRange")
    def address_range(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address_range.setter
    def address_range(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IpAddressArgsDict(TypedDict):
    
    address: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IpAddressArgs:
    def __init__(__self__, *, address: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @address.setter
    def address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeyVaultKeyReferenceKeyVaultArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyVaultKeyReferenceKeyVaultArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeyVaultKeyReferenceArgsDict(TypedDict):
    
    key_name: pulumi.Input[_builtins.str]
    key_vault: pulumi.Input[KeyVaultKeyReferenceKeyVaultArgsDict]
    key_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class KeyVaultKeyReferenceArgs:
    def __init__(__self__, *, key_name: pulumi.Input[_builtins.str], key_vault: pulumi.Input[KeyVaultKeyReferenceKeyVaultArgs], key_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> pulumi.Input[KeyVaultKeyReferenceKeyVaultArgs]:
        
        ...
    
    @key_vault.setter
    def key_vault(self, value: pulumi.Input[KeyVaultKeyReferenceKeyVaultArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class KeyVaultReferenceDict(TypedDict):
    
    id: NotRequired[_builtins.str]
    name: NotRequired[_builtins.str]


@pulumi.input_type
class KeyVaultReference:
    def __init__(__self__, *, id: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[_builtins.str]): # -> None:
        ...
    


class ManagedServiceIdentityArgsDict(TypedDict):
    
    type: pulumi.Input[Union[_builtins.str, ManagedServiceIdentityType]]
    user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ManagedServiceIdentityArgs:
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
    


class NetworkConfigurationArgsDict(TypedDict):
    
    access_endpoint: NotRequired[pulumi.Input[IntegrationServiceEnvironmentAccessEndpointArgsDict]]
    subnets: NotRequired[pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgsDict]]]]
    virtual_network_address_space: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class NetworkConfigurationArgs:
    def __init__(__self__, *, access_endpoint: Optional[pulumi.Input[IntegrationServiceEnvironmentAccessEndpointArgs]] = ..., subnets: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]] = ..., virtual_network_address_space: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessEndpoint")
    def access_endpoint(self) -> Optional[pulumi.Input[IntegrationServiceEnvironmentAccessEndpointArgs]]:
        
        ...
    
    @access_endpoint.setter
    def access_endpoint(self, value: Optional[pulumi.Input[IntegrationServiceEnvironmentAccessEndpointArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]]:
        
        ...
    
    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ResourceReferenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualNetworkAddressSpace")
    def virtual_network_address_space(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @virtual_network_address_space.setter
    def virtual_network_address_space(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class OpenAuthenticationAccessPoliciesArgsDict(TypedDict):
    
    policies: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[OpenAuthenticationAccessPolicyArgsDict]]]]


@pulumi.input_type
class OpenAuthenticationAccessPoliciesArgs:
    def __init__(__self__, *, policies: Optional[pulumi.Input[Mapping[str, pulumi.Input[OpenAuthenticationAccessPolicyArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[OpenAuthenticationAccessPolicyArgs]]]]:
        
        ...
    
    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[OpenAuthenticationAccessPolicyArgs]]]]): # -> None:
        ...
    


class OpenAuthenticationAccessPolicyArgsDict(TypedDict):
    
    claims: NotRequired[pulumi.Input[Sequence[pulumi.Input[OpenAuthenticationPolicyClaimArgsDict]]]]
    type: NotRequired[pulumi.Input[Union[_builtins.str, OpenAuthenticationProviderType]]]


@pulumi.input_type
class OpenAuthenticationAccessPolicyArgs:
    def __init__(__self__, *, claims: Optional[pulumi.Input[Sequence[pulumi.Input[OpenAuthenticationPolicyClaimArgs]]]] = ..., type: Optional[pulumi.Input[Union[_builtins.str, OpenAuthenticationProviderType]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def claims(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[OpenAuthenticationPolicyClaimArgs]]]]:
        
        ...
    
    @claims.setter
    def claims(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[OpenAuthenticationPolicyClaimArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, OpenAuthenticationProviderType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, OpenAuthenticationProviderType]]]): # -> None:
        ...
    


class OpenAuthenticationPolicyClaimArgsDict(TypedDict):
    
    name: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class OpenAuthenticationPolicyClaimArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
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
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class PartnerContentArgsDict(TypedDict):
    
    b2b: NotRequired[pulumi.Input[B2BPartnerContentArgsDict]]


@pulumi.input_type
class PartnerContentArgs:
    def __init__(__self__, *, b2b: Optional[pulumi.Input[B2BPartnerContentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def b2b(self) -> Optional[pulumi.Input[B2BPartnerContentArgs]]:
        
        ...
    
    @b2b.setter
    def b2b(self, value: Optional[pulumi.Input[B2BPartnerContentArgs]]): # -> None:
        ...
    


class RecurrenceScheduleOccurrenceArgsDict(TypedDict):
    
    day: NotRequired[pulumi.Input[DayOfWeek]]
    occurrence: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class RecurrenceScheduleOccurrenceArgs:
    def __init__(__self__, *, day: Optional[pulumi.Input[DayOfWeek]] = ..., occurrence: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[DayOfWeek]]:
        
        ...
    
    @day.setter
    def day(self, value: Optional[pulumi.Input[DayOfWeek]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def occurrence(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @occurrence.setter
    def occurrence(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class RecurrenceScheduleArgsDict(TypedDict):
    
    hours: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    minutes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    month_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]
    monthly_occurrences: NotRequired[pulumi.Input[Sequence[pulumi.Input[RecurrenceScheduleOccurrenceArgsDict]]]]
    week_days: NotRequired[pulumi.Input[Sequence[pulumi.Input[DaysOfWeek]]]]


@pulumi.input_type
class RecurrenceScheduleArgs:
    def __init__(__self__, *, hours: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., minutes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., month_days: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]] = ..., monthly_occurrences: Optional[pulumi.Input[Sequence[pulumi.Input[RecurrenceScheduleOccurrenceArgs]]]] = ..., week_days: Optional[pulumi.Input[Sequence[pulumi.Input[DaysOfWeek]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hours(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @hours.setter
    def hours(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def minutes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @minutes.setter
    def minutes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthDays")
    def month_days(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]:
        
        ...
    
    @month_days.setter
    def month_days(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monthlyOccurrences")
    def monthly_occurrences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RecurrenceScheduleOccurrenceArgs]]]]:
        
        ...
    
    @monthly_occurrences.setter
    def monthly_occurrences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RecurrenceScheduleOccurrenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="weekDays")
    def week_days(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[DaysOfWeek]]]]:
        
        ...
    
    @week_days.setter
    def week_days(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DaysOfWeek]]]]): # -> None:
        ...
    


class ResourceReferenceArgsDict(TypedDict):
    
    id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ResourceReferenceArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RosettaNetPipAcknowledgmentOfReceiptSettingsArgsDict(TypedDict):
    
    is_non_repudiation_required: pulumi.Input[_builtins.bool]
    time_to_acknowledge_in_seconds: pulumi.Input[_builtins.int]


@pulumi.input_type
class RosettaNetPipAcknowledgmentOfReceiptSettingsArgs:
    def __init__(__self__, *, is_non_repudiation_required: pulumi.Input[_builtins.bool], time_to_acknowledge_in_seconds: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="isNonRepudiationRequired")
    def is_non_repudiation_required(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @is_non_repudiation_required.setter
    def is_non_repudiation_required(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToAcknowledgeInSeconds")
    def time_to_acknowledge_in_seconds(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @time_to_acknowledge_in_seconds.setter
    def time_to_acknowledge_in_seconds(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class RosettaNetPipActivityBehaviorArgsDict(TypedDict):
    
    action_type: pulumi.Input[RosettaNetActionType]
    is_authorization_required: pulumi.Input[_builtins.bool]
    is_secured_transport_required: pulumi.Input[_builtins.bool]
    non_repudiation_of_origin_and_content: pulumi.Input[_builtins.bool]
    persistent_confidentiality_scope: pulumi.Input[RosettaNetPipConfidentialityScope]
    response_type: pulumi.Input[RosettaNetResponseType]
    retry_count: pulumi.Input[_builtins.int]
    time_to_perform_in_seconds: pulumi.Input[_builtins.int]


@pulumi.input_type
class RosettaNetPipActivityBehaviorArgs:
    def __init__(__self__, *, action_type: pulumi.Input[RosettaNetActionType], is_authorization_required: pulumi.Input[_builtins.bool], is_secured_transport_required: pulumi.Input[_builtins.bool], non_repudiation_of_origin_and_content: pulumi.Input[_builtins.bool], persistent_confidentiality_scope: pulumi.Input[RosettaNetPipConfidentialityScope], response_type: pulumi.Input[RosettaNetResponseType], retry_count: pulumi.Input[_builtins.int], time_to_perform_in_seconds: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionType")
    def action_type(self) -> pulumi.Input[RosettaNetActionType]:
        
        ...
    
    @action_type.setter
    def action_type(self, value: pulumi.Input[RosettaNetActionType]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isAuthorizationRequired")
    def is_authorization_required(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @is_authorization_required.setter
    def is_authorization_required(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isSecuredTransportRequired")
    def is_secured_transport_required(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @is_secured_transport_required.setter
    def is_secured_transport_required(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nonRepudiationOfOriginAndContent")
    def non_repudiation_of_origin_and_content(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @non_repudiation_of_origin_and_content.setter
    def non_repudiation_of_origin_and_content(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="persistentConfidentialityScope")
    def persistent_confidentiality_scope(self) -> pulumi.Input[RosettaNetPipConfidentialityScope]:
        
        ...
    
    @persistent_confidentiality_scope.setter
    def persistent_confidentiality_scope(self, value: pulumi.Input[RosettaNetPipConfidentialityScope]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responseType")
    def response_type(self) -> pulumi.Input[RosettaNetResponseType]:
        
        ...
    
    @response_type.setter
    def response_type(self, value: pulumi.Input[RosettaNetResponseType]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="retryCount")
    def retry_count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @retry_count.setter
    def retry_count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeToPerformInSeconds")
    def time_to_perform_in_seconds(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @time_to_perform_in_seconds.setter
    def time_to_perform_in_seconds(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class RosettaNetPipActivitySettingsArgsDict(TypedDict):
    
    acknowledgment_of_receipt_settings: pulumi.Input[RosettaNetPipAcknowledgmentOfReceiptSettingsArgsDict]
    activity_behavior: pulumi.Input[RosettaNetPipActivityBehaviorArgsDict]
    activity_type: pulumi.Input[RosettaNetPipActivityType]


@pulumi.input_type
class RosettaNetPipActivitySettingsArgs:
    def __init__(__self__, *, acknowledgment_of_receipt_settings: pulumi.Input[RosettaNetPipAcknowledgmentOfReceiptSettingsArgs], activity_behavior: pulumi.Input[RosettaNetPipActivityBehaviorArgs], activity_type: pulumi.Input[RosettaNetPipActivityType]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgmentOfReceiptSettings")
    def acknowledgment_of_receipt_settings(self) -> pulumi.Input[RosettaNetPipAcknowledgmentOfReceiptSettingsArgs]:
        
        ...
    
    @acknowledgment_of_receipt_settings.setter
    def acknowledgment_of_receipt_settings(self, value: pulumi.Input[RosettaNetPipAcknowledgmentOfReceiptSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activityBehavior")
    def activity_behavior(self) -> pulumi.Input[RosettaNetPipActivityBehaviorArgs]:
        
        ...
    
    @activity_behavior.setter
    def activity_behavior(self, value: pulumi.Input[RosettaNetPipActivityBehaviorArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activityType")
    def activity_type(self) -> pulumi.Input[RosettaNetPipActivityType]:
        
        ...
    
    @activity_type.setter
    def activity_type(self, value: pulumi.Input[RosettaNetPipActivityType]): # -> None:
        ...
    


class RosettaNetPipBusinessDocumentArgsDict(TypedDict):
    
    name: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RosettaNetPipBusinessDocumentArgs:
    def __init__(__self__, *, name: pulumi.Input[_builtins.str], version: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class RosettaNetPipRoleSettingsArgsDict(TypedDict):
    
    action: pulumi.Input[_builtins.str]
    business_document: pulumi.Input[RosettaNetPipBusinessDocumentArgsDict]
    role: pulumi.Input[_builtins.str]
    role_type: pulumi.Input[RosettaNetPipRoleType]
    service: pulumi.Input[_builtins.str]
    service_classification: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class RosettaNetPipRoleSettingsArgs:
    def __init__(__self__, *, action: pulumi.Input[_builtins.str], business_document: pulumi.Input[RosettaNetPipBusinessDocumentArgs], role: pulumi.Input[_builtins.str], role_type: pulumi.Input[RosettaNetPipRoleType], service: pulumi.Input[_builtins.str], service_classification: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action.setter
    def action(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessDocument")
    def business_document(self) -> pulumi.Input[RosettaNetPipBusinessDocumentArgs]:
        
        ...
    
    @business_document.setter
    def business_document(self, value: pulumi.Input[RosettaNetPipBusinessDocumentArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @role.setter
    def role(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="roleType")
    def role_type(self) -> pulumi.Input[RosettaNetPipRoleType]:
        
        ...
    
    @role_type.setter
    def role_type(self, value: pulumi.Input[RosettaNetPipRoleType]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceClassification")
    def service_classification(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_classification.setter
    def service_classification(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkflowParameterArgsDict(TypedDict):
    
    description: NotRequired[pulumi.Input[_builtins.str]]
    metadata: NotRequired[Any]
    type: NotRequired[pulumi.Input[Union[_builtins.str, ParameterType]]]
    value: NotRequired[Any]


@pulumi.input_type
class WorkflowParameterArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., metadata: Optional[Any] = ..., type: Optional[pulumi.Input[Union[_builtins.str, ParameterType]]] = ..., value: Optional[Any] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[Any]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[_builtins.str, ParameterType]]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[_builtins.str, ParameterType]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[Any]): # -> None:
        ...
    


class WorkflowTriggerRecurrenceArgsDict(TypedDict):
    
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    frequency: NotRequired[pulumi.Input[Union[_builtins.str, RecurrenceFrequency]]]
    interval: NotRequired[pulumi.Input[_builtins.int]]
    schedule: NotRequired[pulumi.Input[RecurrenceScheduleArgsDict]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]
    time_zone: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkflowTriggerRecurrenceArgs:
    def __init__(__self__, *, end_time: Optional[pulumi.Input[_builtins.str]] = ..., frequency: Optional[pulumi.Input[Union[_builtins.str, RecurrenceFrequency]]] = ..., interval: Optional[pulumi.Input[_builtins.int]] = ..., schedule: Optional[pulumi.Input[RecurrenceScheduleArgs]] = ..., start_time: Optional[pulumi.Input[_builtins.str]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[Union[_builtins.str, RecurrenceFrequency]]]:
        
        ...
    
    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[Union[_builtins.str, RecurrenceFrequency]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @interval.setter
    def interval(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[RecurrenceScheduleArgs]]:
        
        ...
    
    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[RecurrenceScheduleArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class X12AcknowledgementSettingsArgsDict(TypedDict):
    
    acknowledgement_control_number_lower_bound: pulumi.Input[_builtins.int]
    acknowledgement_control_number_upper_bound: pulumi.Input[_builtins.int]
    batch_functional_acknowledgements: pulumi.Input[_builtins.bool]
    batch_implementation_acknowledgements: pulumi.Input[_builtins.bool]
    batch_technical_acknowledgements: pulumi.Input[_builtins.bool]
    need_functional_acknowledgement: pulumi.Input[_builtins.bool]
    need_implementation_acknowledgement: pulumi.Input[_builtins.bool]
    need_loop_for_valid_messages: pulumi.Input[_builtins.bool]
    need_technical_acknowledgement: pulumi.Input[_builtins.bool]
    rollover_acknowledgement_control_number: pulumi.Input[_builtins.bool]
    send_synchronous_acknowledgement: pulumi.Input[_builtins.bool]
    acknowledgement_control_number_prefix: NotRequired[pulumi.Input[_builtins.str]]
    acknowledgement_control_number_suffix: NotRequired[pulumi.Input[_builtins.str]]
    functional_acknowledgement_version: NotRequired[pulumi.Input[_builtins.str]]
    implementation_acknowledgement_version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class X12AcknowledgementSettingsArgs:
    def __init__(__self__, *, acknowledgement_control_number_lower_bound: pulumi.Input[_builtins.int], acknowledgement_control_number_upper_bound: pulumi.Input[_builtins.int], batch_functional_acknowledgements: pulumi.Input[_builtins.bool], batch_implementation_acknowledgements: pulumi.Input[_builtins.bool], batch_technical_acknowledgements: pulumi.Input[_builtins.bool], need_functional_acknowledgement: pulumi.Input[_builtins.bool], need_implementation_acknowledgement: pulumi.Input[_builtins.bool], need_loop_for_valid_messages: pulumi.Input[_builtins.bool], need_technical_acknowledgement: pulumi.Input[_builtins.bool], rollover_acknowledgement_control_number: pulumi.Input[_builtins.bool], send_synchronous_acknowledgement: pulumi.Input[_builtins.bool], acknowledgement_control_number_prefix: Optional[pulumi.Input[_builtins.str]] = ..., acknowledgement_control_number_suffix: Optional[pulumi.Input[_builtins.str]] = ..., functional_acknowledgement_version: Optional[pulumi.Input[_builtins.str]] = ..., implementation_acknowledgement_version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementControlNumberLowerBound")
    def acknowledgement_control_number_lower_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @acknowledgement_control_number_lower_bound.setter
    def acknowledgement_control_number_lower_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementControlNumberUpperBound")
    def acknowledgement_control_number_upper_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @acknowledgement_control_number_upper_bound.setter
    def acknowledgement_control_number_upper_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchFunctionalAcknowledgements")
    def batch_functional_acknowledgements(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @batch_functional_acknowledgements.setter
    def batch_functional_acknowledgements(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchImplementationAcknowledgements")
    def batch_implementation_acknowledgements(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @batch_implementation_acknowledgements.setter
    def batch_implementation_acknowledgements(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="batchTechnicalAcknowledgements")
    def batch_technical_acknowledgements(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @batch_technical_acknowledgements.setter
    def batch_technical_acknowledgements(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="needFunctionalAcknowledgement")
    def need_functional_acknowledgement(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @need_functional_acknowledgement.setter
    def need_functional_acknowledgement(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="needImplementationAcknowledgement")
    def need_implementation_acknowledgement(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @need_implementation_acknowledgement.setter
    def need_implementation_acknowledgement(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="needLoopForValidMessages")
    def need_loop_for_valid_messages(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @need_loop_for_valid_messages.setter
    def need_loop_for_valid_messages(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="needTechnicalAcknowledgement")
    def need_technical_acknowledgement(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @need_technical_acknowledgement.setter
    def need_technical_acknowledgement(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloverAcknowledgementControlNumber")
    def rollover_acknowledgement_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @rollover_acknowledgement_control_number.setter
    def rollover_acknowledgement_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendSynchronousAcknowledgement")
    def send_synchronous_acknowledgement(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @send_synchronous_acknowledgement.setter
    def send_synchronous_acknowledgement(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementControlNumberPrefix")
    def acknowledgement_control_number_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acknowledgement_control_number_prefix.setter
    def acknowledgement_control_number_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementControlNumberSuffix")
    def acknowledgement_control_number_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @acknowledgement_control_number_suffix.setter
    def acknowledgement_control_number_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionalAcknowledgementVersion")
    def functional_acknowledgement_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @functional_acknowledgement_version.setter
    def functional_acknowledgement_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="implementationAcknowledgementVersion")
    def implementation_acknowledgement_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @implementation_acknowledgement_version.setter
    def implementation_acknowledgement_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class X12AgreementContentArgsDict(TypedDict):
    
    receive_agreement: pulumi.Input[X12OneWayAgreementArgsDict]
    send_agreement: pulumi.Input[X12OneWayAgreementArgsDict]


@pulumi.input_type
class X12AgreementContentArgs:
    def __init__(__self__, *, receive_agreement: pulumi.Input[X12OneWayAgreementArgs], send_agreement: pulumi.Input[X12OneWayAgreementArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiveAgreement")
    def receive_agreement(self) -> pulumi.Input[X12OneWayAgreementArgs]:
        
        ...
    
    @receive_agreement.setter
    def receive_agreement(self, value: pulumi.Input[X12OneWayAgreementArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sendAgreement")
    def send_agreement(self) -> pulumi.Input[X12OneWayAgreementArgs]:
        
        ...
    
    @send_agreement.setter
    def send_agreement(self, value: pulumi.Input[X12OneWayAgreementArgs]): # -> None:
        ...
    


class X12DelimiterOverridesArgsDict(TypedDict):
    
    component_separator: pulumi.Input[_builtins.int]
    data_element_separator: pulumi.Input[_builtins.int]
    replace_character: pulumi.Input[_builtins.int]
    replace_separators_in_payload: pulumi.Input[_builtins.bool]
    segment_terminator: pulumi.Input[_builtins.int]
    segment_terminator_suffix: pulumi.Input[SegmentTerminatorSuffix]
    message_id: NotRequired[pulumi.Input[_builtins.str]]
    protocol_version: NotRequired[pulumi.Input[_builtins.str]]
    target_namespace: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class X12DelimiterOverridesArgs:
    def __init__(__self__, *, component_separator: pulumi.Input[_builtins.int], data_element_separator: pulumi.Input[_builtins.int], replace_character: pulumi.Input[_builtins.int], replace_separators_in_payload: pulumi.Input[_builtins.bool], segment_terminator: pulumi.Input[_builtins.int], segment_terminator_suffix: pulumi.Input[SegmentTerminatorSuffix], message_id: Optional[pulumi.Input[_builtins.str]] = ..., protocol_version: Optional[pulumi.Input[_builtins.str]] = ..., target_namespace: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentSeparator")
    def component_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @component_separator.setter
    def component_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataElementSeparator")
    def data_element_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @data_element_separator.setter
    def data_element_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceCharacter")
    def replace_character(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @replace_character.setter
    def replace_character(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceSeparatorsInPayload")
    def replace_separators_in_payload(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @replace_separators_in_payload.setter
    def replace_separators_in_payload(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentTerminator")
    def segment_terminator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @segment_terminator.setter
    def segment_terminator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentTerminatorSuffix")
    def segment_terminator_suffix(self) -> pulumi.Input[SegmentTerminatorSuffix]:
        
        ...
    
    @segment_terminator_suffix.setter
    def segment_terminator_suffix(self, value: pulumi.Input[SegmentTerminatorSuffix]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @protocol_version.setter
    def protocol_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_namespace.setter
    def target_namespace(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class X12EnvelopeOverrideArgsDict(TypedDict):
    
    date_format: pulumi.Input[Union[_builtins.str, X12DateFormat]]
    header_version: pulumi.Input[_builtins.str]
    message_id: pulumi.Input[_builtins.str]
    protocol_version: pulumi.Input[_builtins.str]
    receiver_application_id: pulumi.Input[_builtins.str]
    responsible_agency_code: pulumi.Input[_builtins.str]
    sender_application_id: pulumi.Input[_builtins.str]
    target_namespace: pulumi.Input[_builtins.str]
    time_format: pulumi.Input[Union[_builtins.str, X12TimeFormat]]
    functional_identifier_code: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class X12EnvelopeOverrideArgs:
    def __init__(__self__, *, date_format: pulumi.Input[Union[_builtins.str, X12DateFormat]], header_version: pulumi.Input[_builtins.str], message_id: pulumi.Input[_builtins.str], protocol_version: pulumi.Input[_builtins.str], receiver_application_id: pulumi.Input[_builtins.str], responsible_agency_code: pulumi.Input[_builtins.str], sender_application_id: pulumi.Input[_builtins.str], target_namespace: pulumi.Input[_builtins.str], time_format: pulumi.Input[Union[_builtins.str, X12TimeFormat]], functional_identifier_code: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dateFormat")
    def date_format(self) -> pulumi.Input[Union[_builtins.str, X12DateFormat]]:
        
        ...
    
    @date_format.setter
    def date_format(self, value: pulumi.Input[Union[_builtins.str, X12DateFormat]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="headerVersion")
    def header_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @header_version.setter
    def header_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolVersion")
    def protocol_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @protocol_version.setter
    def protocol_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverApplicationId")
    def receiver_application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @receiver_application_id.setter
    def receiver_application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="responsibleAgencyCode")
    def responsible_agency_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @responsible_agency_code.setter
    def responsible_agency_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderApplicationId")
    def sender_application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sender_application_id.setter
    def sender_application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @target_namespace.setter
    def target_namespace(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeFormat")
    def time_format(self) -> pulumi.Input[Union[_builtins.str, X12TimeFormat]]:
        
        ...
    
    @time_format.setter
    def time_format(self, value: pulumi.Input[Union[_builtins.str, X12TimeFormat]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionalIdentifierCode")
    def functional_identifier_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @functional_identifier_code.setter
    def functional_identifier_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class X12EnvelopeSettingsArgsDict(TypedDict):
    
    control_standards_id: pulumi.Input[_builtins.int]
    control_version_number: pulumi.Input[_builtins.str]
    enable_default_group_headers: pulumi.Input[_builtins.bool]
    group_control_number_lower_bound: pulumi.Input[_builtins.int]
    group_control_number_upper_bound: pulumi.Input[_builtins.int]
    group_header_agency_code: pulumi.Input[_builtins.str]
    group_header_date_format: pulumi.Input[Union[_builtins.str, X12DateFormat]]
    group_header_time_format: pulumi.Input[Union[_builtins.str, X12TimeFormat]]
    group_header_version: pulumi.Input[_builtins.str]
    interchange_control_number_lower_bound: pulumi.Input[_builtins.int]
    interchange_control_number_upper_bound: pulumi.Input[_builtins.int]
    overwrite_existing_transaction_set_control_number: pulumi.Input[_builtins.bool]
    receiver_application_id: pulumi.Input[_builtins.str]
    rollover_group_control_number: pulumi.Input[_builtins.bool]
    rollover_interchange_control_number: pulumi.Input[_builtins.bool]
    rollover_transaction_set_control_number: pulumi.Input[_builtins.bool]
    sender_application_id: pulumi.Input[_builtins.str]
    transaction_set_control_number_lower_bound: pulumi.Input[_builtins.int]
    transaction_set_control_number_upper_bound: pulumi.Input[_builtins.int]
    usage_indicator: pulumi.Input[Union[_builtins.str, UsageIndicator]]
    use_control_standards_id_as_repetition_character: pulumi.Input[_builtins.bool]
    functional_group_id: NotRequired[pulumi.Input[_builtins.str]]
    transaction_set_control_number_prefix: NotRequired[pulumi.Input[_builtins.str]]
    transaction_set_control_number_suffix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class X12EnvelopeSettingsArgs:
    def __init__(__self__, *, control_standards_id: pulumi.Input[_builtins.int], control_version_number: pulumi.Input[_builtins.str], enable_default_group_headers: pulumi.Input[_builtins.bool], group_control_number_lower_bound: pulumi.Input[_builtins.int], group_control_number_upper_bound: pulumi.Input[_builtins.int], group_header_agency_code: pulumi.Input[_builtins.str], group_header_date_format: pulumi.Input[Union[_builtins.str, X12DateFormat]], group_header_time_format: pulumi.Input[Union[_builtins.str, X12TimeFormat]], group_header_version: pulumi.Input[_builtins.str], interchange_control_number_lower_bound: pulumi.Input[_builtins.int], interchange_control_number_upper_bound: pulumi.Input[_builtins.int], overwrite_existing_transaction_set_control_number: pulumi.Input[_builtins.bool], receiver_application_id: pulumi.Input[_builtins.str], rollover_group_control_number: pulumi.Input[_builtins.bool], rollover_interchange_control_number: pulumi.Input[_builtins.bool], rollover_transaction_set_control_number: pulumi.Input[_builtins.bool], sender_application_id: pulumi.Input[_builtins.str], transaction_set_control_number_lower_bound: pulumi.Input[_builtins.int], transaction_set_control_number_upper_bound: pulumi.Input[_builtins.int], usage_indicator: pulumi.Input[Union[_builtins.str, UsageIndicator]], use_control_standards_id_as_repetition_character: pulumi.Input[_builtins.bool], functional_group_id: Optional[pulumi.Input[_builtins.str]] = ..., transaction_set_control_number_prefix: Optional[pulumi.Input[_builtins.str]] = ..., transaction_set_control_number_suffix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlStandardsId")
    def control_standards_id(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @control_standards_id.setter
    def control_standards_id(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlVersionNumber")
    def control_version_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @control_version_number.setter
    def control_version_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableDefaultGroupHeaders")
    def enable_default_group_headers(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_default_group_headers.setter
    def enable_default_group_headers(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupControlNumberLowerBound")
    def group_control_number_lower_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @group_control_number_lower_bound.setter
    def group_control_number_lower_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupControlNumberUpperBound")
    def group_control_number_upper_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @group_control_number_upper_bound.setter
    def group_control_number_upper_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupHeaderAgencyCode")
    def group_header_agency_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_header_agency_code.setter
    def group_header_agency_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupHeaderDateFormat")
    def group_header_date_format(self) -> pulumi.Input[Union[_builtins.str, X12DateFormat]]:
        
        ...
    
    @group_header_date_format.setter
    def group_header_date_format(self, value: pulumi.Input[Union[_builtins.str, X12DateFormat]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupHeaderTimeFormat")
    def group_header_time_format(self) -> pulumi.Input[Union[_builtins.str, X12TimeFormat]]:
        
        ...
    
    @group_header_time_format.setter
    def group_header_time_format(self, value: pulumi.Input[Union[_builtins.str, X12TimeFormat]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupHeaderVersion")
    def group_header_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @group_header_version.setter
    def group_header_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interchangeControlNumberLowerBound")
    def interchange_control_number_lower_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @interchange_control_number_lower_bound.setter
    def interchange_control_number_lower_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interchangeControlNumberUpperBound")
    def interchange_control_number_upper_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @interchange_control_number_upper_bound.setter
    def interchange_control_number_upper_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="overwriteExistingTransactionSetControlNumber")
    def overwrite_existing_transaction_set_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @overwrite_existing_transaction_set_control_number.setter
    def overwrite_existing_transaction_set_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverApplicationId")
    def receiver_application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @receiver_application_id.setter
    def receiver_application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloverGroupControlNumber")
    def rollover_group_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @rollover_group_control_number.setter
    def rollover_group_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloverInterchangeControlNumber")
    def rollover_interchange_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @rollover_interchange_control_number.setter
    def rollover_interchange_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="rolloverTransactionSetControlNumber")
    def rollover_transaction_set_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @rollover_transaction_set_control_number.setter
    def rollover_transaction_set_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderApplicationId")
    def sender_application_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @sender_application_id.setter
    def sender_application_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionSetControlNumberLowerBound")
    def transaction_set_control_number_lower_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @transaction_set_control_number_lower_bound.setter
    def transaction_set_control_number_lower_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionSetControlNumberUpperBound")
    def transaction_set_control_number_upper_bound(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @transaction_set_control_number_upper_bound.setter
    def transaction_set_control_number_upper_bound(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="usageIndicator")
    def usage_indicator(self) -> pulumi.Input[Union[_builtins.str, UsageIndicator]]:
        
        ...
    
    @usage_indicator.setter
    def usage_indicator(self, value: pulumi.Input[Union[_builtins.str, UsageIndicator]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useControlStandardsIdAsRepetitionCharacter")
    def use_control_standards_id_as_repetition_character(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @use_control_standards_id_as_repetition_character.setter
    def use_control_standards_id_as_repetition_character(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionalGroupId")
    def functional_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @functional_group_id.setter
    def functional_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionSetControlNumberPrefix")
    def transaction_set_control_number_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transaction_set_control_number_prefix.setter
    def transaction_set_control_number_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transactionSetControlNumberSuffix")
    def transaction_set_control_number_suffix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @transaction_set_control_number_suffix.setter
    def transaction_set_control_number_suffix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class X12FramingSettingsArgsDict(TypedDict):
    
    character_set: pulumi.Input[Union[_builtins.str, X12CharacterSet]]
    component_separator: pulumi.Input[_builtins.int]
    data_element_separator: pulumi.Input[_builtins.int]
    replace_character: pulumi.Input[_builtins.int]
    replace_separators_in_payload: pulumi.Input[_builtins.bool]
    segment_terminator: pulumi.Input[_builtins.int]
    segment_terminator_suffix: pulumi.Input[SegmentTerminatorSuffix]


@pulumi.input_type
class X12FramingSettingsArgs:
    def __init__(__self__, *, character_set: pulumi.Input[Union[_builtins.str, X12CharacterSet]], component_separator: pulumi.Input[_builtins.int], data_element_separator: pulumi.Input[_builtins.int], replace_character: pulumi.Input[_builtins.int], replace_separators_in_payload: pulumi.Input[_builtins.bool], segment_terminator: pulumi.Input[_builtins.int], segment_terminator_suffix: pulumi.Input[SegmentTerminatorSuffix]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="characterSet")
    def character_set(self) -> pulumi.Input[Union[_builtins.str, X12CharacterSet]]:
        
        ...
    
    @character_set.setter
    def character_set(self, value: pulumi.Input[Union[_builtins.str, X12CharacterSet]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="componentSeparator")
    def component_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @component_separator.setter
    def component_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataElementSeparator")
    def data_element_separator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @data_element_separator.setter
    def data_element_separator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceCharacter")
    def replace_character(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @replace_character.setter
    def replace_character(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="replaceSeparatorsInPayload")
    def replace_separators_in_payload(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @replace_separators_in_payload.setter
    def replace_separators_in_payload(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentTerminator")
    def segment_terminator(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @segment_terminator.setter
    def segment_terminator(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="segmentTerminatorSuffix")
    def segment_terminator_suffix(self) -> pulumi.Input[SegmentTerminatorSuffix]:
        
        ...
    
    @segment_terminator_suffix.setter
    def segment_terminator_suffix(self, value: pulumi.Input[SegmentTerminatorSuffix]): # -> None:
        ...
    


class X12MessageFilterArgsDict(TypedDict):
    
    message_filter_type: pulumi.Input[Union[_builtins.str, MessageFilterType]]


@pulumi.input_type
class X12MessageFilterArgs:
    def __init__(__self__, *, message_filter_type: pulumi.Input[Union[_builtins.str, MessageFilterType]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFilterType")
    def message_filter_type(self) -> pulumi.Input[Union[_builtins.str, MessageFilterType]]:
        
        ...
    
    @message_filter_type.setter
    def message_filter_type(self, value: pulumi.Input[Union[_builtins.str, MessageFilterType]]): # -> None:
        ...
    


class X12MessageIdentifierArgsDict(TypedDict):
    
    message_id: pulumi.Input[_builtins.str]


@pulumi.input_type
class X12MessageIdentifierArgs:
    def __init__(__self__, *, message_id: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class X12OneWayAgreementArgsDict(TypedDict):
    
    protocol_settings: pulumi.Input[X12ProtocolSettingsArgsDict]
    receiver_business_identity: pulumi.Input[BusinessIdentityArgsDict]
    sender_business_identity: pulumi.Input[BusinessIdentityArgsDict]


@pulumi.input_type
class X12OneWayAgreementArgs:
    def __init__(__self__, *, protocol_settings: pulumi.Input[X12ProtocolSettingsArgs], receiver_business_identity: pulumi.Input[BusinessIdentityArgs], sender_business_identity: pulumi.Input[BusinessIdentityArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="protocolSettings")
    def protocol_settings(self) -> pulumi.Input[X12ProtocolSettingsArgs]:
        
        ...
    
    @protocol_settings.setter
    def protocol_settings(self, value: pulumi.Input[X12ProtocolSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="receiverBusinessIdentity")
    def receiver_business_identity(self) -> pulumi.Input[BusinessIdentityArgs]:
        
        ...
    
    @receiver_business_identity.setter
    def receiver_business_identity(self, value: pulumi.Input[BusinessIdentityArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderBusinessIdentity")
    def sender_business_identity(self) -> pulumi.Input[BusinessIdentityArgs]:
        
        ...
    
    @sender_business_identity.setter
    def sender_business_identity(self, value: pulumi.Input[BusinessIdentityArgs]): # -> None:
        ...
    


class X12ProcessingSettingsArgsDict(TypedDict):
    
    convert_implied_decimal: pulumi.Input[_builtins.bool]
    create_empty_xml_tags_for_trailing_separators: pulumi.Input[_builtins.bool]
    mask_security_info: pulumi.Input[_builtins.bool]
    preserve_interchange: pulumi.Input[_builtins.bool]
    suspend_interchange_on_error: pulumi.Input[_builtins.bool]
    use_dot_as_decimal_separator: pulumi.Input[_builtins.bool]


@pulumi.input_type
class X12ProcessingSettingsArgs:
    def __init__(__self__, *, convert_implied_decimal: pulumi.Input[_builtins.bool], create_empty_xml_tags_for_trailing_separators: pulumi.Input[_builtins.bool], mask_security_info: pulumi.Input[_builtins.bool], preserve_interchange: pulumi.Input[_builtins.bool], suspend_interchange_on_error: pulumi.Input[_builtins.bool], use_dot_as_decimal_separator: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="convertImpliedDecimal")
    def convert_implied_decimal(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @convert_implied_decimal.setter
    def convert_implied_decimal(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createEmptyXmlTagsForTrailingSeparators")
    def create_empty_xml_tags_for_trailing_separators(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @create_empty_xml_tags_for_trailing_separators.setter
    def create_empty_xml_tags_for_trailing_separators(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maskSecurityInfo")
    def mask_security_info(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @mask_security_info.setter
    def mask_security_info(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preserveInterchange")
    def preserve_interchange(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @preserve_interchange.setter
    def preserve_interchange(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suspendInterchangeOnError")
    def suspend_interchange_on_error(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @suspend_interchange_on_error.setter
    def suspend_interchange_on_error(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useDotAsDecimalSeparator")
    def use_dot_as_decimal_separator(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @use_dot_as_decimal_separator.setter
    def use_dot_as_decimal_separator(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class X12ProtocolSettingsArgsDict(TypedDict):
    
    acknowledgement_settings: pulumi.Input[X12AcknowledgementSettingsArgsDict]
    envelope_settings: pulumi.Input[X12EnvelopeSettingsArgsDict]
    framing_settings: pulumi.Input[X12FramingSettingsArgsDict]
    message_filter: pulumi.Input[X12MessageFilterArgsDict]
    processing_settings: pulumi.Input[X12ProcessingSettingsArgsDict]
    schema_references: pulumi.Input[Sequence[pulumi.Input[X12SchemaReferenceArgsDict]]]
    security_settings: pulumi.Input[X12SecuritySettingsArgsDict]
    validation_settings: pulumi.Input[X12ValidationSettingsArgsDict]
    envelope_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[X12EnvelopeOverrideArgsDict]]]]
    message_filter_list: NotRequired[pulumi.Input[Sequence[pulumi.Input[X12MessageIdentifierArgsDict]]]]
    validation_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[X12ValidationOverrideArgsDict]]]]
    x12_delimiter_overrides: NotRequired[pulumi.Input[Sequence[pulumi.Input[X12DelimiterOverridesArgsDict]]]]


@pulumi.input_type
class X12ProtocolSettingsArgs:
    def __init__(__self__, *, acknowledgement_settings: pulumi.Input[X12AcknowledgementSettingsArgs], envelope_settings: pulumi.Input[X12EnvelopeSettingsArgs], framing_settings: pulumi.Input[X12FramingSettingsArgs], message_filter: pulumi.Input[X12MessageFilterArgs], processing_settings: pulumi.Input[X12ProcessingSettingsArgs], schema_references: pulumi.Input[Sequence[pulumi.Input[X12SchemaReferenceArgs]]], security_settings: pulumi.Input[X12SecuritySettingsArgs], validation_settings: pulumi.Input[X12ValidationSettingsArgs], envelope_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[X12EnvelopeOverrideArgs]]]] = ..., message_filter_list: Optional[pulumi.Input[Sequence[pulumi.Input[X12MessageIdentifierArgs]]]] = ..., validation_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[X12ValidationOverrideArgs]]]] = ..., x12_delimiter_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[X12DelimiterOverridesArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acknowledgementSettings")
    def acknowledgement_settings(self) -> pulumi.Input[X12AcknowledgementSettingsArgs]:
        
        ...
    
    @acknowledgement_settings.setter
    def acknowledgement_settings(self, value: pulumi.Input[X12AcknowledgementSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envelopeSettings")
    def envelope_settings(self) -> pulumi.Input[X12EnvelopeSettingsArgs]:
        
        ...
    
    @envelope_settings.setter
    def envelope_settings(self, value: pulumi.Input[X12EnvelopeSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="framingSettings")
    def framing_settings(self) -> pulumi.Input[X12FramingSettingsArgs]:
        
        ...
    
    @framing_settings.setter
    def framing_settings(self, value: pulumi.Input[X12FramingSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFilter")
    def message_filter(self) -> pulumi.Input[X12MessageFilterArgs]:
        
        ...
    
    @message_filter.setter
    def message_filter(self, value: pulumi.Input[X12MessageFilterArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingSettings")
    def processing_settings(self) -> pulumi.Input[X12ProcessingSettingsArgs]:
        
        ...
    
    @processing_settings.setter
    def processing_settings(self, value: pulumi.Input[X12ProcessingSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaReferences")
    def schema_references(self) -> pulumi.Input[Sequence[pulumi.Input[X12SchemaReferenceArgs]]]:
        
        ...
    
    @schema_references.setter
    def schema_references(self, value: pulumi.Input[Sequence[pulumi.Input[X12SchemaReferenceArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> pulumi.Input[X12SecuritySettingsArgs]:
        
        ...
    
    @security_settings.setter
    def security_settings(self, value: pulumi.Input[X12SecuritySettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationSettings")
    def validation_settings(self) -> pulumi.Input[X12ValidationSettingsArgs]:
        
        ...
    
    @validation_settings.setter
    def validation_settings(self, value: pulumi.Input[X12ValidationSettingsArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="envelopeOverrides")
    def envelope_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[X12EnvelopeOverrideArgs]]]]:
        
        ...
    
    @envelope_overrides.setter
    def envelope_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[X12EnvelopeOverrideArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFilterList")
    def message_filter_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[X12MessageIdentifierArgs]]]]:
        
        ...
    
    @message_filter_list.setter
    def message_filter_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[X12MessageIdentifierArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validationOverrides")
    def validation_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[X12ValidationOverrideArgs]]]]:
        
        ...
    
    @validation_overrides.setter
    def validation_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[X12ValidationOverrideArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="x12DelimiterOverrides")
    def x12_delimiter_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[X12DelimiterOverridesArgs]]]]:
        
        ...
    
    @x12_delimiter_overrides.setter
    def x12_delimiter_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[X12DelimiterOverridesArgs]]]]): # -> None:
        ...
    


class X12SchemaReferenceArgsDict(TypedDict):
    
    message_id: pulumi.Input[_builtins.str]
    schema_name: pulumi.Input[_builtins.str]
    schema_version: pulumi.Input[_builtins.str]
    sender_application_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class X12SchemaReferenceArgs:
    def __init__(__self__, *, message_id: pulumi.Input[_builtins.str], schema_name: pulumi.Input[_builtins.str], schema_version: pulumi.Input[_builtins.str], sender_application_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schema_name.setter
    def schema_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @schema_version.setter
    def schema_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="senderApplicationId")
    def sender_application_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sender_application_id.setter
    def sender_application_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class X12SecuritySettingsArgsDict(TypedDict):
    
    authorization_qualifier: pulumi.Input[_builtins.str]
    security_qualifier: pulumi.Input[_builtins.str]
    authorization_value: NotRequired[pulumi.Input[_builtins.str]]
    password_value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class X12SecuritySettingsArgs:
    def __init__(__self__, *, authorization_qualifier: pulumi.Input[_builtins.str], security_qualifier: pulumi.Input[_builtins.str], authorization_value: Optional[pulumi.Input[_builtins.str]] = ..., password_value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationQualifier")
    def authorization_qualifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authorization_qualifier.setter
    def authorization_qualifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityQualifier")
    def security_qualifier(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @security_qualifier.setter
    def security_qualifier(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorizationValue")
    def authorization_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authorization_value.setter
    def authorization_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="passwordValue")
    def password_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password_value.setter
    def password_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class X12ValidationOverrideArgsDict(TypedDict):
    
    allow_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool]
    message_id: pulumi.Input[_builtins.str]
    trailing_separator_policy: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]
    trim_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool]
    validate_character_set: pulumi.Input[_builtins.bool]
    validate_edi_types: pulumi.Input[_builtins.bool]
    validate_xsd_types: pulumi.Input[_builtins.bool]


@pulumi.input_type
class X12ValidationOverrideArgs:
    def __init__(__self__, *, allow_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool], message_id: pulumi.Input[_builtins.str], trailing_separator_policy: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]], trim_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool], validate_character_set: pulumi.Input[_builtins.bool], validate_edi_types: pulumi.Input[_builtins.bool], validate_xsd_types: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowLeadingAndTrailingSpacesAndZeroes")
    def allow_leading_and_trailing_spaces_and_zeroes(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @allow_leading_and_trailing_spaces_and_zeroes.setter
    def allow_leading_and_trailing_spaces_and_zeroes(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageId")
    def message_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @message_id.setter
    def message_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trailingSeparatorPolicy")
    def trailing_separator_policy(self) -> pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]:
        
        ...
    
    @trailing_separator_policy.setter
    def trailing_separator_policy(self, value: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trimLeadingAndTrailingSpacesAndZeroes")
    def trim_leading_and_trailing_spaces_and_zeroes(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @trim_leading_and_trailing_spaces_and_zeroes.setter
    def trim_leading_and_trailing_spaces_and_zeroes(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateCharacterSet")
    def validate_character_set(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_character_set.setter
    def validate_character_set(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateEDITypes")
    def validate_edi_types(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_edi_types.setter
    def validate_edi_types(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateXSDTypes")
    def validate_xsd_types(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_xsd_types.setter
    def validate_xsd_types(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class X12ValidationSettingsArgsDict(TypedDict):
    
    allow_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool]
    check_duplicate_group_control_number: pulumi.Input[_builtins.bool]
    check_duplicate_interchange_control_number: pulumi.Input[_builtins.bool]
    check_duplicate_transaction_set_control_number: pulumi.Input[_builtins.bool]
    interchange_control_number_validity_days: pulumi.Input[_builtins.int]
    trailing_separator_policy: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]
    trim_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool]
    validate_character_set: pulumi.Input[_builtins.bool]
    validate_edi_types: pulumi.Input[_builtins.bool]
    validate_xsd_types: pulumi.Input[_builtins.bool]


@pulumi.input_type
class X12ValidationSettingsArgs:
    def __init__(__self__, *, allow_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool], check_duplicate_group_control_number: pulumi.Input[_builtins.bool], check_duplicate_interchange_control_number: pulumi.Input[_builtins.bool], check_duplicate_transaction_set_control_number: pulumi.Input[_builtins.bool], interchange_control_number_validity_days: pulumi.Input[_builtins.int], trailing_separator_policy: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]], trim_leading_and_trailing_spaces_and_zeroes: pulumi.Input[_builtins.bool], validate_character_set: pulumi.Input[_builtins.bool], validate_edi_types: pulumi.Input[_builtins.bool], validate_xsd_types: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowLeadingAndTrailingSpacesAndZeroes")
    def allow_leading_and_trailing_spaces_and_zeroes(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @allow_leading_and_trailing_spaces_and_zeroes.setter
    def allow_leading_and_trailing_spaces_and_zeroes(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkDuplicateGroupControlNumber")
    def check_duplicate_group_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @check_duplicate_group_control_number.setter
    def check_duplicate_group_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkDuplicateInterchangeControlNumber")
    def check_duplicate_interchange_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @check_duplicate_interchange_control_number.setter
    def check_duplicate_interchange_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkDuplicateTransactionSetControlNumber")
    def check_duplicate_transaction_set_control_number(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @check_duplicate_transaction_set_control_number.setter
    def check_duplicate_transaction_set_control_number(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interchangeControlNumberValidityDays")
    def interchange_control_number_validity_days(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @interchange_control_number_validity_days.setter
    def interchange_control_number_validity_days(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trailingSeparatorPolicy")
    def trailing_separator_policy(self) -> pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]:
        
        ...
    
    @trailing_separator_policy.setter
    def trailing_separator_policy(self, value: pulumi.Input[Union[_builtins.str, TrailingSeparatorPolicy]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trimLeadingAndTrailingSpacesAndZeroes")
    def trim_leading_and_trailing_spaces_and_zeroes(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @trim_leading_and_trailing_spaces_and_zeroes.setter
    def trim_leading_and_trailing_spaces_and_zeroes(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateCharacterSet")
    def validate_character_set(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_character_set.setter
    def validate_character_set(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateEDITypes")
    def validate_edi_types(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_edi_types.setter
    def validate_edi_types(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="validateXSDTypes")
    def validate_xsd_types(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @validate_xsd_types.setter
    def validate_xsd_types(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


